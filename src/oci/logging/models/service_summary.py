# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceSummary(object):
    """
    Summary of services that are integrated with public logging.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenant_id:
            The value to assign to the tenant_id property of this ServiceSummary.
        :type tenant_id: str

        :param namespace:
            The value to assign to the namespace property of this ServiceSummary.
        :type namespace: str

        :param service_principal_name:
            The value to assign to the service_principal_name property of this ServiceSummary.
        :type service_principal_name: str

        :param endpoint:
            The value to assign to the endpoint property of this ServiceSummary.
        :type endpoint: str

        :param name:
            The value to assign to the name property of this ServiceSummary.
        :type name: str

        :param id:
            The value to assign to the id property of this ServiceSummary.
        :type id: str

        :param resource_types:
            The value to assign to the resource_types property of this ServiceSummary.
        :type resource_types: list[oci.logging.models.ResourceType]

        """
        self.swagger_types = {
            'tenant_id': 'str',
            'namespace': 'str',
            'service_principal_name': 'str',
            'endpoint': 'str',
            'name': 'str',
            'id': 'str',
            'resource_types': 'list[ResourceType]'
        }

        self.attribute_map = {
            'tenant_id': 'tenantId',
            'namespace': 'namespace',
            'service_principal_name': 'servicePrincipalName',
            'endpoint': 'endpoint',
            'name': 'name',
            'id': 'id',
            'resource_types': 'resourceTypes'
        }

        self._tenant_id = None
        self._namespace = None
        self._service_principal_name = None
        self._endpoint = None
        self._name = None
        self._id = None
        self._resource_types = None

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this ServiceSummary.
        Tenant OCID.


        :return: The tenant_id of this ServiceSummary.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this ServiceSummary.
        Tenant OCID.


        :param tenant_id: The tenant_id of this ServiceSummary.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def namespace(self):
        """
        Gets the namespace of this ServiceSummary.
        Apollo project namespace, if any.


        :return: The namespace of this ServiceSummary.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this ServiceSummary.
        Apollo project namespace, if any.


        :param namespace: The namespace of this ServiceSummary.
        :type: str
        """
        self._namespace = namespace

    @property
    def service_principal_name(self):
        """
        **[Required]** Gets the service_principal_name of this ServiceSummary.
        Service ID as set in Service Principal.


        :return: The service_principal_name of this ServiceSummary.
        :rtype: str
        """
        return self._service_principal_name

    @service_principal_name.setter
    def service_principal_name(self, service_principal_name):
        """
        Sets the service_principal_name of this ServiceSummary.
        Service ID as set in Service Principal.


        :param service_principal_name: The service_principal_name of this ServiceSummary.
        :type: str
        """
        self._service_principal_name = service_principal_name

    @property
    def endpoint(self):
        """
        **[Required]** Gets the endpoint of this ServiceSummary.
        Service endpoint.


        :return: The endpoint of this ServiceSummary.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this ServiceSummary.
        Service endpoint.


        :param endpoint: The endpoint of this ServiceSummary.
        :type: str
        """
        self._endpoint = endpoint

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ServiceSummary.
        User-friendly service name.


        :return: The name of this ServiceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ServiceSummary.
        User-friendly service name.


        :param name: The name of this ServiceSummary.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """
        Gets the id of this ServiceSummary.
        Service ID.


        :return: The id of this ServiceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ServiceSummary.
        Service ID.


        :param id: The id of this ServiceSummary.
        :type: str
        """
        self._id = id

    @property
    def resource_types(self):
        """
        **[Required]** Gets the resource_types of this ServiceSummary.
        Type of resource that a service provides.


        :return: The resource_types of this ServiceSummary.
        :rtype: list[oci.logging.models.ResourceType]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """
        Sets the resource_types of this ServiceSummary.
        Type of resource that a service provides.


        :param resource_types: The resource_types of this ServiceSummary.
        :type: list[oci.logging.models.ResourceType]
        """
        self._resource_types = resource_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
