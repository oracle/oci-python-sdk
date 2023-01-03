# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Example to annotate record in the dataset
from oci.data_labeling_service_dataplane.data_labeling_client import DataLabelingClient
from oci.data_labeling_service_dataplane.models import Label
from oci.data_labeling_service_dataplane.models import ImageObjectSelectionEntity
from oci.data_labeling_service_dataplane.models import NormalizedVertex
from oci.data_labeling_service_dataplane.models import BoundingPolygon
from oci.data_labeling_service_dataplane.models import CreateAnnotationDetails


def init_dls_dp_client(config, service_endpoint):
    dls_client_dp = DataLabelingClient(config, service_endpoint=service_endpoint)
    return dls_client_dp


# --- Set up
# TODO: Change the below variables
config_file = "<config file>"  # oci.config.from_file('~/.oci/config')

compartment_id = "<compartment ocid>"  # 'ocid1.compartment.oc1..xxxxxxxxxxxxxxxxx'
# dataset_id can be found in create_record response under response.data.id
record_id = "<record ocid>"  # "ocid1.datalabelingdatasetint.oc1.phx.xxxxxx"

label = "<label of annotation>"  # "apple"
entity_type = "IMAGEOBJECTSELECTION"

# Co-ordinates of bounding box
x_coordinates = [0.030035335689045935, 0.030035335689045935, 0.2826855123674912, 0.2826855123674912]
y_coordinates = [0.13743816254416963, 0.3969434628975265, 0.3969434628975265, 0.13743816254416963]

service_endpoint_dp = "https://dlsprod-dp.us-phoenix-1.oci.oraclecloud.com"


labels_obj = [Label(label=label)]

normalized_vector_obj_lst = []
for i in range(len(x_coordinates)):
    normalized_vector_obj = NormalizedVertex(x=x_coordinates[i], y=y_coordinates[i])
    normalized_vector_obj_lst.append(normalized_vector_obj)

bounding_polygon_obj = BoundingPolygon(normalized_vertices=normalized_vector_obj_lst)

entity_obj = [ImageObjectSelectionEntity(entity_type=entity_type, labels=labels_obj,
                                         bounding_polygon=bounding_polygon_obj)]

create_annotation_details_obj = CreateAnnotationDetails(record_id=record_id, compartment_id=compartment_id,
                                                        entities=entity_obj)


dls_client = init_dls_dp_client(config_file, service_endpoint_dp)

try:
    response = dls_client.create_annotation(create_annotation_details=create_annotation_details_obj)
    print(response.data)
except Exception as error:
    response = error
    print(response)
