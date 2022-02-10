# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlertPolicy(object):
    """
    An Alert Policy is a set of alerting rules evaluated against a target.
    The alert policy is said to be satisfied when all rules in the policy evaulate to true.
    If there are three rules: rule1,rule2 and rule3, the policy is satisfied if rule1 AND rule2 AND rule3 is True.
    """

    #: A constant which can be used with the alert_policy_type property of a AlertPolicy.
    #: This constant has a value of "AUDITING"
    ALERT_POLICY_TYPE_AUDITING = "AUDITING"

    #: A constant which can be used with the alert_policy_type property of a AlertPolicy.
    #: This constant has a value of "SECURITY_ASSESSMENT"
    ALERT_POLICY_TYPE_SECURITY_ASSESSMENT = "SECURITY_ASSESSMENT"

    #: A constant which can be used with the alert_policy_type property of a AlertPolicy.
    #: This constant has a value of "USER_ASSESSMENT"
    ALERT_POLICY_TYPE_USER_ASSESSMENT = "USER_ASSESSMENT"

    #: A constant which can be used with the severity property of a AlertPolicy.
    #: This constant has a value of "CRITICAL"
    SEVERITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the severity property of a AlertPolicy.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a AlertPolicy.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the severity property of a AlertPolicy.
    #: This constant has a value of "LOW"
    SEVERITY_LOW = "LOW"

    #: A constant which can be used with the severity property of a AlertPolicy.
    #: This constant has a value of "EVALUATE"
    SEVERITY_EVALUATE = "EVALUATE"

    #: A constant which can be used with the lifecycle_state property of a AlertPolicy.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AlertPolicy.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AlertPolicy.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AlertPolicy.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AlertPolicy.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AlertPolicy.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AlertPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AlertPolicy.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AlertPolicy.
        :type display_name: str

        :param description:
            The value to assign to the description property of this AlertPolicy.
        :type description: str

        :param alert_policy_type:
            The value to assign to the alert_policy_type property of this AlertPolicy.
            Allowed values for this property are: "AUDITING", "SECURITY_ASSESSMENT", "USER_ASSESSMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type alert_policy_type: str

        :param is_user_defined:
            The value to assign to the is_user_defined property of this AlertPolicy.
        :type is_user_defined: bool

        :param severity:
            The value to assign to the severity property of this AlertPolicy.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "EVALUATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AlertPolicy.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this AlertPolicy.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AlertPolicy.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AlertPolicy.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AlertPolicy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AlertPolicy.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AlertPolicy.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'alert_policy_type': 'str',
            'is_user_defined': 'bool',
            'severity': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'alert_policy_type': 'alertPolicyType',
            'is_user_defined': 'isUserDefined',
            'severity': 'severity',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._alert_policy_type = None
        self._is_user_defined = None
        self._severity = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AlertPolicy.
        The OCID of the alert policy.


        :return: The id of this AlertPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AlertPolicy.
        The OCID of the alert policy.


        :param id: The id of this AlertPolicy.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AlertPolicy.
        The display name of the alert policy.


        :return: The display_name of this AlertPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AlertPolicy.
        The display name of the alert policy.


        :param display_name: The display_name of this AlertPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this AlertPolicy.
        The description of the alert policy.


        :return: The description of this AlertPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AlertPolicy.
        The description of the alert policy.


        :param description: The description of this AlertPolicy.
        :type: str
        """
        self._description = description

    @property
    def alert_policy_type(self):
        """
        Gets the alert_policy_type of this AlertPolicy.
        Indicates the Data Safe feature to which the alert policy belongs.

        Allowed values for this property are: "AUDITING", "SECURITY_ASSESSMENT", "USER_ASSESSMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The alert_policy_type of this AlertPolicy.
        :rtype: str
        """
        return self._alert_policy_type

    @alert_policy_type.setter
    def alert_policy_type(self, alert_policy_type):
        """
        Sets the alert_policy_type of this AlertPolicy.
        Indicates the Data Safe feature to which the alert policy belongs.


        :param alert_policy_type: The alert_policy_type of this AlertPolicy.
        :type: str
        """
        allowed_values = ["AUDITING", "SECURITY_ASSESSMENT", "USER_ASSESSMENT"]
        if not value_allowed_none_or_none_sentinel(alert_policy_type, allowed_values):
            alert_policy_type = 'UNKNOWN_ENUM_VALUE'
        self._alert_policy_type = alert_policy_type

    @property
    def is_user_defined(self):
        """
        Gets the is_user_defined of this AlertPolicy.
        Indicates if the alert policy is user-defined (true) or pre-defined (false).


        :return: The is_user_defined of this AlertPolicy.
        :rtype: bool
        """
        return self._is_user_defined

    @is_user_defined.setter
    def is_user_defined(self, is_user_defined):
        """
        Sets the is_user_defined of this AlertPolicy.
        Indicates if the alert policy is user-defined (true) or pre-defined (false).


        :param is_user_defined: The is_user_defined of this AlertPolicy.
        :type: bool
        """
        self._is_user_defined = is_user_defined

    @property
    def severity(self):
        """
        Gets the severity of this AlertPolicy.
        Severity level of the alert raised by this policy.

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "EVALUATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this AlertPolicy.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this AlertPolicy.
        Severity level of the alert raised by this policy.


        :param severity: The severity of this AlertPolicy.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "EVALUATE"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AlertPolicy.
        The OCID of the compartment that contains the alert policy.


        :return: The compartment_id of this AlertPolicy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AlertPolicy.
        The OCID of the compartment that contains the alert policy.


        :param compartment_id: The compartment_id of this AlertPolicy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AlertPolicy.
        Creation date and time of the alert policy, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this AlertPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AlertPolicy.
        Creation date and time of the alert policy, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this AlertPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AlertPolicy.
        Last date and time the alert policy was updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this AlertPolicy.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AlertPolicy.
        Last date and time the alert policy was updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this AlertPolicy.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AlertPolicy.
        The current state of the alert.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AlertPolicy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AlertPolicy.
        The current state of the alert.


        :param lifecycle_state: The lifecycle_state of this AlertPolicy.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AlertPolicy.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AlertPolicy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AlertPolicy.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AlertPolicy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AlertPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AlertPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AlertPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AlertPolicy.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AlertPolicy.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this AlertPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AlertPolicy.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this AlertPolicy.
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
