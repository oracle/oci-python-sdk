# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .config import Config
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApdexRules(Config):
    """
    The set of Apdex rules to be used in Apdex computation. In the current version, only one rule set can exist in the
    configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApdexRules object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_config.models.ApdexRules.config_type` attribute
        of this class is ``APDEX`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ApdexRules.
        :type id: str

        :param config_type:
            The value to assign to the config_type property of this ApdexRules.
            Allowed values for this property are: "SPAN_FILTER", "METRIC_GROUP", "APDEX"
        :type config_type: str

        :param time_created:
            The value to assign to the time_created property of this ApdexRules.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ApdexRules.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ApdexRules.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ApdexRules.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ApdexRules.
        :type display_name: str

        :param rules:
            The value to assign to the rules property of this ApdexRules.
        :type rules: list[oci.apm_config.models.Apdex]

        """
        self.swagger_types = {
            'id': 'str',
            'config_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'rules': 'list[Apdex]'
        }

        self.attribute_map = {
            'id': 'id',
            'config_type': 'configType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'rules': 'rules'
        }

        self._id = None
        self._config_type = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._display_name = None
        self._rules = None
        self._config_type = 'APDEX'

    @property
    def display_name(self):
        """
        Gets the display_name of this ApdexRules.
        The name by which the rule set is displayed to the end user.


        :return: The display_name of this ApdexRules.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApdexRules.
        The name by which the rule set is displayed to the end user.


        :param display_name: The display_name of this ApdexRules.
        :type: str
        """
        self._display_name = display_name

    @property
    def rules(self):
        """
        Gets the rules of this ApdexRules.

        :return: The rules of this ApdexRules.
        :rtype: list[oci.apm_config.models.Apdex]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this ApdexRules.

        :param rules: The rules of this ApdexRules.
        :type: list[oci.apm_config.models.Apdex]
        """
        self._rules = rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
