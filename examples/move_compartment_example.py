# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides an example on how to move a compartment to a different compartment
# This script will
#
#    * create cp_source_PYSDK under tenancy
#    * create cp_target_PYSDK under tenancy
#    * move cp_source_PYSDK under cp_target_PYSDK
import time

import oci

config = oci.config.from_file()
identity = oci.identity.IdentityClient(config)
tenancy_id = config["tenancy"]

# Create source compartment
create_compartment_response = identity.create_compartment(
    oci.identity.models.CreateCompartmentDetails(
        compartment_id=tenancy_id,
        name='cp_source_PYSDK',
        description='compartment_source'
    )
)
compartment_source_id = create_compartment_response.data.id
print('Created source compartment: {}'.format(create_compartment_response.data))

# Create target compartment
create_compartment_response = identity.create_compartment(
    oci.identity.models.CreateCompartmentDetails(
        compartment_id=tenancy_id,
        name='cp_target_PYSDK',
        description='compartment_target'
    )
)
compartment_target_id = create_compartment_response.data.id
print('Created target compartment: {}'.format(create_compartment_response.data))

# require a few seconds for system to process
time.sleep(10)

move_compartment_response = identity.move_compartment(
    compartment_source_id,
    oci.identity.models.MoveCompartmentDetails(
        target_compartment_id=compartment_target_id
    )
)

print('Compartment moved successfully')
