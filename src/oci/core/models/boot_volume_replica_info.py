# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BootVolumeReplicaInfo(object):
    """
    Information about the boot volume replica in the destination availability domain.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BootVolumeReplicaInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this BootVolumeReplicaInfo.
        :type display_name: str

        :param boot_volume_replica_id:
            The value to assign to the boot_volume_replica_id property of this BootVolumeReplicaInfo.
        :type boot_volume_replica_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this BootVolumeReplicaInfo.
        :type availability_domain: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'boot_volume_replica_id': 'str',
            'availability_domain': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'boot_volume_replica_id': 'bootVolumeReplicaId',
            'availability_domain': 'availabilityDomain'
        }

        self._display_name = None
        self._boot_volume_replica_id = None
        self._availability_domain = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BootVolumeReplicaInfo.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this BootVolumeReplicaInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BootVolumeReplicaInfo.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this BootVolumeReplicaInfo.
        :type: str
        """
        self._display_name = display_name

    @property
    def boot_volume_replica_id(self):
        """
        **[Required]** Gets the boot_volume_replica_id of this BootVolumeReplicaInfo.
        The boot volume replica's Oracle ID (OCID).


        :return: The boot_volume_replica_id of this BootVolumeReplicaInfo.
        :rtype: str
        """
        return self._boot_volume_replica_id

    @boot_volume_replica_id.setter
    def boot_volume_replica_id(self, boot_volume_replica_id):
        """
        Sets the boot_volume_replica_id of this BootVolumeReplicaInfo.
        The boot volume replica's Oracle ID (OCID).


        :param boot_volume_replica_id: The boot_volume_replica_id of this BootVolumeReplicaInfo.
        :type: str
        """
        self._boot_volume_replica_id = boot_volume_replica_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this BootVolumeReplicaInfo.
        The availability domain of the boot volume replica.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this BootVolumeReplicaInfo.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this BootVolumeReplicaInfo.
        The availability domain of the boot volume replica.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this BootVolumeReplicaInfo.
        :type: str
        """
        self._availability_domain = availability_domain

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
