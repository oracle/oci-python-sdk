# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsMetaFunction(object):
    """
    LogAnalyticsMetaFunction
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsMetaFunction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param meta_function_argument:
            The value to assign to the meta_function_argument property of this LogAnalyticsMetaFunction.
        :type meta_function_argument: list[oci.log_analytics.models.LogAnalyticsMetaFunctionArgument]

        :param component:
            The value to assign to the component property of this LogAnalyticsMetaFunction.
        :type component: str

        :param description:
            The value to assign to the description property of this LogAnalyticsMetaFunction.
        :type description: str

        :param edit_version:
            The value to assign to the edit_version property of this LogAnalyticsMetaFunction.
        :type edit_version: int

        :param meta_function_id:
            The value to assign to the meta_function_id property of this LogAnalyticsMetaFunction.
        :type meta_function_id: int

        :param java_class_name:
            The value to assign to the java_class_name property of this LogAnalyticsMetaFunction.
        :type java_class_name: str

        :param name:
            The value to assign to the name property of this LogAnalyticsMetaFunction.
        :type name: str

        """
        self.swagger_types = {
            'meta_function_argument': 'list[LogAnalyticsMetaFunctionArgument]',
            'component': 'str',
            'description': 'str',
            'edit_version': 'int',
            'meta_function_id': 'int',
            'java_class_name': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'meta_function_argument': 'metaFunctionArgument',
            'component': 'component',
            'description': 'description',
            'edit_version': 'editVersion',
            'meta_function_id': 'metaFunctionId',
            'java_class_name': 'javaClassName',
            'name': 'name'
        }

        self._meta_function_argument = None
        self._component = None
        self._description = None
        self._edit_version = None
        self._meta_function_id = None
        self._java_class_name = None
        self._name = None

    @property
    def meta_function_argument(self):
        """
        Gets the meta_function_argument of this LogAnalyticsMetaFunction.
        An array of meta function arguments.


        :return: The meta_function_argument of this LogAnalyticsMetaFunction.
        :rtype: list[oci.log_analytics.models.LogAnalyticsMetaFunctionArgument]
        """
        return self._meta_function_argument

    @meta_function_argument.setter
    def meta_function_argument(self, meta_function_argument):
        """
        Sets the meta_function_argument of this LogAnalyticsMetaFunction.
        An array of meta function arguments.


        :param meta_function_argument: The meta_function_argument of this LogAnalyticsMetaFunction.
        :type: list[oci.log_analytics.models.LogAnalyticsMetaFunctionArgument]
        """
        self._meta_function_argument = meta_function_argument

    @property
    def component(self):
        """
        Gets the component of this LogAnalyticsMetaFunction.
        The component.


        :return: The component of this LogAnalyticsMetaFunction.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this LogAnalyticsMetaFunction.
        The component.


        :param component: The component of this LogAnalyticsMetaFunction.
        :type: str
        """
        self._component = component

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsMetaFunction.
        The description.


        :return: The description of this LogAnalyticsMetaFunction.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsMetaFunction.
        The description.


        :param description: The description of this LogAnalyticsMetaFunction.
        :type: str
        """
        self._description = description

    @property
    def edit_version(self):
        """
        Gets the edit_version of this LogAnalyticsMetaFunction.
        The edit version.


        :return: The edit_version of this LogAnalyticsMetaFunction.
        :rtype: int
        """
        return self._edit_version

    @edit_version.setter
    def edit_version(self, edit_version):
        """
        Sets the edit_version of this LogAnalyticsMetaFunction.
        The edit version.


        :param edit_version: The edit_version of this LogAnalyticsMetaFunction.
        :type: int
        """
        self._edit_version = edit_version

    @property
    def meta_function_id(self):
        """
        Gets the meta_function_id of this LogAnalyticsMetaFunction.
        The meta function unique identifier.


        :return: The meta_function_id of this LogAnalyticsMetaFunction.
        :rtype: int
        """
        return self._meta_function_id

    @meta_function_id.setter
    def meta_function_id(self, meta_function_id):
        """
        Sets the meta_function_id of this LogAnalyticsMetaFunction.
        The meta function unique identifier.


        :param meta_function_id: The meta_function_id of this LogAnalyticsMetaFunction.
        :type: int
        """
        self._meta_function_id = meta_function_id

    @property
    def java_class_name(self):
        """
        Gets the java_class_name of this LogAnalyticsMetaFunction.
        The java class name.


        :return: The java_class_name of this LogAnalyticsMetaFunction.
        :rtype: str
        """
        return self._java_class_name

    @java_class_name.setter
    def java_class_name(self, java_class_name):
        """
        Sets the java_class_name of this LogAnalyticsMetaFunction.
        The java class name.


        :param java_class_name: The java_class_name of this LogAnalyticsMetaFunction.
        :type: str
        """
        self._java_class_name = java_class_name

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsMetaFunction.
        The meta function name.


        :return: The name of this LogAnalyticsMetaFunction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsMetaFunction.
        The meta function name.


        :param name: The name of this LogAnalyticsMetaFunction.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
