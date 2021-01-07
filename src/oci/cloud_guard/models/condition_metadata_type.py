# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConditionMetadataType(object):
    """
    condition type provided by cloud guard
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConditionMetadataType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ConditionMetadataType.
        :type name: str

        :param service_types:
            The value to assign to the service_types property of this ConditionMetadataType.
        :type service_types: list[oci.cloud_guard.models.ServiceTypeSummary]

        """
        self.swagger_types = {
            'name': 'str',
            'service_types': 'list[ServiceTypeSummary]'
        }

        self.attribute_map = {
            'name': 'name',
            'service_types': 'serviceTypes'
        }

        self._name = None
        self._service_types = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ConditionMetadataType.
        Name used to identify


        :return: The name of this ConditionMetadataType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConditionMetadataType.
        Name used to identify


        :param name: The name of this ConditionMetadataType.
        :type: str
        """
        self._name = name

    @property
    def service_types(self):
        """
        **[Required]** Gets the service_types of this ConditionMetadataType.
        collection of Service type


        :return: The service_types of this ConditionMetadataType.
        :rtype: list[oci.cloud_guard.models.ServiceTypeSummary]
        """
        return self._service_types

    @service_types.setter
    def service_types(self, service_types):
        """
        Sets the service_types of this ConditionMetadataType.
        collection of Service type


        :param service_types: The service_types of this ConditionMetadataType.
        :type: list[oci.cloud_guard.models.ServiceTypeSummary]
        """
        self._service_types = service_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
