# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .instance_agent_command_source_details import InstanceAgentCommandSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentCommandSourceViaObjectStorageUriDetails(InstanceAgentCommandSourceDetails):
    """
    Command content via uri.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentCommandSourceViaObjectStorageUriDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.compute_instance_agent.models.InstanceAgentCommandSourceViaObjectStorageUriDetails.source_type` attribute
        of this class is ``OBJECT_STORAGE_URI`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this InstanceAgentCommandSourceViaObjectStorageUriDetails.
            Allowed values for this property are: "TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE"
        :type source_type: str

        :param source_uri:
            The value to assign to the source_uri property of this InstanceAgentCommandSourceViaObjectStorageUriDetails.
        :type source_uri: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'source_uri': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'source_uri': 'sourceUri'
        }

        self._source_type = None
        self._source_uri = None
        self._source_type = 'OBJECT_STORAGE_URI'

    @property
    def source_uri(self):
        """
        **[Required]** Gets the source_uri of this InstanceAgentCommandSourceViaObjectStorageUriDetails.
        The Object Storage URL or PAR for the command.


        :return: The source_uri of this InstanceAgentCommandSourceViaObjectStorageUriDetails.
        :rtype: str
        """
        return self._source_uri

    @source_uri.setter
    def source_uri(self, source_uri):
        """
        Sets the source_uri of this InstanceAgentCommandSourceViaObjectStorageUriDetails.
        The Object Storage URL or PAR for the command.


        :param source_uri: The source_uri of this InstanceAgentCommandSourceViaObjectStorageUriDetails.
        :type: str
        """
        self._source_uri = source_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
