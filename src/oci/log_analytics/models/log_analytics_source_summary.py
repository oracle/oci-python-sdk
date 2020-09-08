# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsSourceSummary(object):
    """
    LogAnalyticsSourceSummary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsSourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label_conditions:
            The value to assign to the label_conditions property of this LogAnalyticsSourceSummary.
        :type label_conditions: list[LogAnalyticsSourceLabelCondition]

        :param association_count:
            The value to assign to the association_count property of this LogAnalyticsSourceSummary.
        :type association_count: int

        :param association_entity:
            The value to assign to the association_entity property of this LogAnalyticsSourceSummary.
        :type association_entity: list[LogAnalyticsAssociation]

        :param data_filter_definitions:
            The value to assign to the data_filter_definitions property of this LogAnalyticsSourceSummary.
        :type data_filter_definitions: list[LogAnalyticsSourceDataFilter]

        :param database_credential:
            The value to assign to the database_credential property of this LogAnalyticsSourceSummary.
        :type database_credential: str

        :param extended_field_definitions:
            The value to assign to the extended_field_definitions property of this LogAnalyticsSourceSummary.
        :type extended_field_definitions: list[LogAnalyticsSourceExtendedFieldDefinition]

        :param is_for_cloud:
            The value to assign to the is_for_cloud property of this LogAnalyticsSourceSummary.
        :type is_for_cloud: bool

        :param labels:
            The value to assign to the labels property of this LogAnalyticsSourceSummary.
        :type labels: list[LogAnalyticsLabelView]

        :param metric_definitions:
            The value to assign to the metric_definitions property of this LogAnalyticsSourceSummary.
        :type metric_definitions: list[LogAnalyticsMetric]

        :param metrics:
            The value to assign to the metrics property of this LogAnalyticsSourceSummary.
        :type metrics: list[LogAnalyticsSourceMetric]

        :param oob_parsers:
            The value to assign to the oob_parsers property of this LogAnalyticsSourceSummary.
        :type oob_parsers: list[LogAnalyticsParser]

        :param parameters:
            The value to assign to the parameters property of this LogAnalyticsSourceSummary.
        :type parameters: list[LogAnalyticsParameter]

        :param pattern_count:
            The value to assign to the pattern_count property of this LogAnalyticsSourceSummary.
        :type pattern_count: int

        :param patterns:
            The value to assign to the patterns property of this LogAnalyticsSourceSummary.
        :type patterns: list[LogAnalyticsSourcePattern]

        :param description:
            The value to assign to the description property of this LogAnalyticsSourceSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsSourceSummary.
        :type display_name: str

        :param edit_version:
            The value to assign to the edit_version property of this LogAnalyticsSourceSummary.
        :type edit_version: int

        :param functions:
            The value to assign to the functions property of this LogAnalyticsSourceSummary.
        :type functions: list[LogAnalyticsSourceFunction]

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsSourceSummary.
        :type source_id: int

        :param name:
            The value to assign to the name property of this LogAnalyticsSourceSummary.
        :type name: str

        :param is_secure_content:
            The value to assign to the is_secure_content property of this LogAnalyticsSourceSummary.
        :type is_secure_content: bool

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsSourceSummary.
        :type is_system: bool

        :param parsers:
            The value to assign to the parsers property of this LogAnalyticsSourceSummary.
        :type parsers: list[LogAnalyticsParser]

        :param is_auto_association_enabled:
            The value to assign to the is_auto_association_enabled property of this LogAnalyticsSourceSummary.
        :type is_auto_association_enabled: bool

        :param is_auto_association_override:
            The value to assign to the is_auto_association_override property of this LogAnalyticsSourceSummary.
        :type is_auto_association_override: bool

        :param rule_id:
            The value to assign to the rule_id property of this LogAnalyticsSourceSummary.
        :type rule_id: int

        :param type_name:
            The value to assign to the type_name property of this LogAnalyticsSourceSummary.
        :type type_name: str

        :param type_display_name:
            The value to assign to the type_display_name property of this LogAnalyticsSourceSummary.
        :type type_display_name: str

        :param warning_config:
            The value to assign to the warning_config property of this LogAnalyticsSourceSummary.
        :type warning_config: int

        :param metadata_fields:
            The value to assign to the metadata_fields property of this LogAnalyticsSourceSummary.
        :type metadata_fields: list[LogAnalyticsSourceMetadataField]

        :param label_definitions:
            The value to assign to the label_definitions property of this LogAnalyticsSourceSummary.
        :type label_definitions: list[LogAnalyticsLabelDefinition]

        :param entity_types:
            The value to assign to the entity_types property of this LogAnalyticsSourceSummary.
        :type entity_types: list[LogAnalyticsSourceEntityType]

        :param is_timezone_override:
            The value to assign to the is_timezone_override property of this LogAnalyticsSourceSummary.
        :type is_timezone_override: bool

        :param user_parsers:
            The value to assign to the user_parsers property of this LogAnalyticsSourceSummary.
        :type user_parsers: list[LogAnalyticsParser]

        :param time_updated:
            The value to assign to the time_updated property of this LogAnalyticsSourceSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'label_conditions': 'list[LogAnalyticsSourceLabelCondition]',
            'association_count': 'int',
            'association_entity': 'list[LogAnalyticsAssociation]',
            'data_filter_definitions': 'list[LogAnalyticsSourceDataFilter]',
            'database_credential': 'str',
            'extended_field_definitions': 'list[LogAnalyticsSourceExtendedFieldDefinition]',
            'is_for_cloud': 'bool',
            'labels': 'list[LogAnalyticsLabelView]',
            'metric_definitions': 'list[LogAnalyticsMetric]',
            'metrics': 'list[LogAnalyticsSourceMetric]',
            'oob_parsers': 'list[LogAnalyticsParser]',
            'parameters': 'list[LogAnalyticsParameter]',
            'pattern_count': 'int',
            'patterns': 'list[LogAnalyticsSourcePattern]',
            'description': 'str',
            'display_name': 'str',
            'edit_version': 'int',
            'functions': 'list[LogAnalyticsSourceFunction]',
            'source_id': 'int',
            'name': 'str',
            'is_secure_content': 'bool',
            'is_system': 'bool',
            'parsers': 'list[LogAnalyticsParser]',
            'is_auto_association_enabled': 'bool',
            'is_auto_association_override': 'bool',
            'rule_id': 'int',
            'type_name': 'str',
            'type_display_name': 'str',
            'warning_config': 'int',
            'metadata_fields': 'list[LogAnalyticsSourceMetadataField]',
            'label_definitions': 'list[LogAnalyticsLabelDefinition]',
            'entity_types': 'list[LogAnalyticsSourceEntityType]',
            'is_timezone_override': 'bool',
            'user_parsers': 'list[LogAnalyticsParser]',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'label_conditions': 'labelConditions',
            'association_count': 'associationCount',
            'association_entity': 'associationEntity',
            'data_filter_definitions': 'dataFilterDefinitions',
            'database_credential': 'databaseCredential',
            'extended_field_definitions': 'extendedFieldDefinitions',
            'is_for_cloud': 'isForCloud',
            'labels': 'labels',
            'metric_definitions': 'metricDefinitions',
            'metrics': 'metrics',
            'oob_parsers': 'oobParsers',
            'parameters': 'parameters',
            'pattern_count': 'patternCount',
            'patterns': 'patterns',
            'description': 'description',
            'display_name': 'displayName',
            'edit_version': 'editVersion',
            'functions': 'functions',
            'source_id': 'sourceId',
            'name': 'name',
            'is_secure_content': 'isSecureContent',
            'is_system': 'isSystem',
            'parsers': 'parsers',
            'is_auto_association_enabled': 'isAutoAssociationEnabled',
            'is_auto_association_override': 'isAutoAssociationOverride',
            'rule_id': 'ruleId',
            'type_name': 'typeName',
            'type_display_name': 'typeDisplayName',
            'warning_config': 'warningConfig',
            'metadata_fields': 'metadataFields',
            'label_definitions': 'labelDefinitions',
            'entity_types': 'entityTypes',
            'is_timezone_override': 'isTimezoneOverride',
            'user_parsers': 'userParsers',
            'time_updated': 'timeUpdated'
        }

        self._label_conditions = None
        self._association_count = None
        self._association_entity = None
        self._data_filter_definitions = None
        self._database_credential = None
        self._extended_field_definitions = None
        self._is_for_cloud = None
        self._labels = None
        self._metric_definitions = None
        self._metrics = None
        self._oob_parsers = None
        self._parameters = None
        self._pattern_count = None
        self._patterns = None
        self._description = None
        self._display_name = None
        self._edit_version = None
        self._functions = None
        self._source_id = None
        self._name = None
        self._is_secure_content = None
        self._is_system = None
        self._parsers = None
        self._is_auto_association_enabled = None
        self._is_auto_association_override = None
        self._rule_id = None
        self._type_name = None
        self._type_display_name = None
        self._warning_config = None
        self._metadata_fields = None
        self._label_definitions = None
        self._entity_types = None
        self._is_timezone_override = None
        self._user_parsers = None
        self._time_updated = None

    @property
    def label_conditions(self):
        """
        Gets the label_conditions of this LogAnalyticsSourceSummary.
        alert conditions


        :return: The label_conditions of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsSourceLabelCondition]
        """
        return self._label_conditions

    @label_conditions.setter
    def label_conditions(self, label_conditions):
        """
        Sets the label_conditions of this LogAnalyticsSourceSummary.
        alert conditions


        :param label_conditions: The label_conditions of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsSourceLabelCondition]
        """
        self._label_conditions = label_conditions

    @property
    def association_count(self):
        """
        Gets the association_count of this LogAnalyticsSourceSummary.
        association count


        :return: The association_count of this LogAnalyticsSourceSummary.
        :rtype: int
        """
        return self._association_count

    @association_count.setter
    def association_count(self, association_count):
        """
        Sets the association_count of this LogAnalyticsSourceSummary.
        association count


        :param association_count: The association_count of this LogAnalyticsSourceSummary.
        :type: int
        """
        self._association_count = association_count

    @property
    def association_entity(self):
        """
        Gets the association_entity of this LogAnalyticsSourceSummary.
        association entity


        :return: The association_entity of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsAssociation]
        """
        return self._association_entity

    @association_entity.setter
    def association_entity(self, association_entity):
        """
        Sets the association_entity of this LogAnalyticsSourceSummary.
        association entity


        :param association_entity: The association_entity of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsAssociation]
        """
        self._association_entity = association_entity

    @property
    def data_filter_definitions(self):
        """
        Gets the data_filter_definitions of this LogAnalyticsSourceSummary.
        data filter definitions


        :return: The data_filter_definitions of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsSourceDataFilter]
        """
        return self._data_filter_definitions

    @data_filter_definitions.setter
    def data_filter_definitions(self, data_filter_definitions):
        """
        Sets the data_filter_definitions of this LogAnalyticsSourceSummary.
        data filter definitions


        :param data_filter_definitions: The data_filter_definitions of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsSourceDataFilter]
        """
        self._data_filter_definitions = data_filter_definitions

    @property
    def database_credential(self):
        """
        Gets the database_credential of this LogAnalyticsSourceSummary.
        DB credential


        :return: The database_credential of this LogAnalyticsSourceSummary.
        :rtype: str
        """
        return self._database_credential

    @database_credential.setter
    def database_credential(self, database_credential):
        """
        Sets the database_credential of this LogAnalyticsSourceSummary.
        DB credential


        :param database_credential: The database_credential of this LogAnalyticsSourceSummary.
        :type: str
        """
        self._database_credential = database_credential

    @property
    def extended_field_definitions(self):
        """
        Gets the extended_field_definitions of this LogAnalyticsSourceSummary.
        extended field definition


        :return: The extended_field_definitions of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsSourceExtendedFieldDefinition]
        """
        return self._extended_field_definitions

    @extended_field_definitions.setter
    def extended_field_definitions(self, extended_field_definitions):
        """
        Sets the extended_field_definitions of this LogAnalyticsSourceSummary.
        extended field definition


        :param extended_field_definitions: The extended_field_definitions of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsSourceExtendedFieldDefinition]
        """
        self._extended_field_definitions = extended_field_definitions

    @property
    def is_for_cloud(self):
        """
        Gets the is_for_cloud of this LogAnalyticsSourceSummary.
        is for cloud flag


        :return: The is_for_cloud of this LogAnalyticsSourceSummary.
        :rtype: bool
        """
        return self._is_for_cloud

    @is_for_cloud.setter
    def is_for_cloud(self, is_for_cloud):
        """
        Sets the is_for_cloud of this LogAnalyticsSourceSummary.
        is for cloud flag


        :param is_for_cloud: The is_for_cloud of this LogAnalyticsSourceSummary.
        :type: bool
        """
        self._is_for_cloud = is_for_cloud

    @property
    def labels(self):
        """
        Gets the labels of this LogAnalyticsSourceSummary.
        labels


        :return: The labels of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsLabelView]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this LogAnalyticsSourceSummary.
        labels


        :param labels: The labels of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsLabelView]
        """
        self._labels = labels

    @property
    def metric_definitions(self):
        """
        Gets the metric_definitions of this LogAnalyticsSourceSummary.
        metric definitions


        :return: The metric_definitions of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsMetric]
        """
        return self._metric_definitions

    @metric_definitions.setter
    def metric_definitions(self, metric_definitions):
        """
        Sets the metric_definitions of this LogAnalyticsSourceSummary.
        metric definitions


        :param metric_definitions: The metric_definitions of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsMetric]
        """
        self._metric_definitions = metric_definitions

    @property
    def metrics(self):
        """
        Gets the metrics of this LogAnalyticsSourceSummary.
        metric source map


        :return: The metrics of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsSourceMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this LogAnalyticsSourceSummary.
        metric source map


        :param metrics: The metrics of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsSourceMetric]
        """
        self._metrics = metrics

    @property
    def oob_parsers(self):
        """
        Gets the oob_parsers of this LogAnalyticsSourceSummary.
        out-of-the-box source parser list


        :return: The oob_parsers of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsParser]
        """
        return self._oob_parsers

    @oob_parsers.setter
    def oob_parsers(self, oob_parsers):
        """
        Sets the oob_parsers of this LogAnalyticsSourceSummary.
        out-of-the-box source parser list


        :param oob_parsers: The oob_parsers of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsParser]
        """
        self._oob_parsers = oob_parsers

    @property
    def parameters(self):
        """
        Gets the parameters of this LogAnalyticsSourceSummary.
        parameters


        :return: The parameters of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this LogAnalyticsSourceSummary.
        parameters


        :param parameters: The parameters of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsParameter]
        """
        self._parameters = parameters

    @property
    def pattern_count(self):
        """
        Gets the pattern_count of this LogAnalyticsSourceSummary.
        pattern count


        :return: The pattern_count of this LogAnalyticsSourceSummary.
        :rtype: int
        """
        return self._pattern_count

    @pattern_count.setter
    def pattern_count(self, pattern_count):
        """
        Sets the pattern_count of this LogAnalyticsSourceSummary.
        pattern count


        :param pattern_count: The pattern_count of this LogAnalyticsSourceSummary.
        :type: int
        """
        self._pattern_count = pattern_count

    @property
    def patterns(self):
        """
        Gets the patterns of this LogAnalyticsSourceSummary.
        patterns


        :return: The patterns of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsSourcePattern]
        """
        return self._patterns

    @patterns.setter
    def patterns(self, patterns):
        """
        Sets the patterns of this LogAnalyticsSourceSummary.
        patterns


        :param patterns: The patterns of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsSourcePattern]
        """
        self._patterns = patterns

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsSourceSummary.
        description


        :return: The description of this LogAnalyticsSourceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsSourceSummary.
        description


        :param description: The description of this LogAnalyticsSourceSummary.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this LogAnalyticsSourceSummary.
        display name


        :return: The display_name of this LogAnalyticsSourceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsSourceSummary.
        display name


        :param display_name: The display_name of this LogAnalyticsSourceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def edit_version(self):
        """
        Gets the edit_version of this LogAnalyticsSourceSummary.
        source edit version


        :return: The edit_version of this LogAnalyticsSourceSummary.
        :rtype: int
        """
        return self._edit_version

    @edit_version.setter
    def edit_version(self, edit_version):
        """
        Sets the edit_version of this LogAnalyticsSourceSummary.
        source edit version


        :param edit_version: The edit_version of this LogAnalyticsSourceSummary.
        :type: int
        """
        self._edit_version = edit_version

    @property
    def functions(self):
        """
        Gets the functions of this LogAnalyticsSourceSummary.
        source functions


        :return: The functions of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsSourceFunction]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """
        Sets the functions of this LogAnalyticsSourceSummary.
        source functions


        :param functions: The functions of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsSourceFunction]
        """
        self._functions = functions

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsSourceSummary.
        source Id


        :return: The source_id of this LogAnalyticsSourceSummary.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsSourceSummary.
        source Id


        :param source_id: The source_id of this LogAnalyticsSourceSummary.
        :type: int
        """
        self._source_id = source_id

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsSourceSummary.
        source internal name


        :return: The name of this LogAnalyticsSourceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsSourceSummary.
        source internal name


        :param name: The name of this LogAnalyticsSourceSummary.
        :type: str
        """
        self._name = name

    @property
    def is_secure_content(self):
        """
        Gets the is_secure_content of this LogAnalyticsSourceSummary.
        is secure content flag


        :return: The is_secure_content of this LogAnalyticsSourceSummary.
        :rtype: bool
        """
        return self._is_secure_content

    @is_secure_content.setter
    def is_secure_content(self, is_secure_content):
        """
        Sets the is_secure_content of this LogAnalyticsSourceSummary.
        is secure content flag


        :param is_secure_content: The is_secure_content of this LogAnalyticsSourceSummary.
        :type: bool
        """
        self._is_secure_content = is_secure_content

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsSourceSummary.
        is system flag


        :return: The is_system of this LogAnalyticsSourceSummary.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsSourceSummary.
        is system flag


        :param is_system: The is_system of this LogAnalyticsSourceSummary.
        :type: bool
        """
        self._is_system = is_system

    @property
    def parsers(self):
        """
        Gets the parsers of this LogAnalyticsSourceSummary.
        parser list


        :return: The parsers of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsParser]
        """
        return self._parsers

    @parsers.setter
    def parsers(self, parsers):
        """
        Sets the parsers of this LogAnalyticsSourceSummary.
        parser list


        :param parsers: The parsers of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsParser]
        """
        self._parsers = parsers

    @property
    def is_auto_association_enabled(self):
        """
        Gets the is_auto_association_enabled of this LogAnalyticsSourceSummary.
        rule auto association enabled flag


        :return: The is_auto_association_enabled of this LogAnalyticsSourceSummary.
        :rtype: bool
        """
        return self._is_auto_association_enabled

    @is_auto_association_enabled.setter
    def is_auto_association_enabled(self, is_auto_association_enabled):
        """
        Sets the is_auto_association_enabled of this LogAnalyticsSourceSummary.
        rule auto association enabled flag


        :param is_auto_association_enabled: The is_auto_association_enabled of this LogAnalyticsSourceSummary.
        :type: bool
        """
        self._is_auto_association_enabled = is_auto_association_enabled

    @property
    def is_auto_association_override(self):
        """
        Gets the is_auto_association_override of this LogAnalyticsSourceSummary.
        rule auto association override


        :return: The is_auto_association_override of this LogAnalyticsSourceSummary.
        :rtype: bool
        """
        return self._is_auto_association_override

    @is_auto_association_override.setter
    def is_auto_association_override(self, is_auto_association_override):
        """
        Sets the is_auto_association_override of this LogAnalyticsSourceSummary.
        rule auto association override


        :param is_auto_association_override: The is_auto_association_override of this LogAnalyticsSourceSummary.
        :type: bool
        """
        self._is_auto_association_override = is_auto_association_override

    @property
    def rule_id(self):
        """
        Gets the rule_id of this LogAnalyticsSourceSummary.
        rule Id


        :return: The rule_id of this LogAnalyticsSourceSummary.
        :rtype: int
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """
        Sets the rule_id of this LogAnalyticsSourceSummary.
        rule Id


        :param rule_id: The rule_id of this LogAnalyticsSourceSummary.
        :type: int
        """
        self._rule_id = rule_id

    @property
    def type_name(self):
        """
        Gets the type_name of this LogAnalyticsSourceSummary.
        source type internal name


        :return: The type_name of this LogAnalyticsSourceSummary.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """
        Sets the type_name of this LogAnalyticsSourceSummary.
        source type internal name


        :param type_name: The type_name of this LogAnalyticsSourceSummary.
        :type: str
        """
        self._type_name = type_name

    @property
    def type_display_name(self):
        """
        Gets the type_display_name of this LogAnalyticsSourceSummary.
        source type name


        :return: The type_display_name of this LogAnalyticsSourceSummary.
        :rtype: str
        """
        return self._type_display_name

    @type_display_name.setter
    def type_display_name(self, type_display_name):
        """
        Sets the type_display_name of this LogAnalyticsSourceSummary.
        source type name


        :param type_display_name: The type_display_name of this LogAnalyticsSourceSummary.
        :type: str
        """
        self._type_display_name = type_display_name

    @property
    def warning_config(self):
        """
        Gets the warning_config of this LogAnalyticsSourceSummary.
        source warning configuration


        :return: The warning_config of this LogAnalyticsSourceSummary.
        :rtype: int
        """
        return self._warning_config

    @warning_config.setter
    def warning_config(self, warning_config):
        """
        Sets the warning_config of this LogAnalyticsSourceSummary.
        source warning configuration


        :param warning_config: The warning_config of this LogAnalyticsSourceSummary.
        :type: int
        """
        self._warning_config = warning_config

    @property
    def metadata_fields(self):
        """
        Gets the metadata_fields of this LogAnalyticsSourceSummary.
        source metadata fields


        :return: The metadata_fields of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsSourceMetadataField]
        """
        return self._metadata_fields

    @metadata_fields.setter
    def metadata_fields(self, metadata_fields):
        """
        Sets the metadata_fields of this LogAnalyticsSourceSummary.
        source metadata fields


        :param metadata_fields: The metadata_fields of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsSourceMetadataField]
        """
        self._metadata_fields = metadata_fields

    @property
    def label_definitions(self):
        """
        Gets the label_definitions of this LogAnalyticsSourceSummary.
        tags


        :return: The label_definitions of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsLabelDefinition]
        """
        return self._label_definitions

    @label_definitions.setter
    def label_definitions(self, label_definitions):
        """
        Sets the label_definitions of this LogAnalyticsSourceSummary.
        tags


        :param label_definitions: The label_definitions of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsLabelDefinition]
        """
        self._label_definitions = label_definitions

    @property
    def entity_types(self):
        """
        Gets the entity_types of this LogAnalyticsSourceSummary.
        Entity types


        :return: The entity_types of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsSourceEntityType]
        """
        return self._entity_types

    @entity_types.setter
    def entity_types(self, entity_types):
        """
        Sets the entity_types of this LogAnalyticsSourceSummary.
        Entity types


        :param entity_types: The entity_types of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsSourceEntityType]
        """
        self._entity_types = entity_types

    @property
    def is_timezone_override(self):
        """
        Gets the is_timezone_override of this LogAnalyticsSourceSummary.
        time zone override


        :return: The is_timezone_override of this LogAnalyticsSourceSummary.
        :rtype: bool
        """
        return self._is_timezone_override

    @is_timezone_override.setter
    def is_timezone_override(self, is_timezone_override):
        """
        Sets the is_timezone_override of this LogAnalyticsSourceSummary.
        time zone override


        :param is_timezone_override: The is_timezone_override of this LogAnalyticsSourceSummary.
        :type: bool
        """
        self._is_timezone_override = is_timezone_override

    @property
    def user_parsers(self):
        """
        Gets the user_parsers of this LogAnalyticsSourceSummary.
        source parser list


        :return: The user_parsers of this LogAnalyticsSourceSummary.
        :rtype: list[LogAnalyticsParser]
        """
        return self._user_parsers

    @user_parsers.setter
    def user_parsers(self, user_parsers):
        """
        Sets the user_parsers of this LogAnalyticsSourceSummary.
        source parser list


        :param user_parsers: The user_parsers of this LogAnalyticsSourceSummary.
        :type: list[LogAnalyticsParser]
        """
        self._user_parsers = user_parsers

    @property
    def time_updated(self):
        """
        Gets the time_updated of this LogAnalyticsSourceSummary.
        timeUpdated


        :return: The time_updated of this LogAnalyticsSourceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LogAnalyticsSourceSummary.
        timeUpdated


        :param time_updated: The time_updated of this LogAnalyticsSourceSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
