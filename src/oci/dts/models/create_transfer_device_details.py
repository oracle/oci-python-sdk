# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTransferDeviceDetails(object):
    """
    CreateTransferDeviceDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTransferDeviceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param serial_number:
            The value to assign to the serial_number property of this CreateTransferDeviceDetails.
        :type serial_number: str

        :param iscsi_iqn:
            The value to assign to the iscsi_iqn property of this CreateTransferDeviceDetails.
        :type iscsi_iqn: str

        """
        self.swagger_types = {
            'serial_number': 'str',
            'iscsi_iqn': 'str'
        }

        self.attribute_map = {
            'serial_number': 'serialNumber',
            'iscsi_iqn': 'iscsiIQN'
        }

        self._serial_number = None
        self._iscsi_iqn = None

    @property
    def serial_number(self):
        """
        Gets the serial_number of this CreateTransferDeviceDetails.

        :return: The serial_number of this CreateTransferDeviceDetails.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this CreateTransferDeviceDetails.

        :param serial_number: The serial_number of this CreateTransferDeviceDetails.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def iscsi_iqn(self):
        """
        Gets the iscsi_iqn of this CreateTransferDeviceDetails.

        :return: The iscsi_iqn of this CreateTransferDeviceDetails.
        :rtype: str
        """
        return self._iscsi_iqn

    @iscsi_iqn.setter
    def iscsi_iqn(self, iscsi_iqn):
        """
        Sets the iscsi_iqn of this CreateTransferDeviceDetails.

        :param iscsi_iqn: The iscsi_iqn of this CreateTransferDeviceDetails.
        :type: str
        """
        self._iscsi_iqn = iscsi_iqn

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
