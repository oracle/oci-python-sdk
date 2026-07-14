# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

import re

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

from ._vendor import six


REDACTED_VALUE = "REDACTED"

_NORMALIZED_DELIMITER_PATTERN = re.compile(r"[_-]+")

_EXACT_SENSITIVE_HEADER_NAMES = frozenset([
    "authorization",
    "proxy-authorization",
    "opc-obo-token",
    "x-api-key",
    "cookie",
    "set-cookie",
    "security-context",
    "password",
    "passphrase",
])

_SENSITIVE_HEADER_PREFIX_PATTERNS = (
    re.compile(r"^x-token(?:-|$).*"),
    re.compile(r"^x-authorization(?:-|$).*"),
    re.compile(r"^x-key-.*"),
)

_SENSITIVE_HEADER_SUFFIXES = (
    "access-token",
    "refresh-token",
    "id-token",
    "security-token",
    "session-token",
    "delegation-token",
    "client-secret",
    "private-key",
)

_HEADER_LINE_PATTERN = re.compile(r"(?m)^([!#$%&'*+.^_`|~0-9A-Za-z_-]+)\s*:\s*([^\r\n]*)")

_SENSITIVE_FIELD_NAMES = frozenset([
    "authorization",
    "proxy-authorization",
    "opc-obo-token",
    "x-api-key",
    "token",
    "accesstoken",
    "access_token",
    "refreshtoken",
    "refresh_token",
    "idtoken",
    "id_token",
    "delegationtoken",
    "delegation_token",
    "securitytoken",
    "security_token",
    "sessiontoken",
    "session_token",
    "serviceaccounttoken",
    "service_account_token",
    "subject_token",
    "clientsecret",
    "client_secret",
    "passphrase",
    "password",
    "privatekey",
    "private_key",
    "publickey",
    "public_key",
    "podkey",
    "pod_key",
    "cookie",
    "setcookie",
    "set_cookie",
    "securitycontext",
    "security_context",
])

_SENSITIVE_FIELD_PATTERN = (
    r"authorization|proxy-authorization|opc-obo-token|x-api-key|token|accessToken|"
    r"access_token|refreshToken|refresh_token|idToken|id_token|delegationToken|"
    r"delegation_token|securityToken|security_token|sessionToken|session_token|"
    r"serviceAccountToken|service_account_token|subject_token|client_secret|"
    r"clientSecret|passphrase|password|privateKey|private_key|publicKey|"
    r"public_key|podKey|pod_key"
)

_SENSITIVE_LOG_PATTERNS = (
    # JSON or Python-dict-like string values, for example "token":"value" or 'token': 'value'.
    (
        re.compile(r"(?i)([\"'](?:" + _SENSITIVE_FIELD_PATTERN + r")[\"']\s*:\s*)([\"'])(.*?)(\2)"),
        r"\1\2" + REDACTED_VALUE + r"\2",
    ),
    # JSON or Python-dict-like non-string scalar values, for example "token":123.
    (
        re.compile(r"(?i)([\"'](?:" + _SENSITIVE_FIELD_PATTERN + r")[\"']\s*:\s*)(?![\"'])([^,}\]\s]+)"),
        r"\1" + REDACTED_VALUE,
    ),
    # URL query strings and form bodies.
    (
        re.compile(r"(?i)(^|[?&\s])((?:" + _SENSITIVE_FIELD_PATTERN + r")=)([^&\s]*)"),
        r"\1\2" + REDACTED_VALUE,
    ),
    # Common bearer/basic token fragments outside header-dump format.
    (
        re.compile(r"(?i)\b(Bearer|Basic)\s+[A-Za-z0-9._~+/=-]+"),
        r"\1 " + REDACTED_VALUE,
    ),
    # Security tokens commonly start with ST$.
    (
        re.compile(r"\bST\$[A-Za-z0-9._-]+"),
        "ST$" + REDACTED_VALUE,
    ),
    # JWT-looking strings, including Kubernetes service account tokens.
    (
        re.compile(r"\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b"),
        REDACTED_VALUE,
    ),
    # PEM private keys should never be written to logs.
    (
        re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.DOTALL),
        REDACTED_VALUE,
    ),
)


def _normalize_header_name(key):
    if key is None:
        return None
    normalized_header_name = str(key).strip().lower()
    if not normalized_header_name:
        return ""
    return _NORMALIZED_DELIMITER_PATTERN.sub("-", normalized_header_name)


def _normalize_key_name(key):
    normalized_header_name = _normalize_header_name(key)
    if normalized_header_name is None:
        return None
    return normalized_header_name.replace("-", "")


def _matches_sensitive_header_rules(key):
    normalized_header_name = _normalize_header_name(key)
    if not normalized_header_name:
        return False

    if normalized_header_name in _EXACT_SENSITIVE_HEADER_NAMES:
        return True

    for pattern in _SENSITIVE_HEADER_PREFIX_PATTERNS:
        if pattern.match(normalized_header_name):
            return True

    if normalized_header_name in _SENSITIVE_HEADER_SUFFIXES:
        return True

    for suffix in _SENSITIVE_HEADER_SUFFIXES:
        if normalized_header_name.endswith("-" + suffix):
            return True

    return False


def _is_sensitive_key(key):
    if key is None:
        return False

    key_as_string = str(key)
    normalized_key = _normalize_key_name(key_as_string)
    return (
        key_as_string.lower() in _SENSITIVE_FIELD_NAMES or
        normalized_key in _SENSITIVE_FIELD_NAMES or
        _matches_sensitive_header_rules(key_as_string)
    )


def _redact_sensitive_header_value(value):
    if value is None:
        return None
    if isinstance(value, list):
        return [REDACTED_VALUE for _ in value]
    if isinstance(value, tuple):
        return tuple(REDACTED_VALUE for _ in value)
    return REDACTED_VALUE


def _redact_sensitive_header_lines(value):
    def _redact_header_match(match):
        header_name = match.group(1)
        if _matches_sensitive_header_rules(header_name):
            return "{}: {}".format(header_name, REDACTED_VALUE)
        return match.group(0)

    return _HEADER_LINE_PATTERN.sub(_redact_header_match, value)


def redact_sensitive_string_for_logs(value):
    """Return a string with common credential-bearing values removed for logging."""
    if value is None:
        return None

    redacted_value = value
    if isinstance(redacted_value, bytes):
        redacted_value = redacted_value.decode("utf-8", "replace")
    elif not isinstance(redacted_value, six.string_types):
        redacted_value = str(redacted_value)

    redacted_value = _redact_sensitive_header_lines(redacted_value)

    for pattern, replacement in _SENSITIVE_LOG_PATTERNS:
        redacted_value = pattern.sub(replacement, redacted_value)
    return redacted_value


def redact_sensitive_data_for_logs(value):
    """Return a redacted copy of data that is about to be written to logs."""
    if isinstance(value, Mapping):
        return {
            key: _redact_sensitive_header_value(item) if _is_sensitive_key(key) else redact_sensitive_data_for_logs(item)
            for key, item in six.iteritems(value)
        }

    if isinstance(value, list):
        return [redact_sensitive_data_for_logs(item) for item in value]

    if isinstance(value, tuple):
        return tuple(redact_sensitive_data_for_logs(item) for item in value)

    if isinstance(value, (bytes, six.string_types)):
        return redact_sensitive_string_for_logs(value)

    return value
