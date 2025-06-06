# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseConnectionUrls(object):
    """
    The URLs for accessing Oracle Application Express (APEX) and SQL Developer Web with a browser from a Compute instance within your VCN or that has a direct connection to your VCN. Note that these URLs are provided by the console only for databases on `dedicated Exadata infrastructure`__.

    Example: `{\"sqlDevWebUrl\": \"https://<hostname>/ords...\", \"apexUrl\", \"https://<hostname>/ords...\"}`

    __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseConnectionUrls object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_dev_web_url:
            The value to assign to the sql_dev_web_url property of this AutonomousDatabaseConnectionUrls.
        :type sql_dev_web_url: str

        :param apex_url:
            The value to assign to the apex_url property of this AutonomousDatabaseConnectionUrls.
        :type apex_url: str

        :param machine_learning_user_management_url:
            The value to assign to the machine_learning_user_management_url property of this AutonomousDatabaseConnectionUrls.
        :type machine_learning_user_management_url: str

        :param graph_studio_url:
            The value to assign to the graph_studio_url property of this AutonomousDatabaseConnectionUrls.
        :type graph_studio_url: str

        :param mongo_db_url:
            The value to assign to the mongo_db_url property of this AutonomousDatabaseConnectionUrls.
        :type mongo_db_url: str

        :param machine_learning_notebook_url:
            The value to assign to the machine_learning_notebook_url property of this AutonomousDatabaseConnectionUrls.
        :type machine_learning_notebook_url: str

        :param ords_url:
            The value to assign to the ords_url property of this AutonomousDatabaseConnectionUrls.
        :type ords_url: str

        :param database_transforms_url:
            The value to assign to the database_transforms_url property of this AutonomousDatabaseConnectionUrls.
        :type database_transforms_url: str

        """
        self.swagger_types = {
            'sql_dev_web_url': 'str',
            'apex_url': 'str',
            'machine_learning_user_management_url': 'str',
            'graph_studio_url': 'str',
            'mongo_db_url': 'str',
            'machine_learning_notebook_url': 'str',
            'ords_url': 'str',
            'database_transforms_url': 'str'
        }
        self.attribute_map = {
            'sql_dev_web_url': 'sqlDevWebUrl',
            'apex_url': 'apexUrl',
            'machine_learning_user_management_url': 'machineLearningUserManagementUrl',
            'graph_studio_url': 'graphStudioUrl',
            'mongo_db_url': 'mongoDbUrl',
            'machine_learning_notebook_url': 'machineLearningNotebookUrl',
            'ords_url': 'ordsUrl',
            'database_transforms_url': 'databaseTransformsUrl'
        }
        self._sql_dev_web_url = None
        self._apex_url = None
        self._machine_learning_user_management_url = None
        self._graph_studio_url = None
        self._mongo_db_url = None
        self._machine_learning_notebook_url = None
        self._ords_url = None
        self._database_transforms_url = None

    @property
    def sql_dev_web_url(self):
        """
        Gets the sql_dev_web_url of this AutonomousDatabaseConnectionUrls.
        Oracle SQL Developer Web URL.


        :return: The sql_dev_web_url of this AutonomousDatabaseConnectionUrls.
        :rtype: str
        """
        return self._sql_dev_web_url

    @sql_dev_web_url.setter
    def sql_dev_web_url(self, sql_dev_web_url):
        """
        Sets the sql_dev_web_url of this AutonomousDatabaseConnectionUrls.
        Oracle SQL Developer Web URL.


        :param sql_dev_web_url: The sql_dev_web_url of this AutonomousDatabaseConnectionUrls.
        :type: str
        """
        self._sql_dev_web_url = sql_dev_web_url

    @property
    def apex_url(self):
        """
        Gets the apex_url of this AutonomousDatabaseConnectionUrls.
        Oracle Application Express (APEX) URL.


        :return: The apex_url of this AutonomousDatabaseConnectionUrls.
        :rtype: str
        """
        return self._apex_url

    @apex_url.setter
    def apex_url(self, apex_url):
        """
        Sets the apex_url of this AutonomousDatabaseConnectionUrls.
        Oracle Application Express (APEX) URL.


        :param apex_url: The apex_url of this AutonomousDatabaseConnectionUrls.
        :type: str
        """
        self._apex_url = apex_url

    @property
    def machine_learning_user_management_url(self):
        """
        Gets the machine_learning_user_management_url of this AutonomousDatabaseConnectionUrls.
        Oracle Machine Learning user management URL.


        :return: The machine_learning_user_management_url of this AutonomousDatabaseConnectionUrls.
        :rtype: str
        """
        return self._machine_learning_user_management_url

    @machine_learning_user_management_url.setter
    def machine_learning_user_management_url(self, machine_learning_user_management_url):
        """
        Sets the machine_learning_user_management_url of this AutonomousDatabaseConnectionUrls.
        Oracle Machine Learning user management URL.


        :param machine_learning_user_management_url: The machine_learning_user_management_url of this AutonomousDatabaseConnectionUrls.
        :type: str
        """
        self._machine_learning_user_management_url = machine_learning_user_management_url

    @property
    def graph_studio_url(self):
        """
        Gets the graph_studio_url of this AutonomousDatabaseConnectionUrls.
        The URL of the Graph Studio for the Autonomous Database.


        :return: The graph_studio_url of this AutonomousDatabaseConnectionUrls.
        :rtype: str
        """
        return self._graph_studio_url

    @graph_studio_url.setter
    def graph_studio_url(self, graph_studio_url):
        """
        Sets the graph_studio_url of this AutonomousDatabaseConnectionUrls.
        The URL of the Graph Studio for the Autonomous Database.


        :param graph_studio_url: The graph_studio_url of this AutonomousDatabaseConnectionUrls.
        :type: str
        """
        self._graph_studio_url = graph_studio_url

    @property
    def mongo_db_url(self):
        """
        Gets the mongo_db_url of this AutonomousDatabaseConnectionUrls.
        The URL of the MongoDB API for the Autonomous Database.


        :return: The mongo_db_url of this AutonomousDatabaseConnectionUrls.
        :rtype: str
        """
        return self._mongo_db_url

    @mongo_db_url.setter
    def mongo_db_url(self, mongo_db_url):
        """
        Sets the mongo_db_url of this AutonomousDatabaseConnectionUrls.
        The URL of the MongoDB API for the Autonomous Database.


        :param mongo_db_url: The mongo_db_url of this AutonomousDatabaseConnectionUrls.
        :type: str
        """
        self._mongo_db_url = mongo_db_url

    @property
    def machine_learning_notebook_url(self):
        """
        Gets the machine_learning_notebook_url of this AutonomousDatabaseConnectionUrls.
        The URL of the Oracle Machine Learning (OML) Notebook for the Autonomous Database.


        :return: The machine_learning_notebook_url of this AutonomousDatabaseConnectionUrls.
        :rtype: str
        """
        return self._machine_learning_notebook_url

    @machine_learning_notebook_url.setter
    def machine_learning_notebook_url(self, machine_learning_notebook_url):
        """
        Sets the machine_learning_notebook_url of this AutonomousDatabaseConnectionUrls.
        The URL of the Oracle Machine Learning (OML) Notebook for the Autonomous Database.


        :param machine_learning_notebook_url: The machine_learning_notebook_url of this AutonomousDatabaseConnectionUrls.
        :type: str
        """
        self._machine_learning_notebook_url = machine_learning_notebook_url

    @property
    def ords_url(self):
        """
        Gets the ords_url of this AutonomousDatabaseConnectionUrls.
        The Oracle REST Data Services (ORDS) URL of the Web Access for the Autonomous Database.


        :return: The ords_url of this AutonomousDatabaseConnectionUrls.
        :rtype: str
        """
        return self._ords_url

    @ords_url.setter
    def ords_url(self, ords_url):
        """
        Sets the ords_url of this AutonomousDatabaseConnectionUrls.
        The Oracle REST Data Services (ORDS) URL of the Web Access for the Autonomous Database.


        :param ords_url: The ords_url of this AutonomousDatabaseConnectionUrls.
        :type: str
        """
        self._ords_url = ords_url

    @property
    def database_transforms_url(self):
        """
        Gets the database_transforms_url of this AutonomousDatabaseConnectionUrls.
        The URL of the Database Transforms for the Autonomous Database.


        :return: The database_transforms_url of this AutonomousDatabaseConnectionUrls.
        :rtype: str
        """
        return self._database_transforms_url

    @database_transforms_url.setter
    def database_transforms_url(self, database_transforms_url):
        """
        Sets the database_transforms_url of this AutonomousDatabaseConnectionUrls.
        The URL of the Database Transforms for the Autonomous Database.


        :param database_transforms_url: The database_transforms_url of this AutonomousDatabaseConnectionUrls.
        :type: str
        """
        self._database_transforms_url = database_transforms_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
