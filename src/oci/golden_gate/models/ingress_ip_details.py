# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngressIpDetails(object):
    """
    Private Endpoint IP Addresses created in the customer's subnet.
    GoldenGate service will use these ingress IP addresses to send all specific requests initiated from the service.
    These are typically used for accessing customer resources.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IngressIpDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ingress_ip:
            The value to assign to the ingress_ip property of this IngressIpDetails.
        :type ingress_ip: str

        """
        self.swagger_types = {
            'ingress_ip': 'str'
        }

        self.attribute_map = {
            'ingress_ip': 'ingressIp'
        }

        self._ingress_ip = None

    @property
    def ingress_ip(self):
        """
        **[Required]** Gets the ingress_ip of this IngressIpDetails.
        A Private Endpoint IPv4 or IPv6 Address created in the customer's subnet.


        :return: The ingress_ip of this IngressIpDetails.
        :rtype: str
        """
        return self._ingress_ip

    @ingress_ip.setter
    def ingress_ip(self, ingress_ip):
        """
        Sets the ingress_ip of this IngressIpDetails.
        A Private Endpoint IPv4 or IPv6 Address created in the customer's subnet.


        :param ingress_ip: The ingress_ip of this IngressIpDetails.
        :type: str
        """
        self._ingress_ip = ingress_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
