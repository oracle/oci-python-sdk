# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationAutotunePolicy(object):
    """
    An autotune policy automatically tunes the volume's performace based on the type of the policy.
    """

    #: A constant which can be used with the autotune_type property of a InstanceConfigurationAutotunePolicy.
    #: This constant has a value of "DETACHED_VOLUME"
    AUTOTUNE_TYPE_DETACHED_VOLUME = "DETACHED_VOLUME"

    #: A constant which can be used with the autotune_type property of a InstanceConfigurationAutotunePolicy.
    #: This constant has a value of "PERFORMANCE_BASED"
    AUTOTUNE_TYPE_PERFORMANCE_BASED = "PERFORMANCE_BASED"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationAutotunePolicy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.InstanceConfigurationPerformanceBasedAutotunePolicy`
        * :class:`~oci.core.models.InstanceConfigurationDetachedVolumeAutotunePolicy`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param autotune_type:
            The value to assign to the autotune_type property of this InstanceConfigurationAutotunePolicy.
            Allowed values for this property are: "DETACHED_VOLUME", "PERFORMANCE_BASED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type autotune_type: str

        """
        self.swagger_types = {
            'autotune_type': 'str'
        }

        self.attribute_map = {
            'autotune_type': 'autotuneType'
        }

        self._autotune_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['autotuneType']

        if type == 'PERFORMANCE_BASED':
            return 'InstanceConfigurationPerformanceBasedAutotunePolicy'

        if type == 'DETACHED_VOLUME':
            return 'InstanceConfigurationDetachedVolumeAutotunePolicy'
        else:
            return 'InstanceConfigurationAutotunePolicy'

    @property
    def autotune_type(self):
        """
        **[Required]** Gets the autotune_type of this InstanceConfigurationAutotunePolicy.
        This specifies the type of autotunes supported by OCI.

        Allowed values for this property are: "DETACHED_VOLUME", "PERFORMANCE_BASED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The autotune_type of this InstanceConfigurationAutotunePolicy.
        :rtype: str
        """
        return self._autotune_type

    @autotune_type.setter
    def autotune_type(self, autotune_type):
        """
        Sets the autotune_type of this InstanceConfigurationAutotunePolicy.
        This specifies the type of autotunes supported by OCI.


        :param autotune_type: The autotune_type of this InstanceConfigurationAutotunePolicy.
        :type: str
        """
        allowed_values = ["DETACHED_VOLUME", "PERFORMANCE_BASED"]
        if not value_allowed_none_or_none_sentinel(autotune_type, allowed_values):
            autotune_type = 'UNKNOWN_ENUM_VALUE'
        self._autotune_type = autotune_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
