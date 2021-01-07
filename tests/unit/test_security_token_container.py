# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci._vendor.jwt as jwt
import oci
import pytest
import time


@pytest.fixture
def valid_for_five_minutes_token():
    time_now = int(time.time())
    payload = {
        'exp': time_now + 300,  # Expires 5 minutes in the future
        'some_data': 'blah blah blah'
    }

    encoded = jwt.encode(payload, 'a_secret')
    return {'exp': time_now, 'token': encoded}


@pytest.fixture
def expired_token():
    time_now = int(time.time())
    payload = {
        'exp': time_now - 300,  # Expired 5 minutes ago
        'some_data': 'blah blah blah'
    }

    encoded = jwt.encode(payload, 'a_secret')
    return {'exp': time_now, 'token': encoded}


def test_valid_without_jitter(valid_for_five_minutes_token):
    security_token_container = oci.auth.security_token_container.SecurityTokenContainer(None, valid_for_five_minutes_token['token'])
    assert security_token_container.valid()


def test_valid_with_jitter(valid_for_five_minutes_token):
    security_token_container = oci.auth.security_token_container.SecurityTokenContainer(None, valid_for_five_minutes_token['token'])
    assert security_token_container.valid_with_jitter(1)
    assert security_token_container.valid_with_jitter()
    assert security_token_container.valid_with_jitter(299)
    assert not security_token_container.valid_with_jitter(301)


def test_invalid_without_jitter(expired_token):
    security_token_container = oci.auth.security_token_container.SecurityTokenContainer(None, expired_token['token'])
    assert not security_token_container.valid()


def test_invalid_with_jitter(expired_token):
    security_token_container = oci.auth.security_token_container.SecurityTokenContainer(None, expired_token['token'])
    assert not security_token_container.valid_with_jitter(1)
    assert not security_token_container.valid_with_jitter()
    assert not security_token_container.valid_with_jitter(299)
    assert not security_token_container.valid_with_jitter(300)
    assert not security_token_container.valid_with_jitter(301)
