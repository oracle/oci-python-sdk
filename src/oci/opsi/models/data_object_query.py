# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataObjectQuery(object):
    """
    Information required to form and execute query on a data object.
    """

    #: A constant which can be used with the query_type property of a DataObjectQuery.
    #: This constant has a value of "TEMPLATIZED_QUERY"
    QUERY_TYPE_TEMPLATIZED_QUERY = "TEMPLATIZED_QUERY"

    def __init__(self, **kwargs):
        """
        Initializes a new DataObjectQuery object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.DataObjectTemplatizedQuery`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param query_type:
            The value to assign to the query_type property of this DataObjectQuery.
            Allowed values for this property are: "TEMPLATIZED_QUERY"
        :type query_type: str

        """
        self.swagger_types = {
            'query_type': 'str'
        }

        self.attribute_map = {
            'query_type': 'queryType'
        }

        self._query_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['queryType']

        if type == 'TEMPLATIZED_QUERY':
            return 'DataObjectTemplatizedQuery'
        else:
            return 'DataObjectQuery'

    @property
    def query_type(self):
        """
        **[Required]** Gets the query_type of this DataObjectQuery.
        Type of Query

        Allowed values for this property are: "TEMPLATIZED_QUERY"


        :return: The query_type of this DataObjectQuery.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """
        Sets the query_type of this DataObjectQuery.
        Type of Query


        :param query_type: The query_type of this DataObjectQuery.
        :type: str
        """
        allowed_values = ["TEMPLATIZED_QUERY"]
        if not value_allowed_none_or_none_sentinel(query_type, allowed_values):
            raise ValueError(
                "Invalid value for `query_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._query_type = query_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
