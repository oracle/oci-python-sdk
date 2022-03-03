# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceSummary(object):
    """
    A resource that exists in the cloud network that you're querying.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_type:
            The value to assign to the resource_type property of this ResourceSummary.
        :type resource_type: str

        :param identifier:
            The value to assign to the identifier property of this ResourceSummary.
        :type identifier: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ResourceSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this ResourceSummary.
        :type time_created: datetime

        :param display_name:
            The value to assign to the display_name property of this ResourceSummary.
        :type display_name: str

        :param availability_domain:
            The value to assign to the availability_domain property of this ResourceSummary.
        :type availability_domain: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ResourceSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ResourceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ResourceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ResourceSummary.
        :type system_tags: dict(str, dict(str, object))

        :param search_context:
            The value to assign to the search_context property of this ResourceSummary.
        :type search_context: oci.resource_search.models.SearchContext

        :param identity_context:
            The value to assign to the identity_context property of this ResourceSummary.
        :type identity_context: dict(str, object)

        :param additional_details:
            The value to assign to the additional_details property of this ResourceSummary.
        :type additional_details: dict(str, object)

        """
        self.swagger_types = {
            'resource_type': 'str',
            'identifier': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'display_name': 'str',
            'availability_domain': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'search_context': 'SearchContext',
            'identity_context': 'dict(str, object)',
            'additional_details': 'dict(str, object)'
        }

        self.attribute_map = {
            'resource_type': 'resourceType',
            'identifier': 'identifier',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'display_name': 'displayName',
            'availability_domain': 'availabilityDomain',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'search_context': 'searchContext',
            'identity_context': 'identityContext',
            'additional_details': 'additionalDetails'
        }

        self._resource_type = None
        self._identifier = None
        self._compartment_id = None
        self._time_created = None
        self._display_name = None
        self._availability_domain = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._search_context = None
        self._identity_context = None
        self._additional_details = None

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this ResourceSummary.
        The resource type name.


        :return: The resource_type of this ResourceSummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this ResourceSummary.
        The resource type name.


        :param resource_type: The resource_type of this ResourceSummary.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this ResourceSummary.
        The unique identifier for this particular resource, usually an OCID.


        :return: The identifier of this ResourceSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ResourceSummary.
        The unique identifier for this particular resource, usually an OCID.


        :param identifier: The identifier of this ResourceSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ResourceSummary.
        The OCID of the compartment that contains this resource.


        :return: The compartment_id of this ResourceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ResourceSummary.
        The OCID of the compartment that contains this resource.


        :param compartment_id: The compartment_id of this ResourceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this ResourceSummary.
        The time that this resource was created.


        :return: The time_created of this ResourceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ResourceSummary.
        The time that this resource was created.


        :param time_created: The time_created of this ResourceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def display_name(self):
        """
        Gets the display_name of this ResourceSummary.
        The display name (or name) of this resource, if one exists.


        :return: The display_name of this ResourceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ResourceSummary.
        The display name (or name) of this resource, if one exists.


        :param display_name: The display_name of this ResourceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this ResourceSummary.
        The availability domain where this resource exists, if applicable.


        :return: The availability_domain of this ResourceSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ResourceSummary.
        The availability domain where this resource exists, if applicable.


        :param availability_domain: The availability_domain of this ResourceSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ResourceSummary.
        The lifecycle state of this resource, if applicable.


        :return: The lifecycle_state of this ResourceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ResourceSummary.
        The lifecycle state of this resource, if applicable.


        :param lifecycle_state: The lifecycle_state of this ResourceSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ResourceSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ResourceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ResourceSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ResourceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ResourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ResourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ResourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ResourceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ResourceSummary.
        System tags associated with this resource, if any. System tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ResourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ResourceSummary.
        System tags associated with this resource, if any. System tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ResourceSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def search_context(self):
        """
        Gets the search_context of this ResourceSummary.

        :return: The search_context of this ResourceSummary.
        :rtype: oci.resource_search.models.SearchContext
        """
        return self._search_context

    @search_context.setter
    def search_context(self, search_context):
        """
        Sets the search_context of this ResourceSummary.

        :param search_context: The search_context of this ResourceSummary.
        :type: oci.resource_search.models.SearchContext
        """
        self._search_context = search_context

    @property
    def identity_context(self):
        """
        Gets the identity_context of this ResourceSummary.
        Additional identifiers to use together in a \"Get\" request for a specified resource, only required for resource types
        that explicitly cannot be retrieved by using a single identifier, such as the resource's OCID.


        :return: The identity_context of this ResourceSummary.
        :rtype: dict(str, object)
        """
        return self._identity_context

    @identity_context.setter
    def identity_context(self, identity_context):
        """
        Sets the identity_context of this ResourceSummary.
        Additional identifiers to use together in a \"Get\" request for a specified resource, only required for resource types
        that explicitly cannot be retrieved by using a single identifier, such as the resource's OCID.


        :param identity_context: The identity_context of this ResourceSummary.
        :type: dict(str, object)
        """
        self._identity_context = identity_context

    @property
    def additional_details(self):
        """
        Gets the additional_details of this ResourceSummary.
        Additional resource attribute fields of this resource that match queries with a return clause, if any.
        For example, if you ran a query to find the private IP addresses, public IP addresses, and isPrimary field of
        the VNIC attachment on instance resources, that field would be included in the ResourceSummary object as:
        {\"additionalDetails\": {\"attachedVnic\": [{\"publicIP\" : \"172.110.110.110\",\"privateIP\" : \"10.10.10.10\",\"isPrimary\" : true},
        {\"publicIP\" : \"172.110.110.111\",\"privateIP\" : \"10.10.10.11\",\"isPrimary\" : false}]}.
        The structure of the additional details attribute fields depends on the matching resource.


        :return: The additional_details of this ResourceSummary.
        :rtype: dict(str, object)
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """
        Sets the additional_details of this ResourceSummary.
        Additional resource attribute fields of this resource that match queries with a return clause, if any.
        For example, if you ran a query to find the private IP addresses, public IP addresses, and isPrimary field of
        the VNIC attachment on instance resources, that field would be included in the ResourceSummary object as:
        {\"additionalDetails\": {\"attachedVnic\": [{\"publicIP\" : \"172.110.110.110\",\"privateIP\" : \"10.10.10.10\",\"isPrimary\" : true},
        {\"publicIP\" : \"172.110.110.111\",\"privateIP\" : \"10.10.10.11\",\"isPrimary\" : false}]}.
        The structure of the additional details attribute fields depends on the matching resource.


        :param additional_details: The additional_details of this ResourceSummary.
        :type: dict(str, object)
        """
        self._additional_details = additional_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
