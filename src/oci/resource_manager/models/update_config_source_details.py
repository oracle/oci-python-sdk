# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConfigSourceDetails(object):
    """
    Updates the property details for the configuration source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConfigSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.resource_manager.models.UpdateGitConfigSourceDetails`
        * :class:`~oci.resource_manager.models.UpdateZipUploadConfigSourceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_type:
            The value to assign to the config_source_type property of this UpdateConfigSourceDetails.
        :type config_source_type: str

        :param working_directory:
            The value to assign to the working_directory property of this UpdateConfigSourceDetails.
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
            return 'UpdateGitConfigSourceDetails'

        if type == 'ZIP_UPLOAD':
            return 'UpdateZipUploadConfigSourceDetails'
        else:
            return 'UpdateConfigSourceDetails'

    @property
    def config_source_type(self):
        """
        **[Required]** Gets the config_source_type of this UpdateConfigSourceDetails.
        Specifies the `configSourceType` for uploading the Terraform configuration.


        :return: The config_source_type of this UpdateConfigSourceDetails.
        :rtype: str
        """
        return self._config_source_type

    @config_source_type.setter
    def config_source_type(self, config_source_type):
        """
        Sets the config_source_type of this UpdateConfigSourceDetails.
        Specifies the `configSourceType` for uploading the Terraform configuration.


        :param config_source_type: The config_source_type of this UpdateConfigSourceDetails.
        :type: str
        """
        self._config_source_type = config_source_type

    @property
    def working_directory(self):
        """
        Gets the working_directory of this UpdateConfigSourceDetails.
        The path of the directory from which to run terraform. If not specified, the the root will be used. This parameter is ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.


        :return: The working_directory of this UpdateConfigSourceDetails.
        :rtype: str
        """
        return self._working_directory

    @working_directory.setter
    def working_directory(self, working_directory):
        """
        Sets the working_directory of this UpdateConfigSourceDetails.
        The path of the directory from which to run terraform. If not specified, the the root will be used. This parameter is ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.


        :param working_directory: The working_directory of this UpdateConfigSourceDetails.
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
