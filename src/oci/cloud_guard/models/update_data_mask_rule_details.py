# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDataMaskRuleDetails(object):
    """
    The information to be updated.
    """

    #: A constant which can be used with the data_mask_categories property of a UpdateDataMaskRuleDetails.
    #: This constant has a value of "ACTOR"
    DATA_MASK_CATEGORIES_ACTOR = "ACTOR"

    #: A constant which can be used with the data_mask_categories property of a UpdateDataMaskRuleDetails.
    #: This constant has a value of "PII"
    DATA_MASK_CATEGORIES_PII = "PII"

    #: A constant which can be used with the data_mask_categories property of a UpdateDataMaskRuleDetails.
    #: This constant has a value of "PHI"
    DATA_MASK_CATEGORIES_PHI = "PHI"

    #: A constant which can be used with the data_mask_categories property of a UpdateDataMaskRuleDetails.
    #: This constant has a value of "FINANCIAL"
    DATA_MASK_CATEGORIES_FINANCIAL = "FINANCIAL"

    #: A constant which can be used with the data_mask_categories property of a UpdateDataMaskRuleDetails.
    #: This constant has a value of "LOCATION"
    DATA_MASK_CATEGORIES_LOCATION = "LOCATION"

    #: A constant which can be used with the data_mask_categories property of a UpdateDataMaskRuleDetails.
    #: This constant has a value of "CUSTOM"
    DATA_MASK_CATEGORIES_CUSTOM = "CUSTOM"

    #: A constant which can be used with the data_mask_rule_status property of a UpdateDataMaskRuleDetails.
    #: This constant has a value of "ENABLED"
    DATA_MASK_RULE_STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the data_mask_rule_status property of a UpdateDataMaskRuleDetails.
    #: This constant has a value of "DISABLED"
    DATA_MASK_RULE_STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDataMaskRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDataMaskRuleDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this UpdateDataMaskRuleDetails.
        :type compartment_id: str

        :param iam_group_id:
            The value to assign to the iam_group_id property of this UpdateDataMaskRuleDetails.
        :type iam_group_id: str

        :param target_selected:
            The value to assign to the target_selected property of this UpdateDataMaskRuleDetails.
        :type target_selected: oci.cloud_guard.models.TargetSelected

        :param data_mask_categories:
            The value to assign to the data_mask_categories property of this UpdateDataMaskRuleDetails.
            Allowed values for items in this list are: "ACTOR", "PII", "PHI", "FINANCIAL", "LOCATION", "CUSTOM"
        :type data_mask_categories: list[str]

        :param data_mask_rule_status:
            The value to assign to the data_mask_rule_status property of this UpdateDataMaskRuleDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type data_mask_rule_status: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDataMaskRuleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDataMaskRuleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'iam_group_id': 'str',
            'target_selected': 'TargetSelected',
            'data_mask_categories': 'list[str]',
            'data_mask_rule_status': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'iam_group_id': 'iamGroupId',
            'target_selected': 'targetSelected',
            'data_mask_categories': 'dataMaskCategories',
            'data_mask_rule_status': 'dataMaskRuleStatus',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._iam_group_id = None
        self._target_selected = None
        self._data_mask_categories = None
        self._data_mask_rule_status = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDataMaskRuleDetails.
        Data Mask Rule Name


        :return: The display_name of this UpdateDataMaskRuleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDataMaskRuleDetails.
        Data Mask Rule Name


        :param display_name: The display_name of this UpdateDataMaskRuleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this UpdateDataMaskRuleDetails.
        Compartment Identifier where the resource is created


        :return: The compartment_id of this UpdateDataMaskRuleDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UpdateDataMaskRuleDetails.
        Compartment Identifier where the resource is created


        :param compartment_id: The compartment_id of this UpdateDataMaskRuleDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def iam_group_id(self):
        """
        Gets the iam_group_id of this UpdateDataMaskRuleDetails.
        IAM Group id associated with the data mask rule


        :return: The iam_group_id of this UpdateDataMaskRuleDetails.
        :rtype: str
        """
        return self._iam_group_id

    @iam_group_id.setter
    def iam_group_id(self, iam_group_id):
        """
        Sets the iam_group_id of this UpdateDataMaskRuleDetails.
        IAM Group id associated with the data mask rule


        :param iam_group_id: The iam_group_id of this UpdateDataMaskRuleDetails.
        :type: str
        """
        self._iam_group_id = iam_group_id

    @property
    def target_selected(self):
        """
        Gets the target_selected of this UpdateDataMaskRuleDetails.

        :return: The target_selected of this UpdateDataMaskRuleDetails.
        :rtype: oci.cloud_guard.models.TargetSelected
        """
        return self._target_selected

    @target_selected.setter
    def target_selected(self, target_selected):
        """
        Sets the target_selected of this UpdateDataMaskRuleDetails.

        :param target_selected: The target_selected of this UpdateDataMaskRuleDetails.
        :type: oci.cloud_guard.models.TargetSelected
        """
        self._target_selected = target_selected

    @property
    def data_mask_categories(self):
        """
        Gets the data_mask_categories of this UpdateDataMaskRuleDetails.
        Data Mask Categories

        Allowed values for items in this list are: "ACTOR", "PII", "PHI", "FINANCIAL", "LOCATION", "CUSTOM"


        :return: The data_mask_categories of this UpdateDataMaskRuleDetails.
        :rtype: list[str]
        """
        return self._data_mask_categories

    @data_mask_categories.setter
    def data_mask_categories(self, data_mask_categories):
        """
        Sets the data_mask_categories of this UpdateDataMaskRuleDetails.
        Data Mask Categories


        :param data_mask_categories: The data_mask_categories of this UpdateDataMaskRuleDetails.
        :type: list[str]
        """
        allowed_values = ["ACTOR", "PII", "PHI", "FINANCIAL", "LOCATION", "CUSTOM"]

        if data_mask_categories and data_mask_categories is not NONE_SENTINEL:
            for value in data_mask_categories:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        "Invalid value for `data_mask_categories`, must be None or one of {0}"
                        .format(allowed_values)
                    )
        self._data_mask_categories = data_mask_categories

    @property
    def data_mask_rule_status(self):
        """
        Gets the data_mask_rule_status of this UpdateDataMaskRuleDetails.
        The status of the dataMaskRule.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The data_mask_rule_status of this UpdateDataMaskRuleDetails.
        :rtype: str
        """
        return self._data_mask_rule_status

    @data_mask_rule_status.setter
    def data_mask_rule_status(self, data_mask_rule_status):
        """
        Sets the data_mask_rule_status of this UpdateDataMaskRuleDetails.
        The status of the dataMaskRule.


        :param data_mask_rule_status: The data_mask_rule_status of this UpdateDataMaskRuleDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(data_mask_rule_status, allowed_values):
            raise ValueError(
                "Invalid value for `data_mask_rule_status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._data_mask_rule_status = data_mask_rule_status

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDataMaskRuleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateDataMaskRuleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDataMaskRuleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateDataMaskRuleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDataMaskRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateDataMaskRuleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDataMaskRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateDataMaskRuleDetails.
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
