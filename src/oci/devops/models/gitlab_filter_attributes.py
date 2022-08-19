# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GitlabFilterAttributes(object):
    """
    Attributes to filter GitLab events.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GitlabFilterAttributes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param head_ref:
            The value to assign to the head_ref property of this GitlabFilterAttributes.
        :type head_ref: str

        :param base_ref:
            The value to assign to the base_ref property of this GitlabFilterAttributes.
        :type base_ref: str

        :param file_filter:
            The value to assign to the file_filter property of this GitlabFilterAttributes.
        :type file_filter: oci.devops.models.FileFilter

        """
        self.swagger_types = {
            'head_ref': 'str',
            'base_ref': 'str',
            'file_filter': 'FileFilter'
        }

        self.attribute_map = {
            'head_ref': 'headRef',
            'base_ref': 'baseRef',
            'file_filter': 'fileFilter'
        }

        self._head_ref = None
        self._base_ref = None
        self._file_filter = None

    @property
    def head_ref(self):
        """
        Gets the head_ref of this GitlabFilterAttributes.
        Branch for push event; source branch for pull requests.


        :return: The head_ref of this GitlabFilterAttributes.
        :rtype: str
        """
        return self._head_ref

    @head_ref.setter
    def head_ref(self, head_ref):
        """
        Sets the head_ref of this GitlabFilterAttributes.
        Branch for push event; source branch for pull requests.


        :param head_ref: The head_ref of this GitlabFilterAttributes.
        :type: str
        """
        self._head_ref = head_ref

    @property
    def base_ref(self):
        """
        Gets the base_ref of this GitlabFilterAttributes.
        The target branch for pull requests; not applicable for push requests.


        :return: The base_ref of this GitlabFilterAttributes.
        :rtype: str
        """
        return self._base_ref

    @base_ref.setter
    def base_ref(self, base_ref):
        """
        Sets the base_ref of this GitlabFilterAttributes.
        The target branch for pull requests; not applicable for push requests.


        :param base_ref: The base_ref of this GitlabFilterAttributes.
        :type: str
        """
        self._base_ref = base_ref

    @property
    def file_filter(self):
        """
        Gets the file_filter of this GitlabFilterAttributes.

        :return: The file_filter of this GitlabFilterAttributes.
        :rtype: oci.devops.models.FileFilter
        """
        return self._file_filter

    @file_filter.setter
    def file_filter(self, file_filter):
        """
        Sets the file_filter of this GitlabFilterAttributes.

        :param file_filter: The file_filter of this GitlabFilterAttributes.
        :type: oci.devops.models.FileFilter
        """
        self._file_filter = file_filter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
