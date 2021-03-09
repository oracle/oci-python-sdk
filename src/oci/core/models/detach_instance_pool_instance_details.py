# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetachInstancePoolInstanceDetails(object):
    """
    Detach an instance from the pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetachInstancePoolInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_id:
            The value to assign to the instance_id property of this DetachInstancePoolInstanceDetails.
        :type instance_id: str

        :param is_decrement_size:
            The value to assign to the is_decrement_size property of this DetachInstancePoolInstanceDetails.
        :type is_decrement_size: bool

        :param is_auto_terminate:
            The value to assign to the is_auto_terminate property of this DetachInstancePoolInstanceDetails.
        :type is_auto_terminate: bool

        """
        self.swagger_types = {
            'instance_id': 'str',
            'is_decrement_size': 'bool',
            'is_auto_terminate': 'bool'
        }

        self.attribute_map = {
            'instance_id': 'instanceId',
            'is_decrement_size': 'isDecrementSize',
            'is_auto_terminate': 'isAutoTerminate'
        }

        self._instance_id = None
        self._is_decrement_size = None
        self._is_auto_terminate = None

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this DetachInstancePoolInstanceDetails.
        The instance ocid to detach.


        :return: The instance_id of this DetachInstancePoolInstanceDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this DetachInstancePoolInstanceDetails.
        The instance ocid to detach.


        :param instance_id: The instance_id of this DetachInstancePoolInstanceDetails.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def is_decrement_size(self):
        """
        Gets the is_decrement_size of this DetachInstancePoolInstanceDetails.
        Decrement the size of the instance pool during detachment.


        :return: The is_decrement_size of this DetachInstancePoolInstanceDetails.
        :rtype: bool
        """
        return self._is_decrement_size

    @is_decrement_size.setter
    def is_decrement_size(self, is_decrement_size):
        """
        Sets the is_decrement_size of this DetachInstancePoolInstanceDetails.
        Decrement the size of the instance pool during detachment.


        :param is_decrement_size: The is_decrement_size of this DetachInstancePoolInstanceDetails.
        :type: bool
        """
        self._is_decrement_size = is_decrement_size

    @property
    def is_auto_terminate(self):
        """
        Gets the is_auto_terminate of this DetachInstancePoolInstanceDetails.
        Terminate the instance after it has been detached.


        :return: The is_auto_terminate of this DetachInstancePoolInstanceDetails.
        :rtype: bool
        """
        return self._is_auto_terminate

    @is_auto_terminate.setter
    def is_auto_terminate(self, is_auto_terminate):
        """
        Sets the is_auto_terminate of this DetachInstancePoolInstanceDetails.
        Terminate the instance after it has been detached.


        :param is_auto_terminate: The is_auto_terminate of this DetachInstancePoolInstanceDetails.
        :type: bool
        """
        self._is_auto_terminate = is_auto_terminate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
