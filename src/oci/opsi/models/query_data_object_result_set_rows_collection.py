# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryDataObjectResultSetRowsCollection(object):
    """
    Collection of result set rows from the data object query.
    """

    #: A constant which can be used with the format property of a QueryDataObjectResultSetRowsCollection.
    #: This constant has a value of "JSON"
    FORMAT_JSON = "JSON"

    def __init__(self, **kwargs):
        """
        Initializes a new QueryDataObjectResultSetRowsCollection object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.QueryDataObjectJsonResultSetRowsCollection`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param format:
            The value to assign to the format property of this QueryDataObjectResultSetRowsCollection.
            Allowed values for this property are: "JSON", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type format: str

        """
        self.swagger_types = {
            'format': 'str'
        }

        self.attribute_map = {
            'format': 'format'
        }

        self._format = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['format']

        if type == 'JSON':
            return 'QueryDataObjectJsonResultSetRowsCollection'
        else:
            return 'QueryDataObjectResultSetRowsCollection'

    @property
    def format(self):
        """
        **[Required]** Gets the format of this QueryDataObjectResultSetRowsCollection.
        Format type of data object query result set.

        Allowed values for this property are: "JSON", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The format of this QueryDataObjectResultSetRowsCollection.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this QueryDataObjectResultSetRowsCollection.
        Format type of data object query result set.


        :param format: The format of this QueryDataObjectResultSetRowsCollection.
        :type: str
        """
        allowed_values = ["JSON"]
        if not value_allowed_none_or_none_sentinel(format, allowed_values):
            format = 'UNKNOWN_ENUM_VALUE'
        self._format = format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
