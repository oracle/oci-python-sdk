# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateScheduledJobDetails(object):
    """
    Information for updating a Scheduled Job
    """

    #: A constant which can be used with the schedule_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "ONETIME"
    SCHEDULE_TYPE_ONETIME = "ONETIME"

    #: A constant which can be used with the schedule_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "RECURRING"
    SCHEDULE_TYPE_RECURRING = "RECURRING"

    #: A constant which can be used with the interval_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "HOUR"
    INTERVAL_TYPE_HOUR = "HOUR"

    #: A constant which can be used with the interval_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "DAY"
    INTERVAL_TYPE_DAY = "DAY"

    #: A constant which can be used with the interval_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "WEEK"
    INTERVAL_TYPE_WEEK = "WEEK"

    #: A constant which can be used with the interval_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "MONTH"
    INTERVAL_TYPE_MONTH = "MONTH"

    #: A constant which can be used with the operation_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "INSTALL"
    OPERATION_TYPE_INSTALL = "INSTALL"

    #: A constant which can be used with the operation_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "UPDATE"
    OPERATION_TYPE_UPDATE = "UPDATE"

    #: A constant which can be used with the operation_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "REMOVE"
    OPERATION_TYPE_REMOVE = "REMOVE"

    #: A constant which can be used with the operation_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "UPDATEALL"
    OPERATION_TYPE_UPDATEALL = "UPDATEALL"

    #: A constant which can be used with the update_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "SECURITY"
    UPDATE_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the update_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "BUGFIX"
    UPDATE_TYPE_BUGFIX = "BUGFIX"

    #: A constant which can be used with the update_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "ENHANCEMENT"
    UPDATE_TYPE_ENHANCEMENT = "ENHANCEMENT"

    #: A constant which can be used with the update_type property of a UpdateScheduledJobDetails.
    #: This constant has a value of "ALL"
    UPDATE_TYPE_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateScheduledJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateScheduledJobDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateScheduledJobDetails.
        :type description: str

        :param schedule_type:
            The value to assign to the schedule_type property of this UpdateScheduledJobDetails.
            Allowed values for this property are: "ONETIME", "RECURRING"
        :type schedule_type: str

        :param time_next_execution:
            The value to assign to the time_next_execution property of this UpdateScheduledJobDetails.
        :type time_next_execution: datetime

        :param interval_type:
            The value to assign to the interval_type property of this UpdateScheduledJobDetails.
            Allowed values for this property are: "HOUR", "DAY", "WEEK", "MONTH"
        :type interval_type: str

        :param interval_value:
            The value to assign to the interval_value property of this UpdateScheduledJobDetails.
        :type interval_value: str

        :param operation_type:
            The value to assign to the operation_type property of this UpdateScheduledJobDetails.
            Allowed values for this property are: "INSTALL", "UPDATE", "REMOVE", "UPDATEALL"
        :type operation_type: str

        :param update_type:
            The value to assign to the update_type property of this UpdateScheduledJobDetails.
            Allowed values for this property are: "SECURITY", "BUGFIX", "ENHANCEMENT", "ALL"
        :type update_type: str

        :param package_names:
            The value to assign to the package_names property of this UpdateScheduledJobDetails.
        :type package_names: list[oci.os_management.models.PackageName]

        :param update_names:
            The value to assign to the update_names property of this UpdateScheduledJobDetails.
        :type update_names: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateScheduledJobDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateScheduledJobDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'schedule_type': 'str',
            'time_next_execution': 'datetime',
            'interval_type': 'str',
            'interval_value': 'str',
            'operation_type': 'str',
            'update_type': 'str',
            'package_names': 'list[PackageName]',
            'update_names': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'schedule_type': 'scheduleType',
            'time_next_execution': 'timeNextExecution',
            'interval_type': 'intervalType',
            'interval_value': 'intervalValue',
            'operation_type': 'operationType',
            'update_type': 'updateType',
            'package_names': 'packageNames',
            'update_names': 'updateNames',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._schedule_type = None
        self._time_next_execution = None
        self._interval_type = None
        self._interval_value = None
        self._operation_type = None
        self._update_type = None
        self._package_names = None
        self._update_names = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateScheduledJobDetails.
        Scheduled Job name


        :return: The display_name of this UpdateScheduledJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateScheduledJobDetails.
        Scheduled Job name


        :param display_name: The display_name of this UpdateScheduledJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateScheduledJobDetails.
        Details describing the Scheduled Job.


        :return: The description of this UpdateScheduledJobDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateScheduledJobDetails.
        Details describing the Scheduled Job.


        :param description: The description of this UpdateScheduledJobDetails.
        :type: str
        """
        self._description = description

    @property
    def schedule_type(self):
        """
        Gets the schedule_type of this UpdateScheduledJobDetails.
        the type of scheduling this Scheduled Job follows

        Allowed values for this property are: "ONETIME", "RECURRING"


        :return: The schedule_type of this UpdateScheduledJobDetails.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this UpdateScheduledJobDetails.
        the type of scheduling this Scheduled Job follows


        :param schedule_type: The schedule_type of this UpdateScheduledJobDetails.
        :type: str
        """
        allowed_values = ["ONETIME", "RECURRING"]
        if not value_allowed_none_or_none_sentinel(schedule_type, allowed_values):
            raise ValueError(
                "Invalid value for `schedule_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._schedule_type = schedule_type

    @property
    def time_next_execution(self):
        """
        Gets the time_next_execution of this UpdateScheduledJobDetails.
        the desired time for the next execution of this Scheduled Job


        :return: The time_next_execution of this UpdateScheduledJobDetails.
        :rtype: datetime
        """
        return self._time_next_execution

    @time_next_execution.setter
    def time_next_execution(self, time_next_execution):
        """
        Sets the time_next_execution of this UpdateScheduledJobDetails.
        the desired time for the next execution of this Scheduled Job


        :param time_next_execution: The time_next_execution of this UpdateScheduledJobDetails.
        :type: datetime
        """
        self._time_next_execution = time_next_execution

    @property
    def interval_type(self):
        """
        Gets the interval_type of this UpdateScheduledJobDetails.
        the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)

        Allowed values for this property are: "HOUR", "DAY", "WEEK", "MONTH"


        :return: The interval_type of this UpdateScheduledJobDetails.
        :rtype: str
        """
        return self._interval_type

    @interval_type.setter
    def interval_type(self, interval_type):
        """
        Sets the interval_type of this UpdateScheduledJobDetails.
        the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)


        :param interval_type: The interval_type of this UpdateScheduledJobDetails.
        :type: str
        """
        allowed_values = ["HOUR", "DAY", "WEEK", "MONTH"]
        if not value_allowed_none_or_none_sentinel(interval_type, allowed_values):
            raise ValueError(
                "Invalid value for `interval_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._interval_type = interval_type

    @property
    def interval_value(self):
        """
        Gets the interval_value of this UpdateScheduledJobDetails.
        the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)


        :return: The interval_value of this UpdateScheduledJobDetails.
        :rtype: str
        """
        return self._interval_value

    @interval_value.setter
    def interval_value(self, interval_value):
        """
        Sets the interval_value of this UpdateScheduledJobDetails.
        the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)


        :param interval_value: The interval_value of this UpdateScheduledJobDetails.
        :type: str
        """
        self._interval_value = interval_value

    @property
    def operation_type(self):
        """
        Gets the operation_type of this UpdateScheduledJobDetails.
        the type of operation this Scheduled Job performs

        Allowed values for this property are: "INSTALL", "UPDATE", "REMOVE", "UPDATEALL"


        :return: The operation_type of this UpdateScheduledJobDetails.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this UpdateScheduledJobDetails.
        the type of operation this Scheduled Job performs


        :param operation_type: The operation_type of this UpdateScheduledJobDetails.
        :type: str
        """
        allowed_values = ["INSTALL", "UPDATE", "REMOVE", "UPDATEALL"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            raise ValueError(
                "Invalid value for `operation_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._operation_type = operation_type

    @property
    def update_type(self):
        """
        Gets the update_type of this UpdateScheduledJobDetails.
        Type of the update (only if operation type is UPDATEALL)

        Allowed values for this property are: "SECURITY", "BUGFIX", "ENHANCEMENT", "ALL"


        :return: The update_type of this UpdateScheduledJobDetails.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """
        Sets the update_type of this UpdateScheduledJobDetails.
        Type of the update (only if operation type is UPDATEALL)


        :param update_type: The update_type of this UpdateScheduledJobDetails.
        :type: str
        """
        allowed_values = ["SECURITY", "BUGFIX", "ENHANCEMENT", "ALL"]
        if not value_allowed_none_or_none_sentinel(update_type, allowed_values):
            raise ValueError(
                "Invalid value for `update_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._update_type = update_type

    @property
    def package_names(self):
        """
        Gets the package_names of this UpdateScheduledJobDetails.
        the id of the package (only if operation type is INSTALL/UPDATE/REMOVE)


        :return: The package_names of this UpdateScheduledJobDetails.
        :rtype: list[oci.os_management.models.PackageName]
        """
        return self._package_names

    @package_names.setter
    def package_names(self, package_names):
        """
        Sets the package_names of this UpdateScheduledJobDetails.
        the id of the package (only if operation type is INSTALL/UPDATE/REMOVE)


        :param package_names: The package_names of this UpdateScheduledJobDetails.
        :type: list[oci.os_management.models.PackageName]
        """
        self._package_names = package_names

    @property
    def update_names(self):
        """
        Gets the update_names of this UpdateScheduledJobDetails.
        The unique names of the Windows Updates (only if operation type is INSTALL).
        This is only applicable when the osFamily is for Windows managed instances.


        :return: The update_names of this UpdateScheduledJobDetails.
        :rtype: list[str]
        """
        return self._update_names

    @update_names.setter
    def update_names(self, update_names):
        """
        Sets the update_names of this UpdateScheduledJobDetails.
        The unique names of the Windows Updates (only if operation type is INSTALL).
        This is only applicable when the osFamily is for Windows managed instances.


        :param update_names: The update_names of this UpdateScheduledJobDetails.
        :type: list[str]
        """
        self._update_names = update_names

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateScheduledJobDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateScheduledJobDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateScheduledJobDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateScheduledJobDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateScheduledJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateScheduledJobDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateScheduledJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateScheduledJobDetails.
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
