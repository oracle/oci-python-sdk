# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CopyVolumeGroupBackupDetails(object):
    """
    CopyVolumeGroupBackupDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CopyVolumeGroupBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination_region:
            The value to assign to the destination_region property of this CopyVolumeGroupBackupDetails.
        :type destination_region: str

        :param display_name:
            The value to assign to the display_name property of this CopyVolumeGroupBackupDetails.
        :type display_name: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CopyVolumeGroupBackupDetails.
        :type kms_key_id: str

        """
        self.swagger_types = {
            'destination_region': 'str',
            'display_name': 'str',
            'kms_key_id': 'str'
        }
        self.attribute_map = {
            'destination_region': 'destinationRegion',
            'display_name': 'displayName',
            'kms_key_id': 'kmsKeyId'
        }
        self._destination_region = None
        self._display_name = None
        self._kms_key_id = None

    @property
    def destination_region(self):
        """
        **[Required]** Gets the destination_region of this CopyVolumeGroupBackupDetails.
        The name of the destination region.

        Example: `us-ashburn-1`


        :return: The destination_region of this CopyVolumeGroupBackupDetails.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """
        Sets the destination_region of this CopyVolumeGroupBackupDetails.
        The name of the destination region.

        Example: `us-ashburn-1`


        :param destination_region: The destination_region of this CopyVolumeGroupBackupDetails.
        :type: str
        """
        self._destination_region = destination_region

    @property
    def display_name(self):
        """
        Gets the display_name of this CopyVolumeGroupBackupDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CopyVolumeGroupBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CopyVolumeGroupBackupDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CopyVolumeGroupBackupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this CopyVolumeGroupBackupDetails.
        The OCID of the Vault service key in the destination region which will be the master encryption key
        for the copied volume group backup.
        If you do not specify this attribute the volume group backup will be encrypted with the Oracle-provided encryption
        key when it is copied to the destination region.


        For more information about the Vault service and encryption keys, see
        `Overview of Vault service`__ and
        `Using Keys`__.

        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm
        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm


        :return: The kms_key_id of this CopyVolumeGroupBackupDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CopyVolumeGroupBackupDetails.
        The OCID of the Vault service key in the destination region which will be the master encryption key
        for the copied volume group backup.
        If you do not specify this attribute the volume group backup will be encrypted with the Oracle-provided encryption
        key when it is copied to the destination region.


        For more information about the Vault service and encryption keys, see
        `Overview of Vault service`__ and
        `Using Keys`__.

        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm
        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm


        :param kms_key_id: The kms_key_id of this CopyVolumeGroupBackupDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
