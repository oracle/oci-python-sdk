# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateLogDetails(object):
    """
    The details to create a log object.
    """

    #: A constant which can be used with the log_type property of a CreateLogDetails.
    #: This constant has a value of "CUSTOM"
    LOG_TYPE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the log_type property of a CreateLogDetails.
    #: This constant has a value of "SERVICE"
    LOG_TYPE_SERVICE = "SERVICE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateLogDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateLogDetails.
        :type display_name: str

        :param log_type:
            The value to assign to the log_type property of this CreateLogDetails.
            Allowed values for this property are: "CUSTOM", "SERVICE"
        :type log_type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this CreateLogDetails.
        :type is_enabled: bool

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateLogDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateLogDetails.
        :type freeform_tags: dict(str, str)

        :param configuration:
            The value to assign to the configuration property of this CreateLogDetails.
        :type configuration: oci.logging.models.Configuration

        :param retention_duration:
            The value to assign to the retention_duration property of this CreateLogDetails.
        :type retention_duration: int

        """
        self.swagger_types = {
            'display_name': 'str',
            'log_type': 'str',
            'is_enabled': 'bool',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'configuration': 'Configuration',
            'retention_duration': 'int'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'log_type': 'logType',
            'is_enabled': 'isEnabled',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'configuration': 'configuration',
            'retention_duration': 'retentionDuration'
        }

        self._display_name = None
        self._log_type = None
        self._is_enabled = None
        self._defined_tags = None
        self._freeform_tags = None
        self._configuration = None
        self._retention_duration = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateLogDetails.
        The user-friendly display name. This must be unique within the enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateLogDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateLogDetails.
        The user-friendly display name. This must be unique within the enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateLogDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def log_type(self):
        """
        **[Required]** Gets the log_type of this CreateLogDetails.
        The logType that the log object is for, whether custom or service.

        Allowed values for this property are: "CUSTOM", "SERVICE"


        :return: The log_type of this CreateLogDetails.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """
        Sets the log_type of this CreateLogDetails.
        The logType that the log object is for, whether custom or service.


        :param log_type: The log_type of this CreateLogDetails.
        :type: str
        """
        allowed_values = ["CUSTOM", "SERVICE"]
        if not value_allowed_none_or_none_sentinel(log_type, allowed_values):
            raise ValueError(
                "Invalid value for `log_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._log_type = log_type

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this CreateLogDetails.
        Whether or not this resource is currently enabled.


        :return: The is_enabled of this CreateLogDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this CreateLogDetails.
        Whether or not this resource is currently enabled.


        :param is_enabled: The is_enabled of this CreateLogDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateLogDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateLogDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateLogDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateLogDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateLogDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateLogDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateLogDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateLogDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def configuration(self):
        """
        Gets the configuration of this CreateLogDetails.

        :return: The configuration of this CreateLogDetails.
        :rtype: oci.logging.models.Configuration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this CreateLogDetails.

        :param configuration: The configuration of this CreateLogDetails.
        :type: oci.logging.models.Configuration
        """
        self._configuration = configuration

    @property
    def retention_duration(self):
        """
        Gets the retention_duration of this CreateLogDetails.
        Log retention duration in 30-day increments (30, 60, 90 and so on).


        :return: The retention_duration of this CreateLogDetails.
        :rtype: int
        """
        return self._retention_duration

    @retention_duration.setter
    def retention_duration(self, retention_duration):
        """
        Sets the retention_duration of this CreateLogDetails.
        Log retention duration in 30-day increments (30, 60, 90 and so on).


        :param retention_duration: The retention_duration of this CreateLogDetails.
        :type: int
        """
        self._retention_duration = retention_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
