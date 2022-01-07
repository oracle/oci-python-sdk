# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_command_descriptor import AbstractCommandDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BucketCommandDescriptor(AbstractCommandDescriptor):
    """
    Command descriptor for querylanguage BUCKET command.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BucketCommandDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.BucketCommandDescriptor.name` attribute
        of this class is ``BUCKET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this BucketCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "GEO_STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "JSON_EXTRACT", "XML_EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", "HIGHLIGHT_GROUPS", "CREATE_VIEW", "MAP", "NLP", "COMPARE"
        :type name: str

        :param display_query_string:
            The value to assign to the display_query_string property of this BucketCommandDescriptor.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this BucketCommandDescriptor.
        :type internal_query_string: str

        :param category:
            The value to assign to the category property of this BucketCommandDescriptor.
        :type category: str

        :param referenced_fields:
            The value to assign to the referenced_fields property of this BucketCommandDescriptor.
        :type referenced_fields: list[oci.log_analytics.models.AbstractField]

        :param declared_fields:
            The value to assign to the declared_fields property of this BucketCommandDescriptor.
        :type declared_fields: list[oci.log_analytics.models.AbstractField]

        :param max_buckets:
            The value to assign to the max_buckets property of this BucketCommandDescriptor.
        :type max_buckets: int

        :param span:
            The value to assign to the span property of this BucketCommandDescriptor.
        :type span: float

        :param ranges:
            The value to assign to the ranges property of this BucketCommandDescriptor.
        :type ranges: list[oci.log_analytics.models.BucketRange]

        :param default_value:
            The value to assign to the default_value property of this BucketCommandDescriptor.
        :type default_value: str

        """
        self.swagger_types = {
            'name': 'str',
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'category': 'str',
            'referenced_fields': 'list[AbstractField]',
            'declared_fields': 'list[AbstractField]',
            'max_buckets': 'int',
            'span': 'float',
            'ranges': 'list[BucketRange]',
            'default_value': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'category': 'category',
            'referenced_fields': 'referencedFields',
            'declared_fields': 'declaredFields',
            'max_buckets': 'maxBuckets',
            'span': 'span',
            'ranges': 'ranges',
            'default_value': 'defaultValue'
        }

        self._name = None
        self._display_query_string = None
        self._internal_query_string = None
        self._category = None
        self._referenced_fields = None
        self._declared_fields = None
        self._max_buckets = None
        self._span = None
        self._ranges = None
        self._default_value = None
        self._name = 'BUCKET'

    @property
    def max_buckets(self):
        """
        Gets the max_buckets of this BucketCommandDescriptor.
        number of auto calculated ranges to compute if specified.


        :return: The max_buckets of this BucketCommandDescriptor.
        :rtype: int
        """
        return self._max_buckets

    @max_buckets.setter
    def max_buckets(self, max_buckets):
        """
        Sets the max_buckets of this BucketCommandDescriptor.
        number of auto calculated ranges to compute if specified.


        :param max_buckets: The max_buckets of this BucketCommandDescriptor.
        :type: int
        """
        self._max_buckets = max_buckets

    @property
    def span(self):
        """
        Gets the span of this BucketCommandDescriptor.
        Size of each numeric range if specified. Data type should match numeric field data type specified in the query string.


        :return: The span of this BucketCommandDescriptor.
        :rtype: float
        """
        return self._span

    @span.setter
    def span(self, span):
        """
        Sets the span of this BucketCommandDescriptor.
        Size of each numeric range if specified. Data type should match numeric field data type specified in the query string.


        :param span: The span of this BucketCommandDescriptor.
        :type: float
        """
        self._span = span

    @property
    def ranges(self):
        """
        Gets the ranges of this BucketCommandDescriptor.
        List of the specified numeric ranges.


        :return: The ranges of this BucketCommandDescriptor.
        :rtype: list[oci.log_analytics.models.BucketRange]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """
        Sets the ranges of this BucketCommandDescriptor.
        List of the specified numeric ranges.


        :param ranges: The ranges of this BucketCommandDescriptor.
        :type: list[oci.log_analytics.models.BucketRange]
        """
        self._ranges = ranges

    @property
    def default_value(self):
        """
        Gets the default_value of this BucketCommandDescriptor.
        Default value to use in place of null if a result does not fit into any of the specified / calculated ranges.


        :return: The default_value of this BucketCommandDescriptor.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this BucketCommandDescriptor.
        Default value to use in place of null if a result does not fit into any of the specified / calculated ranges.


        :param default_value: The default_value of this BucketCommandDescriptor.
        :type: str
        """
        self._default_value = default_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
