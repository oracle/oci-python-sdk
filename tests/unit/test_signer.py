import pytest
from oraclebmc.exceptions import InvalidPrivateKey
from oraclebmc import signer
from .utils import generate_key, serialize_key


@pytest.fixture(scope="module")
def private_key():
    return generate_key(2048)


@pytest.fixture(scope="module")
def public_key(private_key):
    return private_key.public_key()


@pytest.mark.parametrize("format", ("pkcs8", "pkcs1"))
@pytest.mark.parametrize("password", ("hunter2", None))
def test_load_private_key(private_key, format, password):
    """Successfully load a private key"""
    secret = serialize_key(private_key=private_key, password=password, encoding="pem", format=format)
    loaded_key = signer.load_private_key(secret, password)
    assert loaded_key.private_numbers() == private_key.private_numbers()


def test_load_unencrypted_private_key_with_password(private_key):
    """Correctly load an unencrypted key even if a password is provided"""
    secret = serialize_key(private_key=private_key)
    loaded_key = signer.load_private_key(secret, "unnecessary_password")
    assert loaded_key.private_numbers() == private_key.private_numbers()


@pytest.mark.parametrize("actual, provided", [("hunter2", None), ("hunter2", "secret")])
def test_load_private_key_wrong_password(private_key, actual, provided):
    """Wrong password or omitted"""
    secret = serialize_key(private_key=private_key, password=actual)
    with pytest.raises(InvalidPrivateKey):
        signer.load_private_key(secret, provided)


@pytest.mark.parametrize("encoding", ("pem", "der"))
@pytest.mark.parametrize("format", ("spk", "pkcs1"))
@pytest.mark.parametrize("password", ("hunter2", None))
def test_load_fails_for_public_key(public_key, encoding, format, password):
    """Trying to load a public key as a private key provides a detailed error message"""
    secret = serialize_key(public_key=public_key, encoding=encoding, format=format)
    with pytest.raises(InvalidPrivateKey) as excinfo:
        signer.load_private_key(secret, password)
    assert str(excinfo.value) == "Authentication requires a private key, but a public key was provided."
