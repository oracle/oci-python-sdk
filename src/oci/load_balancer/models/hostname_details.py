# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostnameDetails(object):
    """
    The details of a hostname resource associated with a load balancer.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostnameDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this HostnameDetails.
        :type name: str

        :param hostname:
            The value to assign to the hostname property of this HostnameDetails.
        :type hostname: str

        """
        self.swagger_types = {
            'name': 'str',
            'hostname': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'hostname': 'hostname'
        }

        self._name = None
        self._hostname = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this HostnameDetails.
        The name of the hostname resource.

        Example: `example_hostname_001`


        :return: The name of this HostnameDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HostnameDetails.
        The name of the hostname resource.

        Example: `example_hostname_001`


        :param name: The name of this HostnameDetails.
        :type: str
        """
        self._name = name

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this HostnameDetails.
        A virtual hostname. For more information about virtual hostname string construction, see
        `Managing Request Routing`__.

        Example: `app.example.com`

        __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm#routing


        :return: The hostname of this HostnameDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this HostnameDetails.
        A virtual hostname. For more information about virtual hostname string construction, see
        `Managing Request Routing`__.

        Example: `app.example.com`

        __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm#routing


        :param hostname: The hostname of this HostnameDetails.
        :type: str
        """
        self._hostname = hostname

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
