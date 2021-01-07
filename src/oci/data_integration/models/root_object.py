# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RootObject(object):
    """
    A base class for all model types, including First Class and its contained objects.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RootObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this RootObject.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this RootObject.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this RootObject.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this RootObject.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param object_status:
            The value to assign to the object_status property of this RootObject.
        :type object_status: int

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'object_status': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'object_status': 'objectStatus'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._object_status = None

    @property
    def key(self):
        """
        Gets the key of this RootObject.
        The key of the object.


        :return: The key of this RootObject.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this RootObject.
        The key of the object.


        :param key: The key of this RootObject.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this RootObject.
        The type of the object.


        :return: The model_type of this RootObject.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this RootObject.
        The type of the object.


        :param model_type: The model_type of this RootObject.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this RootObject.
        The model version of an object.


        :return: The model_version of this RootObject.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this RootObject.
        The model version of an object.


        :param model_version: The model_version of this RootObject.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this RootObject.

        :return: The parent_ref of this RootObject.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this RootObject.

        :param parent_ref: The parent_ref of this RootObject.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def object_status(self):
        """
        Gets the object_status of this RootObject.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this RootObject.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this RootObject.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this RootObject.
        :type: int
        """
        self._object_status = object_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
