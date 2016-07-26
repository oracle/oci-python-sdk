import base64
import email.utils
import hashlib
import httpsig.requests_auth
import json
import urllib

class Signer:
    """A request signer that can be reused across requests"""
    generic_headers = [
        "date", "(request-target)"
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

    def inject_missing_headers(self, headers, body, sign_body):
        # Inject date if missing
        headers.setdefault(
            "date", email.utils.formatdate(usegmt=True))

        headers.setdefault("content-type", "application/json")
        headers.setdefault("accept", "*/*")

        # Requests with a body need to send content-type,
        # content-length, and x-content-sha256
        if sign_body:
            if body is None:
                body = ""
            else:
                body = json.dumps(body)

            if "x-content-sha256" not in headers:
                m = hashlib.sha256(body.encode("utf-8"))
                base64digest = base64.b64encode(m.digest())
                base64string = base64digest.decode("utf-8")
                headers["x-content-sha256"] = base64string
            headers.setdefault("content-length", len(body))

    def sign(self, method, headers, url, path_url, query_params, body):
        verb = method.lower()

        signer = httpsig.sign.HeaderSigner(key_id=self.api_key,
                                           secret=self.private_key,
                                           algorithm="rsa-sha256",
                                           headers=self.required_headers[verb])

        # Inject body headers for put/post requests, date for all requests
        sign_body = verb in ["put", "post"]
        self.inject_missing_headers(headers=headers, body=body, sign_body=sign_body)

        path = urllib.parse.urlparse(url).path
        if query_params:
            path += "?" + urllib.parse.urlencode(query_params)

        signed_headers = signer.sign(headers, method=method, path=path)

        return signed_headers

    @property
    def private_key(self):
        if self._private_key is None:
            with open(self.private_key_file_location) as f:
                self._private_key = f.read().strip()
        return self._private_key