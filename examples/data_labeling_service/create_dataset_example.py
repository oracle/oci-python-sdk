# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Example to create Dataset in Data Labeling Service
from oci.data_labeling_service.data_labeling_management_client import DataLabelingManagementClient
from oci.data_labeling_service.models import ObjectStorageSourceDetails
from oci.data_labeling_service.models import DatasetFormatDetails
from oci.data_labeling_service.models import LabelSet
from oci.data_labeling_service.models import Label
from oci.data_labeling_service.models import CreateDatasetDetails


def init_dls_cp_client(config, service_endpoint):
    dls_client_cp = DataLabelingManagementClient(config,
                                                 service_endpoint=service_endpoint)
    return dls_client_cp


# --- Set up
# TODO: Change the below variables
config_file = "<config file>"  # oci.config.from_file('~/.oci/config')

compartment_id = "<compartment ocid>"  # 'ocid1.compartment.oc1..xxxxxxxxxxxxxxxxx'
namespace = "<object storage bucket namespace>"  # 'idgszs0xipnv'
bucket = "<object storage bucket name>"  # 'testing_bucket'

format_type = "IMAGE"
annotation_format = "BOUNDING_BOX"
label1 = "apple"
label2 = "orange"

service_endpoint_cp = "https://dlsprod-cp.us-phoenix-1.oci.oraclecloud.com"

dls_client = init_dls_cp_client(config_file, service_endpoint_cp)

dataset_source_details_obj = ObjectStorageSourceDetails(namespace=namespace, bucket=bucket)

dataset_format_details_obj = DatasetFormatDetails(format_type=format_type)

label_set_obj = LabelSet(items=[Label(name=label1), Label(name=label2)])

create_dataset_obj = CreateDatasetDetails(compartment_id=compartment_id, annotation_format=annotation_format,
                                          dataset_source_details=dataset_source_details_obj,
                                          dataset_format_details=dataset_format_details_obj,
                                          label_set=label_set_obj)
try:
    response = dls_client.create_dataset(create_dataset_details=create_dataset_obj)
    print(response.data)
except Exception as error:
    response = error
    print(response)
