# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531

from .patching_configs import PatchingConfigs
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BatchingBasedPatchingConfigs(PatchingConfigs):
    """
    Configuration that applies the patch in batches, the batch size is a user defined parameter.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BatchingBasedPatchingConfigs object with values from keyword arguments. The default value of the :py:attr:`~oci.bds.models.BatchingBasedPatchingConfigs.patching_config_strategy` attribute
        of this class is ``BATCHING_BASED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param patching_config_strategy:
            The value to assign to the patching_config_strategy property of this BatchingBasedPatchingConfigs.
            Allowed values for this property are: "DOWNTIME_BASED", "BATCHING_BASED", "DOMAIN_BASED"
        :type patching_config_strategy: str

        :param batch_size:
            The value to assign to the batch_size property of this BatchingBasedPatchingConfigs.
        :type batch_size: int

        :param wait_time_between_batch_in_seconds:
            The value to assign to the wait_time_between_batch_in_seconds property of this BatchingBasedPatchingConfigs.
        :type wait_time_between_batch_in_seconds: int

        :param tolerance_threshold_per_batch:
            The value to assign to the tolerance_threshold_per_batch property of this BatchingBasedPatchingConfigs.
        :type tolerance_threshold_per_batch: int

        """
        self.swagger_types = {
            'patching_config_strategy': 'str',
            'batch_size': 'int',
            'wait_time_between_batch_in_seconds': 'int',
            'tolerance_threshold_per_batch': 'int'
        }
        self.attribute_map = {
            'patching_config_strategy': 'patchingConfigStrategy',
            'batch_size': 'batchSize',
            'wait_time_between_batch_in_seconds': 'waitTimeBetweenBatchInSeconds',
            'tolerance_threshold_per_batch': 'toleranceThresholdPerBatch'
        }
        self._patching_config_strategy = None
        self._batch_size = None
        self._wait_time_between_batch_in_seconds = None
        self._tolerance_threshold_per_batch = None
        self._patching_config_strategy = 'BATCHING_BASED'

    @property
    def batch_size(self):
        """
        **[Required]** Gets the batch_size of this BatchingBasedPatchingConfigs.
        How many nodes to be patched and rebooted in each iteration.


        :return: The batch_size of this BatchingBasedPatchingConfigs.
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """
        Sets the batch_size of this BatchingBasedPatchingConfigs.
        How many nodes to be patched and rebooted in each iteration.


        :param batch_size: The batch_size of this BatchingBasedPatchingConfigs.
        :type: int
        """
        self._batch_size = batch_size

    @property
    def wait_time_between_batch_in_seconds(self):
        """
        **[Required]** Gets the wait_time_between_batch_in_seconds of this BatchingBasedPatchingConfigs.
        The wait time between batches in seconds.


        :return: The wait_time_between_batch_in_seconds of this BatchingBasedPatchingConfigs.
        :rtype: int
        """
        return self._wait_time_between_batch_in_seconds

    @wait_time_between_batch_in_seconds.setter
    def wait_time_between_batch_in_seconds(self, wait_time_between_batch_in_seconds):
        """
        Sets the wait_time_between_batch_in_seconds of this BatchingBasedPatchingConfigs.
        The wait time between batches in seconds.


        :param wait_time_between_batch_in_seconds: The wait_time_between_batch_in_seconds of this BatchingBasedPatchingConfigs.
        :type: int
        """
        self._wait_time_between_batch_in_seconds = wait_time_between_batch_in_seconds

    @property
    def tolerance_threshold_per_batch(self):
        """
        **[Required]** Gets the tolerance_threshold_per_batch of this BatchingBasedPatchingConfigs.
        Acceptable number of failed-to-be-patched nodes in each batch. The maximum number of failed-to-patch nodes cannot exceed 20% of the number of nodes.


        :return: The tolerance_threshold_per_batch of this BatchingBasedPatchingConfigs.
        :rtype: int
        """
        return self._tolerance_threshold_per_batch

    @tolerance_threshold_per_batch.setter
    def tolerance_threshold_per_batch(self, tolerance_threshold_per_batch):
        """
        Sets the tolerance_threshold_per_batch of this BatchingBasedPatchingConfigs.
        Acceptable number of failed-to-be-patched nodes in each batch. The maximum number of failed-to-patch nodes cannot exceed 20% of the number of nodes.


        :param tolerance_threshold_per_batch: The tolerance_threshold_per_batch of this BatchingBasedPatchingConfigs.
        :type: int
        """
        self._tolerance_threshold_per_batch = tolerance_threshold_per_batch

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
