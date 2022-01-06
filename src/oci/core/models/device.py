# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Device(object):
    """
    Device Path corresponding to the block devices attached to instances having a name and isAvailable flag.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Device object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Device.
        :type name: str

        :param is_available:
            The value to assign to the is_available property of this Device.
        :type is_available: bool

        """
        self.swagger_types = {
            'name': 'str',
            'is_available': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'is_available': 'isAvailable'
        }

        self._name = None
        self._is_available = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Device.
        The device name.


        :return: The name of this Device.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Device.
        The device name.


        :param name: The name of this Device.
        :type: str
        """
        self._name = name

    @property
    def is_available(self):
        """
        **[Required]** Gets the is_available of this Device.
        The flag denoting whether device is available.


        :return: The is_available of this Device.
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        """
        Sets the is_available of this Device.
        The flag denoting whether device is available.


        :param is_available: The is_available of this Device.
        :type: bool
        """
        self._is_available = is_available

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
