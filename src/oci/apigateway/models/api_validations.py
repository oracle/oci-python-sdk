# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiValidations(object):
    """
    The result of validations conducted on the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApiValidations object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param validations:
            The value to assign to the validations property of this ApiValidations.
        :type validations: list[oci.apigateway.models.ApiValidationDetails]

        """
        self.swagger_types = {
            'validations': 'list[ApiValidationDetails]'
        }

        self.attribute_map = {
            'validations': 'validations'
        }

        self._validations = None

    @property
    def validations(self):
        """
        **[Required]** Gets the validations of this ApiValidations.
        API validation results.


        :return: The validations of this ApiValidations.
        :rtype: list[oci.apigateway.models.ApiValidationDetails]
        """
        return self._validations

    @validations.setter
    def validations(self, validations):
        """
        Sets the validations of this ApiValidations.
        API validation results.


        :param validations: The validations of this ApiValidations.
        :type: list[oci.apigateway.models.ApiValidationDetails]
        """
        self._validations = validations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
