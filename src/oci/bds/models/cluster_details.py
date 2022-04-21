# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterDetails(object):
    """
    Specific info about a Hadoop cluster
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bda_version:
            The value to assign to the bda_version property of this ClusterDetails.
        :type bda_version: str

        :param bdm_version:
            The value to assign to the bdm_version property of this ClusterDetails.
        :type bdm_version: str

        :param bds_version:
            The value to assign to the bds_version property of this ClusterDetails.
        :type bds_version: str

        :param os_version:
            The value to assign to the os_version property of this ClusterDetails.
        :type os_version: str

        :param db_version:
            The value to assign to the db_version property of this ClusterDetails.
        :type db_version: str

        :param bd_cell_version:
            The value to assign to the bd_cell_version property of this ClusterDetails.
        :type bd_cell_version: str

        :param csql_cell_version:
            The value to assign to the csql_cell_version property of this ClusterDetails.
        :type csql_cell_version: str

        :param time_created:
            The value to assign to the time_created property of this ClusterDetails.
        :type time_created: datetime

        :param time_refreshed:
            The value to assign to the time_refreshed property of this ClusterDetails.
        :type time_refreshed: datetime

        :param cloudera_manager_url:
            The value to assign to the cloudera_manager_url property of this ClusterDetails.
        :type cloudera_manager_url: str

        :param ambari_url:
            The value to assign to the ambari_url property of this ClusterDetails.
        :type ambari_url: str

        :param big_data_manager_url:
            The value to assign to the big_data_manager_url property of this ClusterDetails.
        :type big_data_manager_url: str

        :param hue_server_url:
            The value to assign to the hue_server_url property of this ClusterDetails.
        :type hue_server_url: str

        :param odh_version:
            The value to assign to the odh_version property of this ClusterDetails.
        :type odh_version: str

        :param jupyter_hub_url:
            The value to assign to the jupyter_hub_url property of this ClusterDetails.
        :type jupyter_hub_url: str

        """
        self.swagger_types = {
            'bda_version': 'str',
            'bdm_version': 'str',
            'bds_version': 'str',
            'os_version': 'str',
            'db_version': 'str',
            'bd_cell_version': 'str',
            'csql_cell_version': 'str',
            'time_created': 'datetime',
            'time_refreshed': 'datetime',
            'cloudera_manager_url': 'str',
            'ambari_url': 'str',
            'big_data_manager_url': 'str',
            'hue_server_url': 'str',
            'odh_version': 'str',
            'jupyter_hub_url': 'str'
        }

        self.attribute_map = {
            'bda_version': 'bdaVersion',
            'bdm_version': 'bdmVersion',
            'bds_version': 'bdsVersion',
            'os_version': 'osVersion',
            'db_version': 'dbVersion',
            'bd_cell_version': 'bdCellVersion',
            'csql_cell_version': 'csqlCellVersion',
            'time_created': 'timeCreated',
            'time_refreshed': 'timeRefreshed',
            'cloudera_manager_url': 'clouderaManagerUrl',
            'ambari_url': 'ambariUrl',
            'big_data_manager_url': 'bigDataManagerUrl',
            'hue_server_url': 'hueServerUrl',
            'odh_version': 'odhVersion',
            'jupyter_hub_url': 'jupyterHubUrl'
        }

        self._bda_version = None
        self._bdm_version = None
        self._bds_version = None
        self._os_version = None
        self._db_version = None
        self._bd_cell_version = None
        self._csql_cell_version = None
        self._time_created = None
        self._time_refreshed = None
        self._cloudera_manager_url = None
        self._ambari_url = None
        self._big_data_manager_url = None
        self._hue_server_url = None
        self._odh_version = None
        self._jupyter_hub_url = None

    @property
    def bda_version(self):
        """
        Gets the bda_version of this ClusterDetails.
        BDA version installed in the cluster


        :return: The bda_version of this ClusterDetails.
        :rtype: str
        """
        return self._bda_version

    @bda_version.setter
    def bda_version(self, bda_version):
        """
        Sets the bda_version of this ClusterDetails.
        BDA version installed in the cluster


        :param bda_version: The bda_version of this ClusterDetails.
        :type: str
        """
        self._bda_version = bda_version

    @property
    def bdm_version(self):
        """
        Gets the bdm_version of this ClusterDetails.
        Big Data Manager version installed in the cluster.


        :return: The bdm_version of this ClusterDetails.
        :rtype: str
        """
        return self._bdm_version

    @bdm_version.setter
    def bdm_version(self, bdm_version):
        """
        Sets the bdm_version of this ClusterDetails.
        Big Data Manager version installed in the cluster.


        :param bdm_version: The bdm_version of this ClusterDetails.
        :type: str
        """
        self._bdm_version = bdm_version

    @property
    def bds_version(self):
        """
        Gets the bds_version of this ClusterDetails.
        Big Data Service version installed in the cluster.


        :return: The bds_version of this ClusterDetails.
        :rtype: str
        """
        return self._bds_version

    @bds_version.setter
    def bds_version(self, bds_version):
        """
        Sets the bds_version of this ClusterDetails.
        Big Data Service version installed in the cluster.


        :param bds_version: The bds_version of this ClusterDetails.
        :type: str
        """
        self._bds_version = bds_version

    @property
    def os_version(self):
        """
        Gets the os_version of this ClusterDetails.
        Oracle Linux version installed in the cluster.


        :return: The os_version of this ClusterDetails.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this ClusterDetails.
        Oracle Linux version installed in the cluster.


        :param os_version: The os_version of this ClusterDetails.
        :type: str
        """
        self._os_version = os_version

    @property
    def db_version(self):
        """
        Gets the db_version of this ClusterDetails.
        Cloud SQL query server database version.


        :return: The db_version of this ClusterDetails.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this ClusterDetails.
        Cloud SQL query server database version.


        :param db_version: The db_version of this ClusterDetails.
        :type: str
        """
        self._db_version = db_version

    @property
    def bd_cell_version(self):
        """
        Gets the bd_cell_version of this ClusterDetails.
        Cloud SQL cell version.


        :return: The bd_cell_version of this ClusterDetails.
        :rtype: str
        """
        return self._bd_cell_version

    @bd_cell_version.setter
    def bd_cell_version(self, bd_cell_version):
        """
        Sets the bd_cell_version of this ClusterDetails.
        Cloud SQL cell version.


        :param bd_cell_version: The bd_cell_version of this ClusterDetails.
        :type: str
        """
        self._bd_cell_version = bd_cell_version

    @property
    def csql_cell_version(self):
        """
        Gets the csql_cell_version of this ClusterDetails.
        Big Data SQL version.


        :return: The csql_cell_version of this ClusterDetails.
        :rtype: str
        """
        return self._csql_cell_version

    @csql_cell_version.setter
    def csql_cell_version(self, csql_cell_version):
        """
        Sets the csql_cell_version of this ClusterDetails.
        Big Data SQL version.


        :param csql_cell_version: The csql_cell_version of this ClusterDetails.
        :type: str
        """
        self._csql_cell_version = csql_cell_version

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ClusterDetails.
        The time the cluster was created, shown as an RFC 3339 formatted datetime string.


        :return: The time_created of this ClusterDetails.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ClusterDetails.
        The time the cluster was created, shown as an RFC 3339 formatted datetime string.


        :param time_created: The time_created of this ClusterDetails.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_refreshed(self):
        """
        Gets the time_refreshed of this ClusterDetails.
        The time the cluster was automatically or manually refreshed, shown as an RFC 3339 formatted datetime string.


        :return: The time_refreshed of this ClusterDetails.
        :rtype: datetime
        """
        return self._time_refreshed

    @time_refreshed.setter
    def time_refreshed(self, time_refreshed):
        """
        Sets the time_refreshed of this ClusterDetails.
        The time the cluster was automatically or manually refreshed, shown as an RFC 3339 formatted datetime string.


        :param time_refreshed: The time_refreshed of this ClusterDetails.
        :type: datetime
        """
        self._time_refreshed = time_refreshed

    @property
    def cloudera_manager_url(self):
        """
        Gets the cloudera_manager_url of this ClusterDetails.
        The URL of Cloudera Manager


        :return: The cloudera_manager_url of this ClusterDetails.
        :rtype: str
        """
        return self._cloudera_manager_url

    @cloudera_manager_url.setter
    def cloudera_manager_url(self, cloudera_manager_url):
        """
        Sets the cloudera_manager_url of this ClusterDetails.
        The URL of Cloudera Manager


        :param cloudera_manager_url: The cloudera_manager_url of this ClusterDetails.
        :type: str
        """
        self._cloudera_manager_url = cloudera_manager_url

    @property
    def ambari_url(self):
        """
        Gets the ambari_url of this ClusterDetails.
        The URL of Ambari


        :return: The ambari_url of this ClusterDetails.
        :rtype: str
        """
        return self._ambari_url

    @ambari_url.setter
    def ambari_url(self, ambari_url):
        """
        Sets the ambari_url of this ClusterDetails.
        The URL of Ambari


        :param ambari_url: The ambari_url of this ClusterDetails.
        :type: str
        """
        self._ambari_url = ambari_url

    @property
    def big_data_manager_url(self):
        """
        Gets the big_data_manager_url of this ClusterDetails.
        The URL of Big Data Manager.


        :return: The big_data_manager_url of this ClusterDetails.
        :rtype: str
        """
        return self._big_data_manager_url

    @big_data_manager_url.setter
    def big_data_manager_url(self, big_data_manager_url):
        """
        Sets the big_data_manager_url of this ClusterDetails.
        The URL of Big Data Manager.


        :param big_data_manager_url: The big_data_manager_url of this ClusterDetails.
        :type: str
        """
        self._big_data_manager_url = big_data_manager_url

    @property
    def hue_server_url(self):
        """
        Gets the hue_server_url of this ClusterDetails.
        The URL of the Hue server.


        :return: The hue_server_url of this ClusterDetails.
        :rtype: str
        """
        return self._hue_server_url

    @hue_server_url.setter
    def hue_server_url(self, hue_server_url):
        """
        Sets the hue_server_url of this ClusterDetails.
        The URL of the Hue server.


        :param hue_server_url: The hue_server_url of this ClusterDetails.
        :type: str
        """
        self._hue_server_url = hue_server_url

    @property
    def odh_version(self):
        """
        Gets the odh_version of this ClusterDetails.
        Version of the ODH (Oracle Distribution including Apache Hadoop) installed on the cluster.


        :return: The odh_version of this ClusterDetails.
        :rtype: str
        """
        return self._odh_version

    @odh_version.setter
    def odh_version(self, odh_version):
        """
        Sets the odh_version of this ClusterDetails.
        Version of the ODH (Oracle Distribution including Apache Hadoop) installed on the cluster.


        :param odh_version: The odh_version of this ClusterDetails.
        :type: str
        """
        self._odh_version = odh_version

    @property
    def jupyter_hub_url(self):
        """
        Gets the jupyter_hub_url of this ClusterDetails.
        The URL of the Jupyterhub.


        :return: The jupyter_hub_url of this ClusterDetails.
        :rtype: str
        """
        return self._jupyter_hub_url

    @jupyter_hub_url.setter
    def jupyter_hub_url(self, jupyter_hub_url):
        """
        Sets the jupyter_hub_url of this ClusterDetails.
        The URL of the Jupyterhub.


        :param jupyter_hub_url: The jupyter_hub_url of this ClusterDetails.
        :type: str
        """
        self._jupyter_hub_url = jupyter_hub_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
