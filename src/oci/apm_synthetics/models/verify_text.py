# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VerifyText(object):
    """
    Details to verify text.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VerifyText object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param text:
            The value to assign to the text property of this VerifyText.
        :type text: str

        """
        self.swagger_types = {
            'text': 'str'
        }

        self.attribute_map = {
            'text': 'text'
        }

        self._text = None

    @property
    def text(self):
        """
        Gets the text of this VerifyText.
        Verification text in the response.


        :return: The text of this VerifyText.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this VerifyText.
        Verification text in the response.


        :param text: The text of this VerifyText.
        :type: str
        """
        self._text = text

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
