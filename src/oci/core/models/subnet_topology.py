# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .topology import Topology
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubnetTopology(Topology):
    """
    Defines the visualization of a subnet in a VCN.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubnetTopology object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.SubnetTopology.type` attribute
        of this class is ``SUBNET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this SubnetTopology.
            Allowed values for this property are: "NETWORKING", "VCN", "SUBNET", "PATH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param entities:
            The value to assign to the entities property of this SubnetTopology.
        :type entities: list[object]

        :param relationships:
            The value to assign to the relationships property of this SubnetTopology.
        :type relationships: list[oci.core.models.TopologyEntityRelationship]

        :param time_created:
            The value to assign to the time_created property of this SubnetTopology.
        :type time_created: datetime

        :param subnet_id:
            The value to assign to the subnet_id property of this SubnetTopology.
        :type subnet_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'entities': 'list[object]',
            'relationships': 'list[TopologyEntityRelationship]',
            'time_created': 'datetime',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'entities': 'entities',
            'relationships': 'relationships',
            'time_created': 'timeCreated',
            'subnet_id': 'subnetId'
        }

        self._type = None
        self._entities = None
        self._relationships = None
        self._time_created = None
        self._subnet_id = None
        self._type = 'SUBNET'

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this SubnetTopology.
        The `OCID`__ of the subnet for which the visualization is generated.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this SubnetTopology.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this SubnetTopology.
        The `OCID`__ of the subnet for which the visualization is generated.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this SubnetTopology.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
