# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Log(object):
    """
    Represents a log object.
    """

    #: A constant which can be used with the log_type property of a Log.
    #: This constant has a value of "CUSTOM"
    LOG_TYPE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the log_type property of a Log.
    #: This constant has a value of "SERVICE"
    LOG_TYPE_SERVICE = "SERVICE"

    #: A constant which can be used with the lifecycle_state property of a Log.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Log.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Log.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Log.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Log.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Log.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Log object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Log.
        :type id: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this Log.
        :type tenancy_id: str

        :param log_group_id:
            The value to assign to the log_group_id property of this Log.
        :type log_group_id: str

        :param display_name:
            The value to assign to the display_name property of this Log.
        :type display_name: str

        :param log_type:
            The value to assign to the log_type property of this Log.
            Allowed values for this property are: "CUSTOM", "SERVICE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type log_type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this Log.
        :type is_enabled: bool

        :param defined_tags:
            The value to assign to the defined_tags property of this Log.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Log.
        :type freeform_tags: dict(str, str)

        :param configuration:
            The value to assign to the configuration property of this Log.
        :type configuration: oci.logging.models.Configuration

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Log.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Log.
        :type time_created: datetime

        :param time_last_modified:
            The value to assign to the time_last_modified property of this Log.
        :type time_last_modified: datetime

        :param retention_duration:
            The value to assign to the retention_duration property of this Log.
        :type retention_duration: int

        :param compartment_id:
            The value to assign to the compartment_id property of this Log.
        :type compartment_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'tenancy_id': 'str',
            'log_group_id': 'str',
            'display_name': 'str',
            'log_type': 'str',
            'is_enabled': 'bool',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'configuration': 'Configuration',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_last_modified': 'datetime',
            'retention_duration': 'int',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'tenancy_id': 'tenancyId',
            'log_group_id': 'logGroupId',
            'display_name': 'displayName',
            'log_type': 'logType',
            'is_enabled': 'isEnabled',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'configuration': 'configuration',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_last_modified': 'timeLastModified',
            'retention_duration': 'retentionDuration',
            'compartment_id': 'compartmentId'
        }

        self._id = None
        self._tenancy_id = None
        self._log_group_id = None
        self._display_name = None
        self._log_type = None
        self._is_enabled = None
        self._defined_tags = None
        self._freeform_tags = None
        self._configuration = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_last_modified = None
        self._retention_duration = None
        self._compartment_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Log.
        The OCID of the resource.


        :return: The id of this Log.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Log.
        The OCID of the resource.


        :param id: The id of this Log.
        :type: str
        """
        self._id = id

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this Log.
        The OCID of the tenancy.


        :return: The tenancy_id of this Log.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this Log.
        The OCID of the tenancy.


        :param tenancy_id: The tenancy_id of this Log.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def log_group_id(self):
        """
        **[Required]** Gets the log_group_id of this Log.
        Log group OCID.


        :return: The log_group_id of this Log.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this Log.
        Log group OCID.


        :param log_group_id: The log_group_id of this Log.
        :type: str
        """
        self._log_group_id = log_group_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Log.
        The user-friendly display name. This must be unique within the enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :return: The display_name of this Log.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Log.
        The user-friendly display name. This must be unique within the enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this Log.
        :type: str
        """
        self._display_name = display_name

    @property
    def log_type(self):
        """
        **[Required]** Gets the log_type of this Log.
        The logType that the log object is for, whether custom or service.

        Allowed values for this property are: "CUSTOM", "SERVICE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The log_type of this Log.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """
        Sets the log_type of this Log.
        The logType that the log object is for, whether custom or service.


        :param log_type: The log_type of this Log.
        :type: str
        """
        allowed_values = ["CUSTOM", "SERVICE"]
        if not value_allowed_none_or_none_sentinel(log_type, allowed_values):
            log_type = 'UNKNOWN_ENUM_VALUE'
        self._log_type = log_type

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this Log.
        Whether or not this resource is currently enabled.


        :return: The is_enabled of this Log.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this Log.
        Whether or not this resource is currently enabled.


        :param is_enabled: The is_enabled of this Log.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Log.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Log.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Log.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Log.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Log.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Log.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Log.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Log.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def configuration(self):
        """
        Gets the configuration of this Log.

        :return: The configuration of this Log.
        :rtype: oci.logging.models.Configuration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this Log.

        :param configuration: The configuration of this Log.
        :type: oci.logging.models.Configuration
        """
        self._configuration = configuration

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Log.
        The pipeline state.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Log.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Log.
        The pipeline state.


        :param lifecycle_state: The lifecycle_state of this Log.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Log.
        Time the resource was created.


        :return: The time_created of this Log.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Log.
        Time the resource was created.


        :param time_created: The time_created of this Log.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_modified(self):
        """
        Gets the time_last_modified of this Log.
        Time the resource was last modified.


        :return: The time_last_modified of this Log.
        :rtype: datetime
        """
        return self._time_last_modified

    @time_last_modified.setter
    def time_last_modified(self, time_last_modified):
        """
        Sets the time_last_modified of this Log.
        Time the resource was last modified.


        :param time_last_modified: The time_last_modified of this Log.
        :type: datetime
        """
        self._time_last_modified = time_last_modified

    @property
    def retention_duration(self):
        """
        Gets the retention_duration of this Log.
        Log retention duration in 30-day increments (30, 60, 90 and so on).


        :return: The retention_duration of this Log.
        :rtype: int
        """
        return self._retention_duration

    @retention_duration.setter
    def retention_duration(self, retention_duration):
        """
        Sets the retention_duration of this Log.
        Log retention duration in 30-day increments (30, 60, 90 and so on).


        :param retention_duration: The retention_duration of this Log.
        :type: int
        """
        self._retention_duration = retention_duration

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Log.
        The OCID of the compartment that the resource belongs to.


        :return: The compartment_id of this Log.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Log.
        The OCID of the compartment that the resource belongs to.


        :param compartment_id: The compartment_id of this Log.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
