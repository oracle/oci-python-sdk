# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProxyDetails(object):
    """
    Details of the proxy such as version of the proxy image.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProxyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param proxy_image:
            The value to assign to the proxy_image property of this ProxyDetails.
        :type proxy_image: str

        """
        self.swagger_types = {
            'proxy_image': 'str'
        }

        self.attribute_map = {
            'proxy_image': 'proxyImage'
        }

        self._proxy_image = None

    @property
    def proxy_image(self):
        """
        **[Required]** Gets the proxy_image of this ProxyDetails.
        Proxy container image version to be deployed.


        :return: The proxy_image of this ProxyDetails.
        :rtype: str
        """
        return self._proxy_image

    @proxy_image.setter
    def proxy_image(self, proxy_image):
        """
        Sets the proxy_image of this ProxyDetails.
        Proxy container image version to be deployed.


        :param proxy_image: The proxy_image of this ProxyDetails.
        :type: str
        """
        self._proxy_image = proxy_image

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
