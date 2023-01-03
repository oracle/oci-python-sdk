# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import base64
import re
from oci._vendor import six
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

SIGNATURE_PATTERN = re.compile(
    r"""
    ^
    Signature\s
    algorithm="(?P<algorithm>[^"]*)",
    headers="(?P<headers>[^"]*)",
    keyId="(?P<key_id>[^"]*)",
    signature="(?P<signature>[^"]*)",
    version="(?P<version>[^"]*)"
    $
    """,
    re.VERBOSE)


def unpack_authorization_header(authorization_header):
    return SIGNATURE_PATTERN.match(authorization_header).groupdict()


def generate_key(key_size=2048):
    return rsa.generate_private_key(public_exponent=65537, key_size=key_size, backend=default_backend())


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


def verify_signature(public_key, headers, method):
    signature_pieces = unpack_authorization_header(headers["authorization"])
    signed_headers = signature_pieces["headers"].split(" ")

    # Hardcoded to guard against unexpected changes to signer behavior
    assert signature_pieces["algorithm"] == "rsa-sha256"
    assert signature_pieces["version"] == "1"

    signing_string = []
    for header in signed_headers:
        if header == "(request-target)":
            value = "{} /some-path".format(method)
        else:
            value = headers[header]
        signing_string.append("{}: {}".format(header, value))
    signing_string = "\n".join(signing_string)
    signature_bytes = base64.b64decode(signature_pieces["signature"])

    public_key.verify(signature_bytes, signing_string.encode("utf-8"),
                      padding.PKCS1v15(),
                      hashes.SHA256())


def create_large_file(filename, size_in_mebibytes):
    sample_content = b'a'
    with open(filename, 'wb') as f:
        while f.tell() < 1024 * 1024 * size_in_mebibytes:
            f.write(sample_content * 1024 * 1024)
