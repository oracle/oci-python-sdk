import six
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


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
