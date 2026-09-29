# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import argparse
import sys
import oci

"""
Example showing how to initialize and use the PKCS#11 signer.

This example shows the PKCS#11 signer being used with the
Objectstorage service.  The instance must be set up for PKCS#11 signing for
this example to work.

The compartment ID defaults to the tenancy OCID below, but can be overridden
when running the example. By default, the signer uses the PIV authentication
object. A PKCS#11 object can also be selected by label or numeric object ID.

python pkcs11_example.py [compartment_id]
python pkcs11_example.py [compartment_id] [--slot "CARD AUTH"]
python pkcs11_example.py [compartment_id] [--slot "PIV AUTH"]
python pkcs11_example.py [compartment_id] [--key-id 1]
python pkcs11_example.py [compartment_id] [--key-id 4]
python pkcs11_example.py [compartment_id] [--token-label "YubiKey PIV"]
python pkcs11_example.py [compartment_id] [--token-serial 12345678]
python pkcs11_example.py [compartment_id] [--module-path /usr/local/lib/libykcs11.dylib]
python pkcs11_example.py [compartment_id] [--profile PYTHONSDK]
"""


parser = argparse.ArgumentParser(description='PKCS#11 signer example')
parser.add_argument(
    'compartment_id',
    nargs='?',
    help='OCI compartment OCID to pass to the GetNamespace call.'
)
key_selection = parser.add_mutually_exclusive_group()
key_selection.add_argument(
    '--slot',
    dest='slot',
    default=None,
    help=(
        'PKCS#11 object label. Examples: "PIV AUTH"/"9A" (default when no key ID is provided), '
        '"CARD AUTH"/"9E", or a token label such as "PIV AUTH".'
    )
)
key_selection.add_argument(
    '--key-id',
    dest='key_id',
    help=(
        'PKCS#11 numeric object ID. Examples: 1 for PIV AUTH, 4 for CARD AUTH.'
    )
)
token_selection = parser.add_mutually_exclusive_group()
token_selection.add_argument(
    '--token-label',
    dest='token_label',
    default=None,
    help='PKCS#11 token label to use when multiple tokens are present.'
)
token_selection.add_argument(
    '--token-serial',
    dest='token_serial',
    default=None,
    help='PKCS#11 token serial number to use when multiple tokens are present.'
)
parser.add_argument(
    '--module-path',
    dest='module_path',
    default=None,
    help='PKCS#11 module path. If omitted, the signer searches common module paths.'
)
parser.add_argument(
    '--key-id-override',
    dest='key_id_override',
    default=None,
    help='Override the OCI API key ID instead of using tenancy/user/fingerprint.'
)
parser.add_argument(
    '--profile',
    dest='profile',
    default=None,
    help='OCI configuration profile to use. Defaults to the DEFAULT profile.'
)
args = parser.parse_args()


def _normalize_args(parsed_args):
    if parsed_args.slot and parsed_args.compartment_id:
        combined_slot = '{} {}'.format(parsed_args.slot, parsed_args.compartment_id)
        if combined_slot.upper() in ('PIV AUTH', 'CARD AUTH'):
            parsed_args.slot = combined_slot
            parsed_args.compartment_id = None


_normalize_args(args)


try:
    from oci.auth.signers.pkcs11_signer import PKCS11RequestSigner
except (ImportError, ModuleNotFoundError) as e:
    missing_module = getattr(e, "name", "") or ""
    if missing_module == "pkcs11" or missing_module.startswith("pkcs11."):
        print("Failed to import PKCS#11 signer: python-pkcs11 is not installed in this Python environment.")
    else:
        print("Failed to import PKCS#11 signer from the OCI SDK being used: {}".format(str(e)))
        print("Run this example against the local checkout with: PYTHONPATH=src python examples/pkcs11_example.py")
    sys.exit(1)


def _is_card_auth_slot(slot):
    if slot is None:
        return False

    normalized_slot = slot.strip().upper().replace('_', ' ').replace('-', ' ')
    return normalized_slot in ('CARD', 'CARD AUTH', '9E')


def _is_card_auth_key_id(key_id):
    if key_id is None:
        return False

    normalized_key_id = key_id.strip().lower()
    return normalized_key_id in ('4', '04', '0x04')


def _format_pkcs11_error(error):
    error_message = str(error).strip()
    error_name = error.__class__.__name__
    details_by_error_name = {
        'PinLenRange': 'The PIN length is outside the range accepted by the token.',
        'PinIncorrect': 'The PIN was rejected by the token.',
        'PinInvalid': 'The PIN was rejected by the token.',
        'PinLocked': 'The PIN is locked on the token.',
        'PinExpired': 'The PIN is expired on the token.',
        'NoSuchKey': 'The selected PKCS#11 key was not found on the token.',
        'GeneralError': 'The token rejected the signing operation. Touch the YubiKey when it blinks during signing.',
        'OperationNotInitialized': 'The token rejected context-specific authentication for this signing operation.',
        'UserNotLoggedIn': 'The selected PKCS#11 key requires user login before signing.',
    }

    if error_message:
        return '{}: {}'.format(error_name, error_message)

    return '{}: {}'.format(
        error_name,
        details_by_error_name.get(error_name, 'PKCS#11 operation failed without an error message.')
    )


def _resolve_pkcs11_slot(parsed_args):
    if parsed_args.key_id:
        return None

    return parsed_args.slot


def _uses_card_auth(pkcs11_slot, key_id):
    return _is_card_auth_slot(pkcs11_slot) or _is_card_auth_key_id(key_id)


def _get_pkcs11_authentication_input(card_auth_selected):
    if card_auth_selected:
        print("CARD AUTH selected. Enter your PKCS#11 PIN once to initialize the signer.")
        print("Subsequent signing requests use the cached PIN and require only the token touch.")
        print("Touch policy ALWAYS is verified when attestation is available; older firmware uses compatibility mode.")

    try:
        pkcs11_pin = PKCS11RequestSigner.get_pkcs11_pin()
    except (KeyboardInterrupt, EOFError):
        print("\nPKCS#11 PIN entry was cancelled. Exiting.")
        sys.exit(1)
    except OSError as e:
        print("Failed to read PKCS#11 PIN: {}".format(str(e)))
        sys.exit(1)

    if not pkcs11_pin:
        print("PKCS#11 PIN cannot be empty. Exiting.")
        sys.exit(1)

    return pkcs11_pin


def _build_pkcs11_request_signer(config, parsed_args, pkcs11_slot, pkcs11_pin):
    try:
        return PKCS11RequestSigner.get_pkcs11_signer(
            config,
            pkcs11_pin,
            pkcs11_slot=pkcs11_slot,
            pkcs11_key_id=parsed_args.key_id,
            pkcs11_token_label=parsed_args.token_label,
            pkcs11_token_serial=parsed_args.token_serial,
            pkcs11_key_id_override=parsed_args.key_id_override,
            pkcs11_module_path=parsed_args.module_path,
            pkcs11_required_touch_policy=(
                'always' if _uses_card_auth(pkcs11_slot, parsed_args.key_id) else None
            ),
            pkcs11_allow_unverified_touch_policy=_uses_card_auth(
                pkcs11_slot, parsed_args.key_id
            )
        )
    except (RuntimeError, ValueError, OSError) as e:
        print("Failed to initialize PKCS#11 signer: {}".format(_format_pkcs11_error(e)))
        sys.exit(1)


def _get_object_storage_namespace(config, pkcs11_signer, card_auth_selected, compartment_id):
    print("=" * 80)
    print("Get Objectstorage namespace")
    object_storage_client = oci.object_storage.ObjectStorageClient(config, signer=pkcs11_signer)
    try:
        if card_auth_selected:
            print("Touch your YubiKey when it blinks to sign the Object Storage request.", flush=True)
        if compartment_id:
            print(object_storage_client.get_namespace(compartment_id=compartment_id).data)
        else:
            print(object_storage_client.get_namespace().data)
    except RuntimeError as e:
        if e.__class__.__module__.startswith('pkcs11'):
            print("Failed to sign request with PKCS#11 signer: {}".format(_format_pkcs11_error(e)))
            sys.exit(1)

        raise


def main():
    pkcs11_slot = _resolve_pkcs11_slot(args)
    card_auth_selected = _uses_card_auth(pkcs11_slot, args.key_id)

    print("Initializing new signer", flush=True)
    config = (
        oci.config.from_file(profile_name=args.profile)
        if args.profile else oci.config.from_file()
    )
    pkcs11_pin = _get_pkcs11_authentication_input(card_auth_selected)
    pkcs11_signer = _build_pkcs11_request_signer(config, args, pkcs11_slot, pkcs11_pin)

    print("Using PKCS#11 key {}".format(pkcs11_signer.pkcs11_signer.selected_key_description()))
    _get_object_storage_namespace(config, pkcs11_signer, card_auth_selected, args.compartment_id)
    # Making this call or any subsequent calls again will only ask for yubikey touch and not the pin again, as the pin is cached in memory for the lifetime of the signer.
    _get_object_storage_namespace(config, pkcs11_signer, card_auth_selected, args.compartment_id)


if __name__ == '__main__':
    main()
