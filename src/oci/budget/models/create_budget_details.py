# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBudgetDetails(object):
    """
    The create budget details.

    Client should use 'targetType' & 'targets' to specify the target type and list of targets on which the budget is applied.

    For backwards compatibility, 'targetCompartmentId' will still be supported for all existing clients.
    However, this is considered deprecreated and all clients be upgraded to use 'targetType' & 'targets'.

    Specifying both 'targetCompartmentId' and 'targets' will cause a Bad Request.
    """

    #: A constant which can be used with the reset_period property of a CreateBudgetDetails.
    #: This constant has a value of "MONTHLY"
    RESET_PERIOD_MONTHLY = "MONTHLY"

    #: A constant which can be used with the target_type property of a CreateBudgetDetails.
    #: This constant has a value of "COMPARTMENT"
    TARGET_TYPE_COMPARTMENT = "COMPARTMENT"

    #: A constant which can be used with the target_type property of a CreateBudgetDetails.
    #: This constant has a value of "TAG"
    TARGET_TYPE_TAG = "TAG"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBudgetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateBudgetDetails.
        :type compartment_id: str

        :param target_compartment_id:
            The value to assign to the target_compartment_id property of this CreateBudgetDetails.
        :type target_compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateBudgetDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateBudgetDetails.
        :type description: str

        :param amount:
            The value to assign to the amount property of this CreateBudgetDetails.
        :type amount: float

        :param reset_period:
            The value to assign to the reset_period property of this CreateBudgetDetails.
            Allowed values for this property are: "MONTHLY"
        :type reset_period: str

        :param target_type:
            The value to assign to the target_type property of this CreateBudgetDetails.
            Allowed values for this property are: "COMPARTMENT", "TAG"
        :type target_type: str

        :param targets:
            The value to assign to the targets property of this CreateBudgetDetails.
        :type targets: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBudgetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBudgetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'target_compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'amount': 'float',
            'reset_period': 'str',
            'target_type': 'str',
            'targets': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'target_compartment_id': 'targetCompartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'amount': 'amount',
            'reset_period': 'resetPeriod',
            'target_type': 'targetType',
            'targets': 'targets',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._target_compartment_id = None
        self._display_name = None
        self._description = None
        self._amount = None
        self._reset_period = None
        self._target_type = None
        self._targets = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateBudgetDetails.
        The OCID of the compartment


        :return: The compartment_id of this CreateBudgetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateBudgetDetails.
        The OCID of the compartment


        :param compartment_id: The compartment_id of this CreateBudgetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_compartment_id(self):
        """
        Gets the target_compartment_id of this CreateBudgetDetails.
        This is DEPRECTAED. Set the target compartment id in targets instead.


        :return: The target_compartment_id of this CreateBudgetDetails.
        :rtype: str
        """
        return self._target_compartment_id

    @target_compartment_id.setter
    def target_compartment_id(self, target_compartment_id):
        """
        Sets the target_compartment_id of this CreateBudgetDetails.
        This is DEPRECTAED. Set the target compartment id in targets instead.


        :param target_compartment_id: The target_compartment_id of this CreateBudgetDetails.
        :type: str
        """
        self._target_compartment_id = target_compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateBudgetDetails.
        The displayName of the budget.


        :return: The display_name of this CreateBudgetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateBudgetDetails.
        The displayName of the budget.


        :param display_name: The display_name of this CreateBudgetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateBudgetDetails.
        The description of the budget.


        :return: The description of this CreateBudgetDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateBudgetDetails.
        The description of the budget.


        :param description: The description of this CreateBudgetDetails.
        :type: str
        """
        self._description = description

    @property
    def amount(self):
        """
        **[Required]** Gets the amount of this CreateBudgetDetails.
        The amount of the budget expressed as a whole number in the currency of the customer's rate card.


        :return: The amount of this CreateBudgetDetails.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this CreateBudgetDetails.
        The amount of the budget expressed as a whole number in the currency of the customer's rate card.


        :param amount: The amount of this CreateBudgetDetails.
        :type: float
        """
        self._amount = amount

    @property
    def reset_period(self):
        """
        **[Required]** Gets the reset_period of this CreateBudgetDetails.
        The reset period for the budget.

        Allowed values for this property are: "MONTHLY"


        :return: The reset_period of this CreateBudgetDetails.
        :rtype: str
        """
        return self._reset_period

    @reset_period.setter
    def reset_period(self, reset_period):
        """
        Sets the reset_period of this CreateBudgetDetails.
        The reset period for the budget.


        :param reset_period: The reset_period of this CreateBudgetDetails.
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
    def target_type(self):
        """
        Gets the target_type of this CreateBudgetDetails.
        The type of target on which the budget is applied.

        Allowed values for this property are: "COMPARTMENT", "TAG"


        :return: The target_type of this CreateBudgetDetails.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """
        Sets the target_type of this CreateBudgetDetails.
        The type of target on which the budget is applied.


        :param target_type: The target_type of this CreateBudgetDetails.
        :type: str
        """
        allowed_values = ["COMPARTMENT", "TAG"]
        if not value_allowed_none_or_none_sentinel(target_type, allowed_values):
            raise ValueError(
                "Invalid value for `target_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._target_type = target_type

    @property
    def targets(self):
        """
        Gets the targets of this CreateBudgetDetails.
        The list of targets on which the budget is applied.
          If targetType is \"COMPARTMENT\", targets contains list of compartment OCIDs.
          If targetType is \"TAG\", targets contains list of cost tracking tag identifiers in the form of \"{tagNamespace}.{tagKey}.{tagValue}\".
        Curerntly, the array should contain EXACT ONE item.


        :return: The targets of this CreateBudgetDetails.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this CreateBudgetDetails.
        The list of targets on which the budget is applied.
          If targetType is \"COMPARTMENT\", targets contains list of compartment OCIDs.
          If targetType is \"TAG\", targets contains list of cost tracking tag identifiers in the form of \"{tagNamespace}.{tagKey}.{tagValue}\".
        Curerntly, the array should contain EXACT ONE item.


        :param targets: The targets of this CreateBudgetDetails.
        :type: list[str]
        """
        self._targets = targets

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateBudgetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateBudgetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateBudgetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateBudgetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateBudgetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateBudgetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateBudgetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateBudgetDetails.
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
