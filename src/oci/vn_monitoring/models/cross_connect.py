# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CrossConnect(object):
    """
    For use with Oracle Cloud Infrastructure FastConnect. A cross-connect represents a
    physical connection between an existing network and Oracle. Customers who are colocated
    with Oracle in a FastConnect location create and use cross-connects. For more
    information, see `FastConnect Overview`__.

    Oracle recommends you create each cross-connect in a
    :class:`CrossConnectGroup` so you can use link aggregation
    with the connection.

    **Note:** If you're a provider who is setting up a physical connection to Oracle so customers
    can use FastConnect over the connection, be aware that your connection is modeled the
    same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, and so on).

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a CrossConnect.
    #: This constant has a value of "PENDING_CUSTOMER"
    LIFECYCLE_STATE_PENDING_CUSTOMER = "PENDING_CUSTOMER"

    #: A constant which can be used with the lifecycle_state property of a CrossConnect.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a CrossConnect.
    #: This constant has a value of "PROVISIONED"
    LIFECYCLE_STATE_PROVISIONED = "PROVISIONED"

    #: A constant which can be used with the lifecycle_state property of a CrossConnect.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CrossConnect.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a CrossConnect.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new CrossConnect object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CrossConnect.
        :type compartment_id: str

        :param cross_connect_group_id:
            The value to assign to the cross_connect_group_id property of this CrossConnect.
        :type cross_connect_group_id: str

        :param display_name:
            The value to assign to the display_name property of this CrossConnect.
        :type display_name: str

        :param id:
            The value to assign to the id property of this CrossConnect.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CrossConnect.
            Allowed values for this property are: "PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"
        :type lifecycle_state: str

        :param location_name:
            The value to assign to the location_name property of this CrossConnect.
        :type location_name: str

        :param port_name:
            The value to assign to the port_name property of this CrossConnect.
        :type port_name: str

        :param port_speed_shape_name:
            The value to assign to the port_speed_shape_name property of this CrossConnect.
        :type port_speed_shape_name: str

        :param time_created:
            The value to assign to the time_created property of this CrossConnect.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'cross_connect_group_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'location_name': 'str',
            'port_name': 'str',
            'port_speed_shape_name': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cross_connect_group_id': 'crossConnectGroupId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'location_name': 'locationName',
            'port_name': 'portName',
            'port_speed_shape_name': 'portSpeedShapeName',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._cross_connect_group_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._location_name = None
        self._port_name = None
        self._port_speed_shape_name = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CrossConnect.
        The `OCID`__ of the compartment containing the cross-connect group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CrossConnect.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CrossConnect.
        The `OCID`__ of the compartment containing the cross-connect group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CrossConnect.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cross_connect_group_id(self):
        """
        Gets the cross_connect_group_id of this CrossConnect.
        The `OCID`__ of the cross-connect group this cross-connect belongs to (if any).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The cross_connect_group_id of this CrossConnect.
        :rtype: str
        """
        return self._cross_connect_group_id

    @cross_connect_group_id.setter
    def cross_connect_group_id(self, cross_connect_group_id):
        """
        Sets the cross_connect_group_id of this CrossConnect.
        The `OCID`__ of the cross-connect group this cross-connect belongs to (if any).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param cross_connect_group_id: The cross_connect_group_id of this CrossConnect.
        :type: str
        """
        self._cross_connect_group_id = cross_connect_group_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CrossConnect.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CrossConnect.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CrossConnect.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CrossConnect.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this CrossConnect.
        The cross-connect's Oracle ID (OCID).


        :return: The id of this CrossConnect.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CrossConnect.
        The cross-connect's Oracle ID (OCID).


        :param id: The id of this CrossConnect.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CrossConnect.
        The cross-connect's current state.

        Allowed values for this property are: "PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"


        :return: The lifecycle_state of this CrossConnect.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CrossConnect.
        The cross-connect's current state.


        :param lifecycle_state: The lifecycle_state of this CrossConnect.
        :type: str
        """
        allowed_values = ["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def location_name(self):
        """
        Gets the location_name of this CrossConnect.
        The name of the FastConnect location where this cross-connect is installed.


        :return: The location_name of this CrossConnect.
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """
        Sets the location_name of this CrossConnect.
        The name of the FastConnect location where this cross-connect is installed.


        :param location_name: The location_name of this CrossConnect.
        :type: str
        """
        self._location_name = location_name

    @property
    def port_name(self):
        """
        Gets the port_name of this CrossConnect.
        A string identifying the meet-me room port for this cross-connect.


        :return: The port_name of this CrossConnect.
        :rtype: str
        """
        return self._port_name

    @port_name.setter
    def port_name(self, port_name):
        """
        Sets the port_name of this CrossConnect.
        A string identifying the meet-me room port for this cross-connect.


        :param port_name: The port_name of this CrossConnect.
        :type: str
        """
        self._port_name = port_name

    @property
    def port_speed_shape_name(self):
        """
        Gets the port_speed_shape_name of this CrossConnect.
        The port speed for this cross-connect.

        Example: `10 Gbps`


        :return: The port_speed_shape_name of this CrossConnect.
        :rtype: str
        """
        return self._port_speed_shape_name

    @port_speed_shape_name.setter
    def port_speed_shape_name(self, port_speed_shape_name):
        """
        Sets the port_speed_shape_name of this CrossConnect.
        The port speed for this cross-connect.

        Example: `10 Gbps`


        :param port_speed_shape_name: The port_speed_shape_name of this CrossConnect.
        :type: str
        """
        self._port_speed_shape_name = port_speed_shape_name

    @property
    def time_created(self):
        """
        Gets the time_created of this CrossConnect.
        The date and time the cross-connect was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CrossConnect.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CrossConnect.
        The date and time the cross-connect was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CrossConnect.
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
