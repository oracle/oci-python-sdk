# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .action_details import ActionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateStreamingServiceActionDetails(ActionDetails):
    """
    Create an action that delivers to an Oracle Stream Service stream.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateStreamingServiceActionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.events.models.CreateStreamingServiceActionDetails.action_type` attribute
        of this class is ``OSS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this CreateStreamingServiceActionDetails.
            Allowed values for this property are: "ONS", "OSS", "FAAS"
        :type action_type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this CreateStreamingServiceActionDetails.
        :type is_enabled: bool

        :param description:
            The value to assign to the description property of this CreateStreamingServiceActionDetails.
        :type description: str

        :param stream_id:
            The value to assign to the stream_id property of this CreateStreamingServiceActionDetails.
        :type stream_id: str

        """
        self.swagger_types = {
            'action_type': 'str',
            'is_enabled': 'bool',
            'description': 'str',
            'stream_id': 'str'
        }

        self.attribute_map = {
            'action_type': 'actionType',
            'is_enabled': 'isEnabled',
            'description': 'description',
            'stream_id': 'streamId'
        }

        self._action_type = None
        self._is_enabled = None
        self._description = None
        self._stream_id = None
        self._action_type = 'OSS'

    @property
    def stream_id(self):
        """
        **[Required]** Gets the stream_id of this CreateStreamingServiceActionDetails.
        The `OCID`__ of the stream to which messages are delivered.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The stream_id of this CreateStreamingServiceActionDetails.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """
        Sets the stream_id of this CreateStreamingServiceActionDetails.
        The `OCID`__ of the stream to which messages are delivered.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param stream_id: The stream_id of this CreateStreamingServiceActionDetails.
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
