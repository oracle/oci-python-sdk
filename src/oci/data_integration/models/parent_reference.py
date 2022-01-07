# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParentReference(object):
    """
    A reference to the object's parent.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ParentReference object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parent:
            The value to assign to the parent property of this ParentReference.
        :type parent: str

        :param root_doc_id:
            The value to assign to the root_doc_id property of this ParentReference.
        :type root_doc_id: str

        """
        self.swagger_types = {
            'parent': 'str',
            'root_doc_id': 'str'
        }

        self.attribute_map = {
            'parent': 'parent',
            'root_doc_id': 'rootDocId'
        }

        self._parent = None
        self._root_doc_id = None

    @property
    def parent(self):
        """
        Gets the parent of this ParentReference.
        Key of the parent object.


        :return: The parent of this ParentReference.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ParentReference.
        Key of the parent object.


        :param parent: The parent of this ParentReference.
        :type: str
        """
        self._parent = parent

    @property
    def root_doc_id(self):
        """
        Gets the root_doc_id of this ParentReference.
        Key of the root document object.


        :return: The root_doc_id of this ParentReference.
        :rtype: str
        """
        return self._root_doc_id

    @root_doc_id.setter
    def root_doc_id(self, root_doc_id):
        """
        Sets the root_doc_id of this ParentReference.
        Key of the root document object.


        :param root_doc_id: The root_doc_id of this ParentReference.
        :type: str
        """
        self._root_doc_id = root_doc_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
