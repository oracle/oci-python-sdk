# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchDbSystemBase(object):
    """
    Parameters for provisioning a bare metal, virtual machine, or Exadata DB system.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the source property of a LaunchDbSystemBase.
    #: This constant has a value of "NONE"
    SOURCE_NONE = "NONE"

    #: A constant which can be used with the source property of a LaunchDbSystemBase.
    #: This constant has a value of "DB_BACKUP"
    SOURCE_DB_BACKUP = "DB_BACKUP"

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchDbSystemBase object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.LaunchDbSystemDetails`
        * :class:`~oci.database.models.LaunchDbSystemFromBackupDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this LaunchDbSystemBase.
        :type availability_domain: str

        :param backup_subnet_id:
            The value to assign to the backup_subnet_id property of this LaunchDbSystemBase.
        :type backup_subnet_id: str

        :param cluster_name:
            The value to assign to the cluster_name property of this LaunchDbSystemBase.
        :type cluster_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LaunchDbSystemBase.
        :type compartment_id: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this LaunchDbSystemBase.
        :type cpu_core_count: int

        :param data_storage_percentage:
            The value to assign to the data_storage_percentage property of this LaunchDbSystemBase.
        :type data_storage_percentage: int

        :param defined_tags:
            The value to assign to the defined_tags property of this LaunchDbSystemBase.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this LaunchDbSystemBase.
        :type display_name: str

        :param domain:
            The value to assign to the domain property of this LaunchDbSystemBase.
        :type domain: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LaunchDbSystemBase.
        :type freeform_tags: dict(str, str)

        :param hostname:
            The value to assign to the hostname property of this LaunchDbSystemBase.
        :type hostname: str

        :param initial_data_storage_size_in_gb:
            The value to assign to the initial_data_storage_size_in_gb property of this LaunchDbSystemBase.
        :type initial_data_storage_size_in_gb: int

        :param node_count:
            The value to assign to the node_count property of this LaunchDbSystemBase.
        :type node_count: int

        :param shape:
            The value to assign to the shape property of this LaunchDbSystemBase.
        :type shape: str

        :param source:
            The value to assign to the source property of this LaunchDbSystemBase.
            Allowed values for this property are: "NONE", "DB_BACKUP"
        :type source: str

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this LaunchDbSystemBase.
        :type ssh_public_keys: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this LaunchDbSystemBase.
        :type subnet_id: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'backup_subnet_id': 'str',
            'cluster_name': 'str',
            'compartment_id': 'str',
            'cpu_core_count': 'int',
            'data_storage_percentage': 'int',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'domain': 'str',
            'freeform_tags': 'dict(str, str)',
            'hostname': 'str',
            'initial_data_storage_size_in_gb': 'int',
            'node_count': 'int',
            'shape': 'str',
            'source': 'str',
            'ssh_public_keys': 'list[str]',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'backup_subnet_id': 'backupSubnetId',
            'cluster_name': 'clusterName',
            'compartment_id': 'compartmentId',
            'cpu_core_count': 'cpuCoreCount',
            'data_storage_percentage': 'dataStoragePercentage',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'domain': 'domain',
            'freeform_tags': 'freeformTags',
            'hostname': 'hostname',
            'initial_data_storage_size_in_gb': 'initialDataStorageSizeInGB',
            'node_count': 'nodeCount',
            'shape': 'shape',
            'source': 'source',
            'ssh_public_keys': 'sshPublicKeys',
            'subnet_id': 'subnetId'
        }

        self._availability_domain = None
        self._backup_subnet_id = None
        self._cluster_name = None
        self._compartment_id = None
        self._cpu_core_count = None
        self._data_storage_percentage = None
        self._defined_tags = None
        self._display_name = None
        self._domain = None
        self._freeform_tags = None
        self._hostname = None
        self._initial_data_storage_size_in_gb = None
        self._node_count = None
        self._shape = None
        self._source = None
        self._ssh_public_keys = None
        self._subnet_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['source']

        if type == 'NONE':
            return 'LaunchDbSystemDetails'

        if type == 'DB_BACKUP':
            return 'LaunchDbSystemFromBackupDetails'
        else:
            return 'LaunchDbSystemBase'

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this LaunchDbSystemBase.
        The availability domain where the DB system is located.


        :return: The availability_domain of this LaunchDbSystemBase.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this LaunchDbSystemBase.
        The availability domain where the DB system is located.


        :param availability_domain: The availability_domain of this LaunchDbSystemBase.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def backup_subnet_id(self):
        """
        Gets the backup_subnet_id of this LaunchDbSystemBase.
        The `OCID`__ of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

        **Subnet Restrictions:** See the subnet restrictions information for **subnetId**.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The backup_subnet_id of this LaunchDbSystemBase.
        :rtype: str
        """
        return self._backup_subnet_id

    @backup_subnet_id.setter
    def backup_subnet_id(self, backup_subnet_id):
        """
        Sets the backup_subnet_id of this LaunchDbSystemBase.
        The `OCID`__ of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

        **Subnet Restrictions:** See the subnet restrictions information for **subnetId**.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param backup_subnet_id: The backup_subnet_id of this LaunchDbSystemBase.
        :type: str
        """
        self._backup_subnet_id = backup_subnet_id

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this LaunchDbSystemBase.
        The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :return: The cluster_name of this LaunchDbSystemBase.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this LaunchDbSystemBase.
        The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.


        :param cluster_name: The cluster_name of this LaunchDbSystemBase.
        :type: str
        """
        self._cluster_name = cluster_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LaunchDbSystemBase.
        The `OCID`__ of the compartment the DB system  belongs in.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LaunchDbSystemBase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LaunchDbSystemBase.
        The `OCID`__ of the compartment the DB system  belongs in.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LaunchDbSystemBase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this LaunchDbSystemBase.
        The number of CPU cores to enable for a bare metal or Exadata DB system. The valid values depend on the specified shape:

        - BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36.
        - BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52.
        - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84.
        - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168.
        - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336.
        - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92.
        - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184.
        - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

        This parameter is not used for virtual machine DB systems because virtual machine DB systems have a set number of cores for each shape.
        For information about the number of cores for a virtual machine DB system shape, see `Virtual Machine DB Systems`__

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Database/Concepts/overview.htm#virtualmachine


        :return: The cpu_core_count of this LaunchDbSystemBase.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this LaunchDbSystemBase.
        The number of CPU cores to enable for a bare metal or Exadata DB system. The valid values depend on the specified shape:

        - BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36.
        - BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52.
        - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84.
        - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168.
        - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336.
        - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92.
        - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184.
        - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

        This parameter is not used for virtual machine DB systems because virtual machine DB systems have a set number of cores for each shape.
        For information about the number of cores for a virtual machine DB system shape, see `Virtual Machine DB Systems`__

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Database/Concepts/overview.htm#virtualmachine


        :param cpu_core_count: The cpu_core_count of this LaunchDbSystemBase.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def data_storage_percentage(self):
        """
        Gets the data_storage_percentage of this LaunchDbSystemBase.
        The percentage assigned to DATA storage (user data and database files).
        The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups).
        Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.


        :return: The data_storage_percentage of this LaunchDbSystemBase.
        :rtype: int
        """
        return self._data_storage_percentage

    @data_storage_percentage.setter
    def data_storage_percentage(self, data_storage_percentage):
        """
        Sets the data_storage_percentage of this LaunchDbSystemBase.
        The percentage assigned to DATA storage (user data and database files).
        The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups).
        Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.


        :param data_storage_percentage: The data_storage_percentage of this LaunchDbSystemBase.
        :type: int
        """
        self._data_storage_percentage = data_storage_percentage

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LaunchDbSystemBase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this LaunchDbSystemBase.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LaunchDbSystemBase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this LaunchDbSystemBase.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this LaunchDbSystemBase.
        The user-friendly name for the DB system. The name does not have to be unique.


        :return: The display_name of this LaunchDbSystemBase.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LaunchDbSystemBase.
        The user-friendly name for the DB system. The name does not have to be unique.


        :param display_name: The display_name of this LaunchDbSystemBase.
        :type: str
        """
        self._display_name = display_name

    @property
    def domain(self):
        """
        Gets the domain of this LaunchDbSystemBase.
        A domain name used for the DB system. If the Oracle-provided Internet and VCN
        Resolver is enabled for the specified subnet, the domain name for the subnet is used
        (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.


        :return: The domain of this LaunchDbSystemBase.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this LaunchDbSystemBase.
        A domain name used for the DB system. If the Oracle-provided Internet and VCN
        Resolver is enabled for the specified subnet, the domain name for the subnet is used
        (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.


        :param domain: The domain of this LaunchDbSystemBase.
        :type: str
        """
        self._domain = domain

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LaunchDbSystemBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this LaunchDbSystemBase.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LaunchDbSystemBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this LaunchDbSystemBase.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this LaunchDbSystemBase.
        The hostname for the DB system. The hostname must begin with an alphabetic character and
        can contain a maximum of 30 alphanumeric characters, including hyphens (-).

        The maximum length of the combined hostname and domain is 63 characters.

        **Note:** The hostname must be unique within the subnet. If it is not unique,
        the DB system will fail to provision.


        :return: The hostname of this LaunchDbSystemBase.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this LaunchDbSystemBase.
        The hostname for the DB system. The hostname must begin with an alphabetic character and
        can contain a maximum of 30 alphanumeric characters, including hyphens (-).

        The maximum length of the combined hostname and domain is 63 characters.

        **Note:** The hostname must be unique within the subnet. If it is not unique,
        the DB system will fail to provision.


        :param hostname: The hostname of this LaunchDbSystemBase.
        :type: str
        """
        self._hostname = hostname

    @property
    def initial_data_storage_size_in_gb(self):
        """
        Gets the initial_data_storage_size_in_gb of this LaunchDbSystemBase.
        Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.


        :return: The initial_data_storage_size_in_gb of this LaunchDbSystemBase.
        :rtype: int
        """
        return self._initial_data_storage_size_in_gb

    @initial_data_storage_size_in_gb.setter
    def initial_data_storage_size_in_gb(self, initial_data_storage_size_in_gb):
        """
        Sets the initial_data_storage_size_in_gb of this LaunchDbSystemBase.
        Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.


        :param initial_data_storage_size_in_gb: The initial_data_storage_size_in_gb of this LaunchDbSystemBase.
        :type: int
        """
        self._initial_data_storage_size_in_gb = initial_data_storage_size_in_gb

    @property
    def node_count(self):
        """
        Gets the node_count of this LaunchDbSystemBase.
        The number of nodes to launch for a 2-node RAC virtual machine DB system.


        :return: The node_count of this LaunchDbSystemBase.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this LaunchDbSystemBase.
        The number of nodes to launch for a 2-node RAC virtual machine DB system.


        :param node_count: The node_count of this LaunchDbSystemBase.
        :type: int
        """
        self._node_count = node_count

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this LaunchDbSystemBase.
        The shape of the DB system. The shape determines resources allocated to the DB system.
        - For virtual machine shapes, the number of CPU cores and memory
        - For bare metal and Exadata shapes, the number of CPU cores, memory, and storage

        To get a list of shapes, use the :func:`list_db_system_shapes` operation.


        :return: The shape of this LaunchDbSystemBase.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this LaunchDbSystemBase.
        The shape of the DB system. The shape determines resources allocated to the DB system.
        - For virtual machine shapes, the number of CPU cores and memory
        - For bare metal and Exadata shapes, the number of CPU cores, memory, and storage

        To get a list of shapes, use the :func:`list_db_system_shapes` operation.


        :param shape: The shape of this LaunchDbSystemBase.
        :type: str
        """
        self._shape = shape

    @property
    def source(self):
        """
        Gets the source of this LaunchDbSystemBase.
        The source of the database:
          NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a backup. The default is NONE.

        Allowed values for this property are: "NONE", "DB_BACKUP"


        :return: The source of this LaunchDbSystemBase.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this LaunchDbSystemBase.
        The source of the database:
          NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a backup. The default is NONE.


        :param source: The source of this LaunchDbSystemBase.
        :type: str
        """
        allowed_values = ["NONE", "DB_BACKUP"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            raise ValueError(
                "Invalid value for `source`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._source = source

    @property
    def ssh_public_keys(self):
        """
        **[Required]** Gets the ssh_public_keys of this LaunchDbSystemBase.
        The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.


        :return: The ssh_public_keys of this LaunchDbSystemBase.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this LaunchDbSystemBase.
        The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.


        :param ssh_public_keys: The ssh_public_keys of this LaunchDbSystemBase.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this LaunchDbSystemBase.
        The `OCID`__ of the subnet the DB system is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and the backup subnet.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this LaunchDbSystemBase.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this LaunchDbSystemBase.
        The `OCID`__ of the subnet the DB system is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and the backup subnet.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this LaunchDbSystemBase.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
