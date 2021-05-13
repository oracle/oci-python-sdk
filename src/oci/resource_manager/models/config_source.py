# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigSource(object):
    """
    Information about the Terraform configuration.
    """

    #: A constant which can be used with the config_source_type property of a ConfigSource.
    #: This constant has a value of "ZIP_UPLOAD"
    CONFIG_SOURCE_TYPE_ZIP_UPLOAD = "ZIP_UPLOAD"

    #: A constant which can be used with the config_source_type property of a ConfigSource.
    #: This constant has a value of "GIT_CONFIG_SOURCE"
    CONFIG_SOURCE_TYPE_GIT_CONFIG_SOURCE = "GIT_CONFIG_SOURCE"

    #: A constant which can be used with the config_source_type property of a ConfigSource.
    #: This constant has a value of "COMPARTMENT_CONFIG_SOURCE"
    CONFIG_SOURCE_TYPE_COMPARTMENT_CONFIG_SOURCE = "COMPARTMENT_CONFIG_SOURCE"

    #: A constant which can be used with the config_source_type property of a ConfigSource.
    #: This constant has a value of "OBJECT_STORAGE_CONFIG_SOURCE"
    CONFIG_SOURCE_TYPE_OBJECT_STORAGE_CONFIG_SOURCE = "OBJECT_STORAGE_CONFIG_SOURCE"

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigSource object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.resource_manager.models.GitConfigSource`
        * :class:`~oci.resource_manager.models.ObjectStorageConfigSource`
        * :class:`~oci.resource_manager.models.CompartmentConfigSource`
        * :class:`~oci.resource_manager.models.ZipUploadConfigSource`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_type:
            The value to assign to the config_source_type property of this ConfigSource.
            Allowed values for this property are: "ZIP_UPLOAD", "GIT_CONFIG_SOURCE", "COMPARTMENT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type config_source_type: str

        :param working_directory:
            The value to assign to the working_directory property of this ConfigSource.
        :type working_directory: str

        """
        self.swagger_types = {
            'config_source_type': 'str',
            'working_directory': 'str'
        }

        self.attribute_map = {
            'config_source_type': 'configSourceType',
            'working_directory': 'workingDirectory'
        }

        self._config_source_type = None
        self._working_directory = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['configSourceType']

        if type == 'GIT_CONFIG_SOURCE':
            return 'GitConfigSource'

        if type == 'OBJECT_STORAGE_CONFIG_SOURCE':
            return 'ObjectStorageConfigSource'

        if type == 'COMPARTMENT_CONFIG_SOURCE':
            return 'CompartmentConfigSource'

        if type == 'ZIP_UPLOAD':
            return 'ZipUploadConfigSource'
        else:
            return 'ConfigSource'

    @property
    def config_source_type(self):
        """
        **[Required]** Gets the config_source_type of this ConfigSource.
        The type of configuration source to use for the Terraform configuration.

        Allowed values for this property are: "ZIP_UPLOAD", "GIT_CONFIG_SOURCE", "COMPARTMENT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The config_source_type of this ConfigSource.
        :rtype: str
        """
        return self._config_source_type

    @config_source_type.setter
    def config_source_type(self, config_source_type):
        """
        Sets the config_source_type of this ConfigSource.
        The type of configuration source to use for the Terraform configuration.


        :param config_source_type: The config_source_type of this ConfigSource.
        :type: str
        """
        allowed_values = ["ZIP_UPLOAD", "GIT_CONFIG_SOURCE", "COMPARTMENT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE"]
        if not value_allowed_none_or_none_sentinel(config_source_type, allowed_values):
            config_source_type = 'UNKNOWN_ENUM_VALUE'
        self._config_source_type = config_source_type

    @property
    def working_directory(self):
        """
        Gets the working_directory of this ConfigSource.
        File path to the directory to use for running Terraform.
        If not specified, the root directory is used.
        This parameter is ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.


        :return: The working_directory of this ConfigSource.
        :rtype: str
        """
        return self._working_directory

    @working_directory.setter
    def working_directory(self, working_directory):
        """
        Sets the working_directory of this ConfigSource.
        File path to the directory to use for running Terraform.
        If not specified, the root directory is used.
        This parameter is ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.


        :param working_directory: The working_directory of this ConfigSource.
        :type: str
        """
        self._working_directory = working_directory

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
