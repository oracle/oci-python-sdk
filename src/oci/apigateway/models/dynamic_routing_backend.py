# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .api_specification_route_backend import ApiSpecificationRouteBackend
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DynamicRoutingBackend(ApiSpecificationRouteBackend):
    """
    Send the request to the backend dynamically selected based on the incoming request's context.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DynamicRoutingBackend object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.DynamicRoutingBackend.type` attribute
        of this class is ``DYNAMIC_ROUTING_BACKEND`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DynamicRoutingBackend.
            Allowed values for this property are: "ORACLE_FUNCTIONS_BACKEND", "HTTP_BACKEND", "STOCK_RESPONSE_BACKEND", "DYNAMIC_ROUTING_BACKEND", "OAUTH2_LOGOUT_BACKEND"
        :type type: str

        :param selection_source:
            The value to assign to the selection_source property of this DynamicRoutingBackend.
        :type selection_source: oci.apigateway.models.SelectionSourcePolicy

        :param routing_backends:
            The value to assign to the routing_backends property of this DynamicRoutingBackend.
        :type routing_backends: list[oci.apigateway.models.DynamicRoutingTypeRoutingBackend]

        """
        self.swagger_types = {
            'type': 'str',
            'selection_source': 'SelectionSourcePolicy',
            'routing_backends': 'list[DynamicRoutingTypeRoutingBackend]'
        }

        self.attribute_map = {
            'type': 'type',
            'selection_source': 'selectionSource',
            'routing_backends': 'routingBackends'
        }

        self._type = None
        self._selection_source = None
        self._routing_backends = None
        self._type = 'DYNAMIC_ROUTING_BACKEND'

    @property
    def selection_source(self):
        """
        **[Required]** Gets the selection_source of this DynamicRoutingBackend.

        :return: The selection_source of this DynamicRoutingBackend.
        :rtype: oci.apigateway.models.SelectionSourcePolicy
        """
        return self._selection_source

    @selection_source.setter
    def selection_source(self, selection_source):
        """
        Sets the selection_source of this DynamicRoutingBackend.

        :param selection_source: The selection_source of this DynamicRoutingBackend.
        :type: oci.apigateway.models.SelectionSourcePolicy
        """
        self._selection_source = selection_source

    @property
    def routing_backends(self):
        """
        **[Required]** Gets the routing_backends of this DynamicRoutingBackend.
        List of backends to chose from for Dynamic Routing.


        :return: The routing_backends of this DynamicRoutingBackend.
        :rtype: list[oci.apigateway.models.DynamicRoutingTypeRoutingBackend]
        """
        return self._routing_backends

    @routing_backends.setter
    def routing_backends(self, routing_backends):
        """
        Sets the routing_backends of this DynamicRoutingBackend.
        List of backends to chose from for Dynamic Routing.


        :param routing_backends: The routing_backends of this DynamicRoutingBackend.
        :type: list[oci.apigateway.models.DynamicRoutingTypeRoutingBackend]
        """
        self._routing_backends = routing_backends

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
