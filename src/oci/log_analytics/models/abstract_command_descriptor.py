# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbstractCommandDescriptor(object):
    """
    Generic command descriptor defining all attributes common to all querylanguage commands for parse output.
    """

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "COMMAND"
    NAME_COMMAND = "COMMAND"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "SEARCH"
    NAME_SEARCH = "SEARCH"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "STATS"
    NAME_STATS = "STATS"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "TIME_STATS"
    NAME_TIME_STATS = "TIME_STATS"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "SORT"
    NAME_SORT = "SORT"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "FIELDS"
    NAME_FIELDS = "FIELDS"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "ADD_FIELDS"
    NAME_ADD_FIELDS = "ADD_FIELDS"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "LINK"
    NAME_LINK = "LINK"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "LINK_DETAILS"
    NAME_LINK_DETAILS = "LINK_DETAILS"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "CLUSTER"
    NAME_CLUSTER = "CLUSTER"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "CLUSTER_DETAILS"
    NAME_CLUSTER_DETAILS = "CLUSTER_DETAILS"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "CLUSTER_SPLIT"
    NAME_CLUSTER_SPLIT = "CLUSTER_SPLIT"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "EVAL"
    NAME_EVAL = "EVAL"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "EXTRACT"
    NAME_EXTRACT = "EXTRACT"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "EVENT_STATS"
    NAME_EVENT_STATS = "EVENT_STATS"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "BUCKET"
    NAME_BUCKET = "BUCKET"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "CLASSIFY"
    NAME_CLASSIFY = "CLASSIFY"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "TOP"
    NAME_TOP = "TOP"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "BOTTOM"
    NAME_BOTTOM = "BOTTOM"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "HEAD"
    NAME_HEAD = "HEAD"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "TAIL"
    NAME_TAIL = "TAIL"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "FIELD_SUMMARY"
    NAME_FIELD_SUMMARY = "FIELD_SUMMARY"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "REGEX"
    NAME_REGEX = "REGEX"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "RENAME"
    NAME_RENAME = "RENAME"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "TIME_COMPARE"
    NAME_TIME_COMPARE = "TIME_COMPARE"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "WHERE"
    NAME_WHERE = "WHERE"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "CLUSTER_COMPARE"
    NAME_CLUSTER_COMPARE = "CLUSTER_COMPARE"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "DELETE"
    NAME_DELETE = "DELETE"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "DELTA"
    NAME_DELTA = "DELTA"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "DISTINCT"
    NAME_DISTINCT = "DISTINCT"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "SEARCH_LOOKUP"
    NAME_SEARCH_LOOKUP = "SEARCH_LOOKUP"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "LOOKUP"
    NAME_LOOKUP = "LOOKUP"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "DEMO_MODE"
    NAME_DEMO_MODE = "DEMO_MODE"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "MACRO"
    NAME_MACRO = "MACRO"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "MULTI_SEARCH"
    NAME_MULTI_SEARCH = "MULTI_SEARCH"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "HIGHLIGHT"
    NAME_HIGHLIGHT = "HIGHLIGHT"

    #: A constant which can be used with the name property of a AbstractCommandDescriptor.
    #: This constant has a value of "HIGHLIGHT_ROWS"
    NAME_HIGHLIGHT_ROWS = "HIGHLIGHT_ROWS"

    def __init__(self, **kwargs):
        """
        Initializes a new AbstractCommandDescriptor object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.log_analytics.models.TopCommandDescriptor`
        * :class:`~oci.log_analytics.models.HighlightCommandDescriptor`
        * :class:`~oci.log_analytics.models.MultiSearchCommandDescriptor`
        * :class:`~oci.log_analytics.models.StatsCommandDescriptor`
        * :class:`~oci.log_analytics.models.TimeCompareCommandDescriptor`
        * :class:`~oci.log_analytics.models.TailCommandDescriptor`
        * :class:`~oci.log_analytics.models.RegexCommandDescriptor`
        * :class:`~oci.log_analytics.models.DeltaCommandDescriptor`
        * :class:`~oci.log_analytics.models.LookupCommandDescriptor`
        * :class:`~oci.log_analytics.models.DemoModeCommandDescriptor`
        * :class:`~oci.log_analytics.models.FieldSummaryCommandDescriptor`
        * :class:`~oci.log_analytics.models.EventStatsCommandDescriptor`
        * :class:`~oci.log_analytics.models.WhereCommandDescriptor`
        * :class:`~oci.log_analytics.models.ClusterSplitCommandDescriptor`
        * :class:`~oci.log_analytics.models.TimeStatsCommandDescriptor`
        * :class:`~oci.log_analytics.models.ClusterCommandDescriptor`
        * :class:`~oci.log_analytics.models.ClusterDetailsCommandDescriptor`
        * :class:`~oci.log_analytics.models.DeleteCommandDescriptor`
        * :class:`~oci.log_analytics.models.ClusterCompareCommandDescriptor`
        * :class:`~oci.log_analytics.models.SearchCommandDescriptor`
        * :class:`~oci.log_analytics.models.BucketCommandDescriptor`
        * :class:`~oci.log_analytics.models.CommandDescriptor`
        * :class:`~oci.log_analytics.models.DistinctCommandDescriptor`
        * :class:`~oci.log_analytics.models.LinkCommandDescriptor`
        * :class:`~oci.log_analytics.models.SortCommandDescriptor`
        * :class:`~oci.log_analytics.models.ExtractCommandDescriptor`
        * :class:`~oci.log_analytics.models.BottomCommandDescriptor`
        * :class:`~oci.log_analytics.models.FieldsCommandDescriptor`
        * :class:`~oci.log_analytics.models.HighlightRowsCommandDescriptor`
        * :class:`~oci.log_analytics.models.MacroCommandDescriptor`
        * :class:`~oci.log_analytics.models.ClassifyCommandDescriptor`
        * :class:`~oci.log_analytics.models.LinkDetailsCommandDescriptor`
        * :class:`~oci.log_analytics.models.SearchLookupCommandDescriptor`
        * :class:`~oci.log_analytics.models.HeadCommandDescriptor`
        * :class:`~oci.log_analytics.models.AddFieldsCommandDescriptor`
        * :class:`~oci.log_analytics.models.EvalCommandDescriptor`
        * :class:`~oci.log_analytics.models.RenameCommandDescriptor`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AbstractCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param display_query_string:
            The value to assign to the display_query_string property of this AbstractCommandDescriptor.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this AbstractCommandDescriptor.
        :type internal_query_string: str

        :param category:
            The value to assign to the category property of this AbstractCommandDescriptor.
        :type category: str

        :param referenced_fields:
            The value to assign to the referenced_fields property of this AbstractCommandDescriptor.
        :type referenced_fields: list[AbstractField]

        :param declared_fields:
            The value to assign to the declared_fields property of this AbstractCommandDescriptor.
        :type declared_fields: list[AbstractField]

        """
        self.swagger_types = {
            'name': 'str',
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'category': 'str',
            'referenced_fields': 'list[AbstractField]',
            'declared_fields': 'list[AbstractField]'
        }

        self.attribute_map = {
            'name': 'name',
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'category': 'category',
            'referenced_fields': 'referencedFields',
            'declared_fields': 'declaredFields'
        }

        self._name = None
        self._display_query_string = None
        self._internal_query_string = None
        self._category = None
        self._referenced_fields = None
        self._declared_fields = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['name']

        if type == 'TOP':
            return 'TopCommandDescriptor'

        if type == 'HIGHLIGHT':
            return 'HighlightCommandDescriptor'

        if type == 'MULTI_SEARCH':
            return 'MultiSearchCommandDescriptor'

        if type == 'STATS':
            return 'StatsCommandDescriptor'

        if type == 'TIME_COMPARE':
            return 'TimeCompareCommandDescriptor'

        if type == 'TAIL':
            return 'TailCommandDescriptor'

        if type == 'REGEX':
            return 'RegexCommandDescriptor'

        if type == 'DELTA':
            return 'DeltaCommandDescriptor'

        if type == 'LOOKUP':
            return 'LookupCommandDescriptor'

        if type == 'DEMO_MODE':
            return 'DemoModeCommandDescriptor'

        if type == 'FIELD_SUMMARY':
            return 'FieldSummaryCommandDescriptor'

        if type == 'EVENT_STATS':
            return 'EventStatsCommandDescriptor'

        if type == 'WHERE':
            return 'WhereCommandDescriptor'

        if type == 'CLUSTER_SPLIT':
            return 'ClusterSplitCommandDescriptor'

        if type == 'TIME_STATS':
            return 'TimeStatsCommandDescriptor'

        if type == 'CLUSTER':
            return 'ClusterCommandDescriptor'

        if type == 'CLUSTER_DETAILS':
            return 'ClusterDetailsCommandDescriptor'

        if type == 'DELETE':
            return 'DeleteCommandDescriptor'

        if type == 'CLUSTER_COMPARE':
            return 'ClusterCompareCommandDescriptor'

        if type == 'SEARCH':
            return 'SearchCommandDescriptor'

        if type == 'BUCKET':
            return 'BucketCommandDescriptor'

        if type == 'COMMAND':
            return 'CommandDescriptor'

        if type == 'DISTINCT':
            return 'DistinctCommandDescriptor'

        if type == 'LINK':
            return 'LinkCommandDescriptor'

        if type == 'SORT':
            return 'SortCommandDescriptor'

        if type == 'EXTRACT':
            return 'ExtractCommandDescriptor'

        if type == 'BOTTOM':
            return 'BottomCommandDescriptor'

        if type == 'FIELDS':
            return 'FieldsCommandDescriptor'

        if type == 'HIGHLIGHT_ROWS':
            return 'HighlightRowsCommandDescriptor'

        if type == 'MACRO':
            return 'MacroCommandDescriptor'

        if type == 'CLASSIFY':
            return 'ClassifyCommandDescriptor'

        if type == 'LINK_DETAILS':
            return 'LinkDetailsCommandDescriptor'

        if type == 'SEARCH_LOOKUP':
            return 'SearchLookupCommandDescriptor'

        if type == 'HEAD':
            return 'HeadCommandDescriptor'

        if type == 'ADD_FIELDS':
            return 'AddFieldsCommandDescriptor'

        if type == 'EVAL':
            return 'EvalCommandDescriptor'

        if type == 'RENAME':
            return 'RenameCommandDescriptor'
        else:
            return 'AbstractCommandDescriptor'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AbstractCommandDescriptor.
        Name of querylanguage command

        Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this AbstractCommandDescriptor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AbstractCommandDescriptor.
        Name of querylanguage command


        :param name: The name of this AbstractCommandDescriptor.
        :type: str
        """
        allowed_values = ["COMMAND", "SEARCH", "STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    @property
    def display_query_string(self):
        """
        **[Required]** Gets the display_query_string of this AbstractCommandDescriptor.
        Command fragment display string from user specified query string formatted by query builder.


        :return: The display_query_string of this AbstractCommandDescriptor.
        :rtype: str
        """
        return self._display_query_string

    @display_query_string.setter
    def display_query_string(self, display_query_string):
        """
        Sets the display_query_string of this AbstractCommandDescriptor.
        Command fragment display string from user specified query string formatted by query builder.


        :param display_query_string: The display_query_string of this AbstractCommandDescriptor.
        :type: str
        """
        self._display_query_string = display_query_string

    @property
    def internal_query_string(self):
        """
        **[Required]** Gets the internal_query_string of this AbstractCommandDescriptor.
        Command fragment internal string from user specified query string formatted by query builder.


        :return: The internal_query_string of this AbstractCommandDescriptor.
        :rtype: str
        """
        return self._internal_query_string

    @internal_query_string.setter
    def internal_query_string(self, internal_query_string):
        """
        Sets the internal_query_string of this AbstractCommandDescriptor.
        Command fragment internal string from user specified query string formatted by query builder.


        :param internal_query_string: The internal_query_string of this AbstractCommandDescriptor.
        :type: str
        """
        self._internal_query_string = internal_query_string

    @property
    def category(self):
        """
        Gets the category of this AbstractCommandDescriptor.
        querylanguage command designation for example; reporting vs filtering


        :return: The category of this AbstractCommandDescriptor.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this AbstractCommandDescriptor.
        querylanguage command designation for example; reporting vs filtering


        :param category: The category of this AbstractCommandDescriptor.
        :type: str
        """
        self._category = category

    @property
    def referenced_fields(self):
        """
        Gets the referenced_fields of this AbstractCommandDescriptor.
        Fields referenced in command fragment from user specified query string.


        :return: The referenced_fields of this AbstractCommandDescriptor.
        :rtype: list[AbstractField]
        """
        return self._referenced_fields

    @referenced_fields.setter
    def referenced_fields(self, referenced_fields):
        """
        Sets the referenced_fields of this AbstractCommandDescriptor.
        Fields referenced in command fragment from user specified query string.


        :param referenced_fields: The referenced_fields of this AbstractCommandDescriptor.
        :type: list[AbstractField]
        """
        self._referenced_fields = referenced_fields

    @property
    def declared_fields(self):
        """
        Gets the declared_fields of this AbstractCommandDescriptor.
        Fields declared in command fragment from user specified query string.


        :return: The declared_fields of this AbstractCommandDescriptor.
        :rtype: list[AbstractField]
        """
        return self._declared_fields

    @declared_fields.setter
    def declared_fields(self, declared_fields):
        """
        Sets the declared_fields of this AbstractCommandDescriptor.
        Fields declared in command fragment from user specified query string.


        :param declared_fields: The declared_fields of this AbstractCommandDescriptor.
        :type: list[AbstractField]
        """
        self._declared_fields = declared_fields

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
