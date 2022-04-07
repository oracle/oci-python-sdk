# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageText(object):
    """
    The detected text.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageText object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param words:
            The value to assign to the words property of this ImageText.
        :type words: list[oci.ai_vision.models.Word]

        :param lines:
            The value to assign to the lines property of this ImageText.
        :type lines: list[oci.ai_vision.models.Line]

        """
        self.swagger_types = {
            'words': 'list[Word]',
            'lines': 'list[Line]'
        }

        self.attribute_map = {
            'words': 'words',
            'lines': 'lines'
        }

        self._words = None
        self._lines = None

    @property
    def words(self):
        """
        **[Required]** Gets the words of this ImageText.
        The words recognized in an image.


        :return: The words of this ImageText.
        :rtype: list[oci.ai_vision.models.Word]
        """
        return self._words

    @words.setter
    def words(self, words):
        """
        Sets the words of this ImageText.
        The words recognized in an image.


        :param words: The words of this ImageText.
        :type: list[oci.ai_vision.models.Word]
        """
        self._words = words

    @property
    def lines(self):
        """
        **[Required]** Gets the lines of this ImageText.
        The lines of text recognized in an image.


        :return: The lines of this ImageText.
        :rtype: list[oci.ai_vision.models.Line]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this ImageText.
        The lines of text recognized in an image.


        :param lines: The lines of this ImageText.
        :type: list[oci.ai_vision.models.Line]
        """
        self._lines = lines

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
