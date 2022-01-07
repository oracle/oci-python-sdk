# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .convert_to_pdb_target_base import ConvertToPdbTargetBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PdbConversionToNewDatabaseDetails(ConvertToPdbTargetBase):
    """
    Details of the new container database in which the converted pluggable database will be located.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PdbConversionToNewDatabaseDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.PdbConversionToNewDatabaseDetails.target` attribute
        of this class is ``NEW_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target:
            The value to assign to the target property of this PdbConversionToNewDatabaseDetails.
            Allowed values for this property are: "NEW_DATABASE"
        :type target: str

        :param cdb_name:
            The value to assign to the cdb_name property of this PdbConversionToNewDatabaseDetails.
        :type cdb_name: str

        :param cdb_admin_password:
            The value to assign to the cdb_admin_password property of this PdbConversionToNewDatabaseDetails.
        :type cdb_admin_password: str

        :param pdb_admin_password:
            The value to assign to the pdb_admin_password property of this PdbConversionToNewDatabaseDetails.
        :type pdb_admin_password: str

        :param cdb_tde_wallet_password:
            The value to assign to the cdb_tde_wallet_password property of this PdbConversionToNewDatabaseDetails.
        :type cdb_tde_wallet_password: str

        :param non_cdb_tde_wallet_password:
            The value to assign to the non_cdb_tde_wallet_password property of this PdbConversionToNewDatabaseDetails.
        :type non_cdb_tde_wallet_password: str

        :param additional_cdb_params:
            The value to assign to the additional_cdb_params property of this PdbConversionToNewDatabaseDetails.
        :type additional_cdb_params: str

        """
        self.swagger_types = {
            'target': 'str',
            'cdb_name': 'str',
            'cdb_admin_password': 'str',
            'pdb_admin_password': 'str',
            'cdb_tde_wallet_password': 'str',
            'non_cdb_tde_wallet_password': 'str',
            'additional_cdb_params': 'str'
        }

        self.attribute_map = {
            'target': 'target',
            'cdb_name': 'cdbName',
            'cdb_admin_password': 'cdbAdminPassword',
            'pdb_admin_password': 'pdbAdminPassword',
            'cdb_tde_wallet_password': 'cdbTdeWalletPassword',
            'non_cdb_tde_wallet_password': 'nonCdbTdeWalletPassword',
            'additional_cdb_params': 'additionalCdbParams'
        }

        self._target = None
        self._cdb_name = None
        self._cdb_admin_password = None
        self._pdb_admin_password = None
        self._cdb_tde_wallet_password = None
        self._non_cdb_tde_wallet_password = None
        self._additional_cdb_params = None
        self._target = 'NEW_DATABASE'

    @property
    def cdb_name(self):
        """
        **[Required]** Gets the cdb_name of this PdbConversionToNewDatabaseDetails.
        The database name. The name must begin with an alphabetic character and can contain a maximum of 8 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :return: The cdb_name of this PdbConversionToNewDatabaseDetails.
        :rtype: str
        """
        return self._cdb_name

    @cdb_name.setter
    def cdb_name(self, cdb_name):
        """
        Sets the cdb_name of this PdbConversionToNewDatabaseDetails.
        The database name. The name must begin with an alphabetic character and can contain a maximum of 8 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :param cdb_name: The cdb_name of this PdbConversionToNewDatabaseDetails.
        :type: str
        """
        self._cdb_name = cdb_name

    @property
    def cdb_admin_password(self):
        """
        **[Required]** Gets the cdb_admin_password of this PdbConversionToNewDatabaseDetails.
        A strong password for SYS, SYSTEM, and the plugbable database ADMIN user of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.


        :return: The cdb_admin_password of this PdbConversionToNewDatabaseDetails.
        :rtype: str
        """
        return self._cdb_admin_password

    @cdb_admin_password.setter
    def cdb_admin_password(self, cdb_admin_password):
        """
        Sets the cdb_admin_password of this PdbConversionToNewDatabaseDetails.
        A strong password for SYS, SYSTEM, and the plugbable database ADMIN user of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.


        :param cdb_admin_password: The cdb_admin_password of this PdbConversionToNewDatabaseDetails.
        :type: str
        """
        self._cdb_admin_password = cdb_admin_password

    @property
    def pdb_admin_password(self):
        """
        Gets the pdb_admin_password of this PdbConversionToNewDatabaseDetails.
        A strong password for plugbable database ADMIN user of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.


        :return: The pdb_admin_password of this PdbConversionToNewDatabaseDetails.
        :rtype: str
        """
        return self._pdb_admin_password

    @pdb_admin_password.setter
    def pdb_admin_password(self, pdb_admin_password):
        """
        Sets the pdb_admin_password of this PdbConversionToNewDatabaseDetails.
        A strong password for plugbable database ADMIN user of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.


        :param pdb_admin_password: The pdb_admin_password of this PdbConversionToNewDatabaseDetails.
        :type: str
        """
        self._pdb_admin_password = pdb_admin_password

    @property
    def cdb_tde_wallet_password(self):
        """
        Gets the cdb_tde_wallet_password of this PdbConversionToNewDatabaseDetails.
        The password to open the TDE wallet of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.


        :return: The cdb_tde_wallet_password of this PdbConversionToNewDatabaseDetails.
        :rtype: str
        """
        return self._cdb_tde_wallet_password

    @cdb_tde_wallet_password.setter
    def cdb_tde_wallet_password(self, cdb_tde_wallet_password):
        """
        Sets the cdb_tde_wallet_password of this PdbConversionToNewDatabaseDetails.
        The password to open the TDE wallet of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.


        :param cdb_tde_wallet_password: The cdb_tde_wallet_password of this PdbConversionToNewDatabaseDetails.
        :type: str
        """
        self._cdb_tde_wallet_password = cdb_tde_wallet_password

    @property
    def non_cdb_tde_wallet_password(self):
        """
        **[Required]** Gets the non_cdb_tde_wallet_password of this PdbConversionToNewDatabaseDetails.
        The existing TDE wallet password of the non-container database.


        :return: The non_cdb_tde_wallet_password of this PdbConversionToNewDatabaseDetails.
        :rtype: str
        """
        return self._non_cdb_tde_wallet_password

    @non_cdb_tde_wallet_password.setter
    def non_cdb_tde_wallet_password(self, non_cdb_tde_wallet_password):
        """
        Sets the non_cdb_tde_wallet_password of this PdbConversionToNewDatabaseDetails.
        The existing TDE wallet password of the non-container database.


        :param non_cdb_tde_wallet_password: The non_cdb_tde_wallet_password of this PdbConversionToNewDatabaseDetails.
        :type: str
        """
        self._non_cdb_tde_wallet_password = non_cdb_tde_wallet_password

    @property
    def additional_cdb_params(self):
        """
        Gets the additional_cdb_params of this PdbConversionToNewDatabaseDetails.
        Additional container database parameters.
        Example: \"_pdb_name_case_sensitive=true\"


        :return: The additional_cdb_params of this PdbConversionToNewDatabaseDetails.
        :rtype: str
        """
        return self._additional_cdb_params

    @additional_cdb_params.setter
    def additional_cdb_params(self, additional_cdb_params):
        """
        Sets the additional_cdb_params of this PdbConversionToNewDatabaseDetails.
        Additional container database parameters.
        Example: \"_pdb_name_case_sensitive=true\"


        :param additional_cdb_params: The additional_cdb_params of this PdbConversionToNewDatabaseDetails.
        :type: str
        """
        self._additional_cdb_params = additional_cdb_params

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
