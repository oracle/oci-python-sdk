# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Subscriber(object):
    """
    A subscriber, which encapsulates a number of clients and usage plans that they are subscribed to.
    """

    #: A constant which can be used with the lifecycle_state property of a Subscriber.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Subscriber.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Subscriber.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Subscriber.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Subscriber.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Subscriber.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Subscriber object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Subscriber.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Subscriber.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Subscriber.
        :type display_name: str

        :param clients:
            The value to assign to the clients property of this Subscriber.
        :type clients: list[oci.apigateway.models.Client]

        :param usage_plans:
            The value to assign to the usage_plans property of this Subscriber.
        :type usage_plans: list[str]

        :param time_created:
            The value to assign to the time_created property of this Subscriber.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Subscriber.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Subscriber.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Subscriber.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Subscriber.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Subscriber.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'clients': 'list[Client]',
            'usage_plans': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'clients': 'clients',
            'usage_plans': 'usagePlans',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._clients = None
        self._usage_plans = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Subscriber.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Subscriber.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Subscriber.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Subscriber.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Subscriber.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Subscriber.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Subscriber.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Subscriber.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Subscriber.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this Subscriber.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Subscriber.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this Subscriber.
        :type: str
        """
        self._display_name = display_name

    @property
    def clients(self):
        """
        **[Required]** Gets the clients of this Subscriber.
        The clients belonging to this subscriber.


        :return: The clients of this Subscriber.
        :rtype: list[oci.apigateway.models.Client]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """
        Sets the clients of this Subscriber.
        The clients belonging to this subscriber.


        :param clients: The clients of this Subscriber.
        :type: list[oci.apigateway.models.Client]
        """
        self._clients = clients

    @property
    def usage_plans(self):
        """
        **[Required]** Gets the usage_plans of this Subscriber.
        An array of `OCID`__s of usage
        plan resources.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The usage_plans of this Subscriber.
        :rtype: list[str]
        """
        return self._usage_plans

    @usage_plans.setter
    def usage_plans(self, usage_plans):
        """
        Sets the usage_plans of this Subscriber.
        An array of `OCID`__s of usage
        plan resources.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param usage_plans: The usage_plans of this Subscriber.
        :type: list[str]
        """
        self._usage_plans = usage_plans

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Subscriber.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this Subscriber.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Subscriber.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this Subscriber.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Subscriber.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this Subscriber.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Subscriber.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this Subscriber.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Subscriber.
        The current state of the subscriber.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Subscriber.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Subscriber.
        The current state of the subscriber.


        :param lifecycle_state: The lifecycle_state of this Subscriber.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Subscriber.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a
        resource in a Failed state.


        :return: The lifecycle_details of this Subscriber.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Subscriber.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a
        resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this Subscriber.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Subscriber.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Subscriber.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Subscriber.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Subscriber.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Subscriber.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Subscriber.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Subscriber.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Subscriber.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
