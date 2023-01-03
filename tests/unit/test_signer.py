# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci._vendor import six
import base64
import hashlib
import pytest
import os
import tempfile
from oci._vendor.requests import Request
from oci.exceptions import InvalidConfig, InvalidPrivateKey, MissingPrivateKeyPassphrase
from oci.signer import load_private_key, load_private_key_from_file, inject_missing_headers, Signer
from .utils import generate_key, serialize_key, verify_signature
import io
import subprocess
import sys
from tests.integ.util import create_large_file
from oci.util import DEFAULT_PART_SIZE


def as_bytes(value):
    value = value or ""
    if isinstance(value, six.text_type):
        value = value.encode("utf-8")
    elif hasattr(value, "buffer") or hasattr(value, "read"):
        content = b''
        chunk = ""
        while True:
            if hasattr(value, "read"):
                chunk = value.read(DEFAULT_PART_SIZE)
            elif hasattr(value, "buffer"):
                chunk = value.buffer.read(DEFAULT_PART_SIZE)
            if len(chunk) == 0 or chunk == b'':
                break
            content += chunk
        value = content
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


@pytest.fixture(scope='function')
def content_input_file():
    filename = 'tests/resources/content_input.txt'
    create_large_file(filename, 3)
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


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


def test_key_content_precedence_over_key_file(api_key, private_key_file, pass_phrase):
    tenancy, user, fingerprint = api_key.split("/")
    with pytest.raises(InvalidPrivateKey):
        Signer(tenancy, user, fingerprint, private_key_file.name, pass_phrase, 'invalid private key content')


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


def test_inject_headers_for_body_as_file(content_input_file):
    with open(content_input_file, "rb") as test_file:
        request = Request(url="http://some.domain.com?query=string", data=test_file).prepare()
        inject_missing_headers(request, sign_body=True, enforce_content_headers=True)
        expected = {
            "host": "some.domain.com",
            "content-type": "application/octet-stream",
            "content-length": str(os.stat(content_input_file).st_size),
            "x-content-sha256": base64_sha256(test_file)
        }
        for header, expected_value in six.iteritems(expected):
            assert request.headers[header] == expected_value


def test_inject_headers_for_body_as_io_bytes():
    binary_data = b'0123456789abcdefg'
    data = io.BytesIO(binary_data)
    request = Request(url="http://some.domain.com?query=string", data=data).prepare()
    inject_missing_headers(request, sign_body=True, enforce_content_headers=True)
    expected = {
        "host": "some.domain.com",
        "content-type": "application/octet-stream",
        "content-length": str(len(binary_data)),
        "x-content-sha256": base64_sha256(data)
    }
    for header, expected_value in six.iteritems(expected):
        assert request.headers[header] == expected_value


def test_inject_headers_for_zero_length_stream():
    zero_content_file_path = os.path.join('tests', 'resources', 'zero_length_file.bin')
    with open(zero_content_file_path, 'wb'):
        pass
    with open(zero_content_file_path, "rb") as test_file:
        request = Request(url="http://some.domain.com?query=string", data=test_file).prepare()
        inject_missing_headers(request, sign_body=True, enforce_content_headers=True)
        expected = {
            "host": "some.domain.com",
            "content-type": "application/octet-stream",
            "content-length": str(os.stat(zero_content_file_path).st_size),
            "x-content-sha256": base64_sha256(test_file)
        }
        for header, expected_value in six.iteritems(expected):
            assert request.headers[header] == expected_value
    if os.path.exists(zero_content_file_path):
        os.remove(zero_content_file_path)


def test_inject_headers_from_stdin():
    if sys.platform == 'win32':
        pytest.skip("Stream piping tests don't run on Windows")
    small_file_path = os.path.join('tests', 'resources', 'small_file.bin')
    create_large_file(small_file_path, 5)  # Make a 5 MiB file
    print('cat-ing file and piping to script')
    cat_small_file = subprocess.Popen(['cat', small_file_path], stdout=subprocess.PIPE)
    call_return = subprocess.call(['python', 'tests/scripts/sign_from_stdin.py', str(os.stat(small_file_path).st_size)],
                                  stdin=cat_small_file.stdout)
    cat_small_file.wait()
    if os.path.exists(small_file_path):
        os.remove(small_file_path)
    assert call_return == 0


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

    verify_signature(public_key, signed_request.headers, 'post')
    assert signed_request.headers["x-content-sha256"] == base64_sha256(request_body)
    assert signed_request.headers["content-length"] == str(len(as_bytes(request_body)))


def test_sign_with_patch(signer, public_key, request_body):
    """Signature includes content-* headers by default"""
    request = Request(url="https://host.com/some-path", method="patch", data=request_body).prepare()
    signed_request = signer(request)

    verify_signature(public_key, signed_request.headers, 'patch')
    assert signed_request.headers["x-content-sha256"] == base64_sha256(request_body)
    assert signed_request.headers["content-length"] == str(len(as_bytes(request_body)))


def test_signer_created_from_static_method(config):
    signer = Signer.from_config(config)
    assert signer.api_key == '{}/{}/{}'.format(config['tenancy'], config['user'], config['fingerprint'])


def test_signer_created_from_static_method_with_invalid_config():
    with pytest.raises(InvalidConfig):
        Signer.from_config({})
