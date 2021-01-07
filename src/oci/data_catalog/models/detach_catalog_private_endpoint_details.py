# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetachCatalogPrivateEndpointDetails(object):
    """
    Information about the detaching the private endpoint resource from a catalog
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetachCatalogPrivateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param catalog_private_endpoint_id:
            The value to assign to the catalog_private_endpoint_id property of this DetachCatalogPrivateEndpointDetails.
        :type catalog_private_endpoint_id: str

        """
        self.swagger_types = {
            'catalog_private_endpoint_id': 'str'
        }

        self.attribute_map = {
            'catalog_private_endpoint_id': 'catalogPrivateEndpointId'
        }

        self._catalog_private_endpoint_id = None

    @property
    def catalog_private_endpoint_id(self):
        """
        **[Required]** Gets the catalog_private_endpoint_id of this DetachCatalogPrivateEndpointDetails.
        The identifier of the private endpoint to be detached from catalog resource.


        :return: The catalog_private_endpoint_id of this DetachCatalogPrivateEndpointDetails.
        :rtype: str
        """
        return self._catalog_private_endpoint_id

    @catalog_private_endpoint_id.setter
    def catalog_private_endpoint_id(self, catalog_private_endpoint_id):
        """
        Sets the catalog_private_endpoint_id of this DetachCatalogPrivateEndpointDetails.
        The identifier of the private endpoint to be detached from catalog resource.


        :param catalog_private_endpoint_id: The catalog_private_endpoint_id of this DetachCatalogPrivateEndpointDetails.
        :type: str
        """
        self._catalog_private_endpoint_id = catalog_private_endpoint_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
