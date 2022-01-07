# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityTypeProperty(object):
    """
    Properties used in file patterns specified in log sources.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntityTypeProperty object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this EntityTypeProperty.
        :type name: str

        :param description:
            The value to assign to the description property of this EntityTypeProperty.
        :type description: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description'
        }

        self._name = None
        self._description = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this EntityTypeProperty.
        Log analytics entity type property name.


        :return: The name of this EntityTypeProperty.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EntityTypeProperty.
        Log analytics entity type property name.


        :param name: The name of this EntityTypeProperty.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this EntityTypeProperty.
        Description for the log analytics entity type property.


        :return: The description of this EntityTypeProperty.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EntityTypeProperty.
        Description for the log analytics entity type property.


        :param description: The description of this EntityTypeProperty.
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
