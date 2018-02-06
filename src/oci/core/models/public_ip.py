# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublicIp(object):

    def __init__(self, **kwargs):
        """
        Initializes a new PublicIp object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this PublicIp.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PublicIp.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this PublicIp.
        :type display_name: str

        :param id:
            The value to assign to the id property of this PublicIp.
        :type id: str

        :param ip_address:
            The value to assign to the ip_address property of this PublicIp.
        :type ip_address: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PublicIp.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifetime:
            The value to assign to the lifetime property of this PublicIp.
            Allowed values for this property are: "EPHEMERAL", "RESERVED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifetime: str

        :param private_ip_id:
            The value to assign to the private_ip_id property of this PublicIp.
        :type private_ip_id: str

        :param scope:
            The value to assign to the scope property of this PublicIp.
            Allowed values for this property are: "REGION", "AVAILABILITY_DOMAIN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scope: str

        :param time_created:
            The value to assign to the time_created property of this PublicIp.
        :type time_created: datetime

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'ip_address': 'str',
            'lifecycle_state': 'str',
            'lifetime': 'str',
            'private_ip_id': 'str',
            'scope': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'ip_address': 'ipAddress',
            'lifecycle_state': 'lifecycleState',
            'lifetime': 'lifetime',
            'private_ip_id': 'privateIpId',
            'scope': 'scope',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._ip_address = None
        self._lifecycle_state = None
        self._lifetime = None
        self._private_ip_id = None
        self._scope = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this PublicIp.
        The public IP's Availability Domain. This property is set only for ephemeral public IPs
        (that is, when the `scope` of the public IP is set to AVAILABILITY_DOMAIN). The value
        is the Availability Domain of the assigned private IP.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this PublicIp.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this PublicIp.
        The public IP's Availability Domain. This property is set only for ephemeral public IPs
        (that is, when the `scope` of the public IP is set to AVAILABILITY_DOMAIN). The value
        is the Availability Domain of the assigned private IP.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this PublicIp.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this PublicIp.
        The OCID of the compartment containing the public IP. For an ephemeral public IP, this is
        the same compartment as the private IP's. For a reserved public IP that is currently assigned,
        this can be a different compartment than the assigned private IP's.


        :return: The compartment_id of this PublicIp.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PublicIp.
        The OCID of the compartment containing the public IP. For an ephemeral public IP, this is
        the same compartment as the private IP's. For a reserved public IP that is currently assigned,
        this can be a different compartment than the assigned private IP's.


        :param compartment_id: The compartment_id of this PublicIp.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this PublicIp.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this PublicIp.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PublicIp.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this PublicIp.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this PublicIp.
        The public IP's Oracle ID (OCID).


        :return: The id of this PublicIp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PublicIp.
        The public IP's Oracle ID (OCID).


        :param id: The id of this PublicIp.
        :type: str
        """
        self._id = id

    @property
    def ip_address(self):
        """
        Gets the ip_address of this PublicIp.
        The public IP address of the `publicIp` object.

        Example: `129.146.2.1`


        :return: The ip_address of this PublicIp.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this PublicIp.
        The public IP address of the `publicIp` object.

        Example: `129.146.2.1`


        :param ip_address: The ip_address of this PublicIp.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this PublicIp.
        The public IP's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PublicIp.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PublicIp.
        The public IP's current state.


        :param lifecycle_state: The lifecycle_state of this PublicIp.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifetime(self):
        """
        Gets the lifetime of this PublicIp.
        Defines when the public IP is deleted and released back to Oracle's public IP pool.

        * `EPHEMERAL`: The lifetime is tied to the lifetime of its assigned private IP. The
        ephemeral public IP is automatically deleted when its private IP is deleted, when
        the VNIC is terminated, or when the instance is terminated. An ephemeral
        public IP must always be assigned to a private IP.

        * `RESERVED`: You control the public IP's lifetime. You can delete a reserved public IP
        whenever you like. It does not need to be assigned to a private IP at all times.

        For more information and comparison of the two types,
        see `Public IP Addresses`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingpublicIPs.htm

        Allowed values for this property are: "EPHEMERAL", "RESERVED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifetime of this PublicIp.
        :rtype: str
        """
        return self._lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        """
        Sets the lifetime of this PublicIp.
        Defines when the public IP is deleted and released back to Oracle's public IP pool.

        * `EPHEMERAL`: The lifetime is tied to the lifetime of its assigned private IP. The
        ephemeral public IP is automatically deleted when its private IP is deleted, when
        the VNIC is terminated, or when the instance is terminated. An ephemeral
        public IP must always be assigned to a private IP.

        * `RESERVED`: You control the public IP's lifetime. You can delete a reserved public IP
        whenever you like. It does not need to be assigned to a private IP at all times.

        For more information and comparison of the two types,
        see `Public IP Addresses`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingpublicIPs.htm


        :param lifetime: The lifetime of this PublicIp.
        :type: str
        """
        allowed_values = ["EPHEMERAL", "RESERVED"]
        if not value_allowed_none_or_none_sentinel(lifetime, allowed_values):
            lifetime = 'UNKNOWN_ENUM_VALUE'
        self._lifetime = lifetime

    @property
    def private_ip_id(self):
        """
        Gets the private_ip_id of this PublicIp.
        The OCID of the private IP that the public IP is currently assigned to, or in the
        process of being assigned to.


        :return: The private_ip_id of this PublicIp.
        :rtype: str
        """
        return self._private_ip_id

    @private_ip_id.setter
    def private_ip_id(self, private_ip_id):
        """
        Sets the private_ip_id of this PublicIp.
        The OCID of the private IP that the public IP is currently assigned to, or in the
        process of being assigned to.


        :param private_ip_id: The private_ip_id of this PublicIp.
        :type: str
        """
        self._private_ip_id = private_ip_id

    @property
    def scope(self):
        """
        Gets the scope of this PublicIp.
        Whether the public IP is regional or specific to a particular Availability Domain.

        * `REGION`: The public IP exists within a region and can be assigned to a private IP
        in any Availability Domain in the region. Reserved public IPs have `scope` = `REGION`.

        * `AVAILABILITY_DOMAIN`: The public IP exists within the Availability Domain of the private IP
        it's assigned to, which is specified by the `availabilityDomain` property of the public IP object.
        Ephemeral public IPs have `scope` = `AVAILABILITY_DOMAIN`.

        Allowed values for this property are: "REGION", "AVAILABILITY_DOMAIN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The scope of this PublicIp.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this PublicIp.
        Whether the public IP is regional or specific to a particular Availability Domain.

        * `REGION`: The public IP exists within a region and can be assigned to a private IP
        in any Availability Domain in the region. Reserved public IPs have `scope` = `REGION`.

        * `AVAILABILITY_DOMAIN`: The public IP exists within the Availability Domain of the private IP
        it's assigned to, which is specified by the `availabilityDomain` property of the public IP object.
        Ephemeral public IPs have `scope` = `AVAILABILITY_DOMAIN`.


        :param scope: The scope of this PublicIp.
        :type: str
        """
        allowed_values = ["REGION", "AVAILABILITY_DOMAIN"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            scope = 'UNKNOWN_ENUM_VALUE'
        self._scope = scope

    @property
    def time_created(self):
        """
        Gets the time_created of this PublicIp.
        The date and time the public IP was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this PublicIp.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PublicIp.
        The date and time the public IP was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this PublicIp.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
