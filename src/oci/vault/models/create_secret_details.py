# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSecretDetails(object):
    """
    The details of the secret that you want to create.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSecretDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSecretDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSecretDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this CreateSecretDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSecretDetails.
        :type freeform_tags: dict(str, str)

        :param key_id:
            The value to assign to the key_id property of this CreateSecretDetails.
        :type key_id: str

        :param metadata:
            The value to assign to the metadata property of this CreateSecretDetails.
        :type metadata: dict(str, object)

        :param secret_content:
            The value to assign to the secret_content property of this CreateSecretDetails.
        :type secret_content: oci.vault.models.SecretContentDetails

        :param secret_name:
            The value to assign to the secret_name property of this CreateSecretDetails.
        :type secret_name: str

        :param secret_rules:
            The value to assign to the secret_rules property of this CreateSecretDetails.
        :type secret_rules: list[oci.vault.models.SecretRule]

        :param vault_id:
            The value to assign to the vault_id property of this CreateSecretDetails.
        :type vault_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'key_id': 'str',
            'metadata': 'dict(str, object)',
            'secret_content': 'SecretContentDetails',
            'secret_name': 'str',
            'secret_rules': 'list[SecretRule]',
            'vault_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'key_id': 'keyId',
            'metadata': 'metadata',
            'secret_content': 'secretContent',
            'secret_name': 'secretName',
            'secret_rules': 'secretRules',
            'vault_id': 'vaultId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._description = None
        self._freeform_tags = None
        self._key_id = None
        self._metadata = None
        self._secret_content = None
        self._secret_name = None
        self._secret_rules = None
        self._vault_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSecretDetails.
        The OCID of the compartment where you want to create the secret.


        :return: The compartment_id of this CreateSecretDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSecretDetails.
        The OCID of the compartment where you want to create the secret.


        :param compartment_id: The compartment_id of this CreateSecretDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSecretDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateSecretDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSecretDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateSecretDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this CreateSecretDetails.
        A brief description of the secret. Avoid entering confidential information.


        :return: The description of this CreateSecretDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateSecretDetails.
        A brief description of the secret. Avoid entering confidential information.


        :param description: The description of this CreateSecretDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSecretDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateSecretDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSecretDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateSecretDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def key_id(self):
        """
        Gets the key_id of this CreateSecretDetails.
        The OCID of the master encryption key that is used to encrypt the secret.


        :return: The key_id of this CreateSecretDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this CreateSecretDetails.
        The OCID of the master encryption key that is used to encrypt the secret.


        :param key_id: The key_id of this CreateSecretDetails.
        :type: str
        """
        self._key_id = key_id

    @property
    def metadata(self):
        """
        Gets the metadata of this CreateSecretDetails.
        Additional metadata that you can use to provide context about how to use the secret during rotation or
        other administrative tasks. For example, for a secret that you use to connect to a database, the additional
        metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.


        :return: The metadata of this CreateSecretDetails.
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateSecretDetails.
        Additional metadata that you can use to provide context about how to use the secret during rotation or
        other administrative tasks. For example, for a secret that you use to connect to a database, the additional
        metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.


        :param metadata: The metadata of this CreateSecretDetails.
        :type: dict(str, object)
        """
        self._metadata = metadata

    @property
    def secret_content(self):
        """
        **[Required]** Gets the secret_content of this CreateSecretDetails.

        :return: The secret_content of this CreateSecretDetails.
        :rtype: oci.vault.models.SecretContentDetails
        """
        return self._secret_content

    @secret_content.setter
    def secret_content(self, secret_content):
        """
        Sets the secret_content of this CreateSecretDetails.

        :param secret_content: The secret_content of this CreateSecretDetails.
        :type: oci.vault.models.SecretContentDetails
        """
        self._secret_content = secret_content

    @property
    def secret_name(self):
        """
        **[Required]** Gets the secret_name of this CreateSecretDetails.
        A user-friendly name for the secret. Secret names should be unique within a vault. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :return: The secret_name of this CreateSecretDetails.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """
        Sets the secret_name of this CreateSecretDetails.
        A user-friendly name for the secret. Secret names should be unique within a vault. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :param secret_name: The secret_name of this CreateSecretDetails.
        :type: str
        """
        self._secret_name = secret_name

    @property
    def secret_rules(self):
        """
        Gets the secret_rules of this CreateSecretDetails.
        A list of rules to control how the secret is used and managed.


        :return: The secret_rules of this CreateSecretDetails.
        :rtype: list[oci.vault.models.SecretRule]
        """
        return self._secret_rules

    @secret_rules.setter
    def secret_rules(self, secret_rules):
        """
        Sets the secret_rules of this CreateSecretDetails.
        A list of rules to control how the secret is used and managed.


        :param secret_rules: The secret_rules of this CreateSecretDetails.
        :type: list[oci.vault.models.SecretRule]
        """
        self._secret_rules = secret_rules

    @property
    def vault_id(self):
        """
        **[Required]** Gets the vault_id of this CreateSecretDetails.
        The OCID of the vault where you want to create the secret.


        :return: The vault_id of this CreateSecretDetails.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this CreateSecretDetails.
        The OCID of the vault where you want to create the secret.


        :param vault_id: The vault_id of this CreateSecretDetails.
        :type: str
        """
        self._vault_id = vault_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
