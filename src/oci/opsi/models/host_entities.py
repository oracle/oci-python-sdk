# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_configuration_metric_group import HostConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostEntities(HostConfigurationMetricGroup):
    """
    Database entities running on the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostEntities object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostEntities.metric_name` attribute
        of this class is ``HOST_ENTITIES`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostEntities.
            Allowed values for this property are: "HOST_PRODUCT", "HOST_RESOURCE_ALLOCATION", "HOST_MEMORY_CONFIGURATION", "HOST_HARDWARE_CONFIGURATION", "HOST_CPU_HARDWARE_CONFIGURATION", "HOST_NETWORK_CONFIGURATION", "HOST_ENTITES"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostEntities.
        :type time_collected: datetime

        :param entity_name:
            The value to assign to the entity_name property of this HostEntities.
        :type entity_name: str

        :param entity_type:
            The value to assign to the entity_type property of this HostEntities.
        :type entity_type: str

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'entity_name': 'str',
            'entity_type': 'str'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'entity_name': 'entityName',
            'entity_type': 'entityType'
        }

        self._metric_name = None
        self._time_collected = None
        self._entity_name = None
        self._entity_type = None
        self._metric_name = 'HOST_ENTITIES'

    @property
    def entity_name(self):
        """
        **[Required]** Gets the entity_name of this HostEntities.
        Name of the database entity


        :return: The entity_name of this HostEntities.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this HostEntities.
        Name of the database entity


        :param entity_name: The entity_name of this HostEntities.
        :type: str
        """
        self._entity_name = entity_name

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this HostEntities.
        Type of the database entity


        :return: The entity_type of this HostEntities.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this HostEntities.
        Type of the database entity


        :param entity_type: The entity_type of this HostEntities.
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
