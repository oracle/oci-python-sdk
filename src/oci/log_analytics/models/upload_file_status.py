# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UploadFileStatus(object):
    """
    Upload File Status
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UploadFileStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param file_name:
            The value to assign to the file_name property of this UploadFileStatus.
        :type file_name: str

        :param is_valid:
            The value to assign to the is_valid property of this UploadFileStatus.
        :type is_valid: bool

        """
        self.swagger_types = {
            'file_name': 'str',
            'is_valid': 'bool'
        }

        self.attribute_map = {
            'file_name': 'fileName',
            'is_valid': 'isValid'
        }

        self._file_name = None
        self._is_valid = None

    @property
    def file_name(self):
        """
        Gets the file_name of this UploadFileStatus.
        Name of the file.


        :return: The file_name of this UploadFileStatus.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this UploadFileStatus.
        Name of the file.


        :param file_name: The file_name of this UploadFileStatus.
        :type: str
        """
        self._file_name = file_name

    @property
    def is_valid(self):
        """
        Gets the is_valid of this UploadFileStatus.
        Is Valid flag.


        :return: The is_valid of this UploadFileStatus.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """
        Sets the is_valid of this UploadFileStatus.
        Is Valid flag.


        :param is_valid: The is_valid of this UploadFileStatus.
        :type: bool
        """
        self._is_valid = is_valid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
