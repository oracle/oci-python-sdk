# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Schema(object):
    """
    The table schema information as a JSON object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Schema object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param columns:
            The value to assign to the columns property of this Schema.
        :type columns: list[oci.nosql.models.Column]

        :param primary_key:
            The value to assign to the primary_key property of this Schema.
        :type primary_key: list[str]

        :param shard_key:
            The value to assign to the shard_key property of this Schema.
        :type shard_key: list[str]

        :param ttl:
            The value to assign to the ttl property of this Schema.
        :type ttl: int

        """
        self.swagger_types = {
            'columns': 'list[Column]',
            'primary_key': 'list[str]',
            'shard_key': 'list[str]',
            'ttl': 'int'
        }

        self.attribute_map = {
            'columns': 'columns',
            'primary_key': 'primaryKey',
            'shard_key': 'shardKey',
            'ttl': 'ttl'
        }

        self._columns = None
        self._primary_key = None
        self._shard_key = None
        self._ttl = None

    @property
    def columns(self):
        """
        **[Required]** Gets the columns of this Schema.
        The columns of a table.


        :return: The columns of this Schema.
        :rtype: list[oci.nosql.models.Column]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this Schema.
        The columns of a table.


        :param columns: The columns of this Schema.
        :type: list[oci.nosql.models.Column]
        """
        self._columns = columns

    @property
    def primary_key(self):
        """
        **[Required]** Gets the primary_key of this Schema.
        A list of column names that make up a key.


        :return: The primary_key of this Schema.
        :rtype: list[str]
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """
        Sets the primary_key of this Schema.
        A list of column names that make up a key.


        :param primary_key: The primary_key of this Schema.
        :type: list[str]
        """
        self._primary_key = primary_key

    @property
    def shard_key(self):
        """
        **[Required]** Gets the shard_key of this Schema.
        A list of column names that make up a key.


        :return: The shard_key of this Schema.
        :rtype: list[str]
        """
        return self._shard_key

    @shard_key.setter
    def shard_key(self, shard_key):
        """
        Sets the shard_key of this Schema.
        A list of column names that make up a key.


        :param shard_key: The shard_key of this Schema.
        :type: list[str]
        """
        self._shard_key = shard_key

    @property
    def ttl(self):
        """
        **[Required]** Gets the ttl of this Schema.
        The default Time-to-Live for the table, in days.


        :return: The ttl of this Schema.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this Schema.
        The default Time-to-Live for the table, in days.


        :param ttl: The ttl of this Schema.
        :type: int
        """
        self._ttl = ttl

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
