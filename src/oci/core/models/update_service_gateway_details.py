# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateServiceGatewayDetails(object):
    """
    UpdateServiceGatewayDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateServiceGatewayDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param block_traffic:
            The value to assign to the block_traffic property of this UpdateServiceGatewayDetails.
        :type block_traffic: bool

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateServiceGatewayDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateServiceGatewayDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateServiceGatewayDetails.
        :type freeform_tags: dict(str, str)

        :param services:
            The value to assign to the services property of this UpdateServiceGatewayDetails.
        :type services: list[ServiceIdRequestDetails]

        """
        self.swagger_types = {
            'block_traffic': 'bool',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'services': 'list[ServiceIdRequestDetails]'
        }

        self.attribute_map = {
            'block_traffic': 'blockTraffic',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'services': 'services'
        }

        self._block_traffic = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._services = None

    @property
    def block_traffic(self):
        """
        Gets the block_traffic of this UpdateServiceGatewayDetails.
        Whether the service gateway blocks all traffic through it. The default is `false`. When
        this is `true`, traffic is not routed to any services, regardless of route rules.

        Example: `true`


        :return: The block_traffic of this UpdateServiceGatewayDetails.
        :rtype: bool
        """
        return self._block_traffic

    @block_traffic.setter
    def block_traffic(self, block_traffic):
        """
        Sets the block_traffic of this UpdateServiceGatewayDetails.
        Whether the service gateway blocks all traffic through it. The default is `false`. When
        this is `true`, traffic is not routed to any services, regardless of route rules.

        Example: `true`


        :param block_traffic: The block_traffic of this UpdateServiceGatewayDetails.
        :type: bool
        """
        self._block_traffic = block_traffic

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateServiceGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateServiceGatewayDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateServiceGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateServiceGatewayDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateServiceGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateServiceGatewayDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateServiceGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateServiceGatewayDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateServiceGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateServiceGatewayDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateServiceGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateServiceGatewayDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def services(self):
        """
        Gets the services of this UpdateServiceGatewayDetails.
        List of all the services you want enabled on this service gateway. Sending an empty list
        means you want to disable all services. Omitting this parameter entirely keeps the
        existing list of services intact.

        You can also enable or disable a particular service by using
        :func:`attach_service_id` and
        :func:`detach_service_id`.

        For each enabled service, make sure there's a route rule with the service's `cidrBlock`
        as the rule's destination CIDR and the service gateway as the rule's target. See
        :class:`RouteTable`.


        :return: The services of this UpdateServiceGatewayDetails.
        :rtype: list[ServiceIdRequestDetails]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this UpdateServiceGatewayDetails.
        List of all the services you want enabled on this service gateway. Sending an empty list
        means you want to disable all services. Omitting this parameter entirely keeps the
        existing list of services intact.

        You can also enable or disable a particular service by using
        :func:`attach_service_id` and
        :func:`detach_service_id`.

        For each enabled service, make sure there's a route rule with the service's `cidrBlock`
        as the rule's destination CIDR and the service gateway as the rule's target. See
        :class:`RouteTable`.


        :param services: The services of this UpdateServiceGatewayDetails.
        :type: list[ServiceIdRequestDetails]
        """
        self._services = services

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
