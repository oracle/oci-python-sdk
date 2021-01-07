# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeregisterAutonomousDatabaseDataSafeDetails(object):
    """
    Details to deregister an Autonomous Database with Data Safe.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeregisterAutonomousDatabaseDataSafeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pdb_admin_password:
            The value to assign to the pdb_admin_password property of this DeregisterAutonomousDatabaseDataSafeDetails.
        :type pdb_admin_password: str

        """
        self.swagger_types = {
            'pdb_admin_password': 'str'
        }

        self.attribute_map = {
            'pdb_admin_password': 'pdbAdminPassword'
        }

        self._pdb_admin_password = None

    @property
    def pdb_admin_password(self):
        """
        **[Required]** Gets the pdb_admin_password of this DeregisterAutonomousDatabaseDataSafeDetails.
        The admin password provided during the creation of the database. This password is between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.


        :return: The pdb_admin_password of this DeregisterAutonomousDatabaseDataSafeDetails.
        :rtype: str
        """
        return self._pdb_admin_password

    @pdb_admin_password.setter
    def pdb_admin_password(self, pdb_admin_password):
        """
        Sets the pdb_admin_password of this DeregisterAutonomousDatabaseDataSafeDetails.
        The admin password provided during the creation of the database. This password is between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.


        :param pdb_admin_password: The pdb_admin_password of this DeregisterAutonomousDatabaseDataSafeDetails.
        :type: str
        """
        self._pdb_admin_password = pdb_admin_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
