# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SchemaSummary(object):
    """
    The details of a schema fetched from the database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SchemaSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schema_name:
            The value to assign to the schema_name property of this SchemaSummary.
        :type schema_name: str

        :param is_oracle_maintained:
            The value to assign to the is_oracle_maintained property of this SchemaSummary.
        :type is_oracle_maintained: bool

        """
        self.swagger_types = {
            'schema_name': 'str',
            'is_oracle_maintained': 'bool'
        }
        self.attribute_map = {
            'schema_name': 'schemaName',
            'is_oracle_maintained': 'isOracleMaintained'
        }
        self._schema_name = None
        self._is_oracle_maintained = None

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this SchemaSummary.
        Name of the schema.


        :return: The schema_name of this SchemaSummary.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this SchemaSummary.
        Name of the schema.


        :param schema_name: The schema_name of this SchemaSummary.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def is_oracle_maintained(self):
        """
        **[Required]** Gets the is_oracle_maintained of this SchemaSummary.
        Indicates if the schema is oracle supplied.


        :return: The is_oracle_maintained of this SchemaSummary.
        :rtype: bool
        """
        return self._is_oracle_maintained

    @is_oracle_maintained.setter
    def is_oracle_maintained(self, is_oracle_maintained):
        """
        Sets the is_oracle_maintained of this SchemaSummary.
        Indicates if the schema is oracle supplied.


        :param is_oracle_maintained: The is_oracle_maintained of this SchemaSummary.
        :type: bool
        """
        self._is_oracle_maintained = is_oracle_maintained

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
