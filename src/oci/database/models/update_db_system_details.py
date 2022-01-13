# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDbSystemDetails(object):
    """
    Describes the parameters for updating the DB system.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the license_model property of a UpdateDbSystemDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a UpdateDbSystemDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDbSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this UpdateDbSystemDetails.
        :type cpu_core_count: int

        :param version:
            The value to assign to the version property of this UpdateDbSystemDetails.
        :type version: oci.database.models.PatchDetails

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this UpdateDbSystemDetails.
        :type ssh_public_keys: list[str]

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this UpdateDbSystemDetails.
        :type data_storage_size_in_gbs: int

        :param reco_storage_size_in_gbs:
            The value to assign to the reco_storage_size_in_gbs property of this UpdateDbSystemDetails.
        :type reco_storage_size_in_gbs: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDbSystemDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDbSystemDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param shape:
            The value to assign to the shape property of this UpdateDbSystemDetails.
        :type shape: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateDbSystemDetails.
        :type nsg_ids: list[str]

        :param backup_network_nsg_ids:
            The value to assign to the backup_network_nsg_ids property of this UpdateDbSystemDetails.
        :type backup_network_nsg_ids: list[str]

        :param license_model:
            The value to assign to the license_model property of this UpdateDbSystemDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param maintenance_window_details:
            The value to assign to the maintenance_window_details property of this UpdateDbSystemDetails.
        :type maintenance_window_details: oci.database.models.MaintenanceWindow

        """
        self.swagger_types = {
            'cpu_core_count': 'int',
            'version': 'PatchDetails',
            'ssh_public_keys': 'list[str]',
            'data_storage_size_in_gbs': 'int',
            'reco_storage_size_in_gbs': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'shape': 'str',
            'nsg_ids': 'list[str]',
            'backup_network_nsg_ids': 'list[str]',
            'license_model': 'str',
            'maintenance_window_details': 'MaintenanceWindow'
        }

        self.attribute_map = {
            'cpu_core_count': 'cpuCoreCount',
            'version': 'version',
            'ssh_public_keys': 'sshPublicKeys',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'reco_storage_size_in_gbs': 'recoStorageSizeInGBs',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'shape': 'shape',
            'nsg_ids': 'nsgIds',
            'backup_network_nsg_ids': 'backupNetworkNsgIds',
            'license_model': 'licenseModel',
            'maintenance_window_details': 'maintenanceWindowDetails'
        }

        self._cpu_core_count = None
        self._version = None
        self._ssh_public_keys = None
        self._data_storage_size_in_gbs = None
        self._reco_storage_size_in_gbs = None
        self._freeform_tags = None
        self._defined_tags = None
        self._shape = None
        self._nsg_ids = None
        self._backup_network_nsg_ids = None
        self._license_model = None
        self._maintenance_window_details = None

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this UpdateDbSystemDetails.
        The new number of CPU cores to set for the DB system. Not applicable for virtual machine DB systems.


        :return: The cpu_core_count of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this UpdateDbSystemDetails.
        The new number of CPU cores to set for the DB system. Not applicable for virtual machine DB systems.


        :param cpu_core_count: The cpu_core_count of this UpdateDbSystemDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def version(self):
        """
        Gets the version of this UpdateDbSystemDetails.

        :return: The version of this UpdateDbSystemDetails.
        :rtype: oci.database.models.PatchDetails
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this UpdateDbSystemDetails.

        :param version: The version of this UpdateDbSystemDetails.
        :type: oci.database.models.PatchDetails
        """
        self._version = version

    @property
    def ssh_public_keys(self):
        """
        Gets the ssh_public_keys of this UpdateDbSystemDetails.
        The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 40,000 characters.


        :return: The ssh_public_keys of this UpdateDbSystemDetails.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this UpdateDbSystemDetails.
        The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 40,000 characters.


        :param ssh_public_keys: The ssh_public_keys of this UpdateDbSystemDetails.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this UpdateDbSystemDetails.
        The size, in gigabytes, to scale the attached storage up to for this virtual machine DB system. This value must be greater than current storage size. Note that the resulting total storage size attached will be greater than the amount requested to allow for REDO/RECO space and software volume. Applies only to virtual machine DB systems.


        :return: The data_storage_size_in_gbs of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this UpdateDbSystemDetails.
        The size, in gigabytes, to scale the attached storage up to for this virtual machine DB system. This value must be greater than current storage size. Note that the resulting total storage size attached will be greater than the amount requested to allow for REDO/RECO space and software volume. Applies only to virtual machine DB systems.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this UpdateDbSystemDetails.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def reco_storage_size_in_gbs(self):
        """
        Gets the reco_storage_size_in_gbs of this UpdateDbSystemDetails.
        The size, in gigabytes, to scale the attached RECO storage up to for this virtual machine DB system. This value must be greater than current storage size. Note that the resulting total storage size attached will be greater than the amount requested to allow for the software volume. Applies only to virtual machine DB systems.


        :return: The reco_storage_size_in_gbs of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._reco_storage_size_in_gbs

    @reco_storage_size_in_gbs.setter
    def reco_storage_size_in_gbs(self, reco_storage_size_in_gbs):
        """
        Sets the reco_storage_size_in_gbs of this UpdateDbSystemDetails.
        The size, in gigabytes, to scale the attached RECO storage up to for this virtual machine DB system. This value must be greater than current storage size. Note that the resulting total storage size attached will be greater than the amount requested to allow for the software volume. Applies only to virtual machine DB systems.


        :param reco_storage_size_in_gbs: The reco_storage_size_in_gbs of this UpdateDbSystemDetails.
        :type: int
        """
        self._reco_storage_size_in_gbs = reco_storage_size_in_gbs

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDbSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateDbSystemDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDbSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateDbSystemDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateDbSystemDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateDbSystemDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def shape(self):
        """
        Gets the shape of this UpdateDbSystemDetails.
        The shape of the DB system. The shape determines resources allocated to the DB system.
        - For virtual machine shapes, the number of CPU cores and memory

        To get a list of shapes, use the :func:`list_db_system_shapes` operation.


        :return: The shape of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this UpdateDbSystemDetails.
        The shape of the DB system. The shape determines resources allocated to the DB system.
        - For virtual machine shapes, the number of CPU cores and memory

        To get a list of shapes, use the :func:`list_db_system_shapes` operation.


        :param shape: The shape of this UpdateDbSystemDetails.
        :type: str
        """
        self._shape = shape

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateDbSystemDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this UpdateDbSystemDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateDbSystemDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this UpdateDbSystemDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def backup_network_nsg_ids(self):
        """
        Gets the backup_network_nsg_ids of this UpdateDbSystemDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The backup_network_nsg_ids of this UpdateDbSystemDetails.
        :rtype: list[str]
        """
        return self._backup_network_nsg_ids

    @backup_network_nsg_ids.setter
    def backup_network_nsg_ids(self, backup_network_nsg_ids):
        """
        Sets the backup_network_nsg_ids of this UpdateDbSystemDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param backup_network_nsg_ids: The backup_network_nsg_ids of this UpdateDbSystemDetails.
        :type: list[str]
        """
        self._backup_network_nsg_ids = backup_network_nsg_ids

    @property
    def license_model(self):
        """
        Gets the license_model of this UpdateDbSystemDetails.
        The Oracle Database license model that applies to all databases on the DB system. The default is LICENSE_INCLUDED.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this UpdateDbSystemDetails.
        The Oracle Database license model that applies to all databases on the DB system. The default is LICENSE_INCLUDED.


        :param license_model: The license_model of this UpdateDbSystemDetails.
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
    def maintenance_window_details(self):
        """
        Gets the maintenance_window_details of this UpdateDbSystemDetails.

        :return: The maintenance_window_details of this UpdateDbSystemDetails.
        :rtype: oci.database.models.MaintenanceWindow
        """
        return self._maintenance_window_details

    @maintenance_window_details.setter
    def maintenance_window_details(self, maintenance_window_details):
        """
        Sets the maintenance_window_details of this UpdateDbSystemDetails.

        :param maintenance_window_details: The maintenance_window_details of this UpdateDbSystemDetails.
        :type: oci.database.models.MaintenanceWindow
        """
        self._maintenance_window_details = maintenance_window_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
