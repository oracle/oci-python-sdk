# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .action_details import ActionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNotificationServiceActionDetails(ActionDetails):
    """
    Create an action that delivers to an Oracle Notification Service topic.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNotificationServiceActionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.events.models.CreateNotificationServiceActionDetails.action_type` attribute
        of this class is ``ONS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this CreateNotificationServiceActionDetails.
            Allowed values for this property are: "ONS", "OSS", "FAAS"
        :type action_type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this CreateNotificationServiceActionDetails.
        :type is_enabled: bool

        :param description:
            The value to assign to the description property of this CreateNotificationServiceActionDetails.
        :type description: str

        :param topic_id:
            The value to assign to the topic_id property of this CreateNotificationServiceActionDetails.
        :type topic_id: str

        """
        self.swagger_types = {
            'action_type': 'str',
            'is_enabled': 'bool',
            'description': 'str',
            'topic_id': 'str'
        }

        self.attribute_map = {
            'action_type': 'actionType',
            'is_enabled': 'isEnabled',
            'description': 'description',
            'topic_id': 'topicId'
        }

        self._action_type = None
        self._is_enabled = None
        self._description = None
        self._topic_id = None
        self._action_type = 'ONS'

    @property
    def topic_id(self):
        """
        Gets the topic_id of this CreateNotificationServiceActionDetails.
        The `OCID`__ of the topic to which messages are delivered.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The topic_id of this CreateNotificationServiceActionDetails.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """
        Sets the topic_id of this CreateNotificationServiceActionDetails.
        The `OCID`__ of the topic to which messages are delivered.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param topic_id: The topic_id of this CreateNotificationServiceActionDetails.
        :type: str
        """
        self._topic_id = topic_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
