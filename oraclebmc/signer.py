import base64
import email.utils
import hashlib
import io
import os

import httpsig_cffi.sign
import httpsig_cffi.utils
import requests.auth
import six

from .exceptions import InvalidPrivateKey

from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hmac, serialization


def load_private_key(secret, pass_phrase=None):
    """Loads a private key that may use a pass_phrase.

    Tries to correct or diagnose common errors:

    - provided pass_phrase but didn't need one
    - provided a public key
    """
    if isinstance(secret, six.string_types):
        secret = secret.encode("ascii")
    # CHANGED: added str -> bytes for new param
    if isinstance(pass_phrase, six.string_types):
        pass_phrase = pass_phrase.encode("ascii")

    backend = default_backend()

    try:
        # 0) Try with pass_phrase
        return serialization.load_pem_private_key(secret, pass_phrase, backend=backend)
    except TypeError:
        # 1) Either:
        #    - key has pass_phrase and one wasn't provided
        #    - key doesn't have pass_phrase and one was provided.
        #
        #    Can't fix the first, but we *can* fix the second.
        #    This can happen if the DEFAULT profile has a pass_phrase but
        #    another profile uses a key file without a pass_phrase.
        if pass_phrase is None:
            # 1.1) private key needed a pass_phrase and we don't have one
            raise InvalidPrivateKey("Private key requires a pass_phrase.")
        else:
            # 1.2) try again without pass_phrase; could be an artifact from DEFAULT
            return serialization.load_pem_private_key(secret, None, backend=backend)
    except ValueError:
        # 2) Try to determine what kind of failure this is.
        #    Most likely, this is either a bad password or a public key.
        #    If loading it as a public key fails, it's almost certainly a bad password.
        for loader in [
            serialization.load_der_public_key,
            serialization.load_pem_public_key,
            serialization.load_ssh_public_key
        ]:
            try:
                loader(secret, backend=backend)
            except (ValueError, UnsupportedAlgorithm):
                # 2.1) Not a public key; try the next format
                pass
            else:
                # 2.2) This is a public key
                raise InvalidPrivateKey("Authentication requires a private key, but a public key was provided.")
        # 2.3) Password is probably wrong.
        raise InvalidPrivateKey("Private key is malformed or the pass_phrase is incorrect.")


def inject_missing_headers(request, sign_body, enforce_content_headers):
    # Inject date, host, and content-type if missing
    request.headers.setdefault(
        "date", email.utils.formatdate(usegmt=True))

    request.headers.setdefault(
        "host", six.moves.urllib.parse.urlparse(request.url).netloc)

    if enforce_content_headers:
        request.headers.setdefault("content-type", "application/json")

        # Requests with a body need to send content-type,
        # content-length, and x-content-sha256
        if sign_body:
            # TODO: does not handle streaming bodies (files, stdin)
            body = request.body or ""
            try:
                body = body.encode("utf-8")
            except UnicodeDecodeError:
                # PY2 - str is already encoded byte string
                pass
            except AttributeError:
                # PY3 - body was already bytes
                pass
            if "x-content-sha256" not in request.headers:
                m = hashlib.sha256(body)
                base64digest = base64.b64encode(m.digest())
                base64string = base64digest.decode("utf-8")
                request.headers["x-content-sha256"] = base64string
            request.headers.setdefault("content-length", len(body))


# HeaderSigner doesn't support private keys with passwords.
# We have to rewrite the constructor since the base parses the key
# during __init__
class PatchedHeaderSigner(httpsig_cffi.sign.HeaderSigner):
    def __init__(self, key_id, secret, algorithm=None, pass_phrase=None, headers=None):

        # COPIED from Signer.__init__
        if algorithm is None:
            algorithm = "hmac-sha256"

        assert algorithm in httpsig_cffi.utils.ALGORITHMS, "Unknown algorithm"

        self._rsa_public = None
        self._rsa_private = None
        self._hash = None
        self.sign_algorithm, self.hash_algorithm = algorithm.split('-')

        if self.sign_algorithm == 'rsa':
            self._rsahash = httpsig_cffi.utils.HASHES[self.hash_algorithm]
            # CHANGED from Signer.__init__
            # Only loads private key. Signer loaded public keys because it's also used for verification.
            self._rsa_private = load_private_key(secret, pass_phrase=pass_phrase)
            self._rsa_public = self._rsa_private.public_key()

        elif self.sign_algorithm == 'hmac':
            self._hash = hmac.HMAC(
                secret, httpsig_cffi.utils.HASHES[self.hash_algorithm](), backend=default_backend())

        # COPIED from HeaderSigner.__init__
        self.headers = headers or ['date']
        self.signature_template = httpsig_cffi.utils.build_signature_template(key_id, algorithm, headers)


class Signer(requests.auth.AuthBase):
    """A requests auth instance that can be reused across requests"""

    def __init__(self, tenancy, user, fingerprint, private_key_file_location, pass_phrase=None):
        self.api_key = tenancy + "/" + user + "/" + fingerprint
        self.private_key_file_location = os.path.expanduser(private_key_file_location)
        self._private_key = None

        generic_headers = [
            "date",
            "(request-target)",
            "host"
        ]
        body_headers = [
            "content-length",
            "content-type",
            "x-content-sha256",
        ]

        self._basic_signer = PatchedHeaderSigner(
            key_id=self.api_key,
            secret=self.private_key,
            algorithm="rsa-sha256",
            pass_phrase=pass_phrase,
            headers=generic_headers)

        self._body_signer = PatchedHeaderSigner(
            key_id=self.api_key,
            secret=self.private_key,
            algorithm="rsa-sha256",
            pass_phrase=pass_phrase,
            headers=generic_headers + body_headers)

    @property
    def private_key(self):
        # TODO: this should return the private key instance,
        # not the (possibly encrypted) key bytes.
        if self._private_key is None:
            with io.open(self.private_key_file_location, mode="r") as f:
                self._private_key = f.read().strip()
        return self._private_key

    def __call__(self, request, enforce_content_headers=True):
        verb = request.method.lower()
        if verb not in ["get", "head", "delete", "put", "post"]:
            raise ValueError("Don't know how to sign request verb {}".format(verb))

        sign_body = verb in ["put", "post"]
        if sign_body and enforce_content_headers:
            signer = self._body_signer
        else:
            signer = self._basic_signer

        inject_missing_headers(request, sign_body, enforce_content_headers)
        signed_headers = signer.sign(
            request.headers,
            host=six.moves.urllib.parse.urlparse(request.url).netloc,
            method=request.method,
            path=request.path_url)
        request.headers.update(signed_headers)

        return request


class ObjectUploadSigner(requests.auth.AuthBase):
    def __init__(self, signer):
        """Wraps an existing signer and applies options required for object upload.

        :param signer: The signer to be wrapped.
        """
        self.signer = signer

    def __call__(self, request):
        # The requests library sets the Transfer-Encoding header to 'chunked' if the
        # body is a stream with 0 length. Object storage does not currently support this option,
        # and the request will fail if it is not removed. This is the only hook available where we
        # can do this after the header is added and before the request is sent.
        request.headers.pop('Transfer-Encoding', None)

        return self.signer.__call__(request, enforce_content_headers=False)
