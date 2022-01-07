# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GithubFilterAttributes(object):
    """
    Attributes to filter GitHub events.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GithubFilterAttributes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param head_ref:
            The value to assign to the head_ref property of this GithubFilterAttributes.
        :type head_ref: str

        :param base_ref:
            The value to assign to the base_ref property of this GithubFilterAttributes.
        :type base_ref: str

        """
        self.swagger_types = {
            'head_ref': 'str',
            'base_ref': 'str'
        }

        self.attribute_map = {
            'head_ref': 'headRef',
            'base_ref': 'baseRef'
        }

        self._head_ref = None
        self._base_ref = None

    @property
    def head_ref(self):
        """
        Gets the head_ref of this GithubFilterAttributes.
        Branch for push event; source branch for pull requests.


        :return: The head_ref of this GithubFilterAttributes.
        :rtype: str
        """
        return self._head_ref

    @head_ref.setter
    def head_ref(self, head_ref):
        """
        Sets the head_ref of this GithubFilterAttributes.
        Branch for push event; source branch for pull requests.


        :param head_ref: The head_ref of this GithubFilterAttributes.
        :type: str
        """
        self._head_ref = head_ref

    @property
    def base_ref(self):
        """
        Gets the base_ref of this GithubFilterAttributes.
        The target branch for pull requests; not applicable for push requests.


        :return: The base_ref of this GithubFilterAttributes.
        :rtype: str
        """
        return self._base_ref

    @base_ref.setter
    def base_ref(self, base_ref):
        """
        Sets the base_ref of this GithubFilterAttributes.
        The target branch for pull requests; not applicable for push requests.


        :param base_ref: The base_ref of this GithubFilterAttributes.
        :type: str
        """
        self._base_ref = base_ref

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
