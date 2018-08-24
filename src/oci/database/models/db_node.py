# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbNode(object):
    """
    A server where Oracle Database software is running.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a DbNode.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a DbNode.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a DbNode.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DbNode.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a DbNode.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a DbNode.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a DbNode.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a DbNode.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a DbNode.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DbNode object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backup_vnic_id:
            The value to assign to the backup_vnic_id property of this DbNode.
        :type backup_vnic_id: str

        :param db_system_id:
            The value to assign to the db_system_id property of this DbNode.
        :type db_system_id: str

        :param hostname:
            The value to assign to the hostname property of this DbNode.
        :type hostname: str

        :param id:
            The value to assign to the id property of this DbNode.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbNode.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param software_storage_size_in_gb:
            The value to assign to the software_storage_size_in_gb property of this DbNode.
        :type software_storage_size_in_gb: int

        :param time_created:
            The value to assign to the time_created property of this DbNode.
        :type time_created: datetime

        :param vnic_id:
            The value to assign to the vnic_id property of this DbNode.
        :type vnic_id: str

        """
        self.swagger_types = {
            'backup_vnic_id': 'str',
            'db_system_id': 'str',
            'hostname': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'software_storage_size_in_gb': 'int',
            'time_created': 'datetime',
            'vnic_id': 'str'
        }

        self.attribute_map = {
            'backup_vnic_id': 'backupVnicId',
            'db_system_id': 'dbSystemId',
            'hostname': 'hostname',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'software_storage_size_in_gb': 'softwareStorageSizeInGB',
            'time_created': 'timeCreated',
            'vnic_id': 'vnicId'
        }

        self._backup_vnic_id = None
        self._db_system_id = None
        self._hostname = None
        self._id = None
        self._lifecycle_state = None
        self._software_storage_size_in_gb = None
        self._time_created = None
        self._vnic_id = None

    @property
    def backup_vnic_id(self):
        """
        Gets the backup_vnic_id of this DbNode.
        The `OCID`__ of the backup VNIC.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The backup_vnic_id of this DbNode.
        :rtype: str
        """
        return self._backup_vnic_id

    @backup_vnic_id.setter
    def backup_vnic_id(self, backup_vnic_id):
        """
        Sets the backup_vnic_id of this DbNode.
        The `OCID`__ of the backup VNIC.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param backup_vnic_id: The backup_vnic_id of this DbNode.
        :type: str
        """
        self._backup_vnic_id = backup_vnic_id

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this DbNode.
        The `OCID`__ of the DB system.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The db_system_id of this DbNode.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this DbNode.
        The `OCID`__ of the DB system.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param db_system_id: The db_system_id of this DbNode.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def hostname(self):
        """
        Gets the hostname of this DbNode.
        The host name for the database node.


        :return: The hostname of this DbNode.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this DbNode.
        The host name for the database node.


        :param hostname: The hostname of this DbNode.
        :type: str
        """
        self._hostname = hostname

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DbNode.
        The `OCID`__ of the database node.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DbNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbNode.
        The `OCID`__ of the database node.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DbNode.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DbNode.
        The current state of the database node.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DbNode.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbNode.
        The current state of the database node.


        :param lifecycle_state: The lifecycle_state of this DbNode.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def software_storage_size_in_gb(self):
        """
        Gets the software_storage_size_in_gb of this DbNode.
        The size (in GB) of the block storage volume allocation for the DB system. This attribute applies only for virtual machine DB systems.


        :return: The software_storage_size_in_gb of this DbNode.
        :rtype: int
        """
        return self._software_storage_size_in_gb

    @software_storage_size_in_gb.setter
    def software_storage_size_in_gb(self, software_storage_size_in_gb):
        """
        Sets the software_storage_size_in_gb of this DbNode.
        The size (in GB) of the block storage volume allocation for the DB system. This attribute applies only for virtual machine DB systems.


        :param software_storage_size_in_gb: The software_storage_size_in_gb of this DbNode.
        :type: int
        """
        self._software_storage_size_in_gb = software_storage_size_in_gb

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DbNode.
        The date and time that the database node was created.


        :return: The time_created of this DbNode.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbNode.
        The date and time that the database node was created.


        :param time_created: The time_created of this DbNode.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vnic_id(self):
        """
        **[Required]** Gets the vnic_id of this DbNode.
        The `OCID`__ of the VNIC.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The vnic_id of this DbNode.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this DbNode.
        The `OCID`__ of the VNIC.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param vnic_id: The vnic_id of this DbNode.
        :type: str
        """
        self._vnic_id = vnic_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
