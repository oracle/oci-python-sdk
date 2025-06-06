# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501

from .nat_rule_summary import NatRuleSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NatV4NatSummary(NatRuleSummary):
    """
    Request for updating NATV4 type Nat Rule used in the firewall policy.
    """

    #: A constant which can be used with the action property of a NatV4NatSummary.
    #: This constant has a value of "DIPP_SRC_NAT"
    ACTION_DIPP_SRC_NAT = "DIPP_SRC_NAT"

    def __init__(self, **kwargs):
        """
        Initializes a new NatV4NatSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.network_firewall.models.NatV4NatSummary.type` attribute
        of this class is ``NATV4`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this NatV4NatSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this NatV4NatSummary.
            Allowed values for this property are: "NATV4", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param description:
            The value to assign to the description property of this NatV4NatSummary.
        :type description: str

        :param priority_order:
            The value to assign to the priority_order property of this NatV4NatSummary.
        :type priority_order: int

        :param parent_resource_id:
            The value to assign to the parent_resource_id property of this NatV4NatSummary.
        :type parent_resource_id: str

        :param action:
            The value to assign to the action property of this NatV4NatSummary.
            Allowed values for this property are: "DIPP_SRC_NAT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param condition:
            The value to assign to the condition property of this NatV4NatSummary.
        :type condition: oci.network_firewall.models.NatRuleMatchCriteria

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'description': 'str',
            'priority_order': 'int',
            'parent_resource_id': 'str',
            'action': 'str',
            'condition': 'NatRuleMatchCriteria'
        }
        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'description': 'description',
            'priority_order': 'priorityOrder',
            'parent_resource_id': 'parentResourceId',
            'action': 'action',
            'condition': 'condition'
        }
        self._name = None
        self._type = None
        self._description = None
        self._priority_order = None
        self._parent_resource_id = None
        self._action = None
        self._condition = None
        self._type = 'NATV4'

    @property
    def action(self):
        """
        **[Required]** Gets the action of this NatV4NatSummary.
        action:

        * DIPP_SRC_NAT - Dynamic-ip-port source NAT.

        Allowed values for this property are: "DIPP_SRC_NAT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this NatV4NatSummary.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this NatV4NatSummary.
        action:

        * DIPP_SRC_NAT - Dynamic-ip-port source NAT.


        :param action: The action of this NatV4NatSummary.
        :type: str
        """
        allowed_values = ["DIPP_SRC_NAT"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def condition(self):
        """
        **[Required]** Gets the condition of this NatV4NatSummary.

        :return: The condition of this NatV4NatSummary.
        :rtype: oci.network_firewall.models.NatRuleMatchCriteria
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this NatV4NatSummary.

        :param condition: The condition of this NatV4NatSummary.
        :type: oci.network_firewall.models.NatRuleMatchCriteria
        """
        self._condition = condition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
