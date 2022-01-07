# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DerivedKeyResponse(object):
    """
    DerivedKeyResponse model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DerivedKeyResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param signing_key:
            The value to assign to the signing_key property of this DerivedKeyResponse.
        :type signing_key: str

        :param principal:
            The value to assign to the principal property of this DerivedKeyResponse.
        :type principal: oci.identity_data_plane.models.CommonPrincipal

        """
        self.swagger_types = {
            'signing_key': 'str',
            'principal': 'CommonPrincipal'
        }

        self.attribute_map = {
            'signing_key': 'signingKey',
            'principal': 'principal'
        }

        self._signing_key = None
        self._principal = None

    @property
    def signing_key(self):
        """
        **[Required]** Gets the signing_key of this DerivedKeyResponse.
        The derived key.


        :return: The signing_key of this DerivedKeyResponse.
        :rtype: str
        """
        return self._signing_key

    @signing_key.setter
    def signing_key(self, signing_key):
        """
        Sets the signing_key of this DerivedKeyResponse.
        The derived key.


        :param signing_key: The signing_key of this DerivedKeyResponse.
        :type: str
        """
        self._signing_key = signing_key

    @property
    def principal(self):
        """
        **[Required]** Gets the principal of this DerivedKeyResponse.
        The principal.


        :return: The principal of this DerivedKeyResponse.
        :rtype: oci.identity_data_plane.models.CommonPrincipal
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """
        Sets the principal of this DerivedKeyResponse.
        The principal.


        :param principal: The principal of this DerivedKeyResponse.
        :type: oci.identity_data_plane.models.CommonPrincipal
        """
        self._principal = principal

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
