# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateApplicationDetails(object):
    """
    Properties for a new application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateApplicationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateApplicationDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateApplicationDetails.
        :type display_name: str

        :param config:
            The value to assign to the config property of this CreateApplicationDetails.
        :type config: dict(str, str)

        :param subnet_ids:
            The value to assign to the subnet_ids property of this CreateApplicationDetails.
        :type subnet_ids: list[str]

        :param syslog_url:
            The value to assign to the syslog_url property of this CreateApplicationDetails.
        :type syslog_url: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateApplicationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateApplicationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'config': 'dict(str, str)',
            'subnet_ids': 'list[str]',
            'syslog_url': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'config': 'config',
            'subnet_ids': 'subnetIds',
            'syslog_url': 'syslogUrl',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._config = None
        self._subnet_ids = None
        self._syslog_url = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateApplicationDetails.
        The OCID of the compartment to create the application within.


        :return: The compartment_id of this CreateApplicationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateApplicationDetails.
        The OCID of the compartment to create the application within.


        :param compartment_id: The compartment_id of this CreateApplicationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateApplicationDetails.
        The display name of the application. The display name must be unique within the compartment containing the application. Avoid entering confidential information.


        :return: The display_name of this CreateApplicationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateApplicationDetails.
        The display name of the application. The display name must be unique within the compartment containing the application. Avoid entering confidential information.


        :param display_name: The display_name of this CreateApplicationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def config(self):
        """
        Gets the config of this CreateApplicationDetails.
        Application configuration. These values are passed on to the function as environment variables, functions may override application configuration.
        Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

        Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

        The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.


        :return: The config of this CreateApplicationDetails.
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this CreateApplicationDetails.
        Application configuration. These values are passed on to the function as environment variables, functions may override application configuration.
        Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

        Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

        The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.


        :param config: The config of this CreateApplicationDetails.
        :type: dict(str, str)
        """
        self._config = config

    @property
    def subnet_ids(self):
        """
        **[Required]** Gets the subnet_ids of this CreateApplicationDetails.
        The `OCID`__s of the subnets in which to run functions in the application.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subnet_ids of this CreateApplicationDetails.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """
        Sets the subnet_ids of this CreateApplicationDetails.
        The `OCID`__s of the subnets in which to run functions in the application.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subnet_ids: The subnet_ids of this CreateApplicationDetails.
        :type: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def syslog_url(self):
        """
        Gets the syslog_url of this CreateApplicationDetails.
        A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls.
        The syslog URL must be reachable from all of the subnets configured for the application.
        Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging service, and not to the syslog URL.

        Example: `tcp://logserver.myserver:1234`


        :return: The syslog_url of this CreateApplicationDetails.
        :rtype: str
        """
        return self._syslog_url

    @syslog_url.setter
    def syslog_url(self, syslog_url):
        """
        Sets the syslog_url of this CreateApplicationDetails.
        A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls.
        The syslog URL must be reachable from all of the subnets configured for the application.
        Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging service, and not to the syslog URL.

        Example: `tcp://logserver.myserver:1234`


        :param syslog_url: The syslog_url of this CreateApplicationDetails.
        :type: str
        """
        self._syslog_url = syslog_url

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateApplicationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateApplicationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateApplicationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateApplicationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateApplicationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateApplicationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
