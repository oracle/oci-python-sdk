# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopologyEntityRelationship(object):
    """
    Defines the relationship between Virtual Network topology entities.
    """

    #: A constant which can be used with the type property of a TopologyEntityRelationship.
    #: This constant has a value of "CONTAINS"
    TYPE_CONTAINS = "CONTAINS"

    #: A constant which can be used with the type property of a TopologyEntityRelationship.
    #: This constant has a value of "ASSOCIATED_WITH"
    TYPE_ASSOCIATED_WITH = "ASSOCIATED_WITH"

    #: A constant which can be used with the type property of a TopologyEntityRelationship.
    #: This constant has a value of "ROUTES_TO"
    TYPE_ROUTES_TO = "ROUTES_TO"

    def __init__(self, **kwargs):
        """
        Initializes a new TopologyEntityRelationship object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.vn_monitoring.models.TopologyRoutesToEntityRelationship`
        * :class:`~oci.vn_monitoring.models.TopologyAssociatedWithEntityRelationship`
        * :class:`~oci.vn_monitoring.models.TopologyContainsEntityRelationship`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id1:
            The value to assign to the id1 property of this TopologyEntityRelationship.
        :type id1: str

        :param id2:
            The value to assign to the id2 property of this TopologyEntityRelationship.
        :type id2: str

        :param type:
            The value to assign to the type property of this TopologyEntityRelationship.
            Allowed values for this property are: "CONTAINS", "ASSOCIATED_WITH", "ROUTES_TO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'id1': 'str',
            'id2': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'id1': 'id1',
            'id2': 'id2',
            'type': 'type'
        }

        self._id1 = None
        self._id2 = None
        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'ROUTES_TO':
            return 'TopologyRoutesToEntityRelationship'

        if type == 'ASSOCIATED_WITH':
            return 'TopologyAssociatedWithEntityRelationship'

        if type == 'CONTAINS':
            return 'TopologyContainsEntityRelationship'
        else:
            return 'TopologyEntityRelationship'

    @property
    def id1(self):
        """
        **[Required]** Gets the id1 of this TopologyEntityRelationship.
        The `OCID`__ of the first entity in the relationship.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id1 of this TopologyEntityRelationship.
        :rtype: str
        """
        return self._id1

    @id1.setter
    def id1(self, id1):
        """
        Sets the id1 of this TopologyEntityRelationship.
        The `OCID`__ of the first entity in the relationship.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id1: The id1 of this TopologyEntityRelationship.
        :type: str
        """
        self._id1 = id1

    @property
    def id2(self):
        """
        **[Required]** Gets the id2 of this TopologyEntityRelationship.
        The `OCID`__ of the second entity in the relationship.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id2 of this TopologyEntityRelationship.
        :rtype: str
        """
        return self._id2

    @id2.setter
    def id2(self, id2):
        """
        Sets the id2 of this TopologyEntityRelationship.
        The `OCID`__ of the second entity in the relationship.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id2: The id2 of this TopologyEntityRelationship.
        :type: str
        """
        self._id2 = id2

    @property
    def type(self):
        """
        **[Required]** Gets the type of this TopologyEntityRelationship.
        The type of relationship between the entities.

        Allowed values for this property are: "CONTAINS", "ASSOCIATED_WITH", "ROUTES_TO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this TopologyEntityRelationship.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TopologyEntityRelationship.
        The type of relationship between the entities.


        :param type: The type of this TopologyEntityRelationship.
        :type: str
        """
        allowed_values = ["CONTAINS", "ASSOCIATED_WITH", "ROUTES_TO"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
