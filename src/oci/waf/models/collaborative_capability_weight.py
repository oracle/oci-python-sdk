# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CollaborativeCapabilityWeight(object):
    """
    Defines how much a contributing capability contributes towards the action threshold of a collaborative protection capability.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CollaborativeCapabilityWeight object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CollaborativeCapabilityWeight.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this CollaborativeCapabilityWeight.
        :type display_name: str

        :param weight:
            The value to assign to the weight property of this CollaborativeCapabilityWeight.
        :type weight: int

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'weight': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'weight': 'weight'
        }

        self._key = None
        self._display_name = None
        self._weight = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this CollaborativeCapabilityWeight.
        Unique key of contributing protection capability.


        :return: The key of this CollaborativeCapabilityWeight.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CollaborativeCapabilityWeight.
        Unique key of contributing protection capability.


        :param key: The key of this CollaborativeCapabilityWeight.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CollaborativeCapabilityWeight.
        The display name of contributing protection capability.


        :return: The display_name of this CollaborativeCapabilityWeight.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CollaborativeCapabilityWeight.
        The display name of contributing protection capability.


        :param display_name: The display_name of this CollaborativeCapabilityWeight.
        :type: str
        """
        self._display_name = display_name

    @property
    def weight(self):
        """
        **[Required]** Gets the weight of this CollaborativeCapabilityWeight.
        The weight of contributing protection capability.


        :return: The weight of this CollaborativeCapabilityWeight.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this CollaborativeCapabilityWeight.
        The weight of contributing protection capability.


        :param weight: The weight of this CollaborativeCapabilityWeight.
        :type: int
        """
        self._weight = weight

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
