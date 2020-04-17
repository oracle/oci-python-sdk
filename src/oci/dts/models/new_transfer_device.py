# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NewTransferDevice(object):
    """
    NewTransferDevice model.
    """

    #: A constant which can be used with the lifecycle_state property of a NewTransferDevice.
    #: This constant has a value of "PREPARING"
    LIFECYCLE_STATE_PREPARING = "PREPARING"

    def __init__(self, **kwargs):
        """
        Initializes a new NewTransferDevice object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this NewTransferDevice.
        :type label: str

        :param serial_number:
            The value to assign to the serial_number property of this NewTransferDevice.
        :type serial_number: str

        :param iscsi_iqn:
            The value to assign to the iscsi_iqn property of this NewTransferDevice.
        :type iscsi_iqn: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this NewTransferDevice.
            Allowed values for this property are: "PREPARING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param encryption_passphrase:
            The value to assign to the encryption_passphrase property of this NewTransferDevice.
        :type encryption_passphrase: str

        :param transfer_job_id:
            The value to assign to the transfer_job_id property of this NewTransferDevice.
        :type transfer_job_id: str

        :param creation_time:
            The value to assign to the creation_time property of this NewTransferDevice.
        :type creation_time: datetime

        """
        self.swagger_types = {
            'label': 'str',
            'serial_number': 'str',
            'iscsi_iqn': 'str',
            'lifecycle_state': 'str',
            'encryption_passphrase': 'str',
            'transfer_job_id': 'str',
            'creation_time': 'datetime'
        }

        self.attribute_map = {
            'label': 'label',
            'serial_number': 'serialNumber',
            'iscsi_iqn': 'iscsiIQN',
            'lifecycle_state': 'lifecycleState',
            'encryption_passphrase': 'encryptionPassphrase',
            'transfer_job_id': 'transferJobId',
            'creation_time': 'creationTime'
        }

        self._label = None
        self._serial_number = None
        self._iscsi_iqn = None
        self._lifecycle_state = None
        self._encryption_passphrase = None
        self._transfer_job_id = None
        self._creation_time = None

    @property
    def label(self):
        """
        **[Required]** Gets the label of this NewTransferDevice.

        :return: The label of this NewTransferDevice.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this NewTransferDevice.

        :param label: The label of this NewTransferDevice.
        :type: str
        """
        self._label = label

    @property
    def serial_number(self):
        """
        Gets the serial_number of this NewTransferDevice.

        :return: The serial_number of this NewTransferDevice.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this NewTransferDevice.

        :param serial_number: The serial_number of this NewTransferDevice.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def iscsi_iqn(self):
        """
        Gets the iscsi_iqn of this NewTransferDevice.

        :return: The iscsi_iqn of this NewTransferDevice.
        :rtype: str
        """
        return self._iscsi_iqn

    @iscsi_iqn.setter
    def iscsi_iqn(self, iscsi_iqn):
        """
        Sets the iscsi_iqn of this NewTransferDevice.

        :param iscsi_iqn: The iscsi_iqn of this NewTransferDevice.
        :type: str
        """
        self._iscsi_iqn = iscsi_iqn

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this NewTransferDevice.
        Allowed values for this property are: "PREPARING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this NewTransferDevice.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this NewTransferDevice.

        :param lifecycle_state: The lifecycle_state of this NewTransferDevice.
        :type: str
        """
        allowed_values = ["PREPARING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def encryption_passphrase(self):
        """
        Gets the encryption_passphrase of this NewTransferDevice.

        :return: The encryption_passphrase of this NewTransferDevice.
        :rtype: str
        """
        return self._encryption_passphrase

    @encryption_passphrase.setter
    def encryption_passphrase(self, encryption_passphrase):
        """
        Sets the encryption_passphrase of this NewTransferDevice.

        :param encryption_passphrase: The encryption_passphrase of this NewTransferDevice.
        :type: str
        """
        self._encryption_passphrase = encryption_passphrase

    @property
    def transfer_job_id(self):
        """
        Gets the transfer_job_id of this NewTransferDevice.

        :return: The transfer_job_id of this NewTransferDevice.
        :rtype: str
        """
        return self._transfer_job_id

    @transfer_job_id.setter
    def transfer_job_id(self, transfer_job_id):
        """
        Sets the transfer_job_id of this NewTransferDevice.

        :param transfer_job_id: The transfer_job_id of this NewTransferDevice.
        :type: str
        """
        self._transfer_job_id = transfer_job_id

    @property
    def creation_time(self):
        """
        Gets the creation_time of this NewTransferDevice.

        :return: The creation_time of this NewTransferDevice.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this NewTransferDevice.

        :param creation_time: The creation_time of this NewTransferDevice.
        :type: datetime
        """
        self._creation_time = creation_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
