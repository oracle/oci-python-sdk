# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BaseTagDefinitionValidator(object):
    """
    Validates a definedTag value. Each validator performs validation steps in addition to the standard validation
    for definedTag values (See `Limits on Tags`__.

    If a validator is defined after a value has been set for a definedTag, then any UPDATE operation that attempts
    to change the value must pass the additional validation defined by this rule. Previously set values, that would
    fail validation, are not updated and it is possible to update other attributes of an OCI resource that contains
    a non-valid definedTag.

    To clear the validator call the UPDATE operation with DefaultTagDefinitionValidator.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Limits
    """

    #: A constant which can be used with the validator_type property of a BaseTagDefinitionValidator.
    #: This constant has a value of "ENUM"
    VALIDATOR_TYPE_ENUM = "ENUM"

    #: A constant which can be used with the validator_type property of a BaseTagDefinitionValidator.
    #: This constant has a value of "DEFAULT"
    VALIDATOR_TYPE_DEFAULT = "DEFAULT"

    def __init__(self, **kwargs):
        """
        Initializes a new BaseTagDefinitionValidator object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.identity.models.DefaultTagDefinitionValidator`
        * :class:`~oci.identity.models.EnumTagDefinitionValidator`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param validator_type:
            The value to assign to the validator_type property of this BaseTagDefinitionValidator.
            Allowed values for this property are: "ENUM", "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type validator_type: str

        """
        self.swagger_types = {
            'validator_type': 'str'
        }

        self.attribute_map = {
            'validator_type': 'validatorType'
        }

        self._validator_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['validatorType']

        if type == 'DEFAULT':
            return 'DefaultTagDefinitionValidator'

        if type == 'ENUM':
            return 'EnumTagDefinitionValidator'
        else:
            return 'BaseTagDefinitionValidator'

    @property
    def validator_type(self):
        """
        **[Required]** Gets the validator_type of this BaseTagDefinitionValidator.
        The primitive that any value set for this definedTag must be parseable as.

        Allowed values for this property are: "ENUM", "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The validator_type of this BaseTagDefinitionValidator.
        :rtype: str
        """
        return self._validator_type

    @validator_type.setter
    def validator_type(self, validator_type):
        """
        Sets the validator_type of this BaseTagDefinitionValidator.
        The primitive that any value set for this definedTag must be parseable as.


        :param validator_type: The validator_type of this BaseTagDefinitionValidator.
        :type: str
        """
        allowed_values = ["ENUM", "DEFAULT"]
        if not value_allowed_none_or_none_sentinel(validator_type, allowed_values):
            validator_type = 'UNKNOWN_ENUM_VALUE'
        self._validator_type = validator_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
