# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentServiceConfigurationDetails(object):
    """
    Top level Unified Agent service configuration object.
    """

    #: A constant which can be used with the configuration_type property of a UnifiedAgentServiceConfigurationDetails.
    #: This constant has a value of "LOGGING"
    CONFIGURATION_TYPE_LOGGING = "LOGGING"

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentServiceConfigurationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.logging.models.UnifiedAgentLoggingConfiguration`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param configuration_type:
            The value to assign to the configuration_type property of this UnifiedAgentServiceConfigurationDetails.
            Allowed values for this property are: "LOGGING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type configuration_type: str

        """
        self.swagger_types = {
            'configuration_type': 'str'
        }

        self.attribute_map = {
            'configuration_type': 'configurationType'
        }

        self._configuration_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['configurationType']

        if type == 'LOGGING':
            return 'UnifiedAgentLoggingConfiguration'
        else:
            return 'UnifiedAgentServiceConfigurationDetails'

    @property
    def configuration_type(self):
        """
        **[Required]** Gets the configuration_type of this UnifiedAgentServiceConfigurationDetails.
        Type of Unified Agent service configuration.

        Allowed values for this property are: "LOGGING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The configuration_type of this UnifiedAgentServiceConfigurationDetails.
        :rtype: str
        """
        return self._configuration_type

    @configuration_type.setter
    def configuration_type(self, configuration_type):
        """
        Sets the configuration_type of this UnifiedAgentServiceConfigurationDetails.
        Type of Unified Agent service configuration.


        :param configuration_type: The configuration_type of this UnifiedAgentServiceConfigurationDetails.
        :type: str
        """
        allowed_values = ["LOGGING"]
        if not value_allowed_none_or_none_sentinel(configuration_type, allowed_values):
            configuration_type = 'UNKNOWN_ENUM_VALUE'
        self._configuration_type = configuration_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
