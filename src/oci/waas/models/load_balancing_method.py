# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoadBalancingMethod(object):
    """
    LoadBalancingMethod model.
    """

    #: A constant which can be used with the method property of a LoadBalancingMethod.
    #: This constant has a value of "IP_HASH"
    METHOD_IP_HASH = "IP_HASH"

    #: A constant which can be used with the method property of a LoadBalancingMethod.
    #: This constant has a value of "ROUND_ROBIN"
    METHOD_ROUND_ROBIN = "ROUND_ROBIN"

    #: A constant which can be used with the method property of a LoadBalancingMethod.
    #: This constant has a value of "STICKY_COOKIE"
    METHOD_STICKY_COOKIE = "STICKY_COOKIE"

    def __init__(self, **kwargs):
        """
        Initializes a new LoadBalancingMethod object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.waas.models.RoundRobinLoadBalancingMethod`
        * :class:`~oci.waas.models.StickyCookieLoadBalancingMethod`
        * :class:`~oci.waas.models.IPHashLoadBalancingMethod`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param method:
            The value to assign to the method property of this LoadBalancingMethod.
            Allowed values for this property are: "IP_HASH", "ROUND_ROBIN", "STICKY_COOKIE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type method: str

        """
        self.swagger_types = {
            'method': 'str'
        }

        self.attribute_map = {
            'method': 'method'
        }

        self._method = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['method']

        if type == 'ROUND_ROBIN':
            return 'RoundRobinLoadBalancingMethod'

        if type == 'STICKY_COOKIE':
            return 'StickyCookieLoadBalancingMethod'

        if type == 'IP_HASH':
            return 'IPHashLoadBalancingMethod'
        else:
            return 'LoadBalancingMethod'

    @property
    def method(self):
        """
        **[Required]** Gets the method of this LoadBalancingMethod.
        Load balancing methods are algorithms used to efficiently distribute traffic among origin servers.

        - **`IP_HASH`__:** All the incoming requests from the same client IP address should go to the same content origination server. IP_HASH load balancing method uses origin weights when choosing which origin should the hash be assigned to initially.

        - **`ROUND_ROBIN`__:** Forwards requests sequentially to the available origin servers. The first request - to the first origin server, the second request - to the next origin server, and so on. After it sends a request to the last origin server, it starts again with the first origin server. When using weights on origins, Weighted Round Robin assigns more requests to origins with a greater weight. Over a period of time, origins will receive a number of requests in proportion to their weight.

        - **`STICKY_COOKIE`__:** Adds a session cookie to the first response from the origin server and identifies the server that sent the response. The client's next request contains the cookie value, and nginx routes the request to the origin server that responded to the first request. STICKY_COOKIE load balancing method falls back to Round Robin for the first request.

        __ https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/IPHashLoadBalancingMethod
        __ https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/RoundRobinLoadBalancingMethod
        __ https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/StickyCookieLoadBalancingMethod

        Allowed values for this property are: "IP_HASH", "ROUND_ROBIN", "STICKY_COOKIE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The method of this LoadBalancingMethod.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this LoadBalancingMethod.
        Load balancing methods are algorithms used to efficiently distribute traffic among origin servers.

        - **`IP_HASH`__:** All the incoming requests from the same client IP address should go to the same content origination server. IP_HASH load balancing method uses origin weights when choosing which origin should the hash be assigned to initially.

        - **`ROUND_ROBIN`__:** Forwards requests sequentially to the available origin servers. The first request - to the first origin server, the second request - to the next origin server, and so on. After it sends a request to the last origin server, it starts again with the first origin server. When using weights on origins, Weighted Round Robin assigns more requests to origins with a greater weight. Over a period of time, origins will receive a number of requests in proportion to their weight.

        - **`STICKY_COOKIE`__:** Adds a session cookie to the first response from the origin server and identifies the server that sent the response. The client's next request contains the cookie value, and nginx routes the request to the origin server that responded to the first request. STICKY_COOKIE load balancing method falls back to Round Robin for the first request.

        __ https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/IPHashLoadBalancingMethod
        __ https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/RoundRobinLoadBalancingMethod
        __ https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/StickyCookieLoadBalancingMethod


        :param method: The method of this LoadBalancingMethod.
        :type: str
        """
        allowed_values = ["IP_HASH", "ROUND_ROBIN", "STICKY_COOKIE"]
        if not value_allowed_none_or_none_sentinel(method, allowed_values):
            method = 'UNKNOWN_ENUM_VALUE'
        self._method = method

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
