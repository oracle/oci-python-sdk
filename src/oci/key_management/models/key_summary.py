# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeySummary(object):
    """
    KeySummary model.
    """

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "ENABLING"
    LIFECYCLE_STATE_ENABLING = "ENABLING"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "ENABLED"
    LIFECYCLE_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "DISABLING"
    LIFECYCLE_STATE_DISABLING = "DISABLING"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "DISABLED"
    LIFECYCLE_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "PENDING_DELETION"
    LIFECYCLE_STATE_PENDING_DELETION = "PENDING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "SCHEDULING_DELETION"
    LIFECYCLE_STATE_SCHEDULING_DELETION = "SCHEDULING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "CANCELLING_DELETION"
    LIFECYCLE_STATE_CANCELLING_DELETION = "CANCELLING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a KeySummary.
    #: This constant has a value of "RESTORING"
    LIFECYCLE_STATE_RESTORING = "RESTORING"

    #: A constant which can be used with the protection_mode property of a KeySummary.
    #: This constant has a value of "HSM"
    PROTECTION_MODE_HSM = "HSM"

    #: A constant which can be used with the protection_mode property of a KeySummary.
    #: This constant has a value of "SOFTWARE"
    PROTECTION_MODE_SOFTWARE = "SOFTWARE"

    #: A constant which can be used with the algorithm property of a KeySummary.
    #: This constant has a value of "AES"
    ALGORITHM_AES = "AES"

    #: A constant which can be used with the algorithm property of a KeySummary.
    #: This constant has a value of "RSA"
    ALGORITHM_RSA = "RSA"

    #: A constant which can be used with the algorithm property of a KeySummary.
    #: This constant has a value of "ECDSA"
    ALGORITHM_ECDSA = "ECDSA"

    def __init__(self, **kwargs):
        """
        Initializes a new KeySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this KeySummary.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this KeySummary.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this KeySummary.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this KeySummary.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this KeySummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this KeySummary.
            Allowed values for this property are: "CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this KeySummary.
        :type time_created: datetime

        :param vault_id:
            The value to assign to the vault_id property of this KeySummary.
        :type vault_id: str

        :param protection_mode:
            The value to assign to the protection_mode property of this KeySummary.
            Allowed values for this property are: "HSM", "SOFTWARE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protection_mode: str

        :param algorithm:
            The value to assign to the algorithm property of this KeySummary.
            Allowed values for this property are: "AES", "RSA", "ECDSA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type algorithm: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'vault_id': 'str',
            'protection_mode': 'str',
            'algorithm': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'vault_id': 'vaultId',
            'protection_mode': 'protectionMode',
            'algorithm': 'algorithm'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._vault_id = None
        self._protection_mode = None
        self._algorithm = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this KeySummary.
        The OCID of the compartment that contains the key.


        :return: The compartment_id of this KeySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this KeySummary.
        The OCID of the compartment that contains the key.


        :param compartment_id: The compartment_id of this KeySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this KeySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this KeySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this KeySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this KeySummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this KeySummary.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this KeySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this KeySummary.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this KeySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this KeySummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this KeySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this KeySummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this KeySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this KeySummary.
        The OCID of the key.


        :return: The id of this KeySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this KeySummary.
        The OCID of the key.


        :param id: The id of this KeySummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this KeySummary.
        The key's current lifecycle state.

        Example: `ENABLED`

        Allowed values for this property are: "CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this KeySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this KeySummary.
        The key's current lifecycle state.

        Example: `ENABLED`


        :param lifecycle_state: The lifecycle_state of this KeySummary.
        :type: str
        """
        allowed_values = ["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this KeySummary.
        The date and time the key was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this KeySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this KeySummary.
        The date and time the key was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this KeySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vault_id(self):
        """
        **[Required]** Gets the vault_id of this KeySummary.
        The OCID of the vault that contains the key.


        :return: The vault_id of this KeySummary.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this KeySummary.
        The OCID of the vault that contains the key.


        :param vault_id: The vault_id of this KeySummary.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def protection_mode(self):
        """
        Gets the protection_mode of this KeySummary.
        The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed.
        A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside
        the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists
        on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,
        a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.

        Allowed values for this property are: "HSM", "SOFTWARE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protection_mode of this KeySummary.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this KeySummary.
        The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed.
        A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside
        the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists
        on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,
        a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.


        :param protection_mode: The protection_mode of this KeySummary.
        :type: str
        """
        allowed_values = ["HSM", "SOFTWARE"]
        if not value_allowed_none_or_none_sentinel(protection_mode, allowed_values):
            protection_mode = 'UNKNOWN_ENUM_VALUE'
        self._protection_mode = protection_mode

    @property
    def algorithm(self):
        """
        Gets the algorithm of this KeySummary.
        The algorithm used by a key's key versions to encrypt or decrypt data.

        Allowed values for this property are: "AES", "RSA", "ECDSA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The algorithm of this KeySummary.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """
        Sets the algorithm of this KeySummary.
        The algorithm used by a key's key versions to encrypt or decrypt data.


        :param algorithm: The algorithm of this KeySummary.
        :type: str
        """
        allowed_values = ["AES", "RSA", "ECDSA"]
        if not value_allowed_none_or_none_sentinel(algorithm, allowed_values):
            algorithm = 'UNKNOWN_ENUM_VALUE'
        self._algorithm = algorithm

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
