# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci._vendor.requests.models import Request
from oci._vendor.requests.sessions import Session, HTTPAdapter


def test_add_headers():
    headers = {
        'accept': 'application/json',
        'opc-client-info': 'Oracle-PythonSDK/2.11.1+preview+1',
        'user-agent': 'Oracle-PythonSDK/2.11.1+preview.1 (python 3.6.5; x86_64-Darwin)',
        'opc-request-id': '996FE54D0755404BA477E4CC852819F0'
    }
    request = Request(
        method="POST",
        url='https://datascience.us-phoenix-1.oci.oraclecloud.com/20190101/models/ocid1.datasciencemodel.oc1.phx.amaaaaaaev43fkiaswn7lo3fgcyc3wke3rbcxenp7x4pjtkgw2u65ob2wv7q/artifact',
        headers=headers
    )
    session = Session()
    adapter = HTTPAdapter()
    prepared_request = session.prepare_request(request)
    adapter.add_headers(prepared_request)
    assert prepared_request.headers['content-type'] == 'application/octet-stream'
