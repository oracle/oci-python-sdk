import six
import base64
import hashlib
import pytest
import os
import tempfile
from requests import Request
from oci.exceptions import InvalidPrivateKey, MissingPrivateKeyPassphrase
from oci.signer import load_private_key, load_private_key_from_file, inject_missing_headers, Signer
from .utils import generate_key, serialize_key, verify_signature


def as_bytes(value):
    value = value or ""
    if isinstance(value, six.text_type):
        value = value.encode("utf-8")
    return value


def base64_sha256(body):
    """Returns the sha256 of the body as a base64 encoded string."""
    content_sha256 = hashlib.sha256(as_bytes(body)).digest()
    b64_bytes = base64.b64encode(content_sha256)
    return b64_bytes.decode("utf-8")


@pytest.fixture(scope="module", params=[b"some-bytes", "some-string", "", None])
def request_body(request):
    return request.param


@pytest.fixture
def prepared_request(request_body):
    return Request(url="")


@pytest.fixture(scope="module")
def private_key():
    return generate_key(2048)


@pytest.fixture(scope="module")
def api_key():
    return "/".join(("tenancy", "user", "fingerprint"))


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


@pytest.fixture
def signer(api_key, private_key_file, pass_phrase):
    tenancy, user, fingerprint = api_key.split("/")
    return Signer(tenancy, user, fingerprint, private_key_file.name, pass_phrase)


@pytest.mark.parametrize("format", ["pkcs8", "pkcs1"])
def test_load_private_key(private_key, format, pass_phrase):
    """Successfully load a private key"""
    secret = serialize_key(private_key=private_key, password=pass_phrase, encoding="pem", format=format)
    loaded_key = load_private_key(secret, pass_phrase)
    assert loaded_key.private_numbers() == private_key.private_numbers()


def test_load_unencrypted_private_key_with_password(private_key):
    """Correctly load an unencrypted key even if a password is provided"""
    secret = serialize_key(private_key=private_key)
    loaded_key = load_private_key(secret, "unnecessary_password")
    assert loaded_key.private_numbers() == private_key.private_numbers()


def test_load_private_key_wrong_password(private_key):
    """Wrong password or omitted"""
    secret = serialize_key(private_key=private_key, password="correctpassphrase")
    with pytest.raises(InvalidPrivateKey) as excinfo:
        load_private_key(secret, "incorrectpassphrase")
    assert "provided passphrase is incorrect" in str(excinfo)


def test_load_private_key_missing_password(private_key):
    """Wrong password or omitted"""
    secret = serialize_key(private_key=private_key, password="correctpassphrase")
    with pytest.raises(MissingPrivateKeyPassphrase):
        load_private_key(secret, None)


def test_expand_user_in_private_key_file(api_key, private_key_file, pass_phrase):
    tenancy, user, fingerprint = api_key.split("/")
    with pytest.raises(IOError) as excinfo:
        Signer(tenancy, user, fingerprint, "~/.oci/a_key_that_doesnt_exist.pem", pass_phrase)

    assert "~" not in str(excinfo.value)
    assert "/.oci/a_key_that_doesnt_exist.pem" in str(excinfo.value)


@pytest.mark.parametrize("encoding", ["pem", "der"])
@pytest.mark.parametrize("format", ["spk", "pkcs1"])
def test_load_fails_for_public_key(public_key, pass_phrase, encoding, format):
    """Trying to load a public key as a private key provides a detailed error message"""
    secret = serialize_key(public_key=public_key, encoding=encoding, format=format)
    with pytest.raises(InvalidPrivateKey) as excinfo:
        load_private_key(secret, pass_phrase)
    assert str(excinfo.value) == "Authentication requires a private key, but a public key was provided."


@pytest.mark.parametrize("sign_body", [True, False])
@pytest.mark.parametrize("enforce_content_headers", [True, False])
@pytest.mark.parametrize("existing_header", ["date", "host", "content-type", "content-length", "x-content-sha256"])
def test_inject_headers(request_body, sign_body, enforce_content_headers, existing_header):
    custom_header = "not injected"
    request = Request(url="http://some.domain.com?query=string", data=request_body).prepare()
    # Need to set the header *after* preparing, otherwise requests will blow away Content-Length
    request.headers[existing_header] = custom_header
    inject_missing_headers(request, sign_body, enforce_content_headers)

    # Checked on its own; injected value isn't fixed
    if existing_header != "date":
        assert "date" in request.headers

    request_body = as_bytes(request_body)

    expected = {
        "host": "some.domain.com",
        "content-type": "application/json",
        "content-length": str(len(request_body)),
        "x-content-sha256": base64_sha256(request_body),
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

    loaded_key = load_private_key_from_file("~/.ssh/not-a-real-key-file", pass_phrase)
    assert loaded_key.private_numbers() == private_key.private_numbers()


def test_sign_unknown_method(signer):
    """Methods must be whitelisted for signing"""
    request = Request(url="https://host.com", method="not-a-method").prepare()
    with pytest.raises(ValueError):
        signer(request)


def test_sign_with_body(signer, public_key, request_body):
    """Signature includes content-* headers by default"""
    request = Request(url="https://host.com/some-path", method="post", data=request_body).prepare()
    signed_request = signer(request)

    verify_signature(public_key, signed_request.headers)
    assert signed_request.headers["x-content-sha256"] == base64_sha256(request_body)
    assert signed_request.headers["content-length"] == str(len(as_bytes(request_body)))
