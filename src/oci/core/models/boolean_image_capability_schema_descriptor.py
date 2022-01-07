# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .image_capability_schema_descriptor import ImageCapabilitySchemaDescriptor
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BooleanImageCapabilitySchemaDescriptor(ImageCapabilitySchemaDescriptor):
    """
    Boolean type ImageCapabilitySchemaDescriptor
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BooleanImageCapabilitySchemaDescriptor object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.BooleanImageCapabilitySchemaDescriptor.descriptor_type` attribute
        of this class is ``boolean`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param descriptor_type:
            The value to assign to the descriptor_type property of this BooleanImageCapabilitySchemaDescriptor.
        :type descriptor_type: str

        :param source:
            The value to assign to the source property of this BooleanImageCapabilitySchemaDescriptor.
            Allowed values for this property are: "GLOBAL", "IMAGE"
        :type source: str

        :param default_value:
            The value to assign to the default_value property of this BooleanImageCapabilitySchemaDescriptor.
        :type default_value: bool

        """
        self.swagger_types = {
            'descriptor_type': 'str',
            'source': 'str',
            'default_value': 'bool'
        }

        self.attribute_map = {
            'descriptor_type': 'descriptorType',
            'source': 'source',
            'default_value': 'defaultValue'
        }

        self._descriptor_type = None
        self._source = None
        self._default_value = None
        self._descriptor_type = 'boolean'

    @property
    def default_value(self):
        """
        Gets the default_value of this BooleanImageCapabilitySchemaDescriptor.
        the default value


        :return: The default_value of this BooleanImageCapabilitySchemaDescriptor.
        :rtype: bool
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this BooleanImageCapabilitySchemaDescriptor.
        the default value


        :param default_value: The default_value of this BooleanImageCapabilitySchemaDescriptor.
        :type: bool
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
