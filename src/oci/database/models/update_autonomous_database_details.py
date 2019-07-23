# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


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

        """
        self.swagger_types = {
            'cpu_core_count': 'int',
            'data_storage_size_in_tbs': 'int',
            'display_name': 'str',
            'admin_password': 'str',
            'db_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'license_model': 'str',
            'whitelisted_ips': 'list[str]',
            'is_auto_scaling_enabled': 'bool'
        }

        self.attribute_map = {
            'cpu_core_count': 'cpuCoreCount',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'display_name': 'displayName',
            'admin_password': 'adminPassword',
            'db_name': 'dbName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'license_model': 'licenseModel',
            'whitelisted_ips': 'whitelistedIps',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled'
        }

        self._cpu_core_count = None
        self._data_storage_size_in_tbs = None
        self._display_name = None
        self._admin_password = None
        self._db_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._license_model = None
        self._whitelisted_ips = None
        self._is_auto_scaling_enabled = None

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
        The user-friendly name for the Autonomous Database. The name does not have to be unique.


        :return: The display_name of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAutonomousDatabaseDetails.
        The user-friendly name for the Autonomous Database. The name does not have to be unique.


        :param display_name: The display_name of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._display_name = display_name

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
        New name for this Autonomous Database. It must begin with an alphabetic character and can contain a
        maximum of eight alphanumeric characters. Special characters are not permitted. This is valid only
        for dedicated databases.


        :return: The db_name of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this UpdateAutonomousDatabaseDetails.
        New name for this Autonomous Database. It must begin with an alphabetic character and can contain a
        maximum of eight alphanumeric characters. Special characters are not permitted. This is valid only
        for dedicated databases.


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

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

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

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAutonomousDatabaseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def license_model(self):
        """
        Gets the license_model of this UpdateAutonomousDatabaseDetails.
        The new Oracle license model that applies to the Oracle Autonomous Transaction Processing database. Note that when updating an Autonomous Database that uses the `dedicated deployment`__ option, this attribute must be null.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adbddoverview.htm

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this UpdateAutonomousDatabaseDetails.
        The new Oracle license model that applies to the Oracle Autonomous Transaction Processing database. Note that when updating an Autonomous Database that uses the `dedicated deployment`__ option, this attribute must be null.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adbddoverview.htm


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
        The client IP access control list (ACL). This feature is available for `serverless deployments`__ only.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. This is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet. To delete all the existing white listed IP\u2019s, use an array with a single empty string entry.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :return: The whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        :rtype: list[str]
        """
        return self._whitelisted_ips

    @whitelisted_ips.setter
    def whitelisted_ips(self, whitelisted_ips):
        """
        Sets the whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        The client IP access control list (ACL). This feature is available for `serverless deployments`__ only.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. This is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet. To delete all the existing white listed IP\u2019s, use an array with a single empty string entry.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :param whitelisted_ips: The whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        :type: list[str]
        """
        self._whitelisted_ips = whitelisted_ips

    @property
    def is_auto_scaling_enabled(self):
        """
        Gets the is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates if auto scaling is enabled for the Autonomous Database CPU core count. The default value is false. Note that auto scaling is available for `serverless deployments`__ only.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :return: The is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates if auto scaling is enabled for the Autonomous Database CPU core count. The default value is false. Note that auto scaling is available for `serverless deployments`__ only.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
