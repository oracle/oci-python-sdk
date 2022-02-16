# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttributeProfileResult(object):
    """
    A summary of profiling results of a specefic attribute.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttributeProfileResult object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_connectivity.models.StringAttribute`
        * :class:`~oci.data_connectivity.models.NumericAttribute`
        * :class:`~oci.data_connectivity.models.DateAttribute`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AttributeProfileResult.
        :type type: object

        :param name:
            The value to assign to the name property of this AttributeProfileResult.
        :type name: str

        :param min:
            The value to assign to the min property of this AttributeProfileResult.
        :type min: oci.data_connectivity.models.ProfileStat

        :param max:
            The value to assign to the max property of this AttributeProfileResult.
        :type max: oci.data_connectivity.models.ProfileStat

        :param null_count:
            The value to assign to the null_count property of this AttributeProfileResult.
        :type null_count: oci.data_connectivity.models.ProfileStat

        :param distinct_count:
            The value to assign to the distinct_count property of this AttributeProfileResult.
        :type distinct_count: oci.data_connectivity.models.ProfileStat

        :param unique_count:
            The value to assign to the unique_count property of this AttributeProfileResult.
        :type unique_count: oci.data_connectivity.models.ProfileStat

        :param duplicate_count:
            The value to assign to the duplicate_count property of this AttributeProfileResult.
        :type duplicate_count: oci.data_connectivity.models.ProfileStat

        :param value_frequencies:
            The value to assign to the value_frequencies property of this AttributeProfileResult.
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

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'STRING':
            return 'StringAttribute'

        if type == 'NUMERIC':
            return 'NumericAttribute'

        if type == 'DATE_TIME':
            return 'DateAttribute'
        else:
            return 'AttributeProfileResult'

    @property
    def type(self):
        """
        Gets the type of this AttributeProfileResult.
        Type of attribute


        :return: The type of this AttributeProfileResult.
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AttributeProfileResult.
        Type of attribute


        :param type: The type of this AttributeProfileResult.
        :type: object
        """
        self._type = type

    @property
    def name(self):
        """
        Gets the name of this AttributeProfileResult.
        Name of attribute


        :return: The name of this AttributeProfileResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AttributeProfileResult.
        Name of attribute


        :param name: The name of this AttributeProfileResult.
        :type: str
        """
        self._name = name

    @property
    def min(self):
        """
        Gets the min of this AttributeProfileResult.

        :return: The min of this AttributeProfileResult.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this AttributeProfileResult.

        :param min: The min of this AttributeProfileResult.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._min = min

    @property
    def max(self):
        """
        Gets the max of this AttributeProfileResult.

        :return: The max of this AttributeProfileResult.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this AttributeProfileResult.

        :param max: The max of this AttributeProfileResult.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._max = max

    @property
    def null_count(self):
        """
        Gets the null_count of this AttributeProfileResult.

        :return: The null_count of this AttributeProfileResult.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._null_count

    @null_count.setter
    def null_count(self, null_count):
        """
        Sets the null_count of this AttributeProfileResult.

        :param null_count: The null_count of this AttributeProfileResult.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._null_count = null_count

    @property
    def distinct_count(self):
        """
        Gets the distinct_count of this AttributeProfileResult.

        :return: The distinct_count of this AttributeProfileResult.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._distinct_count

    @distinct_count.setter
    def distinct_count(self, distinct_count):
        """
        Sets the distinct_count of this AttributeProfileResult.

        :param distinct_count: The distinct_count of this AttributeProfileResult.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._distinct_count = distinct_count

    @property
    def unique_count(self):
        """
        Gets the unique_count of this AttributeProfileResult.

        :return: The unique_count of this AttributeProfileResult.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._unique_count

    @unique_count.setter
    def unique_count(self, unique_count):
        """
        Sets the unique_count of this AttributeProfileResult.

        :param unique_count: The unique_count of this AttributeProfileResult.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._unique_count = unique_count

    @property
    def duplicate_count(self):
        """
        Gets the duplicate_count of this AttributeProfileResult.

        :return: The duplicate_count of this AttributeProfileResult.
        :rtype: oci.data_connectivity.models.ProfileStat
        """
        return self._duplicate_count

    @duplicate_count.setter
    def duplicate_count(self, duplicate_count):
        """
        Sets the duplicate_count of this AttributeProfileResult.

        :param duplicate_count: The duplicate_count of this AttributeProfileResult.
        :type: oci.data_connectivity.models.ProfileStat
        """
        self._duplicate_count = duplicate_count

    @property
    def value_frequencies(self):
        """
        Gets the value_frequencies of this AttributeProfileResult.
        Top N value frequencies for the column as described already in profile config topNValueFrequency property.


        :return: The value_frequencies of this AttributeProfileResult.
        :rtype: list[oci.data_connectivity.models.ObjectFreqStat]
        """
        return self._value_frequencies

    @value_frequencies.setter
    def value_frequencies(self, value_frequencies):
        """
        Sets the value_frequencies of this AttributeProfileResult.
        Top N value frequencies for the column as described already in profile config topNValueFrequency property.


        :param value_frequencies: The value_frequencies of this AttributeProfileResult.
        :type: list[oci.data_connectivity.models.ObjectFreqStat]
        """
        self._value_frequencies = value_frequencies

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
