# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .topology_entity_relationship import TopologyEntityRelationship
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopologyAssociatedWithEntityRelationship(TopologyEntityRelationship):
    """
    Defines the `AssociatedWith` relationship between virtual network topology entities. An `AssociatedWith` relationship
    is defined when there is no obvious `contains` relationship but entities are still related.
    For example, a DRG is associated with a VCN because a DRG is not managed by VCN but can be
    attached to a VCN.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TopologyAssociatedWithEntityRelationship object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.TopologyAssociatedWithEntityRelationship.type` attribute
        of this class is ``ASSOCIATED_WITH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id1:
            The value to assign to the id1 property of this TopologyAssociatedWithEntityRelationship.
        :type id1: str

        :param id2:
            The value to assign to the id2 property of this TopologyAssociatedWithEntityRelationship.
        :type id2: str

        :param type:
            The value to assign to the type property of this TopologyAssociatedWithEntityRelationship.
            Allowed values for this property are: "CONTAINS", "ASSOCIATED_WITH", "ROUTES_TO"
        :type type: str

        :param associated_with_details:
            The value to assign to the associated_with_details property of this TopologyAssociatedWithEntityRelationship.
        :type associated_with_details: oci.core.models.TopologyAssociatedWithRelationshipDetails

        """
        self.swagger_types = {
            'id1': 'str',
            'id2': 'str',
            'type': 'str',
            'associated_with_details': 'TopologyAssociatedWithRelationshipDetails'
        }

        self.attribute_map = {
            'id1': 'id1',
            'id2': 'id2',
            'type': 'type',
            'associated_with_details': 'associatedWithDetails'
        }

        self._id1 = None
        self._id2 = None
        self._type = None
        self._associated_with_details = None
        self._type = 'ASSOCIATED_WITH'

    @property
    def associated_with_details(self):
        """
        Gets the associated_with_details of this TopologyAssociatedWithEntityRelationship.

        :return: The associated_with_details of this TopologyAssociatedWithEntityRelationship.
        :rtype: oci.core.models.TopologyAssociatedWithRelationshipDetails
        """
        return self._associated_with_details

    @associated_with_details.setter
    def associated_with_details(self, associated_with_details):
        """
        Sets the associated_with_details of this TopologyAssociatedWithEntityRelationship.

        :param associated_with_details: The associated_with_details of this TopologyAssociatedWithEntityRelationship.
        :type: oci.core.models.TopologyAssociatedWithRelationshipDetails
        """
        self._associated_with_details = associated_with_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
