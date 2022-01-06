# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Action(object):
    """
    An entity that represents an action to apply for a routing rule.
    """

    #: A constant which can be used with the name property of a Action.
    #: This constant has a value of "FORWARD_TO_BACKENDSET"
    NAME_FORWARD_TO_BACKENDSET = "FORWARD_TO_BACKENDSET"

    def __init__(self, **kwargs):
        """
        Initializes a new Action object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.load_balancer.models.ForwardToBackendSet`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Action.
            Allowed values for this property are: "FORWARD_TO_BACKENDSET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        """
        self.swagger_types = {
            'name': 'str'
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['name']

        if type == 'FORWARD_TO_BACKENDSET':
            return 'ForwardToBackendSet'
        else:
            return 'Action'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Action.
        Allowed values for this property are: "FORWARD_TO_BACKENDSET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this Action.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Action.

        :param name: The name of this Action.
        :type: str
        """
        allowed_values = ["FORWARD_TO_BACKENDSET"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
