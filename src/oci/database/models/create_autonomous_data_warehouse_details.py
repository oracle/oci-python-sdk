# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousDataWarehouseDetails(object):
    """
    **Deprecated.** See :func:`create_autonomous_database_details` for reference information about creating an Oracle Autonomous Data Warehouse.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the license_model property of a CreateAutonomousDataWarehouseDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CreateAutonomousDataWarehouseDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousDataWarehouseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAutonomousDataWarehouseDetails.
        :type compartment_id: str

        :param db_name:
            The value to assign to the db_name property of this CreateAutonomousDataWarehouseDetails.
        :type db_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateAutonomousDataWarehouseDetails.
        :type cpu_core_count: int

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this CreateAutonomousDataWarehouseDetails.
        :type data_storage_size_in_tbs: int

        :param admin_password:
            The value to assign to the admin_password property of this CreateAutonomousDataWarehouseDetails.
        :type admin_password: str

        :param display_name:
            The value to assign to the display_name property of this CreateAutonomousDataWarehouseDetails.
        :type display_name: str

        :param license_model:
            The value to assign to the license_model property of this CreateAutonomousDataWarehouseDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAutonomousDataWarehouseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAutonomousDataWarehouseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'db_name': 'str',
            'cpu_core_count': 'int',
            'data_storage_size_in_tbs': 'int',
            'admin_password': 'str',
            'display_name': 'str',
            'license_model': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'db_name': 'dbName',
            'cpu_core_count': 'cpuCoreCount',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'admin_password': 'adminPassword',
            'display_name': 'displayName',
            'license_model': 'licenseModel',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._db_name = None
        self._cpu_core_count = None
        self._data_storage_size_in_tbs = None
        self._admin_password = None
        self._display_name = None
        self._license_model = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAutonomousDataWarehouseDetails.
        The `OCID`__ of the compartment of the Autonomous Data Warehouse.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateAutonomousDataWarehouseDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAutonomousDataWarehouseDetails.
        The `OCID`__ of the compartment of the Autonomous Data Warehouse.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateAutonomousDataWarehouseDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_name(self):
        """
        **[Required]** Gets the db_name of this CreateAutonomousDataWarehouseDetails.
        The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :return: The db_name of this CreateAutonomousDataWarehouseDetails.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this CreateAutonomousDataWarehouseDetails.
        The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :param db_name: The db_name of this CreateAutonomousDataWarehouseDetails.
        :type: str
        """
        self._db_name = db_name

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this CreateAutonomousDataWarehouseDetails.
        The number of CPU Cores to be made available to the database.


        :return: The cpu_core_count of this CreateAutonomousDataWarehouseDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this CreateAutonomousDataWarehouseDetails.
        The number of CPU Cores to be made available to the database.


        :param cpu_core_count: The cpu_core_count of this CreateAutonomousDataWarehouseDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def data_storage_size_in_tbs(self):
        """
        **[Required]** Gets the data_storage_size_in_tbs of this CreateAutonomousDataWarehouseDetails.
        Size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed.


        :return: The data_storage_size_in_tbs of this CreateAutonomousDataWarehouseDetails.
        :rtype: int
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this CreateAutonomousDataWarehouseDetails.
        Size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed.


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this CreateAutonomousDataWarehouseDetails.
        :type: int
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def admin_password(self):
        """
        **[Required]** Gets the admin_password of this CreateAutonomousDataWarehouseDetails.
        The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.


        :return: The admin_password of this CreateAutonomousDataWarehouseDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this CreateAutonomousDataWarehouseDetails.
        The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.


        :param admin_password: The admin_password of this CreateAutonomousDataWarehouseDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAutonomousDataWarehouseDetails.
        The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.


        :return: The display_name of this CreateAutonomousDataWarehouseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAutonomousDataWarehouseDetails.
        The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.


        :param display_name: The display_name of this CreateAutonomousDataWarehouseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def license_model(self):
        """
        Gets the license_model of this CreateAutonomousDataWarehouseDetails.
        The Oracle license model that applies to the Oracle Autonomous Data Warehouse. The default is BRING_YOUR_OWN_LICENSE.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this CreateAutonomousDataWarehouseDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CreateAutonomousDataWarehouseDetails.
        The Oracle license model that applies to the Oracle Autonomous Data Warehouse. The default is BRING_YOUR_OWN_LICENSE.


        :param license_model: The license_model of this CreateAutonomousDataWarehouseDetails.
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
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAutonomousDataWarehouseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAutonomousDataWarehouseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAutonomousDataWarehouseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAutonomousDataWarehouseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAutonomousDataWarehouseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAutonomousDataWarehouseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAutonomousDataWarehouseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAutonomousDataWarehouseDetails.
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
