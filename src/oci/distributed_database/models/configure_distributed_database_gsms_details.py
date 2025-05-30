# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigureDistributedDatabaseGsmsDetails(object):
    """
    Details of the request to configure new global service manager(GSM) instances for the distributed database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigureDistributedDatabaseGsmsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param old_gsm_names:
            The value to assign to the old_gsm_names property of this ConfigureDistributedDatabaseGsmsDetails.
        :type old_gsm_names: list[str]

        :param is_latest_gsm_image:
            The value to assign to the is_latest_gsm_image property of this ConfigureDistributedDatabaseGsmsDetails.
        :type is_latest_gsm_image: bool

        """
        self.swagger_types = {
            'old_gsm_names': 'list[str]',
            'is_latest_gsm_image': 'bool'
        }
        self.attribute_map = {
            'old_gsm_names': 'oldGsmNames',
            'is_latest_gsm_image': 'isLatestGsmImage'
        }
        self._old_gsm_names = None
        self._is_latest_gsm_image = None

    @property
    def old_gsm_names(self):
        """
        **[Required]** Gets the old_gsm_names of this ConfigureDistributedDatabaseGsmsDetails.
        Names of old global service manager(GSM) instances corresponding to which new GSM instances need to be configured.


        :return: The old_gsm_names of this ConfigureDistributedDatabaseGsmsDetails.
        :rtype: list[str]
        """
        return self._old_gsm_names

    @old_gsm_names.setter
    def old_gsm_names(self, old_gsm_names):
        """
        Sets the old_gsm_names of this ConfigureDistributedDatabaseGsmsDetails.
        Names of old global service manager(GSM) instances corresponding to which new GSM instances need to be configured.


        :param old_gsm_names: The old_gsm_names of this ConfigureDistributedDatabaseGsmsDetails.
        :type: list[str]
        """
        self._old_gsm_names = old_gsm_names

    @property
    def is_latest_gsm_image(self):
        """
        **[Required]** Gets the is_latest_gsm_image of this ConfigureDistributedDatabaseGsmsDetails.
        Flag to indicate if new global service manager(GSM) instances shall use latest image or re-use image used by existing
        GSM instances.


        :return: The is_latest_gsm_image of this ConfigureDistributedDatabaseGsmsDetails.
        :rtype: bool
        """
        return self._is_latest_gsm_image

    @is_latest_gsm_image.setter
    def is_latest_gsm_image(self, is_latest_gsm_image):
        """
        Sets the is_latest_gsm_image of this ConfigureDistributedDatabaseGsmsDetails.
        Flag to indicate if new global service manager(GSM) instances shall use latest image or re-use image used by existing
        GSM instances.


        :param is_latest_gsm_image: The is_latest_gsm_image of this ConfigureDistributedDatabaseGsmsDetails.
        :type: bool
        """
        self._is_latest_gsm_image = is_latest_gsm_image

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
