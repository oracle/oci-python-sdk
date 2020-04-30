# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VaultSummary(object):
    """
    VaultSummary model.
    """

    #: A constant which can be used with the lifecycle_state property of a VaultSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a VaultSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a VaultSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a VaultSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a VaultSummary.
    #: This constant has a value of "PENDING_DELETION"
    LIFECYCLE_STATE_PENDING_DELETION = "PENDING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a VaultSummary.
    #: This constant has a value of "SCHEDULING_DELETION"
    LIFECYCLE_STATE_SCHEDULING_DELETION = "SCHEDULING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a VaultSummary.
    #: This constant has a value of "CANCELLING_DELETION"
    LIFECYCLE_STATE_CANCELLING_DELETION = "CANCELLING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a VaultSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a VaultSummary.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a VaultSummary.
    #: This constant has a value of "RESTORING"
    LIFECYCLE_STATE_RESTORING = "RESTORING"

    #: A constant which can be used with the vault_type property of a VaultSummary.
    #: This constant has a value of "VIRTUAL_PRIVATE"
    VAULT_TYPE_VIRTUAL_PRIVATE = "VIRTUAL_PRIVATE"

    #: A constant which can be used with the vault_type property of a VaultSummary.
    #: This constant has a value of "DEFAULT"
    VAULT_TYPE_DEFAULT = "DEFAULT"

    def __init__(self, **kwargs):
        """
        Initializes a new VaultSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this VaultSummary.
        :type compartment_id: str

        :param crypto_endpoint:
            The value to assign to the crypto_endpoint property of this VaultSummary.
        :type crypto_endpoint: str

        :param defined_tags:
            The value to assign to the defined_tags property of this VaultSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this VaultSummary.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VaultSummary.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this VaultSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VaultSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param management_endpoint:
            The value to assign to the management_endpoint property of this VaultSummary.
        :type management_endpoint: str

        :param time_created:
            The value to assign to the time_created property of this VaultSummary.
        :type time_created: datetime

        :param vault_type:
            The value to assign to the vault_type property of this VaultSummary.
            Allowed values for this property are: "VIRTUAL_PRIVATE", "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
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
        self._vault_type = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this VaultSummary.
        The OCID of the compartment that contains a particular vault.


        :return: The compartment_id of this VaultSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VaultSummary.
        The OCID of the compartment that contains a particular vault.


        :param compartment_id: The compartment_id of this VaultSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def crypto_endpoint(self):
        """
        **[Required]** Gets the crypto_endpoint of this VaultSummary.
        The service endpoint to perform cryptographic operations against. Cryptographic operations include
        `Encrypt`__, `Decrypt`__,
        and `GenerateDataEncryptionKey`__ operations.

        __ https://docs.cloud.oracle.com/api/#/en/key/release/EncryptedData/Encrypt
        __ https://docs.cloud.oracle.com/api/#/en/key/release/DecryptedData/Decrypt
        __ https://docs.cloud.oracle.com/api/#/en/key/release/GeneratedKey/GenerateDataEncryptionKey


        :return: The crypto_endpoint of this VaultSummary.
        :rtype: str
        """
        return self._crypto_endpoint

    @crypto_endpoint.setter
    def crypto_endpoint(self, crypto_endpoint):
        """
        Sets the crypto_endpoint of this VaultSummary.
        The service endpoint to perform cryptographic operations against. Cryptographic operations include
        `Encrypt`__, `Decrypt`__,
        and `GenerateDataEncryptionKey`__ operations.

        __ https://docs.cloud.oracle.com/api/#/en/key/release/EncryptedData/Encrypt
        __ https://docs.cloud.oracle.com/api/#/en/key/release/DecryptedData/Decrypt
        __ https://docs.cloud.oracle.com/api/#/en/key/release/GeneratedKey/GenerateDataEncryptionKey


        :param crypto_endpoint: The crypto_endpoint of this VaultSummary.
        :type: str
        """
        self._crypto_endpoint = crypto_endpoint

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this VaultSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this VaultSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VaultSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this VaultSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this VaultSummary.
        A user-friendly name for a vault. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this VaultSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VaultSummary.
        A user-friendly name for a vault. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this VaultSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VaultSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this VaultSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VaultSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this VaultSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VaultSummary.
        The OCID of a vault.


        :return: The id of this VaultSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VaultSummary.
        The OCID of a vault.


        :param id: The id of this VaultSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VaultSummary.
        A vault's current lifecycle state.

        Example: `ACTIVE`

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VaultSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VaultSummary.
        A vault's current lifecycle state.

        Example: `ACTIVE`


        :param lifecycle_state: The lifecycle_state of this VaultSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def management_endpoint(self):
        """
        **[Required]** Gets the management_endpoint of this VaultSummary.
        The service endpoint to perform management operations against. Management operations include \"Create,\" \"Update,\" \"List,\" \"Get,\" and \"Delete\" operations.


        :return: The management_endpoint of this VaultSummary.
        :rtype: str
        """
        return self._management_endpoint

    @management_endpoint.setter
    def management_endpoint(self, management_endpoint):
        """
        Sets the management_endpoint of this VaultSummary.
        The service endpoint to perform management operations against. Management operations include \"Create,\" \"Update,\" \"List,\" \"Get,\" and \"Delete\" operations.


        :param management_endpoint: The management_endpoint of this VaultSummary.
        :type: str
        """
        self._management_endpoint = management_endpoint

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this VaultSummary.
        The date and time a vault was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this VaultSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VaultSummary.
        The date and time a vault was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this VaultSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vault_type(self):
        """
        **[Required]** Gets the vault_type of this VaultSummary.
        The type of vault. Each type of vault stores keys with different
        degrees of isolation and has different options and pricing.

        Allowed values for this property are: "VIRTUAL_PRIVATE", "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The vault_type of this VaultSummary.
        :rtype: str
        """
        return self._vault_type

    @vault_type.setter
    def vault_type(self, vault_type):
        """
        Sets the vault_type of this VaultSummary.
        The type of vault. Each type of vault stores keys with different
        degrees of isolation and has different options and pricing.


        :param vault_type: The vault_type of this VaultSummary.
        :type: str
        """
        allowed_values = ["VIRTUAL_PRIVATE", "DEFAULT"]
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
