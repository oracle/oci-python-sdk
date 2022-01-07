# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompareLineResult(object):
    """
    The result of a comparison of two lines in the two content input strings.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CompareLineResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param left_content:
            The value to assign to the left_content property of this CompareLineResult.
        :type left_content: str

        :param right_content:
            The value to assign to the right_content property of this CompareLineResult.
        :type right_content: str

        :param diff_type:
            The value to assign to the diff_type property of this CompareLineResult.
        :type diff_type: str

        :param left_indices:
            The value to assign to the left_indices property of this CompareLineResult.
        :type left_indices: str

        :param right_indices:
            The value to assign to the right_indices property of this CompareLineResult.
        :type right_indices: str

        """
        self.swagger_types = {
            'left_content': 'str',
            'right_content': 'str',
            'diff_type': 'str',
            'left_indices': 'str',
            'right_indices': 'str'
        }

        self.attribute_map = {
            'left_content': 'leftContent',
            'right_content': 'rightContent',
            'diff_type': 'diffType',
            'left_indices': 'leftIndices',
            'right_indices': 'rightIndices'
        }

        self._left_content = None
        self._right_content = None
        self._diff_type = None
        self._left_indices = None
        self._right_indices = None

    @property
    def left_content(self):
        """
        Gets the left_content of this CompareLineResult.
        A line from the content on the left. This may be empty if there is no matching line on
        the left for a line in the right content.


        :return: The left_content of this CompareLineResult.
        :rtype: str
        """
        return self._left_content

    @left_content.setter
    def left_content(self, left_content):
        """
        Sets the left_content of this CompareLineResult.
        A line from the content on the left. This may be empty if there is no matching line on
        the left for a line in the right content.


        :param left_content: The left_content of this CompareLineResult.
        :type: str
        """
        self._left_content = left_content

    @property
    def right_content(self):
        """
        Gets the right_content of this CompareLineResult.
        A line from the content on the right. This may be empty if there is no matching line on
        the right for a line in the left content.


        :return: The right_content of this CompareLineResult.
        :rtype: str
        """
        return self._right_content

    @right_content.setter
    def right_content(self, right_content):
        """
        Sets the right_content of this CompareLineResult.
        A line from the content on the right. This may be empty if there is no matching line on
        the right for a line in the left content.


        :param right_content: The right_content of this CompareLineResult.
        :type: str
        """
        self._right_content = right_content

    @property
    def diff_type(self):
        """
        Gets the diff_type of this CompareLineResult.
        The result of the line comparison. An empty string means the lines being compared are the
        same. A pipe, |, means the lines are different, and a caret, > or <, means the
        line is only found either on the right or the left.


        :return: The diff_type of this CompareLineResult.
        :rtype: str
        """
        return self._diff_type

    @diff_type.setter
    def diff_type(self, diff_type):
        """
        Sets the diff_type of this CompareLineResult.
        The result of the line comparison. An empty string means the lines being compared are the
        same. A pipe, |, means the lines are different, and a caret, > or <, means the
        line is only found either on the right or the left.


        :param diff_type: The diff_type of this CompareLineResult.
        :type: str
        """
        self._diff_type = diff_type

    @property
    def left_indices(self):
        """
        Gets the left_indices of this CompareLineResult.
        A comma delimited set of indices that identify which characters are different from those
        in the right string.


        :return: The left_indices of this CompareLineResult.
        :rtype: str
        """
        return self._left_indices

    @left_indices.setter
    def left_indices(self, left_indices):
        """
        Sets the left_indices of this CompareLineResult.
        A comma delimited set of indices that identify which characters are different from those
        in the right string.


        :param left_indices: The left_indices of this CompareLineResult.
        :type: str
        """
        self._left_indices = left_indices

    @property
    def right_indices(self):
        """
        Gets the right_indices of this CompareLineResult.
        A comma delimited set of indices that identify which characters are different from those
        in the left string.


        :return: The right_indices of this CompareLineResult.
        :rtype: str
        """
        return self._right_indices

    @right_indices.setter
    def right_indices(self, right_indices):
        """
        Sets the right_indices of this CompareLineResult.
        A comma delimited set of indices that identify which characters are different from those
        in the left string.


        :param right_indices: The right_indices of this CompareLineResult.
        :type: str
        """
        self._right_indices = right_indices

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
