# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchMonitoredResourcesDetails(object):
    """
    The property search criteria for listing monitored resources.
    """

    #: A constant which can be used with the lifecycle_state property of a SearchMonitoredResourcesDetails.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SearchMonitoredResourcesDetails.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SearchMonitoredResourcesDetails.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SearchMonitoredResourcesDetails.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SearchMonitoredResourcesDetails.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SearchMonitoredResourcesDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the sort_order property of a SearchMonitoredResourcesDetails.
    #: This constant has a value of "ASC"
    SORT_ORDER_ASC = "ASC"

    #: A constant which can be used with the sort_order property of a SearchMonitoredResourcesDetails.
    #: This constant has a value of "DESC"
    SORT_ORDER_DESC = "DESC"

    #: A constant which can be used with the sort_by property of a SearchMonitoredResourcesDetails.
    #: This constant has a value of "TIME_CREATED"
    SORT_BY_TIME_CREATED = "TIME_CREATED"

    #: A constant which can be used with the sort_by property of a SearchMonitoredResourcesDetails.
    #: This constant has a value of "RESOURCE_NAME"
    SORT_BY_RESOURCE_NAME = "RESOURCE_NAME"

    def __init__(self, **kwargs):
        """
        Initializes a new SearchMonitoredResourcesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this SearchMonitoredResourcesDetails.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this SearchMonitoredResourcesDetails.
        :type name: str

        :param name_contains:
            The value to assign to the name_contains property of this SearchMonitoredResourcesDetails.
        :type name_contains: str

        :param type:
            The value to assign to the type property of this SearchMonitoredResourcesDetails.
        :type type: str

        :param host_name:
            The value to assign to the host_name property of this SearchMonitoredResourcesDetails.
        :type host_name: str

        :param external_id:
            The value to assign to the external_id property of this SearchMonitoredResourcesDetails.
        :type external_id: str

        :param host_name_contains:
            The value to assign to the host_name_contains property of this SearchMonitoredResourcesDetails.
        :type host_name_contains: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this SearchMonitoredResourcesDetails.
        :type management_agent_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SearchMonitoredResourcesDetails.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param time_created_greater_than_or_equal_to:
            The value to assign to the time_created_greater_than_or_equal_to property of this SearchMonitoredResourcesDetails.
        :type time_created_greater_than_or_equal_to: datetime

        :param time_created_less_than:
            The value to assign to the time_created_less_than property of this SearchMonitoredResourcesDetails.
        :type time_created_less_than: datetime

        :param time_updated_greater_than_or_equal_to:
            The value to assign to the time_updated_greater_than_or_equal_to property of this SearchMonitoredResourcesDetails.
        :type time_updated_greater_than_or_equal_to: datetime

        :param time_updated_less_than:
            The value to assign to the time_updated_less_than property of this SearchMonitoredResourcesDetails.
        :type time_updated_less_than: datetime

        :param resource_time_zone:
            The value to assign to the resource_time_zone property of this SearchMonitoredResourcesDetails.
        :type resource_time_zone: str

        :param sort_order:
            The value to assign to the sort_order property of this SearchMonitoredResourcesDetails.
            Allowed values for this property are: "ASC", "DESC"
        :type sort_order: str

        :param sort_by:
            The value to assign to the sort_by property of this SearchMonitoredResourcesDetails.
            Allowed values for this property are: "TIME_CREATED", "RESOURCE_NAME"
        :type sort_by: str

        :param property_equals:
            The value to assign to the property_equals property of this SearchMonitoredResourcesDetails.
        :type property_equals: dict(str, str)

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'name_contains': 'str',
            'type': 'str',
            'host_name': 'str',
            'external_id': 'str',
            'host_name_contains': 'str',
            'management_agent_id': 'str',
            'lifecycle_state': 'str',
            'time_created_greater_than_or_equal_to': 'datetime',
            'time_created_less_than': 'datetime',
            'time_updated_greater_than_or_equal_to': 'datetime',
            'time_updated_less_than': 'datetime',
            'resource_time_zone': 'str',
            'sort_order': 'str',
            'sort_by': 'str',
            'property_equals': 'dict(str, str)'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'name_contains': 'nameContains',
            'type': 'type',
            'host_name': 'hostName',
            'external_id': 'externalId',
            'host_name_contains': 'hostNameContains',
            'management_agent_id': 'managementAgentId',
            'lifecycle_state': 'lifecycleState',
            'time_created_greater_than_or_equal_to': 'timeCreatedGreaterThanOrEqualTo',
            'time_created_less_than': 'timeCreatedLessThan',
            'time_updated_greater_than_or_equal_to': 'timeUpdatedGreaterThanOrEqualTo',
            'time_updated_less_than': 'timeUpdatedLessThan',
            'resource_time_zone': 'resourceTimeZone',
            'sort_order': 'sortOrder',
            'sort_by': 'sortBy',
            'property_equals': 'propertyEquals'
        }

        self._compartment_id = None
        self._name = None
        self._name_contains = None
        self._type = None
        self._host_name = None
        self._external_id = None
        self._host_name_contains = None
        self._management_agent_id = None
        self._lifecycle_state = None
        self._time_created_greater_than_or_equal_to = None
        self._time_created_less_than = None
        self._time_updated_greater_than_or_equal_to = None
        self._time_updated_less_than = None
        self._resource_time_zone = None
        self._sort_order = None
        self._sort_by = None
        self._property_equals = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SearchMonitoredResourcesDetails.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SearchMonitoredResourcesDetails.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this SearchMonitoredResourcesDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this SearchMonitoredResourcesDetails.
        A filter to return resources that match exact resource name


        :return: The name of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SearchMonitoredResourcesDetails.
        A filter to return resources that match exact resource name


        :param name: The name of this SearchMonitoredResourcesDetails.
        :type: str
        """
        self._name = name

    @property
    def name_contains(self):
        """
        Gets the name_contains of this SearchMonitoredResourcesDetails.
        A filter to return resources that match resource name pattern given. The match is not case sensitive.


        :return: The name_contains of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._name_contains

    @name_contains.setter
    def name_contains(self, name_contains):
        """
        Sets the name_contains of this SearchMonitoredResourcesDetails.
        A filter to return resources that match resource name pattern given. The match is not case sensitive.


        :param name_contains: The name_contains of this SearchMonitoredResourcesDetails.
        :type: str
        """
        self._name_contains = name_contains

    @property
    def type(self):
        """
        Gets the type of this SearchMonitoredResourcesDetails.
        A filter to return resources that match resource type


        :return: The type of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SearchMonitoredResourcesDetails.
        A filter to return resources that match resource type


        :param type: The type of this SearchMonitoredResourcesDetails.
        :type: str
        """
        self._type = type

    @property
    def host_name(self):
        """
        Gets the host_name of this SearchMonitoredResourcesDetails.
        A filter to return resources with host name match


        :return: The host_name of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this SearchMonitoredResourcesDetails.
        A filter to return resources with host name match


        :param host_name: The host_name of this SearchMonitoredResourcesDetails.
        :type: str
        """
        self._host_name = host_name

    @property
    def external_id(self):
        """
        Gets the external_id of this SearchMonitoredResourcesDetails.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.
        Currently supports only following resource type identifiers - externalcontainerdatabase,
        externalnoncontainerdatabase, externalpluggabledatabase and OCI compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_id of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this SearchMonitoredResourcesDetails.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.
        Currently supports only following resource type identifiers - externalcontainerdatabase,
        externalnoncontainerdatabase, externalpluggabledatabase and OCI compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_id: The external_id of this SearchMonitoredResourcesDetails.
        :type: str
        """
        self._external_id = external_id

    @property
    def host_name_contains(self):
        """
        Gets the host_name_contains of this SearchMonitoredResourcesDetails.
        A filter to return resources with host name pattern


        :return: The host_name_contains of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._host_name_contains

    @host_name_contains.setter
    def host_name_contains(self, host_name_contains):
        """
        Sets the host_name_contains of this SearchMonitoredResourcesDetails.
        A filter to return resources with host name pattern


        :param host_name_contains: The host_name_contains of this SearchMonitoredResourcesDetails.
        :type: str
        """
        self._host_name_contains = host_name_contains

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this SearchMonitoredResourcesDetails.
        A filter to return resources with matching management agent id.


        :return: The management_agent_id of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this SearchMonitoredResourcesDetails.
        A filter to return resources with matching management agent id.


        :param management_agent_id: The management_agent_id of this SearchMonitoredResourcesDetails.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SearchMonitoredResourcesDetails.
        A filter to return resources with matching lifecycle state.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"


        :return: The lifecycle_state of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SearchMonitoredResourcesDetails.
        A filter to return resources with matching lifecycle state.


        :param lifecycle_state: The lifecycle_state of this SearchMonitoredResourcesDetails.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def time_created_greater_than_or_equal_to(self):
        """
        Gets the time_created_greater_than_or_equal_to of this SearchMonitoredResourcesDetails.
        Search for resources that were created within a specific date range,
        using this parameter to specify the earliest creation date for the
        returned list (inclusive). Specifying this parameter without the
        corresponding `timeCreatedLessThan` parameter will retrieve resources created from the
        given `timeCreatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a
        Z offset, as defined by `RFC 3339`__.

        **Example:** 2016-12-19T16:39:57.600Z

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created_greater_than_or_equal_to of this SearchMonitoredResourcesDetails.
        :rtype: datetime
        """
        return self._time_created_greater_than_or_equal_to

    @time_created_greater_than_or_equal_to.setter
    def time_created_greater_than_or_equal_to(self, time_created_greater_than_or_equal_to):
        """
        Sets the time_created_greater_than_or_equal_to of this SearchMonitoredResourcesDetails.
        Search for resources that were created within a specific date range,
        using this parameter to specify the earliest creation date for the
        returned list (inclusive). Specifying this parameter without the
        corresponding `timeCreatedLessThan` parameter will retrieve resources created from the
        given `timeCreatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a
        Z offset, as defined by `RFC 3339`__.

        **Example:** 2016-12-19T16:39:57.600Z

        __ https://tools.ietf.org/html/rfc3339


        :param time_created_greater_than_or_equal_to: The time_created_greater_than_or_equal_to of this SearchMonitoredResourcesDetails.
        :type: datetime
        """
        self._time_created_greater_than_or_equal_to = time_created_greater_than_or_equal_to

    @property
    def time_created_less_than(self):
        """
        Gets the time_created_less_than of this SearchMonitoredResourcesDetails.
        Search for resources that were created within a specific date range,
        using this parameter to specify the latest creation date for the returned
        list (exclusive). Specifying this parameter without the corresponding
        `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all resources created before the
        specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as
        defined by `RFC 3339`__.

        **Example:** 2016-12-19T16:39:57.600Z

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created_less_than of this SearchMonitoredResourcesDetails.
        :rtype: datetime
        """
        return self._time_created_less_than

    @time_created_less_than.setter
    def time_created_less_than(self, time_created_less_than):
        """
        Sets the time_created_less_than of this SearchMonitoredResourcesDetails.
        Search for resources that were created within a specific date range,
        using this parameter to specify the latest creation date for the returned
        list (exclusive). Specifying this parameter without the corresponding
        `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all resources created before the
        specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as
        defined by `RFC 3339`__.

        **Example:** 2016-12-19T16:39:57.600Z

        __ https://tools.ietf.org/html/rfc3339


        :param time_created_less_than: The time_created_less_than of this SearchMonitoredResourcesDetails.
        :type: datetime
        """
        self._time_created_less_than = time_created_less_than

    @property
    def time_updated_greater_than_or_equal_to(self):
        """
        Gets the time_updated_greater_than_or_equal_to of this SearchMonitoredResourcesDetails.
        Search for resources that were updated within a specific date range,
        using this parameter to specify the earliest update date for the
        returned list (inclusive). Specifying this parameter without the
        corresponding `timeUpdatedLessThan` parameter will retrieve resources updated from the
        given `timeUpdatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a
        Z offset, as defined by `RFC 3339`__.

        **Example:** 2016-12-19T16:39:57.600Z

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated_greater_than_or_equal_to of this SearchMonitoredResourcesDetails.
        :rtype: datetime
        """
        return self._time_updated_greater_than_or_equal_to

    @time_updated_greater_than_or_equal_to.setter
    def time_updated_greater_than_or_equal_to(self, time_updated_greater_than_or_equal_to):
        """
        Sets the time_updated_greater_than_or_equal_to of this SearchMonitoredResourcesDetails.
        Search for resources that were updated within a specific date range,
        using this parameter to specify the earliest update date for the
        returned list (inclusive). Specifying this parameter without the
        corresponding `timeUpdatedLessThan` parameter will retrieve resources updated from the
        given `timeUpdatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a
        Z offset, as defined by `RFC 3339`__.

        **Example:** 2016-12-19T16:39:57.600Z

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated_greater_than_or_equal_to: The time_updated_greater_than_or_equal_to of this SearchMonitoredResourcesDetails.
        :type: datetime
        """
        self._time_updated_greater_than_or_equal_to = time_updated_greater_than_or_equal_to

    @property
    def time_updated_less_than(self):
        """
        Gets the time_updated_less_than of this SearchMonitoredResourcesDetails.
        Search for resources that were updated within a specific date range,
        using this parameter to specify the latest creation date for the returned
        list (exclusive). Specifying this parameter without the corresponding
        `timeUpdatedGreaterThanOrEqualTo` parameter will retrieve all resources updated before the
        specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as
        defined by `RFC 3339`__.

        **Example:** 2016-12-19T16:39:57.600Z

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated_less_than of this SearchMonitoredResourcesDetails.
        :rtype: datetime
        """
        return self._time_updated_less_than

    @time_updated_less_than.setter
    def time_updated_less_than(self, time_updated_less_than):
        """
        Sets the time_updated_less_than of this SearchMonitoredResourcesDetails.
        Search for resources that were updated within a specific date range,
        using this parameter to specify the latest creation date for the returned
        list (exclusive). Specifying this parameter without the corresponding
        `timeUpdatedGreaterThanOrEqualTo` parameter will retrieve all resources updated before the
        specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as
        defined by `RFC 3339`__.

        **Example:** 2016-12-19T16:39:57.600Z

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated_less_than: The time_updated_less_than of this SearchMonitoredResourcesDetails.
        :type: datetime
        """
        self._time_updated_less_than = time_updated_less_than

    @property
    def resource_time_zone(self):
        """
        Gets the resource_time_zone of this SearchMonitoredResourcesDetails.
        Time zone in the form of tz database canonical zone ID.


        :return: The resource_time_zone of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._resource_time_zone

    @resource_time_zone.setter
    def resource_time_zone(self, resource_time_zone):
        """
        Sets the resource_time_zone of this SearchMonitoredResourcesDetails.
        Time zone in the form of tz database canonical zone ID.


        :param resource_time_zone: The resource_time_zone of this SearchMonitoredResourcesDetails.
        :type: str
        """
        self._resource_time_zone = resource_time_zone

    @property
    def sort_order(self):
        """
        Gets the sort_order of this SearchMonitoredResourcesDetails.
        The sort order to use, either 'ASC' or 'DESC'.

        Allowed values for this property are: "ASC", "DESC"


        :return: The sort_order of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this SearchMonitoredResourcesDetails.
        The sort order to use, either 'ASC' or 'DESC'.


        :param sort_order: The sort_order of this SearchMonitoredResourcesDetails.
        :type: str
        """
        allowed_values = ["ASC", "DESC"]
        if not value_allowed_none_or_none_sentinel(sort_order, allowed_values):
            raise ValueError(
                "Invalid value for `sort_order`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sort_order = sort_order

    @property
    def sort_by(self):
        """
        Gets the sort_by of this SearchMonitoredResourcesDetails.
        The field to sort by. Only one sort order may be provided.
        Default order for timeCreated is descending. Default order for resources is ascending.

        Allowed values for this property are: "TIME_CREATED", "RESOURCE_NAME"


        :return: The sort_by of this SearchMonitoredResourcesDetails.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """
        Sets the sort_by of this SearchMonitoredResourcesDetails.
        The field to sort by. Only one sort order may be provided.
        Default order for timeCreated is descending. Default order for resources is ascending.


        :param sort_by: The sort_by of this SearchMonitoredResourcesDetails.
        :type: str
        """
        allowed_values = ["TIME_CREATED", "RESOURCE_NAME"]
        if not value_allowed_none_or_none_sentinel(sort_by, allowed_values):
            raise ValueError(
                "Invalid value for `sort_by`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sort_by = sort_by

    @property
    def property_equals(self):
        """
        Gets the property_equals of this SearchMonitoredResourcesDetails.
        Criteria based on resource property.


        :return: The property_equals of this SearchMonitoredResourcesDetails.
        :rtype: dict(str, str)
        """
        return self._property_equals

    @property_equals.setter
    def property_equals(self, property_equals):
        """
        Sets the property_equals of this SearchMonitoredResourcesDetails.
        Criteria based on resource property.


        :param property_equals: The property_equals of this SearchMonitoredResourcesDetails.
        :type: dict(str, str)
        """
        self._property_equals = property_equals

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
