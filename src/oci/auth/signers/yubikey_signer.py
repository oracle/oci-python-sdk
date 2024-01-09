# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import base64
import pkcs11
import urllib
import hashlib
import platform
import threading
from oci.auth import signers
from pkcs11.constants import Attribute
from pkcs11.mechanisms import Mechanism
from getpass import getpass
import oci.signer

system = platform.system()

platforms = {
    "Darwin": "/usr/local/lib/opensc-pkcs11.so",
    "Linux": "/usr/lib64/pkcs11/opensc-pkcs11.so",
}

if system == 'Darwin':
    provider = platforms["Darwin"]
elif system == 'Linux':
    provider = platforms["Linux"]
else:
    raise RuntimeError('Unsupported platform {}'.format(system))


class Yubikey:
    lock = threading.Lock()

    def __init__(self, pin):
        self.pin = pin

        with self.lock:
            self.lib = pkcs11.lib(provider)
            self.token = self.lib.get_token()

            with self.token.open(user_pin=self.pin) as session:
                key = session.get_key(label='PIV AUTH pubkey')
                hasher = hashlib.md5()

                hasher.update(key[Attribute.VALUE])
                digest = hasher.hexdigest()

                self.fingerprint = ':'.join(a + b for a, b in zip(digest[::2], digest[1::2]))

    def sign(self, data, mechanism=Mechanism.SHA256_RSA_PKCS):
        with self.lock, self.token.open(user_pin=self.pin) as session:
            key = session.get_key(label='PIV AUTH key')

            return key.sign(data, mechanism=mechanism)

    def verify(self, data, signature, mechanism=Mechanism.SHA256_RSA_PKCS):
        with self.lock, self.token.open(user_pin=self.pin) as session:
            key = session.get_key(label='PIV AUTH pubkey')

            return key.verify(data, signature, mechanism=mechanism)


class YubikeyRequestSigner(signers.SecurityTokenSigner):
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
        'post': generic_headers + body_headers
    }

    def __init__(self, user, tenancy, pin):
        self.yubikey = Yubikey(pin)
        self.keyid = '{}/{}/{}'.format(tenancy, user, self.yubikey.fingerprint)

    def sign(self, request):
        verb = request.method.lower()
        host = urllib.parse.urlparse(request.url).netloc
        path = request.path_url
        values = []

        for header in self.required_headers[verb]:
            header = header.lower()

            if header == '(request-target)':
                values.append('{}: {} {}'.format(header, verb, path))
            elif header == 'host':
                values.append('{}: {}'.format(header, host))
            elif header == 'date':
                values.append('{}: {}'.format(header, request.headers.get('date')))
            else:
                values.append('{}: {}'.format(header, request.headers.get(header)))

        data = '\n'.join(values).encode('ascii')
        signature = self.yubikey.sign(data)

        return {
            'authorization': 'Signature keyId="{}",version="{}",algorithm="{}",headers="{}",signature="{}"'.format(
                self.keyid,
                '1',
                'rsa-sha256',
                ' '.join(self.required_headers[verb]),
                base64.b64encode(signature).decode('ascii')
            )
        }

    def __call__(self, request):
        verb = request.method.lower()

        if verb == 'options':
            return request

        oci.signer.inject_missing_headers(request, verb in ['put', 'post'], enforce_content_headers=True)
        auth_header = self.sign(request)
        request.headers.update(auth_header)
        return request

    def get_yubikey_signer(client_config, ykpin):
        signer = YubikeyRequestSigner(
            client_config['user'],
            client_config['tenancy'],
            ykpin
        )
        return signer

    def get_yubikey_pin():
        ykpin_supplier = (lambda: getpass(prompt='Enter your yubikey pin: '))
        ykpin = ykpin_supplier()
        return ykpin
