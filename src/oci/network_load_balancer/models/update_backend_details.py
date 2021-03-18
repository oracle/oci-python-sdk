# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBackendDetails(object):
    """
    The configuration details for updating a backend server.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBackendDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param weight:
            The value to assign to the weight property of this UpdateBackendDetails.
        :type weight: int

        :param is_backup:
            The value to assign to the is_backup property of this UpdateBackendDetails.
        :type is_backup: bool

        :param is_drain:
            The value to assign to the is_drain property of this UpdateBackendDetails.
        :type is_drain: bool

        :param is_offline:
            The value to assign to the is_offline property of this UpdateBackendDetails.
        :type is_offline: bool

        """
        self.swagger_types = {
            'weight': 'int',
            'is_backup': 'bool',
            'is_drain': 'bool',
            'is_offline': 'bool'
        }

        self.attribute_map = {
            'weight': 'weight',
            'is_backup': 'isBackup',
            'is_drain': 'isDrain',
            'is_offline': 'isOffline'
        }

        self._weight = None
        self._is_backup = None
        self._is_drain = None
        self._is_offline = None

    @property
    def weight(self):
        """
        Gets the weight of this UpdateBackendDetails.
        The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
        proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections
        as a server weighted '1'.
        For more information about load balancing policies, see
        `How Load Balancing Policies Work`__.

        Example: `3`

        __ https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm


        :return: The weight of this UpdateBackendDetails.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this UpdateBackendDetails.
        The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
        proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections
        as a server weighted '1'.
        For more information about load balancing policies, see
        `How Load Balancing Policies Work`__.

        Example: `3`

        __ https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm


        :param weight: The weight of this UpdateBackendDetails.
        :type: int
        """
        self._weight = weight

    @property
    def is_backup(self):
        """
        Gets the is_backup of this UpdateBackendDetails.
        Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress
        traffic to this backend server unless all other backend servers not marked as \"isBackup\" fail the health check policy.

        Example: `false`


        :return: The is_backup of this UpdateBackendDetails.
        :rtype: bool
        """
        return self._is_backup

    @is_backup.setter
    def is_backup(self, is_backup):
        """
        Sets the is_backup of this UpdateBackendDetails.
        Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress
        traffic to this backend server unless all other backend servers not marked as \"isBackup\" fail the health check policy.

        Example: `false`


        :param is_backup: The is_backup of this UpdateBackendDetails.
        :type: bool
        """
        self._is_backup = is_backup

    @property
    def is_drain(self):
        """
        Gets the is_drain of this UpdateBackendDetails.
        Whether the network load balancer should drain this server. Servers marked \"isDrain\" receive no
        incoming traffic.

        Example: `false`


        :return: The is_drain of this UpdateBackendDetails.
        :rtype: bool
        """
        return self._is_drain

    @is_drain.setter
    def is_drain(self, is_drain):
        """
        Sets the is_drain of this UpdateBackendDetails.
        Whether the network load balancer should drain this server. Servers marked \"isDrain\" receive no
        incoming traffic.

        Example: `false`


        :param is_drain: The is_drain of this UpdateBackendDetails.
        :type: bool
        """
        self._is_drain = is_drain

    @property
    def is_offline(self):
        """
        Gets the is_offline of this UpdateBackendDetails.
        Whether the network load balancer should treat this server as offline. Offline servers receive no incoming
        traffic.

        Example: `false`


        :return: The is_offline of this UpdateBackendDetails.
        :rtype: bool
        """
        return self._is_offline

    @is_offline.setter
    def is_offline(self, is_offline):
        """
        Sets the is_offline of this UpdateBackendDetails.
        Whether the network load balancer should treat this server as offline. Offline servers receive no incoming
        traffic.

        Example: `false`


        :param is_offline: The is_offline of this UpdateBackendDetails.
        :type: bool
        """
        self._is_offline = is_offline

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
