# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompareContentDetails(object):
    """
    The two strings to compare.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CompareContentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content1:
            The value to assign to the content1 property of this CompareContentDetails.
        :type content1: str

        :param content2:
            The value to assign to the content2 property of this CompareContentDetails.
        :type content2: str

        """
        self.swagger_types = {
            'content1': 'str',
            'content2': 'str'
        }

        self.attribute_map = {
            'content1': 'content1',
            'content2': 'content2'
        }

        self._content1 = None
        self._content2 = None

    @property
    def content1(self):
        """
        Gets the content1 of this CompareContentDetails.
        The first of two strings to compare.


        :return: The content1 of this CompareContentDetails.
        :rtype: str
        """
        return self._content1

    @content1.setter
    def content1(self, content1):
        """
        Sets the content1 of this CompareContentDetails.
        The first of two strings to compare.


        :param content1: The content1 of this CompareContentDetails.
        :type: str
        """
        self._content1 = content1

    @property
    def content2(self):
        """
        Gets the content2 of this CompareContentDetails.
        The second of two strings to compare.


        :return: The content2 of this CompareContentDetails.
        :rtype: str
        """
        return self._content2

    @content2.setter
    def content2(self, content2):
        """
        Sets the content2 of this CompareContentDetails.
        The second of two strings to compare.


        :param content2: The content2 of this CompareContentDetails.
        :type: str
        """
        self._content2 = content2

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
