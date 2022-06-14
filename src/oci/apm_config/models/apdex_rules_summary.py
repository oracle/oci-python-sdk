# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .config_summary import ConfigSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApdexRulesSummary(ConfigSummary):
    """
    The set of Apdex rules used in Apdex computation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApdexRulesSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_config.models.ApdexRulesSummary.config_type` attribute
        of this class is ``APDEX`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ApdexRulesSummary.
        :type id: str

        :param config_type:
            The value to assign to the config_type property of this ApdexRulesSummary.
            Allowed values for this property are: "SPAN_FILTER", "METRIC_GROUP", "APDEX", "OPTIONS"
        :type config_type: str

        :param time_created:
            The value to assign to the time_created property of this ApdexRulesSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ApdexRulesSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ApdexRulesSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ApdexRulesSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param rules:
            The value to assign to the rules property of this ApdexRulesSummary.
        :type rules: list[oci.apm_config.models.Apdex]

        :param display_name:
            The value to assign to the display_name property of this ApdexRulesSummary.
        :type display_name: str

        """
        self.swagger_types = {
            'id': 'str',
            'config_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'rules': 'list[Apdex]',
            'display_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'config_type': 'configType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'rules': 'rules',
            'display_name': 'displayName'
        }

        self._id = None
        self._config_type = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._rules = None
        self._display_name = None
        self._config_type = 'APDEX'

    @property
    def rules(self):
        """
        Gets the rules of this ApdexRulesSummary.

        :return: The rules of this ApdexRulesSummary.
        :rtype: list[oci.apm_config.models.Apdex]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this ApdexRulesSummary.

        :param rules: The rules of this ApdexRulesSummary.
        :type: list[oci.apm_config.models.Apdex]
        """
        self._rules = rules

    @property
    def display_name(self):
        """
        Gets the display_name of this ApdexRulesSummary.
        The name by which a configuration entity is displayed to the end user.


        :return: The display_name of this ApdexRulesSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApdexRulesSummary.
        The name by which a configuration entity is displayed to the end user.


        :param display_name: The display_name of this ApdexRulesSummary.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
