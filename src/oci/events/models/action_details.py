# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActionDetails(object):
    """
    Object used to create an action.
    """

    #: A constant which can be used with the action_type property of a ActionDetails.
    #: This constant has a value of "ONS"
    ACTION_TYPE_ONS = "ONS"

    #: A constant which can be used with the action_type property of a ActionDetails.
    #: This constant has a value of "OSS"
    ACTION_TYPE_OSS = "OSS"

    #: A constant which can be used with the action_type property of a ActionDetails.
    #: This constant has a value of "FAAS"
    ACTION_TYPE_FAAS = "FAAS"

    def __init__(self, **kwargs):
        """
        Initializes a new ActionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.events.models.CreateStreamingServiceActionDetails`
        * :class:`~oci.events.models.CreateFaaSActionDetails`
        * :class:`~oci.events.models.CreateNotificationServiceActionDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this ActionDetails.
            Allowed values for this property are: "ONS", "OSS", "FAAS"
        :type action_type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this ActionDetails.
        :type is_enabled: bool

        :param description:
            The value to assign to the description property of this ActionDetails.
        :type description: str

        """
        self.swagger_types = {
            'action_type': 'str',
            'is_enabled': 'bool',
            'description': 'str'
        }

        self.attribute_map = {
            'action_type': 'actionType',
            'is_enabled': 'isEnabled',
            'description': 'description'
        }

        self._action_type = None
        self._is_enabled = None
        self._description = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['actionType']

        if type == 'OSS':
            return 'CreateStreamingServiceActionDetails'

        if type == 'FAAS':
            return 'CreateFaaSActionDetails'

        if type == 'ONS':
            return 'CreateNotificationServiceActionDetails'
        else:
            return 'ActionDetails'

    @property
    def action_type(self):
        """
        **[Required]** Gets the action_type of this ActionDetails.
        The action to perform if the condition in the rule matches an event.

        * **ONS:** Send to an Oracle Notification Service topic.
        * **OSS:** Send to a stream from Oracle Streaming Service.
        * **FAAS:** Send to an Oracle Functions Service endpoint.

        Allowed values for this property are: "ONS", "OSS", "FAAS"


        :return: The action_type of this ActionDetails.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this ActionDetails.
        The action to perform if the condition in the rule matches an event.

        * **ONS:** Send to an Oracle Notification Service topic.
        * **OSS:** Send to a stream from Oracle Streaming Service.
        * **FAAS:** Send to an Oracle Functions Service endpoint.


        :param action_type: The action_type of this ActionDetails.
        :type: str
        """
        allowed_values = ["ONS", "OSS", "FAAS"]
        if not value_allowed_none_or_none_sentinel(action_type, allowed_values):
            raise ValueError(
                "Invalid value for `action_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._action_type = action_type

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this ActionDetails.
        Whether or not this action is currently enabled.

        Example: `true`


        :return: The is_enabled of this ActionDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ActionDetails.
        Whether or not this action is currently enabled.

        Example: `true`


        :param is_enabled: The is_enabled of this ActionDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def description(self):
        """
        Gets the description of this ActionDetails.
        A string that describes the details of the action. It does not have to be unique, and you can change it. Avoid entering
        confidential information.


        :return: The description of this ActionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ActionDetails.
        A string that describes the details of the action. It does not have to be unique, and you can change it. Avoid entering
        confidential information.


        :param description: The description of this ActionDetails.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
