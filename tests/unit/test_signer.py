import six
import base64
import hashlib
import pytest
import os
import tempfile
from requests import Request
from oraclebmc.exceptions import InvalidPrivateKey
from oraclebmc import signer
from .utils import generate_key, serialize_key


def as_bytes(value):
    value = value or ""
    if isinstance(value, six.text_type):
        value = value.encode("utf-8")
    return value


@pytest.fixture(scope="module")
def private_key():
    return generate_key(2048)


@pytest.fixture(scope="module", params=["hunter2", None])
def pass_phrase(request):
    return request.param


@pytest.yield_fixture(scope="module")
def private_key_file(private_key, pass_phrase):
    with tempfile.NamedTemporaryFile(mode="w+b") as file:
        file.write(serialize_key(private_key=private_key, password=pass_phrase))
        file.seek(0)  # So the key can be read again
        yield file


@pytest.fixture(scope="module")
def public_key(private_key):
    return private_key.public_key()


@pytest.mark.parametrize("format", ["pkcs8", "pkcs1"])
def test_load_private_key(private_key, format, pass_phrase):
    """Successfully load a private key"""
    secret = serialize_key(private_key=private_key, password=pass_phrase, encoding="pem", format=format)
    loaded_key = signer.load_private_key(secret, pass_phrase)
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


@pytest.mark.parametrize("encoding", ["pem", "der"])
@pytest.mark.parametrize("format", ["spk", "pkcs1"])
def test_load_fails_for_public_key(public_key, encoding, format, pass_phrase):
    """Trying to load a public key as a private key provides a detailed error message"""
    secret = serialize_key(public_key=public_key, encoding=encoding, format=format)
    with pytest.raises(InvalidPrivateKey) as excinfo:
        signer.load_private_key(secret, pass_phrase)
    assert str(excinfo.value) == "Authentication requires a private key, but a public key was provided."


@pytest.mark.parametrize("body", [b"some-bytes", "some-string", "", None])
@pytest.mark.parametrize("sign_body", [True, False])
@pytest.mark.parametrize("enforce_content_headers", [True, False])
@pytest.mark.parametrize("existing_header", ["date", "host", "content-type", "content-length", "x-content-sha256"])
def test_inject_headers(body, sign_body, enforce_content_headers, existing_header):
    custom_header = "not injected"
    request = Request(url="http://some.domain.com?query=string", data=body).prepare()
    # Need to set the header *after* preparing, otherwise requests will blow away Content-Length
    request.headers[existing_header] = custom_header
    signer.inject_missing_headers(request, sign_body, enforce_content_headers)

    # Checked on its own; injected value isn't fixed
    if existing_header != "date":
        assert "date" in request.headers

    body = as_bytes(body)
    x_content_sha256 = base64.b64encode(hashlib.sha256(body).digest()).decode("utf-8")

    expected = {
        "host": "some.domain.com",
        "content-type": "application/json",
        "content-length": str(len(body)),
        "x-content-sha256": x_content_sha256,
        existing_header: custom_header
    }
    if not enforce_content_headers:
        expected.pop("content-type")
        expected.pop("content-length")
        expected.pop("x-content-sha256")
    elif not sign_body:
        expected.pop("content-length")
        expected.pop("x-content-sha256")

    for header, expected_value in six.iteritems(expected):
        assert request.headers[header] == expected_value


def test_from_file_expands_user(monkeypatch, private_key, pass_phrase, private_key_file):
    """~/.ssh/id_rsa should load a key from the full path to user's home"""

    # Hardcode os.path.expanduser to expand every path to the temp private key
    monkeypatch.setattr(os.path, "expanduser", lambda path: private_key_file.name)

    loaded_key = signer.load_private_key_from_file("~/.ssh/not-a-real-key-file", pass_phrase)
    assert loaded_key.private_numbers() == private_key.private_numbers()