# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceSummary(object):
    """
    A resource that exists in the user's cloud network.
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

        :param search_context:
            The value to assign to the search_context property of this ResourceSummary.
        :type search_context: SearchContext

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
            'search_context': 'SearchContext'
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
            'search_context': 'searchContext'
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
        self._search_context = None

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
        The time this resource was created.


        :return: The time_created of this ResourceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ResourceSummary.
        The time this resource was created.


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
        The availability domain this resource is located in, if applicable.


        :return: The availability_domain of this ResourceSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ResourceSummary.
        The availability domain this resource is located in, if applicable.


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
        The freeform tags associated with this resource, if any.


        :return: The freeform_tags of this ResourceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ResourceSummary.
        The freeform tags associated with this resource, if any.


        :param freeform_tags: The freeform_tags of this ResourceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ResourceSummary.
        The defined tags associated with this resource, if any.


        :return: The defined_tags of this ResourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ResourceSummary.
        The defined tags associated with this resource, if any.


        :param defined_tags: The defined_tags of this ResourceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def search_context(self):
        """
        Gets the search_context of this ResourceSummary.
        Contains search context, such as highlighting, for found resources.


        :return: The search_context of this ResourceSummary.
        :rtype: SearchContext
        """
        return self._search_context

    @search_context.setter
    def search_context(self, search_context):
        """
        Sets the search_context of this ResourceSummary.
        Contains search context, such as highlighting, for found resources.


        :param search_context: The search_context of this ResourceSummary.
        :type: SearchContext
        """
        self._search_context = search_context

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
