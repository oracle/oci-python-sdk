# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InputLocation(object):
    """
    The location of the input(s).
    """

    #: A constant which can be used with the source_type property of a InputLocation.
    #: This constant has a value of "OBJECT_LIST_INLINE_INPUT_LOCATION"
    SOURCE_TYPE_OBJECT_LIST_INLINE_INPUT_LOCATION = "OBJECT_LIST_INLINE_INPUT_LOCATION"

    def __init__(self, **kwargs):
        """
        Initializes a new InputLocation object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_vision.models.ObjectListInlineInputLocation`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this InputLocation.
            Allowed values for this property are: "OBJECT_LIST_INLINE_INPUT_LOCATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_type: str

        """
        self.swagger_types = {
            'source_type': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType'
        }

        self._source_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['sourceType']

        if type == 'OBJECT_LIST_INLINE_INPUT_LOCATION':
            return 'ObjectListInlineInputLocation'
        else:
            return 'InputLocation'

    @property
    def source_type(self):
        """
        **[Required]** Gets the source_type of this InputLocation.
        The type of input location
        Allowed values are:
        - `OBJECT_LIST_INLINE_INPUT_LOCATION`: A list of object locations in Object Storage.

        Allowed values for this property are: "OBJECT_LIST_INLINE_INPUT_LOCATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_type of this InputLocation.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this InputLocation.
        The type of input location
        Allowed values are:
        - `OBJECT_LIST_INLINE_INPUT_LOCATION`: A list of object locations in Object Storage.


        :param source_type: The source_type of this InputLocation.
        :type: str
        """
        allowed_values = ["OBJECT_LIST_INLINE_INPUT_LOCATION"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            source_type = 'UNKNOWN_ENUM_VALUE'
        self._source_type = source_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
