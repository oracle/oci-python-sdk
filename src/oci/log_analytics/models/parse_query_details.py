# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParseQueryDetails(object):
    """
    Input information to submit parse query request.
    """

    #: A constant which can be used with the sub_system property of a ParseQueryDetails.
    #: This constant has a value of "LOG"
    SUB_SYSTEM_LOG = "LOG"

    def __init__(self, **kwargs):
        """
        Initializes a new ParseQueryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param query_string:
            The value to assign to the query_string property of this ParseQueryDetails.
        :type query_string: str

        :param sub_system:
            The value to assign to the sub_system property of this ParseQueryDetails.
            Allowed values for this property are: "LOG"
        :type sub_system: str

        """
        self.swagger_types = {
            'query_string': 'str',
            'sub_system': 'str'
        }

        self.attribute_map = {
            'query_string': 'queryString',
            'sub_system': 'subSystem'
        }

        self._query_string = None
        self._sub_system = None

    @property
    def query_string(self):
        """
        **[Required]** Gets the query_string of this ParseQueryDetails.
        Query to parse.


        :return: The query_string of this ParseQueryDetails.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """
        Sets the query_string of this ParseQueryDetails.
        Query to parse.


        :param query_string: The query_string of this ParseQueryDetails.
        :type: str
        """
        self._query_string = query_string

    @property
    def sub_system(self):
        """
        **[Required]** Gets the sub_system of this ParseQueryDetails.
        Default subsystem to qualify fields with in the queryString if not specified.

        Allowed values for this property are: "LOG"


        :return: The sub_system of this ParseQueryDetails.
        :rtype: str
        """
        return self._sub_system

    @sub_system.setter
    def sub_system(self, sub_system):
        """
        Sets the sub_system of this ParseQueryDetails.
        Default subsystem to qualify fields with in the queryString if not specified.


        :param sub_system: The sub_system of this ParseQueryDetails.
        :type: str
        """
        allowed_values = ["LOG"]
        if not value_allowed_none_or_none_sentinel(sub_system, allowed_values):
            raise ValueError(
                "Invalid value for `sub_system`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sub_system = sub_system

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
