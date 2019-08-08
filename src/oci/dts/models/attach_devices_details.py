# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachDevicesDetails(object):
    """
    AttachDevicesDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachDevicesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param device_labels:
            The value to assign to the device_labels property of this AttachDevicesDetails.
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
        Gets the device_labels of this AttachDevicesDetails.
        List of TransferDeviceLabel's


        :return: The device_labels of this AttachDevicesDetails.
        :rtype: list[str]
        """
        return self._device_labels

    @device_labels.setter
    def device_labels(self, device_labels):
        """
        Sets the device_labels of this AttachDevicesDetails.
        List of TransferDeviceLabel's


        :param device_labels: The device_labels of this AttachDevicesDetails.
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
