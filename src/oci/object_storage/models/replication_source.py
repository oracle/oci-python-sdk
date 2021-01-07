# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReplicationSource(object):
    """
    The details of a replication source bucket that replicates to a target destination bucket.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReplicationSource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_name:
            The value to assign to the policy_name property of this ReplicationSource.
        :type policy_name: str

        :param source_region_name:
            The value to assign to the source_region_name property of this ReplicationSource.
        :type source_region_name: str

        :param source_bucket_name:
            The value to assign to the source_bucket_name property of this ReplicationSource.
        :type source_bucket_name: str

        """
        self.swagger_types = {
            'policy_name': 'str',
            'source_region_name': 'str',
            'source_bucket_name': 'str'
        }

        self.attribute_map = {
            'policy_name': 'policyName',
            'source_region_name': 'sourceRegionName',
            'source_bucket_name': 'sourceBucketName'
        }

        self._policy_name = None
        self._source_region_name = None
        self._source_bucket_name = None

    @property
    def policy_name(self):
        """
        **[Required]** Gets the policy_name of this ReplicationSource.
        The name of the policy.


        :return: The policy_name of this ReplicationSource.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """
        Sets the policy_name of this ReplicationSource.
        The name of the policy.


        :param policy_name: The policy_name of this ReplicationSource.
        :type: str
        """
        self._policy_name = policy_name

    @property
    def source_region_name(self):
        """
        **[Required]** Gets the source_region_name of this ReplicationSource.
        The source region replicating data from, for example \"us-ashburn-1\".


        :return: The source_region_name of this ReplicationSource.
        :rtype: str
        """
        return self._source_region_name

    @source_region_name.setter
    def source_region_name(self, source_region_name):
        """
        Sets the source_region_name of this ReplicationSource.
        The source region replicating data from, for example \"us-ashburn-1\".


        :param source_region_name: The source_region_name of this ReplicationSource.
        :type: str
        """
        self._source_region_name = source_region_name

    @property
    def source_bucket_name(self):
        """
        **[Required]** Gets the source_bucket_name of this ReplicationSource.
        The source bucket replicating data from.


        :return: The source_bucket_name of this ReplicationSource.
        :rtype: str
        """
        return self._source_bucket_name

    @source_bucket_name.setter
    def source_bucket_name(self, source_bucket_name):
        """
        Sets the source_bucket_name of this ReplicationSource.
        The source bucket replicating data from.


        :param source_bucket_name: The source_bucket_name of this ReplicationSource.
        :type: str
        """
        self._source_bucket_name = source_bucket_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
