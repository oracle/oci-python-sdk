# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

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
from .key_value import KeyValue
from .kubernetes_network_config import KubernetesNetworkConfig
from .node import Node
from .node_error import NodeError
from .node_pool import NodePool
from .node_pool_options import NodePoolOptions
from .node_pool_summary import NodePoolSummary
from .update_cluster_details import UpdateClusterDetails
from .update_node_pool_details import UpdateNodePoolDetails
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
    "KeyValue": KeyValue,
    "KubernetesNetworkConfig": KubernetesNetworkConfig,
    "Node": Node,
    "NodeError": NodeError,
    "NodePool": NodePool,
    "NodePoolOptions": NodePoolOptions,
    "NodePoolSummary": NodePoolSummary,
    "UpdateClusterDetails": UpdateClusterDetails,
    "UpdateNodePoolDetails": UpdateNodePoolDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
