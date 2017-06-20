# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class IPSecConnection(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'cpe_id': 'str',
            'display_name': 'str',
            'drg_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'static_routes': 'list[str]',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cpe_id': 'cpeId',
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'static_routes': 'staticRoutes',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._cpe_id = None
        self._display_name = None
        self._drg_id = None
        self._id = None
        self._lifecycle_state = None
        self._static_routes = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this IPSecConnection.
        The OCID of the compartment containing the IPSec connection.


        :return: The compartment_id of this IPSecConnection.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IPSecConnection.
        The OCID of the compartment containing the IPSec connection.


        :param compartment_id: The compartment_id of this IPSecConnection.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cpe_id(self):
        """
        Gets the cpe_id of this IPSecConnection.
        The OCID of the CPE.


        :return: The cpe_id of this IPSecConnection.
        :rtype: str
        """
        return self._cpe_id

    @cpe_id.setter
    def cpe_id(self, cpe_id):
        """
        Sets the cpe_id of this IPSecConnection.
        The OCID of the CPE.


        :param cpe_id: The cpe_id of this IPSecConnection.
        :type: str
        """
        self._cpe_id = cpe_id

    @property
    def display_name(self):
        """
        Gets the display_name of this IPSecConnection.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this IPSecConnection.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this IPSecConnection.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this IPSecConnection.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        Gets the drg_id of this IPSecConnection.
        The OCID of the DRG.


        :return: The drg_id of this IPSecConnection.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this IPSecConnection.
        The OCID of the DRG.


        :param drg_id: The drg_id of this IPSecConnection.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def id(self):
        """
        Gets the id of this IPSecConnection.
        The IPSec connection's Oracle ID (OCID).


        :return: The id of this IPSecConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IPSecConnection.
        The IPSec connection's Oracle ID (OCID).


        :param id: The id of this IPSecConnection.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this IPSecConnection.
        The IPSec connection's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this IPSecConnection.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IPSecConnection.
        The IPSec connection's current state.


        :param lifecycle_state: The lifecycle_state of this IPSecConnection.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def static_routes(self):
        """
        Gets the static_routes of this IPSecConnection.
        Static routes to the CPE. At least one route must be included. The CIDR must not be a
        multicast address or class E address.

        Example: `10.0.1.0/24`


        :return: The static_routes of this IPSecConnection.
        :rtype: list[str]
        """
        return self._static_routes

    @static_routes.setter
    def static_routes(self, static_routes):
        """
        Sets the static_routes of this IPSecConnection.
        Static routes to the CPE. At least one route must be included. The CIDR must not be a
        multicast address or class E address.

        Example: `10.0.1.0/24`


        :param static_routes: The static_routes of this IPSecConnection.
        :type: list[str]
        """
        self._static_routes = static_routes

    @property
    def time_created(self):
        """
        Gets the time_created of this IPSecConnection.
        The date and time the IPSec connection was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this IPSecConnection.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IPSecConnection.
        The date and time the IPSec connection was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this IPSecConnection.
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
