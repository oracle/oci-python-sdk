# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbHome(object):
    """
    A directory where Oracle Database software is installed. A bare metal DB system can have multiple database homes
    and each database home can run a different supported version of Oracle Database. A virtual machine DB system can have only one database home.
    For more information, see `Bare Metal and Virtual Machine DB Systems`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an
    administrator. If you're an administrator who needs to write policies to give users access,
    see `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Database/Concepts/overview.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a DbHome.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a DbHome.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a DbHome.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DbHome.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a DbHome.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a DbHome.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DbHome object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this DbHome.
        :type compartment_id: str

        :param db_system_id:
            The value to assign to the db_system_id property of this DbHome.
        :type db_system_id: str

        :param db_version:
            The value to assign to the db_version property of this DbHome.
        :type db_version: str

        :param display_name:
            The value to assign to the display_name property of this DbHome.
        :type display_name: str

        :param id:
            The value to assign to the id property of this DbHome.
        :type id: str

        :param last_patch_history_entry_id:
            The value to assign to the last_patch_history_entry_id property of this DbHome.
        :type last_patch_history_entry_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbHome.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this DbHome.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'db_system_id': 'str',
            'db_version': 'str',
            'display_name': 'str',
            'id': 'str',
            'last_patch_history_entry_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'db_system_id': 'dbSystemId',
            'db_version': 'dbVersion',
            'display_name': 'displayName',
            'id': 'id',
            'last_patch_history_entry_id': 'lastPatchHistoryEntryId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._db_system_id = None
        self._db_version = None
        self._display_name = None
        self._id = None
        self._last_patch_history_entry_id = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DbHome.
        The `OCID`__ of the compartment.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DbHome.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DbHome.
        The `OCID`__ of the compartment.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DbHome.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_system_id(self):
        """
        Gets the db_system_id of this DbHome.
        The `OCID`__ of the DB system.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The db_system_id of this DbHome.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this DbHome.
        The `OCID`__ of the DB system.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param db_system_id: The db_system_id of this DbHome.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def db_version(self):
        """
        **[Required]** Gets the db_version of this DbHome.
        The Oracle Database version.


        :return: The db_version of this DbHome.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this DbHome.
        The Oracle Database version.


        :param db_version: The db_version of this DbHome.
        :type: str
        """
        self._db_version = db_version

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DbHome.
        The user-provided name for the database home. The name does not need to be unique.


        :return: The display_name of this DbHome.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DbHome.
        The user-provided name for the database home. The name does not need to be unique.


        :param display_name: The display_name of this DbHome.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DbHome.
        The `OCID`__ of the database home.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DbHome.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbHome.
        The `OCID`__ of the database home.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DbHome.
        :type: str
        """
        self._id = id

    @property
    def last_patch_history_entry_id(self):
        """
        Gets the last_patch_history_entry_id of this DbHome.
        The `OCID`__ of the last patch history. This value is updated as soon as a patch operation is started.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The last_patch_history_entry_id of this DbHome.
        :rtype: str
        """
        return self._last_patch_history_entry_id

    @last_patch_history_entry_id.setter
    def last_patch_history_entry_id(self, last_patch_history_entry_id):
        """
        Sets the last_patch_history_entry_id of this DbHome.
        The `OCID`__ of the last patch history. This value is updated as soon as a patch operation is started.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param last_patch_history_entry_id: The last_patch_history_entry_id of this DbHome.
        :type: str
        """
        self._last_patch_history_entry_id = last_patch_history_entry_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DbHome.
        The current state of the database home.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DbHome.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbHome.
        The current state of the database home.


        :param lifecycle_state: The lifecycle_state of this DbHome.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this DbHome.
        The date and time the database home was created.


        :return: The time_created of this DbHome.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbHome.
        The date and time the database home was created.


        :param time_created: The time_created of this DbHome.
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
