# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Monitor(object):
    """
    The information about a monitor.
    """

    #: A constant which can be used with the monitor_type property of a Monitor.
    #: This constant has a value of "SCRIPTED_BROWSER"
    MONITOR_TYPE_SCRIPTED_BROWSER = "SCRIPTED_BROWSER"

    #: A constant which can be used with the monitor_type property of a Monitor.
    #: This constant has a value of "BROWSER"
    MONITOR_TYPE_BROWSER = "BROWSER"

    #: A constant which can be used with the monitor_type property of a Monitor.
    #: This constant has a value of "SCRIPTED_REST"
    MONITOR_TYPE_SCRIPTED_REST = "SCRIPTED_REST"

    #: A constant which can be used with the monitor_type property of a Monitor.
    #: This constant has a value of "REST"
    MONITOR_TYPE_REST = "REST"

    #: A constant which can be used with the status property of a Monitor.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a Monitor.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a Monitor.
    #: This constant has a value of "INVALID"
    STATUS_INVALID = "INVALID"

    #: A constant which can be used with the scheduling_policy property of a Monitor.
    #: This constant has a value of "ALL"
    SCHEDULING_POLICY_ALL = "ALL"

    #: A constant which can be used with the scheduling_policy property of a Monitor.
    #: This constant has a value of "ROUND_ROBIN"
    SCHEDULING_POLICY_ROUND_ROBIN = "ROUND_ROBIN"

    #: A constant which can be used with the scheduling_policy property of a Monitor.
    #: This constant has a value of "BATCHED_ROUND_ROBIN"
    SCHEDULING_POLICY_BATCHED_ROUND_ROBIN = "BATCHED_ROUND_ROBIN"

    def __init__(self, **kwargs):
        """
        Initializes a new Monitor object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Monitor.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Monitor.
        :type display_name: str

        :param monitor_type:
            The value to assign to the monitor_type property of this Monitor.
            Allowed values for this property are: "SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type monitor_type: str

        :param vantage_points:
            The value to assign to the vantage_points property of this Monitor.
        :type vantage_points: list[oci.apm_synthetics.models.VantagePointInfo]

        :param vantage_point_count:
            The value to assign to the vantage_point_count property of this Monitor.
        :type vantage_point_count: int

        :param script_id:
            The value to assign to the script_id property of this Monitor.
        :type script_id: str

        :param script_name:
            The value to assign to the script_name property of this Monitor.
        :type script_name: str

        :param status:
            The value to assign to the status property of this Monitor.
            Allowed values for this property are: "ENABLED", "DISABLED", "INVALID", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param repeat_interval_in_seconds:
            The value to assign to the repeat_interval_in_seconds property of this Monitor.
        :type repeat_interval_in_seconds: int

        :param is_run_once:
            The value to assign to the is_run_once property of this Monitor.
        :type is_run_once: bool

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this Monitor.
        :type timeout_in_seconds: int

        :param target:
            The value to assign to the target property of this Monitor.
        :type target: str

        :param script_parameters:
            The value to assign to the script_parameters property of this Monitor.
        :type script_parameters: list[oci.apm_synthetics.models.MonitorScriptParameterInfo]

        :param configuration:
            The value to assign to the configuration property of this Monitor.
        :type configuration: oci.apm_synthetics.models.MonitorConfiguration

        :param time_created:
            The value to assign to the time_created property of this Monitor.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Monitor.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Monitor.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Monitor.
        :type defined_tags: dict(str, dict(str, object))

        :param is_run_now:
            The value to assign to the is_run_now property of this Monitor.
        :type is_run_now: bool

        :param scheduling_policy:
            The value to assign to the scheduling_policy property of this Monitor.
            Allowed values for this property are: "ALL", "ROUND_ROBIN", "BATCHED_ROUND_ROBIN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scheduling_policy: str

        :param batch_interval_in_seconds:
            The value to assign to the batch_interval_in_seconds property of this Monitor.
        :type batch_interval_in_seconds: int

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'monitor_type': 'str',
            'vantage_points': 'list[VantagePointInfo]',
            'vantage_point_count': 'int',
            'script_id': 'str',
            'script_name': 'str',
            'status': 'str',
            'repeat_interval_in_seconds': 'int',
            'is_run_once': 'bool',
            'timeout_in_seconds': 'int',
            'target': 'str',
            'script_parameters': 'list[MonitorScriptParameterInfo]',
            'configuration': 'MonitorConfiguration',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_run_now': 'bool',
            'scheduling_policy': 'str',
            'batch_interval_in_seconds': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'monitor_type': 'monitorType',
            'vantage_points': 'vantagePoints',
            'vantage_point_count': 'vantagePointCount',
            'script_id': 'scriptId',
            'script_name': 'scriptName',
            'status': 'status',
            'repeat_interval_in_seconds': 'repeatIntervalInSeconds',
            'is_run_once': 'isRunOnce',
            'timeout_in_seconds': 'timeoutInSeconds',
            'target': 'target',
            'script_parameters': 'scriptParameters',
            'configuration': 'configuration',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_run_now': 'isRunNow',
            'scheduling_policy': 'schedulingPolicy',
            'batch_interval_in_seconds': 'batchIntervalInSeconds'
        }

        self._id = None
        self._display_name = None
        self._monitor_type = None
        self._vantage_points = None
        self._vantage_point_count = None
        self._script_id = None
        self._script_name = None
        self._status = None
        self._repeat_interval_in_seconds = None
        self._is_run_once = None
        self._timeout_in_seconds = None
        self._target = None
        self._script_parameters = None
        self._configuration = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_run_now = None
        self._scheduling_policy = None
        self._batch_interval_in_seconds = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Monitor.
        The `OCID`__ of the monitor.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Monitor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Monitor.
        The `OCID`__ of the monitor.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Monitor.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Monitor.
        Unique name that can be edited. The name should not contain any confidential information.


        :return: The display_name of this Monitor.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Monitor.
        Unique name that can be edited. The name should not contain any confidential information.


        :param display_name: The display_name of this Monitor.
        :type: str
        """
        self._display_name = display_name

    @property
    def monitor_type(self):
        """
        **[Required]** Gets the monitor_type of this Monitor.
        Type of the monitor.

        Allowed values for this property are: "SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The monitor_type of this Monitor.
        :rtype: str
        """
        return self._monitor_type

    @monitor_type.setter
    def monitor_type(self, monitor_type):
        """
        Sets the monitor_type of this Monitor.
        Type of the monitor.


        :param monitor_type: The monitor_type of this Monitor.
        :type: str
        """
        allowed_values = ["SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST"]
        if not value_allowed_none_or_none_sentinel(monitor_type, allowed_values):
            monitor_type = 'UNKNOWN_ENUM_VALUE'
        self._monitor_type = monitor_type

    @property
    def vantage_points(self):
        """
        **[Required]** Gets the vantage_points of this Monitor.
        List of public and dedicated vantage points where the monitor is running.


        :return: The vantage_points of this Monitor.
        :rtype: list[oci.apm_synthetics.models.VantagePointInfo]
        """
        return self._vantage_points

    @vantage_points.setter
    def vantage_points(self, vantage_points):
        """
        Sets the vantage_points of this Monitor.
        List of public and dedicated vantage points where the monitor is running.


        :param vantage_points: The vantage_points of this Monitor.
        :type: list[oci.apm_synthetics.models.VantagePointInfo]
        """
        self._vantage_points = vantage_points

    @property
    def vantage_point_count(self):
        """
        **[Required]** Gets the vantage_point_count of this Monitor.
        Number of vantage points where monitor is running.


        :return: The vantage_point_count of this Monitor.
        :rtype: int
        """
        return self._vantage_point_count

    @vantage_point_count.setter
    def vantage_point_count(self, vantage_point_count):
        """
        Sets the vantage_point_count of this Monitor.
        Number of vantage points where monitor is running.


        :param vantage_point_count: The vantage_point_count of this Monitor.
        :type: int
        """
        self._vantage_point_count = vantage_point_count

    @property
    def script_id(self):
        """
        **[Required]** Gets the script_id of this Monitor.
        The `OCID`__ of the script.
        scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The script_id of this Monitor.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """
        Sets the script_id of this Monitor.
        The `OCID`__ of the script.
        scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param script_id: The script_id of this Monitor.
        :type: str
        """
        self._script_id = script_id

    @property
    def script_name(self):
        """
        **[Required]** Gets the script_name of this Monitor.
        Name of the script.


        :return: The script_name of this Monitor.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        """
        Sets the script_name of this Monitor.
        Name of the script.


        :param script_name: The script_name of this Monitor.
        :type: str
        """
        self._script_name = script_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this Monitor.
        Enables or disables the monitor.

        Allowed values for this property are: "ENABLED", "DISABLED", "INVALID", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this Monitor.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Monitor.
        Enables or disables the monitor.


        :param status: The status of this Monitor.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "INVALID"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def repeat_interval_in_seconds(self):
        """
        **[Required]** Gets the repeat_interval_in_seconds of this Monitor.
        Interval in seconds after the start time when the job should be repeated.
        Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.


        :return: The repeat_interval_in_seconds of this Monitor.
        :rtype: int
        """
        return self._repeat_interval_in_seconds

    @repeat_interval_in_seconds.setter
    def repeat_interval_in_seconds(self, repeat_interval_in_seconds):
        """
        Sets the repeat_interval_in_seconds of this Monitor.
        Interval in seconds after the start time when the job should be repeated.
        Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.


        :param repeat_interval_in_seconds: The repeat_interval_in_seconds of this Monitor.
        :type: int
        """
        self._repeat_interval_in_seconds = repeat_interval_in_seconds

    @property
    def is_run_once(self):
        """
        **[Required]** Gets the is_run_once of this Monitor.
        If runOnce is enabled, then the monitor will run once.


        :return: The is_run_once of this Monitor.
        :rtype: bool
        """
        return self._is_run_once

    @is_run_once.setter
    def is_run_once(self, is_run_once):
        """
        Sets the is_run_once of this Monitor.
        If runOnce is enabled, then the monitor will run once.


        :param is_run_once: The is_run_once of this Monitor.
        :type: bool
        """
        self._is_run_once = is_run_once

    @property
    def timeout_in_seconds(self):
        """
        **[Required]** Gets the timeout_in_seconds of this Monitor.
        Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors.
        Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors.
        Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.


        :return: The timeout_in_seconds of this Monitor.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this Monitor.
        Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors.
        Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors.
        Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.


        :param timeout_in_seconds: The timeout_in_seconds of this Monitor.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def target(self):
        """
        Gets the target of this Monitor.
        Specify the endpoint on which to run the monitor.
        For BROWSER and REST monitor types, target is mandatory.
        If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint.
        If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.


        :return: The target of this Monitor.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this Monitor.
        Specify the endpoint on which to run the monitor.
        For BROWSER and REST monitor types, target is mandatory.
        If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint.
        If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.


        :param target: The target of this Monitor.
        :type: str
        """
        self._target = target

    @property
    def script_parameters(self):
        """
        Gets the script_parameters of this Monitor.
        List of script parameters. Example: `[{\"monitorScriptParameter\": {\"paramName\": \"userid\", \"paramValue\":\"testuser\"}, \"isSecret\": false, \"isOverwritten\": false}]`


        :return: The script_parameters of this Monitor.
        :rtype: list[oci.apm_synthetics.models.MonitorScriptParameterInfo]
        """
        return self._script_parameters

    @script_parameters.setter
    def script_parameters(self, script_parameters):
        """
        Sets the script_parameters of this Monitor.
        List of script parameters. Example: `[{\"monitorScriptParameter\": {\"paramName\": \"userid\", \"paramValue\":\"testuser\"}, \"isSecret\": false, \"isOverwritten\": false}]`


        :param script_parameters: The script_parameters of this Monitor.
        :type: list[oci.apm_synthetics.models.MonitorScriptParameterInfo]
        """
        self._script_parameters = script_parameters

    @property
    def configuration(self):
        """
        Gets the configuration of this Monitor.

        :return: The configuration of this Monitor.
        :rtype: oci.apm_synthetics.models.MonitorConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this Monitor.

        :param configuration: The configuration of this Monitor.
        :type: oci.apm_synthetics.models.MonitorConfiguration
        """
        self._configuration = configuration

    @property
    def time_created(self):
        """
        Gets the time_created of this Monitor.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Monitor.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Monitor.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Monitor.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Monitor.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Monitor.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Monitor.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Monitor.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Monitor.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Monitor.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Monitor.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Monitor.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Monitor.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Monitor.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Monitor.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Monitor.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_run_now(self):
        """
        **[Required]** Gets the is_run_now of this Monitor.
        If isRunNow is enabled, then the monitor will run now.


        :return: The is_run_now of this Monitor.
        :rtype: bool
        """
        return self._is_run_now

    @is_run_now.setter
    def is_run_now(self, is_run_now):
        """
        Sets the is_run_now of this Monitor.
        If isRunNow is enabled, then the monitor will run now.


        :param is_run_now: The is_run_now of this Monitor.
        :type: bool
        """
        self._is_run_now = is_run_now

    @property
    def scheduling_policy(self):
        """
        **[Required]** Gets the scheduling_policy of this Monitor.
        Scheduling policy on Vantage points.

        Allowed values for this property are: "ALL", "ROUND_ROBIN", "BATCHED_ROUND_ROBIN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The scheduling_policy of this Monitor.
        :rtype: str
        """
        return self._scheduling_policy

    @scheduling_policy.setter
    def scheduling_policy(self, scheduling_policy):
        """
        Sets the scheduling_policy of this Monitor.
        Scheduling policy on Vantage points.


        :param scheduling_policy: The scheduling_policy of this Monitor.
        :type: str
        """
        allowed_values = ["ALL", "ROUND_ROBIN", "BATCHED_ROUND_ROBIN"]
        if not value_allowed_none_or_none_sentinel(scheduling_policy, allowed_values):
            scheduling_policy = 'UNKNOWN_ENUM_VALUE'
        self._scheduling_policy = scheduling_policy

    @property
    def batch_interval_in_seconds(self):
        """
        **[Required]** Gets the batch_interval_in_seconds of this Monitor.
        Time interval between 2 runs in round robin batch mode (*SchedulingPolicy - BATCHED_ROUND_ROBIN).


        :return: The batch_interval_in_seconds of this Monitor.
        :rtype: int
        """
        return self._batch_interval_in_seconds

    @batch_interval_in_seconds.setter
    def batch_interval_in_seconds(self, batch_interval_in_seconds):
        """
        Sets the batch_interval_in_seconds of this Monitor.
        Time interval between 2 runs in round robin batch mode (*SchedulingPolicy - BATCHED_ROUND_ROBIN).


        :param batch_interval_in_seconds: The batch_interval_in_seconds of this Monitor.
        :type: int
        """
        self._batch_interval_in_seconds = batch_interval_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
