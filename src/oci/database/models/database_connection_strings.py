# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseConnectionStrings(object):
    """
    Connection strings to connect to an Oracle Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseConnectionStrings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cdb_default:
            The value to assign to the cdb_default property of this DatabaseConnectionStrings.
        :type cdb_default: str

        :param cdb_ip_default:
            The value to assign to the cdb_ip_default property of this DatabaseConnectionStrings.
        :type cdb_ip_default: str

        :param all_connection_strings:
            The value to assign to the all_connection_strings property of this DatabaseConnectionStrings.
        :type all_connection_strings: dict(str, str)

        """
        self.swagger_types = {
            'cdb_default': 'str',
            'cdb_ip_default': 'str',
            'all_connection_strings': 'dict(str, str)'
        }

        self.attribute_map = {
            'cdb_default': 'cdbDefault',
            'cdb_ip_default': 'cdbIpDefault',
            'all_connection_strings': 'allConnectionStrings'
        }

        self._cdb_default = None
        self._cdb_ip_default = None
        self._all_connection_strings = None

    @property
    def cdb_default(self):
        """
        Gets the cdb_default of this DatabaseConnectionStrings.
        Host name based CDB Connection String.


        :return: The cdb_default of this DatabaseConnectionStrings.
        :rtype: str
        """
        return self._cdb_default

    @cdb_default.setter
    def cdb_default(self, cdb_default):
        """
        Sets the cdb_default of this DatabaseConnectionStrings.
        Host name based CDB Connection String.


        :param cdb_default: The cdb_default of this DatabaseConnectionStrings.
        :type: str
        """
        self._cdb_default = cdb_default

    @property
    def cdb_ip_default(self):
        """
        Gets the cdb_ip_default of this DatabaseConnectionStrings.
        IP based CDB Connection String.


        :return: The cdb_ip_default of this DatabaseConnectionStrings.
        :rtype: str
        """
        return self._cdb_ip_default

    @cdb_ip_default.setter
    def cdb_ip_default(self, cdb_ip_default):
        """
        Sets the cdb_ip_default of this DatabaseConnectionStrings.
        IP based CDB Connection String.


        :param cdb_ip_default: The cdb_ip_default of this DatabaseConnectionStrings.
        :type: str
        """
        self._cdb_ip_default = cdb_ip_default

    @property
    def all_connection_strings(self):
        """
        Gets the all_connection_strings of this DatabaseConnectionStrings.
        All connection strings to use to connect to the Database.


        :return: The all_connection_strings of this DatabaseConnectionStrings.
        :rtype: dict(str, str)
        """
        return self._all_connection_strings

    @all_connection_strings.setter
    def all_connection_strings(self, all_connection_strings):
        """
        Sets the all_connection_strings of this DatabaseConnectionStrings.
        All connection strings to use to connect to the Database.


        :param all_connection_strings: The all_connection_strings of this DatabaseConnectionStrings.
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
