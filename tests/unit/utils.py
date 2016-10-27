import base64
import re
import six
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

SIGNATURE_PATTERN = re.compile(
    r"""
    ^Signature\s
    algorithm="(?P<algorithm>[^"]*)",
    headers="(?P<headers>[^"]*)",
    keyId="(?P<key_id>[^"]*)",
    signature="(?P<signature>[^"]*)"
    $
    """,
    re.VERBOSE)


def unpack_authorization_header(authorization_header):
    return SIGNATURE_PATTERN.match(authorization_header).groupdict()


def generate_key(key_size=2048):
    return rsa.generate_private_key(public_exponent=66537, key_size=key_size, backend=default_backend())


def serialize_key(private_key=None, public_key=None, password=None, encoding="pem", format="pkcs1"):
    """
    >>> private_key = generate_key(2048)
    >>> public_key = private_key.public()
    >>> serialize_key(public_key=public_key, encoding="pem")
    >>> serialize_key(private_key=private_key, password="hunter2", format="pkcs1")
    """
    assert encoding.lower() in {"pem", "der", "ssh"}
    encoding = {
        "pem": serialization.Encoding.PEM,
        "der": serialization.Encoding.DER,
        "ssh": serialization.Encoding.OpenSSH
    }[encoding]

    if private_key:
        format = {
            "pkcs8": serialization.PrivateFormat.PKCS8,
            "pkcs1": serialization.PrivateFormat.TraditionalOpenSSL
        }[format.lower()]
        if password:
            if isinstance(password, six.string_types):
                password = password.encode("ascii")
            encryption_algorithm = serialization.BestAvailableEncryption(password)
        else:
            encryption_algorithm = serialization.NoEncryption()
        return private_key.private_bytes(
            encoding=encoding,
            format=format,
            encryption_algorithm=encryption_algorithm)
    else:
        format = {
            "spk": serialization.PublicFormat.SubjectPublicKeyInfo,
            "pkcs1": serialization.PublicFormat.PKCS1,
            "ssh": serialization.PublicFormat.OpenSSH
        }[format.lower()]
        return public_key.public_bytes(
            encoding=encoding,
            format=format)


def verify_signature(public_key, headers):
    signature_pieces = unpack_authorization_header(headers["authorization"])

    signed_headers = signature_pieces["headers"].split(" ")
    signing_string = []
    for header in signed_headers:
        if header == "(request-target)":
            value = "post /some-path"
        else:
            value = headers[header]
        signing_string.append("{}: {}".format(header, value))
    signing_string = "\n".join(signing_string)
    signature_bytes = base64.b64decode(signature_pieces["signature"])
    public_key.verify(signature_bytes, signing_string.encode("utf-8"),
                      padding.PKCS1v15(),
                      hashes.SHA256())
