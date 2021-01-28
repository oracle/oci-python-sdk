# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalDatabaseConnector(object):
    """
    An Oracle Cloud Infrastructure resource used to connect to an external Oracle Database.
    This resource stores the database connection string, user credentials, and related details that allow you to
    manage your external database using the Oracle Cloud Infrastructure Console and API interfaces.
    """

    #: A constant which can be used with the lifecycle_state property of a ExternalDatabaseConnector.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a ExternalDatabaseConnector.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a ExternalDatabaseConnector.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalDatabaseConnector.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalDatabaseConnector.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a ExternalDatabaseConnector.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the connector_type property of a ExternalDatabaseConnector.
    #: This constant has a value of "MACS"
    CONNECTOR_TYPE_MACS = "MACS"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalDatabaseConnector object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.ExternalMacsConnector`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalDatabaseConnector.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExternalDatabaseConnector.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ExternalDatabaseConnector.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ExternalDatabaseConnector.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ExternalDatabaseConnector.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalDatabaseConnector.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalDatabaseConnector.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ExternalDatabaseConnector.
        :type time_created: datetime

        :param connector_type:
            The value to assign to the connector_type property of this ExternalDatabaseConnector.
            Allowed values for this property are: "MACS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connector_type: str

        :param external_database_id:
            The value to assign to the external_database_id property of this ExternalDatabaseConnector.
        :type external_database_id: str

        :param connection_status:
            The value to assign to the connection_status property of this ExternalDatabaseConnector.
        :type connection_status: str

        :param time_connection_status_last_updated:
            The value to assign to the time_connection_status_last_updated property of this ExternalDatabaseConnector.
        :type time_connection_status_last_updated: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'connector_type': 'str',
            'external_database_id': 'str',
            'connection_status': 'str',
            'time_connection_status_last_updated': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'connector_type': 'connectorType',
            'external_database_id': 'externalDatabaseId',
            'connection_status': 'connectionStatus',
            'time_connection_status_last_updated': 'timeConnectionStatusLastUpdated'
        }

        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._connector_type = None
        self._external_database_id = None
        self._connection_status = None
        self._time_connection_status_last_updated = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectorType']

        if type == 'MACS':
            return 'ExternalMacsConnector'
        else:
            return 'ExternalDatabaseConnector'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExternalDatabaseConnector.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalDatabaseConnector.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalDatabaseConnector.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalDatabaseConnector.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ExternalDatabaseConnector.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ExternalDatabaseConnector.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExternalDatabaseConnector.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ExternalDatabaseConnector.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ExternalDatabaseConnector.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ExternalDatabaseConnector.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExternalDatabaseConnector.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ExternalDatabaseConnector.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExternalDatabaseConnector.
        The user-friendly name for the
        :func:`create_external_database_connector_details`.
        The name does not have to be unique.


        :return: The display_name of this ExternalDatabaseConnector.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExternalDatabaseConnector.
        The user-friendly name for the
        :func:`create_external_database_connector_details`.
        The name does not have to be unique.


        :param display_name: The display_name of this ExternalDatabaseConnector.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExternalDatabaseConnector.
        The `OCID`__ of the
        :func:`create_external_database_connector_details`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExternalDatabaseConnector.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalDatabaseConnector.
        The `OCID`__ of the
        :func:`create_external_database_connector_details`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExternalDatabaseConnector.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExternalDatabaseConnector.
        The current lifecycle state of the external database connector resource.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExternalDatabaseConnector.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExternalDatabaseConnector.
        The current lifecycle state of the external database connector resource.


        :param lifecycle_state: The lifecycle_state of this ExternalDatabaseConnector.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExternalDatabaseConnector.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExternalDatabaseConnector.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExternalDatabaseConnector.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExternalDatabaseConnector.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ExternalDatabaseConnector.
        The date and time the external connector was created.


        :return: The time_created of this ExternalDatabaseConnector.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExternalDatabaseConnector.
        The date and time the external connector was created.


        :param time_created: The time_created of this ExternalDatabaseConnector.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def connector_type(self):
        """
        **[Required]** Gets the connector_type of this ExternalDatabaseConnector.
        The type of connector used by the external database resource.

        Allowed values for this property are: "MACS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connector_type of this ExternalDatabaseConnector.
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """
        Sets the connector_type of this ExternalDatabaseConnector.
        The type of connector used by the external database resource.


        :param connector_type: The connector_type of this ExternalDatabaseConnector.
        :type: str
        """
        allowed_values = ["MACS"]
        if not value_allowed_none_or_none_sentinel(connector_type, allowed_values):
            connector_type = 'UNKNOWN_ENUM_VALUE'
        self._connector_type = connector_type

    @property
    def external_database_id(self):
        """
        **[Required]** Gets the external_database_id of this ExternalDatabaseConnector.
        The `OCID`__ of the external database resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_database_id of this ExternalDatabaseConnector.
        :rtype: str
        """
        return self._external_database_id

    @external_database_id.setter
    def external_database_id(self, external_database_id):
        """
        Sets the external_database_id of this ExternalDatabaseConnector.
        The `OCID`__ of the external database resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_database_id: The external_database_id of this ExternalDatabaseConnector.
        :type: str
        """
        self._external_database_id = external_database_id

    @property
    def connection_status(self):
        """
        **[Required]** Gets the connection_status of this ExternalDatabaseConnector.
        The status of connectivity to the external database.


        :return: The connection_status of this ExternalDatabaseConnector.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this ExternalDatabaseConnector.
        The status of connectivity to the external database.


        :param connection_status: The connection_status of this ExternalDatabaseConnector.
        :type: str
        """
        self._connection_status = connection_status

    @property
    def time_connection_status_last_updated(self):
        """
        **[Required]** Gets the time_connection_status_last_updated of this ExternalDatabaseConnector.
        The date and time the connectionStatus of this external connector was last updated.


        :return: The time_connection_status_last_updated of this ExternalDatabaseConnector.
        :rtype: datetime
        """
        return self._time_connection_status_last_updated

    @time_connection_status_last_updated.setter
    def time_connection_status_last_updated(self, time_connection_status_last_updated):
        """
        Sets the time_connection_status_last_updated of this ExternalDatabaseConnector.
        The date and time the connectionStatus of this external connector was last updated.


        :param time_connection_status_last_updated: The time_connection_status_last_updated of this ExternalDatabaseConnector.
        :type: datetime
        """
        self._time_connection_status_last_updated = time_connection_status_last_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
