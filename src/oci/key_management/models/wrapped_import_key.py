# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WrappedImportKey(object):
    """
    WrappedImportKey model.
    """

    #: A constant which can be used with the wrapping_algorithm property of a WrappedImportKey.
    #: This constant has a value of "RSA_OAEP_SHA256"
    WRAPPING_ALGORITHM_RSA_OAEP_SHA256 = "RSA_OAEP_SHA256"

    #: A constant which can be used with the wrapping_algorithm property of a WrappedImportKey.
    #: This constant has a value of "RSA_OAEP_AES_SHA256"
    WRAPPING_ALGORITHM_RSA_OAEP_AES_SHA256 = "RSA_OAEP_AES_SHA256"

    def __init__(self, **kwargs):
        """
        Initializes a new WrappedImportKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_material:
            The value to assign to the key_material property of this WrappedImportKey.
        :type key_material: str

        :param wrapping_algorithm:
            The value to assign to the wrapping_algorithm property of this WrappedImportKey.
            Allowed values for this property are: "RSA_OAEP_SHA256", "RSA_OAEP_AES_SHA256"
        :type wrapping_algorithm: str

        """
        self.swagger_types = {
            'key_material': 'str',
            'wrapping_algorithm': 'str'
        }

        self.attribute_map = {
            'key_material': 'keyMaterial',
            'wrapping_algorithm': 'wrappingAlgorithm'
        }

        self._key_material = None
        self._wrapping_algorithm = None

    @property
    def key_material(self):
        """
        **[Required]** Gets the key_material of this WrappedImportKey.
        The key material to import, wrapped by the vault's RSA public wrapping key and base64-encoded.


        :return: The key_material of this WrappedImportKey.
        :rtype: str
        """
        return self._key_material

    @key_material.setter
    def key_material(self, key_material):
        """
        Sets the key_material of this WrappedImportKey.
        The key material to import, wrapped by the vault's RSA public wrapping key and base64-encoded.


        :param key_material: The key_material of this WrappedImportKey.
        :type: str
        """
        self._key_material = key_material

    @property
    def wrapping_algorithm(self):
        """
        **[Required]** Gets the wrapping_algorithm of this WrappedImportKey.
        The wrapping mechanism to use during key import.
        `RSA_OAEP_AES_SHA256` invokes the RSA AES key wrap mechanism, which generates a temporary AES key. The temporary AES key is wrapped
        by the vault's RSA public wrapping key, creating a wrapped temporary AES key. The temporary AES key is also used to wrap the private key material.
        The wrapped temporary AES key and the wrapped exportable key material are concatenated, producing concatenated blob output that jointly represents them.
        `RSA_OAEP_SHA256` means that the exportable key material is wrapped by the vault's RSA public wrapping key.

        Allowed values for this property are: "RSA_OAEP_SHA256", "RSA_OAEP_AES_SHA256"


        :return: The wrapping_algorithm of this WrappedImportKey.
        :rtype: str
        """
        return self._wrapping_algorithm

    @wrapping_algorithm.setter
    def wrapping_algorithm(self, wrapping_algorithm):
        """
        Sets the wrapping_algorithm of this WrappedImportKey.
        The wrapping mechanism to use during key import.
        `RSA_OAEP_AES_SHA256` invokes the RSA AES key wrap mechanism, which generates a temporary AES key. The temporary AES key is wrapped
        by the vault's RSA public wrapping key, creating a wrapped temporary AES key. The temporary AES key is also used to wrap the private key material.
        The wrapped temporary AES key and the wrapped exportable key material are concatenated, producing concatenated blob output that jointly represents them.
        `RSA_OAEP_SHA256` means that the exportable key material is wrapped by the vault's RSA public wrapping key.


        :param wrapping_algorithm: The wrapping_algorithm of this WrappedImportKey.
        :type: str
        """
        allowed_values = ["RSA_OAEP_SHA256", "RSA_OAEP_AES_SHA256"]
        if not value_allowed_none_or_none_sentinel(wrapping_algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `wrapping_algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._wrapping_algorithm = wrapping_algorithm

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
