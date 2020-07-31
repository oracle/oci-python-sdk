# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .add_block_storage_details import AddBlockStorageDetails
from .add_cloud_sql_details import AddCloudSqlDetails
from .add_worker_nodes_details import AddWorkerNodesDetails
from .bds_instance import BdsInstance
from .bds_instance_summary import BdsInstanceSummary
from .change_bds_instance_compartment_details import ChangeBdsInstanceCompartmentDetails
from .change_shape_details import ChangeShapeDetails
from .change_shape_nodes import ChangeShapeNodes
from .cloud_sql_details import CloudSqlDetails
from .cluster_details import ClusterDetails
from .create_bds_instance_details import CreateBdsInstanceDetails
from .create_node_details import CreateNodeDetails
from .default_error import DefaultError
from .kerberos_details import KerberosDetails
from .network_config import NetworkConfig
from .node import Node
from .remove_cloud_sql_details import RemoveCloudSqlDetails
from .restart_node_details import RestartNodeDetails
from .update_bds_instance_details import UpdateBdsInstanceDetails
from .volume_attachment_detail import VolumeAttachmentDetail
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource

# Maps type names to classes for bds services.
bds_type_mapping = {
    "AddBlockStorageDetails": AddBlockStorageDetails,
    "AddCloudSqlDetails": AddCloudSqlDetails,
    "AddWorkerNodesDetails": AddWorkerNodesDetails,
    "BdsInstance": BdsInstance,
    "BdsInstanceSummary": BdsInstanceSummary,
    "ChangeBdsInstanceCompartmentDetails": ChangeBdsInstanceCompartmentDetails,
    "ChangeShapeDetails": ChangeShapeDetails,
    "ChangeShapeNodes": ChangeShapeNodes,
    "CloudSqlDetails": CloudSqlDetails,
    "ClusterDetails": ClusterDetails,
    "CreateBdsInstanceDetails": CreateBdsInstanceDetails,
    "CreateNodeDetails": CreateNodeDetails,
    "DefaultError": DefaultError,
    "KerberosDetails": KerberosDetails,
    "NetworkConfig": NetworkConfig,
    "Node": Node,
    "RemoveCloudSqlDetails": RemoveCloudSqlDetails,
    "RestartNodeDetails": RestartNodeDetails,
    "UpdateBdsInstanceDetails": UpdateBdsInstanceDetails,
    "VolumeAttachmentDetail": VolumeAttachmentDetail,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource
}
