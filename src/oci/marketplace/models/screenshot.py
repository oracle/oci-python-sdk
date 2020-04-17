# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Screenshot(object):
    """
    The model for a listing's screenshot.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Screenshot object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Screenshot.
        :type name: str

        :param description:
            The value to assign to the description property of this Screenshot.
        :type description: str

        :param content_url:
            The value to assign to the content_url property of this Screenshot.
        :type content_url: str

        :param mime_type:
            The value to assign to the mime_type property of this Screenshot.
        :type mime_type: str

        :param file_extension:
            The value to assign to the file_extension property of this Screenshot.
        :type file_extension: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'content_url': 'str',
            'mime_type': 'str',
            'file_extension': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'content_url': 'contentUrl',
            'mime_type': 'mimeType',
            'file_extension': 'fileExtension'
        }

        self._name = None
        self._description = None
        self._content_url = None
        self._mime_type = None
        self._file_extension = None

    @property
    def name(self):
        """
        Gets the name of this Screenshot.
        The name of the screenshot.


        :return: The name of this Screenshot.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Screenshot.
        The name of the screenshot.


        :param name: The name of this Screenshot.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Screenshot.
        A description of the screenshot.


        :return: The description of this Screenshot.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Screenshot.
        A description of the screenshot.


        :param description: The description of this Screenshot.
        :type: str
        """
        self._description = description

    @property
    def content_url(self):
        """
        Gets the content_url of this Screenshot.
        The content URL of the screenshot.


        :return: The content_url of this Screenshot.
        :rtype: str
        """
        return self._content_url

    @content_url.setter
    def content_url(self, content_url):
        """
        Sets the content_url of this Screenshot.
        The content URL of the screenshot.


        :param content_url: The content_url of this Screenshot.
        :type: str
        """
        self._content_url = content_url

    @property
    def mime_type(self):
        """
        Gets the mime_type of this Screenshot.
        The MIME type of the screenshot.


        :return: The mime_type of this Screenshot.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this Screenshot.
        The MIME type of the screenshot.


        :param mime_type: The mime_type of this Screenshot.
        :type: str
        """
        self._mime_type = mime_type

    @property
    def file_extension(self):
        """
        Gets the file_extension of this Screenshot.
        The file extension of the screenshot.


        :return: The file_extension of this Screenshot.
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """
        Sets the file_extension of this Screenshot.
        The file extension of the screenshot.


        :param file_extension: The file_extension of this Screenshot.
        :type: str
        """
        self._file_extension = file_extension

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
