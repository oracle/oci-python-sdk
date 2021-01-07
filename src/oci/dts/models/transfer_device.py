# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TransferDevice(object):
    """
    TransferDevice model.
    """

    #: A constant which can be used with the lifecycle_state property of a TransferDevice.
    #: This constant has a value of "PREPARING"
    LIFECYCLE_STATE_PREPARING = "PREPARING"

    #: A constant which can be used with the lifecycle_state property of a TransferDevice.
    #: This constant has a value of "READY"
    LIFECYCLE_STATE_READY = "READY"

    #: A constant which can be used with the lifecycle_state property of a TransferDevice.
    #: This constant has a value of "PACKAGED"
    LIFECYCLE_STATE_PACKAGED = "PACKAGED"

    #: A constant which can be used with the lifecycle_state property of a TransferDevice.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TransferDevice.
    #: This constant has a value of "PROCESSING"
    LIFECYCLE_STATE_PROCESSING = "PROCESSING"

    #: A constant which can be used with the lifecycle_state property of a TransferDevice.
    #: This constant has a value of "COMPLETE"
    LIFECYCLE_STATE_COMPLETE = "COMPLETE"

    #: A constant which can be used with the lifecycle_state property of a TransferDevice.
    #: This constant has a value of "MISSING"
    LIFECYCLE_STATE_MISSING = "MISSING"

    #: A constant which can be used with the lifecycle_state property of a TransferDevice.
    #: This constant has a value of "ERROR"
    LIFECYCLE_STATE_ERROR = "ERROR"

    #: A constant which can be used with the lifecycle_state property of a TransferDevice.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TransferDevice.
    #: This constant has a value of "CANCELLED"
    LIFECYCLE_STATE_CANCELLED = "CANCELLED"

    def __init__(self, **kwargs):
        """
        Initializes a new TransferDevice object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param serial_number:
            The value to assign to the serial_number property of this TransferDevice.
        :type serial_number: str

        :param iscsi_iqn:
            The value to assign to the iscsi_iqn property of this TransferDevice.
        :type iscsi_iqn: str

        :param label:
            The value to assign to the label property of this TransferDevice.
        :type label: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TransferDevice.
            Allowed values for this property are: "PREPARING", "READY", "PACKAGED", "ACTIVE", "PROCESSING", "COMPLETE", "MISSING", "ERROR", "DELETED", "CANCELLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param transfer_job_id:
            The value to assign to the transfer_job_id property of this TransferDevice.
        :type transfer_job_id: str

        :param attached_transfer_package_label:
            The value to assign to the attached_transfer_package_label property of this TransferDevice.
        :type attached_transfer_package_label: str

        :param creation_time:
            The value to assign to the creation_time property of this TransferDevice.
        :type creation_time: datetime

        :param upload_status_log_uri:
            The value to assign to the upload_status_log_uri property of this TransferDevice.
        :type upload_status_log_uri: str

        """
        self.swagger_types = {
            'serial_number': 'str',
            'iscsi_iqn': 'str',
            'label': 'str',
            'lifecycle_state': 'str',
            'transfer_job_id': 'str',
            'attached_transfer_package_label': 'str',
            'creation_time': 'datetime',
            'upload_status_log_uri': 'str'
        }

        self.attribute_map = {
            'serial_number': 'serialNumber',
            'iscsi_iqn': 'iscsiIQN',
            'label': 'label',
            'lifecycle_state': 'lifecycleState',
            'transfer_job_id': 'transferJobId',
            'attached_transfer_package_label': 'attachedTransferPackageLabel',
            'creation_time': 'creationTime',
            'upload_status_log_uri': 'uploadStatusLogUri'
        }

        self._serial_number = None
        self._iscsi_iqn = None
        self._label = None
        self._lifecycle_state = None
        self._transfer_job_id = None
        self._attached_transfer_package_label = None
        self._creation_time = None
        self._upload_status_log_uri = None

    @property
    def serial_number(self):
        """
        Gets the serial_number of this TransferDevice.

        :return: The serial_number of this TransferDevice.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this TransferDevice.

        :param serial_number: The serial_number of this TransferDevice.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def iscsi_iqn(self):
        """
        Gets the iscsi_iqn of this TransferDevice.

        :return: The iscsi_iqn of this TransferDevice.
        :rtype: str
        """
        return self._iscsi_iqn

    @iscsi_iqn.setter
    def iscsi_iqn(self, iscsi_iqn):
        """
        Sets the iscsi_iqn of this TransferDevice.

        :param iscsi_iqn: The iscsi_iqn of this TransferDevice.
        :type: str
        """
        self._iscsi_iqn = iscsi_iqn

    @property
    def label(self):
        """
        **[Required]** Gets the label of this TransferDevice.

        :return: The label of this TransferDevice.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this TransferDevice.

        :param label: The label of this TransferDevice.
        :type: str
        """
        self._label = label

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TransferDevice.
        Allowed values for this property are: "PREPARING", "READY", "PACKAGED", "ACTIVE", "PROCESSING", "COMPLETE", "MISSING", "ERROR", "DELETED", "CANCELLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TransferDevice.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TransferDevice.

        :param lifecycle_state: The lifecycle_state of this TransferDevice.
        :type: str
        """
        allowed_values = ["PREPARING", "READY", "PACKAGED", "ACTIVE", "PROCESSING", "COMPLETE", "MISSING", "ERROR", "DELETED", "CANCELLED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def transfer_job_id(self):
        """
        Gets the transfer_job_id of this TransferDevice.

        :return: The transfer_job_id of this TransferDevice.
        :rtype: str
        """
        return self._transfer_job_id

    @transfer_job_id.setter
    def transfer_job_id(self, transfer_job_id):
        """
        Sets the transfer_job_id of this TransferDevice.

        :param transfer_job_id: The transfer_job_id of this TransferDevice.
        :type: str
        """
        self._transfer_job_id = transfer_job_id

    @property
    def attached_transfer_package_label(self):
        """
        Gets the attached_transfer_package_label of this TransferDevice.

        :return: The attached_transfer_package_label of this TransferDevice.
        :rtype: str
        """
        return self._attached_transfer_package_label

    @attached_transfer_package_label.setter
    def attached_transfer_package_label(self, attached_transfer_package_label):
        """
        Sets the attached_transfer_package_label of this TransferDevice.

        :param attached_transfer_package_label: The attached_transfer_package_label of this TransferDevice.
        :type: str
        """
        self._attached_transfer_package_label = attached_transfer_package_label

    @property
    def creation_time(self):
        """
        Gets the creation_time of this TransferDevice.

        :return: The creation_time of this TransferDevice.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this TransferDevice.

        :param creation_time: The creation_time of this TransferDevice.
        :type: datetime
        """
        self._creation_time = creation_time

    @property
    def upload_status_log_uri(self):
        """
        Gets the upload_status_log_uri of this TransferDevice.

        :return: The upload_status_log_uri of this TransferDevice.
        :rtype: str
        """
        return self._upload_status_log_uri

    @upload_status_log_uri.setter
    def upload_status_log_uri(self, upload_status_log_uri):
        """
        Sets the upload_status_log_uri of this TransferDevice.

        :param upload_status_log_uri: The upload_status_log_uri of this TransferDevice.
        :type: str
        """
        self._upload_status_log_uri = upload_status_log_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
