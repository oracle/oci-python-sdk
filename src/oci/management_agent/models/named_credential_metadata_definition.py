# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200202


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NamedCredentialMetadataDefinition(object):
    """
    A named credential metadata definition
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NamedCredentialMetadataDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this NamedCredentialMetadataDefinition.
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this NamedCredentialMetadataDefinition.
        :type display_name: str

        :param minimum_agent_version:
            The value to assign to the minimum_agent_version property of this NamedCredentialMetadataDefinition.
        :type minimum_agent_version: str

        :param properties:
            The value to assign to the properties property of this NamedCredentialMetadataDefinition.
        :type properties: list[oci.management_agent.models.NamedCredentialFieldDefinition]

        """
        self.swagger_types = {
            'type': 'str',
            'display_name': 'str',
            'minimum_agent_version': 'str',
            'properties': 'list[NamedCredentialFieldDefinition]'
        }
        self.attribute_map = {
            'type': 'type',
            'display_name': 'displayName',
            'minimum_agent_version': 'minimumAgentVersion',
            'properties': 'properties'
        }
        self._type = None
        self._display_name = None
        self._minimum_agent_version = None
        self._properties = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this NamedCredentialMetadataDefinition.
        The type of the Named Credential.


        :return: The type of this NamedCredentialMetadataDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this NamedCredentialMetadataDefinition.
        The type of the Named Credential.


        :param type: The type of this NamedCredentialMetadataDefinition.
        :type: str
        """
        self._type = type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this NamedCredentialMetadataDefinition.
        Display name for this type of Named Credential


        :return: The display_name of this NamedCredentialMetadataDefinition.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this NamedCredentialMetadataDefinition.
        Display name for this type of Named Credential


        :param display_name: The display_name of this NamedCredentialMetadataDefinition.
        :type: str
        """
        self._display_name = display_name

    @property
    def minimum_agent_version(self):
        """
        **[Required]** Gets the minimum_agent_version of this NamedCredentialMetadataDefinition.
        This Named Credential type is supported on management agents at this version or above.


        :return: The minimum_agent_version of this NamedCredentialMetadataDefinition.
        :rtype: str
        """
        return self._minimum_agent_version

    @minimum_agent_version.setter
    def minimum_agent_version(self, minimum_agent_version):
        """
        Sets the minimum_agent_version of this NamedCredentialMetadataDefinition.
        This Named Credential type is supported on management agents at this version or above.


        :param minimum_agent_version: The minimum_agent_version of this NamedCredentialMetadataDefinition.
        :type: str
        """
        self._minimum_agent_version = minimum_agent_version

    @property
    def properties(self):
        """
        **[Required]** Gets the properties of this NamedCredentialMetadataDefinition.
        The property definitions for this named credential metadata


        :return: The properties of this NamedCredentialMetadataDefinition.
        :rtype: list[oci.management_agent.models.NamedCredentialFieldDefinition]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this NamedCredentialMetadataDefinition.
        The property definitions for this named credential metadata


        :param properties: The properties of this NamedCredentialMetadataDefinition.
        :type: list[oci.management_agent.models.NamedCredentialFieldDefinition]
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
