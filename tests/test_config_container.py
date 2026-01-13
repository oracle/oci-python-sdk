# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# A module which holds test configuration information. This is intended to be a shared space where tests
# can figure out what kind of recording (via VCR) is being done and also so that they can take actions (e.g. waiting)
# in a VCR compatible/friendly way

from . import vcr_mods  # noqa: F401

import oci
import time
import vcr

vcr_mode = None
test_mode = None


def using_vcr_with_mock_responses():
    return vcr_mode != 'all'


def create_vcr(**kwargs):
    vcr_to_use = vcr.VCR(
        serializer='yaml',
        cassette_library_dir='tests/fixtures/cassettes',
        record_mode=vcr_mode
    )

    if 'match_on' in kwargs:
        vcr_to_use.match_on = kwargs['match_on']

    return vcr_to_use


# A wrapper around the standard waiter functionality so that if we're mocking responses we don't sleep as we normally
# would (since responses are just going to get returned immediately by VCR anyway)
def do_wait(client, *args, **kwargs):
    if vcr_mode == 'none':
        kwargs['max_interval_seconds'] = 0

    return oci.wait_until(client, *args, **kwargs)


# If we are mocking responses, then we don't need to sleep while waiting
# for a service to get to a particular state
def vcr_sleep(duration):
    if vcr_mode == 'none':
        duration = 0

    time.sleep(duration)
