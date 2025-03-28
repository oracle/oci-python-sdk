# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .launch_create_volume_details import LaunchCreateVolumeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchCreateVolumeFromAttributes(LaunchCreateVolumeDetails):
    """
    The details of the volume to create for CreateVolume operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchCreateVolumeFromAttributes object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.LaunchCreateVolumeFromAttributes.volume_creation_type` attribute
        of this class is ``ATTRIBUTES`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param volume_creation_type:
            The value to assign to the volume_creation_type property of this LaunchCreateVolumeFromAttributes.
            Allowed values for this property are: "ATTRIBUTES"
        :type volume_creation_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LaunchCreateVolumeFromAttributes.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this LaunchCreateVolumeFromAttributes.
        :type display_name: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this LaunchCreateVolumeFromAttributes.
        :type kms_key_id: str

        :param vpus_per_gb:
            The value to assign to the vpus_per_gb property of this LaunchCreateVolumeFromAttributes.
        :type vpus_per_gb: int

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this LaunchCreateVolumeFromAttributes.
        :type size_in_gbs: int

        """
        self.swagger_types = {
            'volume_creation_type': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'kms_key_id': 'str',
            'vpus_per_gb': 'int',
            'size_in_gbs': 'int'
        }
        self.attribute_map = {
            'volume_creation_type': 'volumeCreationType',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'kms_key_id': 'kmsKeyId',
            'vpus_per_gb': 'vpusPerGB',
            'size_in_gbs': 'sizeInGBs'
        }
        self._volume_creation_type = None
        self._compartment_id = None
        self._display_name = None
        self._kms_key_id = None
        self._vpus_per_gb = None
        self._size_in_gbs = None
        self._volume_creation_type = 'ATTRIBUTES'

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this LaunchCreateVolumeFromAttributes.
        The OCID of the compartment that contains the volume. If not provided,
        it will be inherited from the instance.


        :return: The compartment_id of this LaunchCreateVolumeFromAttributes.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LaunchCreateVolumeFromAttributes.
        The OCID of the compartment that contains the volume. If not provided,
        it will be inherited from the instance.


        :param compartment_id: The compartment_id of this LaunchCreateVolumeFromAttributes.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this LaunchCreateVolumeFromAttributes.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this LaunchCreateVolumeFromAttributes.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LaunchCreateVolumeFromAttributes.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this LaunchCreateVolumeFromAttributes.
        :type: str
        """
        self._display_name = display_name

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this LaunchCreateVolumeFromAttributes.
        The OCID of the Vault service key to assign as the master encryption key
        for the volume.


        :return: The kms_key_id of this LaunchCreateVolumeFromAttributes.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this LaunchCreateVolumeFromAttributes.
        The OCID of the Vault service key to assign as the master encryption key
        for the volume.


        :param kms_key_id: The kms_key_id of this LaunchCreateVolumeFromAttributes.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def vpus_per_gb(self):
        """
        Gets the vpus_per_gb of this LaunchCreateVolumeFromAttributes.
        The number of volume performance units (VPUs) that will be applied to this volume per GB,
        representing the Block Volume service's elastic performance options.
        See `Block Volume Performance Levels`__ for more information.

        Allowed values:

          * `0`: Represents Lower Cost option.

          * `10`: Represents Balanced option.

          * `20`: Represents Higher Performance option.

          * `30`-`120`: Represents the Ultra High Performance option.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels


        :return: The vpus_per_gb of this LaunchCreateVolumeFromAttributes.
        :rtype: int
        """
        return self._vpus_per_gb

    @vpus_per_gb.setter
    def vpus_per_gb(self, vpus_per_gb):
        """
        Sets the vpus_per_gb of this LaunchCreateVolumeFromAttributes.
        The number of volume performance units (VPUs) that will be applied to this volume per GB,
        representing the Block Volume service's elastic performance options.
        See `Block Volume Performance Levels`__ for more information.

        Allowed values:

          * `0`: Represents Lower Cost option.

          * `10`: Represents Balanced option.

          * `20`: Represents Higher Performance option.

          * `30`-`120`: Represents the Ultra High Performance option.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels


        :param vpus_per_gb: The vpus_per_gb of this LaunchCreateVolumeFromAttributes.
        :type: int
        """
        self._vpus_per_gb = vpus_per_gb

    @property
    def size_in_gbs(self):
        """
        **[Required]** Gets the size_in_gbs of this LaunchCreateVolumeFromAttributes.
        The size of the volume in GBs.


        :return: The size_in_gbs of this LaunchCreateVolumeFromAttributes.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this LaunchCreateVolumeFromAttributes.
        The size of the volume in GBs.


        :param size_in_gbs: The size_in_gbs of this LaunchCreateVolumeFromAttributes.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
