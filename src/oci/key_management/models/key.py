# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Key(object):
    """
    Key model.
    """

    #: A constant which can be used with the protection_mode property of a Key.
    #: This constant has a value of "HSM"
    PROTECTION_MODE_HSM = "HSM"

    #: A constant which can be used with the protection_mode property of a Key.
    #: This constant has a value of "SOFTWARE"
    PROTECTION_MODE_SOFTWARE = "SOFTWARE"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "ENABLING"
    LIFECYCLE_STATE_ENABLING = "ENABLING"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "ENABLED"
    LIFECYCLE_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "DISABLING"
    LIFECYCLE_STATE_DISABLING = "DISABLING"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "DISABLED"
    LIFECYCLE_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "PENDING_DELETION"
    LIFECYCLE_STATE_PENDING_DELETION = "PENDING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "SCHEDULING_DELETION"
    LIFECYCLE_STATE_SCHEDULING_DELETION = "SCHEDULING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "CANCELLING_DELETION"
    LIFECYCLE_STATE_CANCELLING_DELETION = "CANCELLING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a Key.
    #: This constant has a value of "RESTORING"
    LIFECYCLE_STATE_RESTORING = "RESTORING"

    def __init__(self, **kwargs):
        """
        Initializes a new Key object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Key.
        :type compartment_id: str

        :param current_key_version:
            The value to assign to the current_key_version property of this Key.
        :type current_key_version: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Key.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Key.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Key.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Key.
        :type id: str

        :param key_shape:
            The value to assign to the key_shape property of this Key.
        :type key_shape: oci.key_management.models.KeyShape

        :param protection_mode:
            The value to assign to the protection_mode property of this Key.
            Allowed values for this property are: "HSM", "SOFTWARE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protection_mode: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Key.
            Allowed values for this property are: "CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Key.
        :type time_created: datetime

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this Key.
        :type time_of_deletion: datetime

        :param vault_id:
            The value to assign to the vault_id property of this Key.
        :type vault_id: str

        :param restored_from_key_id:
            The value to assign to the restored_from_key_id property of this Key.
        :type restored_from_key_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'current_key_version': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'key_shape': 'KeyShape',
            'protection_mode': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_of_deletion': 'datetime',
            'vault_id': 'str',
            'restored_from_key_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'current_key_version': 'currentKeyVersion',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'key_shape': 'keyShape',
            'protection_mode': 'protectionMode',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_of_deletion': 'timeOfDeletion',
            'vault_id': 'vaultId',
            'restored_from_key_id': 'restoredFromKeyId'
        }

        self._compartment_id = None
        self._current_key_version = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._key_shape = None
        self._protection_mode = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_of_deletion = None
        self._vault_id = None
        self._restored_from_key_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Key.
        The OCID of the compartment that contains this master encryption key.


        :return: The compartment_id of this Key.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Key.
        The OCID of the compartment that contains this master encryption key.


        :param compartment_id: The compartment_id of this Key.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def current_key_version(self):
        """
        **[Required]** Gets the current_key_version of this Key.
        The OCID of the key version used in cryptographic operations. During key rotation, the service might be
        in a transitional state where this or a newer key version are used intermittently. The `currentKeyVersion`
        property is updated when the service is guaranteed to use the new key version for all subsequent encryption operations.


        :return: The current_key_version of this Key.
        :rtype: str
        """
        return self._current_key_version

    @current_key_version.setter
    def current_key_version(self, current_key_version):
        """
        Sets the current_key_version of this Key.
        The OCID of the key version used in cryptographic operations. During key rotation, the service might be
        in a transitional state where this or a newer key version are used intermittently. The `currentKeyVersion`
        property is updated when the service is guaranteed to use the new key version for all subsequent encryption operations.


        :param current_key_version: The current_key_version of this Key.
        :type: str
        """
        self._current_key_version = current_key_version

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Key.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Key.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Key.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Key.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Key.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this Key.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Key.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Key.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Key.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Key.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Key.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Key.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Key.
        The OCID of the key.


        :return: The id of this Key.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Key.
        The OCID of the key.


        :param id: The id of this Key.
        :type: str
        """
        self._id = id

    @property
    def key_shape(self):
        """
        **[Required]** Gets the key_shape of this Key.

        :return: The key_shape of this Key.
        :rtype: oci.key_management.models.KeyShape
        """
        return self._key_shape

    @key_shape.setter
    def key_shape(self, key_shape):
        """
        Sets the key_shape of this Key.

        :param key_shape: The key_shape of this Key.
        :type: oci.key_management.models.KeyShape
        """
        self._key_shape = key_shape

    @property
    def protection_mode(self):
        """
        Gets the protection_mode of this Key.
        The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed.
        A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside
        the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists
        on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,
        a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.

        Allowed values for this property are: "HSM", "SOFTWARE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protection_mode of this Key.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this Key.
        The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed.
        A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside
        the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists
        on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,
        a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.


        :param protection_mode: The protection_mode of this Key.
        :type: str
        """
        allowed_values = ["HSM", "SOFTWARE"]
        if not value_allowed_none_or_none_sentinel(protection_mode, allowed_values):
            protection_mode = 'UNKNOWN_ENUM_VALUE'
        self._protection_mode = protection_mode

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Key.
        The key's current lifecycle state.

        Example: `ENABLED`

        Allowed values for this property are: "CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Key.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Key.
        The key's current lifecycle state.

        Example: `ENABLED`


        :param lifecycle_state: The lifecycle_state of this Key.
        :type: str
        """
        allowed_values = ["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Key.
        The date and time the key was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Key.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Key.
        The date and time the key was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Key.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this Key.
        An optional property indicating when to delete the key, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this Key.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this Key.
        An optional property indicating when to delete the key, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this Key.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def vault_id(self):
        """
        **[Required]** Gets the vault_id of this Key.
        The OCID of the vault that contains this key.


        :return: The vault_id of this Key.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this Key.
        The OCID of the vault that contains this key.


        :param vault_id: The vault_id of this Key.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def restored_from_key_id(self):
        """
        Gets the restored_from_key_id of this Key.
        The OCID of the key from which this key was restored.


        :return: The restored_from_key_id of this Key.
        :rtype: str
        """
        return self._restored_from_key_id

    @restored_from_key_id.setter
    def restored_from_key_id(self, restored_from_key_id):
        """
        Sets the restored_from_key_id of this Key.
        The OCID of the key from which this key was restored.


        :param restored_from_key_id: The restored_from_key_id of this Key.
        :type: str
        """
        self._restored_from_key_id = restored_from_key_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
