# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.util import extract_service_endpoint


def test_extract_service_endpoint():
    assert extract_service_endpoint('https://foo.bar.com/whatever/path') == 'https://foo.bar.com'
    assert extract_service_endpoint('https://foo.bar.com') == 'https://foo.bar.com'
    assert extract_service_endpoint('https://foo.bar.com/123456') == 'https://foo.bar.com'
    assert extract_service_endpoint('https://my.fake.endpoint') == 'https://my.fake.endpoint'
    assert extract_service_endpoint('https://foo.bar.com:80/123456') == 'https://foo.bar.com:80'
    assert extract_service_endpoint('https://foo.bar.co.uk/123456') == 'https://foo.bar.co.uk'
    assert extract_service_endpoint('https://foo.bar.co.uk:80/123456') == 'https://foo.bar.co.uk:80'
