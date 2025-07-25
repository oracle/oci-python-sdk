# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InputLocation(object):
    """
    The input location definition.
    """

    #: A constant which can be used with the input_location_type property of a InputLocation.
    #: This constant has a value of "INLINE"
    INPUT_LOCATION_TYPE_INLINE = "INLINE"

    #: A constant which can be used with the input_location_type property of a InputLocation.
    #: This constant has a value of "OBJECT_STORAGE_PREFIX"
    INPUT_LOCATION_TYPE_OBJECT_STORAGE_PREFIX = "OBJECT_STORAGE_PREFIX"

    def __init__(self, **kwargs):
        """
        Initializes a new InputLocation object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai_agent.models.ObjectStorageInputLocation`
        * :class:`~oci.generative_ai_agent.models.InlineInputLocation`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input_location_type:
            The value to assign to the input_location_type property of this InputLocation.
            Allowed values for this property are: "INLINE", "OBJECT_STORAGE_PREFIX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type input_location_type: str

        """
        self.swagger_types = {
            'input_location_type': 'str'
        }
        self.attribute_map = {
            'input_location_type': 'inputLocationType'
        }
        self._input_location_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['inputLocationType']

        if type == 'OBJECT_STORAGE_PREFIX':
            return 'ObjectStorageInputLocation'

        if type == 'INLINE':
            return 'InlineInputLocation'
        else:
            return 'InputLocation'

    @property
    def input_location_type(self):
        """
        **[Required]** Gets the input_location_type of this InputLocation.
        Type of InputLocation.

        Allowed values for this property are: "INLINE", "OBJECT_STORAGE_PREFIX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The input_location_type of this InputLocation.
        :rtype: str
        """
        return self._input_location_type

    @input_location_type.setter
    def input_location_type(self, input_location_type):
        """
        Sets the input_location_type of this InputLocation.
        Type of InputLocation.


        :param input_location_type: The input_location_type of this InputLocation.
        :type: str
        """
        allowed_values = ["INLINE", "OBJECT_STORAGE_PREFIX"]
        if not value_allowed_none_or_none_sentinel(input_location_type, allowed_values):
            input_location_type = 'UNKNOWN_ENUM_VALUE'
        self._input_location_type = input_location_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
