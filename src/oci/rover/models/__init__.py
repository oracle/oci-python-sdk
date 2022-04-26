# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_rover_cluster_compartment_details import ChangeRoverClusterCompartmentDetails
from .change_rover_entitlement_compartment_details import ChangeRoverEntitlementCompartmentDetails
from .change_rover_node_compartment_details import ChangeRoverNodeCompartmentDetails
from .create_rover_cluster_details import CreateRoverClusterDetails
from .create_rover_entitlement_details import CreateRoverEntitlementDetails
from .create_rover_node_details import CreateRoverNodeDetails
from .rover_cluster import RoverCluster
from .rover_cluster_certificate import RoverClusterCertificate
from .rover_cluster_collection import RoverClusterCollection
from .rover_cluster_summary import RoverClusterSummary
from .rover_entitlement import RoverEntitlement
from .rover_entitlement_collection import RoverEntitlementCollection
from .rover_entitlement_summary import RoverEntitlementSummary
from .rover_node import RoverNode
from .rover_node_action_set_key_details import RoverNodeActionSetKeyDetails
from .rover_node_certificate import RoverNodeCertificate
from .rover_node_collection import RoverNodeCollection
from .rover_node_encryption_key import RoverNodeEncryptionKey
from .rover_node_get_rpt import RoverNodeGetRpt
from .rover_node_set_key import RoverNodeSetKey
from .rover_node_summary import RoverNodeSummary
from .rover_workload import RoverWorkload
from .shape_collection import ShapeCollection
from .shape_summary import ShapeSummary
from .shipping_address import ShippingAddress
from .update_rover_cluster_details import UpdateRoverClusterDetails
from .update_rover_entitlement_details import UpdateRoverEntitlementDetails
from .update_rover_node_details import UpdateRoverNodeDetails

# Maps type names to classes for rover services.
rover_type_mapping = {
    "ChangeRoverClusterCompartmentDetails": ChangeRoverClusterCompartmentDetails,
    "ChangeRoverEntitlementCompartmentDetails": ChangeRoverEntitlementCompartmentDetails,
    "ChangeRoverNodeCompartmentDetails": ChangeRoverNodeCompartmentDetails,
    "CreateRoverClusterDetails": CreateRoverClusterDetails,
    "CreateRoverEntitlementDetails": CreateRoverEntitlementDetails,
    "CreateRoverNodeDetails": CreateRoverNodeDetails,
    "RoverCluster": RoverCluster,
    "RoverClusterCertificate": RoverClusterCertificate,
    "RoverClusterCollection": RoverClusterCollection,
    "RoverClusterSummary": RoverClusterSummary,
    "RoverEntitlement": RoverEntitlement,
    "RoverEntitlementCollection": RoverEntitlementCollection,
    "RoverEntitlementSummary": RoverEntitlementSummary,
    "RoverNode": RoverNode,
    "RoverNodeActionSetKeyDetails": RoverNodeActionSetKeyDetails,
    "RoverNodeCertificate": RoverNodeCertificate,
    "RoverNodeCollection": RoverNodeCollection,
    "RoverNodeEncryptionKey": RoverNodeEncryptionKey,
    "RoverNodeGetRpt": RoverNodeGetRpt,
    "RoverNodeSetKey": RoverNodeSetKey,
    "RoverNodeSummary": RoverNodeSummary,
    "RoverWorkload": RoverWorkload,
    "ShapeCollection": ShapeCollection,
    "ShapeSummary": ShapeSummary,
    "ShippingAddress": ShippingAddress,
    "UpdateRoverClusterDetails": UpdateRoverClusterDetails,
    "UpdateRoverEntitlementDetails": UpdateRoverEntitlementDetails,
    "UpdateRoverNodeDetails": UpdateRoverNodeDetails
}
