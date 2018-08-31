# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


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

    #: A constant which can be used with the vault_type property of a Vault.
    #: This constant has a value of "VIRTUAL_PRIVATE"
    VAULT_TYPE_VIRTUAL_PRIVATE = "VIRTUAL_PRIVATE"

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
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", 'UNKNOWN_ENUM_VALUE'.
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
            Allowed values for this property are: "VIRTUAL_PRIVATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type vault_type: str

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
            'vault_type': 'str'
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
            'vault_type': 'vaultType'
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
        The service endpoint to perform cryptographic operations against. Cryptographic operations include 'Encrypt,' 'Decrypt,' and 'GenerateDataEncryptionKey' operations.


        :return: The crypto_endpoint of this Vault.
        :rtype: str
        """
        return self._crypto_endpoint

    @crypto_endpoint.setter
    def crypto_endpoint(self, crypto_endpoint):
        """
        Sets the crypto_endpoint of this Vault.
        The service endpoint to perform cryptographic operations against. Cryptographic operations include 'Encrypt,' 'Decrypt,' and 'GenerateDataEncryptionKey' operations.


        :param crypto_endpoint: The crypto_endpoint of this Vault.
        :type: str
        """
        self._crypto_endpoint = crypto_endpoint

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Vault.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :return: The defined_tags of this Vault.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Vault.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


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
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Vault.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Vault.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


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
        The vault's current state.

        Example: `DELETED`

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Vault.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Vault.
        The vault's current state.

        Example: `DELETED`


        :param lifecycle_state: The lifecycle_state of this Vault.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def management_endpoint(self):
        """
        **[Required]** Gets the management_endpoint of this Vault.
        The service endpoint to perform management operations against. Management operations include 'Create,' 'Update,' 'List,' 'Get,' and 'Delete' operations.


        :return: The management_endpoint of this Vault.
        :rtype: str
        """
        return self._management_endpoint

    @management_endpoint.setter
    def management_endpoint(self, management_endpoint):
        """
        Sets the management_endpoint of this Vault.
        The service endpoint to perform management operations against. Management operations include 'Create,' 'Update,' 'List,' 'Get,' and 'Delete' operations.


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
        An optional property for the deletion time of the Vault expressed in `RFC 3339`__ timestamp format.
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
        An optional property for the deletion time of the Vault expressed in `RFC 3339`__ timestamp format.
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
        The type of vault. Each type of vault stores the key with different degrees of isolation and has different options and pricing.

        Allowed values for this property are: "VIRTUAL_PRIVATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The vault_type of this Vault.
        :rtype: str
        """
        return self._vault_type

    @vault_type.setter
    def vault_type(self, vault_type):
        """
        Sets the vault_type of this Vault.
        The type of vault. Each type of vault stores the key with different degrees of isolation and has different options and pricing.


        :param vault_type: The vault_type of this Vault.
        :type: str
        """
        allowed_values = ["VIRTUAL_PRIVATE"]
        if not value_allowed_none_or_none_sentinel(vault_type, allowed_values):
            vault_type = 'UNKNOWN_ENUM_VALUE'
        self._vault_type = vault_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
