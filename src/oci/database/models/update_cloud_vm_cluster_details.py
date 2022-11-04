# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCloudVmClusterDetails(object):
    """
    Details for updating the cloud VM cluster. Applies to Exadata Cloud Service instances only.
    """

    #: A constant which can be used with the license_model property of a UpdateCloudVmClusterDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a UpdateCloudVmClusterDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCloudVmClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateCloudVmClusterDetails.
        :type display_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this UpdateCloudVmClusterDetails.
        :type cpu_core_count: int

        :param ocpu_count:
            The value to assign to the ocpu_count property of this UpdateCloudVmClusterDetails.
        :type ocpu_count: float

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this UpdateCloudVmClusterDetails.
        :type memory_size_in_gbs: int

        :param db_node_storage_size_in_gbs:
            The value to assign to the db_node_storage_size_in_gbs property of this UpdateCloudVmClusterDetails.
        :type db_node_storage_size_in_gbs: int

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this UpdateCloudVmClusterDetails.
        :type data_storage_size_in_tbs: float

        :param license_model:
            The value to assign to the license_model property of this UpdateCloudVmClusterDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this UpdateCloudVmClusterDetails.
        :type ssh_public_keys: list[str]

        :param update_details:
            The value to assign to the update_details property of this UpdateCloudVmClusterDetails.
        :type update_details: oci.database.models.UpdateDetails

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateCloudVmClusterDetails.
        :type nsg_ids: list[str]

        :param backup_network_nsg_ids:
            The value to assign to the backup_network_nsg_ids property of this UpdateCloudVmClusterDetails.
        :type backup_network_nsg_ids: list[str]

        :param compute_nodes:
            The value to assign to the compute_nodes property of this UpdateCloudVmClusterDetails.
        :type compute_nodes: list[str]

        :param storage_size_in_gbs:
            The value to assign to the storage_size_in_gbs property of this UpdateCloudVmClusterDetails.
        :type storage_size_in_gbs: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateCloudVmClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateCloudVmClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param data_collection_options:
            The value to assign to the data_collection_options property of this UpdateCloudVmClusterDetails.
        :type data_collection_options: oci.database.models.DataCollectionOptions

        """
        self.swagger_types = {
            'display_name': 'str',
            'cpu_core_count': 'int',
            'ocpu_count': 'float',
            'memory_size_in_gbs': 'int',
            'db_node_storage_size_in_gbs': 'int',
            'data_storage_size_in_tbs': 'float',
            'license_model': 'str',
            'ssh_public_keys': 'list[str]',
            'update_details': 'UpdateDetails',
            'nsg_ids': 'list[str]',
            'backup_network_nsg_ids': 'list[str]',
            'compute_nodes': 'list[str]',
            'storage_size_in_gbs': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'data_collection_options': 'DataCollectionOptions'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'cpu_core_count': 'cpuCoreCount',
            'ocpu_count': 'ocpuCount',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'db_node_storage_size_in_gbs': 'dbNodeStorageSizeInGBs',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'license_model': 'licenseModel',
            'ssh_public_keys': 'sshPublicKeys',
            'update_details': 'updateDetails',
            'nsg_ids': 'nsgIds',
            'backup_network_nsg_ids': 'backupNetworkNsgIds',
            'compute_nodes': 'computeNodes',
            'storage_size_in_gbs': 'storageSizeInGBs',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'data_collection_options': 'dataCollectionOptions'
        }

        self._display_name = None
        self._cpu_core_count = None
        self._ocpu_count = None
        self._memory_size_in_gbs = None
        self._db_node_storage_size_in_gbs = None
        self._data_storage_size_in_tbs = None
        self._license_model = None
        self._ssh_public_keys = None
        self._update_details = None
        self._nsg_ids = None
        self._backup_network_nsg_ids = None
        self._compute_nodes = None
        self._storage_size_in_gbs = None
        self._freeform_tags = None
        self._defined_tags = None
        self._data_collection_options = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateCloudVmClusterDetails.
        The user-friendly name for the cloud VM cluster. The name does not need to be unique.


        :return: The display_name of this UpdateCloudVmClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateCloudVmClusterDetails.
        The user-friendly name for the cloud VM cluster. The name does not need to be unique.


        :param display_name: The display_name of this UpdateCloudVmClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this UpdateCloudVmClusterDetails.
        The number of CPU cores to enable for the cloud VM cluster.


        :return: The cpu_core_count of this UpdateCloudVmClusterDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this UpdateCloudVmClusterDetails.
        The number of CPU cores to enable for the cloud VM cluster.


        :param cpu_core_count: The cpu_core_count of this UpdateCloudVmClusterDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def ocpu_count(self):
        """
        Gets the ocpu_count of this UpdateCloudVmClusterDetails.
        The number of OCPU cores to enable for a cloud VM cluster. Only 1 decimal place is allowed for the fractional part.


        :return: The ocpu_count of this UpdateCloudVmClusterDetails.
        :rtype: float
        """
        return self._ocpu_count

    @ocpu_count.setter
    def ocpu_count(self, ocpu_count):
        """
        Sets the ocpu_count of this UpdateCloudVmClusterDetails.
        The number of OCPU cores to enable for a cloud VM cluster. Only 1 decimal place is allowed for the fractional part.


        :param ocpu_count: The ocpu_count of this UpdateCloudVmClusterDetails.
        :type: float
        """
        self._ocpu_count = ocpu_count

    @property
    def memory_size_in_gbs(self):
        """
        Gets the memory_size_in_gbs of this UpdateCloudVmClusterDetails.
        The memory to be allocated in GBs.


        :return: The memory_size_in_gbs of this UpdateCloudVmClusterDetails.
        :rtype: int
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this UpdateCloudVmClusterDetails.
        The memory to be allocated in GBs.


        :param memory_size_in_gbs: The memory_size_in_gbs of this UpdateCloudVmClusterDetails.
        :type: int
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def db_node_storage_size_in_gbs(self):
        """
        Gets the db_node_storage_size_in_gbs of this UpdateCloudVmClusterDetails.
        The local node storage to be allocated in GBs.


        :return: The db_node_storage_size_in_gbs of this UpdateCloudVmClusterDetails.
        :rtype: int
        """
        return self._db_node_storage_size_in_gbs

    @db_node_storage_size_in_gbs.setter
    def db_node_storage_size_in_gbs(self, db_node_storage_size_in_gbs):
        """
        Sets the db_node_storage_size_in_gbs of this UpdateCloudVmClusterDetails.
        The local node storage to be allocated in GBs.


        :param db_node_storage_size_in_gbs: The db_node_storage_size_in_gbs of this UpdateCloudVmClusterDetails.
        :type: int
        """
        self._db_node_storage_size_in_gbs = db_node_storage_size_in_gbs

    @property
    def data_storage_size_in_tbs(self):
        """
        Gets the data_storage_size_in_tbs of this UpdateCloudVmClusterDetails.
        The data disk group size to be allocated in TBs.


        :return: The data_storage_size_in_tbs of this UpdateCloudVmClusterDetails.
        :rtype: float
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this UpdateCloudVmClusterDetails.
        The data disk group size to be allocated in TBs.


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this UpdateCloudVmClusterDetails.
        :type: float
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def license_model(self):
        """
        Gets the license_model of this UpdateCloudVmClusterDetails.
        The Oracle license model that applies to the cloud VM cluster. The default is BRING_YOUR_OWN_LICENSE. Applies to Exadata Cloud Service instances only.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this UpdateCloudVmClusterDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this UpdateCloudVmClusterDetails.
        The Oracle license model that applies to the cloud VM cluster. The default is BRING_YOUR_OWN_LICENSE. Applies to Exadata Cloud Service instances only.


        :param license_model: The license_model of this UpdateCloudVmClusterDetails.
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
    def ssh_public_keys(self):
        """
        Gets the ssh_public_keys of this UpdateCloudVmClusterDetails.
        The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.


        :return: The ssh_public_keys of this UpdateCloudVmClusterDetails.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this UpdateCloudVmClusterDetails.
        The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.


        :param ssh_public_keys: The ssh_public_keys of this UpdateCloudVmClusterDetails.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def update_details(self):
        """
        Gets the update_details of this UpdateCloudVmClusterDetails.

        :return: The update_details of this UpdateCloudVmClusterDetails.
        :rtype: oci.database.models.UpdateDetails
        """
        return self._update_details

    @update_details.setter
    def update_details(self, update_details):
        """
        Sets the update_details of this UpdateCloudVmClusterDetails.

        :param update_details: The update_details of this UpdateCloudVmClusterDetails.
        :type: oci.database.models.UpdateDetails
        """
        self._update_details = update_details

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateCloudVmClusterDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this UpdateCloudVmClusterDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateCloudVmClusterDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this UpdateCloudVmClusterDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def backup_network_nsg_ids(self):
        """
        Gets the backup_network_nsg_ids of this UpdateCloudVmClusterDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The backup_network_nsg_ids of this UpdateCloudVmClusterDetails.
        :rtype: list[str]
        """
        return self._backup_network_nsg_ids

    @backup_network_nsg_ids.setter
    def backup_network_nsg_ids(self, backup_network_nsg_ids):
        """
        Sets the backup_network_nsg_ids of this UpdateCloudVmClusterDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param backup_network_nsg_ids: The backup_network_nsg_ids of this UpdateCloudVmClusterDetails.
        :type: list[str]
        """
        self._backup_network_nsg_ids = backup_network_nsg_ids

    @property
    def compute_nodes(self):
        """
        Gets the compute_nodes of this UpdateCloudVmClusterDetails.
        The list of compute servers to be added to the cloud VM cluster.


        :return: The compute_nodes of this UpdateCloudVmClusterDetails.
        :rtype: list[str]
        """
        return self._compute_nodes

    @compute_nodes.setter
    def compute_nodes(self, compute_nodes):
        """
        Sets the compute_nodes of this UpdateCloudVmClusterDetails.
        The list of compute servers to be added to the cloud VM cluster.


        :param compute_nodes: The compute_nodes of this UpdateCloudVmClusterDetails.
        :type: list[str]
        """
        self._compute_nodes = compute_nodes

    @property
    def storage_size_in_gbs(self):
        """
        Gets the storage_size_in_gbs of this UpdateCloudVmClusterDetails.
        The disk group size to be allocated in GBs.


        :return: The storage_size_in_gbs of this UpdateCloudVmClusterDetails.
        :rtype: int
        """
        return self._storage_size_in_gbs

    @storage_size_in_gbs.setter
    def storage_size_in_gbs(self, storage_size_in_gbs):
        """
        Sets the storage_size_in_gbs of this UpdateCloudVmClusterDetails.
        The disk group size to be allocated in GBs.


        :param storage_size_in_gbs: The storage_size_in_gbs of this UpdateCloudVmClusterDetails.
        :type: int
        """
        self._storage_size_in_gbs = storage_size_in_gbs

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateCloudVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateCloudVmClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateCloudVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateCloudVmClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateCloudVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateCloudVmClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateCloudVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateCloudVmClusterDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def data_collection_options(self):
        """
        Gets the data_collection_options of this UpdateCloudVmClusterDetails.

        :return: The data_collection_options of this UpdateCloudVmClusterDetails.
        :rtype: oci.database.models.DataCollectionOptions
        """
        return self._data_collection_options

    @data_collection_options.setter
    def data_collection_options(self, data_collection_options):
        """
        Sets the data_collection_options of this UpdateCloudVmClusterDetails.

        :param data_collection_options: The data_collection_options of this UpdateCloudVmClusterDetails.
        :type: oci.database.models.DataCollectionOptions
        """
        self._data_collection_options = data_collection_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
