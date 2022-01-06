# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_source_details import DataSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSourceDetailsInflux(DataSourceDetails):
    """
    Data Source details for influx.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataSourceDetailsInflux object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_anomaly_detection.models.DataSourceDetailsInflux.data_source_type` attribute
        of this class is ``INFLUX`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_source_type:
            The value to assign to the data_source_type property of this DataSourceDetailsInflux.
            Allowed values for this property are: "ORACLE_OBJECT_STORAGE", "ORACLE_ATP", "INFLUX"
        :type data_source_type: str

        :param version_specific_details:
            The value to assign to the version_specific_details property of this DataSourceDetailsInflux.
        :type version_specific_details: oci.ai_anomaly_detection.models.InfluxDetails

        :param user_name:
            The value to assign to the user_name property of this DataSourceDetailsInflux.
        :type user_name: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this DataSourceDetailsInflux.
        :type password_secret_id: str

        :param measurement_name:
            The value to assign to the measurement_name property of this DataSourceDetailsInflux.
        :type measurement_name: str

        :param url:
            The value to assign to the url property of this DataSourceDetailsInflux.
        :type url: str

        """
        self.swagger_types = {
            'data_source_type': 'str',
            'version_specific_details': 'InfluxDetails',
            'user_name': 'str',
            'password_secret_id': 'str',
            'measurement_name': 'str',
            'url': 'str'
        }

        self.attribute_map = {
            'data_source_type': 'dataSourceType',
            'version_specific_details': 'versionSpecificDetails',
            'user_name': 'userName',
            'password_secret_id': 'passwordSecretId',
            'measurement_name': 'measurementName',
            'url': 'url'
        }

        self._data_source_type = None
        self._version_specific_details = None
        self._user_name = None
        self._password_secret_id = None
        self._measurement_name = None
        self._url = None
        self._data_source_type = 'INFLUX'

    @property
    def version_specific_details(self):
        """
        **[Required]** Gets the version_specific_details of this DataSourceDetailsInflux.

        :return: The version_specific_details of this DataSourceDetailsInflux.
        :rtype: oci.ai_anomaly_detection.models.InfluxDetails
        """
        return self._version_specific_details

    @version_specific_details.setter
    def version_specific_details(self, version_specific_details):
        """
        Sets the version_specific_details of this DataSourceDetailsInflux.

        :param version_specific_details: The version_specific_details of this DataSourceDetailsInflux.
        :type: oci.ai_anomaly_detection.models.InfluxDetails
        """
        self._version_specific_details = version_specific_details

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this DataSourceDetailsInflux.
        Username for connection to Influx


        :return: The user_name of this DataSourceDetailsInflux.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this DataSourceDetailsInflux.
        Username for connection to Influx


        :param user_name: The user_name of this DataSourceDetailsInflux.
        :type: str
        """
        self._user_name = user_name

    @property
    def password_secret_id(self):
        """
        **[Required]** Gets the password_secret_id of this DataSourceDetailsInflux.
        Password Secret Id for the influx connection


        :return: The password_secret_id of this DataSourceDetailsInflux.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this DataSourceDetailsInflux.
        Password Secret Id for the influx connection


        :param password_secret_id: The password_secret_id of this DataSourceDetailsInflux.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def measurement_name(self):
        """
        **[Required]** Gets the measurement_name of this DataSourceDetailsInflux.
        Measurement name for influx


        :return: The measurement_name of this DataSourceDetailsInflux.
        :rtype: str
        """
        return self._measurement_name

    @measurement_name.setter
    def measurement_name(self, measurement_name):
        """
        Sets the measurement_name of this DataSourceDetailsInflux.
        Measurement name for influx


        :param measurement_name: The measurement_name of this DataSourceDetailsInflux.
        :type: str
        """
        self._measurement_name = measurement_name

    @property
    def url(self):
        """
        **[Required]** Gets the url of this DataSourceDetailsInflux.
        public IP address and port to influx DB


        :return: The url of this DataSourceDetailsInflux.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this DataSourceDetailsInflux.
        public IP address and port to influx DB


        :param url: The url of this DataSourceDetailsInflux.
        :type: str
        """
        self._url = url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
