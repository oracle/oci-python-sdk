# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdateVolumeBackupDetails(object):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName'
        }

        self._display_name = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateVolumeBackupDetails.
        A friendly user-specified name for the volume backup.
        Avoid entering confidential information.


        :return: The display_name of this UpdateVolumeBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateVolumeBackupDetails.
        A friendly user-specified name for the volume backup.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateVolumeBackupDetails.
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
