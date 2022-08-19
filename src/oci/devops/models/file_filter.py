# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FileFilter(object):
    """
    Attributes to support include/exclude files for triggering build runs.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FileFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param file_paths:
            The value to assign to the file_paths property of this FileFilter.
        :type file_paths: list[str]

        """
        self.swagger_types = {
            'file_paths': 'list[str]'
        }

        self.attribute_map = {
            'file_paths': 'filePaths'
        }

        self._file_paths = None

    @property
    def file_paths(self):
        """
        Gets the file_paths of this FileFilter.
        The file paths/glob pattern for files.


        :return: The file_paths of this FileFilter.
        :rtype: list[str]
        """
        return self._file_paths

    @file_paths.setter
    def file_paths(self, file_paths):
        """
        Sets the file_paths of this FileFilter.
        The file paths/glob pattern for files.


        :param file_paths: The file_paths of this FileFilter.
        :type: list[str]
        """
        self._file_paths = file_paths

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
