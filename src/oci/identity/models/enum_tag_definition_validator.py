# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .base_tag_definition_validator import BaseTagDefinitionValidator
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnumTagDefinitionValidator(BaseTagDefinitionValidator):
    """
    Validates the 'value' set for a definedTag is contained in the list of allowable 'values'.

    If the 'validatorType' is 'ENUM', then at least one valid value must be specified in the 'values' array.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnumTagDefinitionValidator object with values from keyword arguments. The default value of the :py:attr:`~oci.identity.models.EnumTagDefinitionValidator.validator_type` attribute
        of this class is ``ENUM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param validator_type:
            The value to assign to the validator_type property of this EnumTagDefinitionValidator.
            Allowed values for this property are: "ENUM", "DEFAULT"
        :type validator_type: str

        :param values:
            The value to assign to the values property of this EnumTagDefinitionValidator.
        :type values: list[str]

        """
        self.swagger_types = {
            'validator_type': 'str',
            'values': 'list[str]'
        }

        self.attribute_map = {
            'validator_type': 'validatorType',
            'values': 'values'
        }

        self._validator_type = None
        self._values = None
        self._validator_type = 'ENUM'

    @property
    def values(self):
        """
        Gets the values of this EnumTagDefinitionValidator.
        The list of allowed values for a definedTag value.


        :return: The values of this EnumTagDefinitionValidator.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this EnumTagDefinitionValidator.
        The list of allowed values for a definedTag value.


        :param values: The values of this EnumTagDefinitionValidator.
        :type: list[str]
        """
        self._values = values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
