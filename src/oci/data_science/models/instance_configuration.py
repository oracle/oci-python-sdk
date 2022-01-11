# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfiguration(object):
    """
    The model deployment instance configuration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_shape_name:
            The value to assign to the instance_shape_name property of this InstanceConfiguration.
        :type instance_shape_name: str

        """
        self.swagger_types = {
            'instance_shape_name': 'str'
        }

        self.attribute_map = {
            'instance_shape_name': 'instanceShapeName'
        }

        self._instance_shape_name = None

    @property
    def instance_shape_name(self):
        """
        **[Required]** Gets the instance_shape_name of this InstanceConfiguration.
        The shape used to launch the model deployment instances.


        :return: The instance_shape_name of this InstanceConfiguration.
        :rtype: str
        """
        return self._instance_shape_name

    @instance_shape_name.setter
    def instance_shape_name(self, instance_shape_name):
        """
        Sets the instance_shape_name of this InstanceConfiguration.
        The shape used to launch the model deployment instances.


        :param instance_shape_name: The instance_shape_name of this InstanceConfiguration.
        :type: str
        """
        self._instance_shape_name = instance_shape_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
