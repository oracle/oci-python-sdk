# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConnectionFromRestNoAuth(UpdateConnectionDetails):
    """
    The details to update a no auth rest connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConnectionFromRestNoAuth object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.UpdateConnectionFromRestNoAuth.model_type` attribute
        of this class is ``REST_NO_AUTH_CONNECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this UpdateConnectionFromRestNoAuth.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", "BIP_CONNECTION", "LAKE_HOUSE_CONNECTION", "REST_NO_AUTH_CONNECTION", "REST_BASIC_AUTH_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this UpdateConnectionFromRestNoAuth.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this UpdateConnectionFromRestNoAuth.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this UpdateConnectionFromRestNoAuth.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this UpdateConnectionFromRestNoAuth.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateConnectionFromRestNoAuth.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this UpdateConnectionFromRestNoAuth.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this UpdateConnectionFromRestNoAuth.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this UpdateConnectionFromRestNoAuth.
        :type identifier: str

        :param connection_properties:
            The value to assign to the connection_properties property of this UpdateConnectionFromRestNoAuth.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param registry_metadata:
            The value to assign to the registry_metadata property of this UpdateConnectionFromRestNoAuth.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'object_version': 'int',
            'identifier': 'str',
            'connection_properties': 'list[ConnectionProperty]',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'object_version': 'objectVersion',
            'identifier': 'identifier',
            'connection_properties': 'connectionProperties',
            'registry_metadata': 'registryMetadata'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_status = None
        self._object_version = None
        self._identifier = None
        self._connection_properties = None
        self._registry_metadata = None
        self._model_type = 'REST_NO_AUTH_CONNECTION'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
