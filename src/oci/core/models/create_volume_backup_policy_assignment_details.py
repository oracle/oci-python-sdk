# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVolumeBackupPolicyAssignmentDetails(object):
    """
    CreateVolumeBackupPolicyAssignmentDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVolumeBackupPolicyAssignmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param asset_id:
            The value to assign to the asset_id property of this CreateVolumeBackupPolicyAssignmentDetails.
        :type asset_id: str

        :param policy_id:
            The value to assign to the policy_id property of this CreateVolumeBackupPolicyAssignmentDetails.
        :type policy_id: str

        """
        self.swagger_types = {
            'asset_id': 'str',
            'policy_id': 'str'
        }

        self.attribute_map = {
            'asset_id': 'assetId',
            'policy_id': 'policyId'
        }

        self._asset_id = None
        self._policy_id = None

    @property
    def asset_id(self):
        """
        **[Required]** Gets the asset_id of this CreateVolumeBackupPolicyAssignmentDetails.
        The OCID of the volume to assign the policy to.


        :return: The asset_id of this CreateVolumeBackupPolicyAssignmentDetails.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """
        Sets the asset_id of this CreateVolumeBackupPolicyAssignmentDetails.
        The OCID of the volume to assign the policy to.


        :param asset_id: The asset_id of this CreateVolumeBackupPolicyAssignmentDetails.
        :type: str
        """
        self._asset_id = asset_id

    @property
    def policy_id(self):
        """
        **[Required]** Gets the policy_id of this CreateVolumeBackupPolicyAssignmentDetails.
        The OCID of the volume backup policy to assign to the volume.


        :return: The policy_id of this CreateVolumeBackupPolicyAssignmentDetails.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """
        Sets the policy_id of this CreateVolumeBackupPolicyAssignmentDetails.
        The OCID of the volume backup policy to assign to the volume.


        :param policy_id: The policy_id of this CreateVolumeBackupPolicyAssignmentDetails.
        :type: str
        """
        self._policy_id = policy_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
