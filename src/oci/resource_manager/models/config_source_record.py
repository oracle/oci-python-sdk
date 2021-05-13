# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigSourceRecord(object):
    """
    Information about the Terraform configuration.
    """

    #: A constant which can be used with the config_source_record_type property of a ConfigSourceRecord.
    #: This constant has a value of "ZIP_UPLOAD"
    CONFIG_SOURCE_RECORD_TYPE_ZIP_UPLOAD = "ZIP_UPLOAD"

    #: A constant which can be used with the config_source_record_type property of a ConfigSourceRecord.
    #: This constant has a value of "GIT_CONFIG_SOURCE"
    CONFIG_SOURCE_RECORD_TYPE_GIT_CONFIG_SOURCE = "GIT_CONFIG_SOURCE"

    #: A constant which can be used with the config_source_record_type property of a ConfigSourceRecord.
    #: This constant has a value of "OBJECT_STORAGE_CONFIG_SOURCE"
    CONFIG_SOURCE_RECORD_TYPE_OBJECT_STORAGE_CONFIG_SOURCE = "OBJECT_STORAGE_CONFIG_SOURCE"

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigSourceRecord object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.resource_manager.models.GitConfigSourceRecord`
        * :class:`~oci.resource_manager.models.ZipUploadConfigSourceRecord`
        * :class:`~oci.resource_manager.models.ObjectStorageConfigSourceRecord`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_record_type:
            The value to assign to the config_source_record_type property of this ConfigSourceRecord.
            Allowed values for this property are: "ZIP_UPLOAD", "GIT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type config_source_record_type: str

        """
        self.swagger_types = {
            'config_source_record_type': 'str'
        }

        self.attribute_map = {
            'config_source_record_type': 'configSourceRecordType'
        }

        self._config_source_record_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['configSourceRecordType']

        if type == 'GIT_CONFIG_SOURCE':
            return 'GitConfigSourceRecord'

        if type == 'ZIP_UPLOAD':
            return 'ZipUploadConfigSourceRecord'

        if type == 'OBJECT_STORAGE_CONFIG_SOURCE':
            return 'ObjectStorageConfigSourceRecord'
        else:
            return 'ConfigSourceRecord'

    @property
    def config_source_record_type(self):
        """
        **[Required]** Gets the config_source_record_type of this ConfigSourceRecord.
        The type of configuration source to use for the Terraform configuration.

        Allowed values for this property are: "ZIP_UPLOAD", "GIT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The config_source_record_type of this ConfigSourceRecord.
        :rtype: str
        """
        return self._config_source_record_type

    @config_source_record_type.setter
    def config_source_record_type(self, config_source_record_type):
        """
        Sets the config_source_record_type of this ConfigSourceRecord.
        The type of configuration source to use for the Terraform configuration.


        :param config_source_record_type: The config_source_record_type of this ConfigSourceRecord.
        :type: str
        """
        allowed_values = ["ZIP_UPLOAD", "GIT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE"]
        if not value_allowed_none_or_none_sentinel(config_source_record_type, allowed_values):
            config_source_record_type = 'UNKNOWN_ENUM_VALUE'
        self._config_source_record_type = config_source_record_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
