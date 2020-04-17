# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachBootVolumeDetails(object):
    """
    AttachBootVolumeDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachBootVolumeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param boot_volume_id:
            The value to assign to the boot_volume_id property of this AttachBootVolumeDetails.
        :type boot_volume_id: str

        :param display_name:
            The value to assign to the display_name property of this AttachBootVolumeDetails.
        :type display_name: str

        :param instance_id:
            The value to assign to the instance_id property of this AttachBootVolumeDetails.
        :type instance_id: str

        """
        self.swagger_types = {
            'boot_volume_id': 'str',
            'display_name': 'str',
            'instance_id': 'str'
        }

        self.attribute_map = {
            'boot_volume_id': 'bootVolumeId',
            'display_name': 'displayName',
            'instance_id': 'instanceId'
        }

        self._boot_volume_id = None
        self._display_name = None
        self._instance_id = None

    @property
    def boot_volume_id(self):
        """
        **[Required]** Gets the boot_volume_id of this AttachBootVolumeDetails.
        The OCID of the  boot volume.


        :return: The boot_volume_id of this AttachBootVolumeDetails.
        :rtype: str
        """
        return self._boot_volume_id

    @boot_volume_id.setter
    def boot_volume_id(self, boot_volume_id):
        """
        Sets the boot_volume_id of this AttachBootVolumeDetails.
        The OCID of the  boot volume.


        :param boot_volume_id: The boot_volume_id of this AttachBootVolumeDetails.
        :type: str
        """
        self._boot_volume_id = boot_volume_id

    @property
    def display_name(self):
        """
        Gets the display_name of this AttachBootVolumeDetails.
        A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.


        :return: The display_name of this AttachBootVolumeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AttachBootVolumeDetails.
        A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.


        :param display_name: The display_name of this AttachBootVolumeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this AttachBootVolumeDetails.
        The OCID of the instance.


        :return: The instance_id of this AttachBootVolumeDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this AttachBootVolumeDetails.
        The OCID of the instance.


        :param instance_id: The instance_id of this AttachBootVolumeDetails.
        :type: str
        """
        self._instance_id = instance_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
