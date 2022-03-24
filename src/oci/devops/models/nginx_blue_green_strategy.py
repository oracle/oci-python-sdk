# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .oke_blue_green_strategy import OkeBlueGreenStrategy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NginxBlueGreenStrategy(OkeBlueGreenStrategy):
    """
    Specifies the NGINX blue green release strategy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NginxBlueGreenStrategy object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.NginxBlueGreenStrategy.strategy_type` attribute
        of this class is ``NGINX_BLUE_GREEN_STRATEGY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param strategy_type:
            The value to assign to the strategy_type property of this NginxBlueGreenStrategy.
            Allowed values for this property are: "NGINX_BLUE_GREEN_STRATEGY"
        :type strategy_type: str

        :param namespace_a:
            The value to assign to the namespace_a property of this NginxBlueGreenStrategy.
        :type namespace_a: str

        :param namespace_b:
            The value to assign to the namespace_b property of this NginxBlueGreenStrategy.
        :type namespace_b: str

        :param ingress_name:
            The value to assign to the ingress_name property of this NginxBlueGreenStrategy.
        :type ingress_name: str

        """
        self.swagger_types = {
            'strategy_type': 'str',
            'namespace_a': 'str',
            'namespace_b': 'str',
            'ingress_name': 'str'
        }

        self.attribute_map = {
            'strategy_type': 'strategyType',
            'namespace_a': 'namespaceA',
            'namespace_b': 'namespaceB',
            'ingress_name': 'ingressName'
        }

        self._strategy_type = None
        self._namespace_a = None
        self._namespace_b = None
        self._ingress_name = None
        self._strategy_type = 'NGINX_BLUE_GREEN_STRATEGY'

    @property
    def namespace_a(self):
        """
        **[Required]** Gets the namespace_a of this NginxBlueGreenStrategy.
        Namespace A for deployment.


        :return: The namespace_a of this NginxBlueGreenStrategy.
        :rtype: str
        """
        return self._namespace_a

    @namespace_a.setter
    def namespace_a(self, namespace_a):
        """
        Sets the namespace_a of this NginxBlueGreenStrategy.
        Namespace A for deployment.


        :param namespace_a: The namespace_a of this NginxBlueGreenStrategy.
        :type: str
        """
        self._namespace_a = namespace_a

    @property
    def namespace_b(self):
        """
        **[Required]** Gets the namespace_b of this NginxBlueGreenStrategy.
        Namespace B for deployment.


        :return: The namespace_b of this NginxBlueGreenStrategy.
        :rtype: str
        """
        return self._namespace_b

    @namespace_b.setter
    def namespace_b(self, namespace_b):
        """
        Sets the namespace_b of this NginxBlueGreenStrategy.
        Namespace B for deployment.


        :param namespace_b: The namespace_b of this NginxBlueGreenStrategy.
        :type: str
        """
        self._namespace_b = namespace_b

    @property
    def ingress_name(self):
        """
        **[Required]** Gets the ingress_name of this NginxBlueGreenStrategy.
        Name of the Ingress resource.


        :return: The ingress_name of this NginxBlueGreenStrategy.
        :rtype: str
        """
        return self._ingress_name

    @ingress_name.setter
    def ingress_name(self, ingress_name):
        """
        Sets the ingress_name of this NginxBlueGreenStrategy.
        Name of the Ingress resource.


        :param ingress_name: The ingress_name of this NginxBlueGreenStrategy.
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
