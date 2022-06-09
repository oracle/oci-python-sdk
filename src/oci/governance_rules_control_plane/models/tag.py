# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Tag(object):
    """
    Details of the tag that is being created.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Tag object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Tag.
        :type name: str

        :param description:
            The value to assign to the description property of this Tag.
        :type description: str

        :param is_cost_tracking:
            The value to assign to the is_cost_tracking property of this Tag.
        :type is_cost_tracking: bool

        :param validator:
            The value to assign to the validator property of this Tag.
        :type validator: oci.governance_rules_control_plane.models.BaseTagDefinitionValidator

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'is_cost_tracking': 'bool',
            'validator': 'BaseTagDefinitionValidator'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'is_cost_tracking': 'isCostTracking',
            'validator': 'validator'
        }

        self._name = None
        self._description = None
        self._is_cost_tracking = None
        self._validator = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Tag.
        The name you assign to the tag during creation. This is the tag key definition.
        The name must be unique within the tag namespace and cannot be changed.


        :return: The name of this Tag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tag.
        The name you assign to the tag during creation. This is the tag key definition.
        The name must be unique within the tag namespace and cannot be changed.


        :param name: The name of this Tag.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Tag.
        The description assigned to the tag during creation.


        :return: The description of this Tag.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Tag.
        The description assigned to the tag during creation.


        :param description: The description of this Tag.
        :type: str
        """
        self._description = description

    @property
    def is_cost_tracking(self):
        """
        Gets the is_cost_tracking of this Tag.
        Indicates whether the tag is enabled for cost tracking.


        :return: The is_cost_tracking of this Tag.
        :rtype: bool
        """
        return self._is_cost_tracking

    @is_cost_tracking.setter
    def is_cost_tracking(self, is_cost_tracking):
        """
        Sets the is_cost_tracking of this Tag.
        Indicates whether the tag is enabled for cost tracking.


        :param is_cost_tracking: The is_cost_tracking of this Tag.
        :type: bool
        """
        self._is_cost_tracking = is_cost_tracking

    @property
    def validator(self):
        """
        Gets the validator of this Tag.

        :return: The validator of this Tag.
        :rtype: oci.governance_rules_control_plane.models.BaseTagDefinitionValidator
        """
        return self._validator

    @validator.setter
    def validator(self, validator):
        """
        Sets the validator of this Tag.

        :param validator: The validator of this Tag.
        :type: oci.governance_rules_control_plane.models.BaseTagDefinitionValidator
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
