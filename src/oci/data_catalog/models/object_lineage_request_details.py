# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190325


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectLineageRequestDetails(object):
    """
    Details needed by a lineage fetch request.
    """

    #: A constant which can be used with the direction property of a ObjectLineageRequestDetails.
    #: This constant has a value of "UPSTREAM"
    DIRECTION_UPSTREAM = "UPSTREAM"

    #: A constant which can be used with the direction property of a ObjectLineageRequestDetails.
    #: This constant has a value of "BOTH"
    DIRECTION_BOTH = "BOTH"

    #: A constant which can be used with the direction property of a ObjectLineageRequestDetails.
    #: This constant has a value of "DOWNSTREAM"
    DIRECTION_DOWNSTREAM = "DOWNSTREAM"

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectLineageRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level:
            The value to assign to the level property of this ObjectLineageRequestDetails.
        :type level: int

        :param direction:
            The value to assign to the direction property of this ObjectLineageRequestDetails.
            Allowed values for this property are: "UPSTREAM", "BOTH", "DOWNSTREAM"
        :type direction: str

        :param is_intra_lineage:
            The value to assign to the is_intra_lineage property of this ObjectLineageRequestDetails.
        :type is_intra_lineage: bool

        :param intra_lineage_object_key:
            The value to assign to the intra_lineage_object_key property of this ObjectLineageRequestDetails.
        :type intra_lineage_object_key: str

        """
        self.swagger_types = {
            'level': 'int',
            'direction': 'str',
            'is_intra_lineage': 'bool',
            'intra_lineage_object_key': 'str'
        }
        self.attribute_map = {
            'level': 'level',
            'direction': 'direction',
            'is_intra_lineage': 'isIntraLineage',
            'intra_lineage_object_key': 'intraLineageObjectKey'
        }
        self._level = None
        self._direction = None
        self._is_intra_lineage = None
        self._intra_lineage_object_key = None

    @property
    def level(self):
        """
        Gets the level of this ObjectLineageRequestDetails.
        Object level at which the lineage is returned.


        :return: The level of this ObjectLineageRequestDetails.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this ObjectLineageRequestDetails.
        Object level at which the lineage is returned.


        :param level: The level of this ObjectLineageRequestDetails.
        :type: int
        """
        self._level = level

    @property
    def direction(self):
        """
        Gets the direction of this ObjectLineageRequestDetails.
        Direction of the lineage returned.

        Allowed values for this property are: "UPSTREAM", "BOTH", "DOWNSTREAM"


        :return: The direction of this ObjectLineageRequestDetails.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this ObjectLineageRequestDetails.
        Direction of the lineage returned.


        :param direction: The direction of this ObjectLineageRequestDetails.
        :type: str
        """
        allowed_values = ["UPSTREAM", "BOTH", "DOWNSTREAM"]
        if not value_allowed_none_or_none_sentinel(direction, allowed_values):
            raise ValueError(
                f"Invalid value for `direction`, must be None or one of {allowed_values}"
            )
        self._direction = direction

    @property
    def is_intra_lineage(self):
        """
        Gets the is_intra_lineage of this ObjectLineageRequestDetails.
        Intra-lineages are drill down lineages. This field indicates whether all intra-lineages need to be
        expanded inline in the lineage returned.


        :return: The is_intra_lineage of this ObjectLineageRequestDetails.
        :rtype: bool
        """
        return self._is_intra_lineage

    @is_intra_lineage.setter
    def is_intra_lineage(self, is_intra_lineage):
        """
        Sets the is_intra_lineage of this ObjectLineageRequestDetails.
        Intra-lineages are drill down lineages. This field indicates whether all intra-lineages need to be
        expanded inline in the lineage returned.


        :param is_intra_lineage: The is_intra_lineage of this ObjectLineageRequestDetails.
        :type: bool
        """
        self._is_intra_lineage = is_intra_lineage

    @property
    def intra_lineage_object_key(self):
        """
        Gets the intra_lineage_object_key of this ObjectLineageRequestDetails.
        Unique object key for which intra-lineage needs to be fetched. Only drill-down lineage corresponding
        to the object whose object key is passed is returned.


        :return: The intra_lineage_object_key of this ObjectLineageRequestDetails.
        :rtype: str
        """
        return self._intra_lineage_object_key

    @intra_lineage_object_key.setter
    def intra_lineage_object_key(self, intra_lineage_object_key):
        """
        Sets the intra_lineage_object_key of this ObjectLineageRequestDetails.
        Unique object key for which intra-lineage needs to be fetched. Only drill-down lineage corresponding
        to the object whose object key is passed is returned.


        :param intra_lineage_object_key: The intra_lineage_object_key of this ObjectLineageRequestDetails.
        :type: str
        """
        self._intra_lineage_object_key = intra_lineage_object_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
