# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


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

    #: A constant which can be used with the vault_type property of a CreateVaultDetails.
    #: This constant has a value of "DEFAULT"
    VAULT_TYPE_DEFAULT = "DEFAULT"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVaultDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVaultDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVaultDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateVaultDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVaultDetails.
        :type freeform_tags: dict(str, str)

        :param vault_type:
            The value to assign to the vault_type property of this CreateVaultDetails.
            Allowed values for this property are: "VIRTUAL_PRIVATE", "DEFAULT"
        :type vault_type: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'vault_type': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'vault_type': 'vaultType'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
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
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVaultDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateVaultDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVaultDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateVaultDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

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
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVaultDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateVaultDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVaultDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateVaultDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def vault_type(self):
        """
        **[Required]** Gets the vault_type of this CreateVaultDetails.
        The type of vault to create. Each type of vault stores the key with different degrees of isolation and has different options and pricing.

        Allowed values for this property are: "VIRTUAL_PRIVATE", "DEFAULT"


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
        allowed_values = ["VIRTUAL_PRIVATE", "DEFAULT"]
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
