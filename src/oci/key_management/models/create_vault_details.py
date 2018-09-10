# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVaultDetails(object):
    """
    CreateVaultDetails model.
    """

    #: A constant which can be used with the vault_type property of a CreateVaultDetails.
    #: This constant has a value of "VIRTUAL_PRIVATE"
    VAULT_TYPE_VIRTUAL_PRIVATE = "VIRTUAL_PRIVATE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVaultDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVaultDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateVaultDetails.
        :type display_name: str

        :param vault_type:
            The value to assign to the vault_type property of this CreateVaultDetails.
            Allowed values for this property are: "VIRTUAL_PRIVATE"
        :type vault_type: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'vault_type': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'vault_type': 'vaultType'
        }

        self._compartment_id = None
        self._display_name = None
        self._vault_type = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateVaultDetails.
        The OCID of the compartment where you want to create this vault.


        :return: The compartment_id of this CreateVaultDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVaultDetails.
        The OCID of the compartment where you want to create this vault.


        :param compartment_id: The compartment_id of this CreateVaultDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateVaultDetails.
        A user-friendly name for the vault. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateVaultDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVaultDetails.
        A user-friendly name for the vault. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateVaultDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def vault_type(self):
        """
        **[Required]** Gets the vault_type of this CreateVaultDetails.
        The type of vault to create. Each type of vault stores the key with different degrees of isolation and has different options and pricing.

        Allowed values for this property are: "VIRTUAL_PRIVATE"


        :return: The vault_type of this CreateVaultDetails.
        :rtype: str
        """
        return self._vault_type

    @vault_type.setter
    def vault_type(self, vault_type):
        """
        Sets the vault_type of this CreateVaultDetails.
        The type of vault to create. Each type of vault stores the key with different degrees of isolation and has different options and pricing.


        :param vault_type: The vault_type of this CreateVaultDetails.
        :type: str
        """
        allowed_values = ["VIRTUAL_PRIVATE"]
        if not value_allowed_none_or_none_sentinel(vault_type, allowed_values):
            raise ValueError(
                "Invalid value for `vault_type`, must be None or one of {0}"
                .format(allowed_values)
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
