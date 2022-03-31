# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityAssessment(object):
    """
    A security assessment that provides an overall insight into your database security posture.
    The security assessment results are based on the analysis of your database configurations,
    user accounts, and security controls. For more information, see `Security Assessment Overview`__.

    __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/security-assessment-overview.html
    """

    #: A constant which can be used with the lifecycle_state property of a SecurityAssessment.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SecurityAssessment.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a SecurityAssessment.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SecurityAssessment.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SecurityAssessment.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SecurityAssessment.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the triggered_by property of a SecurityAssessment.
    #: This constant has a value of "USER"
    TRIGGERED_BY_USER = "USER"

    #: A constant which can be used with the triggered_by property of a SecurityAssessment.
    #: This constant has a value of "SYSTEM"
    TRIGGERED_BY_SYSTEM = "SYSTEM"

    #: A constant which can be used with the type property of a SecurityAssessment.
    #: This constant has a value of "LATEST"
    TYPE_LATEST = "LATEST"

    #: A constant which can be used with the type property of a SecurityAssessment.
    #: This constant has a value of "SAVED"
    TYPE_SAVED = "SAVED"

    #: A constant which can be used with the type property of a SecurityAssessment.
    #: This constant has a value of "SAVE_SCHEDULE"
    TYPE_SAVE_SCHEDULE = "SAVE_SCHEDULE"

    #: A constant which can be used with the type property of a SecurityAssessment.
    #: This constant has a value of "COMPARTMENT"
    TYPE_COMPARTMENT = "COMPARTMENT"

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityAssessment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SecurityAssessment.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this SecurityAssessment.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SecurityAssessment.
        :type time_updated: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this SecurityAssessment.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this SecurityAssessment.
        :type display_name: str

        :param target_ids:
            The value to assign to the target_ids property of this SecurityAssessment.
        :type target_ids: list[str]

        :param ignored_targets:
            The value to assign to the ignored_targets property of this SecurityAssessment.
        :type ignored_targets: list[object]

        :param ignored_assessment_ids:
            The value to assign to the ignored_assessment_ids property of this SecurityAssessment.
        :type ignored_assessment_ids: list[object]

        :param target_version:
            The value to assign to the target_version property of this SecurityAssessment.
        :type target_version: str

        :param is_baseline:
            The value to assign to the is_baseline property of this SecurityAssessment.
        :type is_baseline: bool

        :param is_deviated_from_baseline:
            The value to assign to the is_deviated_from_baseline property of this SecurityAssessment.
        :type is_deviated_from_baseline: bool

        :param last_compared_baseline_id:
            The value to assign to the last_compared_baseline_id property of this SecurityAssessment.
        :type last_compared_baseline_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SecurityAssessment.
            Allowed values for this property are: "CREATING", "SUCCEEDED", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SecurityAssessment.
        :type lifecycle_details: str

        :param schedule_security_assessment_id:
            The value to assign to the schedule_security_assessment_id property of this SecurityAssessment.
        :type schedule_security_assessment_id: str

        :param triggered_by:
            The value to assign to the triggered_by property of this SecurityAssessment.
            Allowed values for this property are: "USER", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type triggered_by: str

        :param description:
            The value to assign to the description property of this SecurityAssessment.
        :type description: str

        :param schedule:
            The value to assign to the schedule property of this SecurityAssessment.
        :type schedule: str

        :param link:
            The value to assign to the link property of this SecurityAssessment.
        :type link: str

        :param type:
            The value to assign to the type property of this SecurityAssessment.
            Allowed values for this property are: "LATEST", "SAVED", "SAVE_SCHEDULE", "COMPARTMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param statistics:
            The value to assign to the statistics property of this SecurityAssessment.
        :type statistics: oci.data_safe.models.SecurityAssessmentStatistics

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SecurityAssessment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SecurityAssessment.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SecurityAssessment.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'compartment_id': 'str',
            'display_name': 'str',
            'target_ids': 'list[str]',
            'ignored_targets': 'list[object]',
            'ignored_assessment_ids': 'list[object]',
            'target_version': 'str',
            'is_baseline': 'bool',
            'is_deviated_from_baseline': 'bool',
            'last_compared_baseline_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'schedule_security_assessment_id': 'str',
            'triggered_by': 'str',
            'description': 'str',
            'schedule': 'str',
            'link': 'str',
            'type': 'str',
            'statistics': 'SecurityAssessmentStatistics',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'target_ids': 'targetIds',
            'ignored_targets': 'ignoredTargets',
            'ignored_assessment_ids': 'ignoredAssessmentIds',
            'target_version': 'targetVersion',
            'is_baseline': 'isBaseline',
            'is_deviated_from_baseline': 'isDeviatedFromBaseline',
            'last_compared_baseline_id': 'lastComparedBaselineId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'schedule_security_assessment_id': 'scheduleSecurityAssessmentId',
            'triggered_by': 'triggeredBy',
            'description': 'description',
            'schedule': 'schedule',
            'link': 'link',
            'type': 'type',
            'statistics': 'statistics',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._time_created = None
        self._time_updated = None
        self._compartment_id = None
        self._display_name = None
        self._target_ids = None
        self._ignored_targets = None
        self._ignored_assessment_ids = None
        self._target_version = None
        self._is_baseline = None
        self._is_deviated_from_baseline = None
        self._last_compared_baseline_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._schedule_security_assessment_id = None
        self._triggered_by = None
        self._description = None
        self._schedule = None
        self._link = None
        self._type = None
        self._statistics = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SecurityAssessment.
        The OCID of the security assessment.


        :return: The id of this SecurityAssessment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityAssessment.
        The OCID of the security assessment.


        :param id: The id of this SecurityAssessment.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SecurityAssessment.
        The date and time when the security assessment was created. Conforms to the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this SecurityAssessment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecurityAssessment.
        The date and time when the security assessment was created. Conforms to the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this SecurityAssessment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this SecurityAssessment.
        The date and time when the security assessment was last updated. Conforms to the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this SecurityAssessment.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SecurityAssessment.
        The date and time when the security assessment was last updated. Conforms to the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this SecurityAssessment.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SecurityAssessment.
        The OCID of the compartment that contains the security assessment.


        :return: The compartment_id of this SecurityAssessment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SecurityAssessment.
        The OCID of the compartment that contains the security assessment.


        :param compartment_id: The compartment_id of this SecurityAssessment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SecurityAssessment.
        The display name of the security assessment.


        :return: The display_name of this SecurityAssessment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SecurityAssessment.
        The display name of the security assessment.


        :param display_name: The display_name of this SecurityAssessment.
        :type: str
        """
        self._display_name = display_name

    @property
    def target_ids(self):
        """
        **[Required]** Gets the target_ids of this SecurityAssessment.
        Array of database target OCIDs.


        :return: The target_ids of this SecurityAssessment.
        :rtype: list[str]
        """
        return self._target_ids

    @target_ids.setter
    def target_ids(self, target_ids):
        """
        Sets the target_ids of this SecurityAssessment.
        Array of database target OCIDs.


        :param target_ids: The target_ids of this SecurityAssessment.
        :type: list[str]
        """
        self._target_ids = target_ids

    @property
    def ignored_targets(self):
        """
        Gets the ignored_targets of this SecurityAssessment.
        List containing maps as values.
        Example: `{\"Operations\": [ {\"CostCenter\": \"42\"} ] }`


        :return: The ignored_targets of this SecurityAssessment.
        :rtype: list[object]
        """
        return self._ignored_targets

    @ignored_targets.setter
    def ignored_targets(self, ignored_targets):
        """
        Sets the ignored_targets of this SecurityAssessment.
        List containing maps as values.
        Example: `{\"Operations\": [ {\"CostCenter\": \"42\"} ] }`


        :param ignored_targets: The ignored_targets of this SecurityAssessment.
        :type: list[object]
        """
        self._ignored_targets = ignored_targets

    @property
    def ignored_assessment_ids(self):
        """
        Gets the ignored_assessment_ids of this SecurityAssessment.
        List containing maps as values.
        Example: `{\"Operations\": [ {\"CostCenter\": \"42\"} ] }`


        :return: The ignored_assessment_ids of this SecurityAssessment.
        :rtype: list[object]
        """
        return self._ignored_assessment_ids

    @ignored_assessment_ids.setter
    def ignored_assessment_ids(self, ignored_assessment_ids):
        """
        Sets the ignored_assessment_ids of this SecurityAssessment.
        List containing maps as values.
        Example: `{\"Operations\": [ {\"CostCenter\": \"42\"} ] }`


        :param ignored_assessment_ids: The ignored_assessment_ids of this SecurityAssessment.
        :type: list[object]
        """
        self._ignored_assessment_ids = ignored_assessment_ids

    @property
    def target_version(self):
        """
        Gets the target_version of this SecurityAssessment.
        The version of the target database.


        :return: The target_version of this SecurityAssessment.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """
        Sets the target_version of this SecurityAssessment.
        The version of the target database.


        :param target_version: The target_version of this SecurityAssessment.
        :type: str
        """
        self._target_version = target_version

    @property
    def is_baseline(self):
        """
        Gets the is_baseline of this SecurityAssessment.
        Indicates whether or not the security assessment is set as a baseline. This is applicable only for saved security assessments.


        :return: The is_baseline of this SecurityAssessment.
        :rtype: bool
        """
        return self._is_baseline

    @is_baseline.setter
    def is_baseline(self, is_baseline):
        """
        Sets the is_baseline of this SecurityAssessment.
        Indicates whether or not the security assessment is set as a baseline. This is applicable only for saved security assessments.


        :param is_baseline: The is_baseline of this SecurityAssessment.
        :type: bool
        """
        self._is_baseline = is_baseline

    @property
    def is_deviated_from_baseline(self):
        """
        Gets the is_deviated_from_baseline of this SecurityAssessment.
        Indicates if the assessment has deviated from the baseline.


        :return: The is_deviated_from_baseline of this SecurityAssessment.
        :rtype: bool
        """
        return self._is_deviated_from_baseline

    @is_deviated_from_baseline.setter
    def is_deviated_from_baseline(self, is_deviated_from_baseline):
        """
        Sets the is_deviated_from_baseline of this SecurityAssessment.
        Indicates if the assessment has deviated from the baseline.


        :param is_deviated_from_baseline: The is_deviated_from_baseline of this SecurityAssessment.
        :type: bool
        """
        self._is_deviated_from_baseline = is_deviated_from_baseline

    @property
    def last_compared_baseline_id(self):
        """
        Gets the last_compared_baseline_id of this SecurityAssessment.
        The OCID of the baseline against which the latest security assessment was compared.


        :return: The last_compared_baseline_id of this SecurityAssessment.
        :rtype: str
        """
        return self._last_compared_baseline_id

    @last_compared_baseline_id.setter
    def last_compared_baseline_id(self, last_compared_baseline_id):
        """
        Sets the last_compared_baseline_id of this SecurityAssessment.
        The OCID of the baseline against which the latest security assessment was compared.


        :param last_compared_baseline_id: The last_compared_baseline_id of this SecurityAssessment.
        :type: str
        """
        self._last_compared_baseline_id = last_compared_baseline_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SecurityAssessment.
        The current state of the security assessment.

        Allowed values for this property are: "CREATING", "SUCCEEDED", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SecurityAssessment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SecurityAssessment.
        The current state of the security assessment.


        :param lifecycle_state: The lifecycle_state of this SecurityAssessment.
        :type: str
        """
        allowed_values = ["CREATING", "SUCCEEDED", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this SecurityAssessment.
        Details about the current state of the security assessment.


        :return: The lifecycle_details of this SecurityAssessment.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SecurityAssessment.
        Details about the current state of the security assessment.


        :param lifecycle_details: The lifecycle_details of this SecurityAssessment.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def schedule_security_assessment_id(self):
        """
        Gets the schedule_security_assessment_id of this SecurityAssessment.
        The OCID of the security assessment that is responsible for creating this scheduled save assessment.


        :return: The schedule_security_assessment_id of this SecurityAssessment.
        :rtype: str
        """
        return self._schedule_security_assessment_id

    @schedule_security_assessment_id.setter
    def schedule_security_assessment_id(self, schedule_security_assessment_id):
        """
        Sets the schedule_security_assessment_id of this SecurityAssessment.
        The OCID of the security assessment that is responsible for creating this scheduled save assessment.


        :param schedule_security_assessment_id: The schedule_security_assessment_id of this SecurityAssessment.
        :type: str
        """
        self._schedule_security_assessment_id = schedule_security_assessment_id

    @property
    def triggered_by(self):
        """
        Gets the triggered_by of this SecurityAssessment.
        Indicates whether the security assessment was created by system or by a user.

        Allowed values for this property are: "USER", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The triggered_by of this SecurityAssessment.
        :rtype: str
        """
        return self._triggered_by

    @triggered_by.setter
    def triggered_by(self, triggered_by):
        """
        Sets the triggered_by of this SecurityAssessment.
        Indicates whether the security assessment was created by system or by a user.


        :param triggered_by: The triggered_by of this SecurityAssessment.
        :type: str
        """
        allowed_values = ["USER", "SYSTEM"]
        if not value_allowed_none_or_none_sentinel(triggered_by, allowed_values):
            triggered_by = 'UNKNOWN_ENUM_VALUE'
        self._triggered_by = triggered_by

    @property
    def description(self):
        """
        Gets the description of this SecurityAssessment.
        The description of the security assessment.


        :return: The description of this SecurityAssessment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SecurityAssessment.
        The description of the security assessment.


        :param description: The description of this SecurityAssessment.
        :type: str
        """
        self._description = description

    @property
    def schedule(self):
        """
        Gets the schedule of this SecurityAssessment.
        Schedule to save the assessment periodically in the specified format:
        <version-string>;<version-specific-schedule>

        Allowed version strings - \"v1\"
        v1's version specific schedule -<ss> <mm> <hh> <day-of-week> <day-of-month>
        Each of the above fields potentially introduce constraints. A workrequest is created only
        when clock time satisfies all the constraints. Constraints introduced:
        1. seconds = <ss> (So, the allowed range for <ss> is [0, 59])
        2. minutes = <mm> (So, the allowed range for <mm> is [0, 59])
        3. hours = <hh> (So, the allowed range for <hh> is [0, 23])
        <day-of-week> can be either '*' (without quotes or a number between 1(Monday) and 7(Sunday))
        4. No constraint introduced when it is '*'. When not, day of week must equal the given value
        <day-of-month> can be either '*' (without quotes or a number between 1 and 28)
        5. No constraint introduced when it is '*'. When not, day of month must equal the given value


        :return: The schedule of this SecurityAssessment.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this SecurityAssessment.
        Schedule to save the assessment periodically in the specified format:
        <version-string>;<version-specific-schedule>

        Allowed version strings - \"v1\"
        v1's version specific schedule -<ss> <mm> <hh> <day-of-week> <day-of-month>
        Each of the above fields potentially introduce constraints. A workrequest is created only
        when clock time satisfies all the constraints. Constraints introduced:
        1. seconds = <ss> (So, the allowed range for <ss> is [0, 59])
        2. minutes = <mm> (So, the allowed range for <mm> is [0, 59])
        3. hours = <hh> (So, the allowed range for <hh> is [0, 23])
        <day-of-week> can be either '*' (without quotes or a number between 1(Monday) and 7(Sunday))
        4. No constraint introduced when it is '*'. When not, day of week must equal the given value
        <day-of-month> can be either '*' (without quotes or a number between 1 and 28)
        5. No constraint introduced when it is '*'. When not, day of month must equal the given value


        :param schedule: The schedule of this SecurityAssessment.
        :type: str
        """
        self._schedule = schedule

    @property
    def link(self):
        """
        Gets the link of this SecurityAssessment.
        The summary of findings for the security assessment


        :return: The link of this SecurityAssessment.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this SecurityAssessment.
        The summary of findings for the security assessment


        :param link: The link of this SecurityAssessment.
        :type: str
        """
        self._link = link

    @property
    def type(self):
        """
        **[Required]** Gets the type of this SecurityAssessment.
        The type of this security assessment. The possible types are:

        LATEST: The most up-to-date assessment that is running automatically for a target. It is system generated.
        SAVED: A saved security assessment. LATEST assessments are always saved in order to maintain the history of runs. A SAVED assessment is also generated by a 'refresh' action (triggered by the user).
        SAVE_SCHEDULE: The schedule for periodic saves of LATEST assessments.
        COMPARTMENT: An automatically managed assessment type that stores all details of targets in one compartment.
         This type keeps an up-to-date assessment of all database risks in one compartment. It is automatically updated when
         the latest assessment or refresh action is executed. It is also automatically updated when a target is deleted or move to a different compartment.

        Allowed values for this property are: "LATEST", "SAVED", "SAVE_SCHEDULE", "COMPARTMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this SecurityAssessment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SecurityAssessment.
        The type of this security assessment. The possible types are:

        LATEST: The most up-to-date assessment that is running automatically for a target. It is system generated.
        SAVED: A saved security assessment. LATEST assessments are always saved in order to maintain the history of runs. A SAVED assessment is also generated by a 'refresh' action (triggered by the user).
        SAVE_SCHEDULE: The schedule for periodic saves of LATEST assessments.
        COMPARTMENT: An automatically managed assessment type that stores all details of targets in one compartment.
         This type keeps an up-to-date assessment of all database risks in one compartment. It is automatically updated when
         the latest assessment or refresh action is executed. It is also automatically updated when a target is deleted or move to a different compartment.


        :param type: The type of this SecurityAssessment.
        :type: str
        """
        allowed_values = ["LATEST", "SAVED", "SAVE_SCHEDULE", "COMPARTMENT"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def statistics(self):
        """
        Gets the statistics of this SecurityAssessment.

        :return: The statistics of this SecurityAssessment.
        :rtype: oci.data_safe.models.SecurityAssessmentStatistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """
        Sets the statistics of this SecurityAssessment.

        :param statistics: The statistics of this SecurityAssessment.
        :type: oci.data_safe.models.SecurityAssessmentStatistics
        """
        self._statistics = statistics

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SecurityAssessment.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SecurityAssessment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SecurityAssessment.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SecurityAssessment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SecurityAssessment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SecurityAssessment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SecurityAssessment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SecurityAssessment.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SecurityAssessment.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this SecurityAssessment.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SecurityAssessment.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this SecurityAssessment.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
