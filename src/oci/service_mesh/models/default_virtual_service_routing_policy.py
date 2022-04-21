# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DefaultVirtualServiceRoutingPolicy(object):
    """
    Routing policy for the virtual service.
    """

    #: A constant which can be used with the type property of a DefaultVirtualServiceRoutingPolicy.
    #: This constant has a value of "UNIFORM"
    TYPE_UNIFORM = "UNIFORM"

    #: A constant which can be used with the type property of a DefaultVirtualServiceRoutingPolicy.
    #: This constant has a value of "DENY"
    TYPE_DENY = "DENY"

    def __init__(self, **kwargs):
        """
        Initializes a new DefaultVirtualServiceRoutingPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DefaultVirtualServiceRoutingPolicy.
            Allowed values for this property are: "UNIFORM", "DENY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DefaultVirtualServiceRoutingPolicy.
        Type of the virtual service routing policy.

        Allowed values for this property are: "UNIFORM", "DENY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DefaultVirtualServiceRoutingPolicy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DefaultVirtualServiceRoutingPolicy.
        Type of the virtual service routing policy.


        :param type: The type of this DefaultVirtualServiceRoutingPolicy.
        :type: str
        """
        allowed_values = ["UNIFORM", "DENY"]
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
