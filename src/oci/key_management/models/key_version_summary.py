# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyVersionSummary(object):
    """
    KeyVersionSummary model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KeyVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this KeyVersionSummary.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this KeyVersionSummary.
        :type id: str

        :param key_id:
            The value to assign to the key_id property of this KeyVersionSummary.
        :type key_id: str

        :param time_created:
            The value to assign to the time_created property of this KeyVersionSummary.
        :type time_created: datetime

        :param vault_id:
            The value to assign to the vault_id property of this KeyVersionSummary.
        :type vault_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'id': 'str',
            'key_id': 'str',
            'time_created': 'datetime',
            'vault_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'id': 'id',
            'key_id': 'keyId',
            'time_created': 'timeCreated',
            'vault_id': 'vaultId'
        }

        self._compartment_id = None
        self._id = None
        self._key_id = None
        self._time_created = None
        self._vault_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this KeyVersionSummary.
        The OCID of the compartment that contains this key version.


        :return: The compartment_id of this KeyVersionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this KeyVersionSummary.
        The OCID of the compartment that contains this key version.


        :param compartment_id: The compartment_id of this KeyVersionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this KeyVersionSummary.
        The OCID of the key version.


        :return: The id of this KeyVersionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this KeyVersionSummary.
        The OCID of the key version.


        :param id: The id of this KeyVersionSummary.
        :type: str
        """
        self._id = id

    @property
    def key_id(self):
        """
        **[Required]** Gets the key_id of this KeyVersionSummary.
        The OCID of the key associated with this key version.


        :return: The key_id of this KeyVersionSummary.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this KeyVersionSummary.
        The OCID of the key associated with this key version.


        :param key_id: The key_id of this KeyVersionSummary.
        :type: str
        """
        self._key_id = key_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this KeyVersionSummary.
        The date and time this key version was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this KeyVersionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this KeyVersionSummary.
        The date and time this key version was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this KeyVersionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vault_id(self):
        """
        **[Required]** Gets the vault_id of this KeyVersionSummary.
        The OCID of the vault that contains this key version.


        :return: The vault_id of this KeyVersionSummary.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this KeyVersionSummary.
        The OCID of the vault that contains this key version.


        :param vault_id: The vault_id of this KeyVersionSummary.
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
