# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AdvisorRule(object):
    """
    The details of the Optimizer Statistics Advisor rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AdvisorRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AdvisorRule.
        :type name: str

        :param description:
            The value to assign to the description property of this AdvisorRule.
        :type description: str

        :param findings:
            The value to assign to the findings property of this AdvisorRule.
        :type findings: list[oci.database_management.models.RuleFinding]

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'findings': 'list[RuleFinding]'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'findings': 'findings'
        }

        self._name = None
        self._description = None
        self._findings = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AdvisorRule.
        The name of the rule.


        :return: The name of this AdvisorRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AdvisorRule.
        The name of the rule.


        :param name: The name of this AdvisorRule.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this AdvisorRule.
        The description of the rule.


        :return: The description of this AdvisorRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AdvisorRule.
        The description of the rule.


        :param description: The description of this AdvisorRule.
        :type: str
        """
        self._description = description

    @property
    def findings(self):
        """
        **[Required]** Gets the findings of this AdvisorRule.
        The list of findings for the rule.


        :return: The findings of this AdvisorRule.
        :rtype: list[oci.database_management.models.RuleFinding]
        """
        return self._findings

    @findings.setter
    def findings(self, findings):
        """
        Sets the findings of this AdvisorRule.
        The list of findings for the rule.


        :param findings: The findings of this AdvisorRule.
        :type: list[oci.database_management.models.RuleFinding]
        """
        self._findings = findings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
