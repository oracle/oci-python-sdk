# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .config_summary import ConfigSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OptionsSummary(ConfigSummary):
    """
    An Options object represents configuration options.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OptionsSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_config.models.OptionsSummary.config_type` attribute
        of this class is ``OPTIONS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OptionsSummary.
        :type id: str

        :param config_type:
            The value to assign to the config_type property of this OptionsSummary.
            Allowed values for this property are: "SPAN_FILTER", "METRIC_GROUP", "APDEX", "OPTIONS"
        :type config_type: str

        :param time_created:
            The value to assign to the time_created property of this OptionsSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OptionsSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OptionsSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OptionsSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this OptionsSummary.
        :type display_name: str

        :param options:
            The value to assign to the options property of this OptionsSummary.
        :type options: object

        :param group:
            The value to assign to the group property of this OptionsSummary.
        :type group: str

        :param description:
            The value to assign to the description property of this OptionsSummary.
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
            'options': 'object',
            'group': 'str',
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
            'options': 'options',
            'group': 'group',
            'description': 'description'
        }

        self._id = None
        self._config_type = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._display_name = None
        self._options = None
        self._group = None
        self._description = None
        self._config_type = 'OPTIONS'

    @property
    def display_name(self):
        """
        Gets the display_name of this OptionsSummary.
        The name by which a configuration entity is displayed to the end user.


        :return: The display_name of this OptionsSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OptionsSummary.
        The name by which a configuration entity is displayed to the end user.


        :param display_name: The display_name of this OptionsSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def options(self):
        """
        Gets the options of this OptionsSummary.
        The options are stored here as JSON.


        :return: The options of this OptionsSummary.
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this OptionsSummary.
        The options are stored here as JSON.


        :param options: The options of this OptionsSummary.
        :type: object
        """
        self._options = options

    @property
    def group(self):
        """
        Gets the group of this OptionsSummary.
        A string that specifies the group that an OPTIONS item belongs to.


        :return: The group of this OptionsSummary.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this OptionsSummary.
        A string that specifies the group that an OPTIONS item belongs to.


        :param group: The group of this OptionsSummary.
        :type: str
        """
        self._group = group

    @property
    def description(self):
        """
        Gets the description of this OptionsSummary.
        An optional string that describes what the options are intended or used for.


        :return: The description of this OptionsSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OptionsSummary.
        An optional string that describes what the options are intended or used for.


        :param description: The description of this OptionsSummary.
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
