# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrimaryKey(object):
    """
    The primary key object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrimaryKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this PrimaryKey.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this PrimaryKey.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this PrimaryKey.
        :type parent_ref: ParentReference

        :param name:
            The value to assign to the name property of this PrimaryKey.
        :type name: str

        :param attribute_refs:
            The value to assign to the attribute_refs property of this PrimaryKey.
        :type attribute_refs: list[KeyAttribute]

        :param object_status:
            The value to assign to the object_status property of this PrimaryKey.
        :type object_status: int

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'attribute_refs': 'list[KeyAttribute]',
            'object_status': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'attribute_refs': 'attributeRefs',
            'object_status': 'objectStatus'
        }

        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._attribute_refs = None
        self._object_status = None

    @property
    def key(self):
        """
        Gets the key of this PrimaryKey.
        The key of the object.


        :return: The key of this PrimaryKey.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this PrimaryKey.
        The key of the object.


        :param key: The key of this PrimaryKey.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this PrimaryKey.
        The model version of an object.


        :return: The model_version of this PrimaryKey.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this PrimaryKey.
        The model version of an object.


        :param model_version: The model_version of this PrimaryKey.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this PrimaryKey.

        :return: The parent_ref of this PrimaryKey.
        :rtype: ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this PrimaryKey.

        :param parent_ref: The parent_ref of this PrimaryKey.
        :type: ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this PrimaryKey.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :return: The name of this PrimaryKey.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PrimaryKey.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :param name: The name of this PrimaryKey.
        :type: str
        """
        self._name = name

    @property
    def attribute_refs(self):
        """
        Gets the attribute_refs of this PrimaryKey.
        attributeRefs


        :return: The attribute_refs of this PrimaryKey.
        :rtype: list[KeyAttribute]
        """
        return self._attribute_refs

    @attribute_refs.setter
    def attribute_refs(self, attribute_refs):
        """
        Sets the attribute_refs of this PrimaryKey.
        attributeRefs


        :param attribute_refs: The attribute_refs of this PrimaryKey.
        :type: list[KeyAttribute]
        """
        self._attribute_refs = attribute_refs

    @property
    def object_status(self):
        """
        Gets the object_status of this PrimaryKey.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this PrimaryKey.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this PrimaryKey.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this PrimaryKey.
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
