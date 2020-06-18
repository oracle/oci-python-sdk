# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CountStatisticSummary(object):
    """
    Detail of object.
    """

    #: A constant which can be used with the object_type property of a CountStatisticSummary.
    #: This constant has a value of "PROJECT"
    OBJECT_TYPE_PROJECT = "PROJECT"

    #: A constant which can be used with the object_type property of a CountStatisticSummary.
    #: This constant has a value of "FOLDER"
    OBJECT_TYPE_FOLDER = "FOLDER"

    #: A constant which can be used with the object_type property of a CountStatisticSummary.
    #: This constant has a value of "DATA_FLOW"
    OBJECT_TYPE_DATA_FLOW = "DATA_FLOW"

    #: A constant which can be used with the object_type property of a CountStatisticSummary.
    #: This constant has a value of "DATA_ASSET"
    OBJECT_TYPE_DATA_ASSET = "DATA_ASSET"

    #: A constant which can be used with the object_type property of a CountStatisticSummary.
    #: This constant has a value of "CONNECTION"
    OBJECT_TYPE_CONNECTION = "CONNECTION"

    #: A constant which can be used with the object_type property of a CountStatisticSummary.
    #: This constant has a value of "TASK"
    OBJECT_TYPE_TASK = "TASK"

    #: A constant which can be used with the object_type property of a CountStatisticSummary.
    #: This constant has a value of "APPLICATION"
    OBJECT_TYPE_APPLICATION = "APPLICATION"

    def __init__(self, **kwargs):
        """
        Initializes a new CountStatisticSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_type:
            The value to assign to the object_type property of this CountStatisticSummary.
            Allowed values for this property are: "PROJECT", "FOLDER", "DATA_FLOW", "DATA_ASSET", "CONNECTION", "TASK", "APPLICATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type object_type: str

        :param object_count:
            The value to assign to the object_count property of this CountStatisticSummary.
        :type object_count: int

        """
        self.swagger_types = {
            'object_type': 'str',
            'object_count': 'int'
        }

        self.attribute_map = {
            'object_type': 'objectType',
            'object_count': 'objectCount'
        }

        self._object_type = None
        self._object_count = None

    @property
    def object_type(self):
        """
        Gets the object_type of this CountStatisticSummary.
        the type of object for the object count statistic.

        Allowed values for this property are: "PROJECT", "FOLDER", "DATA_FLOW", "DATA_ASSET", "CONNECTION", "TASK", "APPLICATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The object_type of this CountStatisticSummary.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this CountStatisticSummary.
        the type of object for the object count statistic.


        :param object_type: The object_type of this CountStatisticSummary.
        :type: str
        """
        allowed_values = ["PROJECT", "FOLDER", "DATA_FLOW", "DATA_ASSET", "CONNECTION", "TASK", "APPLICATION"]
        if not value_allowed_none_or_none_sentinel(object_type, allowed_values):
            object_type = 'UNKNOWN_ENUM_VALUE'
        self._object_type = object_type

    @property
    def object_count(self):
        """
        Gets the object_count of this CountStatisticSummary.
        the value for the object count statistic.


        :return: The object_count of this CountStatisticSummary.
        :rtype: int
        """
        return self._object_count

    @object_count.setter
    def object_count(self, object_count):
        """
        Sets the object_count of this CountStatisticSummary.
        the value for the object count statistic.


        :param object_count: The object_count of this CountStatisticSummary.
        :type: int
        """
        self._object_count = object_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
