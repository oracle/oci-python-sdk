# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBudgetDetails(object):
    """
    The update budget details.
    """

    #: A constant which can be used with the reset_period property of a UpdateBudgetDetails.
    #: This constant has a value of "MONTHLY"
    RESET_PERIOD_MONTHLY = "MONTHLY"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBudgetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateBudgetDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateBudgetDetails.
        :type description: str

        :param amount:
            The value to assign to the amount property of this UpdateBudgetDetails.
        :type amount: float

        :param reset_period:
            The value to assign to the reset_period property of this UpdateBudgetDetails.
            Allowed values for this property are: "MONTHLY"
        :type reset_period: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateBudgetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateBudgetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'amount': 'float',
            'reset_period': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'amount': 'amount',
            'reset_period': 'resetPeriod',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._amount = None
        self._reset_period = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateBudgetDetails.
        The displayName of the budget.


        :return: The display_name of this UpdateBudgetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateBudgetDetails.
        The displayName of the budget.


        :param display_name: The display_name of this UpdateBudgetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateBudgetDetails.
        The description of the budget.


        :return: The description of this UpdateBudgetDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateBudgetDetails.
        The description of the budget.


        :param description: The description of this UpdateBudgetDetails.
        :type: str
        """
        self._description = description

    @property
    def amount(self):
        """
        Gets the amount of this UpdateBudgetDetails.
        The amount of the budget expressed as a whole number in the currency of the customer's rate card.


        :return: The amount of this UpdateBudgetDetails.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this UpdateBudgetDetails.
        The amount of the budget expressed as a whole number in the currency of the customer's rate card.


        :param amount: The amount of this UpdateBudgetDetails.
        :type: float
        """
        self._amount = amount

    @property
    def reset_period(self):
        """
        Gets the reset_period of this UpdateBudgetDetails.
        The reset period for the budget.

        Allowed values for this property are: "MONTHLY"


        :return: The reset_period of this UpdateBudgetDetails.
        :rtype: str
        """
        return self._reset_period

    @reset_period.setter
    def reset_period(self, reset_period):
        """
        Sets the reset_period of this UpdateBudgetDetails.
        The reset period for the budget.


        :param reset_period: The reset_period of this UpdateBudgetDetails.
        :type: str
        """
        allowed_values = ["MONTHLY"]
        if not value_allowed_none_or_none_sentinel(reset_period, allowed_values):
            raise ValueError(
                "Invalid value for `reset_period`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._reset_period = reset_period

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateBudgetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateBudgetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateBudgetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateBudgetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateBudgetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateBudgetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateBudgetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateBudgetDetails.
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
