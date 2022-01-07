# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyStoreAssociatedDatabaseDetails(object):
    """
    The databases associated with a key store
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KeyStoreAssociatedDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this KeyStoreAssociatedDatabaseDetails.
        :type id: str

        :param db_name:
            The value to assign to the db_name property of this KeyStoreAssociatedDatabaseDetails.
        :type db_name: str

        """
        self.swagger_types = {
            'id': 'str',
            'db_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'db_name': 'dbName'
        }

        self._id = None
        self._db_name = None

    @property
    def id(self):
        """
        Gets the id of this KeyStoreAssociatedDatabaseDetails.
        The database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this KeyStoreAssociatedDatabaseDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this KeyStoreAssociatedDatabaseDetails.
        The database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this KeyStoreAssociatedDatabaseDetails.
        :type: str
        """
        self._id = id

    @property
    def db_name(self):
        """
        Gets the db_name of this KeyStoreAssociatedDatabaseDetails.
        The name of the database that is associated with the key store.


        :return: The db_name of this KeyStoreAssociatedDatabaseDetails.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this KeyStoreAssociatedDatabaseDetails.
        The name of the database that is associated with the key store.


        :param db_name: The db_name of this KeyStoreAssociatedDatabaseDetails.
        :type: str
        """
        self._db_name = db_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
