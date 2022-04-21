# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlertRule(object):
    """
    The alert rule.
    """

    #: A constant which can be used with the type property of a AlertRule.
    #: This constant has a value of "ACTUAL"
    TYPE_ACTUAL = "ACTUAL"

    #: A constant which can be used with the type property of a AlertRule.
    #: This constant has a value of "FORECAST"
    TYPE_FORECAST = "FORECAST"

    #: A constant which can be used with the threshold_type property of a AlertRule.
    #: This constant has a value of "PERCENTAGE"
    THRESHOLD_TYPE_PERCENTAGE = "PERCENTAGE"

    #: A constant which can be used with the threshold_type property of a AlertRule.
    #: This constant has a value of "ABSOLUTE"
    THRESHOLD_TYPE_ABSOLUTE = "ABSOLUTE"

    #: A constant which can be used with the lifecycle_state property of a AlertRule.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AlertRule.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new AlertRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AlertRule.
        :type id: str

        :param budget_id:
            The value to assign to the budget_id property of this AlertRule.
        :type budget_id: str

        :param display_name:
            The value to assign to the display_name property of this AlertRule.
        :type display_name: str

        :param type:
            The value to assign to the type property of this AlertRule.
            Allowed values for this property are: "ACTUAL", "FORECAST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param threshold:
            The value to assign to the threshold property of this AlertRule.
        :type threshold: float

        :param threshold_type:
            The value to assign to the threshold_type property of this AlertRule.
            Allowed values for this property are: "PERCENTAGE", "ABSOLUTE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type threshold_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AlertRule.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param message:
            The value to assign to the message property of this AlertRule.
        :type message: str

        :param description:
            The value to assign to the description property of this AlertRule.
        :type description: str

        :param version:
            The value to assign to the version property of this AlertRule.
        :type version: int

        :param recipients:
            The value to assign to the recipients property of this AlertRule.
        :type recipients: str

        :param time_created:
            The value to assign to the time_created property of this AlertRule.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AlertRule.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AlertRule.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AlertRule.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'budget_id': 'str',
            'display_name': 'str',
            'type': 'str',
            'threshold': 'float',
            'threshold_type': 'str',
            'lifecycle_state': 'str',
            'message': 'str',
            'description': 'str',
            'version': 'int',
            'recipients': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'budget_id': 'budgetId',
            'display_name': 'displayName',
            'type': 'type',
            'threshold': 'threshold',
            'threshold_type': 'thresholdType',
            'lifecycle_state': 'lifecycleState',
            'message': 'message',
            'description': 'description',
            'version': 'version',
            'recipients': 'recipients',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._budget_id = None
        self._display_name = None
        self._type = None
        self._threshold = None
        self._threshold_type = None
        self._lifecycle_state = None
        self._message = None
        self._description = None
        self._version = None
        self._recipients = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AlertRule.
        The OCID of the alert rule.


        :return: The id of this AlertRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AlertRule.
        The OCID of the alert rule.


        :param id: The id of this AlertRule.
        :type: str
        """
        self._id = id

    @property
    def budget_id(self):
        """
        **[Required]** Gets the budget_id of this AlertRule.
        The OCID of the budget.


        :return: The budget_id of this AlertRule.
        :rtype: str
        """
        return self._budget_id

    @budget_id.setter
    def budget_id(self, budget_id):
        """
        Sets the budget_id of this AlertRule.
        The OCID of the budget.


        :param budget_id: The budget_id of this AlertRule.
        :type: str
        """
        self._budget_id = budget_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AlertRule.
        The name of the alert rule. Avoid entering confidential information.


        :return: The display_name of this AlertRule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AlertRule.
        The name of the alert rule. Avoid entering confidential information.


        :param display_name: The display_name of this AlertRule.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AlertRule.
        The type of the alert. Valid values are ACTUAL (the alert triggers based on actual usage), or
        FORECAST (the alert triggers based on predicted usage).

        Allowed values for this property are: "ACTUAL", "FORECAST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AlertRule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AlertRule.
        The type of the alert. Valid values are ACTUAL (the alert triggers based on actual usage), or
        FORECAST (the alert triggers based on predicted usage).


        :param type: The type of this AlertRule.
        :type: str
        """
        allowed_values = ["ACTUAL", "FORECAST"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def threshold(self):
        """
        **[Required]** Gets the threshold of this AlertRule.
        The threshold for triggering the alert. If the thresholdType is PERCENTAGE, the maximum value is 10000.


        :return: The threshold of this AlertRule.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """
        Sets the threshold of this AlertRule.
        The threshold for triggering the alert. If the thresholdType is PERCENTAGE, the maximum value is 10000.


        :param threshold: The threshold of this AlertRule.
        :type: float
        """
        self._threshold = threshold

    @property
    def threshold_type(self):
        """
        **[Required]** Gets the threshold_type of this AlertRule.
        The type of threshold.

        Allowed values for this property are: "PERCENTAGE", "ABSOLUTE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The threshold_type of this AlertRule.
        :rtype: str
        """
        return self._threshold_type

    @threshold_type.setter
    def threshold_type(self, threshold_type):
        """
        Sets the threshold_type of this AlertRule.
        The type of threshold.


        :param threshold_type: The threshold_type of this AlertRule.
        :type: str
        """
        allowed_values = ["PERCENTAGE", "ABSOLUTE"]
        if not value_allowed_none_or_none_sentinel(threshold_type, allowed_values):
            threshold_type = 'UNKNOWN_ENUM_VALUE'
        self._threshold_type = threshold_type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AlertRule.
        The current state of the alert rule.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AlertRule.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AlertRule.
        The current state of the alert rule.


        :param lifecycle_state: The lifecycle_state of this AlertRule.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def message(self):
        """
        Gets the message of this AlertRule.
        Custom message sent when an alert is triggered.


        :return: The message of this AlertRule.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this AlertRule.
        Custom message sent when an alert is triggered.


        :param message: The message of this AlertRule.
        :type: str
        """
        self._message = message

    @property
    def description(self):
        """
        Gets the description of this AlertRule.
        The description of the alert rule.


        :return: The description of this AlertRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AlertRule.
        The description of the alert rule.


        :param description: The description of this AlertRule.
        :type: str
        """
        self._description = description

    @property
    def version(self):
        """
        Gets the version of this AlertRule.
        The version of the alert rule. Starts from 1 and increments by 1.


        :return: The version of this AlertRule.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this AlertRule.
        The version of the alert rule. Starts from 1 and increments by 1.


        :param version: The version of this AlertRule.
        :type: int
        """
        self._version = version

    @property
    def recipients(self):
        """
        **[Required]** Gets the recipients of this AlertRule.
        The delimited list of email addresses to receive the alert when it triggers.
        Delimiter characters can be a comma, space, TAB, or semicolon.


        :return: The recipients of this AlertRule.
        :rtype: str
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this AlertRule.
        The delimited list of email addresses to receive the alert when it triggers.
        Delimiter characters can be a comma, space, TAB, or semicolon.


        :param recipients: The recipients of this AlertRule.
        :type: str
        """
        self._recipients = recipients

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AlertRule.
        The time the budget was created.


        :return: The time_created of this AlertRule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AlertRule.
        The time the budget was created.


        :param time_created: The time_created of this AlertRule.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AlertRule.
        The time the budget was updated.


        :return: The time_updated of this AlertRule.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AlertRule.
        The time the budget was updated.


        :param time_updated: The time_updated of this AlertRule.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AlertRule.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AlertRule.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AlertRule.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AlertRule.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AlertRule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AlertRule.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AlertRule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AlertRule.
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
