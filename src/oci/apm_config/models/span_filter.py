# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .config import Config
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SpanFilter(Config):
    """
    A named setting that specifies the filter criteria to match a subset of the spans.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SpanFilter object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_config.models.SpanFilter.config_type` attribute
        of this class is ``SPAN_FILTER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SpanFilter.
        :type id: str

        :param config_type:
            The value to assign to the config_type property of this SpanFilter.
            Allowed values for this property are: "SPAN_FILTER", "METRIC_GROUP", "APDEX", "OPTIONS"
        :type config_type: str

        :param time_created:
            The value to assign to the time_created property of this SpanFilter.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SpanFilter.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SpanFilter.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SpanFilter.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this SpanFilter.
        :type display_name: str

        :param filter_text:
            The value to assign to the filter_text property of this SpanFilter.
        :type filter_text: str

        :param description:
            The value to assign to the description property of this SpanFilter.
        :type description: str

        """
        self.swagger_types = {
            'id': 'str',
            'config_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'filter_text': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'config_type': 'configType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'filter_text': 'filterText',
            'description': 'description'
        }

        self._id = None
        self._config_type = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._display_name = None
        self._filter_text = None
        self._description = None
        self._config_type = 'SPAN_FILTER'

    @property
    def display_name(self):
        """
        Gets the display_name of this SpanFilter.
        The name by which a configuration entity is displayed to the end user.


        :return: The display_name of this SpanFilter.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SpanFilter.
        The name by which a configuration entity is displayed to the end user.


        :param display_name: The display_name of this SpanFilter.
        :type: str
        """
        self._display_name = display_name

    @property
    def filter_text(self):
        """
        Gets the filter_text of this SpanFilter.
        The string that defines the Span Filter expression.


        :return: The filter_text of this SpanFilter.
        :rtype: str
        """
        return self._filter_text

    @filter_text.setter
    def filter_text(self, filter_text):
        """
        Sets the filter_text of this SpanFilter.
        The string that defines the Span Filter expression.


        :param filter_text: The filter_text of this SpanFilter.
        :type: str
        """
        self._filter_text = filter_text

    @property
    def description(self):
        """
        Gets the description of this SpanFilter.
        An optional string that describes what the span filter is intended or used for.


        :return: The description of this SpanFilter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SpanFilter.
        An optional string that describes what the span filter is intended or used for.


        :param description: The description of this SpanFilter.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
