# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UploadData(object):
    """
    The model for upload data for images and icons.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UploadData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UploadData.
        :type name: str

        :param content_url:
            The value to assign to the content_url property of this UploadData.
        :type content_url: str

        :param mime_type:
            The value to assign to the mime_type property of this UploadData.
        :type mime_type: str

        :param file_extension:
            The value to assign to the file_extension property of this UploadData.
        :type file_extension: str

        """
        self.swagger_types = {
            'name': 'str',
            'content_url': 'str',
            'mime_type': 'str',
            'file_extension': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'content_url': 'contentUrl',
            'mime_type': 'mimeType',
            'file_extension': 'fileExtension'
        }

        self._name = None
        self._content_url = None
        self._mime_type = None
        self._file_extension = None

    @property
    def name(self):
        """
        Gets the name of this UploadData.
        The name used to refer to the upload data.


        :return: The name of this UploadData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UploadData.
        The name used to refer to the upload data.


        :param name: The name of this UploadData.
        :type: str
        """
        self._name = name

    @property
    def content_url(self):
        """
        Gets the content_url of this UploadData.
        The content URL of the upload data.


        :return: The content_url of this UploadData.
        :rtype: str
        """
        return self._content_url

    @content_url.setter
    def content_url(self, content_url):
        """
        Sets the content_url of this UploadData.
        The content URL of the upload data.


        :param content_url: The content_url of this UploadData.
        :type: str
        """
        self._content_url = content_url

    @property
    def mime_type(self):
        """
        Gets the mime_type of this UploadData.
        The MIME type of the upload data.


        :return: The mime_type of this UploadData.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this UploadData.
        The MIME type of the upload data.


        :param mime_type: The mime_type of this UploadData.
        :type: str
        """
        self._mime_type = mime_type

    @property
    def file_extension(self):
        """
        Gets the file_extension of this UploadData.
        The file extension of the upload data.


        :return: The file_extension of this UploadData.
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """
        Sets the file_extension of this UploadData.
        The file extension of the upload data.


        :param file_extension: The file_extension of this UploadData.
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
