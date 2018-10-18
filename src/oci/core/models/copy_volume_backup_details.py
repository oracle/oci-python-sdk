# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CopyVolumeBackupDetails(object):
    """
    CopyVolumeBackupDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CopyVolumeBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination_region:
            The value to assign to the destination_region property of this CopyVolumeBackupDetails.
        :type destination_region: str

        :param display_name:
            The value to assign to the display_name property of this CopyVolumeBackupDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'destination_region': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'destination_region': 'destinationRegion',
            'display_name': 'displayName'
        }

        self._destination_region = None
        self._display_name = None

    @property
    def destination_region(self):
        """
        **[Required]** Gets the destination_region of this CopyVolumeBackupDetails.
        The name of the destination region.

        Example: `us-ashburn-1`


        :return: The destination_region of this CopyVolumeBackupDetails.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """
        Sets the destination_region of this CopyVolumeBackupDetails.
        The name of the destination region.

        Example: `us-ashburn-1`


        :param destination_region: The destination_region of this CopyVolumeBackupDetails.
        :type: str
        """
        self._destination_region = destination_region

    @property
    def display_name(self):
        """
        Gets the display_name of this CopyVolumeBackupDetails.
        A user-friendly name for the volume backup. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CopyVolumeBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CopyVolumeBackupDetails.
        A user-friendly name for the volume backup. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CopyVolumeBackupDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
