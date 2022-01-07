# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyFilterRuleCase(object):
    """
    SteeringPolicyFilterRuleCase model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyFilterRuleCase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param case_condition:
            The value to assign to the case_condition property of this SteeringPolicyFilterRuleCase.
        :type case_condition: str

        :param answer_data:
            The value to assign to the answer_data property of this SteeringPolicyFilterRuleCase.
        :type answer_data: list[oci.dns.models.SteeringPolicyFilterAnswerData]

        """
        self.swagger_types = {
            'case_condition': 'str',
            'answer_data': 'list[SteeringPolicyFilterAnswerData]'
        }

        self.attribute_map = {
            'case_condition': 'caseCondition',
            'answer_data': 'answerData'
        }

        self._case_condition = None
        self._answer_data = None

    @property
    def case_condition(self):
        """
        Gets the case_condition of this SteeringPolicyFilterRuleCase.
        An expression that uses conditions at the time of a DNS query to indicate
        whether a case matches. Conditions may include the geographical location, IP
        subnet, or ASN the DNS query originated. **Example:** If you have an
        office that uses the subnet `192.0.2.0/24` you could use a `caseCondition`
        expression `query.client.subnet in ('192.0.2.0/24')` to define a case that
        matches queries from that office.


        :return: The case_condition of this SteeringPolicyFilterRuleCase.
        :rtype: str
        """
        return self._case_condition

    @case_condition.setter
    def case_condition(self, case_condition):
        """
        Sets the case_condition of this SteeringPolicyFilterRuleCase.
        An expression that uses conditions at the time of a DNS query to indicate
        whether a case matches. Conditions may include the geographical location, IP
        subnet, or ASN the DNS query originated. **Example:** If you have an
        office that uses the subnet `192.0.2.0/24` you could use a `caseCondition`
        expression `query.client.subnet in ('192.0.2.0/24')` to define a case that
        matches queries from that office.


        :param case_condition: The case_condition of this SteeringPolicyFilterRuleCase.
        :type: str
        """
        self._case_condition = case_condition

    @property
    def answer_data(self):
        """
        Gets the answer_data of this SteeringPolicyFilterRuleCase.
        An array of `SteeringPolicyFilterAnswerData` objects.


        :return: The answer_data of this SteeringPolicyFilterRuleCase.
        :rtype: list[oci.dns.models.SteeringPolicyFilterAnswerData]
        """
        return self._answer_data

    @answer_data.setter
    def answer_data(self, answer_data):
        """
        Sets the answer_data of this SteeringPolicyFilterRuleCase.
        An array of `SteeringPolicyFilterAnswerData` objects.


        :param answer_data: The answer_data of this SteeringPolicyFilterRuleCase.
        :type: list[oci.dns.models.SteeringPolicyFilterAnswerData]
        """
        self._answer_data = answer_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
