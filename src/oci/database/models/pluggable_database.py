# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PluggableDatabase(object):
    """
    A pluggable database (PDB) is portable collection of schemas, schema objects, and non-schema objects that appears to an Oracle client as a non-container database. To use a PDB, it needs to be plugged into a CDB.
    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to a tenancy administrator. If you are an administrator who needs to write policies to give users access, see `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a PluggableDatabase.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a PluggableDatabase.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a PluggableDatabase.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a PluggableDatabase.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a PluggableDatabase.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a PluggableDatabase.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the open_mode property of a PluggableDatabase.
    #: This constant has a value of "READ_ONLY"
    OPEN_MODE_READ_ONLY = "READ_ONLY"

    #: A constant which can be used with the open_mode property of a PluggableDatabase.
    #: This constant has a value of "READ_WRITE"
    OPEN_MODE_READ_WRITE = "READ_WRITE"

    #: A constant which can be used with the open_mode property of a PluggableDatabase.
    #: This constant has a value of "MOUNTED"
    OPEN_MODE_MOUNTED = "MOUNTED"

    #: A constant which can be used with the open_mode property of a PluggableDatabase.
    #: This constant has a value of "MIGRATE"
    OPEN_MODE_MIGRATE = "MIGRATE"

    def __init__(self, **kwargs):
        """
        Initializes a new PluggableDatabase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PluggableDatabase.
        :type id: str

        :param container_database_id:
            The value to assign to the container_database_id property of this PluggableDatabase.
        :type container_database_id: str

        :param pdb_name:
            The value to assign to the pdb_name property of this PluggableDatabase.
        :type pdb_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PluggableDatabase.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PluggableDatabase.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this PluggableDatabase.
        :type time_created: datetime

        :param connection_strings:
            The value to assign to the connection_strings property of this PluggableDatabase.
        :type connection_strings: oci.database.models.PluggableDatabaseConnectionStrings

        :param open_mode:
            The value to assign to the open_mode property of this PluggableDatabase.
            Allowed values for this property are: "READ_ONLY", "READ_WRITE", "MOUNTED", "MIGRATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type open_mode: str

        :param is_restricted:
            The value to assign to the is_restricted property of this PluggableDatabase.
        :type is_restricted: bool

        :param compartment_id:
            The value to assign to the compartment_id property of this PluggableDatabase.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PluggableDatabase.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PluggableDatabase.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'container_database_id': 'str',
            'pdb_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'connection_strings': 'PluggableDatabaseConnectionStrings',
            'open_mode': 'str',
            'is_restricted': 'bool',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'container_database_id': 'containerDatabaseId',
            'pdb_name': 'pdbName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'connection_strings': 'connectionStrings',
            'open_mode': 'openMode',
            'is_restricted': 'isRestricted',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._container_database_id = None
        self._pdb_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._connection_strings = None
        self._open_mode = None
        self._is_restricted = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PluggableDatabase.
        The `OCID`__ of the pluggable database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this PluggableDatabase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PluggableDatabase.
        The `OCID`__ of the pluggable database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this PluggableDatabase.
        :type: str
        """
        self._id = id

    @property
    def container_database_id(self):
        """
        **[Required]** Gets the container_database_id of this PluggableDatabase.
        The `OCID`__ of the CDB.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The container_database_id of this PluggableDatabase.
        :rtype: str
        """
        return self._container_database_id

    @container_database_id.setter
    def container_database_id(self, container_database_id):
        """
        Sets the container_database_id of this PluggableDatabase.
        The `OCID`__ of the CDB.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param container_database_id: The container_database_id of this PluggableDatabase.
        :type: str
        """
        self._container_database_id = container_database_id

    @property
    def pdb_name(self):
        """
        **[Required]** Gets the pdb_name of this PluggableDatabase.
        The name for the pluggable database (PDB). The name is unique in the context of a :class:`Database`. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.


        :return: The pdb_name of this PluggableDatabase.
        :rtype: str
        """
        return self._pdb_name

    @pdb_name.setter
    def pdb_name(self, pdb_name):
        """
        Sets the pdb_name of this PluggableDatabase.
        The name for the pluggable database (PDB). The name is unique in the context of a :class:`Database`. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.


        :param pdb_name: The pdb_name of this PluggableDatabase.
        :type: str
        """
        self._pdb_name = pdb_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PluggableDatabase.
        The current state of the pluggable database.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PluggableDatabase.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PluggableDatabase.
        The current state of the pluggable database.


        :param lifecycle_state: The lifecycle_state of this PluggableDatabase.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this PluggableDatabase.
        Detailed message for the lifecycle state.


        :return: The lifecycle_details of this PluggableDatabase.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this PluggableDatabase.
        Detailed message for the lifecycle state.


        :param lifecycle_details: The lifecycle_details of this PluggableDatabase.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PluggableDatabase.
        The date and time the pluggable database was created.


        :return: The time_created of this PluggableDatabase.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PluggableDatabase.
        The date and time the pluggable database was created.


        :param time_created: The time_created of this PluggableDatabase.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def connection_strings(self):
        """
        Gets the connection_strings of this PluggableDatabase.

        :return: The connection_strings of this PluggableDatabase.
        :rtype: oci.database.models.PluggableDatabaseConnectionStrings
        """
        return self._connection_strings

    @connection_strings.setter
    def connection_strings(self, connection_strings):
        """
        Sets the connection_strings of this PluggableDatabase.

        :param connection_strings: The connection_strings of this PluggableDatabase.
        :type: oci.database.models.PluggableDatabaseConnectionStrings
        """
        self._connection_strings = connection_strings

    @property
    def open_mode(self):
        """
        **[Required]** Gets the open_mode of this PluggableDatabase.
        The mode that pluggable database is in. Open mode can only be changed to READ_ONLY or MIGRATE directly from the backend (within the Oracle Database software).

        Allowed values for this property are: "READ_ONLY", "READ_WRITE", "MOUNTED", "MIGRATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The open_mode of this PluggableDatabase.
        :rtype: str
        """
        return self._open_mode

    @open_mode.setter
    def open_mode(self, open_mode):
        """
        Sets the open_mode of this PluggableDatabase.
        The mode that pluggable database is in. Open mode can only be changed to READ_ONLY or MIGRATE directly from the backend (within the Oracle Database software).


        :param open_mode: The open_mode of this PluggableDatabase.
        :type: str
        """
        allowed_values = ["READ_ONLY", "READ_WRITE", "MOUNTED", "MIGRATE"]
        if not value_allowed_none_or_none_sentinel(open_mode, allowed_values):
            open_mode = 'UNKNOWN_ENUM_VALUE'
        self._open_mode = open_mode

    @property
    def is_restricted(self):
        """
        Gets the is_restricted of this PluggableDatabase.
        The restricted mode of the pluggable database. If a pluggable database is opened in restricted mode,
        the user needs both create a session and have restricted session privileges to connect to it.


        :return: The is_restricted of this PluggableDatabase.
        :rtype: bool
        """
        return self._is_restricted

    @is_restricted.setter
    def is_restricted(self, is_restricted):
        """
        Sets the is_restricted of this PluggableDatabase.
        The restricted mode of the pluggable database. If a pluggable database is opened in restricted mode,
        the user needs both create a session and have restricted session privileges to connect to it.


        :param is_restricted: The is_restricted of this PluggableDatabase.
        :type: bool
        """
        self._is_restricted = is_restricted

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PluggableDatabase.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this PluggableDatabase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PluggableDatabase.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this PluggableDatabase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PluggableDatabase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this PluggableDatabase.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PluggableDatabase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this PluggableDatabase.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PluggableDatabase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this PluggableDatabase.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PluggableDatabase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this PluggableDatabase.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
