# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsImportCustomChangeList(object):
    """
    LogAnalyticsImportCustomChangeList
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsImportCustomChangeList object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param created_parser_names:
            The value to assign to the created_parser_names property of this LogAnalyticsImportCustomChangeList.
        :type created_parser_names: list[str]

        :param updated_parser_names:
            The value to assign to the updated_parser_names property of this LogAnalyticsImportCustomChangeList.
        :type updated_parser_names: list[str]

        :param created_source_names:
            The value to assign to the created_source_names property of this LogAnalyticsImportCustomChangeList.
        :type created_source_names: list[str]

        :param updated_source_names:
            The value to assign to the updated_source_names property of this LogAnalyticsImportCustomChangeList.
        :type updated_source_names: list[str]

        :param created_field_display_names:
            The value to assign to the created_field_display_names property of this LogAnalyticsImportCustomChangeList.
        :type created_field_display_names: list[str]

        :param updated_field_display_names:
            The value to assign to the updated_field_display_names property of this LogAnalyticsImportCustomChangeList.
        :type updated_field_display_names: list[str]

        :param conflict_parser_names:
            The value to assign to the conflict_parser_names property of this LogAnalyticsImportCustomChangeList.
        :type conflict_parser_names: list[str]

        :param conflict_source_names:
            The value to assign to the conflict_source_names property of this LogAnalyticsImportCustomChangeList.
        :type conflict_source_names: list[str]

        :param conflict_field_display_names:
            The value to assign to the conflict_field_display_names property of this LogAnalyticsImportCustomChangeList.
        :type conflict_field_display_names: list[str]

        """
        self.swagger_types = {
            'created_parser_names': 'list[str]',
            'updated_parser_names': 'list[str]',
            'created_source_names': 'list[str]',
            'updated_source_names': 'list[str]',
            'created_field_display_names': 'list[str]',
            'updated_field_display_names': 'list[str]',
            'conflict_parser_names': 'list[str]',
            'conflict_source_names': 'list[str]',
            'conflict_field_display_names': 'list[str]'
        }

        self.attribute_map = {
            'created_parser_names': 'createdParserNames',
            'updated_parser_names': 'updatedParserNames',
            'created_source_names': 'createdSourceNames',
            'updated_source_names': 'updatedSourceNames',
            'created_field_display_names': 'createdFieldDisplayNames',
            'updated_field_display_names': 'updatedFieldDisplayNames',
            'conflict_parser_names': 'conflictParserNames',
            'conflict_source_names': 'conflictSourceNames',
            'conflict_field_display_names': 'conflictFieldDisplayNames'
        }

        self._created_parser_names = None
        self._updated_parser_names = None
        self._created_source_names = None
        self._updated_source_names = None
        self._created_field_display_names = None
        self._updated_field_display_names = None
        self._conflict_parser_names = None
        self._conflict_source_names = None
        self._conflict_field_display_names = None

    @property
    def created_parser_names(self):
        """
        Gets the created_parser_names of this LogAnalyticsImportCustomChangeList.
        createdParserNames


        :return: The created_parser_names of this LogAnalyticsImportCustomChangeList.
        :rtype: list[str]
        """
        return self._created_parser_names

    @created_parser_names.setter
    def created_parser_names(self, created_parser_names):
        """
        Sets the created_parser_names of this LogAnalyticsImportCustomChangeList.
        createdParserNames


        :param created_parser_names: The created_parser_names of this LogAnalyticsImportCustomChangeList.
        :type: list[str]
        """
        self._created_parser_names = created_parser_names

    @property
    def updated_parser_names(self):
        """
        Gets the updated_parser_names of this LogAnalyticsImportCustomChangeList.
        updatedParserNames


        :return: The updated_parser_names of this LogAnalyticsImportCustomChangeList.
        :rtype: list[str]
        """
        return self._updated_parser_names

    @updated_parser_names.setter
    def updated_parser_names(self, updated_parser_names):
        """
        Sets the updated_parser_names of this LogAnalyticsImportCustomChangeList.
        updatedParserNames


        :param updated_parser_names: The updated_parser_names of this LogAnalyticsImportCustomChangeList.
        :type: list[str]
        """
        self._updated_parser_names = updated_parser_names

    @property
    def created_source_names(self):
        """
        Gets the created_source_names of this LogAnalyticsImportCustomChangeList.
        createdSourceNames


        :return: The created_source_names of this LogAnalyticsImportCustomChangeList.
        :rtype: list[str]
        """
        return self._created_source_names

    @created_source_names.setter
    def created_source_names(self, created_source_names):
        """
        Sets the created_source_names of this LogAnalyticsImportCustomChangeList.
        createdSourceNames


        :param created_source_names: The created_source_names of this LogAnalyticsImportCustomChangeList.
        :type: list[str]
        """
        self._created_source_names = created_source_names

    @property
    def updated_source_names(self):
        """
        Gets the updated_source_names of this LogAnalyticsImportCustomChangeList.
        updatedSourceNames


        :return: The updated_source_names of this LogAnalyticsImportCustomChangeList.
        :rtype: list[str]
        """
        return self._updated_source_names

    @updated_source_names.setter
    def updated_source_names(self, updated_source_names):
        """
        Sets the updated_source_names of this LogAnalyticsImportCustomChangeList.
        updatedSourceNames


        :param updated_source_names: The updated_source_names of this LogAnalyticsImportCustomChangeList.
        :type: list[str]
        """
        self._updated_source_names = updated_source_names

    @property
    def created_field_display_names(self):
        """
        Gets the created_field_display_names of this LogAnalyticsImportCustomChangeList.
        createdFieldDisplayNames


        :return: The created_field_display_names of this LogAnalyticsImportCustomChangeList.
        :rtype: list[str]
        """
        return self._created_field_display_names

    @created_field_display_names.setter
    def created_field_display_names(self, created_field_display_names):
        """
        Sets the created_field_display_names of this LogAnalyticsImportCustomChangeList.
        createdFieldDisplayNames


        :param created_field_display_names: The created_field_display_names of this LogAnalyticsImportCustomChangeList.
        :type: list[str]
        """
        self._created_field_display_names = created_field_display_names

    @property
    def updated_field_display_names(self):
        """
        Gets the updated_field_display_names of this LogAnalyticsImportCustomChangeList.
        updatedFieldDisplayNames


        :return: The updated_field_display_names of this LogAnalyticsImportCustomChangeList.
        :rtype: list[str]
        """
        return self._updated_field_display_names

    @updated_field_display_names.setter
    def updated_field_display_names(self, updated_field_display_names):
        """
        Sets the updated_field_display_names of this LogAnalyticsImportCustomChangeList.
        updatedFieldDisplayNames


        :param updated_field_display_names: The updated_field_display_names of this LogAnalyticsImportCustomChangeList.
        :type: list[str]
        """
        self._updated_field_display_names = updated_field_display_names

    @property
    def conflict_parser_names(self):
        """
        Gets the conflict_parser_names of this LogAnalyticsImportCustomChangeList.
        conflictParserNames


        :return: The conflict_parser_names of this LogAnalyticsImportCustomChangeList.
        :rtype: list[str]
        """
        return self._conflict_parser_names

    @conflict_parser_names.setter
    def conflict_parser_names(self, conflict_parser_names):
        """
        Sets the conflict_parser_names of this LogAnalyticsImportCustomChangeList.
        conflictParserNames


        :param conflict_parser_names: The conflict_parser_names of this LogAnalyticsImportCustomChangeList.
        :type: list[str]
        """
        self._conflict_parser_names = conflict_parser_names

    @property
    def conflict_source_names(self):
        """
        Gets the conflict_source_names of this LogAnalyticsImportCustomChangeList.
        conflictSourceNames


        :return: The conflict_source_names of this LogAnalyticsImportCustomChangeList.
        :rtype: list[str]
        """
        return self._conflict_source_names

    @conflict_source_names.setter
    def conflict_source_names(self, conflict_source_names):
        """
        Sets the conflict_source_names of this LogAnalyticsImportCustomChangeList.
        conflictSourceNames


        :param conflict_source_names: The conflict_source_names of this LogAnalyticsImportCustomChangeList.
        :type: list[str]
        """
        self._conflict_source_names = conflict_source_names

    @property
    def conflict_field_display_names(self):
        """
        Gets the conflict_field_display_names of this LogAnalyticsImportCustomChangeList.
        conflictFieldDisplayNames


        :return: The conflict_field_display_names of this LogAnalyticsImportCustomChangeList.
        :rtype: list[str]
        """
        return self._conflict_field_display_names

    @conflict_field_display_names.setter
    def conflict_field_display_names(self, conflict_field_display_names):
        """
        Sets the conflict_field_display_names of this LogAnalyticsImportCustomChangeList.
        conflictFieldDisplayNames


        :param conflict_field_display_names: The conflict_field_display_names of this LogAnalyticsImportCustomChangeList.
        :type: list[str]
        """
        self._conflict_field_display_names = conflict_field_display_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
