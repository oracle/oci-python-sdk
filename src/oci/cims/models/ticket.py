# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Ticket(object):
    """
    Details about the ticket created.
    """

    #: A constant which can be used with the severity property of a Ticket.
    #: This constant has a value of "HIGHEST"
    SEVERITY_HIGHEST = "HIGHEST"

    #: A constant which can be used with the severity property of a Ticket.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a Ticket.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the lifecycle_state property of a Ticket.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Ticket.
    #: This constant has a value of "CLOSED"
    LIFECYCLE_STATE_CLOSED = "CLOSED"

    #: A constant which can be used with the lifecycle_details property of a Ticket.
    #: This constant has a value of "PENDING_WITH_ORACLE"
    LIFECYCLE_DETAILS_PENDING_WITH_ORACLE = "PENDING_WITH_ORACLE"

    #: A constant which can be used with the lifecycle_details property of a Ticket.
    #: This constant has a value of "PENDING_WITH_CUSTOMER"
    LIFECYCLE_DETAILS_PENDING_WITH_CUSTOMER = "PENDING_WITH_CUSTOMER"

    #: A constant which can be used with the lifecycle_details property of a Ticket.
    #: This constant has a value of "CLOSE_REQUESTED"
    LIFECYCLE_DETAILS_CLOSE_REQUESTED = "CLOSE_REQUESTED"

    #: A constant which can be used with the lifecycle_details property of a Ticket.
    #: This constant has a value of "CLOSED"
    LIFECYCLE_DETAILS_CLOSED = "CLOSED"

    def __init__(self, **kwargs):
        """
        Initializes a new Ticket object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ticket_number:
            The value to assign to the ticket_number property of this Ticket.
        :type ticket_number: str

        :param severity:
            The value to assign to the severity property of this Ticket.
            Allowed values for this property are: "HIGHEST", "HIGH", "MEDIUM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param resource_list:
            The value to assign to the resource_list property of this Ticket.
        :type resource_list: list[oci.cims.models.Resource]

        :param title:
            The value to assign to the title property of this Ticket.
        :type title: str

        :param description:
            The value to assign to the description property of this Ticket.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this Ticket.
        :type time_created: int

        :param time_updated:
            The value to assign to the time_updated property of this Ticket.
        :type time_updated: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Ticket.
            Allowed values for this property are: "ACTIVE", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Ticket.
            Allowed values for this property are: "PENDING_WITH_ORACLE", "PENDING_WITH_CUSTOMER", "CLOSE_REQUESTED", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'ticket_number': 'str',
            'severity': 'str',
            'resource_list': 'list[Resource]',
            'title': 'str',
            'description': 'str',
            'time_created': 'int',
            'time_updated': 'int',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'ticket_number': 'ticketNumber',
            'severity': 'severity',
            'resource_list': 'resourceList',
            'title': 'title',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._ticket_number = None
        self._severity = None
        self._resource_list = None
        self._title = None
        self._description = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def ticket_number(self):
        """
        Gets the ticket_number of this Ticket.
        Unique identifier for the ticket.


        :return: The ticket_number of this Ticket.
        :rtype: str
        """
        return self._ticket_number

    @ticket_number.setter
    def ticket_number(self, ticket_number):
        """
        Sets the ticket_number of this Ticket.
        Unique identifier for the ticket.


        :param ticket_number: The ticket_number of this Ticket.
        :type: str
        """
        self._ticket_number = ticket_number

    @property
    def severity(self):
        """
        **[Required]** Gets the severity of this Ticket.
        The severity assigned to the ticket.

        Allowed values for this property are: "HIGHEST", "HIGH", "MEDIUM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this Ticket.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this Ticket.
        The severity assigned to the ticket.


        :param severity: The severity of this Ticket.
        :type: str
        """
        allowed_values = ["HIGHEST", "HIGH", "MEDIUM"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def resource_list(self):
        """
        Gets the resource_list of this Ticket.
        The list of resources associated with the ticket.


        :return: The resource_list of this Ticket.
        :rtype: list[oci.cims.models.Resource]
        """
        return self._resource_list

    @resource_list.setter
    def resource_list(self, resource_list):
        """
        Sets the resource_list of this Ticket.
        The list of resources associated with the ticket.


        :param resource_list: The resource_list of this Ticket.
        :type: list[oci.cims.models.Resource]
        """
        self._resource_list = resource_list

    @property
    def title(self):
        """
        **[Required]** Gets the title of this Ticket.
        The title of the ticket.


        :return: The title of this Ticket.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Ticket.
        The title of the ticket.


        :param title: The title of this Ticket.
        :type: str
        """
        self._title = title

    @property
    def description(self):
        """
        **[Required]** Gets the description of this Ticket.
        The description of the issue addressed in the ticket.


        :return: The description of this Ticket.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Ticket.
        The description of the issue addressed in the ticket.


        :param description: The description of this Ticket.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this Ticket.
        The time when the ticket was created, in milliseconds since epoch time.


        :return: The time_created of this Ticket.
        :rtype: int
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Ticket.
        The time when the ticket was created, in milliseconds since epoch time.


        :param time_created: The time_created of this Ticket.
        :type: int
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Ticket.
        The time when the ticket was updated, in milliseconds since epoch time.


        :return: The time_updated of this Ticket.
        :rtype: int
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Ticket.
        The time when the ticket was updated, in milliseconds since epoch time.


        :param time_updated: The time_updated of this Ticket.
        :type: int
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Ticket.
        The current state of the ticket.

        Allowed values for this property are: "ACTIVE", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Ticket.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Ticket.
        The current state of the ticket.


        :param lifecycle_state: The lifecycle_state of this Ticket.
        :type: str
        """
        allowed_values = ["ACTIVE", "CLOSED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Ticket.
        Additional information about the current `lifecycleState`.

        Allowed values for this property are: "PENDING_WITH_ORACLE", "PENDING_WITH_CUSTOMER", "CLOSE_REQUESTED", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this Ticket.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Ticket.
        Additional information about the current `lifecycleState`.


        :param lifecycle_details: The lifecycle_details of this Ticket.
        :type: str
        """
        allowed_values = ["PENDING_WITH_ORACLE", "PENDING_WITH_CUSTOMER", "CLOSE_REQUESTED", "CLOSED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
