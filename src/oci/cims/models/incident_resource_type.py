# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IncidentResourceType(object):
    """
    Details of incident type
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IncidentResourceType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_type_key:
            The value to assign to the resource_type_key property of this IncidentResourceType.
        :type resource_type_key: str

        :param name:
            The value to assign to the name property of this IncidentResourceType.
        :type name: str

        :param label:
            The value to assign to the label property of this IncidentResourceType.
        :type label: str

        :param description:
            The value to assign to the description property of this IncidentResourceType.
        :type description: str

        :param service_category_list:
            The value to assign to the service_category_list property of this IncidentResourceType.
        :type service_category_list: list[ServiceCategory]

        """
        self.swagger_types = {
            'resource_type_key': 'str',
            'name': 'str',
            'label': 'str',
            'description': 'str',
            'service_category_list': 'list[ServiceCategory]'
        }

        self.attribute_map = {
            'resource_type_key': 'resourceTypeKey',
            'name': 'name',
            'label': 'label',
            'description': 'description',
            'service_category_list': 'serviceCategoryList'
        }

        self._resource_type_key = None
        self._name = None
        self._label = None
        self._description = None
        self._service_category_list = None

    @property
    def resource_type_key(self):
        """
        Gets the resource_type_key of this IncidentResourceType.
        Unique ID that identifies an Incident Type


        :return: The resource_type_key of this IncidentResourceType.
        :rtype: str
        """
        return self._resource_type_key

    @resource_type_key.setter
    def resource_type_key(self, resource_type_key):
        """
        Sets the resource_type_key of this IncidentResourceType.
        Unique ID that identifies an Incident Type


        :param resource_type_key: The resource_type_key of this IncidentResourceType.
        :type: str
        """
        self._resource_type_key = resource_type_key

    @property
    def name(self):
        """
        Gets the name of this IncidentResourceType.
        Name of Incident type


        :return: The name of this IncidentResourceType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IncidentResourceType.
        Name of Incident type


        :param name: The name of this IncidentResourceType.
        :type: str
        """
        self._name = name

    @property
    def label(self):
        """
        **[Required]** Gets the label of this IncidentResourceType.
        Label associated with Incident Type


        :return: The label of this IncidentResourceType.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this IncidentResourceType.
        Label associated with Incident Type


        :param label: The label of this IncidentResourceType.
        :type: str
        """
        self._label = label

    @property
    def description(self):
        """
        Gets the description of this IncidentResourceType.
        Details of Incident Type


        :return: The description of this IncidentResourceType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this IncidentResourceType.
        Details of Incident Type


        :param description: The description of this IncidentResourceType.
        :type: str
        """
        self._description = description

    @property
    def service_category_list(self):
        """
        Gets the service_category_list of this IncidentResourceType.
        Service Category List


        :return: The service_category_list of this IncidentResourceType.
        :rtype: list[ServiceCategory]
        """
        return self._service_category_list

    @service_category_list.setter
    def service_category_list(self, service_category_list):
        """
        Sets the service_category_list of this IncidentResourceType.
        Service Category List


        :param service_category_list: The service_category_list of this IncidentResourceType.
        :type: list[ServiceCategory]
        """
        self._service_category_list = service_category_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
