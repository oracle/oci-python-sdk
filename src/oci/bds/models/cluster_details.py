# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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

        :param time_created:
            The value to assign to the time_created property of this ClusterDetails.
        :type time_created: datetime

        :param time_refreshed:
            The value to assign to the time_refreshed property of this ClusterDetails.
        :type time_refreshed: datetime

        :param cloudera_manager_url:
            The value to assign to the cloudera_manager_url property of this ClusterDetails.
        :type cloudera_manager_url: str

        :param big_data_manager_url:
            The value to assign to the big_data_manager_url property of this ClusterDetails.
        :type big_data_manager_url: str

        :param hue_server_url:
            The value to assign to the hue_server_url property of this ClusterDetails.
        :type hue_server_url: str

        """
        self.swagger_types = {
            'bda_version': 'str',
            'bdm_version': 'str',
            'time_created': 'datetime',
            'time_refreshed': 'datetime',
            'cloudera_manager_url': 'str',
            'big_data_manager_url': 'str',
            'hue_server_url': 'str'
        }

        self.attribute_map = {
            'bda_version': 'bdaVersion',
            'bdm_version': 'bdmVersion',
            'time_created': 'timeCreated',
            'time_refreshed': 'timeRefreshed',
            'cloudera_manager_url': 'clouderaManagerUrl',
            'big_data_manager_url': 'bigDataManagerUrl',
            'hue_server_url': 'hueServerUrl'
        }

        self._bda_version = None
        self._bdm_version = None
        self._time_created = None
        self._time_refreshed = None
        self._cloudera_manager_url = None
        self._big_data_manager_url = None
        self._hue_server_url = None

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
        BDM version installed in the cluster


        :return: The bdm_version of this ClusterDetails.
        :rtype: str
        """
        return self._bdm_version

    @bdm_version.setter
    def bdm_version(self, bdm_version):
        """
        Sets the bdm_version of this ClusterDetails.
        BDM version installed in the cluster


        :param bdm_version: The bdm_version of this ClusterDetails.
        :type: str
        """
        self._bdm_version = bdm_version

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ClusterDetails.
        The time the cluster was created. An RFC3339 formatted datetime string


        :return: The time_created of this ClusterDetails.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ClusterDetails.
        The time the cluster was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this ClusterDetails.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_refreshed(self):
        """
        Gets the time_refreshed of this ClusterDetails.
        The time the BDS instance was automatically, or manually refreshed.
        An RFC3339 formatted datetime string


        :return: The time_refreshed of this ClusterDetails.
        :rtype: datetime
        """
        return self._time_refreshed

    @time_refreshed.setter
    def time_refreshed(self, time_refreshed):
        """
        Sets the time_refreshed of this ClusterDetails.
        The time the BDS instance was automatically, or manually refreshed.
        An RFC3339 formatted datetime string


        :param time_refreshed: The time_refreshed of this ClusterDetails.
        :type: datetime
        """
        self._time_refreshed = time_refreshed

    @property
    def cloudera_manager_url(self):
        """
        Gets the cloudera_manager_url of this ClusterDetails.
        The URL of a Cloudera Manager


        :return: The cloudera_manager_url of this ClusterDetails.
        :rtype: str
        """
        return self._cloudera_manager_url

    @cloudera_manager_url.setter
    def cloudera_manager_url(self, cloudera_manager_url):
        """
        Sets the cloudera_manager_url of this ClusterDetails.
        The URL of a Cloudera Manager


        :param cloudera_manager_url: The cloudera_manager_url of this ClusterDetails.
        :type: str
        """
        self._cloudera_manager_url = cloudera_manager_url

    @property
    def big_data_manager_url(self):
        """
        Gets the big_data_manager_url of this ClusterDetails.
        The URL of a Big Data Manager


        :return: The big_data_manager_url of this ClusterDetails.
        :rtype: str
        """
        return self._big_data_manager_url

    @big_data_manager_url.setter
    def big_data_manager_url(self, big_data_manager_url):
        """
        Sets the big_data_manager_url of this ClusterDetails.
        The URL of a Big Data Manager


        :param big_data_manager_url: The big_data_manager_url of this ClusterDetails.
        :type: str
        """
        self._big_data_manager_url = big_data_manager_url

    @property
    def hue_server_url(self):
        """
        Gets the hue_server_url of this ClusterDetails.
        The URL of a Hue Server


        :return: The hue_server_url of this ClusterDetails.
        :rtype: str
        """
        return self._hue_server_url

    @hue_server_url.setter
    def hue_server_url(self, hue_server_url):
        """
        Sets the hue_server_url of this ClusterDetails.
        The URL of a Hue Server


        :param hue_server_url: The hue_server_url of this ClusterDetails.
        :type: str
        """
        self._hue_server_url = hue_server_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
