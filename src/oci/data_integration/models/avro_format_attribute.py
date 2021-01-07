# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_format_attribute import AbstractFormatAttribute
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvroFormatAttribute(AbstractFormatAttribute):
    """
    The AVRO format attribute.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AvroFormatAttribute object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.AvroFormatAttribute.model_type` attribute
        of this class is ``AVRO_FORMAT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this AvroFormatAttribute.
            Allowed values for this property are: "JSON_FORMAT", "CSV_FORMAT", "AVRO_FORMAT"
        :type model_type: str

        :param compression:
            The value to assign to the compression property of this AvroFormatAttribute.
        :type compression: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'compression': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'compression': 'compression'
        }

        self._model_type = None
        self._compression = None
        self._model_type = 'AVRO_FORMAT'

    @property
    def compression(self):
        """
        Gets the compression of this AvroFormatAttribute.
        The compression for the file.


        :return: The compression of this AvroFormatAttribute.
        :rtype: str
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """
        Sets the compression of this AvroFormatAttribute.
        The compression for the file.


        :param compression: The compression of this AvroFormatAttribute.
        :type: str
        """
        self._compression = compression

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
