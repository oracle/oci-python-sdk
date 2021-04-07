# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrationPhaseSummary(object):
    """
    Migration Phase Summary of details.
    """

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_VALIDATE_TGT"
    NAME_ODMS_VALIDATE_TGT = "ODMS_VALIDATE_TGT"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_VALIDATE_SRC"
    NAME_ODMS_VALIDATE_SRC = "ODMS_VALIDATE_SRC"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_VALIDATE_GG_HUB"
    NAME_ODMS_VALIDATE_GG_HUB = "ODMS_VALIDATE_GG_HUB"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS"
    NAME_ODMS_VALIDATE_DATAPUMP_SETTINGS = "ODMS_VALIDATE_DATAPUMP_SETTINGS"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC"
    NAME_ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC = "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT"
    NAME_ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT = "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_VALIDATE"
    NAME_ODMS_VALIDATE = "ODMS_VALIDATE"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_PREPARE"
    NAME_ODMS_PREPARE = "ODMS_PREPARE"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_INITIAL_LOAD_EXPORT"
    NAME_ODMS_INITIAL_LOAD_EXPORT = "ODMS_INITIAL_LOAD_EXPORT"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_DATA_UPLOAD"
    NAME_ODMS_DATA_UPLOAD = "ODMS_DATA_UPLOAD"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_INITIAL_LOAD_IMPORT"
    NAME_ODMS_INITIAL_LOAD_IMPORT = "ODMS_INITIAL_LOAD_IMPORT"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_POST_INITIAL_LOAD"
    NAME_ODMS_POST_INITIAL_LOAD = "ODMS_POST_INITIAL_LOAD"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_PREPARE_REPLICATION_TARGET"
    NAME_ODMS_PREPARE_REPLICATION_TARGET = "ODMS_PREPARE_REPLICATION_TARGET"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_MONITOR_REPLICATION_LAG"
    NAME_ODMS_MONITOR_REPLICATION_LAG = "ODMS_MONITOR_REPLICATION_LAG"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_SWITCHOVER"
    NAME_ODMS_SWITCHOVER = "ODMS_SWITCHOVER"

    #: A constant which can be used with the name property of a MigrationPhaseSummary.
    #: This constant has a value of "ODMS_CLEANUP"
    NAME_ODMS_CLEANUP = "ODMS_CLEANUP"

    #: A constant which can be used with the recommended_action property of a MigrationPhaseSummary.
    #: This constant has a value of "WAIT"
    RECOMMENDED_ACTION_WAIT = "WAIT"

    def __init__(self, **kwargs):
        """
        Initializes a new MigrationPhaseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this MigrationPhaseSummary.
            Allowed values for this property are: "ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param recommended_action:
            The value to assign to the recommended_action property of this MigrationPhaseSummary.
            Allowed values for this property are: "WAIT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type recommended_action: str

        :param supported_actions:
            The value to assign to the supported_actions property of this MigrationPhaseSummary.
        :type supported_actions: list[oci.database_migration.models.OdmsPhaseActions]

        """
        self.swagger_types = {
            'name': 'str',
            'recommended_action': 'str',
            'supported_actions': 'list[OdmsPhaseActions]'
        }

        self.attribute_map = {
            'name': 'name',
            'recommended_action': 'recommendedAction',
            'supported_actions': 'supportedActions'
        }

        self._name = None
        self._recommended_action = None
        self._supported_actions = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MigrationPhaseSummary.
        ODMS Job phase name

        Allowed values for this property are: "ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this MigrationPhaseSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MigrationPhaseSummary.
        ODMS Job phase name


        :param name: The name of this MigrationPhaseSummary.
        :type: str
        """
        allowed_values = ["ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    @property
    def recommended_action(self):
        """
        Gets the recommended_action of this MigrationPhaseSummary.
        Action recommended for this phase. If not included in the response, there is no recommended action for the phase.

        Allowed values for this property are: "WAIT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The recommended_action of this MigrationPhaseSummary.
        :rtype: str
        """
        return self._recommended_action

    @recommended_action.setter
    def recommended_action(self, recommended_action):
        """
        Sets the recommended_action of this MigrationPhaseSummary.
        Action recommended for this phase. If not included in the response, there is no recommended action for the phase.


        :param recommended_action: The recommended_action of this MigrationPhaseSummary.
        :type: str
        """
        allowed_values = ["WAIT"]
        if not value_allowed_none_or_none_sentinel(recommended_action, allowed_values):
            recommended_action = 'UNKNOWN_ENUM_VALUE'
        self._recommended_action = recommended_action

    @property
    def supported_actions(self):
        """
        **[Required]** Gets the supported_actions of this MigrationPhaseSummary.
        Array of actions for the corresponding phase. Empty array would indicate there is no supported action for the phase.


        :return: The supported_actions of this MigrationPhaseSummary.
        :rtype: list[oci.database_migration.models.OdmsPhaseActions]
        """
        return self._supported_actions

    @supported_actions.setter
    def supported_actions(self, supported_actions):
        """
        Sets the supported_actions of this MigrationPhaseSummary.
        Array of actions for the corresponding phase. Empty array would indicate there is no supported action for the phase.


        :param supported_actions: The supported_actions of this MigrationPhaseSummary.
        :type: list[oci.database_migration.models.OdmsPhaseActions]
        """
        self._supported_actions = supported_actions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
