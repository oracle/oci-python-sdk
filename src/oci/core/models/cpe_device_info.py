# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CpeDeviceInfo(object):
    """
    Basic information about a particular CPE device type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CpeDeviceInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vendor:
            The value to assign to the vendor property of this CpeDeviceInfo.
        :type vendor: str

        :param platform_software_version:
            The value to assign to the platform_software_version property of this CpeDeviceInfo.
        :type platform_software_version: str

        """
        self.swagger_types = {
            'vendor': 'str',
            'platform_software_version': 'str'
        }

        self.attribute_map = {
            'vendor': 'vendor',
            'platform_software_version': 'platformSoftwareVersion'
        }

        self._vendor = None
        self._platform_software_version = None

    @property
    def vendor(self):
        """
        Gets the vendor of this CpeDeviceInfo.
        The vendor that makes the CPE device.


        :return: The vendor of this CpeDeviceInfo.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this CpeDeviceInfo.
        The vendor that makes the CPE device.


        :param vendor: The vendor of this CpeDeviceInfo.
        :type: str
        """
        self._vendor = vendor

    @property
    def platform_software_version(self):
        """
        Gets the platform_software_version of this CpeDeviceInfo.
        The platform or software version of the CPE device.


        :return: The platform_software_version of this CpeDeviceInfo.
        :rtype: str
        """
        return self._platform_software_version

    @platform_software_version.setter
    def platform_software_version(self, platform_software_version):
        """
        Sets the platform_software_version of this CpeDeviceInfo.
        The platform or software version of the CPE device.


        :param platform_software_version: The platform_software_version of this CpeDeviceInfo.
        :type: str
        """
        self._platform_software_version = platform_software_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
