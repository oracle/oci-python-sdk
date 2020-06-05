# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIntegrationInstanceDetails(object):
    """
    The information to be updated.
    """

    #: A constant which can be used with the integration_instance_type property of a UpdateIntegrationInstanceDetails.
    #: This constant has a value of "STANDARD"
    INTEGRATION_INSTANCE_TYPE_STANDARD = "STANDARD"

    #: A constant which can be used with the integration_instance_type property of a UpdateIntegrationInstanceDetails.
    #: This constant has a value of "ENTERPRISE"
    INTEGRATION_INSTANCE_TYPE_ENTERPRISE = "ENTERPRISE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIntegrationInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateIntegrationInstanceDetails.
        :type display_name: str

        :param integration_instance_type:
            The value to assign to the integration_instance_type property of this UpdateIntegrationInstanceDetails.
            Allowed values for this property are: "STANDARD", "ENTERPRISE"
        :type integration_instance_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateIntegrationInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateIntegrationInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param is_byol:
            The value to assign to the is_byol property of this UpdateIntegrationInstanceDetails.
        :type is_byol: bool

        :param message_packs:
            The value to assign to the message_packs property of this UpdateIntegrationInstanceDetails.
        :type message_packs: int

        :param is_file_server_enabled:
            The value to assign to the is_file_server_enabled property of this UpdateIntegrationInstanceDetails.
        :type is_file_server_enabled: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'integration_instance_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_byol': 'bool',
            'message_packs': 'int',
            'is_file_server_enabled': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'integration_instance_type': 'integrationInstanceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_byol': 'isByol',
            'message_packs': 'messagePacks',
            'is_file_server_enabled': 'isFileServerEnabled'
        }

        self._display_name = None
        self._integration_instance_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_byol = None
        self._message_packs = None
        self._is_file_server_enabled = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateIntegrationInstanceDetails.
        Integration Instance Identifier.


        :return: The display_name of this UpdateIntegrationInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateIntegrationInstanceDetails.
        Integration Instance Identifier.


        :param display_name: The display_name of this UpdateIntegrationInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def integration_instance_type(self):
        """
        Gets the integration_instance_type of this UpdateIntegrationInstanceDetails.
        Standard or Enterprise type

        Allowed values for this property are: "STANDARD", "ENTERPRISE"


        :return: The integration_instance_type of this UpdateIntegrationInstanceDetails.
        :rtype: str
        """
        return self._integration_instance_type

    @integration_instance_type.setter
    def integration_instance_type(self, integration_instance_type):
        """
        Sets the integration_instance_type of this UpdateIntegrationInstanceDetails.
        Standard or Enterprise type


        :param integration_instance_type: The integration_instance_type of this UpdateIntegrationInstanceDetails.
        :type: str
        """
        allowed_values = ["STANDARD", "ENTERPRISE"]
        if not value_allowed_none_or_none_sentinel(integration_instance_type, allowed_values):
            raise ValueError(
                "Invalid value for `integration_instance_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._integration_instance_type = integration_instance_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateIntegrationInstanceDetails.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateIntegrationInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateIntegrationInstanceDetails.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateIntegrationInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateIntegrationInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateIntegrationInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateIntegrationInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateIntegrationInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_byol(self):
        """
        Gets the is_byol of this UpdateIntegrationInstanceDetails.
        Bring your own license.


        :return: The is_byol of this UpdateIntegrationInstanceDetails.
        :rtype: bool
        """
        return self._is_byol

    @is_byol.setter
    def is_byol(self, is_byol):
        """
        Sets the is_byol of this UpdateIntegrationInstanceDetails.
        Bring your own license.


        :param is_byol: The is_byol of this UpdateIntegrationInstanceDetails.
        :type: bool
        """
        self._is_byol = is_byol

    @property
    def message_packs(self):
        """
        Gets the message_packs of this UpdateIntegrationInstanceDetails.
        The number of configured message packs


        :return: The message_packs of this UpdateIntegrationInstanceDetails.
        :rtype: int
        """
        return self._message_packs

    @message_packs.setter
    def message_packs(self, message_packs):
        """
        Sets the message_packs of this UpdateIntegrationInstanceDetails.
        The number of configured message packs


        :param message_packs: The message_packs of this UpdateIntegrationInstanceDetails.
        :type: int
        """
        self._message_packs = message_packs

    @property
    def is_file_server_enabled(self):
        """
        Gets the is_file_server_enabled of this UpdateIntegrationInstanceDetails.
        The file server is enabled or not.


        :return: The is_file_server_enabled of this UpdateIntegrationInstanceDetails.
        :rtype: bool
        """
        return self._is_file_server_enabled

    @is_file_server_enabled.setter
    def is_file_server_enabled(self, is_file_server_enabled):
        """
        Sets the is_file_server_enabled of this UpdateIntegrationInstanceDetails.
        The file server is enabled or not.


        :param is_file_server_enabled: The is_file_server_enabled of this UpdateIntegrationInstanceDetails.
        :type: bool
        """
        self._is_file_server_enabled = is_file_server_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
