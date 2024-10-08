# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSourceConfig(object):
    """
    **DataSourceConfig**

    The details of data source.
    """

    #: A constant which can be used with the data_source_config_type property of a DataSourceConfig.
    #: This constant has a value of "OCI_OBJECT_STORAGE"
    DATA_SOURCE_CONFIG_TYPE_OCI_OBJECT_STORAGE = "OCI_OBJECT_STORAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new DataSourceConfig object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai_agent.models.OciObjectStorageDataSourceConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_source_config_type:
            The value to assign to the data_source_config_type property of this DataSourceConfig.
            Allowed values for this property are: "OCI_OBJECT_STORAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_source_config_type: str

        """
        self.swagger_types = {
            'data_source_config_type': 'str'
        }

        self.attribute_map = {
            'data_source_config_type': 'dataSourceConfigType'
        }

        self._data_source_config_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['dataSourceConfigType']

        if type == 'OCI_OBJECT_STORAGE':
            return 'OciObjectStorageDataSourceConfig'
        else:
            return 'DataSourceConfig'

    @property
    def data_source_config_type(self):
        """
        **[Required]** Gets the data_source_config_type of this DataSourceConfig.
        The type of the tool.
        The allowed values are:
        - `OCI_OBJECT_STORAGE`: The data source is OCI Object Storage.

        Allowed values for this property are: "OCI_OBJECT_STORAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_source_config_type of this DataSourceConfig.
        :rtype: str
        """
        return self._data_source_config_type

    @data_source_config_type.setter
    def data_source_config_type(self, data_source_config_type):
        """
        Sets the data_source_config_type of this DataSourceConfig.
        The type of the tool.
        The allowed values are:
        - `OCI_OBJECT_STORAGE`: The data source is OCI Object Storage.


        :param data_source_config_type: The data_source_config_type of this DataSourceConfig.
        :type: str
        """
        allowed_values = ["OCI_OBJECT_STORAGE"]
        if not value_allowed_none_or_none_sentinel(data_source_config_type, allowed_values):
            data_source_config_type = 'UNKNOWN_ENUM_VALUE'
        self._data_source_config_type = data_source_config_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
