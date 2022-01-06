# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidationRequestPolicy(object):
    """
    Top-level validation policy mixin (not directly used).
    """

    #: A constant which can be used with the validation_mode property of a ValidationRequestPolicy.
    #: This constant has a value of "ENFORCING"
    VALIDATION_MODE_ENFORCING = "ENFORCING"

    #: A constant which can be used with the validation_mode property of a ValidationRequestPolicy.
    #: This constant has a value of "PERMISSIVE"
    VALIDATION_MODE_PERMISSIVE = "PERMISSIVE"

    #: A constant which can be used with the validation_mode property of a ValidationRequestPolicy.
    #: This constant has a value of "DISABLED"
    VALIDATION_MODE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new ValidationRequestPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param validation_mode:
            The value to assign to the validation_mode property of this ValidationRequestPolicy.
            Allowed values for this property are: "ENFORCING", "PERMISSIVE", "DISABLED"
        :type validation_mode: str

        """
        self.swagger_types = {
            'validation_mode': 'str'
        }

        self.attribute_map = {
            'validation_mode': 'validationMode'
        }

        self._validation_mode = None

    @property
    def validation_mode(self):
        """
        Gets the validation_mode of this ValidationRequestPolicy.
        Validation behavior mode.

        In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
        and not sent to the backend.

        In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
        will follow the normal path.

        `DISABLED` type turns the validation off.

        Allowed values for this property are: "ENFORCING", "PERMISSIVE", "DISABLED"


        :return: The validation_mode of this ValidationRequestPolicy.
        :rtype: str
        """
        return self._validation_mode

    @validation_mode.setter
    def validation_mode(self, validation_mode):
        """
        Sets the validation_mode of this ValidationRequestPolicy.
        Validation behavior mode.

        In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
        and not sent to the backend.

        In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
        will follow the normal path.

        `DISABLED` type turns the validation off.


        :param validation_mode: The validation_mode of this ValidationRequestPolicy.
        :type: str
        """
        allowed_values = ["ENFORCING", "PERMISSIVE", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(validation_mode, allowed_values):
            raise ValueError(
                "Invalid value for `validation_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._validation_mode = validation_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
