# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Vault(object):
    """
    Vault model.
    """

    #: A constant which can be used with the lifecycle_state property of a Vault.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Vault.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Vault.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Vault.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Vault.
    #: This constant has a value of "PENDING_DELETION"
    LIFECYCLE_STATE_PENDING_DELETION = "PENDING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a Vault.
    #: This constant has a value of "SCHEDULING_DELETION"
    LIFECYCLE_STATE_SCHEDULING_DELETION = "SCHEDULING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a Vault.
    #: This constant has a value of "CANCELLING_DELETION"
    LIFECYCLE_STATE_CANCELLING_DELETION = "CANCELLING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a Vault.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Vault.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a Vault.
    #: This constant has a value of "RESTORING"
    LIFECYCLE_STATE_RESTORING = "RESTORING"

    #: A constant which can be used with the vault_type property of a Vault.
    #: This constant has a value of "VIRTUAL_PRIVATE"
    VAULT_TYPE_VIRTUAL_PRIVATE = "VIRTUAL_PRIVATE"

    #: A constant which can be used with the vault_type property of a Vault.
    #: This constant has a value of "DEFAULT"
    VAULT_TYPE_DEFAULT = "DEFAULT"

    def __init__(self, **kwargs):
        """
        Initializes a new Vault object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Vault.
        :type compartment_id: str

        :param crypto_endpoint:
            The value to assign to the crypto_endpoint property of this Vault.
        :type crypto_endpoint: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Vault.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Vault.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Vault.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Vault.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Vault.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param management_endpoint:
            The value to assign to the management_endpoint property of this Vault.
        :type management_endpoint: str

        :param time_created:
            The value to assign to the time_created property of this Vault.
        :type time_created: datetime

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this Vault.
        :type time_of_deletion: datetime

        :param vault_type:
            The value to assign to the vault_type property of this Vault.
            Allowed values for this property are: "VIRTUAL_PRIVATE", "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type vault_type: str

        :param restored_from_vault_id:
            The value to assign to the restored_from_vault_id property of this Vault.
        :type restored_from_vault_id: str

        :param wrappingkey_id:
            The value to assign to the wrappingkey_id property of this Vault.
        :type wrappingkey_id: str

        :param replica_details:
            The value to assign to the replica_details property of this Vault.
        :type replica_details: oci.key_management.models.VaultReplicaDetails

        :param is_primary:
            The value to assign to the is_primary property of this Vault.
        :type is_primary: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'crypto_endpoint': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'management_endpoint': 'str',
            'time_created': 'datetime',
            'time_of_deletion': 'datetime',
            'vault_type': 'str',
            'restored_from_vault_id': 'str',
            'wrappingkey_id': 'str',
            'replica_details': 'VaultReplicaDetails',
            'is_primary': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'crypto_endpoint': 'cryptoEndpoint',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'management_endpoint': 'managementEndpoint',
            'time_created': 'timeCreated',
            'time_of_deletion': 'timeOfDeletion',
            'vault_type': 'vaultType',
            'restored_from_vault_id': 'restoredFromVaultId',
            'wrappingkey_id': 'wrappingkeyId',
            'replica_details': 'replicaDetails',
            'is_primary': 'isPrimary'
        }

        self._compartment_id = None
        self._crypto_endpoint = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._management_endpoint = None
        self._time_created = None
        self._time_of_deletion = None
        self._vault_type = None
        self._restored_from_vault_id = None
        self._wrappingkey_id = None
        self._replica_details = None
        self._is_primary = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Vault.
        The OCID of the compartment that contains this vault.


        :return: The compartment_id of this Vault.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Vault.
        The OCID of the compartment that contains this vault.


        :param compartment_id: The compartment_id of this Vault.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def crypto_endpoint(self):
        """
        **[Required]** Gets the crypto_endpoint of this Vault.
        The service endpoint to perform cryptographic operations against. Cryptographic operations include
        `Encrypt`__, `Decrypt`__,
        and `GenerateDataEncryptionKey`__ operations.

        __ https://docs.cloud.oracle.com/api/#/en/key/latest/EncryptedData/Encrypt
        __ https://docs.cloud.oracle.com/api/#/en/key/latest/DecryptedData/Decrypt
        __ https://docs.cloud.oracle.com/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey


        :return: The crypto_endpoint of this Vault.
        :rtype: str
        """
        return self._crypto_endpoint

    @crypto_endpoint.setter
    def crypto_endpoint(self, crypto_endpoint):
        """
        Sets the crypto_endpoint of this Vault.
        The service endpoint to perform cryptographic operations against. Cryptographic operations include
        `Encrypt`__, `Decrypt`__,
        and `GenerateDataEncryptionKey`__ operations.

        __ https://docs.cloud.oracle.com/api/#/en/key/latest/EncryptedData/Encrypt
        __ https://docs.cloud.oracle.com/api/#/en/key/latest/DecryptedData/Decrypt
        __ https://docs.cloud.oracle.com/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey


        :param crypto_endpoint: The crypto_endpoint of this Vault.
        :type: str
        """
        self._crypto_endpoint = crypto_endpoint

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Vault.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Vault.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Vault.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Vault.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Vault.
        A user-friendly name for the vault. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this Vault.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Vault.
        A user-friendly name for the vault. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Vault.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Vault.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Vault.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Vault.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Vault.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Vault.
        The OCID of the vault.


        :return: The id of this Vault.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vault.
        The OCID of the vault.


        :param id: The id of this Vault.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Vault.
        The vault's current lifecycle state.

        Example: `DELETED`

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Vault.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Vault.
        The vault's current lifecycle state.

        Example: `DELETED`


        :param lifecycle_state: The lifecycle_state of this Vault.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def management_endpoint(self):
        """
        **[Required]** Gets the management_endpoint of this Vault.
        The service endpoint to perform management operations against. Management operations include \"Create,\" \"Update,\" \"List,\" \"Get,\" and \"Delete\" operations.


        :return: The management_endpoint of this Vault.
        :rtype: str
        """
        return self._management_endpoint

    @management_endpoint.setter
    def management_endpoint(self, management_endpoint):
        """
        Sets the management_endpoint of this Vault.
        The service endpoint to perform management operations against. Management operations include \"Create,\" \"Update,\" \"List,\" \"Get,\" and \"Delete\" operations.


        :param management_endpoint: The management_endpoint of this Vault.
        :type: str
        """
        self._management_endpoint = management_endpoint

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Vault.
        The date and time this vault was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Vault.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Vault.
        The date and time this vault was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Vault.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this Vault.
        An optional property to indicate when to delete the vault, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this Vault.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this Vault.
        An optional property to indicate when to delete the vault, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this Vault.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def vault_type(self):
        """
        **[Required]** Gets the vault_type of this Vault.
        The type of vault. Each type of vault stores the key with different
        degrees of isolation and has different options and pricing.

        Allowed values for this property are: "VIRTUAL_PRIVATE", "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The vault_type of this Vault.
        :rtype: str
        """
        return self._vault_type

    @vault_type.setter
    def vault_type(self, vault_type):
        """
        Sets the vault_type of this Vault.
        The type of vault. Each type of vault stores the key with different
        degrees of isolation and has different options and pricing.


        :param vault_type: The vault_type of this Vault.
        :type: str
        """
        allowed_values = ["VIRTUAL_PRIVATE", "DEFAULT"]
        if not value_allowed_none_or_none_sentinel(vault_type, allowed_values):
            vault_type = 'UNKNOWN_ENUM_VALUE'
        self._vault_type = vault_type

    @property
    def restored_from_vault_id(self):
        """
        Gets the restored_from_vault_id of this Vault.
        The OCID of the vault from which this vault was restored, if it was restored from a backup file.
        If you restore a vault to the same region, the vault retains the same OCID that it had when you
        backed up the vault.


        :return: The restored_from_vault_id of this Vault.
        :rtype: str
        """
        return self._restored_from_vault_id

    @restored_from_vault_id.setter
    def restored_from_vault_id(self, restored_from_vault_id):
        """
        Sets the restored_from_vault_id of this Vault.
        The OCID of the vault from which this vault was restored, if it was restored from a backup file.
        If you restore a vault to the same region, the vault retains the same OCID that it had when you
        backed up the vault.


        :param restored_from_vault_id: The restored_from_vault_id of this Vault.
        :type: str
        """
        self._restored_from_vault_id = restored_from_vault_id

    @property
    def wrappingkey_id(self):
        """
        **[Required]** Gets the wrappingkey_id of this Vault.
        The OCID of the vault's wrapping key.


        :return: The wrappingkey_id of this Vault.
        :rtype: str
        """
        return self._wrappingkey_id

    @wrappingkey_id.setter
    def wrappingkey_id(self, wrappingkey_id):
        """
        Sets the wrappingkey_id of this Vault.
        The OCID of the vault's wrapping key.


        :param wrappingkey_id: The wrappingkey_id of this Vault.
        :type: str
        """
        self._wrappingkey_id = wrappingkey_id

    @property
    def replica_details(self):
        """
        Gets the replica_details of this Vault.

        :return: The replica_details of this Vault.
        :rtype: oci.key_management.models.VaultReplicaDetails
        """
        return self._replica_details

    @replica_details.setter
    def replica_details(self, replica_details):
        """
        Sets the replica_details of this Vault.

        :param replica_details: The replica_details of this Vault.
        :type: oci.key_management.models.VaultReplicaDetails
        """
        self._replica_details = replica_details

    @property
    def is_primary(self):
        """
        Gets the is_primary of this Vault.

        :return: The is_primary of this Vault.
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """
        Sets the is_primary of this Vault.

        :param is_primary: The is_primary of this Vault.
        :type: bool
        """
        self._is_primary = is_primary

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
