# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CallOperationConfig(object):
    """
    Holder for parameters names.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CallOperationConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param in_fields:
            The value to assign to the in_fields property of this CallOperationConfig.
        :type in_fields: list[str]

        :param out_fields:
            The value to assign to the out_fields property of this CallOperationConfig.
        :type out_fields: list[str]

        :param call_attribute:
            The value to assign to the call_attribute property of this CallOperationConfig.
        :type call_attribute: oci.data_connectivity.models.AbstractCallAttribute

        :param push_down_operations:
            The value to assign to the push_down_operations property of this CallOperationConfig.
        :type push_down_operations: list[oci.data_connectivity.models.PushDownOperation]

        """
        self.swagger_types = {
            'in_fields': 'list[str]',
            'out_fields': 'list[str]',
            'call_attribute': 'AbstractCallAttribute',
            'push_down_operations': 'list[PushDownOperation]'
        }

        self.attribute_map = {
            'in_fields': 'inFields',
            'out_fields': 'outFields',
            'call_attribute': 'callAttribute',
            'push_down_operations': 'pushDownOperations'
        }

        self._in_fields = None
        self._out_fields = None
        self._call_attribute = None
        self._push_down_operations = None

    @property
    def in_fields(self):
        """
        Gets the in_fields of this CallOperationConfig.
        List of names of IN/INOUT parameters.


        :return: The in_fields of this CallOperationConfig.
        :rtype: list[str]
        """
        return self._in_fields

    @in_fields.setter
    def in_fields(self, in_fields):
        """
        Sets the in_fields of this CallOperationConfig.
        List of names of IN/INOUT parameters.


        :param in_fields: The in_fields of this CallOperationConfig.
        :type: list[str]
        """
        self._in_fields = in_fields

    @property
    def out_fields(self):
        """
        Gets the out_fields of this CallOperationConfig.
        List of names of OUT/INOUT parameters.


        :return: The out_fields of this CallOperationConfig.
        :rtype: list[str]
        """
        return self._out_fields

    @out_fields.setter
    def out_fields(self, out_fields):
        """
        Sets the out_fields of this CallOperationConfig.
        List of names of OUT/INOUT parameters.


        :param out_fields: The out_fields of this CallOperationConfig.
        :type: list[str]
        """
        self._out_fields = out_fields

    @property
    def call_attribute(self):
        """
        Gets the call_attribute of this CallOperationConfig.

        :return: The call_attribute of this CallOperationConfig.
        :rtype: oci.data_connectivity.models.AbstractCallAttribute
        """
        return self._call_attribute

    @call_attribute.setter
    def call_attribute(self, call_attribute):
        """
        Sets the call_attribute of this CallOperationConfig.

        :param call_attribute: The call_attribute of this CallOperationConfig.
        :type: oci.data_connectivity.models.AbstractCallAttribute
        """
        self._call_attribute = call_attribute

    @property
    def push_down_operations(self):
        """
        Gets the push_down_operations of this CallOperationConfig.
        List of push down operations.


        :return: The push_down_operations of this CallOperationConfig.
        :rtype: list[oci.data_connectivity.models.PushDownOperation]
        """
        return self._push_down_operations

    @push_down_operations.setter
    def push_down_operations(self, push_down_operations):
        """
        Sets the push_down_operations of this CallOperationConfig.
        List of push down operations.


        :param push_down_operations: The push_down_operations of this CallOperationConfig.
        :type: list[oci.data_connectivity.models.PushDownOperation]
        """
        self._push_down_operations = push_down_operations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
