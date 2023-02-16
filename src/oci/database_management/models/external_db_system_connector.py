# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalDbSystemConnector(object):
    """
    The details of an external DB system connector.
    """

    #: A constant which can be used with the connector_type property of a ExternalDbSystemConnector.
    #: This constant has a value of "MACS"
    CONNECTOR_TYPE_MACS = "MACS"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemConnector.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemConnector.
    #: This constant has a value of "NOT_CONNECTED"
    LIFECYCLE_STATE_NOT_CONNECTED = "NOT_CONNECTED"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemConnector.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemConnector.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemConnector.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemConnector.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemConnector.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemConnector.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalDbSystemConnector object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.ExternalDbSystemMacsConnector`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connector_type:
            The value to assign to the connector_type property of this ExternalDbSystemConnector.
            Allowed values for this property are: "MACS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connector_type: str

        :param id:
            The value to assign to the id property of this ExternalDbSystemConnector.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalDbSystemConnector.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalDbSystemConnector.
        :type compartment_id: str

        :param external_db_system_id:
            The value to assign to the external_db_system_id property of this ExternalDbSystemConnector.
        :type external_db_system_id: str

        :param connection_status:
            The value to assign to the connection_status property of this ExternalDbSystemConnector.
        :type connection_status: str

        :param connection_failure_message:
            The value to assign to the connection_failure_message property of this ExternalDbSystemConnector.
        :type connection_failure_message: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalDbSystemConnector.
            Allowed values for this property are: "CREATING", "NOT_CONNECTED", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalDbSystemConnector.
        :type lifecycle_details: str

        :param time_connection_status_last_updated:
            The value to assign to the time_connection_status_last_updated property of this ExternalDbSystemConnector.
        :type time_connection_status_last_updated: datetime

        :param time_created:
            The value to assign to the time_created property of this ExternalDbSystemConnector.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExternalDbSystemConnector.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'connector_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'external_db_system_id': 'str',
            'connection_status': 'str',
            'connection_failure_message': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_connection_status_last_updated': 'datetime',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'connector_type': 'connectorType',
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'external_db_system_id': 'externalDbSystemId',
            'connection_status': 'connectionStatus',
            'connection_failure_message': 'connectionFailureMessage',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_connection_status_last_updated': 'timeConnectionStatusLastUpdated',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._connector_type = None
        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._external_db_system_id = None
        self._connection_status = None
        self._connection_failure_message = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_connection_status_last_updated = None
        self._time_created = None
        self._time_updated = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectorType']

        if type == 'MACS':
            return 'ExternalDbSystemMacsConnector'
        else:
            return 'ExternalDbSystemConnector'

    @property
    def connector_type(self):
        """
        **[Required]** Gets the connector_type of this ExternalDbSystemConnector.
        The type of connector.

        Allowed values for this property are: "MACS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connector_type of this ExternalDbSystemConnector.
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """
        Sets the connector_type of this ExternalDbSystemConnector.
        The type of connector.


        :param connector_type: The connector_type of this ExternalDbSystemConnector.
        :type: str
        """
        allowed_values = ["MACS"]
        if not value_allowed_none_or_none_sentinel(connector_type, allowed_values):
            connector_type = 'UNKNOWN_ENUM_VALUE'
        self._connector_type = connector_type

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExternalDbSystemConnector.
        The `OCID`__ of the external DB system connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExternalDbSystemConnector.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalDbSystemConnector.
        The `OCID`__ of the external DB system connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExternalDbSystemConnector.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExternalDbSystemConnector.
        The user-friendly name for the external connector. The name does not have to be unique.


        :return: The display_name of this ExternalDbSystemConnector.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExternalDbSystemConnector.
        The user-friendly name for the external connector. The name does not have to be unique.


        :param display_name: The display_name of this ExternalDbSystemConnector.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExternalDbSystemConnector.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalDbSystemConnector.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalDbSystemConnector.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalDbSystemConnector.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def external_db_system_id(self):
        """
        **[Required]** Gets the external_db_system_id of this ExternalDbSystemConnector.
        The `OCID`__ of the external DB system that the connector is a part of.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_db_system_id of this ExternalDbSystemConnector.
        :rtype: str
        """
        return self._external_db_system_id

    @external_db_system_id.setter
    def external_db_system_id(self, external_db_system_id):
        """
        Sets the external_db_system_id of this ExternalDbSystemConnector.
        The `OCID`__ of the external DB system that the connector is a part of.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_db_system_id: The external_db_system_id of this ExternalDbSystemConnector.
        :type: str
        """
        self._external_db_system_id = external_db_system_id

    @property
    def connection_status(self):
        """
        Gets the connection_status of this ExternalDbSystemConnector.
        The status of connectivity to the external DB system component.


        :return: The connection_status of this ExternalDbSystemConnector.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this ExternalDbSystemConnector.
        The status of connectivity to the external DB system component.


        :param connection_status: The connection_status of this ExternalDbSystemConnector.
        :type: str
        """
        self._connection_status = connection_status

    @property
    def connection_failure_message(self):
        """
        Gets the connection_failure_message of this ExternalDbSystemConnector.
        The error message indicating the reason for connection failure or `null` if
        the connection was successful.


        :return: The connection_failure_message of this ExternalDbSystemConnector.
        :rtype: str
        """
        return self._connection_failure_message

    @connection_failure_message.setter
    def connection_failure_message(self, connection_failure_message):
        """
        Sets the connection_failure_message of this ExternalDbSystemConnector.
        The error message indicating the reason for connection failure or `null` if
        the connection was successful.


        :param connection_failure_message: The connection_failure_message of this ExternalDbSystemConnector.
        :type: str
        """
        self._connection_failure_message = connection_failure_message

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExternalDbSystemConnector.
        The current lifecycle state of the external DB system connector.

        Allowed values for this property are: "CREATING", "NOT_CONNECTED", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExternalDbSystemConnector.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExternalDbSystemConnector.
        The current lifecycle state of the external DB system connector.


        :param lifecycle_state: The lifecycle_state of this ExternalDbSystemConnector.
        :type: str
        """
        allowed_values = ["CREATING", "NOT_CONNECTED", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExternalDbSystemConnector.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExternalDbSystemConnector.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExternalDbSystemConnector.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExternalDbSystemConnector.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_connection_status_last_updated(self):
        """
        Gets the time_connection_status_last_updated of this ExternalDbSystemConnector.
        The date and time the connectionStatus of the external DB system connector was last updated.


        :return: The time_connection_status_last_updated of this ExternalDbSystemConnector.
        :rtype: datetime
        """
        return self._time_connection_status_last_updated

    @time_connection_status_last_updated.setter
    def time_connection_status_last_updated(self, time_connection_status_last_updated):
        """
        Sets the time_connection_status_last_updated of this ExternalDbSystemConnector.
        The date and time the connectionStatus of the external DB system connector was last updated.


        :param time_connection_status_last_updated: The time_connection_status_last_updated of this ExternalDbSystemConnector.
        :type: datetime
        """
        self._time_connection_status_last_updated = time_connection_status_last_updated

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ExternalDbSystemConnector.
        The date and time the external DB system connector was created.


        :return: The time_created of this ExternalDbSystemConnector.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExternalDbSystemConnector.
        The date and time the external DB system connector was created.


        :param time_created: The time_created of this ExternalDbSystemConnector.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ExternalDbSystemConnector.
        The date and time the external DB system connector was last updated.


        :return: The time_updated of this ExternalDbSystemConnector.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ExternalDbSystemConnector.
        The date and time the external DB system connector was last updated.


        :param time_updated: The time_updated of this ExternalDbSystemConnector.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
