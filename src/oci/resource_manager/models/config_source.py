# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigSource(object):
    """
    Location of the zip file that contains the Terraform configuration.
    """

    #: A constant which can be used with the config_source_type property of a ConfigSource.
    #: This constant has a value of "ZIP_UPLOAD"
    CONFIG_SOURCE_TYPE_ZIP_UPLOAD = "ZIP_UPLOAD"

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigSource object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.resource_manager.models.ZipUploadConfigSource`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_type:
            The value to assign to the config_source_type property of this ConfigSource.
            Allowed values for this property are: "ZIP_UPLOAD", 'UNKNOWN_ENUM_VALUE'.
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

        if type == 'ZIP_UPLOAD':
            return 'ZipUploadConfigSource'
        else:
            return 'ConfigSource'

    @property
    def config_source_type(self):
        """
        **[Required]** Gets the config_source_type of this ConfigSource.
        The configuration file type.

        Allowed values for this property are: "ZIP_UPLOAD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The config_source_type of this ConfigSource.
        :rtype: str
        """
        return self._config_source_type

    @config_source_type.setter
    def config_source_type(self, config_source_type):
        """
        Sets the config_source_type of this ConfigSource.
        The configuration file type.


        :param config_source_type: The config_source_type of this ConfigSource.
        :type: str
        """
        allowed_values = ["ZIP_UPLOAD"]
        if not value_allowed_none_or_none_sentinel(config_source_type, allowed_values):
            config_source_type = 'UNKNOWN_ENUM_VALUE'
        self._config_source_type = config_source_type

    @property
    def working_directory(self):
        """
        Gets the working_directory of this ConfigSource.
        File path to the directory from which Terraform runs.
        If not specified, we use the root directory.


        :return: The working_directory of this ConfigSource.
        :rtype: str
        """
        return self._working_directory

    @working_directory.setter
    def working_directory(self, working_directory):
        """
        Sets the working_directory of this ConfigSource.
        File path to the directory from which Terraform runs.
        If not specified, we use the root directory.


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
