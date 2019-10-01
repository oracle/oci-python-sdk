# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .base_tag_definition_validator import BaseTagDefinitionValidator
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DefaultTagDefinitionValidator(BaseTagDefinitionValidator):
    """
    This is the default validatorType for definedTag. This is same as not setting any value on the validator field.
    By default only string value can be set for this definedTag.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DefaultTagDefinitionValidator object with values from keyword arguments. The default value of the :py:attr:`~oci.identity.models.DefaultTagDefinitionValidator.validator_type` attribute
        of this class is ``DEFAULT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param validator_type:
            The value to assign to the validator_type property of this DefaultTagDefinitionValidator.
            Allowed values for this property are: "ENUM", "DEFAULT"
        :type validator_type: str

        """
        self.swagger_types = {
            'validator_type': 'str'
        }

        self.attribute_map = {
            'validator_type': 'validatorType'
        }

        self._validator_type = None
        self._validator_type = 'DEFAULT'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
