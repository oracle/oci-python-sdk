# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityRule(object):
    """
    Security Rule used in the firewall policy rules.
    Security Rules determine whether to block or allow a session based on traffic attributes,
    such as  the source and destination IP address, protocol/port, and the HTTP(S) target URL.
    """

    #: A constant which can be used with the action property of a SecurityRule.
    #: This constant has a value of "ALLOW"
    ACTION_ALLOW = "ALLOW"

    #: A constant which can be used with the action property of a SecurityRule.
    #: This constant has a value of "DROP"
    ACTION_DROP = "DROP"

    #: A constant which can be used with the action property of a SecurityRule.
    #: This constant has a value of "REJECT"
    ACTION_REJECT = "REJECT"

    #: A constant which can be used with the action property of a SecurityRule.
    #: This constant has a value of "INSPECT"
    ACTION_INSPECT = "INSPECT"

    #: A constant which can be used with the inspection property of a SecurityRule.
    #: This constant has a value of "INTRUSION_DETECTION"
    INSPECTION_INTRUSION_DETECTION = "INTRUSION_DETECTION"

    #: A constant which can be used with the inspection property of a SecurityRule.
    #: This constant has a value of "INTRUSION_PREVENTION"
    INSPECTION_INTRUSION_PREVENTION = "INTRUSION_PREVENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SecurityRule.
        :type name: str

        :param condition:
            The value to assign to the condition property of this SecurityRule.
        :type condition: oci.network_firewall.models.SecurityRuleMatchCriteria

        :param action:
            The value to assign to the action property of this SecurityRule.
            Allowed values for this property are: "ALLOW", "DROP", "REJECT", "INSPECT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param inspection:
            The value to assign to the inspection property of this SecurityRule.
            Allowed values for this property are: "INTRUSION_DETECTION", "INTRUSION_PREVENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type inspection: str

        """
        self.swagger_types = {
            'name': 'str',
            'condition': 'SecurityRuleMatchCriteria',
            'action': 'str',
            'inspection': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'condition': 'condition',
            'action': 'action',
            'inspection': 'inspection'
        }

        self._name = None
        self._condition = None
        self._action = None
        self._inspection = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SecurityRule.
        Name for the Security rule, must be unique within the policy.


        :return: The name of this SecurityRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SecurityRule.
        Name for the Security rule, must be unique within the policy.


        :param name: The name of this SecurityRule.
        :type: str
        """
        self._name = name

    @property
    def condition(self):
        """
        **[Required]** Gets the condition of this SecurityRule.

        :return: The condition of this SecurityRule.
        :rtype: oci.network_firewall.models.SecurityRuleMatchCriteria
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this SecurityRule.

        :param condition: The condition of this SecurityRule.
        :type: oci.network_firewall.models.SecurityRuleMatchCriteria
        """
        self._condition = condition

    @property
    def action(self):
        """
        **[Required]** Gets the action of this SecurityRule.
        Types of Action on the Traffic flow.

          * ALLOW - Allows the traffic.
          * DROP - Silently drops the traffic, e.g. without sending a TCP reset.
          * REJECT - Rejects the traffic, sending a TCP reset to client and/or server as applicable.
          * INSPECT - Inspects traffic for vulnerability as specified in `inspection`, which may result in rejection.

        Allowed values for this property are: "ALLOW", "DROP", "REJECT", "INSPECT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this SecurityRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this SecurityRule.
        Types of Action on the Traffic flow.

          * ALLOW - Allows the traffic.
          * DROP - Silently drops the traffic, e.g. without sending a TCP reset.
          * REJECT - Rejects the traffic, sending a TCP reset to client and/or server as applicable.
          * INSPECT - Inspects traffic for vulnerability as specified in `inspection`, which may result in rejection.


        :param action: The action of this SecurityRule.
        :type: str
        """
        allowed_values = ["ALLOW", "DROP", "REJECT", "INSPECT"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def inspection(self):
        """
        Gets the inspection of this SecurityRule.
        Type of inspection to affect the Traffic flow. This is only applicable if action is INSPECT.

          * INTRUSION_DETECTION - Intrusion Detection.
          * INTRUSION_PREVENTION - Intrusion Detection and Prevention. Traffic classified as potentially malicious will be rejected as described in `type`.

        Allowed values for this property are: "INTRUSION_DETECTION", "INTRUSION_PREVENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The inspection of this SecurityRule.
        :rtype: str
        """
        return self._inspection

    @inspection.setter
    def inspection(self, inspection):
        """
        Sets the inspection of this SecurityRule.
        Type of inspection to affect the Traffic flow. This is only applicable if action is INSPECT.

          * INTRUSION_DETECTION - Intrusion Detection.
          * INTRUSION_PREVENTION - Intrusion Detection and Prevention. Traffic classified as potentially malicious will be rejected as described in `type`.


        :param inspection: The inspection of this SecurityRule.
        :type: str
        """
        allowed_values = ["INTRUSION_DETECTION", "INTRUSION_PREVENTION"]
        if not value_allowed_none_or_none_sentinel(inspection, allowed_values):
            inspection = 'UNKNOWN_ENUM_VALUE'
        self._inspection = inspection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
