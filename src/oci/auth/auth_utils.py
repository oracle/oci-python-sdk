# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from oci._vendor import six


def get_tenancy_id_from_certificate(cert):
    if not cert:
        raise RuntimeError('A certificate must be provided')

    for name_attribute in cert.subject:
        val = name_attribute.value
        if val.startswith('opc-tenant:'):
            return val[len('opc-tenant:'):]

    raise RuntimeError('The certificate does not contain a tenancy OCID')


def sanitize_certificate_string(cert_string):
    if six.PY3:
        string_to_replace = cert_string.decode('ascii')
    else:
        string_to_replace = cert_string

    return string_to_replace \
        .replace('-----BEGIN CERTIFICATE-----', '') \
        .replace('-----END CERTIFICATE-----', '') \
        .replace('-----BEGIN PUBLIC KEY-----', '') \
        .replace('-----END PUBLIC KEY-----', '') \
        .replace('\n', '')
