# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConsoleConnection(object):

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConsoleConnection object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this InstanceConsoleConnection.
        :type compartment_id: str

        :param connection_string:
            The value to assign to the connection_string property of this InstanceConsoleConnection.
        :type connection_string: str

        :param fingerprint:
            The value to assign to the fingerprint property of this InstanceConsoleConnection.
        :type fingerprint: str

        :param id:
            The value to assign to the id property of this InstanceConsoleConnection.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this InstanceConsoleConnection.
        :type instance_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InstanceConsoleConnection.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'connection_string': 'str',
            'fingerprint': 'str',
            'id': 'str',
            'instance_id': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'connection_string': 'connectionString',
            'fingerprint': 'fingerprint',
            'id': 'id',
            'instance_id': 'instanceId',
            'lifecycle_state': 'lifecycleState'
        }

        self._compartment_id = None
        self._connection_string = None
        self._fingerprint = None
        self._id = None
        self._instance_id = None
        self._lifecycle_state = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this InstanceConsoleConnection.
        The OCID of the compartment to contain the console connection.


        :return: The compartment_id of this InstanceConsoleConnection.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InstanceConsoleConnection.
        The OCID of the compartment to contain the console connection.


        :param compartment_id: The compartment_id of this InstanceConsoleConnection.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def connection_string(self):
        """
        Gets the connection_string of this InstanceConsoleConnection.
        The SSH connection string for the console connection.


        :return: The connection_string of this InstanceConsoleConnection.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this InstanceConsoleConnection.
        The SSH connection string for the console connection.


        :param connection_string: The connection_string of this InstanceConsoleConnection.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def fingerprint(self):
        """
        Gets the fingerprint of this InstanceConsoleConnection.
        The SSH public key fingerprint for the console connection.


        :return: The fingerprint of this InstanceConsoleConnection.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this InstanceConsoleConnection.
        The SSH public key fingerprint for the console connection.


        :param fingerprint: The fingerprint of this InstanceConsoleConnection.
        :type: str
        """
        self._fingerprint = fingerprint

    @property
    def id(self):
        """
        Gets the id of this InstanceConsoleConnection.
        The OCID of the console connection.


        :return: The id of this InstanceConsoleConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceConsoleConnection.
        The OCID of the console connection.


        :param id: The id of this InstanceConsoleConnection.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        Gets the instance_id of this InstanceConsoleConnection.
        The OCID of the instance the console connection connects to.


        :return: The instance_id of this InstanceConsoleConnection.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this InstanceConsoleConnection.
        The OCID of the instance the console connection connects to.


        :param instance_id: The instance_id of this InstanceConsoleConnection.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this InstanceConsoleConnection.
        The current state of the console connection.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this InstanceConsoleConnection.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InstanceConsoleConnection.
        The current state of the console connection.


        :param lifecycle_state: The lifecycle_state of this InstanceConsoleConnection.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]
        if lifecycle_state not in allowed_values:
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
