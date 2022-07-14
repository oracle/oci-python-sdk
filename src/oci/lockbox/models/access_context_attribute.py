# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessContextAttribute(object):
    """
    Defined by partner while creating a lockbox. These attributes provides context for creating access request
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AccessContextAttribute object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AccessContextAttribute.
        :type name: str

        :param description:
            The value to assign to the description property of this AccessContextAttribute.
        :type description: str

        :param default_value:
            The value to assign to the default_value property of this AccessContextAttribute.
        :type default_value: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'default_value': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'default_value': 'defaultValue'
        }

        self._name = None
        self._description = None
        self._default_value = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AccessContextAttribute.
        The name of the context attribute


        :return: The name of this AccessContextAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AccessContextAttribute.
        The name of the context attribute


        :param name: The name of this AccessContextAttribute.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this AccessContextAttribute.
        The description of the context attribute


        :return: The description of this AccessContextAttribute.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AccessContextAttribute.
        The description of the context attribute


        :param description: The description of this AccessContextAttribute.
        :type: str
        """
        self._description = description

    @property
    def default_value(self):
        """
        Gets the default_value of this AccessContextAttribute.
        An optional default value used when access request context value is not provided


        :return: The default_value of this AccessContextAttribute.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this AccessContextAttribute.
        An optional default value used when access request context value is not provided


        :param default_value: The default_value of this AccessContextAttribute.
        :type: str
        """
        self._default_value = default_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
