# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .static_public_key import StaticPublicKey
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PemEncodedPublicKey(StaticPublicKey):
    """
    A PEM-encoded public key used for verifying the JWT signature.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PemEncodedPublicKey object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.PemEncodedPublicKey.format` attribute
        of this class is ``PEM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kid:
            The value to assign to the kid property of this PemEncodedPublicKey.
        :type kid: str

        :param format:
            The value to assign to the format property of this PemEncodedPublicKey.
            Allowed values for this property are: "JSON_WEB_KEY", "PEM"
        :type format: str

        :param key:
            The value to assign to the key property of this PemEncodedPublicKey.
        :type key: str

        """
        self.swagger_types = {
            'kid': 'str',
            'format': 'str',
            'key': 'str'
        }

        self.attribute_map = {
            'kid': 'kid',
            'format': 'format',
            'key': 'key'
        }

        self._kid = None
        self._format = None
        self._key = None
        self._format = 'PEM'

    @property
    def key(self):
        """
        **[Required]** Gets the key of this PemEncodedPublicKey.
        The content of the PEM-encoded public key.


        :return: The key of this PemEncodedPublicKey.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this PemEncodedPublicKey.
        The content of the PEM-encoded public key.


        :param key: The key of this PemEncodedPublicKey.
        :type: str
        """
        self._key = key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
