# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsLabelDefinition(object):
    """
    LogAnalyticsLabelDefinition
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsLabelDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param edit_version:
            The value to assign to the edit_version property of this LogAnalyticsLabelDefinition.
        :type edit_version: int

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsLabelDefinition.
        :type is_system: bool

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsLabelDefinition.
        :type source_id: int

        :param label_name:
            The value to assign to the label_name property of this LogAnalyticsLabelDefinition.
        :type label_name: str

        """
        self.swagger_types = {
            'edit_version': 'int',
            'is_system': 'bool',
            'source_id': 'int',
            'label_name': 'str'
        }

        self.attribute_map = {
            'edit_version': 'editVersion',
            'is_system': 'isSystem',
            'source_id': 'sourceId',
            'label_name': 'labelName'
        }

        self._edit_version = None
        self._is_system = None
        self._source_id = None
        self._label_name = None

    @property
    def edit_version(self):
        """
        Gets the edit_version of this LogAnalyticsLabelDefinition.
        The edit version.


        :return: The edit_version of this LogAnalyticsLabelDefinition.
        :rtype: int
        """
        return self._edit_version

    @edit_version.setter
    def edit_version(self, edit_version):
        """
        Sets the edit_version of this LogAnalyticsLabelDefinition.
        The edit version.


        :param edit_version: The edit_version of this LogAnalyticsLabelDefinition.
        :type: int
        """
        self._edit_version = edit_version

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsLabelDefinition.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :return: The is_system of this LogAnalyticsLabelDefinition.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsLabelDefinition.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :param is_system: The is_system of this LogAnalyticsLabelDefinition.
        :type: bool
        """
        self._is_system = is_system

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsLabelDefinition.
        The source unique identifier.


        :return: The source_id of this LogAnalyticsLabelDefinition.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsLabelDefinition.
        The source unique identifier.


        :param source_id: The source_id of this LogAnalyticsLabelDefinition.
        :type: int
        """
        self._source_id = source_id

    @property
    def label_name(self):
        """
        Gets the label_name of this LogAnalyticsLabelDefinition.
        The label name.


        :return: The label_name of this LogAnalyticsLabelDefinition.
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        """
        Sets the label_name of this LogAnalyticsLabelDefinition.
        The label name.


        :param label_name: The label_name of this LogAnalyticsLabelDefinition.
        :type: str
        """
        self._label_name = label_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
