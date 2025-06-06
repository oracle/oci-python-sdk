# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OccmDemandSignalItemSummary(object):
    """
    A summary model containing information about various demand signal resource requests.
    """

    #: A constant which can be used with the demand_signal_namespace property of a OccmDemandSignalItemSummary.
    #: This constant has a value of "COMPUTE"
    DEMAND_SIGNAL_NAMESPACE_COMPUTE = "COMPUTE"

    #: A constant which can be used with the demand_signal_namespace property of a OccmDemandSignalItemSummary.
    #: This constant has a value of "NETWORK"
    DEMAND_SIGNAL_NAMESPACE_NETWORK = "NETWORK"

    #: A constant which can be used with the demand_signal_namespace property of a OccmDemandSignalItemSummary.
    #: This constant has a value of "GPU"
    DEMAND_SIGNAL_NAMESPACE_GPU = "GPU"

    #: A constant which can be used with the demand_signal_namespace property of a OccmDemandSignalItemSummary.
    #: This constant has a value of "STORAGE"
    DEMAND_SIGNAL_NAMESPACE_STORAGE = "STORAGE"

    #: A constant which can be used with the request_type property of a OccmDemandSignalItemSummary.
    #: This constant has a value of "DEMAND"
    REQUEST_TYPE_DEMAND = "DEMAND"

    def __init__(self, **kwargs):
        """
        Initializes a new OccmDemandSignalItemSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OccmDemandSignalItemSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OccmDemandSignalItemSummary.
        :type compartment_id: str

        :param demand_signal_id:
            The value to assign to the demand_signal_id property of this OccmDemandSignalItemSummary.
        :type demand_signal_id: str

        :param demand_signal_namespace:
            The value to assign to the demand_signal_namespace property of this OccmDemandSignalItemSummary.
            Allowed values for this property are: "COMPUTE", "NETWORK", "GPU", "STORAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type demand_signal_namespace: str

        :param demand_signal_catalog_resource_id:
            The value to assign to the demand_signal_catalog_resource_id property of this OccmDemandSignalItemSummary.
        :type demand_signal_catalog_resource_id: str

        :param request_type:
            The value to assign to the request_type property of this OccmDemandSignalItemSummary.
            Allowed values for this property are: "DEMAND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type request_type: str

        :param resource_name:
            The value to assign to the resource_name property of this OccmDemandSignalItemSummary.
        :type resource_name: str

        :param region:
            The value to assign to the region property of this OccmDemandSignalItemSummary.
        :type region: str

        :param availability_domain:
            The value to assign to the availability_domain property of this OccmDemandSignalItemSummary.
        :type availability_domain: str

        :param target_compartment_id:
            The value to assign to the target_compartment_id property of this OccmDemandSignalItemSummary.
        :type target_compartment_id: str

        :param quantity:
            The value to assign to the quantity property of this OccmDemandSignalItemSummary.
        :type quantity: int

        :param time_needed_before:
            The value to assign to the time_needed_before property of this OccmDemandSignalItemSummary.
        :type time_needed_before: datetime

        :param resource_properties:
            The value to assign to the resource_properties property of this OccmDemandSignalItemSummary.
        :type resource_properties: dict(str, str)

        :param notes:
            The value to assign to the notes property of this OccmDemandSignalItemSummary.
        :type notes: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OccmDemandSignalItemSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OccmDemandSignalItemSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OccmDemandSignalItemSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OccmDemandSignalItemSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'demand_signal_id': 'str',
            'demand_signal_namespace': 'str',
            'demand_signal_catalog_resource_id': 'str',
            'request_type': 'str',
            'resource_name': 'str',
            'region': 'str',
            'availability_domain': 'str',
            'target_compartment_id': 'str',
            'quantity': 'int',
            'time_needed_before': 'datetime',
            'resource_properties': 'dict(str, str)',
            'notes': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'demand_signal_id': 'demandSignalId',
            'demand_signal_namespace': 'demandSignalNamespace',
            'demand_signal_catalog_resource_id': 'demandSignalCatalogResourceId',
            'request_type': 'requestType',
            'resource_name': 'resourceName',
            'region': 'region',
            'availability_domain': 'availabilityDomain',
            'target_compartment_id': 'targetCompartmentId',
            'quantity': 'quantity',
            'time_needed_before': 'timeNeededBefore',
            'resource_properties': 'resourceProperties',
            'notes': 'notes',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._compartment_id = None
        self._demand_signal_id = None
        self._demand_signal_namespace = None
        self._demand_signal_catalog_resource_id = None
        self._request_type = None
        self._resource_name = None
        self._region = None
        self._availability_domain = None
        self._target_compartment_id = None
        self._quantity = None
        self._time_needed_before = None
        self._resource_properties = None
        self._notes = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OccmDemandSignalItemSummary.
        The OCID of the demand signal resource request.


        :return: The id of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OccmDemandSignalItemSummary.
        The OCID of the demand signal resource request.


        :param id: The id of this OccmDemandSignalItemSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OccmDemandSignalItemSummary.
        The OCID of the tenancy from which the demand signal item was created.


        :return: The compartment_id of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OccmDemandSignalItemSummary.
        The OCID of the tenancy from which the demand signal item was created.


        :param compartment_id: The compartment_id of this OccmDemandSignalItemSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def demand_signal_id(self):
        """
        **[Required]** Gets the demand_signal_id of this OccmDemandSignalItemSummary.
        The OCID of the demand signal under which this item will be grouped.


        :return: The demand_signal_id of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._demand_signal_id

    @demand_signal_id.setter
    def demand_signal_id(self, demand_signal_id):
        """
        Sets the demand_signal_id of this OccmDemandSignalItemSummary.
        The OCID of the demand signal under which this item will be grouped.


        :param demand_signal_id: The demand_signal_id of this OccmDemandSignalItemSummary.
        :type: str
        """
        self._demand_signal_id = demand_signal_id

    @property
    def demand_signal_namespace(self):
        """
        **[Required]** Gets the demand_signal_namespace of this OccmDemandSignalItemSummary.
        The name of the OCI service in consideration for demand signal submission. For example: COMPUTE, NETWORK, GPU etc.

        Allowed values for this property are: "COMPUTE", "NETWORK", "GPU", "STORAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The demand_signal_namespace of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._demand_signal_namespace

    @demand_signal_namespace.setter
    def demand_signal_namespace(self, demand_signal_namespace):
        """
        Sets the demand_signal_namespace of this OccmDemandSignalItemSummary.
        The name of the OCI service in consideration for demand signal submission. For example: COMPUTE, NETWORK, GPU etc.


        :param demand_signal_namespace: The demand_signal_namespace of this OccmDemandSignalItemSummary.
        :type: str
        """
        allowed_values = ["COMPUTE", "NETWORK", "GPU", "STORAGE"]
        if not value_allowed_none_or_none_sentinel(demand_signal_namespace, allowed_values):
            demand_signal_namespace = 'UNKNOWN_ENUM_VALUE'
        self._demand_signal_namespace = demand_signal_namespace

    @property
    def demand_signal_catalog_resource_id(self):
        """
        **[Required]** Gets the demand_signal_catalog_resource_id of this OccmDemandSignalItemSummary.
        The OCID of the corresponding demand signal catalog resource.


        :return: The demand_signal_catalog_resource_id of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._demand_signal_catalog_resource_id

    @demand_signal_catalog_resource_id.setter
    def demand_signal_catalog_resource_id(self, demand_signal_catalog_resource_id):
        """
        Sets the demand_signal_catalog_resource_id of this OccmDemandSignalItemSummary.
        The OCID of the corresponding demand signal catalog resource.


        :param demand_signal_catalog_resource_id: The demand_signal_catalog_resource_id of this OccmDemandSignalItemSummary.
        :type: str
        """
        self._demand_signal_catalog_resource_id = demand_signal_catalog_resource_id

    @property
    def request_type(self):
        """
        **[Required]** Gets the request_type of this OccmDemandSignalItemSummary.
        The type of request (DEMAND or RETURN) made against a particular demand signal item.

        Allowed values for this property are: "DEMAND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The request_type of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """
        Sets the request_type of this OccmDemandSignalItemSummary.
        The type of request (DEMAND or RETURN) made against a particular demand signal item.


        :param request_type: The request_type of this OccmDemandSignalItemSummary.
        :type: str
        """
        allowed_values = ["DEMAND"]
        if not value_allowed_none_or_none_sentinel(request_type, allowed_values):
            request_type = 'UNKNOWN_ENUM_VALUE'
        self._request_type = request_type

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this OccmDemandSignalItemSummary.
        The name of the OCI resource that you want to request.


        :return: The resource_name of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this OccmDemandSignalItemSummary.
        The name of the OCI resource that you want to request.


        :param resource_name: The resource_name of this OccmDemandSignalItemSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def region(self):
        """
        **[Required]** Gets the region of this OccmDemandSignalItemSummary.
        The name of region for which you want to request the OCI resource.


        :return: The region of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this OccmDemandSignalItemSummary.
        The name of region for which you want to request the OCI resource.


        :param region: The region of this OccmDemandSignalItemSummary.
        :type: str
        """
        self._region = region

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this OccmDemandSignalItemSummary.
        The name of the availability domain for which you want to request the OCI resource.


        :return: The availability_domain of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this OccmDemandSignalItemSummary.
        The name of the availability domain for which you want to request the OCI resource.


        :param availability_domain: The availability_domain of this OccmDemandSignalItemSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def target_compartment_id(self):
        """
        Gets the target_compartment_id of this OccmDemandSignalItemSummary.
        The ocid of the tenancy for which you want to request the OCI resource for. This is an optional parameter.


        :return: The target_compartment_id of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._target_compartment_id

    @target_compartment_id.setter
    def target_compartment_id(self, target_compartment_id):
        """
        Sets the target_compartment_id of this OccmDemandSignalItemSummary.
        The ocid of the tenancy for which you want to request the OCI resource for. This is an optional parameter.


        :param target_compartment_id: The target_compartment_id of this OccmDemandSignalItemSummary.
        :type: str
        """
        self._target_compartment_id = target_compartment_id

    @property
    def quantity(self):
        """
        **[Required]** Gets the quantity of this OccmDemandSignalItemSummary.
        The quantity of the resource that you want to demand from OCI or return to OCI.


        :return: The quantity of this OccmDemandSignalItemSummary.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this OccmDemandSignalItemSummary.
        The quantity of the resource that you want to demand from OCI or return to OCI.


        :param quantity: The quantity of this OccmDemandSignalItemSummary.
        :type: int
        """
        self._quantity = quantity

    @property
    def time_needed_before(self):
        """
        **[Required]** Gets the time_needed_before of this OccmDemandSignalItemSummary.
        the date before which you would ideally like the OCI resource to be delivered to you.


        :return: The time_needed_before of this OccmDemandSignalItemSummary.
        :rtype: datetime
        """
        return self._time_needed_before

    @time_needed_before.setter
    def time_needed_before(self, time_needed_before):
        """
        Sets the time_needed_before of this OccmDemandSignalItemSummary.
        the date before which you would ideally like the OCI resource to be delivered to you.


        :param time_needed_before: The time_needed_before of this OccmDemandSignalItemSummary.
        :type: datetime
        """
        self._time_needed_before = time_needed_before

    @property
    def resource_properties(self):
        """
        **[Required]** Gets the resource_properties of this OccmDemandSignalItemSummary.
        A map of various properties associated with the OCI resource.


        :return: The resource_properties of this OccmDemandSignalItemSummary.
        :rtype: dict(str, str)
        """
        return self._resource_properties

    @resource_properties.setter
    def resource_properties(self, resource_properties):
        """
        Sets the resource_properties of this OccmDemandSignalItemSummary.
        A map of various properties associated with the OCI resource.


        :param resource_properties: The resource_properties of this OccmDemandSignalItemSummary.
        :type: dict(str, str)
        """
        self._resource_properties = resource_properties

    @property
    def notes(self):
        """
        Gets the notes of this OccmDemandSignalItemSummary.
        This field will serve as notes section for you. You can use this section to convey a message to OCI regarding your resource request.

        NOTE: The previous value gets overwritten with the new one for this once updated.


        :return: The notes of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this OccmDemandSignalItemSummary.
        This field will serve as notes section for you. You can use this section to convey a message to OCI regarding your resource request.

        NOTE: The previous value gets overwritten with the new one for this once updated.


        :param notes: The notes of this OccmDemandSignalItemSummary.
        :type: str
        """
        self._notes = notes

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OccmDemandSignalItemSummary.
        The current lifecycle state of the demand signal item.


        :return: The lifecycle_state of this OccmDemandSignalItemSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OccmDemandSignalItemSummary.
        The current lifecycle state of the demand signal item.


        :param lifecycle_state: The lifecycle_state of this OccmDemandSignalItemSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OccmDemandSignalItemSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OccmDemandSignalItemSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OccmDemandSignalItemSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OccmDemandSignalItemSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OccmDemandSignalItemSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OccmDemandSignalItemSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OccmDemandSignalItemSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OccmDemandSignalItemSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OccmDemandSignalItemSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OccmDemandSignalItemSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OccmDemandSignalItemSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OccmDemandSignalItemSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
