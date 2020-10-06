# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OracleAdwcWriteAttributes(object):
    """
    Properties to configure when writing to Oracle Autonomous Data Warehouse Cloud.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OracleAdwcWriteAttributes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bucket_name:
            The value to assign to the bucket_name property of this OracleAdwcWriteAttributes.
        :type bucket_name: str

        :param staging_file_name:
            The value to assign to the staging_file_name property of this OracleAdwcWriteAttributes.
        :type staging_file_name: str

        :param staging_data_asset:
            The value to assign to the staging_data_asset property of this OracleAdwcWriteAttributes.
        :type staging_data_asset: DataAsset

        :param staging_connection:
            The value to assign to the staging_connection property of this OracleAdwcWriteAttributes.
        :type staging_connection: Connection

        """
        self.swagger_types = {
            'bucket_name': 'str',
            'staging_file_name': 'str',
            'staging_data_asset': 'DataAsset',
            'staging_connection': 'Connection'
        }

        self.attribute_map = {
            'bucket_name': 'bucketName',
            'staging_file_name': 'stagingFileName',
            'staging_data_asset': 'stagingDataAsset',
            'staging_connection': 'stagingConnection'
        }

        self._bucket_name = None
        self._staging_file_name = None
        self._staging_data_asset = None
        self._staging_connection = None

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this OracleAdwcWriteAttributes.
        The bucket name for the attribute.


        :return: The bucket_name of this OracleAdwcWriteAttributes.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this OracleAdwcWriteAttributes.
        The bucket name for the attribute.


        :param bucket_name: The bucket_name of this OracleAdwcWriteAttributes.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def staging_file_name(self):
        """
        Gets the staging_file_name of this OracleAdwcWriteAttributes.
        The file name for the attribute.


        :return: The staging_file_name of this OracleAdwcWriteAttributes.
        :rtype: str
        """
        return self._staging_file_name

    @staging_file_name.setter
    def staging_file_name(self, staging_file_name):
        """
        Sets the staging_file_name of this OracleAdwcWriteAttributes.
        The file name for the attribute.


        :param staging_file_name: The staging_file_name of this OracleAdwcWriteAttributes.
        :type: str
        """
        self._staging_file_name = staging_file_name

    @property
    def staging_data_asset(self):
        """
        Gets the staging_data_asset of this OracleAdwcWriteAttributes.

        :return: The staging_data_asset of this OracleAdwcWriteAttributes.
        :rtype: DataAsset
        """
        return self._staging_data_asset

    @staging_data_asset.setter
    def staging_data_asset(self, staging_data_asset):
        """
        Sets the staging_data_asset of this OracleAdwcWriteAttributes.

        :param staging_data_asset: The staging_data_asset of this OracleAdwcWriteAttributes.
        :type: DataAsset
        """
        self._staging_data_asset = staging_data_asset

    @property
    def staging_connection(self):
        """
        Gets the staging_connection of this OracleAdwcWriteAttributes.

        :return: The staging_connection of this OracleAdwcWriteAttributes.
        :rtype: Connection
        """
        return self._staging_connection

    @staging_connection.setter
    def staging_connection(self, staging_connection):
        """
        Sets the staging_connection of this OracleAdwcWriteAttributes.

        :param staging_connection: The staging_connection of this OracleAdwcWriteAttributes.
        :type: Connection
        """
        self._staging_connection = staging_connection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
