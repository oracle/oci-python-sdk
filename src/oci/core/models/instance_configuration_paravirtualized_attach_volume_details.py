# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .instance_configuration_attach_volume_details import InstanceConfigurationAttachVolumeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationParavirtualizedAttachVolumeDetails(InstanceConfigurationAttachVolumeDetails):
    """
    InstanceConfigurationParavirtualizedAttachVolumeDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationParavirtualizedAttachVolumeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.InstanceConfigurationParavirtualizedAttachVolumeDetails.type` attribute
        of this class is ``paravirtualized`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        :type display_name: str

        :param is_read_only:
            The value to assign to the is_read_only property of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        :type is_read_only: bool

        :param device:
            The value to assign to the device property of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        :type device: str

        :param is_shareable:
            The value to assign to the is_shareable property of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        :type is_shareable: bool

        :param type:
            The value to assign to the type property of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        :type type: str

        :param is_pv_encryption_in_transit_enabled:
            The value to assign to the is_pv_encryption_in_transit_enabled property of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        :type is_pv_encryption_in_transit_enabled: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'is_read_only': 'bool',
            'device': 'str',
            'is_shareable': 'bool',
            'type': 'str',
            'is_pv_encryption_in_transit_enabled': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'is_read_only': 'isReadOnly',
            'device': 'device',
            'is_shareable': 'isShareable',
            'type': 'type',
            'is_pv_encryption_in_transit_enabled': 'isPvEncryptionInTransitEnabled'
        }

        self._display_name = None
        self._is_read_only = None
        self._device = None
        self._is_shareable = None
        self._type = None
        self._is_pv_encryption_in_transit_enabled = None
        self._type = 'paravirtualized'

    @property
    def is_pv_encryption_in_transit_enabled(self):
        """
        Gets the is_pv_encryption_in_transit_enabled of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.


        :return: The is_pv_encryption_in_transit_enabled of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        :rtype: bool
        """
        return self._is_pv_encryption_in_transit_enabled

    @is_pv_encryption_in_transit_enabled.setter
    def is_pv_encryption_in_transit_enabled(self, is_pv_encryption_in_transit_enabled):
        """
        Sets the is_pv_encryption_in_transit_enabled of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.


        :param is_pv_encryption_in_transit_enabled: The is_pv_encryption_in_transit_enabled of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
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
