# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousDatabaseBase(object):
    """
    Details to create an Oracle Autonomous Database.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the db_workload property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "OLTP"
    DB_WORKLOAD_OLTP = "OLTP"

    #: A constant which can be used with the db_workload property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "DW"
    DB_WORKLOAD_DW = "DW"

    #: A constant which can be used with the license_model property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the source property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "NONE"
    SOURCE_NONE = "NONE"

    #: A constant which can be used with the source property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "DATABASE"
    SOURCE_DATABASE = "DATABASE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousDatabaseBase object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.CreateAutonomousDatabaseCloneDetails`
        * :class:`~oci.database.models.CreateAutonomousDatabaseDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAutonomousDatabaseBase.
        :type compartment_id: str

        :param db_name:
            The value to assign to the db_name property of this CreateAutonomousDatabaseBase.
        :type db_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateAutonomousDatabaseBase.
        :type cpu_core_count: int

        :param db_workload:
            The value to assign to the db_workload property of this CreateAutonomousDatabaseBase.
            Allowed values for this property are: "OLTP", "DW"
        :type db_workload: str

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this CreateAutonomousDatabaseBase.
        :type data_storage_size_in_tbs: int

        :param admin_password:
            The value to assign to the admin_password property of this CreateAutonomousDatabaseBase.
        :type admin_password: str

        :param display_name:
            The value to assign to the display_name property of this CreateAutonomousDatabaseBase.
        :type display_name: str

        :param license_model:
            The value to assign to the license_model property of this CreateAutonomousDatabaseBase.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAutonomousDatabaseBase.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAutonomousDatabaseBase.
        :type defined_tags: dict(str, dict(str, object))

        :param source:
            The value to assign to the source property of this CreateAutonomousDatabaseBase.
            Allowed values for this property are: "NONE", "DATABASE"
        :type source: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'db_name': 'str',
            'cpu_core_count': 'int',
            'db_workload': 'str',
            'data_storage_size_in_tbs': 'int',
            'admin_password': 'str',
            'display_name': 'str',
            'license_model': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'source': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'db_name': 'dbName',
            'cpu_core_count': 'cpuCoreCount',
            'db_workload': 'dbWorkload',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'admin_password': 'adminPassword',
            'display_name': 'displayName',
            'license_model': 'licenseModel',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'source': 'source'
        }

        self._compartment_id = None
        self._db_name = None
        self._cpu_core_count = None
        self._db_workload = None
        self._data_storage_size_in_tbs = None
        self._admin_password = None
        self._display_name = None
        self._license_model = None
        self._freeform_tags = None
        self._defined_tags = None
        self._source = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['source']

        if type == 'DATABASE':
            return 'CreateAutonomousDatabaseCloneDetails'

        if type == 'NONE':
            return 'CreateAutonomousDatabaseDetails'
        else:
            return 'CreateAutonomousDatabaseBase'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAutonomousDatabaseBase.
        The `OCID`__ of the compartment of the autonomous database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAutonomousDatabaseBase.
        The `OCID`__ of the compartment of the autonomous database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_name(self):
        """
        **[Required]** Gets the db_name of this CreateAutonomousDatabaseBase.
        The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :return: The db_name of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this CreateAutonomousDatabaseBase.
        The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :param db_name: The db_name of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._db_name = db_name

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this CreateAutonomousDatabaseBase.
        The number of CPU Cores to be made available to the database.


        :return: The cpu_core_count of this CreateAutonomousDatabaseBase.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this CreateAutonomousDatabaseBase.
        The number of CPU Cores to be made available to the database.


        :param cpu_core_count: The cpu_core_count of this CreateAutonomousDatabaseBase.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def db_workload(self):
        """
        Gets the db_workload of this CreateAutonomousDatabaseBase.
        The autonomous database workload type. OLTP indicates an Autonomous Transaction Processing database and DW indicates an Autonomous Data Warehouse. The default is OLTP.

        Allowed values for this property are: "OLTP", "DW"


        :return: The db_workload of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this CreateAutonomousDatabaseBase.
        The autonomous database workload type. OLTP indicates an Autonomous Transaction Processing database and DW indicates an Autonomous Data Warehouse. The default is OLTP.


        :param db_workload: The db_workload of this CreateAutonomousDatabaseBase.
        :type: str
        """
        allowed_values = ["OLTP", "DW"]
        if not value_allowed_none_or_none_sentinel(db_workload, allowed_values):
            raise ValueError(
                "Invalid value for `db_workload`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._db_workload = db_workload

    @property
    def data_storage_size_in_tbs(self):
        """
        **[Required]** Gets the data_storage_size_in_tbs of this CreateAutonomousDatabaseBase.
        The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed.


        :return: The data_storage_size_in_tbs of this CreateAutonomousDatabaseBase.
        :rtype: int
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this CreateAutonomousDatabaseBase.
        The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed.


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this CreateAutonomousDatabaseBase.
        :type: int
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def admin_password(self):
        """
        **[Required]** Gets the admin_password of this CreateAutonomousDatabaseBase.
        The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.


        :return: The admin_password of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this CreateAutonomousDatabaseBase.
        The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.


        :param admin_password: The admin_password of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAutonomousDatabaseBase.
        The user-friendly name for the Autonomous Database. The name does not have to be unique.


        :return: The display_name of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAutonomousDatabaseBase.
        The user-friendly name for the Autonomous Database. The name does not have to be unique.


        :param display_name: The display_name of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._display_name = display_name

    @property
    def license_model(self):
        """
        Gets the license_model of this CreateAutonomousDatabaseBase.
        The Oracle license model that applies to the Oracle Autonomous Database. The default is BRING_YOUR_OWN_LICENSE.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CreateAutonomousDatabaseBase.
        The Oracle license model that applies to the Oracle Autonomous Database. The default is BRING_YOUR_OWN_LICENSE.


        :param license_model: The license_model of this CreateAutonomousDatabaseBase.
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
        Gets the freeform_tags of this CreateAutonomousDatabaseBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAutonomousDatabaseBase.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAutonomousDatabaseBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAutonomousDatabaseBase.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAutonomousDatabaseBase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAutonomousDatabaseBase.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAutonomousDatabaseBase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAutonomousDatabaseBase.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def source(self):
        """
        Gets the source of this CreateAutonomousDatabaseBase.
        The source of the database: Use NONE for creating a new Autonomous Database. Use DATABASE for creating a new Autonomous Database by cloning an existing Autonomous Database.

        Allowed values for this property are: "NONE", "DATABASE"


        :return: The source of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateAutonomousDatabaseBase.
        The source of the database: Use NONE for creating a new Autonomous Database. Use DATABASE for creating a new Autonomous Database by cloning an existing Autonomous Database.


        :param source: The source of this CreateAutonomousDatabaseBase.
        :type: str
        """
        allowed_values = ["NONE", "DATABASE"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            raise ValueError(
                "Invalid value for `source`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._source = source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
