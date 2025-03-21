# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IncrementalReadConfig(object):
    """
    Config for incremental read operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IncrementalReadConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param last_extracted_field_date:
            The value to assign to the last_extracted_field_date property of this IncrementalReadConfig.
        :type last_extracted_field_date: list[oci.data_integration.models.IncrementalFieldClause]

        :param last_extracted_data_entity_date:
            The value to assign to the last_extracted_data_entity_date property of this IncrementalReadConfig.
        :type last_extracted_data_entity_date: list[oci.data_integration.models.IncrementalDataEntityClause]

        """
        self.swagger_types = {
            'last_extracted_field_date': 'list[IncrementalFieldClause]',
            'last_extracted_data_entity_date': 'list[IncrementalDataEntityClause]'
        }
        self.attribute_map = {
            'last_extracted_field_date': 'lastExtractedFieldDate',
            'last_extracted_data_entity_date': 'lastExtractedDataEntityDate'
        }
        self._last_extracted_field_date = None
        self._last_extracted_data_entity_date = None

    @property
    def last_extracted_field_date(self):
        """
        Gets the last_extracted_field_date of this IncrementalReadConfig.
        List of incremental field clauses.


        :return: The last_extracted_field_date of this IncrementalReadConfig.
        :rtype: list[oci.data_integration.models.IncrementalFieldClause]
        """
        return self._last_extracted_field_date

    @last_extracted_field_date.setter
    def last_extracted_field_date(self, last_extracted_field_date):
        """
        Sets the last_extracted_field_date of this IncrementalReadConfig.
        List of incremental field clauses.


        :param last_extracted_field_date: The last_extracted_field_date of this IncrementalReadConfig.
        :type: list[oci.data_integration.models.IncrementalFieldClause]
        """
        self._last_extracted_field_date = last_extracted_field_date

    @property
    def last_extracted_data_entity_date(self):
        """
        Gets the last_extracted_data_entity_date of this IncrementalReadConfig.
        List of incremental data entity clauses.


        :return: The last_extracted_data_entity_date of this IncrementalReadConfig.
        :rtype: list[oci.data_integration.models.IncrementalDataEntityClause]
        """
        return self._last_extracted_data_entity_date

    @last_extracted_data_entity_date.setter
    def last_extracted_data_entity_date(self, last_extracted_data_entity_date):
        """
        Sets the last_extracted_data_entity_date of this IncrementalReadConfig.
        List of incremental data entity clauses.


        :param last_extracted_data_entity_date: The last_extracted_data_entity_date of this IncrementalReadConfig.
        :type: list[oci.data_integration.models.IncrementalDataEntityClause]
        """
        self._last_extracted_data_entity_date = last_extracted_data_entity_date

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
