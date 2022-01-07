# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateRoutingPolicyDetails(object):
    """
    An updated list of routing rules that overwrites the existing list of routing rules.
    """

    #: A constant which can be used with the condition_language_version property of a UpdateRoutingPolicyDetails.
    #: This constant has a value of "V1"
    CONDITION_LANGUAGE_VERSION_V1 = "V1"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateRoutingPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param condition_language_version:
            The value to assign to the condition_language_version property of this UpdateRoutingPolicyDetails.
            Allowed values for this property are: "V1"
        :type condition_language_version: str

        :param rules:
            The value to assign to the rules property of this UpdateRoutingPolicyDetails.
        :type rules: list[oci.load_balancer.models.RoutingRule]

        """
        self.swagger_types = {
            'condition_language_version': 'str',
            'rules': 'list[RoutingRule]'
        }

        self.attribute_map = {
            'condition_language_version': 'conditionLanguageVersion',
            'rules': 'rules'
        }

        self._condition_language_version = None
        self._rules = None

    @property
    def condition_language_version(self):
        """
        Gets the condition_language_version of this UpdateRoutingPolicyDetails.
        The version of the language in which `condition` of `rules` are composed.

        Allowed values for this property are: "V1"


        :return: The condition_language_version of this UpdateRoutingPolicyDetails.
        :rtype: str
        """
        return self._condition_language_version

    @condition_language_version.setter
    def condition_language_version(self, condition_language_version):
        """
        Sets the condition_language_version of this UpdateRoutingPolicyDetails.
        The version of the language in which `condition` of `rules` are composed.


        :param condition_language_version: The condition_language_version of this UpdateRoutingPolicyDetails.
        :type: str
        """
        allowed_values = ["V1"]
        if not value_allowed_none_or_none_sentinel(condition_language_version, allowed_values):
            raise ValueError(
                "Invalid value for `condition_language_version`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._condition_language_version = condition_language_version

    @property
    def rules(self):
        """
        **[Required]** Gets the rules of this UpdateRoutingPolicyDetails.
        The list of routing rules.


        :return: The rules of this UpdateRoutingPolicyDetails.
        :rtype: list[oci.load_balancer.models.RoutingRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this UpdateRoutingPolicyDetails.
        The list of routing rules.


        :param rules: The rules of this UpdateRoutingPolicyDetails.
        :type: list[oci.load_balancer.models.RoutingRule]
        """
        self._rules = rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
