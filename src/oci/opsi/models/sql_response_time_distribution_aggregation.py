# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlResponseTimeDistributionAggregation(object):
    """
    SQL Response time distribution entry.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlResponseTimeDistributionAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bucket_id:
            The value to assign to the bucket_id property of this SqlResponseTimeDistributionAggregation.
        :type bucket_id: str

        :param executions_count:
            The value to assign to the executions_count property of this SqlResponseTimeDistributionAggregation.
        :type executions_count: int

        """
        self.swagger_types = {
            'bucket_id': 'str',
            'executions_count': 'int'
        }

        self.attribute_map = {
            'bucket_id': 'bucketId',
            'executions_count': 'executionsCount'
        }

        self._bucket_id = None
        self._executions_count = None

    @property
    def bucket_id(self):
        """
        **[Required]** Gets the bucket_id of this SqlResponseTimeDistributionAggregation.
        Response time bucket id


        :return: The bucket_id of this SqlResponseTimeDistributionAggregation.
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """
        Sets the bucket_id of this SqlResponseTimeDistributionAggregation.
        Response time bucket id


        :param bucket_id: The bucket_id of this SqlResponseTimeDistributionAggregation.
        :type: str
        """
        self._bucket_id = bucket_id

    @property
    def executions_count(self):
        """
        **[Required]** Gets the executions_count of this SqlResponseTimeDistributionAggregation.
        Total number of SQL executions


        :return: The executions_count of this SqlResponseTimeDistributionAggregation.
        :rtype: int
        """
        return self._executions_count

    @executions_count.setter
    def executions_count(self, executions_count):
        """
        Sets the executions_count of this SqlResponseTimeDistributionAggregation.
        Total number of SQL executions


        :param executions_count: The executions_count of this SqlResponseTimeDistributionAggregation.
        :type: int
        """
        self._executions_count = executions_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
