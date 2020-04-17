# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTagDetails(object):
    """
    UpdateTagDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTagDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateTagDetails.
        :type description: str

        :param is_retired:
            The value to assign to the is_retired property of this UpdateTagDetails.
        :type is_retired: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateTagDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateTagDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param is_cost_tracking:
            The value to assign to the is_cost_tracking property of this UpdateTagDetails.
        :type is_cost_tracking: bool

        :param validator:
            The value to assign to the validator property of this UpdateTagDetails.
        :type validator: BaseTagDefinitionValidator

        """
        self.swagger_types = {
            'description': 'str',
            'is_retired': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_cost_tracking': 'bool',
            'validator': 'BaseTagDefinitionValidator'
        }

        self.attribute_map = {
            'description': 'description',
            'is_retired': 'isRetired',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_cost_tracking': 'isCostTracking',
            'validator': 'validator'
        }

        self._description = None
        self._is_retired = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_cost_tracking = None
        self._validator = None

    @property
    def description(self):
        """
        Gets the description of this UpdateTagDetails.
        The description you assign to the tag during creation.


        :return: The description of this UpdateTagDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateTagDetails.
        The description you assign to the tag during creation.


        :param description: The description of this UpdateTagDetails.
        :type: str
        """
        self._description = description

    @property
    def is_retired(self):
        """
        Gets the is_retired of this UpdateTagDetails.
        Whether the tag is retired.
        See `Retiring Key Definitions and Namespace Definitions`__.

        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Retiring


        :return: The is_retired of this UpdateTagDetails.
        :rtype: bool
        """
        return self._is_retired

    @is_retired.setter
    def is_retired(self, is_retired):
        """
        Sets the is_retired of this UpdateTagDetails.
        Whether the tag is retired.
        See `Retiring Key Definitions and Namespace Definitions`__.

        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Retiring


        :param is_retired: The is_retired of this UpdateTagDetails.
        :type: bool
        """
        self._is_retired = is_retired

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateTagDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateTagDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateTagDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateTagDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateTagDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateTagDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateTagDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateTagDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_cost_tracking(self):
        """
        Gets the is_cost_tracking of this UpdateTagDetails.
        Indicates whether the tag is enabled for cost tracking.


        :return: The is_cost_tracking of this UpdateTagDetails.
        :rtype: bool
        """
        return self._is_cost_tracking

    @is_cost_tracking.setter
    def is_cost_tracking(self, is_cost_tracking):
        """
        Sets the is_cost_tracking of this UpdateTagDetails.
        Indicates whether the tag is enabled for cost tracking.


        :param is_cost_tracking: The is_cost_tracking of this UpdateTagDetails.
        :type: bool
        """
        self._is_cost_tracking = is_cost_tracking

    @property
    def validator(self):
        """
        Gets the validator of this UpdateTagDetails.
        The tag must have a value type, which is specified with a validator. Tags can use either a
        static value or a list of possible values. Static values are entered by a user applying the tag
        to a resource. Lists are created by you and the user must apply a value from the list. Lists
        are validiated.

        If you use the default validiator (or don't define a validator), the user applying the tag
        enters a value. No additional validation is performed.

        To clear the validator, call UpdateTag with
        `DefaultTagDefinitionValidator`__.

        __ https://docs.cloud.oracle.com/api/#/en/identity/latest/datatypes/DefaultTagDefinitionValidator


        :return: The validator of this UpdateTagDetails.
        :rtype: BaseTagDefinitionValidator
        """
        return self._validator

    @validator.setter
    def validator(self, validator):
        """
        Sets the validator of this UpdateTagDetails.
        The tag must have a value type, which is specified with a validator. Tags can use either a
        static value or a list of possible values. Static values are entered by a user applying the tag
        to a resource. Lists are created by you and the user must apply a value from the list. Lists
        are validiated.

        If you use the default validiator (or don't define a validator), the user applying the tag
        enters a value. No additional validation is performed.

        To clear the validator, call UpdateTag with
        `DefaultTagDefinitionValidator`__.

        __ https://docs.cloud.oracle.com/api/#/en/identity/latest/datatypes/DefaultTagDefinitionValidator


        :param validator: The validator of this UpdateTagDetails.
        :type: BaseTagDefinitionValidator
        """
        self._validator = validator

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
