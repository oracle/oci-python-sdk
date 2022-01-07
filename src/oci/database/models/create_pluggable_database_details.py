# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePluggableDatabaseDetails(object):
    """
    Parameters for creating a pluggable database in a specified container database (CDB).

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePluggableDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pdb_name:
            The value to assign to the pdb_name property of this CreatePluggableDatabaseDetails.
        :type pdb_name: str

        :param container_database_id:
            The value to assign to the container_database_id property of this CreatePluggableDatabaseDetails.
        :type container_database_id: str

        :param pdb_admin_password:
            The value to assign to the pdb_admin_password property of this CreatePluggableDatabaseDetails.
        :type pdb_admin_password: str

        :param tde_wallet_password:
            The value to assign to the tde_wallet_password property of this CreatePluggableDatabaseDetails.
        :type tde_wallet_password: str

        :param should_pdb_admin_account_be_locked:
            The value to assign to the should_pdb_admin_account_be_locked property of this CreatePluggableDatabaseDetails.
        :type should_pdb_admin_account_be_locked: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePluggableDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePluggableDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'pdb_name': 'str',
            'container_database_id': 'str',
            'pdb_admin_password': 'str',
            'tde_wallet_password': 'str',
            'should_pdb_admin_account_be_locked': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'pdb_name': 'pdbName',
            'container_database_id': 'containerDatabaseId',
            'pdb_admin_password': 'pdbAdminPassword',
            'tde_wallet_password': 'tdeWalletPassword',
            'should_pdb_admin_account_be_locked': 'shouldPdbAdminAccountBeLocked',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._pdb_name = None
        self._container_database_id = None
        self._pdb_admin_password = None
        self._tde_wallet_password = None
        self._should_pdb_admin_account_be_locked = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def pdb_name(self):
        """
        **[Required]** Gets the pdb_name of this CreatePluggableDatabaseDetails.
        The name for the pluggable database (PDB). The name is unique in the context of a :class:`Database`. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.


        :return: The pdb_name of this CreatePluggableDatabaseDetails.
        :rtype: str
        """
        return self._pdb_name

    @pdb_name.setter
    def pdb_name(self, pdb_name):
        """
        Sets the pdb_name of this CreatePluggableDatabaseDetails.
        The name for the pluggable database (PDB). The name is unique in the context of a :class:`Database`. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.


        :param pdb_name: The pdb_name of this CreatePluggableDatabaseDetails.
        :type: str
        """
        self._pdb_name = pdb_name

    @property
    def container_database_id(self):
        """
        **[Required]** Gets the container_database_id of this CreatePluggableDatabaseDetails.
        The `OCID`__ of the CDB

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The container_database_id of this CreatePluggableDatabaseDetails.
        :rtype: str
        """
        return self._container_database_id

    @container_database_id.setter
    def container_database_id(self, container_database_id):
        """
        Sets the container_database_id of this CreatePluggableDatabaseDetails.
        The `OCID`__ of the CDB

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param container_database_id: The container_database_id of this CreatePluggableDatabaseDetails.
        :type: str
        """
        self._container_database_id = container_database_id

    @property
    def pdb_admin_password(self):
        """
        Gets the pdb_admin_password of this CreatePluggableDatabaseDetails.
        A strong password for PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :return: The pdb_admin_password of this CreatePluggableDatabaseDetails.
        :rtype: str
        """
        return self._pdb_admin_password

    @pdb_admin_password.setter
    def pdb_admin_password(self, pdb_admin_password):
        """
        Sets the pdb_admin_password of this CreatePluggableDatabaseDetails.
        A strong password for PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :param pdb_admin_password: The pdb_admin_password of this CreatePluggableDatabaseDetails.
        :type: str
        """
        self._pdb_admin_password = pdb_admin_password

    @property
    def tde_wallet_password(self):
        """
        Gets the tde_wallet_password of this CreatePluggableDatabaseDetails.
        The existing TDE wallet password of the CDB.


        :return: The tde_wallet_password of this CreatePluggableDatabaseDetails.
        :rtype: str
        """
        return self._tde_wallet_password

    @tde_wallet_password.setter
    def tde_wallet_password(self, tde_wallet_password):
        """
        Sets the tde_wallet_password of this CreatePluggableDatabaseDetails.
        The existing TDE wallet password of the CDB.


        :param tde_wallet_password: The tde_wallet_password of this CreatePluggableDatabaseDetails.
        :type: str
        """
        self._tde_wallet_password = tde_wallet_password

    @property
    def should_pdb_admin_account_be_locked(self):
        """
        Gets the should_pdb_admin_account_be_locked of this CreatePluggableDatabaseDetails.
        The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it.
        If true, the pluggable database will be locked and user cannot login to it.


        :return: The should_pdb_admin_account_be_locked of this CreatePluggableDatabaseDetails.
        :rtype: bool
        """
        return self._should_pdb_admin_account_be_locked

    @should_pdb_admin_account_be_locked.setter
    def should_pdb_admin_account_be_locked(self, should_pdb_admin_account_be_locked):
        """
        Sets the should_pdb_admin_account_be_locked of this CreatePluggableDatabaseDetails.
        The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it.
        If true, the pluggable database will be locked and user cannot login to it.


        :param should_pdb_admin_account_be_locked: The should_pdb_admin_account_be_locked of this CreatePluggableDatabaseDetails.
        :type: bool
        """
        self._should_pdb_admin_account_be_locked = should_pdb_admin_account_be_locked

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreatePluggableDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreatePluggableDatabaseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreatePluggableDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreatePluggableDatabaseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreatePluggableDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreatePluggableDatabaseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreatePluggableDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreatePluggableDatabaseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
