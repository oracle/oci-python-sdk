# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableReplicationToRegionDetails(object):
    """
    Domain replication request packet
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnableReplicationToRegionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param replica_region:
            The value to assign to the replica_region property of this EnableReplicationToRegionDetails.
        :type replica_region: str

        """
        self.swagger_types = {
            'replica_region': 'str'
        }

        self.attribute_map = {
            'replica_region': 'replicaRegion'
        }

        self._replica_region = None

    @property
    def replica_region(self):
        """
        Gets the replica_region of this EnableReplicationToRegionDetails.
        A region for which domain replication is requested for.
        See `Regions and Availability Domains`__
        for the full list of supported region names.

        Example: `us-phoenix-1`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :return: The replica_region of this EnableReplicationToRegionDetails.
        :rtype: str
        """
        return self._replica_region

    @replica_region.setter
    def replica_region(self, replica_region):
        """
        Sets the replica_region of this EnableReplicationToRegionDetails.
        A region for which domain replication is requested for.
        See `Regions and Availability Domains`__
        for the full list of supported region names.

        Example: `us-phoenix-1`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :param replica_region: The replica_region of this EnableReplicationToRegionDetails.
        :type: str
        """
        self._replica_region = replica_region

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
