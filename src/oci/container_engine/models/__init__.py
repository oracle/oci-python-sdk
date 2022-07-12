# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .add_on_options import AddOnOptions
from .admission_controller_options import AdmissionControllerOptions
from .cluster import Cluster
from .cluster_create_options import ClusterCreateOptions
from .cluster_endpoint_config import ClusterEndpointConfig
from .cluster_endpoints import ClusterEndpoints
from .cluster_metadata import ClusterMetadata
from .cluster_migrate_to_native_vcn_details import ClusterMigrateToNativeVcnDetails
from .cluster_migrate_to_native_vcn_status import ClusterMigrateToNativeVcnStatus
from .cluster_options import ClusterOptions
from .cluster_pod_network_option_details import ClusterPodNetworkOptionDetails
from .cluster_summary import ClusterSummary
from .create_cluster_details import CreateClusterDetails
from .create_cluster_endpoint_config_details import CreateClusterEndpointConfigDetails
from .create_cluster_kubeconfig_content_details import CreateClusterKubeconfigContentDetails
from .create_image_policy_config_details import CreateImagePolicyConfigDetails
from .create_node_pool_details import CreateNodePoolDetails
from .create_node_pool_node_config_details import CreateNodePoolNodeConfigDetails
from .create_node_shape_config_details import CreateNodeShapeConfigDetails
from .flannel_overlay_cluster_pod_network_option_details import FlannelOverlayClusterPodNetworkOptionDetails
from .flannel_overlay_node_pool_pod_network_option_details import FlannelOverlayNodePoolPodNetworkOptionDetails
from .image_policy_config import ImagePolicyConfig
from .key_details import KeyDetails
from .key_value import KeyValue
from .kubernetes_network_config import KubernetesNetworkConfig
from .node import Node
from .node_error import NodeError
from .node_eviction_node_pool_settings import NodeEvictionNodePoolSettings
from .node_pool import NodePool
from .node_pool_node_config_details import NodePoolNodeConfigDetails
from .node_pool_options import NodePoolOptions
from .node_pool_placement_config_details import NodePoolPlacementConfigDetails
from .node_pool_pod_network_option_details import NodePoolPodNetworkOptionDetails
from .node_pool_summary import NodePoolSummary
from .node_shape_config import NodeShapeConfig
from .node_source_details import NodeSourceDetails
from .node_source_option import NodeSourceOption
from .node_source_via_image_details import NodeSourceViaImageDetails
from .node_source_via_image_option import NodeSourceViaImageOption
from .oci_vcn_ip_native_cluster_pod_network_option_details import OciVcnIpNativeClusterPodNetworkOptionDetails
from .oci_vcn_ip_native_node_pool_pod_network_option_details import OciVcnIpNativeNodePoolPodNetworkOptionDetails
from .persistent_volume_config_details import PersistentVolumeConfigDetails
from .service_lb_config_details import ServiceLbConfigDetails
from .update_cluster_details import UpdateClusterDetails
from .update_cluster_endpoint_config_details import UpdateClusterEndpointConfigDetails
from .update_cluster_options_details import UpdateClusterOptionsDetails
from .update_image_policy_config_details import UpdateImagePolicyConfigDetails
from .update_node_pool_details import UpdateNodePoolDetails
from .update_node_pool_node_config_details import UpdateNodePoolNodeConfigDetails
from .update_node_shape_config_details import UpdateNodeShapeConfigDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for container_engine services.
container_engine_type_mapping = {
    "AddOnOptions": AddOnOptions,
    "AdmissionControllerOptions": AdmissionControllerOptions,
    "Cluster": Cluster,
    "ClusterCreateOptions": ClusterCreateOptions,
    "ClusterEndpointConfig": ClusterEndpointConfig,
    "ClusterEndpoints": ClusterEndpoints,
    "ClusterMetadata": ClusterMetadata,
    "ClusterMigrateToNativeVcnDetails": ClusterMigrateToNativeVcnDetails,
    "ClusterMigrateToNativeVcnStatus": ClusterMigrateToNativeVcnStatus,
    "ClusterOptions": ClusterOptions,
    "ClusterPodNetworkOptionDetails": ClusterPodNetworkOptionDetails,
    "ClusterSummary": ClusterSummary,
    "CreateClusterDetails": CreateClusterDetails,
    "CreateClusterEndpointConfigDetails": CreateClusterEndpointConfigDetails,
    "CreateClusterKubeconfigContentDetails": CreateClusterKubeconfigContentDetails,
    "CreateImagePolicyConfigDetails": CreateImagePolicyConfigDetails,
    "CreateNodePoolDetails": CreateNodePoolDetails,
    "CreateNodePoolNodeConfigDetails": CreateNodePoolNodeConfigDetails,
    "CreateNodeShapeConfigDetails": CreateNodeShapeConfigDetails,
    "FlannelOverlayClusterPodNetworkOptionDetails": FlannelOverlayClusterPodNetworkOptionDetails,
    "FlannelOverlayNodePoolPodNetworkOptionDetails": FlannelOverlayNodePoolPodNetworkOptionDetails,
    "ImagePolicyConfig": ImagePolicyConfig,
    "KeyDetails": KeyDetails,
    "KeyValue": KeyValue,
    "KubernetesNetworkConfig": KubernetesNetworkConfig,
    "Node": Node,
    "NodeError": NodeError,
    "NodeEvictionNodePoolSettings": NodeEvictionNodePoolSettings,
    "NodePool": NodePool,
    "NodePoolNodeConfigDetails": NodePoolNodeConfigDetails,
    "NodePoolOptions": NodePoolOptions,
    "NodePoolPlacementConfigDetails": NodePoolPlacementConfigDetails,
    "NodePoolPodNetworkOptionDetails": NodePoolPodNetworkOptionDetails,
    "NodePoolSummary": NodePoolSummary,
    "NodeShapeConfig": NodeShapeConfig,
    "NodeSourceDetails": NodeSourceDetails,
    "NodeSourceOption": NodeSourceOption,
    "NodeSourceViaImageDetails": NodeSourceViaImageDetails,
    "NodeSourceViaImageOption": NodeSourceViaImageOption,
    "OciVcnIpNativeClusterPodNetworkOptionDetails": OciVcnIpNativeClusterPodNetworkOptionDetails,
    "OciVcnIpNativeNodePoolPodNetworkOptionDetails": OciVcnIpNativeNodePoolPodNetworkOptionDetails,
    "PersistentVolumeConfigDetails": PersistentVolumeConfigDetails,
    "ServiceLbConfigDetails": ServiceLbConfigDetails,
    "UpdateClusterDetails": UpdateClusterDetails,
    "UpdateClusterEndpointConfigDetails": UpdateClusterEndpointConfigDetails,
    "UpdateClusterOptionsDetails": UpdateClusterOptionsDetails,
    "UpdateImagePolicyConfigDetails": UpdateImagePolicyConfigDetails,
    "UpdateNodePoolDetails": UpdateNodePoolDetails,
    "UpdateNodePoolNodeConfigDetails": UpdateNodePoolNodeConfigDetails,
    "UpdateNodeShapeConfigDetails": UpdateNodeShapeConfigDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
