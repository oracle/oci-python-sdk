# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateReplicationPolicyDetails(object):
    """
    The details to create a replication policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateReplicationPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateReplicationPolicyDetails.
        :type name: str

        :param destination_region_name:
            The value to assign to the destination_region_name property of this CreateReplicationPolicyDetails.
        :type destination_region_name: str

        :param destination_bucket_name:
            The value to assign to the destination_bucket_name property of this CreateReplicationPolicyDetails.
        :type destination_bucket_name: str

        """
        self.swagger_types = {
            'name': 'str',
            'destination_region_name': 'str',
            'destination_bucket_name': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'destination_region_name': 'destinationRegionName',
            'destination_bucket_name': 'destinationBucketName'
        }

        self._name = None
        self._destination_region_name = None
        self._destination_bucket_name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateReplicationPolicyDetails.
        The name of the policy. Avoid entering confidential information.


        :return: The name of this CreateReplicationPolicyDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateReplicationPolicyDetails.
        The name of the policy. Avoid entering confidential information.


        :param name: The name of this CreateReplicationPolicyDetails.
        :type: str
        """
        self._name = name

    @property
    def destination_region_name(self):
        """
        **[Required]** Gets the destination_region_name of this CreateReplicationPolicyDetails.
        The destination region to replicate to, for example \"us-ashburn-1\".


        :return: The destination_region_name of this CreateReplicationPolicyDetails.
        :rtype: str
        """
        return self._destination_region_name

    @destination_region_name.setter
    def destination_region_name(self, destination_region_name):
        """
        Sets the destination_region_name of this CreateReplicationPolicyDetails.
        The destination region to replicate to, for example \"us-ashburn-1\".


        :param destination_region_name: The destination_region_name of this CreateReplicationPolicyDetails.
        :type: str
        """
        self._destination_region_name = destination_region_name

    @property
    def destination_bucket_name(self):
        """
        **[Required]** Gets the destination_bucket_name of this CreateReplicationPolicyDetails.
        The bucket to replicate to in the destination region. Replication policy creation does not automatically
        create a destination bucket. Create the destination bucket before creating the policy.


        :return: The destination_bucket_name of this CreateReplicationPolicyDetails.
        :rtype: str
        """
        return self._destination_bucket_name

    @destination_bucket_name.setter
    def destination_bucket_name(self, destination_bucket_name):
        """
        Sets the destination_bucket_name of this CreateReplicationPolicyDetails.
        The bucket to replicate to in the destination region. Replication policy creation does not automatically
        create a destination bucket. Create the destination bucket before creating the policy.


        :param destination_bucket_name: The destination_bucket_name of this CreateReplicationPolicyDetails.
        :type: str
        """
        self._destination_bucket_name = destination_bucket_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
