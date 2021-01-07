# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .action import Action
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StreamingServiceAction(Action):
    """
    An action that delivers to an Oracle Stream Service stream.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StreamingServiceAction object with values from keyword arguments. The default value of the :py:attr:`~oci.events.models.StreamingServiceAction.action_type` attribute
        of this class is ``OSS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this StreamingServiceAction.
            Allowed values for this property are: "ONS", "OSS", "FAAS"
        :type action_type: str

        :param id:
            The value to assign to the id property of this StreamingServiceAction.
        :type id: str

        :param lifecycle_message:
            The value to assign to the lifecycle_message property of this StreamingServiceAction.
        :type lifecycle_message: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this StreamingServiceAction.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param is_enabled:
            The value to assign to the is_enabled property of this StreamingServiceAction.
        :type is_enabled: bool

        :param description:
            The value to assign to the description property of this StreamingServiceAction.
        :type description: str

        :param stream_id:
            The value to assign to the stream_id property of this StreamingServiceAction.
        :type stream_id: str

        """
        self.swagger_types = {
            'action_type': 'str',
            'id': 'str',
            'lifecycle_message': 'str',
            'lifecycle_state': 'str',
            'is_enabled': 'bool',
            'description': 'str',
            'stream_id': 'str'
        }

        self.attribute_map = {
            'action_type': 'actionType',
            'id': 'id',
            'lifecycle_message': 'lifecycleMessage',
            'lifecycle_state': 'lifecycleState',
            'is_enabled': 'isEnabled',
            'description': 'description',
            'stream_id': 'streamId'
        }

        self._action_type = None
        self._id = None
        self._lifecycle_message = None
        self._lifecycle_state = None
        self._is_enabled = None
        self._description = None
        self._stream_id = None
        self._action_type = 'OSS'

    @property
    def stream_id(self):
        """
        Gets the stream_id of this StreamingServiceAction.
        The `OCID`__ of the stream to which messages are delivered.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The stream_id of this StreamingServiceAction.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """
        Sets the stream_id of this StreamingServiceAction.
        The `OCID`__ of the stream to which messages are delivered.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param stream_id: The stream_id of this StreamingServiceAction.
        :type: str
        """
        self._stream_id = stream_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
