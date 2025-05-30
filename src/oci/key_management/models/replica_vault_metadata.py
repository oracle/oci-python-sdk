# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: release


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReplicaVaultMetadata(object):
    """
    Metadata for the replica vault, needed if different from primary vault
    """

    #: A constant which can be used with the vault_type property of a ReplicaVaultMetadata.
    #: This constant has a value of "EXTERNAL"
    VAULT_TYPE_EXTERNAL = "EXTERNAL"

    def __init__(self, **kwargs):
        """
        Initializes a new ReplicaVaultMetadata object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.key_management.models.ReplicaExternalVaultMetadata`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vault_type:
            The value to assign to the vault_type property of this ReplicaVaultMetadata.
            Allowed values for this property are: "EXTERNAL"
        :type vault_type: str

        """
        self.swagger_types = {
            'vault_type': 'str'
        }
        self.attribute_map = {
            'vault_type': 'vaultType'
        }
        self._vault_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['vaultType']

        if type == 'EXTERNAL':
            return 'ReplicaExternalVaultMetadata'
        else:
            return 'ReplicaVaultMetadata'

    @property
    def vault_type(self):
        """
        **[Required]** Gets the vault_type of this ReplicaVaultMetadata.
        The type of vault. Each type of vault stores keys with different
        degrees of isolation and has different options and pricing.

        Allowed values for this property are: "EXTERNAL"


        :return: The vault_type of this ReplicaVaultMetadata.
        :rtype: str
        """
        return self._vault_type

    @vault_type.setter
    def vault_type(self, vault_type):
        """
        Sets the vault_type of this ReplicaVaultMetadata.
        The type of vault. Each type of vault stores keys with different
        degrees of isolation and has different options and pricing.


        :param vault_type: The vault_type of this ReplicaVaultMetadata.
        :type: str
        """
        allowed_values = ["EXTERNAL"]
        if not value_allowed_none_or_none_sentinel(vault_type, allowed_values):
            raise ValueError(
                f"Invalid value for `vault_type`, must be None or one of {allowed_values}"
            )
        self._vault_type = vault_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
