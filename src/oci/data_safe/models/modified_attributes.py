# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModifiedAttributes(object):
    """
    The attributes of a sensitive column that have been modified in the target database. It's populated only in the case
    of MODIFIED discovery results and shows the new values of the modified attributes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModifiedAttributes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param app_defined_child_column_keys:
            The value to assign to the app_defined_child_column_keys property of this ModifiedAttributes.
        :type app_defined_child_column_keys: list[str]

        :param db_defined_child_column_keys:
            The value to assign to the db_defined_child_column_keys property of this ModifiedAttributes.
        :type db_defined_child_column_keys: list[str]

        """
        self.swagger_types = {
            'app_defined_child_column_keys': 'list[str]',
            'db_defined_child_column_keys': 'list[str]'
        }

        self.attribute_map = {
            'app_defined_child_column_keys': 'appDefinedChildColumnKeys',
            'db_defined_child_column_keys': 'dbDefinedChildColumnKeys'
        }

        self._app_defined_child_column_keys = None
        self._db_defined_child_column_keys = None

    @property
    def app_defined_child_column_keys(self):
        """
        Gets the app_defined_child_column_keys of this ModifiedAttributes.
        Unique keys identifying the columns that are application-level (non-dictionary) children of the sensitive column.


        :return: The app_defined_child_column_keys of this ModifiedAttributes.
        :rtype: list[str]
        """
        return self._app_defined_child_column_keys

    @app_defined_child_column_keys.setter
    def app_defined_child_column_keys(self, app_defined_child_column_keys):
        """
        Sets the app_defined_child_column_keys of this ModifiedAttributes.
        Unique keys identifying the columns that are application-level (non-dictionary) children of the sensitive column.


        :param app_defined_child_column_keys: The app_defined_child_column_keys of this ModifiedAttributes.
        :type: list[str]
        """
        self._app_defined_child_column_keys = app_defined_child_column_keys

    @property
    def db_defined_child_column_keys(self):
        """
        Gets the db_defined_child_column_keys of this ModifiedAttributes.
        Unique keys identifying the columns that are database-level (dictionary-defined) children of the sensitive column.


        :return: The db_defined_child_column_keys of this ModifiedAttributes.
        :rtype: list[str]
        """
        return self._db_defined_child_column_keys

    @db_defined_child_column_keys.setter
    def db_defined_child_column_keys(self, db_defined_child_column_keys):
        """
        Sets the db_defined_child_column_keys of this ModifiedAttributes.
        Unique keys identifying the columns that are database-level (dictionary-defined) children of the sensitive column.


        :param db_defined_child_column_keys: The db_defined_child_column_keys of this ModifiedAttributes.
        :type: list[str]
        """
        self._db_defined_child_column_keys = db_defined_child_column_keys

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
