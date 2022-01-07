# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Example to create record in the dataset
from oci.data_labeling_service_dataplane.data_labeling_client import DataLabelingClient
from oci.data_labeling_service_dataplane.models import CreateObjectStorageSourceDetails
from oci.data_labeling_service_dataplane.models import CreateRecordDetails


def init_dls_dp_client(config, service_endpoint):
    dls_client_dp = DataLabelingClient(config, service_endpoint=service_endpoint)
    return dls_client_dp


# --- Set up
# TODO: Change the below variables
config_file = "<config file>"  # oci.config.from_file('~/.oci/config')

compartment_id = "<compartment ocid>"  # 'ocid1.compartment.oc1..xxxxxxxxxxxxxxxxx'
# dataset_id can be found in create_dataset response under response.data.id
dataset_id = "<dataset ocid>"  # "ocid1.datalabelingdatasetint.oc1.phx.xxxxxx"

# Details of image being sourced from bucket
relative_path = "<relative path of the image w.r.t. bucket>"  # training/banana.jpeg(in case images are placed under
# folder named training) or banana.jpeg(if image is directly uploaded in the bucket)
name = "<image name in bucket>"  # "pineapple.jpeg"

service_endpoint_dp = "https://dlsprod-dp.us-phoenix-1.oci.oraclecloud.com"

dls_client = init_dls_dp_client(config_file, service_endpoint_dp)

source_details_obj = CreateObjectStorageSourceDetails(relative_path=relative_path)

create_record_obj = CreateRecordDetails(name=name,
                                        dataset_id=dataset_id,
                                        compartment_id=compartment_id,
                                        source_details=source_details_obj)
try:
    response = dls_client.create_record(create_record_details=create_record_obj)
    print(response.data)
except Exception as error:
    response = error
    print(response)
