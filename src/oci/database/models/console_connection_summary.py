# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConsoleConnectionSummary(object):
    """
    The `InstanceConsoleConnection` API provides you with console access to dbnode
    enabling you to troubleshoot malfunctioning dbnode.
    """

    #: A constant which can be used with the lifecycle_state property of a ConsoleConnectionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ConsoleConnectionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ConsoleConnectionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ConsoleConnectionSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ConsoleConnectionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ConsoleConnectionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ConsoleConnectionSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ConsoleConnectionSummary.
        :type compartment_id: str

        :param db_node_id:
            The value to assign to the db_node_id property of this ConsoleConnectionSummary.
        :type db_node_id: str

        :param connection_string:
            The value to assign to the connection_string property of this ConsoleConnectionSummary.
        :type connection_string: str

        :param fingerprint:
            The value to assign to the fingerprint property of this ConsoleConnectionSummary.
        :type fingerprint: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConsoleConnectionSummary.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'db_node_id': 'str',
            'connection_string': 'str',
            'fingerprint': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'db_node_id': 'dbNodeId',
            'connection_string': 'connectionString',
            'fingerprint': 'fingerprint',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._compartment_id = None
        self._db_node_id = None
        self._connection_string = None
        self._fingerprint = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ConsoleConnectionSummary.
        The OCID of the console connection.


        :return: The id of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConsoleConnectionSummary.
        The OCID of the console connection.


        :param id: The id of this ConsoleConnectionSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ConsoleConnectionSummary.
        The OCID of the compartment to contain the console connection.


        :return: The compartment_id of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ConsoleConnectionSummary.
        The OCID of the compartment to contain the console connection.


        :param compartment_id: The compartment_id of this ConsoleConnectionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_node_id(self):
        """
        **[Required]** Gets the db_node_id of this ConsoleConnectionSummary.
        The OCID of the database node.


        :return: The db_node_id of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._db_node_id

    @db_node_id.setter
    def db_node_id(self, db_node_id):
        """
        Sets the db_node_id of this ConsoleConnectionSummary.
        The OCID of the database node.


        :param db_node_id: The db_node_id of this ConsoleConnectionSummary.
        :type: str
        """
        self._db_node_id = db_node_id

    @property
    def connection_string(self):
        """
        **[Required]** Gets the connection_string of this ConsoleConnectionSummary.
        The SSH connection string for the console connection.


        :return: The connection_string of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this ConsoleConnectionSummary.
        The SSH connection string for the console connection.


        :param connection_string: The connection_string of this ConsoleConnectionSummary.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def fingerprint(self):
        """
        **[Required]** Gets the fingerprint of this ConsoleConnectionSummary.
        The SSH public key fingerprint for the console connection.


        :return: The fingerprint of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this ConsoleConnectionSummary.
        The SSH public key fingerprint for the console connection.


        :param fingerprint: The fingerprint of this ConsoleConnectionSummary.
        :type: str
        """
        self._fingerprint = fingerprint

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ConsoleConnectionSummary.
        The current state of the console connection.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ConsoleConnectionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConsoleConnectionSummary.
        The current state of the console connection.


        :param lifecycle_state: The lifecycle_state of this ConsoleConnectionSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
