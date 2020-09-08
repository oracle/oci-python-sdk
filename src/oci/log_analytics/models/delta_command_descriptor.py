# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_command_descriptor import AbstractCommandDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeltaCommandDescriptor(AbstractCommandDescriptor):
    """
    Command descriptor for querylanguage DELTA command.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeltaCommandDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.DeltaCommandDescriptor.name` attribute
        of this class is ``DELTA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DeltaCommandDescriptor.
            Allowed values for this property are: "COMMAND", "SEARCH", "STATS", "TIME_STATS", "SORT", "FIELDS", "ADD_FIELDS", "LINK", "LINK_DETAILS", "CLUSTER", "CLUSTER_DETAILS", "CUSLTER_SPLIT", "EVAL", "EXTRACT", "EVENT_STATS", "BUCKET", "CLASSIFY", "TOP", "BOTTOM", "HEAD", "TAIL", "FIELD_SUMMARY", "REGEX", "RENAME", "TIME_COMPARE", "WHERE", "CLUSTER_COMPARE", "DELETE", "DELTA", "DISTINCT", "SEARCH_LOOKUP", "LOOKUP", "DEMO_MODE", "MACRO", "MULTI_SEARCH", "HIGHLIGHT", "HIGHLIGHT_ROWS"
        :type name: str

        :param display_query_string:
            The value to assign to the display_query_string property of this DeltaCommandDescriptor.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this DeltaCommandDescriptor.
        :type internal_query_string: str

        :param category:
            The value to assign to the category property of this DeltaCommandDescriptor.
        :type category: str

        :param referenced_fields:
            The value to assign to the referenced_fields property of this DeltaCommandDescriptor.
        :type referenced_fields: list[AbstractField]

        :param declared_fields:
            The value to assign to the declared_fields property of this DeltaCommandDescriptor.
        :type declared_fields: list[AbstractField]

        :param step:
            The value to assign to the step property of this DeltaCommandDescriptor.
        :type step: int

        """
        self.swagger_types = {
            'name': 'str',
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'category': 'str',
            'referenced_fields': 'list[AbstractField]',
            'declared_fields': 'list[AbstractField]',
            'step': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'category': 'category',
            'referenced_fields': 'referencedFields',
            'declared_fields': 'declaredFields',
            'step': 'step'
        }

        self._name = None
        self._display_query_string = None
        self._internal_query_string = None
        self._category = None
        self._referenced_fields = None
        self._declared_fields = None
        self._step = None
        self._name = 'DELTA'

    @property
    def step(self):
        """
        Gets the step of this DeltaCommandDescriptor.
        Value specified in DELTA command in queryString if set controlling whether delta is calculating difference between consecutive result rows or skipping N rows for each calculation.


        :return: The step of this DeltaCommandDescriptor.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """
        Sets the step of this DeltaCommandDescriptor.
        Value specified in DELTA command in queryString if set controlling whether delta is calculating difference between consecutive result rows or skipping N rows for each calculation.


        :param step: The step of this DeltaCommandDescriptor.
        :type: int
        """
        self._step = step

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
