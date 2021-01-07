# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HeaderManipulationAction(object):
    """
    An object that represents an action to apply to an HTTP headers.
    """

    #: A constant which can be used with the action property of a HeaderManipulationAction.
    #: This constant has a value of "EXTEND_HTTP_RESPONSE_HEADER"
    ACTION_EXTEND_HTTP_RESPONSE_HEADER = "EXTEND_HTTP_RESPONSE_HEADER"

    #: A constant which can be used with the action property of a HeaderManipulationAction.
    #: This constant has a value of "ADD_HTTP_RESPONSE_HEADER"
    ACTION_ADD_HTTP_RESPONSE_HEADER = "ADD_HTTP_RESPONSE_HEADER"

    #: A constant which can be used with the action property of a HeaderManipulationAction.
    #: This constant has a value of "REMOVE_HTTP_RESPONSE_HEADER"
    ACTION_REMOVE_HTTP_RESPONSE_HEADER = "REMOVE_HTTP_RESPONSE_HEADER"

    def __init__(self, **kwargs):
        """
        Initializes a new HeaderManipulationAction object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.waas.models.ExtendHttpResponseHeaderAction`
        * :class:`~oci.waas.models.AddHttpResponseHeaderAction`
        * :class:`~oci.waas.models.RemoveHttpResponseHeaderAction`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this HeaderManipulationAction.
            Allowed values for this property are: "EXTEND_HTTP_RESPONSE_HEADER", "ADD_HTTP_RESPONSE_HEADER", "REMOVE_HTTP_RESPONSE_HEADER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        """
        self.swagger_types = {
            'action': 'str'
        }

        self.attribute_map = {
            'action': 'action'
        }

        self._action = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['action']

        if type == 'EXTEND_HTTP_RESPONSE_HEADER':
            return 'ExtendHttpResponseHeaderAction'

        if type == 'ADD_HTTP_RESPONSE_HEADER':
            return 'AddHttpResponseHeaderAction'

        if type == 'REMOVE_HTTP_RESPONSE_HEADER':
            return 'RemoveHttpResponseHeaderAction'
        else:
            return 'HeaderManipulationAction'

    @property
    def action(self):
        """
        **[Required]** Gets the action of this HeaderManipulationAction.
        Allowed values for this property are: "EXTEND_HTTP_RESPONSE_HEADER", "ADD_HTTP_RESPONSE_HEADER", "REMOVE_HTTP_RESPONSE_HEADER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this HeaderManipulationAction.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this HeaderManipulationAction.

        :param action: The action of this HeaderManipulationAction.
        :type: str
        """
        allowed_values = ["EXTEND_HTTP_RESPONSE_HEADER", "ADD_HTTP_RESPONSE_HEADER", "REMOVE_HTTP_RESPONSE_HEADER"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
