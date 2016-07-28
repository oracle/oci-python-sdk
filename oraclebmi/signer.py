import base64
import email.utils
import hashlib

import httpsig.requests_auth
import requests

class Signer(requests.auth.AuthBase):
    """A requests auth instance that can be reused across requests"""
    generic_headers = [
        "date",
        "(request-target)"
    ]
    body_headers = [
        "content-length",
        "content-type",
        "x-content-sha256",
    ]
    required_headers = {
        "options": [],
        "get": generic_headers,
        "head": generic_headers,
        "delete": generic_headers,
        "put": generic_headers + body_headers,
        "post": generic_headers + body_headers
    }

    def __init__(self, tenancy, user, fingerprint, private_key_file_location):
        self.api_key = tenancy + "/" + user + "/" + fingerprint
        self.private_key_file_location = private_key_file_location
        self._private_key = None

        # Build a httpsig.requests_auth.HTTPSignatureAuth for each
        # HTTP method's required headers
        self.signers = {}
        for method, headers in self.required_headers.items():
            signer = httpsig.sign.HeaderSigner(
                key_id=self.api_key, secret=self.private_key,
                algorithm="rsa-sha256", headers=headers[:])
            self.signers[method] = signer

    def inject_missing_headers(self, request, sign_body):
        # Inject date and content-type if missing
        request.headers.setdefault(
            "date", email.utils.formatdate(usegmt=True))
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

    def __call__(self, request):
        verb = request.method.lower()
        signer = self.signers.get(verb, (None, None))
        if signer is None:
            raise ValueError(
                "Don't know how to sign request verb {}".format(verb))

        # Inject body headers for put/post requests, date for all requests
        sign_body = verb in ["put", "post"]
        self.inject_missing_headers(request, sign_body=sign_body)

        signed_headers = signer.sign(
            request.headers,
            method=request.method,
            path=request.path_url)

        request.headers.update(signed_headers)
        return request

