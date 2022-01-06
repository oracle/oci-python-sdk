# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RepositoryObject(object):
    """
    Object containing information about files and directories in a repository.
    """

    #: A constant which can be used with the type property of a RepositoryObject.
    #: This constant has a value of "BLOB"
    TYPE_BLOB = "BLOB"

    #: A constant which can be used with the type property of a RepositoryObject.
    #: This constant has a value of "TREE"
    TYPE_TREE = "TREE"

    #: A constant which can be used with the type property of a RepositoryObject.
    #: This constant has a value of "COMMIT"
    TYPE_COMMIT = "COMMIT"

    def __init__(self, **kwargs):
        """
        Initializes a new RepositoryObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this RepositoryObject.
            Allowed values for this property are: "BLOB", "TREE", "COMMIT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this RepositoryObject.
        :type size_in_bytes: int

        :param sha:
            The value to assign to the sha property of this RepositoryObject.
        :type sha: str

        :param is_binary:
            The value to assign to the is_binary property of this RepositoryObject.
        :type is_binary: bool

        """
        self.swagger_types = {
            'type': 'str',
            'size_in_bytes': 'int',
            'sha': 'str',
            'is_binary': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'size_in_bytes': 'sizeInBytes',
            'sha': 'sha',
            'is_binary': 'isBinary'
        }

        self._type = None
        self._size_in_bytes = None
        self._sha = None
        self._is_binary = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this RepositoryObject.
        The type of git object.

        Allowed values for this property are: "BLOB", "TREE", "COMMIT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this RepositoryObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RepositoryObject.
        The type of git object.


        :param type: The type of this RepositoryObject.
        :type: str
        """
        allowed_values = ["BLOB", "TREE", "COMMIT"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def size_in_bytes(self):
        """
        **[Required]** Gets the size_in_bytes of this RepositoryObject.
        Size in bytes.


        :return: The size_in_bytes of this RepositoryObject.
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this RepositoryObject.
        Size in bytes.


        :param size_in_bytes: The size_in_bytes of this RepositoryObject.
        :type: int
        """
        self._size_in_bytes = size_in_bytes

    @property
    def sha(self):
        """
        **[Required]** Gets the sha of this RepositoryObject.
        SHA-1 hash of git object.


        :return: The sha of this RepositoryObject.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """
        Sets the sha of this RepositoryObject.
        SHA-1 hash of git object.


        :param sha: The sha of this RepositoryObject.
        :type: str
        """
        self._sha = sha

    @property
    def is_binary(self):
        """
        Gets the is_binary of this RepositoryObject.
        Flag to determine if the object contains binary file content or not.


        :return: The is_binary of this RepositoryObject.
        :rtype: bool
        """
        return self._is_binary

    @is_binary.setter
    def is_binary(self, is_binary):
        """
        Sets the is_binary of this RepositoryObject.
        Flag to determine if the object contains binary file content or not.


        :param is_binary: The is_binary of this RepositoryObject.
        :type: bool
        """
        self._is_binary = is_binary

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
