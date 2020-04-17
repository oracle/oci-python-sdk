# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubCategory(object):
    """
    Details of Sub Category of the incident
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubCategory object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sub_category_key:
            The value to assign to the sub_category_key property of this SubCategory.
        :type sub_category_key: str

        :param name:
            The value to assign to the name property of this SubCategory.
        :type name: str

        """
        self.swagger_types = {
            'sub_category_key': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'sub_category_key': 'subCategoryKey',
            'name': 'name'
        }

        self._sub_category_key = None
        self._name = None

    @property
    def sub_category_key(self):
        """
        Gets the sub_category_key of this SubCategory.
        Unique ID that identifies a Sub Category


        :return: The sub_category_key of this SubCategory.
        :rtype: str
        """
        return self._sub_category_key

    @sub_category_key.setter
    def sub_category_key(self, sub_category_key):
        """
        Sets the sub_category_key of this SubCategory.
        Unique ID that identifies a Sub Category


        :param sub_category_key: The sub_category_key of this SubCategory.
        :type: str
        """
        self._sub_category_key = sub_category_key

    @property
    def name(self):
        """
        Gets the name of this SubCategory.
        Name of sub category. eg: Backup Count, Custom Image Count


        :return: The name of this SubCategory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SubCategory.
        Name of sub category. eg: Backup Count, Custom Image Count


        :param name: The name of this SubCategory.
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
