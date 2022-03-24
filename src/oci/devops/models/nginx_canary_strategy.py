# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .oke_canary_strategy import OkeCanaryStrategy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NginxCanaryStrategy(OkeCanaryStrategy):
    """
    Specifies the NGINX canary release strategy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NginxCanaryStrategy object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.NginxCanaryStrategy.strategy_type` attribute
        of this class is ``NGINX_CANARY_STRATEGY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param strategy_type:
            The value to assign to the strategy_type property of this NginxCanaryStrategy.
            Allowed values for this property are: "NGINX_CANARY_STRATEGY"
        :type strategy_type: str

        :param namespace:
            The value to assign to the namespace property of this NginxCanaryStrategy.
        :type namespace: str

        :param ingress_name:
            The value to assign to the ingress_name property of this NginxCanaryStrategy.
        :type ingress_name: str

        """
        self.swagger_types = {
            'strategy_type': 'str',
            'namespace': 'str',
            'ingress_name': 'str'
        }

        self.attribute_map = {
            'strategy_type': 'strategyType',
            'namespace': 'namespace',
            'ingress_name': 'ingressName'
        }

        self._strategy_type = None
        self._namespace = None
        self._ingress_name = None
        self._strategy_type = 'NGINX_CANARY_STRATEGY'

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this NginxCanaryStrategy.
        Canary namespace to be used for Kubernetes canary deployment.


        :return: The namespace of this NginxCanaryStrategy.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this NginxCanaryStrategy.
        Canary namespace to be used for Kubernetes canary deployment.


        :param namespace: The namespace of this NginxCanaryStrategy.
        :type: str
        """
        self._namespace = namespace

    @property
    def ingress_name(self):
        """
        **[Required]** Gets the ingress_name of this NginxCanaryStrategy.
        Name of the Ingress resource.


        :return: The ingress_name of this NginxCanaryStrategy.
        :rtype: str
        """
        return self._ingress_name

    @ingress_name.setter
    def ingress_name(self, ingress_name):
        """
        Sets the ingress_name of this NginxCanaryStrategy.
        Name of the Ingress resource.


        :param ingress_name: The ingress_name of this NginxCanaryStrategy.
        :type: str
        """
        self._ingress_name = ingress_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
