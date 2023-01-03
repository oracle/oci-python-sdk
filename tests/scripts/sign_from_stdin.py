# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import
from oci._vendor import six
from oci._vendor.requests import Request
from oci.signer import inject_missing_headers
import sys

if len(sys.argv) != 2:
    print("Please provide the length of the file to be signed")
    exit(1)

request = Request(url="http://some.domain.com?query=string", data=sys.stdin).prepare()
inject_missing_headers(request, sign_body=True, enforce_content_headers=True)
expected = {
    "host": "some.domain.com",
    "content-type": "application/octet-stream",
    "content-length": sys.argv[1]
}
for header, expected_value in six.iteritems(expected):
    assert request.headers[header] == expected_value
