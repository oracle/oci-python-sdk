# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateApplicationDetails(object):
    """
    Properties to update an application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateApplicationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config:
            The value to assign to the config property of this UpdateApplicationDetails.
        :type config: dict(str, str)

        :param network_security_group_ids:
            The value to assign to the network_security_group_ids property of this UpdateApplicationDetails.
        :type network_security_group_ids: list[str]

        :param syslog_url:
            The value to assign to the syslog_url property of this UpdateApplicationDetails.
        :type syslog_url: str

        :param trace_config:
            The value to assign to the trace_config property of this UpdateApplicationDetails.
        :type trace_config: oci.functions.models.ApplicationTraceConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateApplicationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateApplicationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param image_policy_config:
            The value to assign to the image_policy_config property of this UpdateApplicationDetails.
        :type image_policy_config: oci.functions.models.ImagePolicyConfig

        """
        self.swagger_types = {
            'config': 'dict(str, str)',
            'network_security_group_ids': 'list[str]',
            'syslog_url': 'str',
            'trace_config': 'ApplicationTraceConfig',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'image_policy_config': 'ImagePolicyConfig'
        }

        self.attribute_map = {
            'config': 'config',
            'network_security_group_ids': 'networkSecurityGroupIds',
            'syslog_url': 'syslogUrl',
            'trace_config': 'traceConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'image_policy_config': 'imagePolicyConfig'
        }

        self._config = None
        self._network_security_group_ids = None
        self._syslog_url = None
        self._trace_config = None
        self._freeform_tags = None
        self._defined_tags = None
        self._image_policy_config = None

    @property
    def config(self):
        """
        Gets the config of this UpdateApplicationDetails.
        Application configuration. These values are passed on to the function as environment variables, functions may override application configuration.
        Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

        Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

        The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.


        :return: The config of this UpdateApplicationDetails.
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this UpdateApplicationDetails.
        Application configuration. These values are passed on to the function as environment variables, functions may override application configuration.
        Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

        Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

        The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.


        :param config: The config of this UpdateApplicationDetails.
        :type: dict(str, str)
        """
        self._config = config

    @property
    def network_security_group_ids(self):
        """
        Gets the network_security_group_ids of this UpdateApplicationDetails.
        The `OCID`__s of the Network Security Groups to add the application to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The network_security_group_ids of this UpdateApplicationDetails.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this UpdateApplicationDetails.
        The `OCID`__s of the Network Security Groups to add the application to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param network_security_group_ids: The network_security_group_ids of this UpdateApplicationDetails.
        :type: list[str]
        """
        self._network_security_group_ids = network_security_group_ids

    @property
    def syslog_url(self):
        """
        Gets the syslog_url of this UpdateApplicationDetails.
        A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls.
        The syslog URL must be reachable from all of the subnets configured for the application.
        Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging service, and not to the syslog URL.

        Example: `tcp://logserver.myserver:1234`


        :return: The syslog_url of this UpdateApplicationDetails.
        :rtype: str
        """
        return self._syslog_url

    @syslog_url.setter
    def syslog_url(self, syslog_url):
        """
        Sets the syslog_url of this UpdateApplicationDetails.
        A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls.
        The syslog URL must be reachable from all of the subnets configured for the application.
        Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging service, and not to the syslog URL.

        Example: `tcp://logserver.myserver:1234`


        :param syslog_url: The syslog_url of this UpdateApplicationDetails.
        :type: str
        """
        self._syslog_url = syslog_url

    @property
    def trace_config(self):
        """
        Gets the trace_config of this UpdateApplicationDetails.

        :return: The trace_config of this UpdateApplicationDetails.
        :rtype: oci.functions.models.ApplicationTraceConfig
        """
        return self._trace_config

    @trace_config.setter
    def trace_config(self, trace_config):
        """
        Sets the trace_config of this UpdateApplicationDetails.

        :param trace_config: The trace_config of this UpdateApplicationDetails.
        :type: oci.functions.models.ApplicationTraceConfig
        """
        self._trace_config = trace_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateApplicationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateApplicationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateApplicationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateApplicationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateApplicationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateApplicationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def image_policy_config(self):
        """
        Gets the image_policy_config of this UpdateApplicationDetails.

        :return: The image_policy_config of this UpdateApplicationDetails.
        :rtype: oci.functions.models.ImagePolicyConfig
        """
        return self._image_policy_config

    @image_policy_config.setter
    def image_policy_config(self, image_policy_config):
        """
        Sets the image_policy_config of this UpdateApplicationDetails.

        :param image_policy_config: The image_policy_config of this UpdateApplicationDetails.
        :type: oci.functions.models.ImagePolicyConfig
        """
        self._image_policy_config = image_policy_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
