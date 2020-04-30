# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WrappingKey(object):
    """
    WrappingKey model.
    """

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "ENABLING"
    LIFECYCLE_STATE_ENABLING = "ENABLING"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "ENABLED"
    LIFECYCLE_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "DISABLING"
    LIFECYCLE_STATE_DISABLING = "DISABLING"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "DISABLED"
    LIFECYCLE_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "PENDING_DELETION"
    LIFECYCLE_STATE_PENDING_DELETION = "PENDING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "SCHEDULING_DELETION"
    LIFECYCLE_STATE_SCHEDULING_DELETION = "SCHEDULING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "CANCELLING_DELETION"
    LIFECYCLE_STATE_CANCELLING_DELETION = "CANCELLING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a WrappingKey.
    #: This constant has a value of "RESTORING"
    LIFECYCLE_STATE_RESTORING = "RESTORING"

    def __init__(self, **kwargs):
        """
        Initializes a new WrappingKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this WrappingKey.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this WrappingKey.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this WrappingKey.
            Allowed values for this property are: "CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param public_key:
            The value to assign to the public_key property of this WrappingKey.
        :type public_key: str

        :param time_created:
            The value to assign to the time_created property of this WrappingKey.
        :type time_created: datetime

        :param vault_id:
            The value to assign to the vault_id property of this WrappingKey.
        :type vault_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'public_key': 'str',
            'time_created': 'datetime',
            'vault_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'public_key': 'publicKey',
            'time_created': 'timeCreated',
            'vault_id': 'vaultId'
        }

        self._compartment_id = None
        self._id = None
        self._lifecycle_state = None
        self._public_key = None
        self._time_created = None
        self._vault_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WrappingKey.
        The OCID of the compartment that contains this key.


        :return: The compartment_id of this WrappingKey.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WrappingKey.
        The OCID of the compartment that contains this key.


        :param compartment_id: The compartment_id of this WrappingKey.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WrappingKey.
        The OCID of the key.


        :return: The id of this WrappingKey.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WrappingKey.
        The OCID of the key.


        :param id: The id of this WrappingKey.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this WrappingKey.
        The key's current lifecycle state.

        Example: `ENABLED`

        Allowed values for this property are: "CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this WrappingKey.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this WrappingKey.
        The key's current lifecycle state.

        Example: `ENABLED`


        :param lifecycle_state: The lifecycle_state of this WrappingKey.
        :type: str
        """
        allowed_values = ["CREATING", "ENABLING", "ENABLED", "DISABLING", "DISABLED", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", "UPDATING", "BACKUP_IN_PROGRESS", "RESTORING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def public_key(self):
        """
        **[Required]** Gets the public_key of this WrappingKey.
        The public key in PEM format to encrypt the key material before importing it with ImportKey/ImportKeyVersion.


        :return: The public_key of this WrappingKey.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this WrappingKey.
        The public key in PEM format to encrypt the key material before importing it with ImportKey/ImportKeyVersion.


        :param public_key: The public_key of this WrappingKey.
        :type: str
        """
        self._public_key = public_key

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this WrappingKey.
        The date and time the key was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this WrappingKey.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this WrappingKey.
        The date and time the key was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this WrappingKey.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vault_id(self):
        """
        **[Required]** Gets the vault_id of this WrappingKey.
        The OCID of the vault that contains this key.


        :return: The vault_id of this WrappingKey.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this WrappingKey.
        The OCID of the vault that contains this key.


        :param vault_id: The vault_id of this WrappingKey.
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
