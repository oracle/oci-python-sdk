# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobDatabase(object):
    """
    The Managed Database on which the job is executed.
    """

    #: A constant which can be used with the database_type property of a JobDatabase.
    #: This constant has a value of "EXTERNAL_SIDB"
    DATABASE_TYPE_EXTERNAL_SIDB = "EXTERNAL_SIDB"

    #: A constant which can be used with the database_type property of a JobDatabase.
    #: This constant has a value of "EXTERNAL_RAC"
    DATABASE_TYPE_EXTERNAL_RAC = "EXTERNAL_RAC"

    #: A constant which can be used with the database_type property of a JobDatabase.
    #: This constant has a value of "CLOUD_SIDB"
    DATABASE_TYPE_CLOUD_SIDB = "CLOUD_SIDB"

    #: A constant which can be used with the database_type property of a JobDatabase.
    #: This constant has a value of "CLOUD_RAC"
    DATABASE_TYPE_CLOUD_RAC = "CLOUD_RAC"

    #: A constant which can be used with the database_sub_type property of a JobDatabase.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a JobDatabase.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a JobDatabase.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the deployment_type property of a JobDatabase.
    #: This constant has a value of "ONPREMISE"
    DEPLOYMENT_TYPE_ONPREMISE = "ONPREMISE"

    #: A constant which can be used with the deployment_type property of a JobDatabase.
    #: This constant has a value of "BM"
    DEPLOYMENT_TYPE_BM = "BM"

    #: A constant which can be used with the deployment_type property of a JobDatabase.
    #: This constant has a value of "VM"
    DEPLOYMENT_TYPE_VM = "VM"

    #: A constant which can be used with the deployment_type property of a JobDatabase.
    #: This constant has a value of "EXADATA"
    DEPLOYMENT_TYPE_EXADATA = "EXADATA"

    #: A constant which can be used with the deployment_type property of a JobDatabase.
    #: This constant has a value of "EXADATA_CC"
    DEPLOYMENT_TYPE_EXADATA_CC = "EXADATA_CC"

    def __init__(self, **kwargs):
        """
        Initializes a new JobDatabase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this JobDatabase.
        :type id: str

        :param name:
            The value to assign to the name property of this JobDatabase.
        :type name: str

        :param database_type:
            The value to assign to the database_type property of this JobDatabase.
            Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param database_sub_type:
            The value to assign to the database_sub_type property of this JobDatabase.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param deployment_type:
            The value to assign to the deployment_type property of this JobDatabase.
            Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_type: str

        :param is_cluster:
            The value to assign to the is_cluster property of this JobDatabase.
        :type is_cluster: bool

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'database_type': 'str',
            'database_sub_type': 'str',
            'deployment_type': 'str',
            'is_cluster': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'database_type': 'databaseType',
            'database_sub_type': 'databaseSubType',
            'deployment_type': 'deploymentType',
            'is_cluster': 'isCluster'
        }

        self._id = None
        self._name = None
        self._database_type = None
        self._database_sub_type = None
        self._deployment_type = None
        self._is_cluster = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this JobDatabase.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this JobDatabase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobDatabase.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this JobDatabase.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this JobDatabase.
        The name of the Managed Database.


        :return: The name of this JobDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this JobDatabase.
        The name of the Managed Database.


        :param name: The name of this JobDatabase.
        :type: str
        """
        self._name = name

    @property
    def database_type(self):
        """
        Gets the database_type of this JobDatabase.
        The type of Oracle Database installation.

        Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this JobDatabase.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this JobDatabase.
        The type of Oracle Database installation.


        :param database_type: The database_type of this JobDatabase.
        :type: str
        """
        allowed_values = ["EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def database_sub_type(self):
        """
        Gets the database_sub_type of this JobDatabase.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_sub_type of this JobDatabase.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this JobDatabase.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.


        :param database_sub_type: The database_sub_type of this JobDatabase.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._database_sub_type = database_sub_type

    @property
    def deployment_type(self):
        """
        Gets the deployment_type of this JobDatabase.
        A list of the supported infrastructure that can be used to deploy the database.

        Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_type of this JobDatabase.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this JobDatabase.
        A list of the supported infrastructure that can be used to deploy the database.


        :param deployment_type: The deployment_type of this JobDatabase.
        :type: str
        """
        allowed_values = ["ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            deployment_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_type = deployment_type

    @property
    def is_cluster(self):
        """
        Gets the is_cluster of this JobDatabase.
        Indicates whether the Oracle Database is part of a cluster.


        :return: The is_cluster of this JobDatabase.
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """
        Sets the is_cluster of this JobDatabase.
        Indicates whether the Oracle Database is part of a cluster.


        :param is_cluster: The is_cluster of this JobDatabase.
        :type: bool
        """
        self._is_cluster = is_cluster

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
