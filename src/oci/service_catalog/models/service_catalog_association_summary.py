# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceCatalogAssociationSummary(object):
    """
    The model for a summary of a service catalog association.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceCatalogAssociationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ServiceCatalogAssociationSummary.
        :type id: str

        :param service_catalog_id:
            The value to assign to the service_catalog_id property of this ServiceCatalogAssociationSummary.
        :type service_catalog_id: str

        :param entity_id:
            The value to assign to the entity_id property of this ServiceCatalogAssociationSummary.
        :type entity_id: str

        :param entity_type:
            The value to assign to the entity_type property of this ServiceCatalogAssociationSummary.
        :type entity_type: str

        :param time_created:
            The value to assign to the time_created property of this ServiceCatalogAssociationSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'service_catalog_id': 'str',
            'entity_id': 'str',
            'entity_type': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'service_catalog_id': 'serviceCatalogId',
            'entity_id': 'entityId',
            'entity_type': 'entityType',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._service_catalog_id = None
        self._entity_id = None
        self._entity_type = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ServiceCatalogAssociationSummary.
        The unique identifier of the service catalog association.


        :return: The id of this ServiceCatalogAssociationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ServiceCatalogAssociationSummary.
        The unique identifier of the service catalog association.


        :param id: The id of this ServiceCatalogAssociationSummary.
        :type: str
        """
        self._id = id

    @property
    def service_catalog_id(self):
        """
        **[Required]** Gets the service_catalog_id of this ServiceCatalogAssociationSummary.
        The unique identifier of the service catalog.


        :return: The service_catalog_id of this ServiceCatalogAssociationSummary.
        :rtype: str
        """
        return self._service_catalog_id

    @service_catalog_id.setter
    def service_catalog_id(self, service_catalog_id):
        """
        Sets the service_catalog_id of this ServiceCatalogAssociationSummary.
        The unique identifier of the service catalog.


        :param service_catalog_id: The service_catalog_id of this ServiceCatalogAssociationSummary.
        :type: str
        """
        self._service_catalog_id = service_catalog_id

    @property
    def entity_id(self):
        """
        **[Required]** Gets the entity_id of this ServiceCatalogAssociationSummary.
        The unique identifier of the resource being associated to service catalog.


        :return: The entity_id of this ServiceCatalogAssociationSummary.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this ServiceCatalogAssociationSummary.
        The unique identifier of the resource being associated to service catalog.


        :param entity_id: The entity_id of this ServiceCatalogAssociationSummary.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this ServiceCatalogAssociationSummary.
        The type of the entity that is associated with the service catalog.


        :return: The entity_type of this ServiceCatalogAssociationSummary.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this ServiceCatalogAssociationSummary.
        The type of the entity that is associated with the service catalog.


        :param entity_type: The entity_type of this ServiceCatalogAssociationSummary.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ServiceCatalogAssociationSummary.
        Timestamp of when the resource was associated with service catalog.


        :return: The time_created of this ServiceCatalogAssociationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ServiceCatalogAssociationSummary.
        Timestamp of when the resource was associated with service catalog.


        :param time_created: The time_created of this ServiceCatalogAssociationSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
