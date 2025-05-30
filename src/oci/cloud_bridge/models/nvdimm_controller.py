# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220509


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NvdimmController(object):
    """
    The asset's NVDIMM configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NvdimmController object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this NvdimmController.
        :type label: str

        :param bus_number:
            The value to assign to the bus_number property of this NvdimmController.
        :type bus_number: int

        """
        self.swagger_types = {
            'label': 'str',
            'bus_number': 'int'
        }
        self.attribute_map = {
            'label': 'label',
            'bus_number': 'busNumber'
        }
        self._label = None
        self._bus_number = None

    @property
    def label(self):
        """
        Gets the label of this NvdimmController.
        Provides a label and summary information for the device.


        :return: The label of this NvdimmController.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this NvdimmController.
        Provides a label and summary information for the device.


        :param label: The label of this NvdimmController.
        :type: str
        """
        self._label = label

    @property
    def bus_number(self):
        """
        Gets the bus_number of this NvdimmController.
        Bus number.


        :return: The bus_number of this NvdimmController.
        :rtype: int
        """
        return self._bus_number

    @bus_number.setter
    def bus_number(self, bus_number):
        """
        Sets the bus_number of this NvdimmController.
        Bus number.


        :param bus_number: The bus_number of this NvdimmController.
        :type: int
        """
        self._bus_number = bus_number

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
