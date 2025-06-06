# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .launch_attach_volume_details import LaunchAttachVolumeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchAttachParavirtualizedVolumeDetails(LaunchAttachVolumeDetails):
    """
    Details specific to PV type volume attachments.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchAttachParavirtualizedVolumeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.LaunchAttachParavirtualizedVolumeDetails.type` attribute
        of this class is ``paravirtualized`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param device:
            The value to assign to the device property of this LaunchAttachParavirtualizedVolumeDetails.
        :type device: str

        :param display_name:
            The value to assign to the display_name property of this LaunchAttachParavirtualizedVolumeDetails.
        :type display_name: str

        :param is_read_only:
            The value to assign to the is_read_only property of this LaunchAttachParavirtualizedVolumeDetails.
        :type is_read_only: bool

        :param is_shareable:
            The value to assign to the is_shareable property of this LaunchAttachParavirtualizedVolumeDetails.
        :type is_shareable: bool

        :param type:
            The value to assign to the type property of this LaunchAttachParavirtualizedVolumeDetails.
        :type type: str

        :param volume_id:
            The value to assign to the volume_id property of this LaunchAttachParavirtualizedVolumeDetails.
        :type volume_id: str

        :param launch_create_volume_details:
            The value to assign to the launch_create_volume_details property of this LaunchAttachParavirtualizedVolumeDetails.
        :type launch_create_volume_details: oci.core.models.LaunchCreateVolumeDetails

        :param is_pv_encryption_in_transit_enabled:
            The value to assign to the is_pv_encryption_in_transit_enabled property of this LaunchAttachParavirtualizedVolumeDetails.
        :type is_pv_encryption_in_transit_enabled: bool

        """
        self.swagger_types = {
            'device': 'str',
            'display_name': 'str',
            'is_read_only': 'bool',
            'is_shareable': 'bool',
            'type': 'str',
            'volume_id': 'str',
            'launch_create_volume_details': 'LaunchCreateVolumeDetails',
            'is_pv_encryption_in_transit_enabled': 'bool'
        }
        self.attribute_map = {
            'device': 'device',
            'display_name': 'displayName',
            'is_read_only': 'isReadOnly',
            'is_shareable': 'isShareable',
            'type': 'type',
            'volume_id': 'volumeId',
            'launch_create_volume_details': 'launchCreateVolumeDetails',
            'is_pv_encryption_in_transit_enabled': 'isPvEncryptionInTransitEnabled'
        }
        self._device = None
        self._display_name = None
        self._is_read_only = None
        self._is_shareable = None
        self._type = None
        self._volume_id = None
        self._launch_create_volume_details = None
        self._is_pv_encryption_in_transit_enabled = None
        self._type = 'paravirtualized'

    @property
    def is_pv_encryption_in_transit_enabled(self):
        """
        Gets the is_pv_encryption_in_transit_enabled of this LaunchAttachParavirtualizedVolumeDetails.
        Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.


        :return: The is_pv_encryption_in_transit_enabled of this LaunchAttachParavirtualizedVolumeDetails.
        :rtype: bool
        """
        return self._is_pv_encryption_in_transit_enabled

    @is_pv_encryption_in_transit_enabled.setter
    def is_pv_encryption_in_transit_enabled(self, is_pv_encryption_in_transit_enabled):
        """
        Sets the is_pv_encryption_in_transit_enabled of this LaunchAttachParavirtualizedVolumeDetails.
        Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.


        :param is_pv_encryption_in_transit_enabled: The is_pv_encryption_in_transit_enabled of this LaunchAttachParavirtualizedVolumeDetails.
        :type: bool
        """
        self._is_pv_encryption_in_transit_enabled = is_pv_encryption_in_transit_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
