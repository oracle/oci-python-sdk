# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChannelFilter(object):
    """
    Replication filter rule for a channel.
    """

    #: A constant which can be used with the type property of a ChannelFilter.
    #: This constant has a value of "REPLICATE_DO_DB"
    TYPE_REPLICATE_DO_DB = "REPLICATE_DO_DB"

    #: A constant which can be used with the type property of a ChannelFilter.
    #: This constant has a value of "REPLICATE_IGNORE_DB"
    TYPE_REPLICATE_IGNORE_DB = "REPLICATE_IGNORE_DB"

    #: A constant which can be used with the type property of a ChannelFilter.
    #: This constant has a value of "REPLICATE_DO_TABLE"
    TYPE_REPLICATE_DO_TABLE = "REPLICATE_DO_TABLE"

    #: A constant which can be used with the type property of a ChannelFilter.
    #: This constant has a value of "REPLICATE_IGNORE_TABLE"
    TYPE_REPLICATE_IGNORE_TABLE = "REPLICATE_IGNORE_TABLE"

    #: A constant which can be used with the type property of a ChannelFilter.
    #: This constant has a value of "REPLICATE_WILD_DO_TABLE"
    TYPE_REPLICATE_WILD_DO_TABLE = "REPLICATE_WILD_DO_TABLE"

    #: A constant which can be used with the type property of a ChannelFilter.
    #: This constant has a value of "REPLICATE_WILD_IGNORE_TABLE"
    TYPE_REPLICATE_WILD_IGNORE_TABLE = "REPLICATE_WILD_IGNORE_TABLE"

    #: A constant which can be used with the type property of a ChannelFilter.
    #: This constant has a value of "REPLICATE_REWRITE_DB"
    TYPE_REPLICATE_REWRITE_DB = "REPLICATE_REWRITE_DB"

    def __init__(self, **kwargs):
        """
        Initializes a new ChannelFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ChannelFilter.
            Allowed values for this property are: "REPLICATE_DO_DB", "REPLICATE_IGNORE_DB", "REPLICATE_DO_TABLE", "REPLICATE_IGNORE_TABLE", "REPLICATE_WILD_DO_TABLE", "REPLICATE_WILD_IGNORE_TABLE", "REPLICATE_REWRITE_DB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param value:
            The value to assign to the value property of this ChannelFilter.
        :type value: str

        """
        self.swagger_types = {
            'type': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }

        self._type = None
        self._value = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ChannelFilter.
        The type of the filter rule.

        For details on each type, see
        `Replication Filtering Rules`__

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html

        Allowed values for this property are: "REPLICATE_DO_DB", "REPLICATE_IGNORE_DB", "REPLICATE_DO_TABLE", "REPLICATE_IGNORE_TABLE", "REPLICATE_WILD_DO_TABLE", "REPLICATE_WILD_IGNORE_TABLE", "REPLICATE_REWRITE_DB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ChannelFilter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ChannelFilter.
        The type of the filter rule.

        For details on each type, see
        `Replication Filtering Rules`__

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html


        :param type: The type of this ChannelFilter.
        :type: str
        """
        allowed_values = ["REPLICATE_DO_DB", "REPLICATE_IGNORE_DB", "REPLICATE_DO_TABLE", "REPLICATE_IGNORE_TABLE", "REPLICATE_WILD_DO_TABLE", "REPLICATE_WILD_IGNORE_TABLE", "REPLICATE_REWRITE_DB"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this ChannelFilter.
        The body of the filter rule. This can represent a database, a table, or a database pair (represented as
        \"db1->db2\"). For more information, see
        `Replication Filtering Rules`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html


        :return: The value of this ChannelFilter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ChannelFilter.
        The body of the filter rule. This can represent a database, a table, or a database pair (represented as
        \"db1->db2\"). For more information, see
        `Replication Filtering Rules`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html


        :param value: The value of this ChannelFilter.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
