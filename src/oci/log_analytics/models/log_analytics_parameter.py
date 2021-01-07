# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsParameter(object):
    """
    LogAnalyticsParameter
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsParameter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param default_value:
            The value to assign to the default_value property of this LogAnalyticsParameter.
        :type default_value: str

        :param description:
            The value to assign to the description property of this LogAnalyticsParameter.
        :type description: str

        :param is_active:
            The value to assign to the is_active property of this LogAnalyticsParameter.
        :type is_active: bool

        :param name:
            The value to assign to the name property of this LogAnalyticsParameter.
        :type name: str

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsParameter.
        :type source_id: int

        """
        self.swagger_types = {
            'default_value': 'str',
            'description': 'str',
            'is_active': 'bool',
            'name': 'str',
            'source_id': 'int'
        }

        self.attribute_map = {
            'default_value': 'defaultValue',
            'description': 'description',
            'is_active': 'isActive',
            'name': 'name',
            'source_id': 'sourceId'
        }

        self._default_value = None
        self._description = None
        self._is_active = None
        self._name = None
        self._source_id = None

    @property
    def default_value(self):
        """
        Gets the default_value of this LogAnalyticsParameter.
        default value


        :return: The default_value of this LogAnalyticsParameter.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this LogAnalyticsParameter.
        default value


        :param default_value: The default_value of this LogAnalyticsParameter.
        :type: str
        """
        self._default_value = default_value

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsParameter.
        description


        :return: The description of this LogAnalyticsParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsParameter.
        description


        :param description: The description of this LogAnalyticsParameter.
        :type: str
        """
        self._description = description

    @property
    def is_active(self):
        """
        Gets the is_active of this LogAnalyticsParameter.
        is active flag


        :return: The is_active of this LogAnalyticsParameter.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this LogAnalyticsParameter.
        is active flag


        :param is_active: The is_active of this LogAnalyticsParameter.
        :type: bool
        """
        self._is_active = is_active

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsParameter.
        parameter name


        :return: The name of this LogAnalyticsParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsParameter.
        parameter name


        :param name: The name of this LogAnalyticsParameter.
        :type: str
        """
        self._name = name

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsParameter.
        source Id


        :return: The source_id of this LogAnalyticsParameter.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsParameter.
        source Id


        :param source_id: The source_id of this LogAnalyticsParameter.
        :type: int
        """
        self._source_id = source_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
