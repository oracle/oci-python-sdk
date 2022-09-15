# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IndicatorCountDimensions(object):
    """
    The indicator dimension that was counted, such as the indicator type.
    """

    #: A constant which can be used with the type property of a IndicatorCountDimensions.
    #: This constant has a value of "DOMAIN_NAME"
    TYPE_DOMAIN_NAME = "DOMAIN_NAME"

    #: A constant which can be used with the type property of a IndicatorCountDimensions.
    #: This constant has a value of "FILE_NAME"
    TYPE_FILE_NAME = "FILE_NAME"

    #: A constant which can be used with the type property of a IndicatorCountDimensions.
    #: This constant has a value of "MD5_HASH"
    TYPE_MD5_HASH = "MD5_HASH"

    #: A constant which can be used with the type property of a IndicatorCountDimensions.
    #: This constant has a value of "SHA1_HASH"
    TYPE_SHA1_HASH = "SHA1_HASH"

    #: A constant which can be used with the type property of a IndicatorCountDimensions.
    #: This constant has a value of "SHA256_HASH"
    TYPE_SHA256_HASH = "SHA256_HASH"

    #: A constant which can be used with the type property of a IndicatorCountDimensions.
    #: This constant has a value of "IP_ADDRESS"
    TYPE_IP_ADDRESS = "IP_ADDRESS"

    #: A constant which can be used with the type property of a IndicatorCountDimensions.
    #: This constant has a value of "URL"
    TYPE_URL = "URL"

    def __init__(self, **kwargs):
        """
        Initializes a new IndicatorCountDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this IndicatorCountDimensions.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this IndicatorCountDimensions.
            Allowed values for this property are: "DOMAIN_NAME", "FILE_NAME", "MD5_HASH", "SHA1_HASH", "SHA256_HASH", "IP_ADDRESS", "URL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'type': 'type'
        }

        self._compartment_id = None
        self._type = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this IndicatorCountDimensions.
        The compartment OCID that contains the indicator type.


        :return: The compartment_id of this IndicatorCountDimensions.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IndicatorCountDimensions.
        The compartment OCID that contains the indicator type.


        :param compartment_id: The compartment_id of this IndicatorCountDimensions.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def type(self):
        """
        Gets the type of this IndicatorCountDimensions.
        The indicator type that was counted.

        Allowed values for this property are: "DOMAIN_NAME", "FILE_NAME", "MD5_HASH", "SHA1_HASH", "SHA256_HASH", "IP_ADDRESS", "URL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this IndicatorCountDimensions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IndicatorCountDimensions.
        The indicator type that was counted.


        :param type: The type of this IndicatorCountDimensions.
        :type: str
        """
        allowed_values = ["DOMAIN_NAME", "FILE_NAME", "MD5_HASH", "SHA1_HASH", "SHA256_HASH", "IP_ADDRESS", "URL"]
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
