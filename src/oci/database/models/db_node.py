# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbNode(object):
    """
    DbNode model.
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

        :param id:
            The value to assign to the id property of this DbNode.
        :type id: str

        :param db_system_id:
            The value to assign to the db_system_id property of this DbNode.
        :type db_system_id: str

        :param vnic_id:
            The value to assign to the vnic_id property of this DbNode.
        :type vnic_id: str

        :param backup_vnic_id:
            The value to assign to the backup_vnic_id property of this DbNode.
        :type backup_vnic_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbNode.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param hostname:
            The value to assign to the hostname property of this DbNode.
        :type hostname: str

        :param fault_domain:
            The value to assign to the fault_domain property of this DbNode.
        :type fault_domain: str

        :param time_created:
            The value to assign to the time_created property of this DbNode.
        :type time_created: datetime

        :param software_storage_size_in_gb:
            The value to assign to the software_storage_size_in_gb property of this DbNode.
        :type software_storage_size_in_gb: int

        """
        self.swagger_types = {
            'id': 'str',
            'db_system_id': 'str',
            'vnic_id': 'str',
            'backup_vnic_id': 'str',
            'lifecycle_state': 'str',
            'hostname': 'str',
            'fault_domain': 'str',
            'time_created': 'datetime',
            'software_storage_size_in_gb': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'db_system_id': 'dbSystemId',
            'vnic_id': 'vnicId',
            'backup_vnic_id': 'backupVnicId',
            'lifecycle_state': 'lifecycleState',
            'hostname': 'hostname',
            'fault_domain': 'faultDomain',
            'time_created': 'timeCreated',
            'software_storage_size_in_gb': 'softwareStorageSizeInGB'
        }

        self._id = None
        self._db_system_id = None
        self._vnic_id = None
        self._backup_vnic_id = None
        self._lifecycle_state = None
        self._hostname = None
        self._fault_domain = None
        self._time_created = None
        self._software_storage_size_in_gb = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DbNode.
        The `OCID`__ of the database node.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DbNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbNode.
        The `OCID`__ of the database node.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DbNode.
        :type: str
        """
        self._id = id

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this DbNode.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_system_id of this DbNode.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this DbNode.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_system_id: The db_system_id of this DbNode.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def vnic_id(self):
        """
        **[Required]** Gets the vnic_id of this DbNode.
        The `OCID`__ of the VNIC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vnic_id of this DbNode.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this DbNode.
        The `OCID`__ of the VNIC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vnic_id: The vnic_id of this DbNode.
        :type: str
        """
        self._vnic_id = vnic_id

    @property
    def backup_vnic_id(self):
        """
        Gets the backup_vnic_id of this DbNode.
        The `OCID`__ of the backup VNIC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The backup_vnic_id of this DbNode.
        :rtype: str
        """
        return self._backup_vnic_id

    @backup_vnic_id.setter
    def backup_vnic_id(self, backup_vnic_id):
        """
        Sets the backup_vnic_id of this DbNode.
        The `OCID`__ of the backup VNIC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param backup_vnic_id: The backup_vnic_id of this DbNode.
        :type: str
        """
        self._backup_vnic_id = backup_vnic_id

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
    def fault_domain(self):
        """
        Gets the fault_domain of this DbNode.
        The name of the Fault Domain the instance is contained in.


        :return: The fault_domain of this DbNode.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this DbNode.
        The name of the Fault Domain the instance is contained in.


        :param fault_domain: The fault_domain of this DbNode.
        :type: str
        """
        self._fault_domain = fault_domain

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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
