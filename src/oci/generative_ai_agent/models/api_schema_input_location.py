# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiSchemaInputLocation(object):
    """
    The input location definition for Api schema.
    """

    #: A constant which can be used with the api_schema_input_location_type property of a ApiSchemaInputLocation.
    #: This constant has a value of "INLINE"
    API_SCHEMA_INPUT_LOCATION_TYPE_INLINE = "INLINE"

    #: A constant which can be used with the api_schema_input_location_type property of a ApiSchemaInputLocation.
    #: This constant has a value of "OBJECT_STORAGE_LOCATION"
    API_SCHEMA_INPUT_LOCATION_TYPE_OBJECT_STORAGE_LOCATION = "OBJECT_STORAGE_LOCATION"

    def __init__(self, **kwargs):
        """
        Initializes a new ApiSchemaInputLocation object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai_agent.models.ApiSchemaObjectStorageInputLocation`
        * :class:`~oci.generative_ai_agent.models.ApiSchemaInlineInputLocation`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param api_schema_input_location_type:
            The value to assign to the api_schema_input_location_type property of this ApiSchemaInputLocation.
            Allowed values for this property are: "INLINE", "OBJECT_STORAGE_LOCATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type api_schema_input_location_type: str

        """
        self.swagger_types = {
            'api_schema_input_location_type': 'str'
        }
        self.attribute_map = {
            'api_schema_input_location_type': 'apiSchemaInputLocationType'
        }
        self._api_schema_input_location_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['apiSchemaInputLocationType']

        if type == 'OBJECT_STORAGE_LOCATION':
            return 'ApiSchemaObjectStorageInputLocation'

        if type == 'INLINE':
            return 'ApiSchemaInlineInputLocation'
        else:
            return 'ApiSchemaInputLocation'

    @property
    def api_schema_input_location_type(self):
        """
        **[Required]** Gets the api_schema_input_location_type of this ApiSchemaInputLocation.
        Type of Api Schema InputLocation.

        Allowed values for this property are: "INLINE", "OBJECT_STORAGE_LOCATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The api_schema_input_location_type of this ApiSchemaInputLocation.
        :rtype: str
        """
        return self._api_schema_input_location_type

    @api_schema_input_location_type.setter
    def api_schema_input_location_type(self, api_schema_input_location_type):
        """
        Sets the api_schema_input_location_type of this ApiSchemaInputLocation.
        Type of Api Schema InputLocation.


        :param api_schema_input_location_type: The api_schema_input_location_type of this ApiSchemaInputLocation.
        :type: str
        """
        allowed_values = ["INLINE", "OBJECT_STORAGE_LOCATION"]
        if not value_allowed_none_or_none_sentinel(api_schema_input_location_type, allowed_values):
            api_schema_input_location_type = 'UNKNOWN_ENUM_VALUE'
        self._api_schema_input_location_type = api_schema_input_location_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
