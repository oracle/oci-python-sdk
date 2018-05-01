# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


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

        :param backup:
            The value to assign to the backup property of this UpdateBackendDetails.
        :type backup: bool

        :param drain:
            The value to assign to the drain property of this UpdateBackendDetails.
        :type drain: bool

        :param offline:
            The value to assign to the offline property of this UpdateBackendDetails.
        :type offline: bool

        :param weight:
            The value to assign to the weight property of this UpdateBackendDetails.
        :type weight: int

        """
        self.swagger_types = {
            'backup': 'bool',
            'drain': 'bool',
            'offline': 'bool',
            'weight': 'int'
        }

        self.attribute_map = {
            'backup': 'backup',
            'drain': 'drain',
            'offline': 'offline',
            'weight': 'weight'
        }

        self._backup = None
        self._drain = None
        self._offline = None
        self._weight = None

    @property
    def backup(self):
        """
        **[Required]** Gets the backup of this UpdateBackendDetails.
        Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
        traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy.

        Example: `false`


        :return: The backup of this UpdateBackendDetails.
        :rtype: bool
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        """
        Sets the backup of this UpdateBackendDetails.
        Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
        traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy.

        Example: `false`


        :param backup: The backup of this UpdateBackendDetails.
        :type: bool
        """
        self._backup = backup

    @property
    def drain(self):
        """
        **[Required]** Gets the drain of this UpdateBackendDetails.
        Whether the load balancer should drain this server. Servers marked \"drain\" receive no new
        incoming traffic.

        Example: `false`


        :return: The drain of this UpdateBackendDetails.
        :rtype: bool
        """
        return self._drain

    @drain.setter
    def drain(self, drain):
        """
        Sets the drain of this UpdateBackendDetails.
        Whether the load balancer should drain this server. Servers marked \"drain\" receive no new
        incoming traffic.

        Example: `false`


        :param drain: The drain of this UpdateBackendDetails.
        :type: bool
        """
        self._drain = drain

    @property
    def offline(self):
        """
        **[Required]** Gets the offline of this UpdateBackendDetails.
        Whether the load balancer should treat this server as offline. Offline servers receive no incoming
        traffic.

        Example: `false`


        :return: The offline of this UpdateBackendDetails.
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """
        Sets the offline of this UpdateBackendDetails.
        Whether the load balancer should treat this server as offline. Offline servers receive no incoming
        traffic.

        Example: `false`


        :param offline: The offline of this UpdateBackendDetails.
        :type: bool
        """
        self._offline = offline

    @property
    def weight(self):
        """
        **[Required]** Gets the weight of this UpdateBackendDetails.
        The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
        proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
        as a server weighted '1'.
        For more information on load balancing policies, see
        `How Load Balancing Policies Work`__.

        Example: `3`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Balance/Reference/lbpolicies.htm


        :return: The weight of this UpdateBackendDetails.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this UpdateBackendDetails.
        The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
        proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
        as a server weighted '1'.
        For more information on load balancing policies, see
        `How Load Balancing Policies Work`__.

        Example: `3`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Balance/Reference/lbpolicies.htm


        :param weight: The weight of this UpdateBackendDetails.
        :type: int
        """
        self._weight = weight

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
