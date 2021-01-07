# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVmClusterDetails(object):
    """
    Details for the create Exadata VM cluster operation. Applies to Exadata Cloud@Customer instances only.
    For details on the create cloud Exadata VM cluster operation used with Exadata Cloud Service instances, see :func:`create_cloud_vm_cluster_details`
    """

    #: A constant which can be used with the license_model property of a CreateVmClusterDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CreateVmClusterDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVmClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVmClusterDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateVmClusterDetails.
        :type display_name: str

        :param exadata_infrastructure_id:
            The value to assign to the exadata_infrastructure_id property of this CreateVmClusterDetails.
        :type exadata_infrastructure_id: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateVmClusterDetails.
        :type cpu_core_count: int

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this CreateVmClusterDetails.
        :type memory_size_in_gbs: int

        :param db_node_storage_size_in_gbs:
            The value to assign to the db_node_storage_size_in_gbs property of this CreateVmClusterDetails.
        :type db_node_storage_size_in_gbs: int

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this CreateVmClusterDetails.
        :type data_storage_size_in_tbs: float

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this CreateVmClusterDetails.
        :type ssh_public_keys: list[str]

        :param vm_cluster_network_id:
            The value to assign to the vm_cluster_network_id property of this CreateVmClusterDetails.
        :type vm_cluster_network_id: str

        :param license_model:
            The value to assign to the license_model property of this CreateVmClusterDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param is_sparse_diskgroup_enabled:
            The value to assign to the is_sparse_diskgroup_enabled property of this CreateVmClusterDetails.
        :type is_sparse_diskgroup_enabled: bool

        :param is_local_backup_enabled:
            The value to assign to the is_local_backup_enabled property of this CreateVmClusterDetails.
        :type is_local_backup_enabled: bool

        :param time_zone:
            The value to assign to the time_zone property of this CreateVmClusterDetails.
        :type time_zone: str

        :param gi_version:
            The value to assign to the gi_version property of this CreateVmClusterDetails.
        :type gi_version: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVmClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVmClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'exadata_infrastructure_id': 'str',
            'cpu_core_count': 'int',
            'memory_size_in_gbs': 'int',
            'db_node_storage_size_in_gbs': 'int',
            'data_storage_size_in_tbs': 'float',
            'ssh_public_keys': 'list[str]',
            'vm_cluster_network_id': 'str',
            'license_model': 'str',
            'is_sparse_diskgroup_enabled': 'bool',
            'is_local_backup_enabled': 'bool',
            'time_zone': 'str',
            'gi_version': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'exadata_infrastructure_id': 'exadataInfrastructureId',
            'cpu_core_count': 'cpuCoreCount',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'db_node_storage_size_in_gbs': 'dbNodeStorageSizeInGBs',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'ssh_public_keys': 'sshPublicKeys',
            'vm_cluster_network_id': 'vmClusterNetworkId',
            'license_model': 'licenseModel',
            'is_sparse_diskgroup_enabled': 'isSparseDiskgroupEnabled',
            'is_local_backup_enabled': 'isLocalBackupEnabled',
            'time_zone': 'timeZone',
            'gi_version': 'giVersion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._exadata_infrastructure_id = None
        self._cpu_core_count = None
        self._memory_size_in_gbs = None
        self._db_node_storage_size_in_gbs = None
        self._data_storage_size_in_tbs = None
        self._ssh_public_keys = None
        self._vm_cluster_network_id = None
        self._license_model = None
        self._is_sparse_diskgroup_enabled = None
        self._is_local_backup_enabled = None
        self._time_zone = None
        self._gi_version = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateVmClusterDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateVmClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVmClusterDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateVmClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateVmClusterDetails.
        The user-friendly name for the VM cluster. The name does not need to be unique.


        :return: The display_name of this CreateVmClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVmClusterDetails.
        The user-friendly name for the VM cluster. The name does not need to be unique.


        :param display_name: The display_name of this CreateVmClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def exadata_infrastructure_id(self):
        """
        **[Required]** Gets the exadata_infrastructure_id of this CreateVmClusterDetails.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The exadata_infrastructure_id of this CreateVmClusterDetails.
        :rtype: str
        """
        return self._exadata_infrastructure_id

    @exadata_infrastructure_id.setter
    def exadata_infrastructure_id(self, exadata_infrastructure_id):
        """
        Sets the exadata_infrastructure_id of this CreateVmClusterDetails.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param exadata_infrastructure_id: The exadata_infrastructure_id of this CreateVmClusterDetails.
        :type: str
        """
        self._exadata_infrastructure_id = exadata_infrastructure_id

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this CreateVmClusterDetails.
        The number of CPU cores to enable for the VM cluster.


        :return: The cpu_core_count of this CreateVmClusterDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this CreateVmClusterDetails.
        The number of CPU cores to enable for the VM cluster.


        :param cpu_core_count: The cpu_core_count of this CreateVmClusterDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def memory_size_in_gbs(self):
        """
        Gets the memory_size_in_gbs of this CreateVmClusterDetails.
        The memory to be allocated in GBs.


        :return: The memory_size_in_gbs of this CreateVmClusterDetails.
        :rtype: int
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this CreateVmClusterDetails.
        The memory to be allocated in GBs.


        :param memory_size_in_gbs: The memory_size_in_gbs of this CreateVmClusterDetails.
        :type: int
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def db_node_storage_size_in_gbs(self):
        """
        Gets the db_node_storage_size_in_gbs of this CreateVmClusterDetails.
        The local node storage to be allocated in GBs.


        :return: The db_node_storage_size_in_gbs of this CreateVmClusterDetails.
        :rtype: int
        """
        return self._db_node_storage_size_in_gbs

    @db_node_storage_size_in_gbs.setter
    def db_node_storage_size_in_gbs(self, db_node_storage_size_in_gbs):
        """
        Sets the db_node_storage_size_in_gbs of this CreateVmClusterDetails.
        The local node storage to be allocated in GBs.


        :param db_node_storage_size_in_gbs: The db_node_storage_size_in_gbs of this CreateVmClusterDetails.
        :type: int
        """
        self._db_node_storage_size_in_gbs = db_node_storage_size_in_gbs

    @property
    def data_storage_size_in_tbs(self):
        """
        Gets the data_storage_size_in_tbs of this CreateVmClusterDetails.
        The data disk group size to be allocated in TBs.


        :return: The data_storage_size_in_tbs of this CreateVmClusterDetails.
        :rtype: float
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this CreateVmClusterDetails.
        The data disk group size to be allocated in TBs.


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this CreateVmClusterDetails.
        :type: float
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def ssh_public_keys(self):
        """
        **[Required]** Gets the ssh_public_keys of this CreateVmClusterDetails.
        The public key portion of one or more key pairs used for SSH access to the VM cluster.


        :return: The ssh_public_keys of this CreateVmClusterDetails.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this CreateVmClusterDetails.
        The public key portion of one or more key pairs used for SSH access to the VM cluster.


        :param ssh_public_keys: The ssh_public_keys of this CreateVmClusterDetails.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def vm_cluster_network_id(self):
        """
        **[Required]** Gets the vm_cluster_network_id of this CreateVmClusterDetails.
        The `OCID`__ of the VM cluster network.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vm_cluster_network_id of this CreateVmClusterDetails.
        :rtype: str
        """
        return self._vm_cluster_network_id

    @vm_cluster_network_id.setter
    def vm_cluster_network_id(self, vm_cluster_network_id):
        """
        Sets the vm_cluster_network_id of this CreateVmClusterDetails.
        The `OCID`__ of the VM cluster network.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vm_cluster_network_id: The vm_cluster_network_id of this CreateVmClusterDetails.
        :type: str
        """
        self._vm_cluster_network_id = vm_cluster_network_id

    @property
    def license_model(self):
        """
        Gets the license_model of this CreateVmClusterDetails.
        The Oracle license model that applies to the VM cluster. The default is BRING_YOUR_OWN_LICENSE.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this CreateVmClusterDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CreateVmClusterDetails.
        The Oracle license model that applies to the VM cluster. The default is BRING_YOUR_OWN_LICENSE.


        :param license_model: The license_model of this CreateVmClusterDetails.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            raise ValueError(
                "Invalid value for `license_model`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._license_model = license_model

    @property
    def is_sparse_diskgroup_enabled(self):
        """
        Gets the is_sparse_diskgroup_enabled of this CreateVmClusterDetails.
        If true, the sparse disk group is configured for the VM cluster. If false, the sparse disk group is not created.


        :return: The is_sparse_diskgroup_enabled of this CreateVmClusterDetails.
        :rtype: bool
        """
        return self._is_sparse_diskgroup_enabled

    @is_sparse_diskgroup_enabled.setter
    def is_sparse_diskgroup_enabled(self, is_sparse_diskgroup_enabled):
        """
        Sets the is_sparse_diskgroup_enabled of this CreateVmClusterDetails.
        If true, the sparse disk group is configured for the VM cluster. If false, the sparse disk group is not created.


        :param is_sparse_diskgroup_enabled: The is_sparse_diskgroup_enabled of this CreateVmClusterDetails.
        :type: bool
        """
        self._is_sparse_diskgroup_enabled = is_sparse_diskgroup_enabled

    @property
    def is_local_backup_enabled(self):
        """
        Gets the is_local_backup_enabled of this CreateVmClusterDetails.
        If true, database backup on local Exadata storage is configured for the VM cluster. If false, database backup on local Exadata storage is not available in the VM cluster.


        :return: The is_local_backup_enabled of this CreateVmClusterDetails.
        :rtype: bool
        """
        return self._is_local_backup_enabled

    @is_local_backup_enabled.setter
    def is_local_backup_enabled(self, is_local_backup_enabled):
        """
        Sets the is_local_backup_enabled of this CreateVmClusterDetails.
        If true, database backup on local Exadata storage is configured for the VM cluster. If false, database backup on local Exadata storage is not available in the VM cluster.


        :param is_local_backup_enabled: The is_local_backup_enabled of this CreateVmClusterDetails.
        :type: bool
        """
        self._is_local_backup_enabled = is_local_backup_enabled

    @property
    def time_zone(self):
        """
        Gets the time_zone of this CreateVmClusterDetails.
        The time zone to use for the VM cluster. For details, see `DB System Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this CreateVmClusterDetails.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this CreateVmClusterDetails.
        The time zone to use for the VM cluster. For details, see `DB System Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this CreateVmClusterDetails.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def gi_version(self):
        """
        **[Required]** Gets the gi_version of this CreateVmClusterDetails.
        The Oracle Grid Infrastructure software version for the VM cluster.


        :return: The gi_version of this CreateVmClusterDetails.
        :rtype: str
        """
        return self._gi_version

    @gi_version.setter
    def gi_version(self, gi_version):
        """
        Sets the gi_version of this CreateVmClusterDetails.
        The Oracle Grid Infrastructure software version for the VM cluster.


        :param gi_version: The gi_version of this CreateVmClusterDetails.
        :type: str
        """
        self._gi_version = gi_version

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateVmClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateVmClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateVmClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateVmClusterDetails.
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
