# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PluggableDatabaseConnectionStrings(object):
    """
    Connection strings to connect to an Oracle Pluggable Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PluggableDatabaseConnectionStrings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pdb_default:
            The value to assign to the pdb_default property of this PluggableDatabaseConnectionStrings.
        :type pdb_default: str

        :param pdb_ip_default:
            The value to assign to the pdb_ip_default property of this PluggableDatabaseConnectionStrings.
        :type pdb_ip_default: str

        :param all_connection_strings:
            The value to assign to the all_connection_strings property of this PluggableDatabaseConnectionStrings.
        :type all_connection_strings: dict(str, str)

        """
        self.swagger_types = {
            'pdb_default': 'str',
            'pdb_ip_default': 'str',
            'all_connection_strings': 'dict(str, str)'
        }

        self.attribute_map = {
            'pdb_default': 'pdbDefault',
            'pdb_ip_default': 'pdbIpDefault',
            'all_connection_strings': 'allConnectionStrings'
        }

        self._pdb_default = None
        self._pdb_ip_default = None
        self._all_connection_strings = None

    @property
    def pdb_default(self):
        """
        Gets the pdb_default of this PluggableDatabaseConnectionStrings.
        A host name-based PDB connection string.


        :return: The pdb_default of this PluggableDatabaseConnectionStrings.
        :rtype: str
        """
        return self._pdb_default

    @pdb_default.setter
    def pdb_default(self, pdb_default):
        """
        Sets the pdb_default of this PluggableDatabaseConnectionStrings.
        A host name-based PDB connection string.


        :param pdb_default: The pdb_default of this PluggableDatabaseConnectionStrings.
        :type: str
        """
        self._pdb_default = pdb_default

    @property
    def pdb_ip_default(self):
        """
        Gets the pdb_ip_default of this PluggableDatabaseConnectionStrings.
        An IP-based PDB connection string.


        :return: The pdb_ip_default of this PluggableDatabaseConnectionStrings.
        :rtype: str
        """
        return self._pdb_ip_default

    @pdb_ip_default.setter
    def pdb_ip_default(self, pdb_ip_default):
        """
        Sets the pdb_ip_default of this PluggableDatabaseConnectionStrings.
        An IP-based PDB connection string.


        :param pdb_ip_default: The pdb_ip_default of this PluggableDatabaseConnectionStrings.
        :type: str
        """
        self._pdb_ip_default = pdb_ip_default

    @property
    def all_connection_strings(self):
        """
        Gets the all_connection_strings of this PluggableDatabaseConnectionStrings.
        All connection strings to use to connect to the pluggable database.


        :return: The all_connection_strings of this PluggableDatabaseConnectionStrings.
        :rtype: dict(str, str)
        """
        return self._all_connection_strings

    @all_connection_strings.setter
    def all_connection_strings(self, all_connection_strings):
        """
        Sets the all_connection_strings of this PluggableDatabaseConnectionStrings.
        All connection strings to use to connect to the pluggable database.


        :param all_connection_strings: The all_connection_strings of this PluggableDatabaseConnectionStrings.
        :type: dict(str, str)
        """
        self._all_connection_strings = all_connection_strings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
