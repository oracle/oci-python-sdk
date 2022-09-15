# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScsiController(object):
    """
    The assets SCSI controller.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScsiController object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this ScsiController.
        :type label: str

        :param unit_number:
            The value to assign to the unit_number property of this ScsiController.
        :type unit_number: int

        :param shared_bus:
            The value to assign to the shared_bus property of this ScsiController.
        :type shared_bus: str

        """
        self.swagger_types = {
            'label': 'str',
            'unit_number': 'int',
            'shared_bus': 'str'
        }

        self.attribute_map = {
            'label': 'label',
            'unit_number': 'unitNumber',
            'shared_bus': 'sharedBus'
        }

        self._label = None
        self._unit_number = None
        self._shared_bus = None

    @property
    def label(self):
        """
        Gets the label of this ScsiController.
        Provides a label and summary information for the device.


        :return: The label of this ScsiController.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this ScsiController.
        Provides a label and summary information for the device.


        :param label: The label of this ScsiController.
        :type: str
        """
        self._label = label

    @property
    def unit_number(self):
        """
        Gets the unit_number of this ScsiController.
        The unit number of the SCSI controller.


        :return: The unit_number of this ScsiController.
        :rtype: int
        """
        return self._unit_number

    @unit_number.setter
    def unit_number(self, unit_number):
        """
        Sets the unit_number of this ScsiController.
        The unit number of the SCSI controller.


        :param unit_number: The unit_number of this ScsiController.
        :type: int
        """
        self._unit_number = unit_number

    @property
    def shared_bus(self):
        """
        Gets the shared_bus of this ScsiController.
        Shared bus.


        :return: The shared_bus of this ScsiController.
        :rtype: str
        """
        return self._shared_bus

    @shared_bus.setter
    def shared_bus(self, shared_bus):
        """
        Sets the shared_bus of this ScsiController.
        Shared bus.


        :param shared_bus: The shared_bus of this ScsiController.
        :type: str
        """
        self._shared_bus = shared_bus

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
