# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeBackupPolicyAssignment(object):
    """
    Specifies that a particular volume backup policy is assigned to an asset such as a volume.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeBackupPolicyAssignment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param asset_id:
            The value to assign to the asset_id property of this VolumeBackupPolicyAssignment.
        :type asset_id: str

        :param id:
            The value to assign to the id property of this VolumeBackupPolicyAssignment.
        :type id: str

        :param policy_id:
            The value to assign to the policy_id property of this VolumeBackupPolicyAssignment.
        :type policy_id: str

        :param time_created:
            The value to assign to the time_created property of this VolumeBackupPolicyAssignment.
        :type time_created: datetime

        """
        self.swagger_types = {
            'asset_id': 'str',
            'id': 'str',
            'policy_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'asset_id': 'assetId',
            'id': 'id',
            'policy_id': 'policyId',
            'time_created': 'timeCreated'
        }

        self._asset_id = None
        self._id = None
        self._policy_id = None
        self._time_created = None

    @property
    def asset_id(self):
        """
        **[Required]** Gets the asset_id of this VolumeBackupPolicyAssignment.
        The OCID of the asset (e.g. a volume) to which the policy has been assigned.


        :return: The asset_id of this VolumeBackupPolicyAssignment.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """
        Sets the asset_id of this VolumeBackupPolicyAssignment.
        The OCID of the asset (e.g. a volume) to which the policy has been assigned.


        :param asset_id: The asset_id of this VolumeBackupPolicyAssignment.
        :type: str
        """
        self._asset_id = asset_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VolumeBackupPolicyAssignment.
        The OCID of the volume backup policy assignment.


        :return: The id of this VolumeBackupPolicyAssignment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeBackupPolicyAssignment.
        The OCID of the volume backup policy assignment.


        :param id: The id of this VolumeBackupPolicyAssignment.
        :type: str
        """
        self._id = id

    @property
    def policy_id(self):
        """
        **[Required]** Gets the policy_id of this VolumeBackupPolicyAssignment.
        The OCID of the volume backup policy that has been assigned to an asset.


        :return: The policy_id of this VolumeBackupPolicyAssignment.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """
        Sets the policy_id of this VolumeBackupPolicyAssignment.
        The OCID of the volume backup policy that has been assigned to an asset.


        :param policy_id: The policy_id of this VolumeBackupPolicyAssignment.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this VolumeBackupPolicyAssignment.
        The date and time the volume backup policy assignment was created. Format defined by RFC3339.


        :return: The time_created of this VolumeBackupPolicyAssignment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VolumeBackupPolicyAssignment.
        The date and time the volume backup policy assignment was created. Format defined by RFC3339.


        :param time_created: The time_created of this VolumeBackupPolicyAssignment.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
