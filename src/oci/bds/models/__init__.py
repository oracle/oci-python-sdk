# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activate_bds_metastore_configuration_details import ActivateBdsMetastoreConfigurationDetails
from .add_auto_scaling_configuration_details import AddAutoScalingConfigurationDetails
from .add_block_storage_details import AddBlockStorageDetails
from .add_cloud_sql_details import AddCloudSqlDetails
from .add_worker_nodes_details import AddWorkerNodesDetails
from .auto_scale_policy import AutoScalePolicy
from .auto_scale_policy_metric_rule import AutoScalePolicyMetricRule
from .auto_scale_policy_rule import AutoScalePolicyRule
from .auto_scaling_configuration import AutoScalingConfiguration
from .auto_scaling_configuration_summary import AutoScalingConfigurationSummary
from .bds_api_key import BdsApiKey
from .bds_api_key_summary import BdsApiKeySummary
from .bds_instance import BdsInstance
from .bds_instance_summary import BdsInstanceSummary
from .bds_metastore_configuration import BdsMetastoreConfiguration
from .bds_metastore_configuration_summary import BdsMetastoreConfigurationSummary
from .change_bds_instance_compartment_details import ChangeBdsInstanceCompartmentDetails
from .change_shape_details import ChangeShapeDetails
from .change_shape_nodes import ChangeShapeNodes
from .cloud_sql_details import CloudSqlDetails
from .cluster_details import ClusterDetails
from .create_bds_api_key_details import CreateBdsApiKeyDetails
from .create_bds_instance_details import CreateBdsInstanceDetails
from .create_bds_metastore_configuration_details import CreateBdsMetastoreConfigurationDetails
from .create_node_details import CreateNodeDetails
from .default_error import DefaultError
from .kerberos_details import KerberosDetails
from .metric_threshold_rule import MetricThresholdRule
from .network_config import NetworkConfig
from .node import Node
from .remove_auto_scaling_configuration_details import RemoveAutoScalingConfigurationDetails
from .remove_cloud_sql_details import RemoveCloudSqlDetails
from .restart_node_details import RestartNodeDetails
from .test_bds_metastore_configuration_details import TestBdsMetastoreConfigurationDetails
from .test_bds_object_storage_connection_details import TestBdsObjectStorageConnectionDetails
from .update_auto_scaling_configuration_details import UpdateAutoScalingConfigurationDetails
from .update_bds_instance_details import UpdateBdsInstanceDetails
from .update_bds_metastore_configuration_details import UpdateBdsMetastoreConfigurationDetails
from .volume_attachment_detail import VolumeAttachmentDetail
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource

# Maps type names to classes for bds services.
bds_type_mapping = {
    "ActivateBdsMetastoreConfigurationDetails": ActivateBdsMetastoreConfigurationDetails,
    "AddAutoScalingConfigurationDetails": AddAutoScalingConfigurationDetails,
    "AddBlockStorageDetails": AddBlockStorageDetails,
    "AddCloudSqlDetails": AddCloudSqlDetails,
    "AddWorkerNodesDetails": AddWorkerNodesDetails,
    "AutoScalePolicy": AutoScalePolicy,
    "AutoScalePolicyMetricRule": AutoScalePolicyMetricRule,
    "AutoScalePolicyRule": AutoScalePolicyRule,
    "AutoScalingConfiguration": AutoScalingConfiguration,
    "AutoScalingConfigurationSummary": AutoScalingConfigurationSummary,
    "BdsApiKey": BdsApiKey,
    "BdsApiKeySummary": BdsApiKeySummary,
    "BdsInstance": BdsInstance,
    "BdsInstanceSummary": BdsInstanceSummary,
    "BdsMetastoreConfiguration": BdsMetastoreConfiguration,
    "BdsMetastoreConfigurationSummary": BdsMetastoreConfigurationSummary,
    "ChangeBdsInstanceCompartmentDetails": ChangeBdsInstanceCompartmentDetails,
    "ChangeShapeDetails": ChangeShapeDetails,
    "ChangeShapeNodes": ChangeShapeNodes,
    "CloudSqlDetails": CloudSqlDetails,
    "ClusterDetails": ClusterDetails,
    "CreateBdsApiKeyDetails": CreateBdsApiKeyDetails,
    "CreateBdsInstanceDetails": CreateBdsInstanceDetails,
    "CreateBdsMetastoreConfigurationDetails": CreateBdsMetastoreConfigurationDetails,
    "CreateNodeDetails": CreateNodeDetails,
    "DefaultError": DefaultError,
    "KerberosDetails": KerberosDetails,
    "MetricThresholdRule": MetricThresholdRule,
    "NetworkConfig": NetworkConfig,
    "Node": Node,
    "RemoveAutoScalingConfigurationDetails": RemoveAutoScalingConfigurationDetails,
    "RemoveCloudSqlDetails": RemoveCloudSqlDetails,
    "RestartNodeDetails": RestartNodeDetails,
    "TestBdsMetastoreConfigurationDetails": TestBdsMetastoreConfigurationDetails,
    "TestBdsObjectStorageConnectionDetails": TestBdsObjectStorageConnectionDetails,
    "UpdateAutoScalingConfigurationDetails": UpdateAutoScalingConfigurationDetails,
    "UpdateBdsInstanceDetails": UpdateBdsInstanceDetails,
    "UpdateBdsMetastoreConfigurationDetails": UpdateBdsMetastoreConfigurationDetails,
    "VolumeAttachmentDetail": VolumeAttachmentDetail,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource
}
