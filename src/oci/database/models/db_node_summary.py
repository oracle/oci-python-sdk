# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbNodeSummary(object):

    def __init__(self, **kwargs):
        """
        Initializes a new DbNodeSummary object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backup_vnic_id:
            The value to assign to the backup_vnic_id property of this DbNodeSummary.
        :type backup_vnic_id: str

        :param db_system_id:
            The value to assign to the db_system_id property of this DbNodeSummary.
        :type db_system_id: str

        :param hostname:
            The value to assign to the hostname property of this DbNodeSummary.
        :type hostname: str

        :param id:
            The value to assign to the id property of this DbNodeSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbNodeSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param software_storage_size_in_gb:
            The value to assign to the software_storage_size_in_gb property of this DbNodeSummary.
        :type software_storage_size_in_gb: int

        :param time_created:
            The value to assign to the time_created property of this DbNodeSummary.
        :type time_created: datetime

        :param vnic_id:
            The value to assign to the vnic_id property of this DbNodeSummary.
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
        Gets the backup_vnic_id of this DbNodeSummary.
        The OCID of the backup VNIC.


        :return: The backup_vnic_id of this DbNodeSummary.
        :rtype: str
        """
        return self._backup_vnic_id

    @backup_vnic_id.setter
    def backup_vnic_id(self, backup_vnic_id):
        """
        Sets the backup_vnic_id of this DbNodeSummary.
        The OCID of the backup VNIC.


        :param backup_vnic_id: The backup_vnic_id of this DbNodeSummary.
        :type: str
        """
        self._backup_vnic_id = backup_vnic_id

    @property
    def db_system_id(self):
        """
        Gets the db_system_id of this DbNodeSummary.
        The OCID of the DB System.


        :return: The db_system_id of this DbNodeSummary.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this DbNodeSummary.
        The OCID of the DB System.


        :param db_system_id: The db_system_id of this DbNodeSummary.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def hostname(self):
        """
        Gets the hostname of this DbNodeSummary.
        The host name for the DB Node.


        :return: The hostname of this DbNodeSummary.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this DbNodeSummary.
        The host name for the DB Node.


        :param hostname: The hostname of this DbNodeSummary.
        :type: str
        """
        self._hostname = hostname

    @property
    def id(self):
        """
        Gets the id of this DbNodeSummary.
        The OCID of the DB Node.


        :return: The id of this DbNodeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbNodeSummary.
        The OCID of the DB Node.


        :param id: The id of this DbNodeSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DbNodeSummary.
        The current state of the database node.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DbNodeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbNodeSummary.
        The current state of the database node.


        :param lifecycle_state: The lifecycle_state of this DbNodeSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def software_storage_size_in_gb(self):
        """
        Gets the software_storage_size_in_gb of this DbNodeSummary.
        Storage size, in GBs, of the software volume that is allocated to the DB system. This is applicable only for VM-based DBs.


        :return: The software_storage_size_in_gb of this DbNodeSummary.
        :rtype: int
        """
        return self._software_storage_size_in_gb

    @software_storage_size_in_gb.setter
    def software_storage_size_in_gb(self, software_storage_size_in_gb):
        """
        Sets the software_storage_size_in_gb of this DbNodeSummary.
        Storage size, in GBs, of the software volume that is allocated to the DB system. This is applicable only for VM-based DBs.


        :param software_storage_size_in_gb: The software_storage_size_in_gb of this DbNodeSummary.
        :type: int
        """
        self._software_storage_size_in_gb = software_storage_size_in_gb

    @property
    def time_created(self):
        """
        Gets the time_created of this DbNodeSummary.
        The date and time that the DB Node was created.


        :return: The time_created of this DbNodeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbNodeSummary.
        The date and time that the DB Node was created.


        :param time_created: The time_created of this DbNodeSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vnic_id(self):
        """
        Gets the vnic_id of this DbNodeSummary.
        The OCID of the VNIC.


        :return: The vnic_id of this DbNodeSummary.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this DbNodeSummary.
        The OCID of the VNIC.


        :param vnic_id: The vnic_id of this DbNodeSummary.
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
