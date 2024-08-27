# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230801


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceProviderAction(object):
    """
    Details of the Service Provider Action. Service provider actions are a pre-defined set of commands available to the support operator on different layers of the infrastructure. Although the groupings may differ depending on the infrastructure layers,
    the groups are designed to enable the support operator access to commands to resolve a specific set of issues.
    """

    #: A constant which can be used with the resource_type property of a ServiceProviderAction.
    #: This constant has a value of "VMCLUSTER"
    RESOURCE_TYPE_VMCLUSTER = "VMCLUSTER"

    #: A constant which can be used with the resource_type property of a ServiceProviderAction.
    #: This constant has a value of "CLOUDVMCLUSTER"
    RESOURCE_TYPE_CLOUDVMCLUSTER = "CLOUDVMCLUSTER"

    #: A constant which can be used with the service_provider_service_types property of a ServiceProviderAction.
    #: This constant has a value of "TROUBLESHOOTING"
    SERVICE_PROVIDER_SERVICE_TYPES_TROUBLESHOOTING = "TROUBLESHOOTING"

    #: A constant which can be used with the service_provider_service_types property of a ServiceProviderAction.
    #: This constant has a value of "ASSISTED_PATCHING"
    SERVICE_PROVIDER_SERVICE_TYPES_ASSISTED_PATCHING = "ASSISTED_PATCHING"

    #: A constant which can be used with the lifecycle_state property of a ServiceProviderAction.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ServiceProviderAction.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceProviderAction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ServiceProviderAction.
        :type id: str

        :param name:
            The value to assign to the name property of this ServiceProviderAction.
        :type name: str

        :param customer_display_name:
            The value to assign to the customer_display_name property of this ServiceProviderAction.
        :type customer_display_name: str

        :param component:
            The value to assign to the component property of this ServiceProviderAction.
        :type component: str

        :param resource_type:
            The value to assign to the resource_type property of this ServiceProviderAction.
            Allowed values for this property are: "VMCLUSTER", "CLOUDVMCLUSTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param service_provider_service_types:
            The value to assign to the service_provider_service_types property of this ServiceProviderAction.
            Allowed values for items in this list are: "TROUBLESHOOTING", "ASSISTED_PATCHING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type service_provider_service_types: list[str]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ServiceProviderAction.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param description:
            The value to assign to the description property of this ServiceProviderAction.
        :type description: str

        :param properties:
            The value to assign to the properties property of this ServiceProviderAction.
        :type properties: list[oci.delegate_access_control.models.ServiceProviderActionProperties]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'customer_display_name': 'str',
            'component': 'str',
            'resource_type': 'str',
            'service_provider_service_types': 'list[str]',
            'lifecycle_state': 'str',
            'description': 'str',
            'properties': 'list[ServiceProviderActionProperties]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'customer_display_name': 'customerDisplayName',
            'component': 'component',
            'resource_type': 'resourceType',
            'service_provider_service_types': 'serviceProviderServiceTypes',
            'lifecycle_state': 'lifecycleState',
            'description': 'description',
            'properties': 'properties'
        }

        self._id = None
        self._name = None
        self._customer_display_name = None
        self._component = None
        self._resource_type = None
        self._service_provider_service_types = None
        self._lifecycle_state = None
        self._description = None
        self._properties = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ServiceProviderAction.
        Unique Oracle assigned identifier for the Service Provider Action.


        :return: The id of this ServiceProviderAction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ServiceProviderAction.
        Unique Oracle assigned identifier for the Service Provider Action.


        :param id: The id of this ServiceProviderAction.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ServiceProviderAction.
        Unique name of the Service Provider Action.


        :return: The name of this ServiceProviderAction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ServiceProviderAction.
        Unique name of the Service Provider Action.


        :param name: The name of this ServiceProviderAction.
        :type: str
        """
        self._name = name

    @property
    def customer_display_name(self):
        """
        Gets the customer_display_name of this ServiceProviderAction.
        Display Name of the Service Provider Action.


        :return: The customer_display_name of this ServiceProviderAction.
        :rtype: str
        """
        return self._customer_display_name

    @customer_display_name.setter
    def customer_display_name(self, customer_display_name):
        """
        Sets the customer_display_name of this ServiceProviderAction.
        Display Name of the Service Provider Action.


        :param customer_display_name: The customer_display_name of this ServiceProviderAction.
        :type: str
        """
        self._customer_display_name = customer_display_name

    @property
    def component(self):
        """
        Gets the component of this ServiceProviderAction.
        Name of the infrastructure layer associated with the Service Provider Action.


        :return: The component of this ServiceProviderAction.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this ServiceProviderAction.
        Name of the infrastructure layer associated with the Service Provider Action.


        :param component: The component of this ServiceProviderAction.
        :type: str
        """
        self._component = component

    @property
    def resource_type(self):
        """
        Gets the resource_type of this ServiceProviderAction.
        resourceType for which the ServiceProviderAction is applicable

        Allowed values for this property are: "VMCLUSTER", "CLOUDVMCLUSTER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_type of this ServiceProviderAction.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this ServiceProviderAction.
        resourceType for which the ServiceProviderAction is applicable


        :param resource_type: The resource_type of this ServiceProviderAction.
        :type: str
        """
        allowed_values = ["VMCLUSTER", "CLOUDVMCLUSTER"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            resource_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_type = resource_type

    @property
    def service_provider_service_types(self):
        """
        Gets the service_provider_service_types of this ServiceProviderAction.
        List of Service Provider Service Types that this Service Provider Action is applicable to.

        Allowed values for items in this list are: "TROUBLESHOOTING", "ASSISTED_PATCHING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The service_provider_service_types of this ServiceProviderAction.
        :rtype: list[str]
        """
        return self._service_provider_service_types

    @service_provider_service_types.setter
    def service_provider_service_types(self, service_provider_service_types):
        """
        Sets the service_provider_service_types of this ServiceProviderAction.
        List of Service Provider Service Types that this Service Provider Action is applicable to.


        :param service_provider_service_types: The service_provider_service_types of this ServiceProviderAction.
        :type: list[str]
        """
        allowed_values = ["TROUBLESHOOTING", "ASSISTED_PATCHING"]
        if service_provider_service_types:
            service_provider_service_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in service_provider_service_types]
        self._service_provider_service_types = service_provider_service_types

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ServiceProviderAction.
        The current lifecycle state of the Service Provider Action.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ServiceProviderAction.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ServiceProviderAction.
        The current lifecycle state of the Service Provider Action.


        :param lifecycle_state: The lifecycle_state of this ServiceProviderAction.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def description(self):
        """
        Gets the description of this ServiceProviderAction.
        Description of the Service Provider Action in terms of associated risk profile, and characteristics of the operating system commands made
        available to the support operator under this Service Provider Action.


        :return: The description of this ServiceProviderAction.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ServiceProviderAction.
        Description of the Service Provider Action in terms of associated risk profile, and characteristics of the operating system commands made
        available to the support operator under this Service Provider Action.


        :param description: The description of this ServiceProviderAction.
        :type: str
        """
        self._description = description

    @property
    def properties(self):
        """
        Gets the properties of this ServiceProviderAction.
        Fine grained properties associated with the Delegation Control.


        :return: The properties of this ServiceProviderAction.
        :rtype: list[oci.delegate_access_control.models.ServiceProviderActionProperties]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this ServiceProviderAction.
        Fine grained properties associated with the Delegation Control.


        :param properties: The properties of this ServiceProviderAction.
        :type: list[oci.delegate_access_control.models.ServiceProviderActionProperties]
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
