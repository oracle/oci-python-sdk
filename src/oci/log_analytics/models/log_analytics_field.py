# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsField(object):
    """
    Field Details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsField object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cee_alias:
            The value to assign to the cee_alias property of this LogAnalyticsField.
        :type cee_alias: str

        :param data_type:
            The value to assign to the data_type property of this LogAnalyticsField.
        :type data_type: str

        :param regular_expression:
            The value to assign to the regular_expression property of this LogAnalyticsField.
        :type regular_expression: str

        :param description:
            The value to assign to the description property of this LogAnalyticsField.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsField.
        :type display_name: str

        :param edit_version:
            The value to assign to the edit_version property of this LogAnalyticsField.
        :type edit_version: int

        :param facet_priority:
            The value to assign to the facet_priority property of this LogAnalyticsField.
        :type facet_priority: int

        :param name:
            The value to assign to the name property of this LogAnalyticsField.
        :type name: str

        :param is_facet_eligible:
            The value to assign to the is_facet_eligible property of this LogAnalyticsField.
        :type is_facet_eligible: bool

        :param is_high_cardinality:
            The value to assign to the is_high_cardinality property of this LogAnalyticsField.
        :type is_high_cardinality: bool

        :param is_large_data:
            The value to assign to the is_large_data property of this LogAnalyticsField.
        :type is_large_data: bool

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this LogAnalyticsField.
        :type is_multi_valued: bool

        :param is_primary:
            The value to assign to the is_primary property of this LogAnalyticsField.
        :type is_primary: bool

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsField.
        :type is_system: bool

        :param is_summarizable:
            The value to assign to the is_summarizable property of this LogAnalyticsField.
        :type is_summarizable: bool

        :param mapped_value:
            The value to assign to the mapped_value property of this LogAnalyticsField.
        :type mapped_value: str

        :param is_metric_key_eligible:
            The value to assign to the is_metric_key_eligible property of this LogAnalyticsField.
        :type is_metric_key_eligible: bool

        :param is_metric_value_eligible:
            The value to assign to the is_metric_value_eligible property of this LogAnalyticsField.
        :type is_metric_value_eligible: bool

        :param range_facet_eligible:
            The value to assign to the range_facet_eligible property of this LogAnalyticsField.
        :type range_facet_eligible: int

        :param is_table_eligible:
            The value to assign to the is_table_eligible property of this LogAnalyticsField.
        :type is_table_eligible: bool

        :param unit_type:
            The value to assign to the unit_type property of this LogAnalyticsField.
        :type unit_type: str

        """
        self.swagger_types = {
            'cee_alias': 'str',
            'data_type': 'str',
            'regular_expression': 'str',
            'description': 'str',
            'display_name': 'str',
            'edit_version': 'int',
            'facet_priority': 'int',
            'name': 'str',
            'is_facet_eligible': 'bool',
            'is_high_cardinality': 'bool',
            'is_large_data': 'bool',
            'is_multi_valued': 'bool',
            'is_primary': 'bool',
            'is_system': 'bool',
            'is_summarizable': 'bool',
            'mapped_value': 'str',
            'is_metric_key_eligible': 'bool',
            'is_metric_value_eligible': 'bool',
            'range_facet_eligible': 'int',
            'is_table_eligible': 'bool',
            'unit_type': 'str'
        }

        self.attribute_map = {
            'cee_alias': 'ceeAlias',
            'data_type': 'dataType',
            'regular_expression': 'regularExpression',
            'description': 'description',
            'display_name': 'displayName',
            'edit_version': 'editVersion',
            'facet_priority': 'facetPriority',
            'name': 'name',
            'is_facet_eligible': 'isFacetEligible',
            'is_high_cardinality': 'isHighCardinality',
            'is_large_data': 'isLargeData',
            'is_multi_valued': 'isMultiValued',
            'is_primary': 'isPrimary',
            'is_system': 'isSystem',
            'is_summarizable': 'isSummarizable',
            'mapped_value': 'mappedValue',
            'is_metric_key_eligible': 'isMetricKeyEligible',
            'is_metric_value_eligible': 'isMetricValueEligible',
            'range_facet_eligible': 'rangeFacetEligible',
            'is_table_eligible': 'isTableEligible',
            'unit_type': 'unitType'
        }

        self._cee_alias = None
        self._data_type = None
        self._regular_expression = None
        self._description = None
        self._display_name = None
        self._edit_version = None
        self._facet_priority = None
        self._name = None
        self._is_facet_eligible = None
        self._is_high_cardinality = None
        self._is_large_data = None
        self._is_multi_valued = None
        self._is_primary = None
        self._is_system = None
        self._is_summarizable = None
        self._mapped_value = None
        self._is_metric_key_eligible = None
        self._is_metric_value_eligible = None
        self._range_facet_eligible = None
        self._is_table_eligible = None
        self._unit_type = None

    @property
    def cee_alias(self):
        """
        Gets the cee_alias of this LogAnalyticsField.
        The name this field is given in the common event expression standard from mitre.org.
        This is used for reference when exporting content conforming to CEE standard


        :return: The cee_alias of this LogAnalyticsField.
        :rtype: str
        """
        return self._cee_alias

    @cee_alias.setter
    def cee_alias(self, cee_alias):
        """
        Sets the cee_alias of this LogAnalyticsField.
        The name this field is given in the common event expression standard from mitre.org.
        This is used for reference when exporting content conforming to CEE standard


        :param cee_alias: The cee_alias of this LogAnalyticsField.
        :type: str
        """
        self._cee_alias = cee_alias

    @property
    def data_type(self):
        """
        Gets the data_type of this LogAnalyticsField.
        The field data type.


        :return: The data_type of this LogAnalyticsField.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this LogAnalyticsField.
        The field data type.


        :param data_type: The data_type of this LogAnalyticsField.
        :type: str
        """
        self._data_type = data_type

    @property
    def regular_expression(self):
        """
        Gets the regular_expression of this LogAnalyticsField.
        The field default regular expression.


        :return: The regular_expression of this LogAnalyticsField.
        :rtype: str
        """
        return self._regular_expression

    @regular_expression.setter
    def regular_expression(self, regular_expression):
        """
        Sets the regular_expression of this LogAnalyticsField.
        The field default regular expression.


        :param regular_expression: The regular_expression of this LogAnalyticsField.
        :type: str
        """
        self._regular_expression = regular_expression

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsField.
        The field description.


        :return: The description of this LogAnalyticsField.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsField.
        The field description.


        :param description: The description of this LogAnalyticsField.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this LogAnalyticsField.
        The field display name.


        :return: The display_name of this LogAnalyticsField.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsField.
        The field display name.


        :param display_name: The display_name of this LogAnalyticsField.
        :type: str
        """
        self._display_name = display_name

    @property
    def edit_version(self):
        """
        Gets the edit_version of this LogAnalyticsField.
        The field edit version.


        :return: The edit_version of this LogAnalyticsField.
        :rtype: int
        """
        return self._edit_version

    @edit_version.setter
    def edit_version(self, edit_version):
        """
        Sets the edit_version of this LogAnalyticsField.
        The field edit version.


        :param edit_version: The edit_version of this LogAnalyticsField.
        :type: int
        """
        self._edit_version = edit_version

    @property
    def facet_priority(self):
        """
        Gets the facet_priority of this LogAnalyticsField.
        The facet priority.


        :return: The facet_priority of this LogAnalyticsField.
        :rtype: int
        """
        return self._facet_priority

    @facet_priority.setter
    def facet_priority(self, facet_priority):
        """
        Sets the facet_priority of this LogAnalyticsField.
        The facet priority.


        :param facet_priority: The facet_priority of this LogAnalyticsField.
        :type: int
        """
        self._facet_priority = facet_priority

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsField.
        The field internal name.


        :return: The name of this LogAnalyticsField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsField.
        The field internal name.


        :param name: The name of this LogAnalyticsField.
        :type: str
        """
        self._name = name

    @property
    def is_facet_eligible(self):
        """
        Gets the is_facet_eligible of this LogAnalyticsField.
        A flag inidcating whether or not the facet is elibigle for use.


        :return: The is_facet_eligible of this LogAnalyticsField.
        :rtype: bool
        """
        return self._is_facet_eligible

    @is_facet_eligible.setter
    def is_facet_eligible(self, is_facet_eligible):
        """
        Sets the is_facet_eligible of this LogAnalyticsField.
        A flag inidcating whether or not the facet is elibigle for use.


        :param is_facet_eligible: The is_facet_eligible of this LogAnalyticsField.
        :type: bool
        """
        self._is_facet_eligible = is_facet_eligible

    @property
    def is_high_cardinality(self):
        """
        Gets the is_high_cardinality of this LogAnalyticsField.
        A flag inidcating whether or not the cardinality of the field is high.


        :return: The is_high_cardinality of this LogAnalyticsField.
        :rtype: bool
        """
        return self._is_high_cardinality

    @is_high_cardinality.setter
    def is_high_cardinality(self, is_high_cardinality):
        """
        Sets the is_high_cardinality of this LogAnalyticsField.
        A flag inidcating whether or not the cardinality of the field is high.


        :param is_high_cardinality: The is_high_cardinality of this LogAnalyticsField.
        :type: bool
        """
        self._is_high_cardinality = is_high_cardinality

    @property
    def is_large_data(self):
        """
        Gets the is_large_data of this LogAnalyticsField.
        A flag inidcating whether or not the field is a large data field.


        :return: The is_large_data of this LogAnalyticsField.
        :rtype: bool
        """
        return self._is_large_data

    @is_large_data.setter
    def is_large_data(self, is_large_data):
        """
        Sets the is_large_data of this LogAnalyticsField.
        A flag inidcating whether or not the field is a large data field.


        :param is_large_data: The is_large_data of this LogAnalyticsField.
        :type: bool
        """
        self._is_large_data = is_large_data

    @property
    def is_multi_valued(self):
        """
        Gets the is_multi_valued of this LogAnalyticsField.
        A flag indicating whether or not the field is multi-valued.


        :return: The is_multi_valued of this LogAnalyticsField.
        :rtype: bool
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued):
        """
        Sets the is_multi_valued of this LogAnalyticsField.
        A flag indicating whether or not the field is multi-valued.


        :param is_multi_valued: The is_multi_valued of this LogAnalyticsField.
        :type: bool
        """
        self._is_multi_valued = is_multi_valued

    @property
    def is_primary(self):
        """
        Gets the is_primary of this LogAnalyticsField.
        A flag inidcating whether or not this is a primary field.


        :return: The is_primary of this LogAnalyticsField.
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """
        Sets the is_primary of this LogAnalyticsField.
        A flag inidcating whether or not this is a primary field.


        :param is_primary: The is_primary of this LogAnalyticsField.
        :type: bool
        """
        self._is_primary = is_primary

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsField.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :return: The is_system of this LogAnalyticsField.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsField.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :param is_system: The is_system of this LogAnalyticsField.
        :type: bool
        """
        self._is_system = is_system

    @property
    def is_summarizable(self):
        """
        Gets the is_summarizable of this LogAnalyticsField.
        A flag inidcating whether or not the field can be summarized.


        :return: The is_summarizable of this LogAnalyticsField.
        :rtype: bool
        """
        return self._is_summarizable

    @is_summarizable.setter
    def is_summarizable(self, is_summarizable):
        """
        Sets the is_summarizable of this LogAnalyticsField.
        A flag inidcating whether or not the field can be summarized.


        :param is_summarizable: The is_summarizable of this LogAnalyticsField.
        :type: bool
        """
        self._is_summarizable = is_summarizable

    @property
    def mapped_value(self):
        """
        Gets the mapped_value of this LogAnalyticsField.
        The mapped value.


        :return: The mapped_value of this LogAnalyticsField.
        :rtype: str
        """
        return self._mapped_value

    @mapped_value.setter
    def mapped_value(self, mapped_value):
        """
        Sets the mapped_value of this LogAnalyticsField.
        The mapped value.


        :param mapped_value: The mapped_value of this LogAnalyticsField.
        :type: str
        """
        self._mapped_value = mapped_value

    @property
    def is_metric_key_eligible(self):
        """
        Gets the is_metric_key_eligible of this LogAnalyticsField.
        A flag inidcating whether or not the field is metric key eligible.


        :return: The is_metric_key_eligible of this LogAnalyticsField.
        :rtype: bool
        """
        return self._is_metric_key_eligible

    @is_metric_key_eligible.setter
    def is_metric_key_eligible(self, is_metric_key_eligible):
        """
        Sets the is_metric_key_eligible of this LogAnalyticsField.
        A flag inidcating whether or not the field is metric key eligible.


        :param is_metric_key_eligible: The is_metric_key_eligible of this LogAnalyticsField.
        :type: bool
        """
        self._is_metric_key_eligible = is_metric_key_eligible

    @property
    def is_metric_value_eligible(self):
        """
        Gets the is_metric_value_eligible of this LogAnalyticsField.
        A flag inidcating whether or not the field is metric value eligible.


        :return: The is_metric_value_eligible of this LogAnalyticsField.
        :rtype: bool
        """
        return self._is_metric_value_eligible

    @is_metric_value_eligible.setter
    def is_metric_value_eligible(self, is_metric_value_eligible):
        """
        Sets the is_metric_value_eligible of this LogAnalyticsField.
        A flag inidcating whether or not the field is metric value eligible.


        :param is_metric_value_eligible: The is_metric_value_eligible of this LogAnalyticsField.
        :type: bool
        """
        self._is_metric_value_eligible = is_metric_value_eligible

    @property
    def range_facet_eligible(self):
        """
        Gets the range_facet_eligible of this LogAnalyticsField.
        A flag inidcating whether or not the field is range facet eligible.


        :return: The range_facet_eligible of this LogAnalyticsField.
        :rtype: int
        """
        return self._range_facet_eligible

    @range_facet_eligible.setter
    def range_facet_eligible(self, range_facet_eligible):
        """
        Sets the range_facet_eligible of this LogAnalyticsField.
        A flag inidcating whether or not the field is range facet eligible.


        :param range_facet_eligible: The range_facet_eligible of this LogAnalyticsField.
        :type: int
        """
        self._range_facet_eligible = range_facet_eligible

    @property
    def is_table_eligible(self):
        """
        Gets the is_table_eligible of this LogAnalyticsField.
        A flag inidcating whether or not the field is table eligible.


        :return: The is_table_eligible of this LogAnalyticsField.
        :rtype: bool
        """
        return self._is_table_eligible

    @is_table_eligible.setter
    def is_table_eligible(self, is_table_eligible):
        """
        Sets the is_table_eligible of this LogAnalyticsField.
        A flag inidcating whether or not the field is table eligible.


        :param is_table_eligible: The is_table_eligible of this LogAnalyticsField.
        :type: bool
        """
        self._is_table_eligible = is_table_eligible

    @property
    def unit_type(self):
        """
        Gets the unit_type of this LogAnalyticsField.
        The field unit type.


        :return: The unit_type of this LogAnalyticsField.
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """
        Sets the unit_type of this LogAnalyticsField.
        The field unit type.


        :param unit_type: The unit_type of this LogAnalyticsField.
        :type: str
        """
        self._unit_type = unit_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
