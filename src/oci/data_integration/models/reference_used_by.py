# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReferenceUsedBy(object):
    """
    Referenced object information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReferenceUsedBy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ReferenceUsedBy.
        :type key: str

        :param name:
            The value to assign to the name property of this ReferenceUsedBy.
        :type name: str

        :param name_path:
            The value to assign to the name_path property of this ReferenceUsedBy.
        :type name_path: str

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'name_path': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'name_path': 'namePath'
        }

        self._key = None
        self._name = None
        self._name_path = None

    @property
    def key(self):
        """
        Gets the key of this ReferenceUsedBy.
        The key of the published object.


        :return: The key of this ReferenceUsedBy.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ReferenceUsedBy.
        The key of the published object.


        :param key: The key of this ReferenceUsedBy.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this ReferenceUsedBy.
        The name of an published object.


        :return: The name of this ReferenceUsedBy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReferenceUsedBy.
        The name of an published object.


        :param name: The name of this ReferenceUsedBy.
        :type: str
        """
        self._name = name

    @property
    def name_path(self):
        """
        Gets the name_path of this ReferenceUsedBy.
        The name path of the published object.


        :return: The name_path of this ReferenceUsedBy.
        :rtype: str
        """
        return self._name_path

    @name_path.setter
    def name_path(self, name_path):
        """
        Sets the name_path of this ReferenceUsedBy.
        The name path of the published object.


        :param name_path: The name_path of this ReferenceUsedBy.
        :type: str
        """
        self._name_path = name_path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
