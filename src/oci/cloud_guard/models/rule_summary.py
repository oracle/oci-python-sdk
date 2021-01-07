# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuleSummary(object):
    """
    Summary of rules
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RuleSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this RuleSummary.
        :type description: str

        :param parameters:
            The value to assign to the parameters property of this RuleSummary.
        :type parameters: list[oci.cloud_guard.models.OperatorSummary]

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'parameters': 'list[OperatorSummary]'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'parameters': 'parameters'
        }

        self._id = None
        self._description = None
        self._parameters = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RuleSummary.
        id of the rule


        :return: The id of this RuleSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RuleSummary.
        id of the rule


        :param id: The id of this RuleSummary.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        **[Required]** Gets the description of this RuleSummary.
        description of the rule


        :return: The description of this RuleSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RuleSummary.
        description of the rule


        :param description: The description of this RuleSummary.
        :type: str
        """
        self._description = description

    @property
    def parameters(self):
        """
        **[Required]** Gets the parameters of this RuleSummary.
        List of parameters applicable for rule


        :return: The parameters of this RuleSummary.
        :rtype: list[oci.cloud_guard.models.OperatorSummary]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this RuleSummary.
        List of parameters applicable for rule


        :param parameters: The parameters of this RuleSummary.
        :type: list[oci.cloud_guard.models.OperatorSummary]
        """
        self._parameters = parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
