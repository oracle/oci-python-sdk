# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_target_asset_details import UpdateTargetAssetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVmTargetAssetDetails(UpdateTargetAssetDetails):
    """
    Description of the VM target asset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVmTargetAssetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_migrations.models.UpdateVmTargetAssetDetails.type` attribute
        of this class is ``INSTANCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateVmTargetAssetDetails.
            Allowed values for this property are: "INSTANCE"
        :type type: str

        :param is_excluded_from_execution:
            The value to assign to the is_excluded_from_execution property of this UpdateVmTargetAssetDetails.
        :type is_excluded_from_execution: bool

        :param preferred_shape_type:
            The value to assign to the preferred_shape_type property of this UpdateVmTargetAssetDetails.
        :type preferred_shape_type: str

        :param block_volumes_performance:
            The value to assign to the block_volumes_performance property of this UpdateVmTargetAssetDetails.
        :type block_volumes_performance: int

        :param ms_license:
            The value to assign to the ms_license property of this UpdateVmTargetAssetDetails.
        :type ms_license: str

        :param user_spec:
            The value to assign to the user_spec property of this UpdateVmTargetAssetDetails.
        :type user_spec: oci.cloud_migrations.models.LaunchInstanceDetails

        """
        self.swagger_types = {
            'type': 'str',
            'is_excluded_from_execution': 'bool',
            'preferred_shape_type': 'str',
            'block_volumes_performance': 'int',
            'ms_license': 'str',
            'user_spec': 'LaunchInstanceDetails'
        }

        self.attribute_map = {
            'type': 'type',
            'is_excluded_from_execution': 'isExcludedFromExecution',
            'preferred_shape_type': 'preferredShapeType',
            'block_volumes_performance': 'blockVolumesPerformance',
            'ms_license': 'msLicense',
            'user_spec': 'userSpec'
        }

        self._type = None
        self._is_excluded_from_execution = None
        self._preferred_shape_type = None
        self._block_volumes_performance = None
        self._ms_license = None
        self._user_spec = None
        self._type = 'INSTANCE'

    @property
    def preferred_shape_type(self):
        """
        Gets the preferred_shape_type of this UpdateVmTargetAssetDetails.
        Preferred VM shape type that you provided.


        :return: The preferred_shape_type of this UpdateVmTargetAssetDetails.
        :rtype: str
        """
        return self._preferred_shape_type

    @preferred_shape_type.setter
    def preferred_shape_type(self, preferred_shape_type):
        """
        Sets the preferred_shape_type of this UpdateVmTargetAssetDetails.
        Preferred VM shape type that you provided.


        :param preferred_shape_type: The preferred_shape_type of this UpdateVmTargetAssetDetails.
        :type: str
        """
        self._preferred_shape_type = preferred_shape_type

    @property
    def block_volumes_performance(self):
        """
        Gets the block_volumes_performance of this UpdateVmTargetAssetDetails.
        Performance of the block volumes.


        :return: The block_volumes_performance of this UpdateVmTargetAssetDetails.
        :rtype: int
        """
        return self._block_volumes_performance

    @block_volumes_performance.setter
    def block_volumes_performance(self, block_volumes_performance):
        """
        Sets the block_volumes_performance of this UpdateVmTargetAssetDetails.
        Performance of the block volumes.


        :param block_volumes_performance: The block_volumes_performance of this UpdateVmTargetAssetDetails.
        :type: int
        """
        self._block_volumes_performance = block_volumes_performance

    @property
    def ms_license(self):
        """
        Gets the ms_license of this UpdateVmTargetAssetDetails.
        Microsoft license for VM configuration.


        :return: The ms_license of this UpdateVmTargetAssetDetails.
        :rtype: str
        """
        return self._ms_license

    @ms_license.setter
    def ms_license(self, ms_license):
        """
        Sets the ms_license of this UpdateVmTargetAssetDetails.
        Microsoft license for VM configuration.


        :param ms_license: The ms_license of this UpdateVmTargetAssetDetails.
        :type: str
        """
        self._ms_license = ms_license

    @property
    def user_spec(self):
        """
        Gets the user_spec of this UpdateVmTargetAssetDetails.

        :return: The user_spec of this UpdateVmTargetAssetDetails.
        :rtype: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        return self._user_spec

    @user_spec.setter
    def user_spec(self, user_spec):
        """
        Sets the user_spec of this UpdateVmTargetAssetDetails.

        :param user_spec: The user_spec of this UpdateVmTargetAssetDetails.
        :type: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        self._user_spec = user_spec

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
