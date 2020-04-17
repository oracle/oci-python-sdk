# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MultipleTransferDevices(object):
    """
    MultipleTransferDevices model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MultipleTransferDevices object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param transfer_device_objects:
            The value to assign to the transfer_device_objects property of this MultipleTransferDevices.
        :type transfer_device_objects: list[TransferDeviceSummary]

        """
        self.swagger_types = {
            'transfer_device_objects': 'list[TransferDeviceSummary]'
        }

        self.attribute_map = {
            'transfer_device_objects': 'transferDeviceObjects'
        }

        self._transfer_device_objects = None

    @property
    def transfer_device_objects(self):
        """
        Gets the transfer_device_objects of this MultipleTransferDevices.
        List of TransferDeviceObject's


        :return: The transfer_device_objects of this MultipleTransferDevices.
        :rtype: list[TransferDeviceSummary]
        """
        return self._transfer_device_objects

    @transfer_device_objects.setter
    def transfer_device_objects(self, transfer_device_objects):
        """
        Sets the transfer_device_objects of this MultipleTransferDevices.
        List of TransferDeviceObject's


        :param transfer_device_objects: The transfer_device_objects of this MultipleTransferDevices.
        :type: list[TransferDeviceSummary]
        """
        self._transfer_device_objects = transfer_device_objects

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
