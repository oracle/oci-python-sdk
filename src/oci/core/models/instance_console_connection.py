# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConsoleConnection(object):
    """
    The `InstanceConsoleConnection` API provides you with console access to Compute instances,
    enabling you to troubleshoot malfunctioning instances remotely.

    For more information about console access, see
    `Accessing the Console`__.

    __ https://docs.cloud.oracle.com/Content/Compute/References/serialconsole.htm
    """

    #: A constant which can be used with the lifecycle_state property of a InstanceConsoleConnection.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a InstanceConsoleConnection.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a InstanceConsoleConnection.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a InstanceConsoleConnection.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a InstanceConsoleConnection.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConsoleConnection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this InstanceConsoleConnection.
        :type compartment_id: str

        :param connection_string:
            The value to assign to the connection_string property of this InstanceConsoleConnection.
        :type connection_string: str

        :param defined_tags:
            The value to assign to the defined_tags property of this InstanceConsoleConnection.
        :type defined_tags: dict(str, dict(str, object))

        :param fingerprint:
            The value to assign to the fingerprint property of this InstanceConsoleConnection.
        :type fingerprint: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this InstanceConsoleConnection.
        :type freeform_tags: dict(str, str)

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

        :param vnc_connection_string:
            The value to assign to the vnc_connection_string property of this InstanceConsoleConnection.
        :type vnc_connection_string: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'connection_string': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'fingerprint': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'instance_id': 'str',
            'lifecycle_state': 'str',
            'vnc_connection_string': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'connection_string': 'connectionString',
            'defined_tags': 'definedTags',
            'fingerprint': 'fingerprint',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'instance_id': 'instanceId',
            'lifecycle_state': 'lifecycleState',
            'vnc_connection_string': 'vncConnectionString'
        }

        self._compartment_id = None
        self._connection_string = None
        self._defined_tags = None
        self._fingerprint = None
        self._freeform_tags = None
        self._id = None
        self._instance_id = None
        self._lifecycle_state = None
        self._vnc_connection_string = None

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
    def defined_tags(self):
        """
        Gets the defined_tags of this InstanceConsoleConnection.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this InstanceConsoleConnection.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this InstanceConsoleConnection.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this InstanceConsoleConnection.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

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
    def freeform_tags(self):
        """
        Gets the freeform_tags of this InstanceConsoleConnection.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this InstanceConsoleConnection.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this InstanceConsoleConnection.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this InstanceConsoleConnection.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

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
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def vnc_connection_string(self):
        """
        Gets the vnc_connection_string of this InstanceConsoleConnection.
        The SSH connection string for the SSH tunnel used to
        connect to the console connection over VNC.


        :return: The vnc_connection_string of this InstanceConsoleConnection.
        :rtype: str
        """
        return self._vnc_connection_string

    @vnc_connection_string.setter
    def vnc_connection_string(self, vnc_connection_string):
        """
        Sets the vnc_connection_string of this InstanceConsoleConnection.
        The SSH connection string for the SSH tunnel used to
        connect to the console connection over VNC.


        :param vnc_connection_string: The vnc_connection_string of this InstanceConsoleConnection.
        :type: str
        """
        self._vnc_connection_string = vnc_connection_string

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
