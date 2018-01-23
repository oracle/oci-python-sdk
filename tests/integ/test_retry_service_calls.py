# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

# Sanity test that we can pass a retry strategy to a service call and it can succeed

import oci
import pytest

from . import util
from .. import test_config_container


@pytest.mark.skip(reason='Waiting for codegen change')
def test_create_volume(block_storage):
    volume_id = None

    try:
        volume_name_gbs = util.random_name('python_sdk_test_volume_gb')
        create_volume_details = oci.core.models.CreateVolumeDetails()
        create_volume_details.availability_domain = util.availability_domain()
        create_volume_details.compartment_id = util.COMPARTMENT_ID
        create_volume_details.display_name = volume_name_gbs
        create_volume_details.size_in_gbs = 50

        result = block_storage.create_volume(create_volume_details, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

        util.validate_response(result)
        volume_id = result.data.id
        test_config_container.do_wait(block_storage, block_storage.get_volume(volume_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=180)
    finally:
        if volume_id:
            block_storage.delete_volume(volume_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
            test_config_container.do_wait(block_storage, block_storage.get_volume(volume_id), 'lifecycle_state', 'TERMINATED', max_interval_seconds=180, succeed_on_not_found=True)
