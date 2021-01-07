# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LabelSourceSummary(object):
    """
    source summary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LabelSourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_display_name:
            The value to assign to the source_display_name property of this LabelSourceSummary.
        :type source_display_name: str

        :param source_name:
            The value to assign to the source_name property of this LabelSourceSummary.
        :type source_name: str

        :param source_id:
            The value to assign to the source_id property of this LabelSourceSummary.
        :type source_id: int

        :param label_operator_name:
            The value to assign to the label_operator_name property of this LabelSourceSummary.
        :type label_operator_name: str

        :param label_condition:
            The value to assign to the label_condition property of this LabelSourceSummary.
        :type label_condition: str

        :param label_field_displayname:
            The value to assign to the label_field_displayname property of this LabelSourceSummary.
        :type label_field_displayname: str

        :param label_field_name:
            The value to assign to the label_field_name property of this LabelSourceSummary.
        :type label_field_name: str

        """
        self.swagger_types = {
            'source_display_name': 'str',
            'source_name': 'str',
            'source_id': 'int',
            'label_operator_name': 'str',
            'label_condition': 'str',
            'label_field_displayname': 'str',
            'label_field_name': 'str'
        }

        self.attribute_map = {
            'source_display_name': 'sourceDisplayName',
            'source_name': 'sourceName',
            'source_id': 'sourceId',
            'label_operator_name': 'labelOperatorName',
            'label_condition': 'labelCondition',
            'label_field_displayname': 'labelFieldDisplayname',
            'label_field_name': 'labelFieldName'
        }

        self._source_display_name = None
        self._source_name = None
        self._source_id = None
        self._label_operator_name = None
        self._label_condition = None
        self._label_field_displayname = None
        self._label_field_name = None

    @property
    def source_display_name(self):
        """
        Gets the source_display_name of this LabelSourceSummary.
        display name


        :return: The source_display_name of this LabelSourceSummary.
        :rtype: str
        """
        return self._source_display_name

    @source_display_name.setter
    def source_display_name(self, source_display_name):
        """
        Sets the source_display_name of this LabelSourceSummary.
        display name


        :param source_display_name: The source_display_name of this LabelSourceSummary.
        :type: str
        """
        self._source_display_name = source_display_name

    @property
    def source_name(self):
        """
        Gets the source_name of this LabelSourceSummary.
        source internal name


        :return: The source_name of this LabelSourceSummary.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this LabelSourceSummary.
        source internal name


        :param source_name: The source_name of this LabelSourceSummary.
        :type: str
        """
        self._source_name = source_name

    @property
    def source_id(self):
        """
        Gets the source_id of this LabelSourceSummary.
        source Id


        :return: The source_id of this LabelSourceSummary.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LabelSourceSummary.
        source Id


        :param source_id: The source_id of this LabelSourceSummary.
        :type: int
        """
        self._source_id = source_id

    @property
    def label_operator_name(self):
        """
        Gets the label_operator_name of this LabelSourceSummary.
        label Operator


        :return: The label_operator_name of this LabelSourceSummary.
        :rtype: str
        """
        return self._label_operator_name

    @label_operator_name.setter
    def label_operator_name(self, label_operator_name):
        """
        Sets the label_operator_name of this LabelSourceSummary.
        label Operator


        :param label_operator_name: The label_operator_name of this LabelSourceSummary.
        :type: str
        """
        self._label_operator_name = label_operator_name

    @property
    def label_condition(self):
        """
        Gets the label_condition of this LabelSourceSummary.
        label Condition


        :return: The label_condition of this LabelSourceSummary.
        :rtype: str
        """
        return self._label_condition

    @label_condition.setter
    def label_condition(self, label_condition):
        """
        Sets the label_condition of this LabelSourceSummary.
        label Condition


        :param label_condition: The label_condition of this LabelSourceSummary.
        :type: str
        """
        self._label_condition = label_condition

    @property
    def label_field_displayname(self):
        """
        Gets the label_field_displayname of this LabelSourceSummary.
        label Field Display Name


        :return: The label_field_displayname of this LabelSourceSummary.
        :rtype: str
        """
        return self._label_field_displayname

    @label_field_displayname.setter
    def label_field_displayname(self, label_field_displayname):
        """
        Sets the label_field_displayname of this LabelSourceSummary.
        label Field Display Name


        :param label_field_displayname: The label_field_displayname of this LabelSourceSummary.
        :type: str
        """
        self._label_field_displayname = label_field_displayname

    @property
    def label_field_name(self):
        """
        Gets the label_field_name of this LabelSourceSummary.
        label Field name


        :return: The label_field_name of this LabelSourceSummary.
        :rtype: str
        """
        return self._label_field_name

    @label_field_name.setter
    def label_field_name(self, label_field_name):
        """
        Sets the label_field_name of this LabelSourceSummary.
        label Field name


        :param label_field_name: The label_field_name of this LabelSourceSummary.
        :type: str
        """
        self._label_field_name = label_field_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
