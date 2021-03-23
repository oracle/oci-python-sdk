# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchInstancePlatformConfig(object):
    """
    The platform configuration requested for the instance.

    If you provide the parameter, the instance is created with the platform configuration that you specify.
    For any values that you omit, the instance uses the default configuration values for the `shape` that you
    specify. If you don't provide the parameter, the default values for the `shape` are used.

    Each shape only supports certain configurable values. If the values that you provide are not valid for the
    specified `shape`, an error is returned.
    """

    #: A constant which can be used with the type property of a LaunchInstancePlatformConfig.
    #: This constant has a value of "AMD_MILAN_BM"
    TYPE_AMD_MILAN_BM = "AMD_MILAN_BM"

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchInstancePlatformConfig object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.AmdMilanBmLaunchInstancePlatformConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this LaunchInstancePlatformConfig.
            Allowed values for this property are: "AMD_MILAN_BM"
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'AMD_MILAN_BM':
            return 'AmdMilanBmLaunchInstancePlatformConfig'
        else:
            return 'LaunchInstancePlatformConfig'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this LaunchInstancePlatformConfig.
        The type of platform being configured. The only supported
        `type` is `AMD_MILAN_BM`

        Allowed values for this property are: "AMD_MILAN_BM"


        :return: The type of this LaunchInstancePlatformConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LaunchInstancePlatformConfig.
        The type of platform being configured. The only supported
        `type` is `AMD_MILAN_BM`


        :param type: The type of this LaunchInstancePlatformConfig.
        :type: str
        """
        allowed_values = ["AMD_MILAN_BM"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
