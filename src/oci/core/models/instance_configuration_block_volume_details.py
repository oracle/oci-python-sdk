# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationBlockVolumeDetails(object):
    """
    Create new block volumes or attach to an existing volume. Specify either createDetails or volumeId.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationBlockVolumeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attach_details:
            The value to assign to the attach_details property of this InstanceConfigurationBlockVolumeDetails.
        :type attach_details: oci.core.models.InstanceConfigurationAttachVolumeDetails

        :param create_details:
            The value to assign to the create_details property of this InstanceConfigurationBlockVolumeDetails.
        :type create_details: oci.core.models.InstanceConfigurationCreateVolumeDetails

        :param volume_id:
            The value to assign to the volume_id property of this InstanceConfigurationBlockVolumeDetails.
        :type volume_id: str

        """
        self.swagger_types = {
            'attach_details': 'InstanceConfigurationAttachVolumeDetails',
            'create_details': 'InstanceConfigurationCreateVolumeDetails',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'attach_details': 'attachDetails',
            'create_details': 'createDetails',
            'volume_id': 'volumeId'
        }

        self._attach_details = None
        self._create_details = None
        self._volume_id = None

    @property
    def attach_details(self):
        """
        Gets the attach_details of this InstanceConfigurationBlockVolumeDetails.

        :return: The attach_details of this InstanceConfigurationBlockVolumeDetails.
        :rtype: oci.core.models.InstanceConfigurationAttachVolumeDetails
        """
        return self._attach_details

    @attach_details.setter
    def attach_details(self, attach_details):
        """
        Sets the attach_details of this InstanceConfigurationBlockVolumeDetails.

        :param attach_details: The attach_details of this InstanceConfigurationBlockVolumeDetails.
        :type: oci.core.models.InstanceConfigurationAttachVolumeDetails
        """
        self._attach_details = attach_details

    @property
    def create_details(self):
        """
        Gets the create_details of this InstanceConfigurationBlockVolumeDetails.

        :return: The create_details of this InstanceConfigurationBlockVolumeDetails.
        :rtype: oci.core.models.InstanceConfigurationCreateVolumeDetails
        """
        return self._create_details

    @create_details.setter
    def create_details(self, create_details):
        """
        Sets the create_details of this InstanceConfigurationBlockVolumeDetails.

        :param create_details: The create_details of this InstanceConfigurationBlockVolumeDetails.
        :type: oci.core.models.InstanceConfigurationCreateVolumeDetails
        """
        self._create_details = create_details

    @property
    def volume_id(self):
        """
        Gets the volume_id of this InstanceConfigurationBlockVolumeDetails.
        The OCID of the volume.


        :return: The volume_id of this InstanceConfigurationBlockVolumeDetails.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this InstanceConfigurationBlockVolumeDetails.
        The OCID of the volume.


        :param volume_id: The volume_id of this InstanceConfigurationBlockVolumeDetails.
        :type: str
        """
        self._volume_id = volume_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
