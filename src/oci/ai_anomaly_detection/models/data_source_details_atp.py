# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_source_details import DataSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSourceDetailsATP(DataSourceDetails):
    """
    Data Source details for ATP
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataSourceDetailsATP object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_anomaly_detection.models.DataSourceDetailsATP.data_source_type` attribute
        of this class is ``ORACLE_ATP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_source_type:
            The value to assign to the data_source_type property of this DataSourceDetailsATP.
            Allowed values for this property are: "ORACLE_OBJECT_STORAGE", "ORACLE_ATP", "INFLUX"
        :type data_source_type: str

        :param wallet_password_secret_id:
            The value to assign to the wallet_password_secret_id property of this DataSourceDetailsATP.
        :type wallet_password_secret_id: str

        :param atp_user_name:
            The value to assign to the atp_user_name property of this DataSourceDetailsATP.
        :type atp_user_name: str

        :param atp_password_secret_id:
            The value to assign to the atp_password_secret_id property of this DataSourceDetailsATP.
        :type atp_password_secret_id: str

        :param cwallet_file_secret_id:
            The value to assign to the cwallet_file_secret_id property of this DataSourceDetailsATP.
        :type cwallet_file_secret_id: str

        :param ewallet_file_secret_id:
            The value to assign to the ewallet_file_secret_id property of this DataSourceDetailsATP.
        :type ewallet_file_secret_id: str

        :param key_store_file_secret_id:
            The value to assign to the key_store_file_secret_id property of this DataSourceDetailsATP.
        :type key_store_file_secret_id: str

        :param ojdbc_file_secret_id:
            The value to assign to the ojdbc_file_secret_id property of this DataSourceDetailsATP.
        :type ojdbc_file_secret_id: str

        :param tnsnames_file_secret_id:
            The value to assign to the tnsnames_file_secret_id property of this DataSourceDetailsATP.
        :type tnsnames_file_secret_id: str

        :param truststore_file_secret_id:
            The value to assign to the truststore_file_secret_id property of this DataSourceDetailsATP.
        :type truststore_file_secret_id: str

        :param database_name:
            The value to assign to the database_name property of this DataSourceDetailsATP.
        :type database_name: str

        :param table_name:
            The value to assign to the table_name property of this DataSourceDetailsATP.
        :type table_name: str

        """
        self.swagger_types = {
            'data_source_type': 'str',
            'wallet_password_secret_id': 'str',
            'atp_user_name': 'str',
            'atp_password_secret_id': 'str',
            'cwallet_file_secret_id': 'str',
            'ewallet_file_secret_id': 'str',
            'key_store_file_secret_id': 'str',
            'ojdbc_file_secret_id': 'str',
            'tnsnames_file_secret_id': 'str',
            'truststore_file_secret_id': 'str',
            'database_name': 'str',
            'table_name': 'str'
        }

        self.attribute_map = {
            'data_source_type': 'dataSourceType',
            'wallet_password_secret_id': 'walletPasswordSecretId',
            'atp_user_name': 'atpUserName',
            'atp_password_secret_id': 'atpPasswordSecretId',
            'cwallet_file_secret_id': 'cwalletFileSecretId',
            'ewallet_file_secret_id': 'ewalletFileSecretId',
            'key_store_file_secret_id': 'keyStoreFileSecretId',
            'ojdbc_file_secret_id': 'ojdbcFileSecretId',
            'tnsnames_file_secret_id': 'tnsnamesFileSecretId',
            'truststore_file_secret_id': 'truststoreFileSecretId',
            'database_name': 'databaseName',
            'table_name': 'tableName'
        }

        self._data_source_type = None
        self._wallet_password_secret_id = None
        self._atp_user_name = None
        self._atp_password_secret_id = None
        self._cwallet_file_secret_id = None
        self._ewallet_file_secret_id = None
        self._key_store_file_secret_id = None
        self._ojdbc_file_secret_id = None
        self._tnsnames_file_secret_id = None
        self._truststore_file_secret_id = None
        self._database_name = None
        self._table_name = None
        self._data_source_type = 'ORACLE_ATP'

    @property
    def wallet_password_secret_id(self):
        """
        Gets the wallet_password_secret_id of this DataSourceDetailsATP.
        wallet password Secret ID in String format


        :return: The wallet_password_secret_id of this DataSourceDetailsATP.
        :rtype: str
        """
        return self._wallet_password_secret_id

    @wallet_password_secret_id.setter
    def wallet_password_secret_id(self, wallet_password_secret_id):
        """
        Sets the wallet_password_secret_id of this DataSourceDetailsATP.
        wallet password Secret ID in String format


        :param wallet_password_secret_id: The wallet_password_secret_id of this DataSourceDetailsATP.
        :type: str
        """
        self._wallet_password_secret_id = wallet_password_secret_id

    @property
    def atp_user_name(self):
        """
        Gets the atp_user_name of this DataSourceDetailsATP.
        atp db user name


        :return: The atp_user_name of this DataSourceDetailsATP.
        :rtype: str
        """
        return self._atp_user_name

    @atp_user_name.setter
    def atp_user_name(self, atp_user_name):
        """
        Sets the atp_user_name of this DataSourceDetailsATP.
        atp db user name


        :param atp_user_name: The atp_user_name of this DataSourceDetailsATP.
        :type: str
        """
        self._atp_user_name = atp_user_name

    @property
    def atp_password_secret_id(self):
        """
        Gets the atp_password_secret_id of this DataSourceDetailsATP.
        atp db password Secret Id


        :return: The atp_password_secret_id of this DataSourceDetailsATP.
        :rtype: str
        """
        return self._atp_password_secret_id

    @atp_password_secret_id.setter
    def atp_password_secret_id(self, atp_password_secret_id):
        """
        Sets the atp_password_secret_id of this DataSourceDetailsATP.
        atp db password Secret Id


        :param atp_password_secret_id: The atp_password_secret_id of this DataSourceDetailsATP.
        :type: str
        """
        self._atp_password_secret_id = atp_password_secret_id

    @property
    def cwallet_file_secret_id(self):
        """
        Gets the cwallet_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret containing the containers certificates of ATP wallet


        :return: The cwallet_file_secret_id of this DataSourceDetailsATP.
        :rtype: str
        """
        return self._cwallet_file_secret_id

    @cwallet_file_secret_id.setter
    def cwallet_file_secret_id(self, cwallet_file_secret_id):
        """
        Sets the cwallet_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret containing the containers certificates of ATP wallet


        :param cwallet_file_secret_id: The cwallet_file_secret_id of this DataSourceDetailsATP.
        :type: str
        """
        self._cwallet_file_secret_id = cwallet_file_secret_id

    @property
    def ewallet_file_secret_id(self):
        """
        Gets the ewallet_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret containing the PDB'S certificates of ATP wallet


        :return: The ewallet_file_secret_id of this DataSourceDetailsATP.
        :rtype: str
        """
        return self._ewallet_file_secret_id

    @ewallet_file_secret_id.setter
    def ewallet_file_secret_id(self, ewallet_file_secret_id):
        """
        Sets the ewallet_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret containing the PDB'S certificates of ATP wallet


        :param ewallet_file_secret_id: The ewallet_file_secret_id of this DataSourceDetailsATP.
        :type: str
        """
        self._ewallet_file_secret_id = ewallet_file_secret_id

    @property
    def key_store_file_secret_id(self):
        """
        Gets the key_store_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret containing Keystore.jks file of the ATP wallet


        :return: The key_store_file_secret_id of this DataSourceDetailsATP.
        :rtype: str
        """
        return self._key_store_file_secret_id

    @key_store_file_secret_id.setter
    def key_store_file_secret_id(self, key_store_file_secret_id):
        """
        Sets the key_store_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret containing Keystore.jks file of the ATP wallet


        :param key_store_file_secret_id: The key_store_file_secret_id of this DataSourceDetailsATP.
        :type: str
        """
        self._key_store_file_secret_id = key_store_file_secret_id

    @property
    def ojdbc_file_secret_id(self):
        """
        Gets the ojdbc_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret that contains jdbc properties file of ATP wallet


        :return: The ojdbc_file_secret_id of this DataSourceDetailsATP.
        :rtype: str
        """
        return self._ojdbc_file_secret_id

    @ojdbc_file_secret_id.setter
    def ojdbc_file_secret_id(self, ojdbc_file_secret_id):
        """
        Sets the ojdbc_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret that contains jdbc properties file of ATP wallet


        :param ojdbc_file_secret_id: The ojdbc_file_secret_id of this DataSourceDetailsATP.
        :type: str
        """
        self._ojdbc_file_secret_id = ojdbc_file_secret_id

    @property
    def tnsnames_file_secret_id(self):
        """
        Gets the tnsnames_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret that contains the tnsnames file of ATP wallet


        :return: The tnsnames_file_secret_id of this DataSourceDetailsATP.
        :rtype: str
        """
        return self._tnsnames_file_secret_id

    @tnsnames_file_secret_id.setter
    def tnsnames_file_secret_id(self, tnsnames_file_secret_id):
        """
        Sets the tnsnames_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret that contains the tnsnames file of ATP wallet


        :param tnsnames_file_secret_id: The tnsnames_file_secret_id of this DataSourceDetailsATP.
        :type: str
        """
        self._tnsnames_file_secret_id = tnsnames_file_secret_id

    @property
    def truststore_file_secret_id(self):
        """
        Gets the truststore_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret containing truststore.jks file of the ATP wallet


        :return: The truststore_file_secret_id of this DataSourceDetailsATP.
        :rtype: str
        """
        return self._truststore_file_secret_id

    @truststore_file_secret_id.setter
    def truststore_file_secret_id(self, truststore_file_secret_id):
        """
        Sets the truststore_file_secret_id of this DataSourceDetailsATP.
        OCID of the secret containing truststore.jks file of the ATP wallet


        :param truststore_file_secret_id: The truststore_file_secret_id of this DataSourceDetailsATP.
        :type: str
        """
        self._truststore_file_secret_id = truststore_file_secret_id

    @property
    def database_name(self):
        """
        Gets the database_name of this DataSourceDetailsATP.
        atp database name


        :return: The database_name of this DataSourceDetailsATP.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this DataSourceDetailsATP.
        atp database name


        :param database_name: The database_name of this DataSourceDetailsATP.
        :type: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """
        Gets the table_name of this DataSourceDetailsATP.
        atp database table name


        :return: The table_name of this DataSourceDetailsATP.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this DataSourceDetailsATP.
        atp database table name


        :param table_name: The table_name of this DataSourceDetailsATP.
        :type: str
        """
        self._table_name = table_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
