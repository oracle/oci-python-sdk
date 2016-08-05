import base64
import email.utils
import hashlib

import httpsig.requests_auth
import requests

class Signer(requests.auth.AuthBase):
    """A requests auth instance that can be reused across requests"""

    def __init__(self, tenancy, user, fingerprint, private_key_file_location):
        self.api_key = tenancy + "/" + user + "/" + fingerprint
        self.private_key_file_location = private_key_file_location
        self._private_key = None

        generic_headers = [
            "date",
            "(request-target)"
        ]
        body_headers = [
            "content-length",
            "content-type",
            "x-content-sha256",
        ]

        self._basic_signer = httpsig.sign.HeaderSigner(key_id=self.api_key,
                                                     secret=self.private_key,
                                                     algorithm="rsa-sha256",
                                                     headers=generic_headers)

        self._body_signer = httpsig.sign.HeaderSigner(key_id=self.api_key,
                                                     secret=self.private_key,
                                                     algorithm="rsa-sha256",
                                                     headers=generic_headers + body_headers)

    def inject_missing_headers(self, request, sign_body, enforce_content_headers):
        # Inject date and content-type if missing
        request.headers.setdefault(
            "date", email.utils.formatdate(usegmt=True))

        if enforce_content_headers:
            request.headers.setdefault("content-type", "application/json")

            # Requests with a body need to send content-type,
            # content-length, and x-content-sha256
            if sign_body:
                body = request.body or ""
                if "x-content-sha256" not in request.headers:
                    m = hashlib.sha256(body.encode("utf-8"))
                    base64digest = base64.b64encode(m.digest())
                    base64string = base64digest.decode("utf-8")
                    request.headers["x-content-sha256"] = base64string
                request.headers.setdefault("content-length", len(body))

    @property
    def private_key(self):
        if self._private_key is None:
            with open(self.private_key_file_location) as f:
                self._private_key = f.read().strip()
        return self._private_key

    def __call__(self, request, enforce_content_headers=True):
        verb = request.method.lower()

        if verb not in ["get", "head", "delete", "put", "post"]:
            raise ValueError(
                "Don't know how to sign request verb {}".format(verb))

        sign_body = verb in ["put", "post"]

        if sign_body and enforce_content_headers:
            signer = self._body_signer
        else:
            signer = self._basic_signer

        self.inject_missing_headers(request, sign_body, enforce_content_headers)

        signed_headers = signer.sign(
            request.headers,
            method=request.method,
            path=request.path_url)

        request.headers.update(signed_headers)
        return request

class SignerWrapper(requests.auth.AuthBase):

    def __init__(self, signer, enforce_content_headers=True):
        """Wraps an existing Signer and applies additional options.

        :param signer: The signer to be wrapped.
        :param enforce_content_headers: True if content headers should be automatically added if not present when
            signing put and post requests.
        """
        self._signer = signer
        self._enforce_content_headers = enforce_content_headers

    def __call__(self, request):
        return self._signer.__call__(request, enforce_content_headers = self._enforce_content_headers)
