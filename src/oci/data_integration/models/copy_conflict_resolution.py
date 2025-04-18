# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CopyConflictResolution(object):
    """
    Copy Object Conflict resolution.
    """

    #: A constant which can be used with the request_type property of a CopyConflictResolution.
    #: This constant has a value of "RETAIN"
    REQUEST_TYPE_RETAIN = "RETAIN"

    #: A constant which can be used with the request_type property of a CopyConflictResolution.
    #: This constant has a value of "DUPLICATE"
    REQUEST_TYPE_DUPLICATE = "DUPLICATE"

    #: A constant which can be used with the request_type property of a CopyConflictResolution.
    #: This constant has a value of "REPLACE"
    REQUEST_TYPE_REPLACE = "REPLACE"

    def __init__(self, **kwargs):
        """
        Initializes a new CopyConflictResolution object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param duplicate_prefix:
            The value to assign to the duplicate_prefix property of this CopyConflictResolution.
        :type duplicate_prefix: str

        :param duplicate_suffix:
            The value to assign to the duplicate_suffix property of this CopyConflictResolution.
        :type duplicate_suffix: str

        :param request_type:
            The value to assign to the request_type property of this CopyConflictResolution.
            Allowed values for this property are: "RETAIN", "DUPLICATE", "REPLACE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type request_type: str

        """
        self.swagger_types = {
            'duplicate_prefix': 'str',
            'duplicate_suffix': 'str',
            'request_type': 'str'
        }
        self.attribute_map = {
            'duplicate_prefix': 'duplicatePrefix',
            'duplicate_suffix': 'duplicateSuffix',
            'request_type': 'requestType'
        }
        self._duplicate_prefix = None
        self._duplicate_suffix = None
        self._request_type = None

    @property
    def duplicate_prefix(self):
        """
        Gets the duplicate_prefix of this CopyConflictResolution.
        In case of DUPLICATE mode, this prefix will be used to disambiguate the object.


        :return: The duplicate_prefix of this CopyConflictResolution.
        :rtype: str
        """
        return self._duplicate_prefix

    @duplicate_prefix.setter
    def duplicate_prefix(self, duplicate_prefix):
        """
        Sets the duplicate_prefix of this CopyConflictResolution.
        In case of DUPLICATE mode, this prefix will be used to disambiguate the object.


        :param duplicate_prefix: The duplicate_prefix of this CopyConflictResolution.
        :type: str
        """
        self._duplicate_prefix = duplicate_prefix

    @property
    def duplicate_suffix(self):
        """
        Gets the duplicate_suffix of this CopyConflictResolution.
        In case of DUPLICATE mode, this suffix will be used to disambiguate the object.


        :return: The duplicate_suffix of this CopyConflictResolution.
        :rtype: str
        """
        return self._duplicate_suffix

    @duplicate_suffix.setter
    def duplicate_suffix(self, duplicate_suffix):
        """
        Sets the duplicate_suffix of this CopyConflictResolution.
        In case of DUPLICATE mode, this suffix will be used to disambiguate the object.


        :param duplicate_suffix: The duplicate_suffix of this CopyConflictResolution.
        :type: str
        """
        self._duplicate_suffix = duplicate_suffix

    @property
    def request_type(self):
        """
        **[Required]** Gets the request_type of this CopyConflictResolution.
        Copy Object Conflict Resolution Type (RETAIN/DUPLICATE/REPLACE).

        Allowed values for this property are: "RETAIN", "DUPLICATE", "REPLACE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The request_type of this CopyConflictResolution.
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """
        Sets the request_type of this CopyConflictResolution.
        Copy Object Conflict Resolution Type (RETAIN/DUPLICATE/REPLACE).


        :param request_type: The request_type of this CopyConflictResolution.
        :type: str
        """
        allowed_values = ["RETAIN", "DUPLICATE", "REPLACE"]
        if not value_allowed_none_or_none_sentinel(request_type, allowed_values):
            request_type = 'UNKNOWN_ENUM_VALUE'
        self._request_type = request_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
