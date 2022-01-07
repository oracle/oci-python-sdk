# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponseCacheDetails(object):
    """
    Base Gateway response cache.
    """

    #: A constant which can be used with the type property of a ResponseCacheDetails.
    #: This constant has a value of "EXTERNAL_RESP_CACHE"
    TYPE_EXTERNAL_RESP_CACHE = "EXTERNAL_RESP_CACHE"

    #: A constant which can be used with the type property of a ResponseCacheDetails.
    #: This constant has a value of "NONE"
    TYPE_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new ResponseCacheDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apigateway.models.ExternalRespCache`
        * :class:`~oci.apigateway.models.NoCache`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ResponseCacheDetails.
            Allowed values for this property are: "EXTERNAL_RESP_CACHE", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'EXTERNAL_RESP_CACHE':
            return 'ExternalRespCache'

        if type == 'NONE':
            return 'NoCache'
        else:
            return 'ResponseCacheDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ResponseCacheDetails.
        Type of the Response Cache.

        Allowed values for this property are: "EXTERNAL_RESP_CACHE", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ResponseCacheDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ResponseCacheDetails.
        Type of the Response Cache.


        :param type: The type of this ResponseCacheDetails.
        :type: str
        """
        allowed_values = ["EXTERNAL_RESP_CACHE", "NONE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
