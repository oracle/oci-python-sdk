# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TermAssociatedObject(object):
    """
    Projection of an object that is tagged to a term.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TermAssociatedObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TermAssociatedObject.
        :type key: str

        :param name:
            The value to assign to the name property of this TermAssociatedObject.
        :type name: str

        :param uri:
            The value to assign to the uri property of this TermAssociatedObject.
        :type uri: str

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'uri': 'uri'
        }

        self._key = None
        self._name = None
        self._uri = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this TermAssociatedObject.
        Immutable key used to uniquely identify the associated object.


        :return: The key of this TermAssociatedObject.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TermAssociatedObject.
        Immutable key used to uniquely identify the associated object.


        :param key: The key of this TermAssociatedObject.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this TermAssociatedObject.
        Name of the associated object.


        :return: The name of this TermAssociatedObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TermAssociatedObject.
        Name of the associated object.


        :param name: The name of this TermAssociatedObject.
        :type: str
        """
        self._name = name

    @property
    def uri(self):
        """
        Gets the uri of this TermAssociatedObject.
        URI of the associated object within the data catalog API.


        :return: The uri of this TermAssociatedObject.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this TermAssociatedObject.
        URI of the associated object within the data catalog API.


        :param uri: The uri of this TermAssociatedObject.
        :type: str
        """
        self._uri = uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
