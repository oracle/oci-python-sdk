# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectionFromHdfs(CreateConnectionDetails):
    """
    The details to create the HDFS data asset connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectionFromHdfs object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CreateConnectionFromHdfs.model_type` attribute
        of this class is ``HDFS_CONNECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateConnectionFromHdfs.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", "BIP_CONNECTION", "LAKE_CONNECTION", "ORACLE_PEOPLESOFT_CONNECTION", "ORACLE_EBS_CONNECTION", "ORACLE_SIEBEL_CONNECTION", "HDFS_CONNECTION", "MYSQL_HEATWAVE_CONNECTION", "REST_NO_AUTH_CONNECTION", "REST_BASIC_AUTH_CONNECTION", "OAUTH2_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateConnectionFromHdfs.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateConnectionFromHdfs.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateConnectionFromHdfs.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateConnectionFromHdfs.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateConnectionFromHdfs.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateConnectionFromHdfs.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateConnectionFromHdfs.
        :type identifier: str

        :param connection_properties:
            The value to assign to the connection_properties property of this CreateConnectionFromHdfs.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateConnectionFromHdfs.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param hdfs_principal:
            The value to assign to the hdfs_principal property of this CreateConnectionFromHdfs.
        :type hdfs_principal: str

        :param data_node_principal:
            The value to assign to the data_node_principal property of this CreateConnectionFromHdfs.
        :type data_node_principal: str

        :param name_node_principal:
            The value to assign to the name_node_principal property of this CreateConnectionFromHdfs.
        :type name_node_principal: str

        :param realm:
            The value to assign to the realm property of this CreateConnectionFromHdfs.
        :type realm: str

        :param key_distribution_center:
            The value to assign to the key_distribution_center property of this CreateConnectionFromHdfs.
        :type key_distribution_center: str

        :param key_tab_content:
            The value to assign to the key_tab_content property of this CreateConnectionFromHdfs.
        :type key_tab_content: oci.data_integration.models.SensitiveAttribute

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'connection_properties': 'list[ConnectionProperty]',
            'registry_metadata': 'RegistryMetadata',
            'hdfs_principal': 'str',
            'data_node_principal': 'str',
            'name_node_principal': 'str',
            'realm': 'str',
            'key_distribution_center': 'str',
            'key_tab_content': 'SensitiveAttribute'
        }
        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'connection_properties': 'connectionProperties',
            'registry_metadata': 'registryMetadata',
            'hdfs_principal': 'hdfsPrincipal',
            'data_node_principal': 'dataNodePrincipal',
            'name_node_principal': 'nameNodePrincipal',
            'realm': 'realm',
            'key_distribution_center': 'keyDistributionCenter',
            'key_tab_content': 'keyTabContent'
        }
        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._connection_properties = None
        self._registry_metadata = None
        self._hdfs_principal = None
        self._data_node_principal = None
        self._name_node_principal = None
        self._realm = None
        self._key_distribution_center = None
        self._key_tab_content = None
        self._model_type = 'HDFS_CONNECTION'

    @property
    def hdfs_principal(self):
        """
        **[Required]** Gets the hdfs_principal of this CreateConnectionFromHdfs.
        The HDFS principal.


        :return: The hdfs_principal of this CreateConnectionFromHdfs.
        :rtype: str
        """
        return self._hdfs_principal

    @hdfs_principal.setter
    def hdfs_principal(self, hdfs_principal):
        """
        Sets the hdfs_principal of this CreateConnectionFromHdfs.
        The HDFS principal.


        :param hdfs_principal: The hdfs_principal of this CreateConnectionFromHdfs.
        :type: str
        """
        self._hdfs_principal = hdfs_principal

    @property
    def data_node_principal(self):
        """
        **[Required]** Gets the data_node_principal of this CreateConnectionFromHdfs.
        The HDFS Data Node principal.


        :return: The data_node_principal of this CreateConnectionFromHdfs.
        :rtype: str
        """
        return self._data_node_principal

    @data_node_principal.setter
    def data_node_principal(self, data_node_principal):
        """
        Sets the data_node_principal of this CreateConnectionFromHdfs.
        The HDFS Data Node principal.


        :param data_node_principal: The data_node_principal of this CreateConnectionFromHdfs.
        :type: str
        """
        self._data_node_principal = data_node_principal

    @property
    def name_node_principal(self):
        """
        **[Required]** Gets the name_node_principal of this CreateConnectionFromHdfs.
        The HDFS Name Node principal.


        :return: The name_node_principal of this CreateConnectionFromHdfs.
        :rtype: str
        """
        return self._name_node_principal

    @name_node_principal.setter
    def name_node_principal(self, name_node_principal):
        """
        Sets the name_node_principal of this CreateConnectionFromHdfs.
        The HDFS Name Node principal.


        :param name_node_principal: The name_node_principal of this CreateConnectionFromHdfs.
        :type: str
        """
        self._name_node_principal = name_node_principal

    @property
    def realm(self):
        """
        Gets the realm of this CreateConnectionFromHdfs.
        HDFS Realm name.


        :return: The realm of this CreateConnectionFromHdfs.
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """
        Sets the realm of this CreateConnectionFromHdfs.
        HDFS Realm name.


        :param realm: The realm of this CreateConnectionFromHdfs.
        :type: str
        """
        self._realm = realm

    @property
    def key_distribution_center(self):
        """
        Gets the key_distribution_center of this CreateConnectionFromHdfs.
        The HDFS Key Distribution Center.


        :return: The key_distribution_center of this CreateConnectionFromHdfs.
        :rtype: str
        """
        return self._key_distribution_center

    @key_distribution_center.setter
    def key_distribution_center(self, key_distribution_center):
        """
        Sets the key_distribution_center of this CreateConnectionFromHdfs.
        The HDFS Key Distribution Center.


        :param key_distribution_center: The key_distribution_center of this CreateConnectionFromHdfs.
        :type: str
        """
        self._key_distribution_center = key_distribution_center

    @property
    def key_tab_content(self):
        """
        Gets the key_tab_content of this CreateConnectionFromHdfs.

        :return: The key_tab_content of this CreateConnectionFromHdfs.
        :rtype: oci.data_integration.models.SensitiveAttribute
        """
        return self._key_tab_content

    @key_tab_content.setter
    def key_tab_content(self, key_tab_content):
        """
        Sets the key_tab_content of this CreateConnectionFromHdfs.

        :param key_tab_content: The key_tab_content of this CreateConnectionFromHdfs.
        :type: oci.data_integration.models.SensitiveAttribute
        """
        self._key_tab_content = key_tab_content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
