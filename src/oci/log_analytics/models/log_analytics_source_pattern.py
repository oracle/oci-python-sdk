# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsSourcePattern(object):
    """
    LogAnalyticsSourcePattern
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsSourcePattern object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param converted_text:
            The value to assign to the converted_text property of this LogAnalyticsSourcePattern.
        :type converted_text: str

        :param db_parser_id:
            The value to assign to the db_parser_id property of this LogAnalyticsSourcePattern.
        :type db_parser_id: int

        :param db_pattern_date_time_columns:
            The value to assign to the db_pattern_date_time_columns property of this LogAnalyticsSourcePattern.
        :type db_pattern_date_time_columns: str

        :param db_pattern_date_time_field:
            The value to assign to the db_pattern_date_time_field property of this LogAnalyticsSourcePattern.
        :type db_pattern_date_time_field: str

        :param db_pattern_sequence_column:
            The value to assign to the db_pattern_sequence_column property of this LogAnalyticsSourcePattern.
        :type db_pattern_sequence_column: str

        :param fields:
            The value to assign to the fields property of this LogAnalyticsSourcePattern.
        :type fields: list[LogAnalyticsParserField]

        :param is_include:
            The value to assign to the is_include property of this LogAnalyticsSourcePattern.
        :type is_include: bool

        :param is_default:
            The value to assign to the is_default property of this LogAnalyticsSourcePattern.
        :type is_default: bool

        :param pattern_filter:
            The value to assign to the pattern_filter property of this LogAnalyticsSourcePattern.
        :type pattern_filter: LogAnalyticsPatternFilter

        :param alias:
            The value to assign to the alias property of this LogAnalyticsSourcePattern.
        :type alias: str

        :param description:
            The value to assign to the description property of this LogAnalyticsSourcePattern.
        :type description: str

        :param is_enabled:
            The value to assign to the is_enabled property of this LogAnalyticsSourcePattern.
        :type is_enabled: bool

        :param pattern_id:
            The value to assign to the pattern_id property of this LogAnalyticsSourcePattern.
        :type pattern_id: int

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsSourcePattern.
        :type is_system: bool

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsSourcePattern.
        :type source_id: int

        :param is_agent_warning_suppressed:
            The value to assign to the is_agent_warning_suppressed property of this LogAnalyticsSourcePattern.
        :type is_agent_warning_suppressed: bool

        :param pattern_text:
            The value to assign to the pattern_text property of this LogAnalyticsSourcePattern.
        :type pattern_text: str

        :param pattern_type:
            The value to assign to the pattern_type property of this LogAnalyticsSourcePattern.
        :type pattern_type: int

        :param entity_type:
            The value to assign to the entity_type property of this LogAnalyticsSourcePattern.
        :type entity_type: list[str]

        """
        self.swagger_types = {
            'converted_text': 'str',
            'db_parser_id': 'int',
            'db_pattern_date_time_columns': 'str',
            'db_pattern_date_time_field': 'str',
            'db_pattern_sequence_column': 'str',
            'fields': 'list[LogAnalyticsParserField]',
            'is_include': 'bool',
            'is_default': 'bool',
            'pattern_filter': 'LogAnalyticsPatternFilter',
            'alias': 'str',
            'description': 'str',
            'is_enabled': 'bool',
            'pattern_id': 'int',
            'is_system': 'bool',
            'source_id': 'int',
            'is_agent_warning_suppressed': 'bool',
            'pattern_text': 'str',
            'pattern_type': 'int',
            'entity_type': 'list[str]'
        }

        self.attribute_map = {
            'converted_text': 'convertedText',
            'db_parser_id': 'dbParserId',
            'db_pattern_date_time_columns': 'dbPatternDateTimeColumns',
            'db_pattern_date_time_field': 'dbPatternDateTimeField',
            'db_pattern_sequence_column': 'dbPatternSequenceColumn',
            'fields': 'fields',
            'is_include': 'isInclude',
            'is_default': 'isDefault',
            'pattern_filter': 'patternFilter',
            'alias': 'alias',
            'description': 'description',
            'is_enabled': 'isEnabled',
            'pattern_id': 'patternId',
            'is_system': 'isSystem',
            'source_id': 'sourceId',
            'is_agent_warning_suppressed': 'isAgentWarningSuppressed',
            'pattern_text': 'patternText',
            'pattern_type': 'patternType',
            'entity_type': 'entityType'
        }

        self._converted_text = None
        self._db_parser_id = None
        self._db_pattern_date_time_columns = None
        self._db_pattern_date_time_field = None
        self._db_pattern_sequence_column = None
        self._fields = None
        self._is_include = None
        self._is_default = None
        self._pattern_filter = None
        self._alias = None
        self._description = None
        self._is_enabled = None
        self._pattern_id = None
        self._is_system = None
        self._source_id = None
        self._is_agent_warning_suppressed = None
        self._pattern_text = None
        self._pattern_type = None
        self._entity_type = None

    @property
    def converted_text(self):
        """
        Gets the converted_text of this LogAnalyticsSourcePattern.
        converted text


        :return: The converted_text of this LogAnalyticsSourcePattern.
        :rtype: str
        """
        return self._converted_text

    @converted_text.setter
    def converted_text(self, converted_text):
        """
        Sets the converted_text of this LogAnalyticsSourcePattern.
        converted text


        :param converted_text: The converted_text of this LogAnalyticsSourcePattern.
        :type: str
        """
        self._converted_text = converted_text

    @property
    def db_parser_id(self):
        """
        Gets the db_parser_id of this LogAnalyticsSourcePattern.
        parser Id


        :return: The db_parser_id of this LogAnalyticsSourcePattern.
        :rtype: int
        """
        return self._db_parser_id

    @db_parser_id.setter
    def db_parser_id(self, db_parser_id):
        """
        Sets the db_parser_id of this LogAnalyticsSourcePattern.
        parser Id


        :param db_parser_id: The db_parser_id of this LogAnalyticsSourcePattern.
        :type: int
        """
        self._db_parser_id = db_parser_id

    @property
    def db_pattern_date_time_columns(self):
        """
        Gets the db_pattern_date_time_columns of this LogAnalyticsSourcePattern.
        date time columns


        :return: The db_pattern_date_time_columns of this LogAnalyticsSourcePattern.
        :rtype: str
        """
        return self._db_pattern_date_time_columns

    @db_pattern_date_time_columns.setter
    def db_pattern_date_time_columns(self, db_pattern_date_time_columns):
        """
        Sets the db_pattern_date_time_columns of this LogAnalyticsSourcePattern.
        date time columns


        :param db_pattern_date_time_columns: The db_pattern_date_time_columns of this LogAnalyticsSourcePattern.
        :type: str
        """
        self._db_pattern_date_time_columns = db_pattern_date_time_columns

    @property
    def db_pattern_date_time_field(self):
        """
        Gets the db_pattern_date_time_field of this LogAnalyticsSourcePattern.
        date time field


        :return: The db_pattern_date_time_field of this LogAnalyticsSourcePattern.
        :rtype: str
        """
        return self._db_pattern_date_time_field

    @db_pattern_date_time_field.setter
    def db_pattern_date_time_field(self, db_pattern_date_time_field):
        """
        Sets the db_pattern_date_time_field of this LogAnalyticsSourcePattern.
        date time field


        :param db_pattern_date_time_field: The db_pattern_date_time_field of this LogAnalyticsSourcePattern.
        :type: str
        """
        self._db_pattern_date_time_field = db_pattern_date_time_field

    @property
    def db_pattern_sequence_column(self):
        """
        Gets the db_pattern_sequence_column of this LogAnalyticsSourcePattern.
        sequence column


        :return: The db_pattern_sequence_column of this LogAnalyticsSourcePattern.
        :rtype: str
        """
        return self._db_pattern_sequence_column

    @db_pattern_sequence_column.setter
    def db_pattern_sequence_column(self, db_pattern_sequence_column):
        """
        Sets the db_pattern_sequence_column of this LogAnalyticsSourcePattern.
        sequence column


        :param db_pattern_sequence_column: The db_pattern_sequence_column of this LogAnalyticsSourcePattern.
        :type: str
        """
        self._db_pattern_sequence_column = db_pattern_sequence_column

    @property
    def fields(self):
        """
        Gets the fields of this LogAnalyticsSourcePattern.
        field list


        :return: The fields of this LogAnalyticsSourcePattern.
        :rtype: list[LogAnalyticsParserField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this LogAnalyticsSourcePattern.
        field list


        :param fields: The fields of this LogAnalyticsSourcePattern.
        :type: list[LogAnalyticsParserField]
        """
        self._fields = fields

    @property
    def is_include(self):
        """
        Gets the is_include of this LogAnalyticsSourcePattern.
        is include flag


        :return: The is_include of this LogAnalyticsSourcePattern.
        :rtype: bool
        """
        return self._is_include

    @is_include.setter
    def is_include(self, is_include):
        """
        Sets the is_include of this LogAnalyticsSourcePattern.
        is include flag


        :param is_include: The is_include of this LogAnalyticsSourcePattern.
        :type: bool
        """
        self._is_include = is_include

    @property
    def is_default(self):
        """
        Gets the is_default of this LogAnalyticsSourcePattern.
        is default flag


        :return: The is_default of this LogAnalyticsSourcePattern.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this LogAnalyticsSourcePattern.
        is default flag


        :param is_default: The is_default of this LogAnalyticsSourcePattern.
        :type: bool
        """
        self._is_default = is_default

    @property
    def pattern_filter(self):
        """
        Gets the pattern_filter of this LogAnalyticsSourcePattern.

        :return: The pattern_filter of this LogAnalyticsSourcePattern.
        :rtype: LogAnalyticsPatternFilter
        """
        return self._pattern_filter

    @pattern_filter.setter
    def pattern_filter(self, pattern_filter):
        """
        Sets the pattern_filter of this LogAnalyticsSourcePattern.

        :param pattern_filter: The pattern_filter of this LogAnalyticsSourcePattern.
        :type: LogAnalyticsPatternFilter
        """
        self._pattern_filter = pattern_filter

    @property
    def alias(self):
        """
        Gets the alias of this LogAnalyticsSourcePattern.
        alias


        :return: The alias of this LogAnalyticsSourcePattern.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this LogAnalyticsSourcePattern.
        alias


        :param alias: The alias of this LogAnalyticsSourcePattern.
        :type: str
        """
        self._alias = alias

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsSourcePattern.
        description


        :return: The description of this LogAnalyticsSourcePattern.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsSourcePattern.
        description


        :param description: The description of this LogAnalyticsSourcePattern.
        :type: str
        """
        self._description = description

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this LogAnalyticsSourcePattern.
        is enabled flag


        :return: The is_enabled of this LogAnalyticsSourcePattern.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this LogAnalyticsSourcePattern.
        is enabled flag


        :param is_enabled: The is_enabled of this LogAnalyticsSourcePattern.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def pattern_id(self):
        """
        Gets the pattern_id of this LogAnalyticsSourcePattern.
        pattern Id


        :return: The pattern_id of this LogAnalyticsSourcePattern.
        :rtype: int
        """
        return self._pattern_id

    @pattern_id.setter
    def pattern_id(self, pattern_id):
        """
        Sets the pattern_id of this LogAnalyticsSourcePattern.
        pattern Id


        :param pattern_id: The pattern_id of this LogAnalyticsSourcePattern.
        :type: int
        """
        self._pattern_id = pattern_id

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsSourcePattern.
        is system flag


        :return: The is_system of this LogAnalyticsSourcePattern.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsSourcePattern.
        is system flag


        :param is_system: The is_system of this LogAnalyticsSourcePattern.
        :type: bool
        """
        self._is_system = is_system

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsSourcePattern.
        source Id


        :return: The source_id of this LogAnalyticsSourcePattern.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsSourcePattern.
        source Id


        :param source_id: The source_id of this LogAnalyticsSourcePattern.
        :type: int
        """
        self._source_id = source_id

    @property
    def is_agent_warning_suppressed(self):
        """
        Gets the is_agent_warning_suppressed of this LogAnalyticsSourcePattern.
        suppress agent warning


        :return: The is_agent_warning_suppressed of this LogAnalyticsSourcePattern.
        :rtype: bool
        """
        return self._is_agent_warning_suppressed

    @is_agent_warning_suppressed.setter
    def is_agent_warning_suppressed(self, is_agent_warning_suppressed):
        """
        Sets the is_agent_warning_suppressed of this LogAnalyticsSourcePattern.
        suppress agent warning


        :param is_agent_warning_suppressed: The is_agent_warning_suppressed of this LogAnalyticsSourcePattern.
        :type: bool
        """
        self._is_agent_warning_suppressed = is_agent_warning_suppressed

    @property
    def pattern_text(self):
        """
        Gets the pattern_text of this LogAnalyticsSourcePattern.
        pattern text


        :return: The pattern_text of this LogAnalyticsSourcePattern.
        :rtype: str
        """
        return self._pattern_text

    @pattern_text.setter
    def pattern_text(self, pattern_text):
        """
        Sets the pattern_text of this LogAnalyticsSourcePattern.
        pattern text


        :param pattern_text: The pattern_text of this LogAnalyticsSourcePattern.
        :type: str
        """
        self._pattern_text = pattern_text

    @property
    def pattern_type(self):
        """
        Gets the pattern_type of this LogAnalyticsSourcePattern.
        pattern type


        :return: The pattern_type of this LogAnalyticsSourcePattern.
        :rtype: int
        """
        return self._pattern_type

    @pattern_type.setter
    def pattern_type(self, pattern_type):
        """
        Sets the pattern_type of this LogAnalyticsSourcePattern.
        pattern type


        :param pattern_type: The pattern_type of this LogAnalyticsSourcePattern.
        :type: int
        """
        self._pattern_type = pattern_type

    @property
    def entity_type(self):
        """
        Gets the entity_type of this LogAnalyticsSourcePattern.
        source entity types


        :return: The entity_type of this LogAnalyticsSourcePattern.
        :rtype: list[str]
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this LogAnalyticsSourcePattern.
        source entity types


        :param entity_type: The entity_type of this LogAnalyticsSourcePattern.
        :type: list[str]
        """
        self._entity_type = entity_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
