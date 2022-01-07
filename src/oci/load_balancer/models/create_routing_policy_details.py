# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRoutingPolicyDetails(object):
    """
    An ordered list of routing rules.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the condition_language_version property of a CreateRoutingPolicyDetails.
    #: This constant has a value of "V1"
    CONDITION_LANGUAGE_VERSION_V1 = "V1"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRoutingPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateRoutingPolicyDetails.
        :type name: str

        :param condition_language_version:
            The value to assign to the condition_language_version property of this CreateRoutingPolicyDetails.
            Allowed values for this property are: "V1"
        :type condition_language_version: str

        :param rules:
            The value to assign to the rules property of this CreateRoutingPolicyDetails.
        :type rules: list[oci.load_balancer.models.RoutingRule]

        """
        self.swagger_types = {
            'name': 'str',
            'condition_language_version': 'str',
            'rules': 'list[RoutingRule]'
        }

        self.attribute_map = {
            'name': 'name',
            'condition_language_version': 'conditionLanguageVersion',
            'rules': 'rules'
        }

        self._name = None
        self._condition_language_version = None
        self._rules = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateRoutingPolicyDetails.
        The name for this list of routing rules. It must be unique and it cannot be changed. Avoid entering
        confidential information.

        Example: `example_routing_rules`


        :return: The name of this CreateRoutingPolicyDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateRoutingPolicyDetails.
        The name for this list of routing rules. It must be unique and it cannot be changed. Avoid entering
        confidential information.

        Example: `example_routing_rules`


        :param name: The name of this CreateRoutingPolicyDetails.
        :type: str
        """
        self._name = name

    @property
    def condition_language_version(self):
        """
        **[Required]** Gets the condition_language_version of this CreateRoutingPolicyDetails.
        The version of the language in which `condition` of `rules` are composed.

        Allowed values for this property are: "V1"


        :return: The condition_language_version of this CreateRoutingPolicyDetails.
        :rtype: str
        """
        return self._condition_language_version

    @condition_language_version.setter
    def condition_language_version(self, condition_language_version):
        """
        Sets the condition_language_version of this CreateRoutingPolicyDetails.
        The version of the language in which `condition` of `rules` are composed.


        :param condition_language_version: The condition_language_version of this CreateRoutingPolicyDetails.
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
        **[Required]** Gets the rules of this CreateRoutingPolicyDetails.
        The list of routing rules.


        :return: The rules of this CreateRoutingPolicyDetails.
        :rtype: list[oci.load_balancer.models.RoutingRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this CreateRoutingPolicyDetails.
        The list of routing rules.


        :param rules: The rules of this CreateRoutingPolicyDetails.
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
