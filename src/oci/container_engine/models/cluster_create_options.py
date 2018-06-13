# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterCreateOptions(object):
    """
    The properties that define extra options for a cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterCreateOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param service_lb_subnet_ids:
            The value to assign to the service_lb_subnet_ids property of this ClusterCreateOptions.
        :type service_lb_subnet_ids: list[str]

        :param kubernetes_network_config:
            The value to assign to the kubernetes_network_config property of this ClusterCreateOptions.
        :type kubernetes_network_config: KubernetesNetworkConfig

        :param add_ons:
            The value to assign to the add_ons property of this ClusterCreateOptions.
        :type add_ons: AddOnOptions

        """
        self.swagger_types = {
            'service_lb_subnet_ids': 'list[str]',
            'kubernetes_network_config': 'KubernetesNetworkConfig',
            'add_ons': 'AddOnOptions'
        }

        self.attribute_map = {
            'service_lb_subnet_ids': 'serviceLbSubnetIds',
            'kubernetes_network_config': 'kubernetesNetworkConfig',
            'add_ons': 'addOns'
        }

        self._service_lb_subnet_ids = None
        self._kubernetes_network_config = None
        self._add_ons = None

    @property
    def service_lb_subnet_ids(self):
        """
        Gets the service_lb_subnet_ids of this ClusterCreateOptions.
        The OCIDs of the subnets used for Kubernetes services load balancers.


        :return: The service_lb_subnet_ids of this ClusterCreateOptions.
        :rtype: list[str]
        """
        return self._service_lb_subnet_ids

    @service_lb_subnet_ids.setter
    def service_lb_subnet_ids(self, service_lb_subnet_ids):
        """
        Sets the service_lb_subnet_ids of this ClusterCreateOptions.
        The OCIDs of the subnets used for Kubernetes services load balancers.


        :param service_lb_subnet_ids: The service_lb_subnet_ids of this ClusterCreateOptions.
        :type: list[str]
        """
        self._service_lb_subnet_ids = service_lb_subnet_ids

    @property
    def kubernetes_network_config(self):
        """
        Gets the kubernetes_network_config of this ClusterCreateOptions.
        Network configuration for Kubernetes.


        :return: The kubernetes_network_config of this ClusterCreateOptions.
        :rtype: KubernetesNetworkConfig
        """
        return self._kubernetes_network_config

    @kubernetes_network_config.setter
    def kubernetes_network_config(self, kubernetes_network_config):
        """
        Sets the kubernetes_network_config of this ClusterCreateOptions.
        Network configuration for Kubernetes.


        :param kubernetes_network_config: The kubernetes_network_config of this ClusterCreateOptions.
        :type: KubernetesNetworkConfig
        """
        self._kubernetes_network_config = kubernetes_network_config

    @property
    def add_ons(self):
        """
        Gets the add_ons of this ClusterCreateOptions.
        Configurable cluster add-ons


        :return: The add_ons of this ClusterCreateOptions.
        :rtype: AddOnOptions
        """
        return self._add_ons

    @add_ons.setter
    def add_ons(self, add_ons):
        """
        Sets the add_ons of this ClusterCreateOptions.
        Configurable cluster add-ons


        :param add_ons: The add_ons of this ClusterCreateOptions.
        :type: AddOnOptions
        """
        self._add_ons = add_ons

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
