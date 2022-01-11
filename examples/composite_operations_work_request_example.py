# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use composite operations via work request service in the Python SDK.
# There's another similar example ./composite_operations_example.py shows how to use composite operations based on
# a resources's states (such as: compute instance's lifecycle states), which internally keep pulling that resource via
# a GET call until the resource's states change to expected one. However, in some other cases, a resource can be impacted
# by many different things or multiple resources are impacted by an operation. A work request service is for that use
# case. For details, please see work request service document here:
# https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/viewingworkrequestcompute.htm
#
# This script demonstrates how to use work request service via composite operations. In particular, how to create an image
#
# The script accepts two arguments:
#   - The first argument is the instance id which you want to use as the basis for the image
#   - The second argument is the target compartment id containing the instance you want to use as the basis for the image

import oci
import sys


def create_image(compute_composite_ops, instance_id, compartment_id):
    # Here we use a composite operation to create a VCN and wait for it to enter the given state. Note that the
    # states are passed as an array so it is possible to wait on multiple states. The waiter will complete
    # (and the method will return) once the resource enters ANY of the provided states.
    create_image_details = oci.core.models.CreateImageDetails()
    create_image_details.instance_id = instance_id
    create_image_details.compartment_id = compartment_id
    work_request_response = compute_composite_ops.create_image_and_wait_for_work_request(
        create_image_details,
    )

    print('{}\n\n'.format(work_request_response.data))


# Default config file and profile
config = oci.config.from_file()
compute_client = oci.core.ComputeClient(config)

# To use different config for work request client, you can init composite operation like:
# work_request_client = oci.work_requests.WorkRequestClient(new_config)
# compute_composite_ops = oci.core.ComputeClientCompositeOperations(client=compute_client, work_request_client=work_request_client)

# if work request client not provided, it will be initialize internally and use config for compute_client
compute_composite_ops = oci.core.ComputeClientCompositeOperations(compute_client)

if len(sys.argv) != 3:
    raise RuntimeError('This script needs to be provided a instance ID and compartment ID')

instance_id = sys.argv[1]
compartment_id = sys.argv[2]

create_image(compute_composite_ops, instance_id, compartment_id)
print('create image operation complete')
