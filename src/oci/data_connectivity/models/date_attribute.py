# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .attribute_profile_result import AttributeProfileResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DateAttribute(AttributeProfileResult):
    """
    A summary of profiling results of a specefic attribute.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DateAttribute object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.DateAttribute.type` attribute
        of this class is ``DATE_TIME`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DateAttribute.
        :type type: object

        :param name:
            The value to assign to the name property of this DateAttribute.
        :type name: str

        :param min:
            The value to assign to the min property of this DateAttribute.
        :type min: oci.data_connectivity.models.ProfileStat

        :param max:
            The value to assign to the max property of this DateAttribute.
        :type max: oci.data_connectivity.models.ProfileStat

        :param null_count:
            The value to assign to the null_count property of this DateAttribute.
        :type null_count: oci.data_connectivity.models.ProfileStat

        :param distinct_count:
            The value to assign to the distinct_count property of this DateAttribute.
        :type distinct_count: oci.data_connectivity.models.ProfileStat

        :param unique_count:
            The value to assign to the unique_count property of this DateAttribute.
        :type unique_count: oci.data_connectivity.models.ProfileStat

        :param duplicate_count:
            The value to assign to the duplicate_count property of this DateAttribute.
        :type duplicate_count: oci.data_connectivity.models.ProfileStat

        :param value_frequencies:
            The value to assign to the value_frequencies property of this DateAttribute.
        :type value_frequencies: list[oci.data_connectivity.models.ObjectFreqStat]

        """
        self.swagger_types = {
            'type': 'object',
            'name': 'str',
            'min': 'ProfileStat',
            'max': 'ProfileStat',
            'null_count': 'ProfileStat',
            'distinct_count': 'ProfileStat',
            'unique_count': 'ProfileStat',
            'duplicate_count': 'ProfileStat',
            'value_frequencies': 'list[ObjectFreqStat]'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'min': 'min',
            'max': 'max',
            'null_count': 'nullCount',
            'distinct_count': 'distinctCount',
            'unique_count': 'uniqueCount',
            'duplicate_count': 'duplicateCount',
            'value_frequencies': 'valueFrequencies'
        }

        self._type = None
        self._name = None
        self._min = None
        self._max = None
        self._null_count = None
        self._distinct_count = None
        self._unique_count = None
        self._duplicate_count = None
        self._value_frequencies = None
        self._type = 'DATE_TIME'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
