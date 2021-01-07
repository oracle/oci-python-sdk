# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeleteRowResult(object):
    """
    The result of a DeleteRow operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeleteRowResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_success:
            The value to assign to the is_success property of this DeleteRowResult.
        :type is_success: bool

        :param existing_version:
            The value to assign to the existing_version property of this DeleteRowResult.
        :type existing_version: str

        :param existing_value:
            The value to assign to the existing_value property of this DeleteRowResult.
        :type existing_value: dict(str, object)

        :param usage:
            The value to assign to the usage property of this DeleteRowResult.
        :type usage: oci.nosql.models.RequestUsage

        """
        self.swagger_types = {
            'is_success': 'bool',
            'existing_version': 'str',
            'existing_value': 'dict(str, object)',
            'usage': 'RequestUsage'
        }

        self.attribute_map = {
            'is_success': 'isSuccess',
            'existing_version': 'existingVersion',
            'existing_value': 'existingValue',
            'usage': 'usage'
        }

        self._is_success = None
        self._existing_version = None
        self._existing_value = None
        self._usage = None

    @property
    def is_success(self):
        """
        Gets the is_success of this DeleteRowResult.
        Convey the success or failure of the operation.


        :return: The is_success of this DeleteRowResult.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """
        Sets the is_success of this DeleteRowResult.
        Convey the success or failure of the operation.


        :param is_success: The is_success of this DeleteRowResult.
        :type: bool
        """
        self._is_success = is_success

    @property
    def existing_version(self):
        """
        Gets the existing_version of this DeleteRowResult.
        The version string associated with the existing row.
        Returned if the delete fails due to options setting in the
        request.


        :return: The existing_version of this DeleteRowResult.
        :rtype: str
        """
        return self._existing_version

    @existing_version.setter
    def existing_version(self, existing_version):
        """
        Sets the existing_version of this DeleteRowResult.
        The version string associated with the existing row.
        Returned if the delete fails due to options setting in the
        request.


        :param existing_version: The existing_version of this DeleteRowResult.
        :type: str
        """
        self._existing_version = existing_version

    @property
    def existing_value(self):
        """
        Gets the existing_value of this DeleteRowResult.
        The map of values from a row.


        :return: The existing_value of this DeleteRowResult.
        :rtype: dict(str, object)
        """
        return self._existing_value

    @existing_value.setter
    def existing_value(self, existing_value):
        """
        Sets the existing_value of this DeleteRowResult.
        The map of values from a row.


        :param existing_value: The existing_value of this DeleteRowResult.
        :type: dict(str, object)
        """
        self._existing_value = existing_value

    @property
    def usage(self):
        """
        Gets the usage of this DeleteRowResult.

        :return: The usage of this DeleteRowResult.
        :rtype: oci.nosql.models.RequestUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this DeleteRowResult.

        :param usage: The usage of this DeleteRowResult.
        :type: oci.nosql.models.RequestUsage
        """
        self._usage = usage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
