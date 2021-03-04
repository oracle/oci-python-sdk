# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MessageDetails(object):
    """
    The content of the message to be published.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MessageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param title:
            The value to assign to the title property of this MessageDetails.
        :type title: str

        :param body:
            The value to assign to the body property of this MessageDetails.
        :type body: str

        """
        self.swagger_types = {
            'title': 'str',
            'body': 'str'
        }

        self.attribute_map = {
            'title': 'title',
            'body': 'body'
        }

        self._title = None
        self._body = None

    @property
    def title(self):
        """
        Gets the title of this MessageDetails.
        The title of the message to be published. Avoid entering confidential information.


        :return: The title of this MessageDetails.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this MessageDetails.
        The title of the message to be published. Avoid entering confidential information.


        :param title: The title of this MessageDetails.
        :type: str
        """
        self._title = title

    @property
    def body(self):
        """
        **[Required]** Gets the body of this MessageDetails.
        The body of the message to be published.
        Avoid entering confidential information.


        :return: The body of this MessageDetails.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this MessageDetails.
        The body of the message to be published.
        Avoid entering confidential information.


        :param body: The body of this MessageDetails.
        :type: str
        """
        self._body = body

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
