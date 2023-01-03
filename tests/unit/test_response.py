# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci


def test_response():
    status = "mystatus"
    headers = {'h1': 'h1val', 'opc-next-page': 'next!', 'opc-request-id': 'myid'}
    data = 'testdata'
    request = oci.Request(
        'method',
        'url',
        'query_params',
        'header_params',
        'body',
        'response_type'
    )

    response = oci.Response(status, headers, data, request)

    assert status == response.status
    assert 'h1val' == response.headers['h1']
    assert 'next!' == response.next_page
    assert 'myid' == response.request_id
    assert response.has_next_page is True


def test_response_none_headers():
    status = "mystatus"
    headers = None
    data = 'testdata'

    response = oci.Response(status, headers, data, None)

    assert status == response.status
    assert response.next_page is None
    assert response.request_id is None
    assert response.has_next_page is False


def test_response_empty_headers():
    status = "mystatus"
    headers = {}
    data = 'testdata'

    response = oci.Response(status, headers, data, None)

    assert status == response.status
    assert response.next_page is None
    assert response.request_id is None
    assert response.has_next_page is False
