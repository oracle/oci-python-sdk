# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAutonomousDatabaseDetails(object):
    """
    Details to update an Oracle Autonomous Database.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the license_model property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAutonomousDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this UpdateAutonomousDatabaseDetails.
        :type cpu_core_count: int

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this UpdateAutonomousDatabaseDetails.
        :type data_storage_size_in_tbs: int

        :param display_name:
            The value to assign to the display_name property of this UpdateAutonomousDatabaseDetails.
        :type display_name: str

        :param is_free_tier:
            The value to assign to the is_free_tier property of this UpdateAutonomousDatabaseDetails.
        :type is_free_tier: bool

        :param admin_password:
            The value to assign to the admin_password property of this UpdateAutonomousDatabaseDetails.
        :type admin_password: str

        :param db_name:
            The value to assign to the db_name property of this UpdateAutonomousDatabaseDetails.
        :type db_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAutonomousDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAutonomousDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param license_model:
            The value to assign to the license_model property of this UpdateAutonomousDatabaseDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param whitelisted_ips:
            The value to assign to the whitelisted_ips property of this UpdateAutonomousDatabaseDetails.
        :type whitelisted_ips: list[str]

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this UpdateAutonomousDatabaseDetails.
        :type is_auto_scaling_enabled: bool

        :param is_data_guard_enabled:
            The value to assign to the is_data_guard_enabled property of this UpdateAutonomousDatabaseDetails.
        :type is_data_guard_enabled: bool

        :param db_version:
            The value to assign to the db_version property of this UpdateAutonomousDatabaseDetails.
        :type db_version: str

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateAutonomousDatabaseDetails.
        :type subnet_id: str

        :param private_endpoint_label:
            The value to assign to the private_endpoint_label property of this UpdateAutonomousDatabaseDetails.
        :type private_endpoint_label: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateAutonomousDatabaseDetails.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'cpu_core_count': 'int',
            'data_storage_size_in_tbs': 'int',
            'display_name': 'str',
            'is_free_tier': 'bool',
            'admin_password': 'str',
            'db_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'license_model': 'str',
            'whitelisted_ips': 'list[str]',
            'is_auto_scaling_enabled': 'bool',
            'is_data_guard_enabled': 'bool',
            'db_version': 'str',
            'subnet_id': 'str',
            'private_endpoint_label': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'cpu_core_count': 'cpuCoreCount',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'display_name': 'displayName',
            'is_free_tier': 'isFreeTier',
            'admin_password': 'adminPassword',
            'db_name': 'dbName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'license_model': 'licenseModel',
            'whitelisted_ips': 'whitelistedIps',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'is_data_guard_enabled': 'isDataGuardEnabled',
            'db_version': 'dbVersion',
            'subnet_id': 'subnetId',
            'private_endpoint_label': 'privateEndpointLabel',
            'nsg_ids': 'nsgIds'
        }

        self._cpu_core_count = None
        self._data_storage_size_in_tbs = None
        self._display_name = None
        self._is_free_tier = None
        self._admin_password = None
        self._db_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._license_model = None
        self._whitelisted_ips = None
        self._is_auto_scaling_enabled = None
        self._is_data_guard_enabled = None
        self._db_version = None
        self._subnet_id = None
        self._private_endpoint_label = None
        self._nsg_ids = None

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this UpdateAutonomousDatabaseDetails.
        The number of CPU cores to be made available to the database.


        :return: The cpu_core_count of this UpdateAutonomousDatabaseDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this UpdateAutonomousDatabaseDetails.
        The number of CPU cores to be made available to the database.


        :param cpu_core_count: The cpu_core_count of this UpdateAutonomousDatabaseDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def data_storage_size_in_tbs(self):
        """
        Gets the data_storage_size_in_tbs of this UpdateAutonomousDatabaseDetails.
        The size, in terabytes, of the data volume that will be attached to the database.


        :return: The data_storage_size_in_tbs of this UpdateAutonomousDatabaseDetails.
        :rtype: int
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this UpdateAutonomousDatabaseDetails.
        The size, in terabytes, of the data volume that will be attached to the database.


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this UpdateAutonomousDatabaseDetails.
        :type: int
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAutonomousDatabaseDetails.
        The user-friendly name for the Autonomous Database. The name does not have to be unique. Can only be updated for Autonomous Databases
        using dedicated Exadata infrastructure.


        :return: The display_name of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAutonomousDatabaseDetails.
        The user-friendly name for the Autonomous Database. The name does not have to be unique. Can only be updated for Autonomous Databases
        using dedicated Exadata infrastructure.


        :param display_name: The display_name of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_free_tier(self):
        """
        Gets the is_free_tier of this UpdateAutonomousDatabaseDetails.
        Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled.


        :return: The is_free_tier of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_free_tier

    @is_free_tier.setter
    def is_free_tier(self, is_free_tier):
        """
        Sets the is_free_tier of this UpdateAutonomousDatabaseDetails.
        Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled.


        :param is_free_tier: The is_free_tier of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_free_tier = is_free_tier

    @property
    def admin_password(self):
        """
        Gets the admin_password of this UpdateAutonomousDatabaseDetails.
        The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing. It must be different from the last four passwords and it must not be a password used within the last 24 hours.


        :return: The admin_password of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this UpdateAutonomousDatabaseDetails.
        The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing. It must be different from the last four passwords and it must not be a password used within the last 24 hours.


        :param admin_password: The admin_password of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def db_name(self):
        """
        Gets the db_name of this UpdateAutonomousDatabaseDetails.
        New name for this Autonomous Database.
        For databases using dedicated Exadata infrastructure, the name must begin with an alphabetic character, and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.
        For databases using shared Exadata infrastructure, the name must begin with an alphabetic character, and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :return: The db_name of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this UpdateAutonomousDatabaseDetails.
        New name for this Autonomous Database.
        For databases using dedicated Exadata infrastructure, the name must begin with an alphabetic character, and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.
        For databases using shared Exadata infrastructure, the name must begin with an alphabetic character, and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :param db_name: The db_name of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._db_name = db_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAutonomousDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateAutonomousDatabaseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAutonomousDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateAutonomousDatabaseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAutonomousDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateAutonomousDatabaseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAutonomousDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAutonomousDatabaseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def license_model(self):
        """
        Gets the license_model of this UpdateAutonomousDatabaseDetails.
        The Oracle license model that applies to the Oracle Autonomous Database. Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adbddoverview.htm
        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this UpdateAutonomousDatabaseDetails.
        The Oracle license model that applies to the Oracle Autonomous Database. Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adbddoverview.htm
        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :param license_model: The license_model of this UpdateAutonomousDatabaseDetails.
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
    def whitelisted_ips(self):
        """
        Gets the whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        The client IP access control list (ACL). This feature is available for databases on `shared Exadata infrastructure`__ only.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. This is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID. To delete all the existing white listed IP\u2019s, use an array with a single empty string entry.
        To add the whitelist VCN specific subnet or IP, use a semicoln ';' as a deliminator to add the VCN specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.aaaaaaaard2hfx2nn3e5xeo6j6o62jga44xjizkw\",\"ocid1.vcn.oc1.sea.aaaaaaaard2hfx2nn3e5xeo6j6o62jga44xjizkw;1.1.1.1\",\"ocid1.vcn.oc1.sea.aaaaaaaard2hfx2nn3e5xeo6j6o62jga44xjizkw\"]`

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :return: The whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        :rtype: list[str]
        """
        return self._whitelisted_ips

    @whitelisted_ips.setter
    def whitelisted_ips(self, whitelisted_ips):
        """
        Sets the whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        The client IP access control list (ACL). This feature is available for databases on `shared Exadata infrastructure`__ only.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. This is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID. To delete all the existing white listed IP\u2019s, use an array with a single empty string entry.
        To add the whitelist VCN specific subnet or IP, use a semicoln ';' as a deliminator to add the VCN specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.aaaaaaaard2hfx2nn3e5xeo6j6o62jga44xjizkw\",\"ocid1.vcn.oc1.sea.aaaaaaaard2hfx2nn3e5xeo6j6o62jga44xjizkw;1.1.1.1\",\"ocid1.vcn.oc1.sea.aaaaaaaard2hfx2nn3e5xeo6j6o62jga44xjizkw\"]`

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :param whitelisted_ips: The whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        :type: list[str]
        """
        self._whitelisted_ips = whitelisted_ips

    @property
    def is_auto_scaling_enabled(self):
        """
        Gets the is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates whether to enable or disable auto scaling for the Autonomous Database OCPU core count. Setting to `true` enables auto scaling. Setting to `false` disables auto scaling. The default value is true. Auto scaling is available for databases on `shared Exadata infrastructure`__ only.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :return: The is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates whether to enable or disable auto scaling for the Autonomous Database OCPU core count. Setting to `true` enables auto scaling. Setting to `false` disables auto scaling. The default value is true. Auto scaling is available for databases on `shared Exadata infrastructure`__ only.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    @property
    def is_data_guard_enabled(self):
        """
        Gets the is_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates whether the Autonomous Database has Data Guard enabled.


        :return: The is_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_data_guard_enabled

    @is_data_guard_enabled.setter
    def is_data_guard_enabled(self, is_data_guard_enabled):
        """
        Sets the is_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates whether the Autonomous Database has Data Guard enabled.


        :param is_data_guard_enabled: The is_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_data_guard_enabled = is_data_guard_enabled

    @property
    def db_version(self):
        """
        Gets the db_version of this UpdateAutonomousDatabaseDetails.
        A valid Oracle Database version for Autonomous Database.


        :return: The db_version of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this UpdateAutonomousDatabaseDetails.
        A valid Oracle Database version for Autonomous Database.


        :param db_version: The db_version of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._db_version = db_version

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this UpdateAutonomousDatabaseDetails.
        The `OCID`__ of the subnet the resource is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.
        - For Autonomous Database, setting this will disable public secure access to the database.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and the backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this UpdateAutonomousDatabaseDetails.
        The `OCID`__ of the subnet the resource is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.
        - For Autonomous Database, setting this will disable public secure access to the database.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and the backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_endpoint_label(self):
        """
        Gets the private_endpoint_label of this UpdateAutonomousDatabaseDetails.
        The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change the same private endpoint database to the public endpoint database.


        :return: The private_endpoint_label of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._private_endpoint_label

    @private_endpoint_label.setter
    def private_endpoint_label(self, private_endpoint_label):
        """
        Sets the private_endpoint_label of this UpdateAutonomousDatabaseDetails.
        The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change the same private endpoint database to the public endpoint database.


        :param private_endpoint_label: The private_endpoint_label of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._private_endpoint_label = private_endpoint_label

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateAutonomousDatabaseDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this UpdateAutonomousDatabaseDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateAutonomousDatabaseDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this UpdateAutonomousDatabaseDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
