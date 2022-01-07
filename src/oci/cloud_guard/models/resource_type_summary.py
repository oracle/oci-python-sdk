# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceTypeSummary(object):
    """
    Summary of ResourceType
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceTypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ResourceTypeSummary.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this ResourceTypeSummary.
        :type display_name: str

        :param rules:
            The value to assign to the rules property of this ResourceTypeSummary.
        :type rules: list[oci.cloud_guard.models.RuleSummary]

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'rules': 'list[RuleSummary]'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'rules': 'rules'
        }

        self._name = None
        self._display_name = None
        self._rules = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ResourceTypeSummary.
        name of the resource


        :return: The name of this ResourceTypeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ResourceTypeSummary.
        name of the resource


        :param name: The name of this ResourceTypeSummary.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ResourceTypeSummary.
        display name of the resource


        :return: The display_name of this ResourceTypeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ResourceTypeSummary.
        display name of the resource


        :param display_name: The display_name of this ResourceTypeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def rules(self):
        """
        Gets the rules of this ResourceTypeSummary.
        List of rules


        :return: The rules of this ResourceTypeSummary.
        :rtype: list[oci.cloud_guard.models.RuleSummary]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this ResourceTypeSummary.
        List of rules


        :param rules: The rules of this ResourceTypeSummary.
        :type: list[oci.cloud_guard.models.RuleSummary]
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
