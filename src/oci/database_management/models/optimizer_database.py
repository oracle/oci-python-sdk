# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OptimizerDatabase(object):
    """
    The subset information of the Managed Database resource, which is used by Optimizer Statistics.
    """

    #: A constant which can be used with the db_type property of a OptimizerDatabase.
    #: This constant has a value of "EXTERNAL_SIDB"
    DB_TYPE_EXTERNAL_SIDB = "EXTERNAL_SIDB"

    #: A constant which can be used with the db_type property of a OptimizerDatabase.
    #: This constant has a value of "EXTERNAL_RAC"
    DB_TYPE_EXTERNAL_RAC = "EXTERNAL_RAC"

    #: A constant which can be used with the db_type property of a OptimizerDatabase.
    #: This constant has a value of "CLOUD_SIDB"
    DB_TYPE_CLOUD_SIDB = "CLOUD_SIDB"

    #: A constant which can be used with the db_type property of a OptimizerDatabase.
    #: This constant has a value of "CLOUD_RAC"
    DB_TYPE_CLOUD_RAC = "CLOUD_RAC"

    #: A constant which can be used with the db_type property of a OptimizerDatabase.
    #: This constant has a value of "SHARED"
    DB_TYPE_SHARED = "SHARED"

    #: A constant which can be used with the db_type property of a OptimizerDatabase.
    #: This constant has a value of "DEDICATED"
    DB_TYPE_DEDICATED = "DEDICATED"

    #: A constant which can be used with the db_sub_type property of a OptimizerDatabase.
    #: This constant has a value of "CDB"
    DB_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the db_sub_type property of a OptimizerDatabase.
    #: This constant has a value of "PDB"
    DB_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the db_sub_type property of a OptimizerDatabase.
    #: This constant has a value of "NON_CDB"
    DB_SUB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the db_sub_type property of a OptimizerDatabase.
    #: This constant has a value of "ACD"
    DB_SUB_TYPE_ACD = "ACD"

    #: A constant which can be used with the db_sub_type property of a OptimizerDatabase.
    #: This constant has a value of "ADB"
    DB_SUB_TYPE_ADB = "ADB"

    #: A constant which can be used with the db_deployment_type property of a OptimizerDatabase.
    #: This constant has a value of "ONPREMISE"
    DB_DEPLOYMENT_TYPE_ONPREMISE = "ONPREMISE"

    #: A constant which can be used with the db_deployment_type property of a OptimizerDatabase.
    #: This constant has a value of "BM"
    DB_DEPLOYMENT_TYPE_BM = "BM"

    #: A constant which can be used with the db_deployment_type property of a OptimizerDatabase.
    #: This constant has a value of "VM"
    DB_DEPLOYMENT_TYPE_VM = "VM"

    #: A constant which can be used with the db_deployment_type property of a OptimizerDatabase.
    #: This constant has a value of "EXADATA"
    DB_DEPLOYMENT_TYPE_EXADATA = "EXADATA"

    #: A constant which can be used with the db_deployment_type property of a OptimizerDatabase.
    #: This constant has a value of "EXADATA_CC"
    DB_DEPLOYMENT_TYPE_EXADATA_CC = "EXADATA_CC"

    #: A constant which can be used with the db_deployment_type property of a OptimizerDatabase.
    #: This constant has a value of "AUTONOMOUS"
    DB_DEPLOYMENT_TYPE_AUTONOMOUS = "AUTONOMOUS"

    def __init__(self, **kwargs):
        """
        Initializes a new OptimizerDatabase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OptimizerDatabase.
        :type id: str

        :param name:
            The value to assign to the name property of this OptimizerDatabase.
        :type name: str

        :param db_type:
            The value to assign to the db_type property of this OptimizerDatabase.
            Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_type: str

        :param db_sub_type:
            The value to assign to the db_sub_type property of this OptimizerDatabase.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_sub_type: str

        :param db_deployment_type:
            The value to assign to the db_deployment_type property of this OptimizerDatabase.
            Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_deployment_type: str

        :param db_version:
            The value to assign to the db_version property of this OptimizerDatabase.
        :type db_version: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OptimizerDatabase.
        :type compartment_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'db_type': 'str',
            'db_sub_type': 'str',
            'db_deployment_type': 'str',
            'db_version': 'str',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'db_type': 'dbType',
            'db_sub_type': 'dbSubType',
            'db_deployment_type': 'dbDeploymentType',
            'db_version': 'dbVersion',
            'compartment_id': 'compartmentId'
        }

        self._id = None
        self._name = None
        self._db_type = None
        self._db_sub_type = None
        self._db_deployment_type = None
        self._db_version = None
        self._compartment_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OptimizerDatabase.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this OptimizerDatabase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OptimizerDatabase.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this OptimizerDatabase.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this OptimizerDatabase.
        The name of the Managed Database.


        :return: The name of this OptimizerDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OptimizerDatabase.
        The name of the Managed Database.


        :param name: The name of this OptimizerDatabase.
        :type: str
        """
        self._name = name

    @property
    def db_type(self):
        """
        **[Required]** Gets the db_type of this OptimizerDatabase.
        The type of Oracle Database installation.

        Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The db_type of this OptimizerDatabase.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """
        Sets the db_type of this OptimizerDatabase.
        The type of Oracle Database installation.


        :param db_type: The db_type of this OptimizerDatabase.
        :type: str
        """
        allowed_values = ["EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED"]
        if not value_allowed_none_or_none_sentinel(db_type, allowed_values):
            db_type = 'UNKNOWN_ENUM_VALUE'
        self._db_type = db_type

    @property
    def db_sub_type(self):
        """
        **[Required]** Gets the db_sub_type of this OptimizerDatabase.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The db_sub_type of this OptimizerDatabase.
        :rtype: str
        """
        return self._db_sub_type

    @db_sub_type.setter
    def db_sub_type(self, db_sub_type):
        """
        Sets the db_sub_type of this OptimizerDatabase.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.


        :param db_sub_type: The db_sub_type of this OptimizerDatabase.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB", "ACD", "ADB"]
        if not value_allowed_none_or_none_sentinel(db_sub_type, allowed_values):
            db_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._db_sub_type = db_sub_type

    @property
    def db_deployment_type(self):
        """
        **[Required]** Gets the db_deployment_type of this OptimizerDatabase.
        The infrastructure used to deploy the Oracle Database.

        Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The db_deployment_type of this OptimizerDatabase.
        :rtype: str
        """
        return self._db_deployment_type

    @db_deployment_type.setter
    def db_deployment_type(self, db_deployment_type):
        """
        Sets the db_deployment_type of this OptimizerDatabase.
        The infrastructure used to deploy the Oracle Database.


        :param db_deployment_type: The db_deployment_type of this OptimizerDatabase.
        :type: str
        """
        allowed_values = ["ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS"]
        if not value_allowed_none_or_none_sentinel(db_deployment_type, allowed_values):
            db_deployment_type = 'UNKNOWN_ENUM_VALUE'
        self._db_deployment_type = db_deployment_type

    @property
    def db_version(self):
        """
        **[Required]** Gets the db_version of this OptimizerDatabase.
        The version of the Oracle Database.


        :return: The db_version of this OptimizerDatabase.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this OptimizerDatabase.
        The version of the Oracle Database.


        :param db_version: The db_version of this OptimizerDatabase.
        :type: str
        """
        self._db_version = db_version

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OptimizerDatabase.
        The `OCID`__ of the compartment in which the Managed Database resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this OptimizerDatabase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OptimizerDatabase.
        The `OCID`__ of the compartment in which the Managed Database resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this OptimizerDatabase.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
