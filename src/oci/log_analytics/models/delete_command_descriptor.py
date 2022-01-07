# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_command_descriptor import AbstractCommandDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeleteCommandDescriptor(AbstractCommandDescriptor):
    """
    Command descriptor for querylanguage DELETE command.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeleteCommandDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.DeleteCommandDescriptor.name` attribute
        of this class is ``DELETE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DeleteCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "GEO_STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CLUSTER_SPLIT", "EVAL", "EXTRACT", "JSON_EXTRACT", "XML_EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS", "HIGHLIGHT_GROUPS", "CREATE_VIEW", "MAP", "NLP", "COMPARE"
        :type name: str

        :param display_query_string:
            The value to assign to the display_query_string property of this DeleteCommandDescriptor.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this DeleteCommandDescriptor.
        :type internal_query_string: str

        :param category:
            The value to assign to the category property of this DeleteCommandDescriptor.
        :type category: str

        :param referenced_fields:
            The value to assign to the referenced_fields property of this DeleteCommandDescriptor.
        :type referenced_fields: list[oci.log_analytics.models.AbstractField]

        :param declared_fields:
            The value to assign to the declared_fields property of this DeleteCommandDescriptor.
        :type declared_fields: list[oci.log_analytics.models.AbstractField]

        :param is_dry_run:
            The value to assign to the is_dry_run property of this DeleteCommandDescriptor.
        :type is_dry_run: bool

        """
        self.swagger_types = {
            'name': 'str',
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'category': 'str',
            'referenced_fields': 'list[AbstractField]',
            'declared_fields': 'list[AbstractField]',
            'is_dry_run': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'category': 'category',
            'referenced_fields': 'referencedFields',
            'declared_fields': 'declaredFields',
            'is_dry_run': 'isDryRun'
        }

        self._name = None
        self._display_query_string = None
        self._internal_query_string = None
        self._category = None
        self._referenced_fields = None
        self._declared_fields = None
        self._is_dry_run = None
        self._name = 'DELETE'

    @property
    def is_dry_run(self):
        """
        Gets the is_dry_run of this DeleteCommandDescriptor.
        Value specified in DELETE command in queryString as to whether the delete is a dry-run (only report number of rows removed) rather than actually remove matching log records.


        :return: The is_dry_run of this DeleteCommandDescriptor.
        :rtype: bool
        """
        return self._is_dry_run

    @is_dry_run.setter
    def is_dry_run(self, is_dry_run):
        """
        Sets the is_dry_run of this DeleteCommandDescriptor.
        Value specified in DELETE command in queryString as to whether the delete is a dry-run (only report number of rows removed) rather than actually remove matching log records.


        :param is_dry_run: The is_dry_run of this DeleteCommandDescriptor.
        :type: bool
        """
        self._is_dry_run = is_dry_run

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
