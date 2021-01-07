# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceGateway(object):
    """
    Represents a router that lets your VCN privately access specific Oracle services such as Object
    Storage without exposing the VCN to the public internet. Traffic leaving the VCN and destined
    for a supported Oracle service (see :func:`list_services`) is
    routed through the service gateway and does not traverse the internet. The instances in the VCN
    do not need to have public IP addresses nor be in a public subnet. The VCN does not need an internet gateway
    for this traffic. For more information, see
    `Access to Oracle Services: Service Gateway`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Network/Tasks/servicegateway.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a ServiceGateway.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a ServiceGateway.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a ServiceGateway.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a ServiceGateway.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceGateway object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param block_traffic:
            The value to assign to the block_traffic property of this ServiceGateway.
        :type block_traffic: bool

        :param compartment_id:
            The value to assign to the compartment_id property of this ServiceGateway.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ServiceGateway.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ServiceGateway.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ServiceGateway.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this ServiceGateway.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ServiceGateway.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param route_table_id:
            The value to assign to the route_table_id property of this ServiceGateway.
        :type route_table_id: str

        :param services:
            The value to assign to the services property of this ServiceGateway.
        :type services: list[oci.core.models.ServiceIdResponseDetails]

        :param time_created:
            The value to assign to the time_created property of this ServiceGateway.
        :type time_created: datetime

        :param vcn_id:
            The value to assign to the vcn_id property of this ServiceGateway.
        :type vcn_id: str

        """
        self.swagger_types = {
            'block_traffic': 'bool',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'route_table_id': 'str',
            'services': 'list[ServiceIdResponseDetails]',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'block_traffic': 'blockTraffic',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'route_table_id': 'routeTableId',
            'services': 'services',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._block_traffic = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._route_table_id = None
        self._services = None
        self._time_created = None
        self._vcn_id = None

    @property
    def block_traffic(self):
        """
        **[Required]** Gets the block_traffic of this ServiceGateway.
        Whether the service gateway blocks all traffic through it. The default is `false`. When
        this is `true`, traffic is not routed to any services, regardless of route rules.

        Example: `true`


        :return: The block_traffic of this ServiceGateway.
        :rtype: bool
        """
        return self._block_traffic

    @block_traffic.setter
    def block_traffic(self, block_traffic):
        """
        Sets the block_traffic of this ServiceGateway.
        Whether the service gateway blocks all traffic through it. The default is `false`. When
        this is `true`, traffic is not routed to any services, regardless of route rules.

        Example: `true`


        :param block_traffic: The block_traffic of this ServiceGateway.
        :type: bool
        """
        self._block_traffic = block_traffic

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ServiceGateway.
        The `OCID`__ of the compartment that contains the
        service gateway.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ServiceGateway.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ServiceGateway.
        The `OCID`__ of the compartment that contains the
        service gateway.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ServiceGateway.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ServiceGateway.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ServiceGateway.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ServiceGateway.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ServiceGateway.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this ServiceGateway.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this ServiceGateway.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ServiceGateway.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this ServiceGateway.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ServiceGateway.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ServiceGateway.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ServiceGateway.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ServiceGateway.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ServiceGateway.
        The `OCID`__ of the service gateway.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ServiceGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ServiceGateway.
        The `OCID`__ of the service gateway.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ServiceGateway.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ServiceGateway.
        The service gateway's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ServiceGateway.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ServiceGateway.
        The service gateway's current state.


        :param lifecycle_state: The lifecycle_state of this ServiceGateway.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this ServiceGateway.
        The OCID of the route table the service gateway is using.
        For information about why you would associate a route table with a service gateway, see
        `Transit Routing: Private Access to Oracle Services`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/transitroutingoracleservices.htm


        :return: The route_table_id of this ServiceGateway.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this ServiceGateway.
        The OCID of the route table the service gateway is using.
        For information about why you would associate a route table with a service gateway, see
        `Transit Routing: Private Access to Oracle Services`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/transitroutingoracleservices.htm


        :param route_table_id: The route_table_id of this ServiceGateway.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def services(self):
        """
        **[Required]** Gets the services of this ServiceGateway.
        List of the :class:`Service` objects enabled for this service gateway.
        The list can be empty. You can enable a particular `Service` by using
        :func:`attach_service_id` or
        :func:`update_service_gateway`.


        :return: The services of this ServiceGateway.
        :rtype: list[oci.core.models.ServiceIdResponseDetails]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this ServiceGateway.
        List of the :class:`Service` objects enabled for this service gateway.
        The list can be empty. You can enable a particular `Service` by using
        :func:`attach_service_id` or
        :func:`update_service_gateway`.


        :param services: The services of this ServiceGateway.
        :type: list[oci.core.models.ServiceIdResponseDetails]
        """
        self._services = services

    @property
    def time_created(self):
        """
        Gets the time_created of this ServiceGateway.
        The date and time the service gateway was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ServiceGateway.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ServiceGateway.
        The date and time the service gateway was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ServiceGateway.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this ServiceGateway.
        The `OCID`__ of the VCN the service gateway
        belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this ServiceGateway.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this ServiceGateway.
        The `OCID`__ of the VCN the service gateway
        belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this ServiceGateway.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
