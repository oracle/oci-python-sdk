# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreationSource(object):
    """
    Details for auto-created entity.
    """

    #: A constant which can be used with the type property of a CreationSource.
    #: This constant has a value of "EM_BRIDGE"
    TYPE_EM_BRIDGE = "EM_BRIDGE"

    #: A constant which can be used with the type property of a CreationSource.
    #: This constant has a value of "SERVICE_CONNECTOR_HUB"
    TYPE_SERVICE_CONNECTOR_HUB = "SERVICE_CONNECTOR_HUB"

    #: A constant which can be used with the type property of a CreationSource.
    #: This constant has a value of "NONE"
    TYPE_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreationSource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreationSource.
            Allowed values for this property are: "EM_BRIDGE", "SERVICE_CONNECTOR_HUB", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param details:
            The value to assign to the details property of this CreationSource.
        :type details: str

        """
        self.swagger_types = {
            'type': 'str',
            'details': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'details': 'details'
        }

        self._type = None
        self._details = None

    @property
    def type(self):
        """
        Gets the type of this CreationSource.
        Source that auto-created the entity.

        Allowed values for this property are: "EM_BRIDGE", "SERVICE_CONNECTOR_HUB", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this CreationSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreationSource.
        Source that auto-created the entity.


        :param type: The type of this CreationSource.
        :type: str
        """
        allowed_values = ["EM_BRIDGE", "SERVICE_CONNECTOR_HUB", "NONE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def details(self):
        """
        Gets the details of this CreationSource.
        This will provide additional details for source of auto-creation. For example, if entity is auto-created
        by enterprise manager bridge, this field provides additional detail on enterprise manager that contributed
        to the entity auto-creation.


        :return: The details of this CreationSource.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this CreationSource.
        This will provide additional details for source of auto-creation. For example, if entity is auto-created
        by enterprise manager bridge, this field provides additional detail on enterprise manager that contributed
        to the entity auto-creation.


        :param details: The details of this CreationSource.
        :type: str
        """
        self._details = details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
