# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReplicatedRegionDetails(object):
    """
    (For tenancies that support identity domains) Properties for a region where a replica for the identity domain exists.
    """

    #: A constant which can be used with the state property of a ReplicatedRegionDetails.
    #: This constant has a value of "ENABLING_REPLICATION"
    STATE_ENABLING_REPLICATION = "ENABLING_REPLICATION"

    #: A constant which can be used with the state property of a ReplicatedRegionDetails.
    #: This constant has a value of "REPLICATION_ENABLED"
    STATE_REPLICATION_ENABLED = "REPLICATION_ENABLED"

    #: A constant which can be used with the state property of a ReplicatedRegionDetails.
    #: This constant has a value of "DISABLING_REPLICATION"
    STATE_DISABLING_REPLICATION = "DISABLING_REPLICATION"

    #: A constant which can be used with the state property of a ReplicatedRegionDetails.
    #: This constant has a value of "REPLICATION_DISABLED"
    STATE_REPLICATION_DISABLED = "REPLICATION_DISABLED"

    #: A constant which can be used with the state property of a ReplicatedRegionDetails.
    #: This constant has a value of "DELETED"
    STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ReplicatedRegionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region:
            The value to assign to the region property of this ReplicatedRegionDetails.
        :type region: str

        :param url:
            The value to assign to the url property of this ReplicatedRegionDetails.
        :type url: str

        :param state:
            The value to assign to the state property of this ReplicatedRegionDetails.
            Allowed values for this property are: "ENABLING_REPLICATION", "REPLICATION_ENABLED", "DISABLING_REPLICATION", "REPLICATION_DISABLED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        """
        self.swagger_types = {
            'region': 'str',
            'url': 'str',
            'state': 'str'
        }

        self.attribute_map = {
            'region': 'region',
            'url': 'url',
            'state': 'state'
        }

        self._region = None
        self._url = None
        self._state = None

    @property
    def region(self):
        """
        Gets the region of this ReplicatedRegionDetails.
        A REPLICATION_ENABLED region, e.g. us-ashburn-1.
        See `Regions and Availability Domains`__
        for the full list of supported region names.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :return: The region of this ReplicatedRegionDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this ReplicatedRegionDetails.
        A REPLICATION_ENABLED region, e.g. us-ashburn-1.
        See `Regions and Availability Domains`__
        for the full list of supported region names.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :param region: The region of this ReplicatedRegionDetails.
        :type: str
        """
        self._region = region

    @property
    def url(self):
        """
        Gets the url of this ReplicatedRegionDetails.
        Region-agnostic identity domain URL.


        :return: The url of this ReplicatedRegionDetails.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ReplicatedRegionDetails.
        Region-agnostic identity domain URL.


        :param url: The url of this ReplicatedRegionDetails.
        :type: str
        """
        self._url = url

    @property
    def state(self):
        """
        Gets the state of this ReplicatedRegionDetails.
        The IDCS-replicated region state.

        Allowed values for this property are: "ENABLING_REPLICATION", "REPLICATION_ENABLED", "DISABLING_REPLICATION", "REPLICATION_DISABLED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this ReplicatedRegionDetails.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ReplicatedRegionDetails.
        The IDCS-replicated region state.


        :param state: The state of this ReplicatedRegionDetails.
        :type: str
        """
        allowed_values = ["ENABLING_REPLICATION", "REPLICATION_ENABLED", "DISABLING_REPLICATION", "REPLICATION_DISABLED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
