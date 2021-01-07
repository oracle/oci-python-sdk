# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateRowResult(object):
    """
    The result of an UpdateRow operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateRowResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this UpdateRowResult.
        :type version: str

        :param existing_version:
            The value to assign to the existing_version property of this UpdateRowResult.
        :type existing_version: str

        :param existing_value:
            The value to assign to the existing_value property of this UpdateRowResult.
        :type existing_value: dict(str, object)

        :param generated_value:
            The value to assign to the generated_value property of this UpdateRowResult.
        :type generated_value: str

        :param usage:
            The value to assign to the usage property of this UpdateRowResult.
        :type usage: oci.nosql.models.RequestUsage

        """
        self.swagger_types = {
            'version': 'str',
            'existing_version': 'str',
            'existing_value': 'dict(str, object)',
            'generated_value': 'str',
            'usage': 'RequestUsage'
        }

        self.attribute_map = {
            'version': 'version',
            'existing_version': 'existingVersion',
            'existing_value': 'existingValue',
            'generated_value': 'generatedValue',
            'usage': 'usage'
        }

        self._version = None
        self._existing_version = None
        self._existing_value = None
        self._generated_value = None
        self._usage = None

    @property
    def version(self):
        """
        Gets the version of this UpdateRowResult.
        An opaque version string associated with the row.


        :return: The version of this UpdateRowResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this UpdateRowResult.
        An opaque version string associated with the row.


        :param version: The version of this UpdateRowResult.
        :type: str
        """
        self._version = version

    @property
    def existing_version(self):
        """
        Gets the existing_version of this UpdateRowResult.
        The version string associated with the existing row.
        Returned if the put fails due to options setting in the
        request.


        :return: The existing_version of this UpdateRowResult.
        :rtype: str
        """
        return self._existing_version

    @existing_version.setter
    def existing_version(self, existing_version):
        """
        Sets the existing_version of this UpdateRowResult.
        The version string associated with the existing row.
        Returned if the put fails due to options setting in the
        request.


        :param existing_version: The existing_version of this UpdateRowResult.
        :type: str
        """
        self._existing_version = existing_version

    @property
    def existing_value(self):
        """
        Gets the existing_value of this UpdateRowResult.
        The map of values from a row.


        :return: The existing_value of this UpdateRowResult.
        :rtype: dict(str, object)
        """
        return self._existing_value

    @existing_value.setter
    def existing_value(self, existing_value):
        """
        Sets the existing_value of this UpdateRowResult.
        The map of values from a row.


        :param existing_value: The existing_value of this UpdateRowResult.
        :type: dict(str, object)
        """
        self._existing_value = existing_value

    @property
    def generated_value(self):
        """
        Gets the generated_value of this UpdateRowResult.
        The value generated if the operation created a new value for
        an identity column. If the table has no identity column, this value
        is null. If it has an identity column, and a value was generated for
        that column, it is non-null.


        :return: The generated_value of this UpdateRowResult.
        :rtype: str
        """
        return self._generated_value

    @generated_value.setter
    def generated_value(self, generated_value):
        """
        Sets the generated_value of this UpdateRowResult.
        The value generated if the operation created a new value for
        an identity column. If the table has no identity column, this value
        is null. If it has an identity column, and a value was generated for
        that column, it is non-null.


        :param generated_value: The generated_value of this UpdateRowResult.
        :type: str
        """
        self._generated_value = generated_value

    @property
    def usage(self):
        """
        Gets the usage of this UpdateRowResult.

        :return: The usage of this UpdateRowResult.
        :rtype: oci.nosql.models.RequestUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this UpdateRowResult.

        :param usage: The usage of this UpdateRowResult.
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
