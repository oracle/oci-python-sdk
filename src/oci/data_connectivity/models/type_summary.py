# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TypeSummary(object):
    """
    The type object for supported connectors.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TypeSummary.
        :type key: str

        :param name:
            The value to assign to the name property of this TypeSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this TypeSummary.
        :type description: str

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'description': 'description'
        }

        self._key = None
        self._name = None
        self._description = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this TypeSummary.
        unique id of specefic data asset type.


        :return: The key of this TypeSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TypeSummary.
        unique id of specefic data asset type.


        :param key: The key of this TypeSummary.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        **[Required]** Gets the name of this TypeSummary.
        Name of the specific data asset type.


        :return: The name of this TypeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TypeSummary.
        Name of the specific data asset type.


        :param name: The name of this TypeSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TypeSummary.
        desctription for the specific data asset type.


        :return: The description of this TypeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TypeSummary.
        desctription for the specific data asset type.


        :param description: The description of this TypeSummary.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
