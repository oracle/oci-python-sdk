# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AdditionalValidationPolicy(object):
    """
    Additional JWT validation checks.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AdditionalValidationPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param issuers:
            The value to assign to the issuers property of this AdditionalValidationPolicy.
        :type issuers: list[str]

        :param audiences:
            The value to assign to the audiences property of this AdditionalValidationPolicy.
        :type audiences: list[str]

        :param verify_claims:
            The value to assign to the verify_claims property of this AdditionalValidationPolicy.
        :type verify_claims: list[oci.apigateway.models.JsonWebTokenClaim]

        """
        self.swagger_types = {
            'issuers': 'list[str]',
            'audiences': 'list[str]',
            'verify_claims': 'list[JsonWebTokenClaim]'
        }

        self.attribute_map = {
            'issuers': 'issuers',
            'audiences': 'audiences',
            'verify_claims': 'verifyClaims'
        }

        self._issuers = None
        self._audiences = None
        self._verify_claims = None

    @property
    def issuers(self):
        """
        Gets the issuers of this AdditionalValidationPolicy.
        A list of parties that could have issued the token.


        :return: The issuers of this AdditionalValidationPolicy.
        :rtype: list[str]
        """
        return self._issuers

    @issuers.setter
    def issuers(self, issuers):
        """
        Sets the issuers of this AdditionalValidationPolicy.
        A list of parties that could have issued the token.


        :param issuers: The issuers of this AdditionalValidationPolicy.
        :type: list[str]
        """
        self._issuers = issuers

    @property
    def audiences(self):
        """
        Gets the audiences of this AdditionalValidationPolicy.
        The list of intended recipients for the token.


        :return: The audiences of this AdditionalValidationPolicy.
        :rtype: list[str]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences):
        """
        Sets the audiences of this AdditionalValidationPolicy.
        The list of intended recipients for the token.


        :param audiences: The audiences of this AdditionalValidationPolicy.
        :type: list[str]
        """
        self._audiences = audiences

    @property
    def verify_claims(self):
        """
        Gets the verify_claims of this AdditionalValidationPolicy.
        A list of claims which should be validated to consider the token valid.


        :return: The verify_claims of this AdditionalValidationPolicy.
        :rtype: list[oci.apigateway.models.JsonWebTokenClaim]
        """
        return self._verify_claims

    @verify_claims.setter
    def verify_claims(self, verify_claims):
        """
        Sets the verify_claims of this AdditionalValidationPolicy.
        A list of claims which should be validated to consider the token valid.


        :param verify_claims: The verify_claims of this AdditionalValidationPolicy.
        :type: list[oci.apigateway.models.JsonWebTokenClaim]
        """
        self._verify_claims = verify_claims

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
