# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import base64
import email.utils
import hashlib
import io
import functools
import os

import httpsig_cffi.sign
import httpsig_cffi.utils
import requests.auth
import six

from .exceptions import InvalidPrivateKey, MissingPrivateKeyPassphrase

from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

SIGNATURE_VERSION = "1"


def load_private_key_from_file(filename, pass_phrase=None):
    filename = os.path.expanduser(filename)
    with io.open(filename, mode="rb") as f:
        private_key_data = f.read().strip()
    return load_private_key(private_key_data, pass_phrase)


def load_private_key(secret, pass_phrase):
    """Loads a private key that may use a pass_phrase.

    Tries to correct or diagnose common errors:

    - provided pass_phrase but didn't need one
    - provided a public key
    """
    if isinstance(secret, six.text_type):
        secret = secret.encode("ascii")
    if isinstance(pass_phrase, six.text_type):
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
            raise MissingPrivateKeyPassphrase("The provided key requires a passphrase.")
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
        raise InvalidPrivateKey("The provided key is not a private key, or the provided passphrase is incorrect.")


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
            if isinstance(body, six.string_types):
                body = body.encode("utf-8")
            if "x-content-sha256" not in request.headers:
                m = hashlib.sha256(body)
                base64digest = base64.b64encode(m.digest())
                base64string = base64digest.decode("utf-8")
                request.headers["x-content-sha256"] = base64string
            request.headers.setdefault("content-length", str(len(body)))


# HeaderSigner doesn't support private keys with passwords.
# Patched since the constructor parses the key in __init__
class _PatchedHeaderSigner(httpsig_cffi.sign.HeaderSigner):
    """Internal.  If you need to construct a Signer, use :class:`~.Signer` instead."""
    def __init__(self, key_id, private_key, headers):
        # Dropped general support for the specific signing/hash the SDK uses.
        self.sign_algorithm = "rsa"
        self.hash_algorithm = "sha256"

        self._hash = None
        self._rsahash = httpsig_cffi.utils.HASHES[self.hash_algorithm]

        self._rsa_private = private_key
        self._rsa_public = self._rsa_private.public_key()

        self.headers = headers
        # Base template doesn't include version
        template = 'Signature algorithm="rsa-sha256",headers="{}",keyId="{}",signature="%s",version="{}"'
        self.signature_template = template.format(" ".join(headers), key_id, SIGNATURE_VERSION)


class Signer(requests.auth.AuthBase):
    """A requests auth instance that can be reused across requests.

    You can manually sign calls by creating an instance of the signer, and
    providing it as the ``auth`` argument to Requests functions:

    .. code-block:: python

        import requests
        from oraclebmc import Signer

        auth = Signer(...)
        resp = requests.get("https://...", auth=auth)


    """

    def __init__(self, tenancy, user, fingerprint, private_key_file_location, pass_phrase=None):
        self.api_key = tenancy + "/" + user + "/" + fingerprint
        self.private_key = load_private_key_from_file(private_key_file_location, pass_phrase)

        generic_headers = ["date", "(request-target)", "host"]
        body_headers = ["content-length", "content-type", "x-content-sha256"]

        self._basic_signer = _PatchedHeaderSigner(
            key_id=self.api_key,
            private_key=self.private_key,
            headers=generic_headers)

        self._body_signer = _PatchedHeaderSigner(
            key_id=self.api_key,
            private_key=self.private_key,
            headers=generic_headers + body_headers)

    def __call__(self, request, enforce_content_headers=True):
        verb = request.method.lower()
        if verb not in ["get", "head", "delete", "put", "post"]:
            raise ValueError("Don't know how to sign request verb {}".format(verb))

        sign_body = verb in ["put", "post"]
        if sign_body and enforce_content_headers:
            signer = self._body_signer
        else:
            signer = self._basic_signer
            # The requests library sets the Transfer-Encoding header to 'chunked' if the
            # body is a stream with 0 length. Object storage does not currently support this option,
            # and the request will fail if it is not removed. This is the only hook available where we
            # can do this after the header is added and before the request is sent.
            request.headers.pop('Transfer-Encoding', None)

        inject_missing_headers(request, sign_body, enforce_content_headers)
        signed_headers = signer.sign(
            request.headers,
            host=six.moves.urllib.parse.urlparse(request.url).netloc,
            method=request.method,
            path=request.path_url)
        request.headers.update(signed_headers)

        return request

    @property
    def without_content_headers(self):
        return functools.partial(self, enforce_content_headers=False)
