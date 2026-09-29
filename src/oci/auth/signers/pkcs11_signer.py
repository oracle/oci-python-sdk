# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import base64
import pkcs11
import urllib
import hashlib
import platform
import threading
import os
import ntpath
import ctypes.util
import logging
import oci.signer
from oci.auth import signers
from pkcs11.constants import Attribute, ObjectClass, SlotFlag
from pkcs11.mechanisms import Mechanism
from getpass import getpass
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID, ObjectIdentifier

system = platform.system()
DEFAULT_KEY_SLOT_LABEL = 'PIV AUTH'
CARD_AUTH_KEY_SLOT_LABEL = 'CARD AUTH'
PIV_AUTH_KEY_ID = b'\x01'
CARD_AUTH_KEY_ID = b'\x04'
SHA256_DIGEST_INFO_PREFIX = bytes.fromhex("3031300d060960864801650304020105000420")
YUBICO_PIV_USAGE_POLICY_OID = ObjectIdentifier("1.3.6.1.4.1.41482.3.8")
YUBICO_TOUCH_POLICIES = {1: "never", 2: "always", 3: "cached"}

# Common aliases for PKCS#11 PIV object labels.
SLOT_LABEL_ALIASES = {
    'PIV': 'PIV AUTH',
    'PIV AUTH': 'PIV AUTH',
    '9A': 'PIV AUTH',
    'CARD': CARD_AUTH_KEY_SLOT_LABEL,
    'CARD AUTH': CARD_AUTH_KEY_SLOT_LABEL,
    '9E': CARD_AUTH_KEY_SLOT_LABEL,
}

platforms = {
    "Darwin": [
        "/usr/local/lib/opensc-pkcs11.so",
        "/opt/homebrew/lib/opensc-pkcs11.so",
        "/usr/local/lib/opensc-pkcs11.dylib",
        "/opt/homebrew/lib/opensc-pkcs11.dylib",
        "/usr/local/lib/libykcs11.dylib",
        "/opt/homebrew/lib/libykcs11.dylib",
    ],
    "Linux": [
        "/usr/lib64/pkcs11/opensc-pkcs11.so",
        "/usr/lib64/opensc-pkcs11.so",
        "/usr/lib/x86_64-linux-gnu/pkcs11/opensc-pkcs11.so",
        "/usr/lib/x86_64-linux-gnu/opensc-pkcs11.so",
        "/usr/lib/aarch64-linux-gnu/pkcs11/opensc-pkcs11.so",
        "/usr/lib/aarch64-linux-gnu/opensc-pkcs11.so",
        "/usr/lib/pkcs11/opensc-pkcs11.so",
        "/usr/lib/opensc-pkcs11.so",
        "/usr/local/lib/libykcs11.so",
        "/usr/local/lib64/libykcs11.so",
        "/usr/lib64/libykcs11.so",
        "/usr/lib/libykcs11.so",
        "/usr/lib/x86_64-linux-gnu/libykcs11.so",
        "/usr/lib/aarch64-linux-gnu/libykcs11.so",
    ],
    "Windows": [
        r"C:\Program Files\OpenSC Project\OpenSC\pkcs11\opensc-pkcs11.dll",
        r"C:\Program Files (x86)\OpenSC Project\OpenSC\pkcs11\opensc-pkcs11.dll",
        r"C:\Program Files\Yubico\Yubico PIV Tool\bin\libykcs11.dll",
        r"C:\Program Files (x86)\Yubico\Yubico PIV Tool\bin\libykcs11.dll",
    ],
}

_PLATFORM_ALIASES = {
    "darwin": "Darwin",
    "mac": "Darwin",
    "macos": "Darwin",
    "osx": "Darwin",
    "linux": "Linux",
    "ubuntu": "Linux",
    "unix": "Linux",
    "windows": "Windows",
}

_SUPPORTED_PKCS11_MODULE_NAMES = ("opensc-pkcs11", "ykcs11", "libykcs11")


def _canonical_platform_name(system_name):
    if not system_name:
        return system_name

    if system_name in platforms:
        return system_name

    return _PLATFORM_ALIASES.get(system_name.strip().lower(), system_name)


def _platform_provider_candidates(system_name, environ=None):
    system_name = _canonical_platform_name(system_name)
    environ = environ if environ is not None else os.environ
    provider_candidates = list(platforms.get(system_name, []))

    if system_name == "Windows":
        windows_base_dirs = [
            environ.get("PROGRAMFILES"),
            environ.get("PROGRAMW6432"),
            environ.get("PROGRAMFILES(X86)"),
        ]
        for base in windows_base_dirs:
            if not base:
                continue
            provider_candidates.append(
                ntpath.join(base, "OpenSC Project", "OpenSC", "pkcs11", "opensc-pkcs11.dll")
            )
            provider_candidates.append(
                ntpath.join(base, "Yubico", "Yubico PIV Tool", "bin", "libykcs11.dll")
            )

    deduped_candidates = []
    seen = set()
    for candidate in provider_candidates:
        if candidate not in seen:
            deduped_candidates.append(candidate)
            seen.add(candidate)

    return deduped_candidates


def _find_dynamic_pkcs11_libraries(system_name, find_library=None):
    system_name = _canonical_platform_name(system_name)
    find_library = find_library or ctypes.util.find_library

    module_names = list(_SUPPORTED_PKCS11_MODULE_NAMES)

    discovered_libraries = []
    for module_name in module_names:
        discovered = find_library(module_name)
        if discovered:
            discovered_libraries.append(discovered)

    deduped_libraries = []
    seen = set()
    for discovered in discovered_libraries:
        if discovered not in seen:
            deduped_libraries.append(discovered)
            seen.add(discovered)

    return deduped_libraries


def _resolve_provider(system_name=None, environ=None, path_exists=None):
    raw_system_name = system_name or platform.system()
    system_name = _canonical_platform_name(raw_system_name)
    environ = environ if environ is not None else os.environ
    path_exists = path_exists or os.path.exists

    provider_override = environ.get("OCI_PKCS11_LIB") or environ.get("PKCS11_MODULE_PATH")
    if provider_override:
        provider_override_looks_like_path = (
            "/" in provider_override or
            "\\" in provider_override or
            (len(provider_override) > 1 and provider_override[1] == ":")
        )
        if provider_override_looks_like_path and not path_exists(provider_override):
            raise RuntimeError(
                "Configured PKCS#11 module path does not exist: {}".format(provider_override)
            )
        return provider_override

    provider_candidates = _platform_provider_candidates(system_name, environ=environ)
    if not provider_candidates:
        raise RuntimeError('Unsupported platform {}'.format(raw_system_name))

    for candidate in provider_candidates:
        if path_exists(candidate):
            return candidate

    dynamic_candidates = _find_dynamic_pkcs11_libraries(system_name)
    if dynamic_candidates:
        return dynamic_candidates[0]

    raise RuntimeError(
        "Unable to find a supported PKCS#11 module ({}) for platform {}. "
        "Checked paths: {}. Set OCI_PKCS11_LIB (or PKCS11_MODULE_PATH) "
        "to a valid opensc-pkcs11/libykcs11 module path.".format(
            ", ".join(_SUPPORTED_PKCS11_MODULE_NAMES),
            raw_system_name,
            ", ".join(provider_candidates)
        )
    )


def _resolve_provider_path(module_path=None, system_name=None):
    if module_path:
        if not os.path.exists(module_path) or os.path.isdir(module_path):
            raise RuntimeError('PKCS#11 module path "{}" does not exist'.format(module_path))
        return module_path

    return provider or _resolve_provider(system_name=system_name or system)


provider = None


def _build_no_token_error(provider_path, available_slots_count):
    message = (
        "No PKCS#11 token detected (provider: {}). "
        "Available slots: {}. "
        "Ensure your PKCS#11 token is connected/unlocked and PKCS#11 tooling can see it "
        "(for example: pkcs11-tool --module {} --list-slots)."
    ).format(provider_path, available_slots_count, provider_path)

    return message


def _slot_has_token(slot):
    flags = getattr(slot, "flags", None)
    if flags is not None:
        token_present_attr = getattr(flags, "token_present", None)
        if token_present_attr is not None:
            return bool(token_present_attr)

        try:
            if SlotFlag.TOKEN_PRESENT in flags:
                return True
        except TypeError:
            pass

    try:
        slot.get_token()
        return True
    except Exception:
        return False


def _normalize_token_selector_value(value):
    if value is None:
        return None

    if isinstance(value, bytes):
        stripped_value = value.rstrip()
        try:
            decoded_value = stripped_value.decode('ascii').strip()
            if decoded_value and all(character.isprintable() for character in decoded_value):
                return decoded_value
        except UnicodeDecodeError:
            pass

        return stripped_value.hex()

    cleaned_value = str(value).strip()
    if not cleaned_value:
        return None

    return cleaned_value


def _normalize_token_serial(value):
    normalized_value = _normalize_token_selector_value(value)
    if normalized_value is None:
        return None

    normalized_value = normalized_value.strip().lower()
    if normalized_value.startswith("0x"):
        normalized_value = normalized_value[2:]

    return ''.join(character for character in normalized_value if character not in ' :-')


def _validate_token_selection(token_label=None, token_serial=None):
    if _normalize_token_selector_value(token_label) and _normalize_token_serial(token_serial):
        raise ValueError("PKCS#11 token label and token serial cannot both be provided")


def _token_attribute_matches(token, attribute_name, expected_value):
    expected_value = _normalize_token_selector_value(expected_value)
    if expected_value is None:
        return True

    return _normalize_token_selector_value(getattr(token, attribute_name, None)) == expected_value


def _token_serial_matches(token, expected_serial):
    expected_serial = _normalize_token_serial(expected_serial)
    if expected_serial is None:
        return True

    return _normalize_token_serial(getattr(token, "serial", None)) == expected_serial


def _select_token(token_present_slots, token_label=None, token_serial=None):
    _validate_token_selection(token_label=token_label, token_serial=token_serial)

    tokens = [slot.get_token() for slot in token_present_slots]
    normalized_token_label = _normalize_token_selector_value(token_label)
    normalized_token_serial = _normalize_token_serial(token_serial)

    if normalized_token_label is None and normalized_token_serial is None:
        return tokens[0]

    for token in tokens:
        if _token_attribute_matches(token, "label", normalized_token_label) and _token_serial_matches(token, token_serial):
            return token

    if normalized_token_label is not None:
        raise RuntimeError('PKCS#11 token with label "{}" was not found'.format(normalized_token_label))

    raise RuntimeError('PKCS#11 token with serial "{}" was not found'.format(normalized_token_serial))


def _resolve_key_slot_label(slot_label):
    if slot_label is None:
        return DEFAULT_KEY_SLOT_LABEL

    cleaned_slot_label = slot_label.strip()
    if not cleaned_slot_label:
        return DEFAULT_KEY_SLOT_LABEL

    return SLOT_LABEL_ALIASES.get(cleaned_slot_label.upper(), cleaned_slot_label)


def _resolve_object_selection(key_slot_label=None, key_id=None):
    _validate_key_selection(key_slot_label=key_slot_label, key_id=key_id)

    if key_id is not None:
        normalized_key_id = _normalize_key_id(key_id)
        if normalized_key_id == b'\x00':
            return PIV_AUTH_KEY_ID, None
        if len(normalized_key_id) > 1:
            raise ValueError("Unsupported PKCS#11 key ID: object IDs must fit in one byte")
        return normalized_key_id, None

    resolved_label = _resolve_key_slot_label(key_slot_label)
    if resolved_label == DEFAULT_KEY_SLOT_LABEL:
        return PIV_AUTH_KEY_ID, None
    if resolved_label == CARD_AUTH_KEY_SLOT_LABEL:
        return CARD_AUTH_KEY_ID, None

    return None, resolved_label


def _validate_key_selection(key_slot_label=None, key_id=None):
    if key_id is None:
        return

    if key_slot_label is None:
        return

    if key_slot_label.strip():
        raise ValueError("PKCS#11 key label and key ID cannot both be provided")


def _normalize_key_id(key_id):
    if key_id is None:
        return None

    if isinstance(key_id, bytes):
        if not key_id:
            raise ValueError("PKCS#11 key ID cannot be empty")
        return key_id

    if isinstance(key_id, bytearray):
        if not key_id:
            raise ValueError("PKCS#11 key ID cannot be empty")
        return bytes(key_id)

    if isinstance(key_id, str):
        cleaned_key_id = key_id.strip()
        if not cleaned_key_id:
            raise ValueError("PKCS#11 key ID cannot be empty")

        base = 16 if cleaned_key_id.lower().startswith("0x") else 10
        try:
            key_id = int(cleaned_key_id, base)
        except ValueError:
            raise ValueError("PKCS#11 key ID must be a non-negative integer")

    if isinstance(key_id, int):
        if key_id < 0:
            raise ValueError("PKCS#11 key ID must be a non-negative integer")

        byte_length = max(1, (key_id.bit_length() + 7) // 8)
        return key_id.to_bytes(byte_length, byteorder='big')

    raise TypeError("PKCS#11 key ID must be provided as an integer, numeric string, or bytes")


def _key_selection_allows_authless(key_slot_label=None, key_id=None):
    if _normalize_key_id(key_id) == CARD_AUTH_KEY_ID:
        return True

    if key_slot_label is None:
        return False

    return _resolve_key_slot_label(key_slot_label) == CARD_AUTH_KEY_SLOT_LABEL


def _create_md5_fingerprint_hasher():
    try:
        return hashlib.md5()
    except ValueError:
        # OCI API key fingerprints are MD5 by definition; in FIPS mode this
        # is non-security metadata generation.
        pass

    try:
        return hashlib.md5(usedforsecurity=False)
    except TypeError:
        # usedforsecurity is unavailable on older Python hashlib APIs.
        pass
    except ValueError:
        try:
            return hashlib.new('md5', usedforsecurity=False)
        except TypeError:
            return hashlib.new('md5')


def _fingerprint_bytes(value):
    hasher = _create_md5_fingerprint_hasher()
    hasher.update(value)
    digest = hasher.hexdigest()
    return ':'.join(a + b for a, b in zip(digest[::2], digest[1::2]))


def _sha256_digest_info(data):
    return SHA256_DIGEST_INFO_PREFIX + hashlib.sha256(data).digest()


def _pkcs11_signing_payload(data, mechanism):
    if mechanism == Mechanism.SHA256_RSA_PKCS:
        return _sha256_digest_info(data), Mechanism.RSA_PKCS

    return data, mechanism


def _certificate_public_key_fingerprint(certificate_der):
    certificate = x509.load_der_x509_certificate(certificate_der)
    public_key = certificate.public_key()
    if not isinstance(public_key, rsa.RSAPublicKey):
        raise RuntimeError("PKCS#11 token contains unsupported public key type {}".format(type(public_key)))

    public_key_der = public_key.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return _fingerprint_bytes(public_key_der), certificate


def _certificate_appears_to_require_touch(certificate):
    if certificate is None:
        return False

    common_names = certificate.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
    return any("touch" in common_name.value.lower() for common_name in common_names)


def _normalize_required_touch_policy(required_touch_policy):
    if required_touch_policy is None:
        return None
    if not isinstance(required_touch_policy, str):
        raise TypeError("Required touch policy must be provided as a string")
    normalized = required_touch_policy.strip().lower()
    if normalized not in YUBICO_TOUCH_POLICIES.values():
        raise ValueError("Required touch policy must be one of: always, cached, never")
    return normalized


def _attested_touch_policy(certificate_der):
    certificate = x509.load_der_x509_certificate(certificate_der)
    try:
        extension = certificate.extensions.get_extension_for_oid(YUBICO_PIV_USAGE_POLICY_OID)
    except x509.ExtensionNotFound:
        return None

    extension_value = getattr(extension.value, "value", b"")
    if len(extension_value) != 2:
        raise RuntimeError("YubiKey attestation contains an invalid usage-policy extension")
    touch_policy = YUBICO_TOUCH_POLICIES.get(extension_value[1])
    if touch_policy is None:
        raise RuntimeError("YubiKey attestation contains an unknown touch policy")
    return touch_policy


class PKCS11Signer:
    lock = threading.Lock()

    def __init__(
        self,
        pin,
        key_slot_label=None,
        key_id=None,
        token_label=None,
        token_serial=None,
        key_id_override=None,
        module_path=None,
        required_touch_policy=None,
        allow_unverified_touch_policy=False
    ):
        """
        Create a PKCS#11-backed signer.

        `key_slot_label` and `key_id` are mutually exclusive. If neither is
        provided, the default PIV authentication key label is used.
        `token_label` and `token_serial` are mutually exclusive. If neither is
        provided, the first token returned by the PKCS#11 module is used.
        """
        self._pin = None
        self._closed = False
        _validate_key_selection(key_slot_label=key_slot_label, key_id=key_id)
        _validate_token_selection(token_label=token_label, token_serial=token_serial)
        self.key_id, self.key_slot_label = _resolve_object_selection(
            key_slot_label=key_slot_label,
            key_id=key_id
        )
        if self.key_slot_label is not None:
            self.public_key_label = '{} pubkey'.format(self.key_slot_label)
            self.private_key_label = '{} key'.format(self.key_slot_label)
        else:
            self.public_key_label = None
            self.private_key_label = None
        self._touch_prompt_required = False
        self.required_touch_policy = _normalize_required_touch_policy(required_touch_policy)
        if not isinstance(allow_unverified_touch_policy, bool):
            raise TypeError("allow_unverified_touch_policy must be provided as a boolean")
        self.allow_unverified_touch_policy = allow_unverified_touch_policy
        self.key_id_override = key_id_override
        self._card_auth_selected = _key_selection_allows_authless(
            key_slot_label=self.key_slot_label,
            key_id=self.key_id
        )
        # YKCS11 can require a logged-in session for CARD AUTH private-key
        # operations even when slot 9E uses its default PIN policy. Retain the
        # initial PIN so every new PKCS#11 session can authenticate.
        self._pin_required = True
        self._set_pin(pin)

        try:
            with self.lock:
                resolved_provider = _resolve_provider_path(module_path=module_path, system_name=system)
                self.lib = pkcs11.lib(resolved_provider)
                slots = list(self.lib.get_slots())
                token_present_slots = [slot for slot in slots if _slot_has_token(slot)]
                if not token_present_slots:
                    raise RuntimeError(_build_no_token_error(resolved_provider, len(slots)))

                self.token = _select_token(
                    token_present_slots,
                    token_label=token_label,
                    token_serial=token_serial
                )

                with self._open_session() as session:
                    certificate = self._get_certificate(session)
                    if certificate is not None:
                        self.fingerprint, parsed_certificate = _certificate_public_key_fingerprint(
                            certificate[Attribute.VALUE]
                        )
                        self._touch_prompt_required = _certificate_appears_to_require_touch(parsed_certificate)
                    else:
                        try:
                            key = self._get_public_key(session)
                        except Exception as error:
                            if self._card_auth_selected:
                                raise RuntimeError(
                                    "Unable to read the CARD AUTH public key. On YubiKey firmware earlier than "
                                    "5.3, install the CARD AUTH certificate so its public key can be used instead "
                                    "of PIV key metadata."
                                ) from error
                            raise
                        self.fingerprint = _fingerprint_bytes(key[Attribute.VALUE])

                    if self.required_touch_policy is not None:
                        self._enforce_required_touch_policy(session)
        except Exception:
            self._clear_pin()
            raise

    def sign(self, data, mechanism=Mechanism.SHA256_RSA_PKCS):
        if getattr(self, "_touch_prompt_required", False):
            logging.getLogger(__name__).info("Touch the external authenticator to authorize signing")
        with self.lock:
            with self._open_session() as session:
                key = self._get_private_key(session)
                signing_payload, signing_mechanism = _pkcs11_signing_payload(data, mechanism)
                return key.sign(signing_payload, mechanism=signing_mechanism)

    def verify(self, data, signature, mechanism=Mechanism.SHA256_RSA_PKCS):
        with self.lock:
            with self._open_session() as session:
                key = self._get_public_key(session)
                signing_payload, signing_mechanism = _pkcs11_signing_payload(data, mechanism)
                return key.verify(signing_payload, signature, mechanism=signing_mechanism)

    def _open_session(self):
        pin_value = self._get_pin()
        if pin_value is None:
            return self.token.open()

        return self.token.open(user_pin=pin_value)

    def _get_public_key(self, session):
        if getattr(self, "key_id", None) is not None:
            return session.get_key(object_class=ObjectClass.PUBLIC_KEY, id=self.key_id)

        return session.get_key(label=self.public_key_label)

    def _get_certificate(self, session):
        attrs = {Attribute.CLASS: ObjectClass.CERTIFICATE}
        if getattr(self, "key_id", None) is not None:
            attrs[Attribute.ID] = self.key_id
        else:
            attrs[Attribute.LABEL] = self.key_slot_label

        try:
            return next(iter(session.get_objects(attrs)))
        except AttributeError:
            return None
        except StopIteration:
            return None

    def _get_attestation_certificate(self, session):
        if getattr(self, "key_id", None) is None:
            return None

        attrs = {
            Attribute.CLASS: ObjectClass.CERTIFICATE,
            Attribute.ID: self.key_id,
            Attribute.TOKEN: False,
        }
        try:
            for certificate in session.get_objects(attrs):
                certificate_der = certificate[Attribute.VALUE]
                if _attested_touch_policy(certificate_der) is not None:
                    return certificate_der
        except (AttributeError, RuntimeError):
            return None
        return None

    def _enforce_required_touch_policy(self, session):
        attestation_der = self._get_attestation_certificate(session)
        if attestation_der is None:
            if self.allow_unverified_touch_policy:
                logging.getLogger(__name__).warning(
                    "Unable to verify YubiKey touch policy %s from PIV attestation; "
                    "continuing in compatibility mode and relying on the token's provisioned policy",
                    self.required_touch_policy.upper()
                )
                return
            raise RuntimeError(
                "Unable to verify the required touch policy. Use a key generated on the YubiKey "
                "with PIV attestation support, and provision it with touch policy {}."
                .format(self.required_touch_policy.upper())
            )

        actual_touch_policy = _attested_touch_policy(attestation_der)
        if actual_touch_policy != self.required_touch_policy:
            raise RuntimeError(
                "YubiKey touch policy is {}, but {} is required. The policy can only be changed "
                "by generating or importing a replacement key."
                .format(actual_touch_policy.upper(), self.required_touch_policy.upper())
            )

    def _get_private_key(self, session):
        if getattr(self, "key_id", None) is not None:
            return session.get_key(object_class=ObjectClass.PRIVATE_KEY, id=self.key_id)

        return session.get_key(label=self.private_key_label)

    def close(self):
        self._clear_pin()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.close()
        return False

    def _set_pin(self, pin):
        self._closed = False
        if pin is None:
            if getattr(self, "_pin_required", True):
                raise TypeError("PKCS#11 PIN must be provided as a string")
            self._pin = None
            return

        if not isinstance(pin, str):
            raise TypeError("PKCS#11 PIN must be provided as a string")

        pin_bytes = pin.encode('utf-8')

        self._pin = bytearray(pin_bytes)

    def _get_pin(self):
        if self._closed:
            raise RuntimeError("PKCS#11 PIN is unavailable for this signer")

        if self._pin is None:
            return None

        return self._pin.decode('utf-8')

    def _clear_pin(self):
        if self._pin is None:
            self._closed = True
            return

        for index in range(len(self._pin)):
            self._pin[index] = 0
        self._pin = None
        self._closed = True

    def selected_key_description(self):
        if getattr(self, "key_id", None) is not None:
            return "ID {}".format(self.key_id.hex())

        if getattr(self, "key_slot_label", None):
            return 'label "{}"'.format(self.key_slot_label)

        return "unknown"


class PKCS11RequestSigner(signers.SecurityTokenSigner):
    generic_headers = [
        'date',
        '(request-target)',
        'host'
    ]
    body_headers = [
        'content-length',
        'content-type',
        'x-content-sha256',
    ]
    required_headers = {
        'get': generic_headers,
        'head': generic_headers,
        'delete': generic_headers,
        'put': generic_headers + body_headers,
        'post': generic_headers + body_headers,
        'patch': generic_headers + body_headers
    }

    def __init__(
        self,
        user,
        tenancy,
        pin,
        pkcs11_slot=None,
        pkcs11_key_id=None,
        pkcs11_token_label=None,
        pkcs11_token_serial=None,
        pkcs11_key_id_override=None,
        pkcs11_module_path=None,
        pkcs11_required_touch_policy=None,
        pkcs11_allow_unverified_touch_policy=False
    ):
        _validate_key_selection(key_slot_label=pkcs11_slot, key_id=pkcs11_key_id)
        _validate_token_selection(token_label=pkcs11_token_label, token_serial=pkcs11_token_serial)
        normalized_key_id = _normalize_key_id(pkcs11_key_id)
        self.pkcs11_signer = PKCS11Signer(
            pin,
            key_slot_label=pkcs11_slot,
            key_id=normalized_key_id,
            token_label=pkcs11_token_label,
            token_serial=pkcs11_token_serial,
            key_id_override=pkcs11_key_id_override,
            module_path=pkcs11_module_path,
            required_touch_policy=pkcs11_required_touch_policy,
            allow_unverified_touch_policy=pkcs11_allow_unverified_touch_policy
        )
        self.keyid = pkcs11_key_id_override or '{}/{}/{}'.format(tenancy, user, self.pkcs11_signer.fingerprint)

    def sign(self, request):
        verb = request.method.lower()
        if verb not in self.required_headers:
            raise ValueError("Don't know how to sign request verb {}".format(verb))

        required_headers = self.required_headers[verb]
        host = urllib.parse.urlparse(request.url).netloc
        path = request.path_url
        values = []

        for header in required_headers:
            header = header.lower()

            if header == '(request-target)':
                values.append('{}: {} {}'.format(header, verb, path))
            elif header == 'host':
                values.append('{}: {}'.format(header, host))
            elif header == 'date':
                header_value = request.headers.get(header)
                if header_value is None or header_value == '':
                    raise ValueError("Missing required header '{}' for request verb {}".format(header, verb))
                values.append('{}: {}'.format(header, header_value))
            else:
                header_value = request.headers.get(header)
                if header_value is None or header_value == '':
                    raise ValueError("Missing required header '{}' for request verb {}".format(header, verb))
                values.append('{}: {}'.format(header, header_value))

        data = '\n'.join(values).encode('ascii')
        signature = self.pkcs11_signer.sign(data)

        return {
            'authorization': 'Signature keyId="{}",version="{}",algorithm="{}",headers="{}",signature="{}"'.format(
                self.keyid,
                '1',
                'rsa-sha256',
                ' '.join(required_headers),
                base64.b64encode(signature).decode('ascii')
            )
        }

    def __call__(self, request):
        verb = request.method.lower()

        if verb == 'options':
            return request

        oci.signer.inject_missing_headers(request, verb in ['put', 'post', 'patch'], enforce_content_headers=True)
        auth_header = self.sign(request)
        request.headers.update(auth_header)
        return request

    @staticmethod
    def get_pkcs11_signer(
        client_config,
        pkcs11_pin,
        pkcs11_slot=None,
        pkcs11_key_id=None,
        pkcs11_token_label=None,
        pkcs11_token_serial=None,
        pkcs11_key_id_override=None,
        pkcs11_module_path=None,
        pkcs11_required_touch_policy=None,
        pkcs11_allow_unverified_touch_policy=False
    ):
        """
        Build a PKCS11RequestSigner.

        `pkcs11_pin` must be provided as `str`.
        `pkcs11_slot` and `pkcs11_key_id` are mutually exclusive.
        `pkcs11_token_label` and `pkcs11_token_serial` are mutually exclusive.
        """
        _validate_token_selection(token_label=pkcs11_token_label, token_serial=pkcs11_token_serial)
        normalized_key_id = _normalize_key_id(pkcs11_key_id)
        if pkcs11_pin is None or not isinstance(pkcs11_pin, str):
            raise TypeError("PKCS#11 PIN must be provided as a string")

        signer = PKCS11RequestSigner(
            client_config['user'],
            client_config['tenancy'],
            pkcs11_pin,
            pkcs11_slot=pkcs11_slot,
            pkcs11_key_id=normalized_key_id,
            pkcs11_token_label=pkcs11_token_label,
            pkcs11_token_serial=pkcs11_token_serial,
            pkcs11_key_id_override=pkcs11_key_id_override,
            pkcs11_module_path=pkcs11_module_path,
            pkcs11_required_touch_policy=pkcs11_required_touch_policy,
            pkcs11_allow_unverified_touch_policy=pkcs11_allow_unverified_touch_policy
        )
        return signer

    @staticmethod
    def get_pkcs11_pin():
        """
        Prompt for a PIN and return it as `str`.
        """
        pin_supplier = (lambda: getpass(prompt='Enter your PKCS#11 PIN: '))
        return pin_supplier()
