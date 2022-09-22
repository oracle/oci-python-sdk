# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReplicationEstimate(object):
    """
    Details for response from replication estimation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReplicationEstimate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param change_rate_in_m_bps:
            The value to assign to the change_rate_in_m_bps property of this ReplicationEstimate.
        :type change_rate_in_m_bps: int

        :param is_replication_supported:
            The value to assign to the is_replication_supported property of this ReplicationEstimate.
        :type is_replication_supported: bool

        :param minimum_supported_interval_in_minutes:
            The value to assign to the minimum_supported_interval_in_minutes property of this ReplicationEstimate.
        :type minimum_supported_interval_in_minutes: int

        :param estimated_base_copy_time_in_minutes:
            The value to assign to the estimated_base_copy_time_in_minutes property of this ReplicationEstimate.
        :type estimated_base_copy_time_in_minutes: int

        :param allowed_target_regions:
            The value to assign to the allowed_target_regions property of this ReplicationEstimate.
        :type allowed_target_regions: list[str]

        """
        self.swagger_types = {
            'change_rate_in_m_bps': 'int',
            'is_replication_supported': 'bool',
            'minimum_supported_interval_in_minutes': 'int',
            'estimated_base_copy_time_in_minutes': 'int',
            'allowed_target_regions': 'list[str]'
        }

        self.attribute_map = {
            'change_rate_in_m_bps': 'changeRateInMBps',
            'is_replication_supported': 'isReplicationSupported',
            'minimum_supported_interval_in_minutes': 'minimumSupportedIntervalInMinutes',
            'estimated_base_copy_time_in_minutes': 'estimatedBaseCopyTimeInMinutes',
            'allowed_target_regions': 'allowedTargetRegions'
        }

        self._change_rate_in_m_bps = None
        self._is_replication_supported = None
        self._minimum_supported_interval_in_minutes = None
        self._estimated_base_copy_time_in_minutes = None
        self._allowed_target_regions = None

    @property
    def change_rate_in_m_bps(self):
        """
        **[Required]** Gets the change_rate_in_m_bps of this ReplicationEstimate.
        The rate of change on source filesystem which was used to provide the estimate in MegaBytes per second.


        :return: The change_rate_in_m_bps of this ReplicationEstimate.
        :rtype: int
        """
        return self._change_rate_in_m_bps

    @change_rate_in_m_bps.setter
    def change_rate_in_m_bps(self, change_rate_in_m_bps):
        """
        Sets the change_rate_in_m_bps of this ReplicationEstimate.
        The rate of change on source filesystem which was used to provide the estimate in MegaBytes per second.


        :param change_rate_in_m_bps: The change_rate_in_m_bps of this ReplicationEstimate.
        :type: int
        """
        self._change_rate_in_m_bps = change_rate_in_m_bps

    @property
    def is_replication_supported(self):
        """
        **[Required]** Gets the is_replication_supported of this ReplicationEstimate.
        Specifies whether replication can be enabled on the file system.


        :return: The is_replication_supported of this ReplicationEstimate.
        :rtype: bool
        """
        return self._is_replication_supported

    @is_replication_supported.setter
    def is_replication_supported(self, is_replication_supported):
        """
        Sets the is_replication_supported of this ReplicationEstimate.
        Specifies whether replication can be enabled on the file system.


        :param is_replication_supported: The is_replication_supported of this ReplicationEstimate.
        :type: bool
        """
        self._is_replication_supported = is_replication_supported

    @property
    def minimum_supported_interval_in_minutes(self):
        """
        **[Required]** Gets the minimum_supported_interval_in_minutes of this ReplicationEstimate.
        The minimum supported replication interval for specified file system in minutes.


        :return: The minimum_supported_interval_in_minutes of this ReplicationEstimate.
        :rtype: int
        """
        return self._minimum_supported_interval_in_minutes

    @minimum_supported_interval_in_minutes.setter
    def minimum_supported_interval_in_minutes(self, minimum_supported_interval_in_minutes):
        """
        Sets the minimum_supported_interval_in_minutes of this ReplicationEstimate.
        The minimum supported replication interval for specified file system in minutes.


        :param minimum_supported_interval_in_minutes: The minimum_supported_interval_in_minutes of this ReplicationEstimate.
        :type: int
        """
        self._minimum_supported_interval_in_minutes = minimum_supported_interval_in_minutes

    @property
    def estimated_base_copy_time_in_minutes(self):
        """
        **[Required]** Gets the estimated_base_copy_time_in_minutes of this ReplicationEstimate.
        The approximate time required for the base sync between source and target to finish.


        :return: The estimated_base_copy_time_in_minutes of this ReplicationEstimate.
        :rtype: int
        """
        return self._estimated_base_copy_time_in_minutes

    @estimated_base_copy_time_in_minutes.setter
    def estimated_base_copy_time_in_minutes(self, estimated_base_copy_time_in_minutes):
        """
        Sets the estimated_base_copy_time_in_minutes of this ReplicationEstimate.
        The approximate time required for the base sync between source and target to finish.


        :param estimated_base_copy_time_in_minutes: The estimated_base_copy_time_in_minutes of this ReplicationEstimate.
        :type: int
        """
        self._estimated_base_copy_time_in_minutes = estimated_base_copy_time_in_minutes

    @property
    def allowed_target_regions(self):
        """
        **[Required]** Gets the allowed_target_regions of this ReplicationEstimate.
        Array of allowed target region names which can be paired with source file system.


        :return: The allowed_target_regions of this ReplicationEstimate.
        :rtype: list[str]
        """
        return self._allowed_target_regions

    @allowed_target_regions.setter
    def allowed_target_regions(self, allowed_target_regions):
        """
        Sets the allowed_target_regions of this ReplicationEstimate.
        Array of allowed target region names which can be paired with source file system.


        :param allowed_target_regions: The allowed_target_regions of this ReplicationEstimate.
        :type: list[str]
        """
        self._allowed_target_regions = allowed_target_regions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
