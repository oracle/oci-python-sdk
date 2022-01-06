# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationInstanceDetails(object):
    """
    InstanceConfigurationInstanceDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationInstanceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.ComputeInstanceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_type:
            The value to assign to the instance_type property of this InstanceConfigurationInstanceDetails.
        :type instance_type: str

        """
        self.swagger_types = {
            'instance_type': 'str'
        }

        self.attribute_map = {
            'instance_type': 'instanceType'
        }

        self._instance_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['instanceType']

        if type == 'compute':
            return 'ComputeInstanceDetails'
        else:
            return 'InstanceConfigurationInstanceDetails'

    @property
    def instance_type(self):
        """
        **[Required]** Gets the instance_type of this InstanceConfigurationInstanceDetails.
        The type of instance details. Supported instanceType is compute


        :return: The instance_type of this InstanceConfigurationInstanceDetails.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """
        Sets the instance_type of this InstanceConfigurationInstanceDetails.
        The type of instance details. Supported instanceType is compute


        :param instance_type: The instance_type of this InstanceConfigurationInstanceDetails.
        :type: str
        """
        self._instance_type = instance_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
