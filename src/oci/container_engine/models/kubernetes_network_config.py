# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KubernetesNetworkConfig(object):
    """
    The properties that define the network configuration for Kubernetes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KubernetesNetworkConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pods_cidr:
            The value to assign to the pods_cidr property of this KubernetesNetworkConfig.
        :type pods_cidr: str

        :param services_cidr:
            The value to assign to the services_cidr property of this KubernetesNetworkConfig.
        :type services_cidr: str

        """
        self.swagger_types = {
            'pods_cidr': 'str',
            'services_cidr': 'str'
        }

        self.attribute_map = {
            'pods_cidr': 'podsCidr',
            'services_cidr': 'servicesCidr'
        }

        self._pods_cidr = None
        self._services_cidr = None

    @property
    def pods_cidr(self):
        """
        Gets the pods_cidr of this KubernetesNetworkConfig.
        The CIDR block for Kubernetes pods.


        :return: The pods_cidr of this KubernetesNetworkConfig.
        :rtype: str
        """
        return self._pods_cidr

    @pods_cidr.setter
    def pods_cidr(self, pods_cidr):
        """
        Sets the pods_cidr of this KubernetesNetworkConfig.
        The CIDR block for Kubernetes pods.


        :param pods_cidr: The pods_cidr of this KubernetesNetworkConfig.
        :type: str
        """
        self._pods_cidr = pods_cidr

    @property
    def services_cidr(self):
        """
        Gets the services_cidr of this KubernetesNetworkConfig.
        The CIDR block for Kubernetes services.


        :return: The services_cidr of this KubernetesNetworkConfig.
        :rtype: str
        """
        return self._services_cidr

    @services_cidr.setter
    def services_cidr(self, services_cidr):
        """
        Sets the services_cidr of this KubernetesNetworkConfig.
        The CIDR block for Kubernetes services.


        :param services_cidr: The services_cidr of this KubernetesNetworkConfig.
        :type: str
        """
        self._services_cidr = services_cidr

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
