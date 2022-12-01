# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DynamicRoutingTypeRoutingBackend(object):
    """
    Policy for the details regarding each routing backend under dynamic routing. We specify the value of selectors for which this routing backend must be selected for a request under keys. We specify the configuration details of routing backend under backend.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DynamicRoutingTypeRoutingBackend object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DynamicRoutingTypeRoutingBackend.
        :type key: oci.apigateway.models.DynamicSelectionKey

        :param backend:
            The value to assign to the backend property of this DynamicRoutingTypeRoutingBackend.
        :type backend: oci.apigateway.models.ApiSpecificationRouteBackend

        """
        self.swagger_types = {
            'key': 'DynamicSelectionKey',
            'backend': 'ApiSpecificationRouteBackend'
        }

        self.attribute_map = {
            'key': 'key',
            'backend': 'backend'
        }

        self._key = None
        self._backend = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this DynamicRoutingTypeRoutingBackend.

        :return: The key of this DynamicRoutingTypeRoutingBackend.
        :rtype: oci.apigateway.models.DynamicSelectionKey
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DynamicRoutingTypeRoutingBackend.

        :param key: The key of this DynamicRoutingTypeRoutingBackend.
        :type: oci.apigateway.models.DynamicSelectionKey
        """
        self._key = key

    @property
    def backend(self):
        """
        **[Required]** Gets the backend of this DynamicRoutingTypeRoutingBackend.

        :return: The backend of this DynamicRoutingTypeRoutingBackend.
        :rtype: oci.apigateway.models.ApiSpecificationRouteBackend
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        """
        Sets the backend of this DynamicRoutingTypeRoutingBackend.

        :param backend: The backend of this DynamicRoutingTypeRoutingBackend.
        :type: oci.apigateway.models.ApiSpecificationRouteBackend
        """
        self._backend = backend

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
