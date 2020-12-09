# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Category(object):
    """
    Categories for resources.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Category object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Category.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this Category.
        :type display_name: str

        :param parameters:
            The value to assign to the parameters property of this Category.
        :type parameters: list[oci.logging.models.Parameter]

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'parameters': 'list[Parameter]'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'parameters': 'parameters'
        }

        self._name = None
        self._display_name = None
        self._parameters = None

    @property
    def name(self):
        """
        Gets the name of this Category.
        Category name.


        :return: The name of this Category.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Category.
        Category name.


        :param name: The name of this Category.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this Category.
        Category display name.


        :return: The display_name of this Category.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Category.
        Category display name.


        :param display_name: The display_name of this Category.
        :type: str
        """
        self._display_name = display_name

    @property
    def parameters(self):
        """
        Gets the parameters of this Category.
        Parameters the category supports.


        :return: The parameters of this Category.
        :rtype: list[oci.logging.models.Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this Category.
        Parameters the category supports.


        :param parameters: The parameters of this Category.
        :type: list[oci.logging.models.Parameter]
        """
        self._parameters = parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
