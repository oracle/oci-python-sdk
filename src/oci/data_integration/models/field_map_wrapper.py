# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FieldMapWrapper(object):
    """
    A wrapper for a field map.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FieldMapWrapper object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field_map:
            The value to assign to the field_map property of this FieldMapWrapper.
        :type field_map: oci.data_integration.models.FieldMap

        """
        self.swagger_types = {
            'field_map': 'FieldMap'
        }

        self.attribute_map = {
            'field_map': 'fieldMap'
        }

        self._field_map = None

    @property
    def field_map(self):
        """
        Gets the field_map of this FieldMapWrapper.

        :return: The field_map of this FieldMapWrapper.
        :rtype: oci.data_integration.models.FieldMap
        """
        return self._field_map

    @field_map.setter
    def field_map(self, field_map):
        """
        Sets the field_map of this FieldMapWrapper.

        :param field_map: The field_map of this FieldMapWrapper.
        :type: oci.data_integration.models.FieldMap
        """
        self._field_map = field_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
