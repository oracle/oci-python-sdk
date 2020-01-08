# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .add_on_options import AddOnOptions
from .cluster import Cluster
from .cluster_create_options import ClusterCreateOptions
from .cluster_endpoints import ClusterEndpoints
from .cluster_metadata import ClusterMetadata
from .cluster_options import ClusterOptions
from .cluster_summary import ClusterSummary
from .create_cluster_details import CreateClusterDetails
from .create_cluster_kubeconfig_content_details import CreateClusterKubeconfigContentDetails
from .create_node_pool_details import CreateNodePoolDetails
from .create_node_pool_node_config_details import CreateNodePoolNodeConfigDetails
from .key_value import KeyValue
from .kubernetes_network_config import KubernetesNetworkConfig
from .node import Node
from .node_error import NodeError
from .node_pool import NodePool
from .node_pool_node_config_details import NodePoolNodeConfigDetails
from .node_pool_options import NodePoolOptions
from .node_pool_placement_config_details import NodePoolPlacementConfigDetails
from .node_pool_summary import NodePoolSummary
from .node_source_details import NodeSourceDetails
from .node_source_option import NodeSourceOption
from .node_source_via_image_details import NodeSourceViaImageDetails
from .node_source_via_image_option import NodeSourceViaImageOption
from .update_cluster_details import UpdateClusterDetails
from .update_node_pool_details import UpdateNodePoolDetails
from .update_node_pool_node_config_details import UpdateNodePoolNodeConfigDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for container_engine services.
container_engine_type_mapping = {
    "AddOnOptions": AddOnOptions,
    "Cluster": Cluster,
    "ClusterCreateOptions": ClusterCreateOptions,
    "ClusterEndpoints": ClusterEndpoints,
    "ClusterMetadata": ClusterMetadata,
    "ClusterOptions": ClusterOptions,
    "ClusterSummary": ClusterSummary,
    "CreateClusterDetails": CreateClusterDetails,
    "CreateClusterKubeconfigContentDetails": CreateClusterKubeconfigContentDetails,
    "CreateNodePoolDetails": CreateNodePoolDetails,
    "CreateNodePoolNodeConfigDetails": CreateNodePoolNodeConfigDetails,
    "KeyValue": KeyValue,
    "KubernetesNetworkConfig": KubernetesNetworkConfig,
    "Node": Node,
    "NodeError": NodeError,
    "NodePool": NodePool,
    "NodePoolNodeConfigDetails": NodePoolNodeConfigDetails,
    "NodePoolOptions": NodePoolOptions,
    "NodePoolPlacementConfigDetails": NodePoolPlacementConfigDetails,
    "NodePoolSummary": NodePoolSummary,
    "NodeSourceDetails": NodeSourceDetails,
    "NodeSourceOption": NodeSourceOption,
    "NodeSourceViaImageDetails": NodeSourceViaImageDetails,
    "NodeSourceViaImageOption": NodeSourceViaImageOption,
    "UpdateClusterDetails": UpdateClusterDetails,
    "UpdateNodePoolDetails": UpdateNodePoolDetails,
    "UpdateNodePoolNodeConfigDetails": UpdateNodePoolNodeConfigDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
