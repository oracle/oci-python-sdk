# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .image_capability_schema_descriptor import ImageCapabilitySchemaDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnumIntegerImageCapabilityDescriptor(ImageCapabilitySchemaDescriptor):
    """
    Enum Integer type CapabilityDescriptor
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnumIntegerImageCapabilityDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.EnumIntegerImageCapabilityDescriptor.descriptor_type` attribute
        of this class is ``enuminteger`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param descriptor_type:
            The value to assign to the descriptor_type property of this EnumIntegerImageCapabilityDescriptor.
        :type descriptor_type: str

        :param source:
            The value to assign to the source property of this EnumIntegerImageCapabilityDescriptor.
            Allowed values for this property are: "GLOBAL", "IMAGE"
        :type source: str

        :param values:
            The value to assign to the values property of this EnumIntegerImageCapabilityDescriptor.
        :type values: list[int]

        :param default_value:
            The value to assign to the default_value property of this EnumIntegerImageCapabilityDescriptor.
        :type default_value: int

        """
        self.swagger_types = {
            'descriptor_type': 'str',
            'source': 'str',
            'values': 'list[int]',
            'default_value': 'int'
        }

        self.attribute_map = {
            'descriptor_type': 'descriptorType',
            'source': 'source',
            'values': 'values',
            'default_value': 'defaultValue'
        }

        self._descriptor_type = None
        self._source = None
        self._values = None
        self._default_value = None
        self._descriptor_type = 'enuminteger'

    @property
    def values(self):
        """
        **[Required]** Gets the values of this EnumIntegerImageCapabilityDescriptor.
        the list of values for the enum


        :return: The values of this EnumIntegerImageCapabilityDescriptor.
        :rtype: list[int]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this EnumIntegerImageCapabilityDescriptor.
        the list of values for the enum


        :param values: The values of this EnumIntegerImageCapabilityDescriptor.
        :type: list[int]
        """
        self._values = values

    @property
    def default_value(self):
        """
        Gets the default_value of this EnumIntegerImageCapabilityDescriptor.
        the default value


        :return: The default_value of this EnumIntegerImageCapabilityDescriptor.
        :rtype: int
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this EnumIntegerImageCapabilityDescriptor.
        the default value


        :param default_value: The default_value of this EnumIntegerImageCapabilityDescriptor.
        :type: int
        """
        self._default_value = default_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
