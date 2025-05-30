# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeGroupReplicaInfo(object):
    """
    Information about the volume group replica in the destination availability domain.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeGroupReplicaInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this VolumeGroupReplicaInfo.
        :type display_name: str

        :param volume_group_replica_id:
            The value to assign to the volume_group_replica_id property of this VolumeGroupReplicaInfo.
        :type volume_group_replica_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this VolumeGroupReplicaInfo.
        :type availability_domain: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this VolumeGroupReplicaInfo.
        :type kms_key_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'volume_group_replica_id': 'str',
            'availability_domain': 'str',
            'kms_key_id': 'str'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'volume_group_replica_id': 'volumeGroupReplicaId',
            'availability_domain': 'availabilityDomain',
            'kms_key_id': 'kmsKeyId'
        }
        self._display_name = None
        self._volume_group_replica_id = None
        self._availability_domain = None
        self._kms_key_id = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this VolumeGroupReplicaInfo.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this VolumeGroupReplicaInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VolumeGroupReplicaInfo.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this VolumeGroupReplicaInfo.
        :type: str
        """
        self._display_name = display_name

    @property
    def volume_group_replica_id(self):
        """
        **[Required]** Gets the volume_group_replica_id of this VolumeGroupReplicaInfo.
        The volume group replica's Oracle ID (OCID).


        :return: The volume_group_replica_id of this VolumeGroupReplicaInfo.
        :rtype: str
        """
        return self._volume_group_replica_id

    @volume_group_replica_id.setter
    def volume_group_replica_id(self, volume_group_replica_id):
        """
        Sets the volume_group_replica_id of this VolumeGroupReplicaInfo.
        The volume group replica's Oracle ID (OCID).


        :param volume_group_replica_id: The volume_group_replica_id of this VolumeGroupReplicaInfo.
        :type: str
        """
        self._volume_group_replica_id = volume_group_replica_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this VolumeGroupReplicaInfo.
        The availability domain of the boot volume replica replica.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this VolumeGroupReplicaInfo.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this VolumeGroupReplicaInfo.
        The availability domain of the boot volume replica replica.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this VolumeGroupReplicaInfo.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this VolumeGroupReplicaInfo.
        The OCID of the Vault service key to assign as the master encryption key for the block volume replica, see
        `Overview of Vault service`__ and
        `Using Keys`__.

        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm
        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm


        :return: The kms_key_id of this VolumeGroupReplicaInfo.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this VolumeGroupReplicaInfo.
        The OCID of the Vault service key to assign as the master encryption key for the block volume replica, see
        `Overview of Vault service`__ and
        `Using Keys`__.

        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm
        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm


        :param kms_key_id: The kms_key_id of this VolumeGroupReplicaInfo.
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
