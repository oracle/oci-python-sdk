# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateServiceCatalogAssociationDetails(object):
    """
    The model to create a single association between a service catalog and a resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateServiceCatalogAssociationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param service_catalog_id:
            The value to assign to the service_catalog_id property of this CreateServiceCatalogAssociationDetails.
        :type service_catalog_id: str

        :param entity_id:
            The value to assign to the entity_id property of this CreateServiceCatalogAssociationDetails.
        :type entity_id: str

        :param entity_type:
            The value to assign to the entity_type property of this CreateServiceCatalogAssociationDetails.
        :type entity_type: str

        """
        self.swagger_types = {
            'service_catalog_id': 'str',
            'entity_id': 'str',
            'entity_type': 'str'
        }

        self.attribute_map = {
            'service_catalog_id': 'serviceCatalogId',
            'entity_id': 'entityId',
            'entity_type': 'entityType'
        }

        self._service_catalog_id = None
        self._entity_id = None
        self._entity_type = None

    @property
    def service_catalog_id(self):
        """
        **[Required]** Gets the service_catalog_id of this CreateServiceCatalogAssociationDetails.
        Identifier of the service catalog.


        :return: The service_catalog_id of this CreateServiceCatalogAssociationDetails.
        :rtype: str
        """
        return self._service_catalog_id

    @service_catalog_id.setter
    def service_catalog_id(self, service_catalog_id):
        """
        Sets the service_catalog_id of this CreateServiceCatalogAssociationDetails.
        Identifier of the service catalog.


        :param service_catalog_id: The service_catalog_id of this CreateServiceCatalogAssociationDetails.
        :type: str
        """
        self._service_catalog_id = service_catalog_id

    @property
    def entity_id(self):
        """
        **[Required]** Gets the entity_id of this CreateServiceCatalogAssociationDetails.
        Identifier of the entity being associated with service catalog.


        :return: The entity_id of this CreateServiceCatalogAssociationDetails.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this CreateServiceCatalogAssociationDetails.
        Identifier of the entity being associated with service catalog.


        :param entity_id: The entity_id of this CreateServiceCatalogAssociationDetails.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this CreateServiceCatalogAssociationDetails.
        The type of the entity that is associated with the service catalog.


        :return: The entity_type of this CreateServiceCatalogAssociationDetails.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this CreateServiceCatalogAssociationDetails.
        The type of the entity that is associated with the service catalog.


        :param entity_type: The entity_type of this CreateServiceCatalogAssociationDetails.
        :type: str
        """
        self._entity_type = entity_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
