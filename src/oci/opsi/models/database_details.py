# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseDetails(object):
    """
    Partial information about the database which includes id, name, type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_id:
            The value to assign to the database_id property of this DatabaseDetails.
        :type database_id: str

        :param database_name:
            The value to assign to the database_name property of this DatabaseDetails.
        :type database_name: str

        :param database_display_name:
            The value to assign to the database_display_name property of this DatabaseDetails.
        :type database_display_name: str

        :param database_type:
            The value to assign to the database_type property of this DatabaseDetails.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this DatabaseDetails.
        :type database_version: str

        """
        self.swagger_types = {
            'database_id': 'str',
            'database_name': 'str',
            'database_display_name': 'str',
            'database_type': 'str',
            'database_version': 'str'
        }

        self.attribute_map = {
            'database_id': 'databaseId',
            'database_name': 'databaseName',
            'database_display_name': 'databaseDisplayName',
            'database_type': 'databaseType',
            'database_version': 'databaseVersion'
        }

        self._database_id = None
        self._database_name = None
        self._database_display_name = None
        self._database_type = None
        self._database_version = None

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this DatabaseDetails.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The database_id of this DatabaseDetails.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this DatabaseDetails.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this DatabaseDetails.
        :type: str
        """
        self._database_id = database_id

    @property
    def database_name(self):
        """
        **[Required]** Gets the database_name of this DatabaseDetails.
        The database name. The database name is unique within the tenancy.


        :return: The database_name of this DatabaseDetails.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this DatabaseDetails.
        The database name. The database name is unique within the tenancy.


        :param database_name: The database_name of this DatabaseDetails.
        :type: str
        """
        self._database_name = database_name

    @property
    def database_display_name(self):
        """
        Gets the database_display_name of this DatabaseDetails.
        The user-friendly name for the database. The name does not have to be unique.


        :return: The database_display_name of this DatabaseDetails.
        :rtype: str
        """
        return self._database_display_name

    @database_display_name.setter
    def database_display_name(self, database_display_name):
        """
        Sets the database_display_name of this DatabaseDetails.
        The user-friendly name for the database. The name does not have to be unique.


        :param database_display_name: The database_display_name of this DatabaseDetails.
        :type: str
        """
        self._database_display_name = database_display_name

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this DatabaseDetails.
        Operations Insights internal representation of the database type.


        :return: The database_type of this DatabaseDetails.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this DatabaseDetails.
        Operations Insights internal representation of the database type.


        :param database_type: The database_type of this DatabaseDetails.
        :type: str
        """
        self._database_type = database_type

    @property
    def database_version(self):
        """
        Gets the database_version of this DatabaseDetails.
        The version of the database.


        :return: The database_version of this DatabaseDetails.
        :rtype: str
        """
        return self._database_version

    @database_version.setter
    def database_version(self, database_version):
        """
        Sets the database_version of this DatabaseDetails.
        The version of the database.


        :param database_version: The database_version of this DatabaseDetails.
        :type: str
        """
        self._database_version = database_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
