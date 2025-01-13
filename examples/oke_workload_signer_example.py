# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci

oke_workload_signer = oci.auth.signers.get_oke_workload_identity_resource_principal_signer()

# If you have a kubernetes service account token path different from the default path then:
# token_path = "path_to_your_token_file"
# oke_workload_signer = oci.auth.signers.get_oke_workload_identity_resource_principal_signer(service_account_token_path=token_path)

# If you want to directly pass in the kubernetes service account token then:
# token_string = "your_token_string"
# oke_workload_signer = oci.auth.signers.get_oke_workload_identity_resource_principal_signer(service_account_token=token_string)

# A populated config is not needed when using the OKE Workload Auth signer
container_engine_client = oci.container_engine.ContainerEngineClient({}, signer=oke_workload_signer)

create_cluster_response = container_engine_client.create_cluster(
    create_cluster_details=oci.container_engine.models.CreateClusterDetails(
        name="name_of_your_cluster",
        compartment_id="ocid_of_your_compartment",
        vcn_id="ocid_of_your_vcn",
        kubernetes_version="choice_of_kubernetes_version"
    )
)
print(create_cluster_response.data)

get_cluster_response = container_engine_client.get_cluster(
    cluster_id="ocid_of_your_cluster_id"
)
print(get_cluster_response.data.lifecycle_state)
