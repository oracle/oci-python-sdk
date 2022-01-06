# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbServer(object):
    """
    Details of the Exacc Db server resource. Applies to Exadata Cloud@Customer instances only.
    """

    #: A constant which can be used with the lifecycle_state property of a DbServer.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DbServer.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a DbServer.
    #: This constant has a value of "UNAVAILABLE"
    LIFECYCLE_STATE_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a DbServer.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DbServer.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DbServer.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new DbServer object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DbServer.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DbServer.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DbServer.
        :type compartment_id: str

        :param exadata_infrastructure_id:
            The value to assign to the exadata_infrastructure_id property of this DbServer.
        :type exadata_infrastructure_id: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this DbServer.
        :type cpu_core_count: int

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this DbServer.
        :type memory_size_in_gbs: int

        :param db_node_storage_size_in_gbs:
            The value to assign to the db_node_storage_size_in_gbs property of this DbServer.
        :type db_node_storage_size_in_gbs: int

        :param vm_cluster_ids:
            The value to assign to the vm_cluster_ids property of this DbServer.
        :type vm_cluster_ids: list[str]

        :param db_node_ids:
            The value to assign to the db_node_ids property of this DbServer.
        :type db_node_ids: list[str]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbServer.
            Allowed values for this property are: "CREATING", "AVAILABLE", "UNAVAILABLE", "DELETING", "DELETED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DbServer.
        :type lifecycle_details: str

        :param max_cpu_count:
            The value to assign to the max_cpu_count property of this DbServer.
        :type max_cpu_count: int

        :param max_memory_in_gbs:
            The value to assign to the max_memory_in_gbs property of this DbServer.
        :type max_memory_in_gbs: int

        :param max_db_node_storage_in_gbs:
            The value to assign to the max_db_node_storage_in_gbs property of this DbServer.
        :type max_db_node_storage_in_gbs: int

        :param time_created:
            The value to assign to the time_created property of this DbServer.
        :type time_created: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DbServer.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DbServer.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'exadata_infrastructure_id': 'str',
            'cpu_core_count': 'int',
            'memory_size_in_gbs': 'int',
            'db_node_storage_size_in_gbs': 'int',
            'vm_cluster_ids': 'list[str]',
            'db_node_ids': 'list[str]',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'max_cpu_count': 'int',
            'max_memory_in_gbs': 'int',
            'max_db_node_storage_in_gbs': 'int',
            'time_created': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'exadata_infrastructure_id': 'exadataInfrastructureId',
            'cpu_core_count': 'cpuCoreCount',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'db_node_storage_size_in_gbs': 'dbNodeStorageSizeInGBs',
            'vm_cluster_ids': 'vmClusterIds',
            'db_node_ids': 'dbNodeIds',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'max_cpu_count': 'maxCpuCount',
            'max_memory_in_gbs': 'maxMemoryInGBs',
            'max_db_node_storage_in_gbs': 'maxDbNodeStorageInGBs',
            'time_created': 'timeCreated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._exadata_infrastructure_id = None
        self._cpu_core_count = None
        self._memory_size_in_gbs = None
        self._db_node_storage_size_in_gbs = None
        self._vm_cluster_ids = None
        self._db_node_ids = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._max_cpu_count = None
        self._max_memory_in_gbs = None
        self._max_db_node_storage_in_gbs = None
        self._time_created = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this DbServer.
        The `OCID`__ of the Exacc Db server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DbServer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbServer.
        The `OCID`__ of the Exacc Db server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DbServer.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this DbServer.
        The user-friendly name for the Db server. The name does not need to be unique.


        :return: The display_name of this DbServer.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DbServer.
        The user-friendly name for the Db server. The name does not need to be unique.


        :param display_name: The display_name of this DbServer.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DbServer.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DbServer.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DbServer.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DbServer.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def exadata_infrastructure_id(self):
        """
        Gets the exadata_infrastructure_id of this DbServer.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The exadata_infrastructure_id of this DbServer.
        :rtype: str
        """
        return self._exadata_infrastructure_id

    @exadata_infrastructure_id.setter
    def exadata_infrastructure_id(self, exadata_infrastructure_id):
        """
        Sets the exadata_infrastructure_id of this DbServer.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param exadata_infrastructure_id: The exadata_infrastructure_id of this DbServer.
        :type: str
        """
        self._exadata_infrastructure_id = exadata_infrastructure_id

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this DbServer.
        The number of CPU cores enabled on the Db server.


        :return: The cpu_core_count of this DbServer.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this DbServer.
        The number of CPU cores enabled on the Db server.


        :param cpu_core_count: The cpu_core_count of this DbServer.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def memory_size_in_gbs(self):
        """
        Gets the memory_size_in_gbs of this DbServer.
        The allocated memory in GBs on the Db server.


        :return: The memory_size_in_gbs of this DbServer.
        :rtype: int
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this DbServer.
        The allocated memory in GBs on the Db server.


        :param memory_size_in_gbs: The memory_size_in_gbs of this DbServer.
        :type: int
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def db_node_storage_size_in_gbs(self):
        """
        Gets the db_node_storage_size_in_gbs of this DbServer.
        The allocated local node storage in GBs on the Db server.


        :return: The db_node_storage_size_in_gbs of this DbServer.
        :rtype: int
        """
        return self._db_node_storage_size_in_gbs

    @db_node_storage_size_in_gbs.setter
    def db_node_storage_size_in_gbs(self, db_node_storage_size_in_gbs):
        """
        Sets the db_node_storage_size_in_gbs of this DbServer.
        The allocated local node storage in GBs on the Db server.


        :param db_node_storage_size_in_gbs: The db_node_storage_size_in_gbs of this DbServer.
        :type: int
        """
        self._db_node_storage_size_in_gbs = db_node_storage_size_in_gbs

    @property
    def vm_cluster_ids(self):
        """
        Gets the vm_cluster_ids of this DbServer.
        The `OCID`__ of the VM Clusters associated with the Db server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vm_cluster_ids of this DbServer.
        :rtype: list[str]
        """
        return self._vm_cluster_ids

    @vm_cluster_ids.setter
    def vm_cluster_ids(self, vm_cluster_ids):
        """
        Sets the vm_cluster_ids of this DbServer.
        The `OCID`__ of the VM Clusters associated with the Db server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vm_cluster_ids: The vm_cluster_ids of this DbServer.
        :type: list[str]
        """
        self._vm_cluster_ids = vm_cluster_ids

    @property
    def db_node_ids(self):
        """
        Gets the db_node_ids of this DbServer.
        The `OCID`__ of the Db nodes associated with the Db server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_node_ids of this DbServer.
        :rtype: list[str]
        """
        return self._db_node_ids

    @db_node_ids.setter
    def db_node_ids(self, db_node_ids):
        """
        Sets the db_node_ids of this DbServer.
        The `OCID`__ of the Db nodes associated with the Db server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_node_ids: The db_node_ids of this DbServer.
        :type: list[str]
        """
        self._db_node_ids = db_node_ids

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DbServer.
        The current state of the Db server.

        Allowed values for this property are: "CREATING", "AVAILABLE", "UNAVAILABLE", "DELETING", "DELETED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DbServer.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbServer.
        The current state of the Db server.


        :param lifecycle_state: The lifecycle_state of this DbServer.
        :type: str
        """
        allowed_values = ["CREATING", "AVAILABLE", "UNAVAILABLE", "DELETING", "DELETED", "MAINTENANCE_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DbServer.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this DbServer.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DbServer.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this DbServer.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def max_cpu_count(self):
        """
        Gets the max_cpu_count of this DbServer.
        The total number of CPU cores available.


        :return: The max_cpu_count of this DbServer.
        :rtype: int
        """
        return self._max_cpu_count

    @max_cpu_count.setter
    def max_cpu_count(self, max_cpu_count):
        """
        Sets the max_cpu_count of this DbServer.
        The total number of CPU cores available.


        :param max_cpu_count: The max_cpu_count of this DbServer.
        :type: int
        """
        self._max_cpu_count = max_cpu_count

    @property
    def max_memory_in_gbs(self):
        """
        Gets the max_memory_in_gbs of this DbServer.
        The total memory available in GBs.


        :return: The max_memory_in_gbs of this DbServer.
        :rtype: int
        """
        return self._max_memory_in_gbs

    @max_memory_in_gbs.setter
    def max_memory_in_gbs(self, max_memory_in_gbs):
        """
        Sets the max_memory_in_gbs of this DbServer.
        The total memory available in GBs.


        :param max_memory_in_gbs: The max_memory_in_gbs of this DbServer.
        :type: int
        """
        self._max_memory_in_gbs = max_memory_in_gbs

    @property
    def max_db_node_storage_in_gbs(self):
        """
        Gets the max_db_node_storage_in_gbs of this DbServer.
        The total local node storage available in GBs.


        :return: The max_db_node_storage_in_gbs of this DbServer.
        :rtype: int
        """
        return self._max_db_node_storage_in_gbs

    @max_db_node_storage_in_gbs.setter
    def max_db_node_storage_in_gbs(self, max_db_node_storage_in_gbs):
        """
        Sets the max_db_node_storage_in_gbs of this DbServer.
        The total local node storage available in GBs.


        :param max_db_node_storage_in_gbs: The max_db_node_storage_in_gbs of this DbServer.
        :type: int
        """
        self._max_db_node_storage_in_gbs = max_db_node_storage_in_gbs

    @property
    def time_created(self):
        """
        Gets the time_created of this DbServer.
        The date and time that the Db Server was created.


        :return: The time_created of this DbServer.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbServer.
        The date and time that the Db Server was created.


        :param time_created: The time_created of this DbServer.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DbServer.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DbServer.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DbServer.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DbServer.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DbServer.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DbServer.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DbServer.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DbServer.
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
