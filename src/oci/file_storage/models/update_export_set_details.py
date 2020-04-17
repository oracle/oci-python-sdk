# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateExportSetDetails(object):
    """
    Details for updating the export set.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateExportSetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateExportSetDetails.
        :type display_name: str

        :param max_fs_stat_bytes:
            The value to assign to the max_fs_stat_bytes property of this UpdateExportSetDetails.
        :type max_fs_stat_bytes: int

        :param max_fs_stat_files:
            The value to assign to the max_fs_stat_files property of this UpdateExportSetDetails.
        :type max_fs_stat_files: int

        """
        self.swagger_types = {
            'display_name': 'str',
            'max_fs_stat_bytes': 'int',
            'max_fs_stat_files': 'int'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'max_fs_stat_bytes': 'maxFsStatBytes',
            'max_fs_stat_files': 'maxFsStatFiles'
        }

        self._display_name = None
        self._max_fs_stat_bytes = None
        self._max_fs_stat_files = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateExportSetDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My export set`


        :return: The display_name of this UpdateExportSetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateExportSetDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My export set`


        :param display_name: The display_name of this UpdateExportSetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def max_fs_stat_bytes(self):
        """
        Gets the max_fs_stat_bytes of this UpdateExportSetDetails.
        Controls the maximum `tbytes`, `fbytes`, and `abytes`
        values reported by `NFS FSSTAT` calls through any associated
        mount targets. This is an advanced feature. For most
        applications, use the default value. The
        `tbytes` value reported by `FSSTAT` will be
        `maxFsStatBytes`. The value of `fbytes` and `abytes` will be
        `maxFsStatBytes` minus the metered size of the file
        system. If the metered size is larger than `maxFsStatBytes`,
        then `fbytes` and `abytes` will both be '0'.


        :return: The max_fs_stat_bytes of this UpdateExportSetDetails.
        :rtype: int
        """
        return self._max_fs_stat_bytes

    @max_fs_stat_bytes.setter
    def max_fs_stat_bytes(self, max_fs_stat_bytes):
        """
        Sets the max_fs_stat_bytes of this UpdateExportSetDetails.
        Controls the maximum `tbytes`, `fbytes`, and `abytes`
        values reported by `NFS FSSTAT` calls through any associated
        mount targets. This is an advanced feature. For most
        applications, use the default value. The
        `tbytes` value reported by `FSSTAT` will be
        `maxFsStatBytes`. The value of `fbytes` and `abytes` will be
        `maxFsStatBytes` minus the metered size of the file
        system. If the metered size is larger than `maxFsStatBytes`,
        then `fbytes` and `abytes` will both be '0'.


        :param max_fs_stat_bytes: The max_fs_stat_bytes of this UpdateExportSetDetails.
        :type: int
        """
        self._max_fs_stat_bytes = max_fs_stat_bytes

    @property
    def max_fs_stat_files(self):
        """
        Gets the max_fs_stat_files of this UpdateExportSetDetails.
        Controls the maximum `ffiles`, `ffiles`, and `afiles`
        values reported by `NFS FSSTAT` calls through any associated
        mount targets. This is an advanced feature. For most
        applications, use the default value. The
        `tfiles` value reported by `FSSTAT` will be
        `maxFsStatFiles`. The value of `ffiles` and `afiles` will be
        `maxFsStatFiles` minus the metered size of the file
        system. If the metered size is larger than `maxFsStatFiles`,
        then `ffiles` and `afiles` will both be '0'.


        :return: The max_fs_stat_files of this UpdateExportSetDetails.
        :rtype: int
        """
        return self._max_fs_stat_files

    @max_fs_stat_files.setter
    def max_fs_stat_files(self, max_fs_stat_files):
        """
        Sets the max_fs_stat_files of this UpdateExportSetDetails.
        Controls the maximum `ffiles`, `ffiles`, and `afiles`
        values reported by `NFS FSSTAT` calls through any associated
        mount targets. This is an advanced feature. For most
        applications, use the default value. The
        `tfiles` value reported by `FSSTAT` will be
        `maxFsStatFiles`. The value of `ffiles` and `afiles` will be
        `maxFsStatFiles` minus the metered size of the file
        system. If the metered size is larger than `maxFsStatFiles`,
        then `ffiles` and `afiles` will both be '0'.


        :param max_fs_stat_files: The max_fs_stat_files of this UpdateExportSetDetails.
        :type: int
        """
        self._max_fs_stat_files = max_fs_stat_files

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
