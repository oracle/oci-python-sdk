# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import warnings

from oci.base_client import OCIHTTPAdapter


def test_oci_http_adapter_does_not_emit_urllib3_strict_future_warning():
    with warnings.catch_warnings(record=True) as caught_warnings:
        warnings.simplefilter("always", FutureWarning)

        adapter = OCIHTTPAdapter()
        adapter.poolmanager.connection_from_url("https://objectstorage.us-phoenix-1.oraclecloud.com")

    strict_future_warnings = [
        warning for warning in caught_warnings
        if issubclass(warning.category, FutureWarning) and
        "'strict' parameter is no longer needed" in str(warning.message)
    ]

    assert strict_future_warnings == []
