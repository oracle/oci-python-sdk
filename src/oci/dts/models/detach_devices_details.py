# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetachDevicesDetails(object):
    """
    DetachDevicesDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetachDevicesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param device_labels:
            The value to assign to the device_labels property of this DetachDevicesDetails.
        :type device_labels: list[str]

        """
        self.swagger_types = {
            'device_labels': 'list[str]'
        }

        self.attribute_map = {
            'device_labels': 'deviceLabels'
        }

        self._device_labels = None

    @property
    def device_labels(self):
        """
        Gets the device_labels of this DetachDevicesDetails.
        List of TransferDeviceLabel's


        :return: The device_labels of this DetachDevicesDetails.
        :rtype: list[str]
        """
        return self._device_labels

    @device_labels.setter
    def device_labels(self, device_labels):
        """
        Sets the device_labels of this DetachDevicesDetails.
        List of TransferDeviceLabel's


        :param device_labels: The device_labels of this DetachDevicesDetails.
        :type: list[str]
        """
        self._device_labels = device_labels

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
