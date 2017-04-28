# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class InternetGateway(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'is_enabled': 'bool',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'is_enabled': 'isEnabled',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._is_enabled = None
        self._lifecycle_state = None
        self._time_created = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this InternetGateway.
        The OCID of the compartment containing the Internet Gateway.


        :return: The compartment_id of this InternetGateway.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InternetGateway.
        The OCID of the compartment containing the Internet Gateway.


        :param compartment_id: The compartment_id of this InternetGateway.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this InternetGateway.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this InternetGateway.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InternetGateway.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this InternetGateway.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this InternetGateway.
        The Internet Gateway's Oracle ID (OCID).


        :return: The id of this InternetGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InternetGateway.
        The Internet Gateway's Oracle ID (OCID).


        :param id: The id of this InternetGateway.
        :type: str
        """
        self._id = id

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this InternetGateway.
        Whether the gateway is enabled. When the gateway is disabled, traffic is not
        routed to/from the Internet, regardless of route rules.


        :return: The is_enabled of this InternetGateway.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this InternetGateway.
        Whether the gateway is enabled. When the gateway is disabled, traffic is not
        routed to/from the Internet, regardless of route rules.


        :param is_enabled: The is_enabled of this InternetGateway.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this InternetGateway.
        The Internet Gateway's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this InternetGateway.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InternetGateway.
        The Internet Gateway's current state.


        :param lifecycle_state: The lifecycle_state of this InternetGateway.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this InternetGateway.
        The date and time the Internet Gateway was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this InternetGateway.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InternetGateway.
        The date and time the Internet Gateway was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this InternetGateway.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this InternetGateway.
        The OCID of the VCN the Internet Gateway belongs to.


        :return: The vcn_id of this InternetGateway.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this InternetGateway.
        The OCID of the VCN the Internet Gateway belongs to.


        :param vcn_id: The vcn_id of this InternetGateway.
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
