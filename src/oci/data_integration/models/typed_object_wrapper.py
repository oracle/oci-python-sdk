# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TypedObjectWrapper(object):
    """
    A wrapper for a typed object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TypedObjectWrapper object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param typed_object:
            The value to assign to the typed_object property of this TypedObjectWrapper.
        :type typed_object: oci.data_integration.models.TypedObject

        """
        self.swagger_types = {
            'typed_object': 'TypedObject'
        }

        self.attribute_map = {
            'typed_object': 'typedObject'
        }

        self._typed_object = None

    @property
    def typed_object(self):
        """
        Gets the typed_object of this TypedObjectWrapper.

        :return: The typed_object of this TypedObjectWrapper.
        :rtype: oci.data_integration.models.TypedObject
        """
        return self._typed_object

    @typed_object.setter
    def typed_object(self, typed_object):
        """
        Sets the typed_object of this TypedObjectWrapper.

        :param typed_object: The typed_object of this TypedObjectWrapper.
        :type: oci.data_integration.models.TypedObject
        """
        self._typed_object = typed_object

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
