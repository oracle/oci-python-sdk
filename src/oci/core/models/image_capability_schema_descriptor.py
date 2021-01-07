# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageCapabilitySchemaDescriptor(object):
    """
    Image Capability Schema Descriptor is a type of capability for an image.
    """

    #: A constant which can be used with the source property of a ImageCapabilitySchemaDescriptor.
    #: This constant has a value of "GLOBAL"
    SOURCE_GLOBAL = "GLOBAL"

    #: A constant which can be used with the source property of a ImageCapabilitySchemaDescriptor.
    #: This constant has a value of "IMAGE"
    SOURCE_IMAGE = "IMAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new ImageCapabilitySchemaDescriptor object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.EnumStringImageCapabilitySchemaDescriptor`
        * :class:`~oci.core.models.EnumIntegerImageCapabilityDescriptor`
        * :class:`~oci.core.models.BooleanImageCapabilitySchemaDescriptor`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param descriptor_type:
            The value to assign to the descriptor_type property of this ImageCapabilitySchemaDescriptor.
        :type descriptor_type: str

        :param source:
            The value to assign to the source property of this ImageCapabilitySchemaDescriptor.
            Allowed values for this property are: "GLOBAL", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source: str

        """
        self.swagger_types = {
            'descriptor_type': 'str',
            'source': 'str'
        }

        self.attribute_map = {
            'descriptor_type': 'descriptorType',
            'source': 'source'
        }

        self._descriptor_type = None
        self._source = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['descriptorType']

        if type == 'enumstring':
            return 'EnumStringImageCapabilitySchemaDescriptor'

        if type == 'enuminteger':
            return 'EnumIntegerImageCapabilityDescriptor'

        if type == 'boolean':
            return 'BooleanImageCapabilitySchemaDescriptor'
        else:
            return 'ImageCapabilitySchemaDescriptor'

    @property
    def descriptor_type(self):
        """
        **[Required]** Gets the descriptor_type of this ImageCapabilitySchemaDescriptor.
        The image capability schema descriptor type for the capability


        :return: The descriptor_type of this ImageCapabilitySchemaDescriptor.
        :rtype: str
        """
        return self._descriptor_type

    @descriptor_type.setter
    def descriptor_type(self, descriptor_type):
        """
        Sets the descriptor_type of this ImageCapabilitySchemaDescriptor.
        The image capability schema descriptor type for the capability


        :param descriptor_type: The descriptor_type of this ImageCapabilitySchemaDescriptor.
        :type: str
        """
        self._descriptor_type = descriptor_type

    @property
    def source(self):
        """
        **[Required]** Gets the source of this ImageCapabilitySchemaDescriptor.
        Allowed values for this property are: "GLOBAL", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source of this ImageCapabilitySchemaDescriptor.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this ImageCapabilitySchemaDescriptor.

        :param source: The source of this ImageCapabilitySchemaDescriptor.
        :type: str
        """
        allowed_values = ["GLOBAL", "IMAGE"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            source = 'UNKNOWN_ENUM_VALUE'
        self._source = source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
