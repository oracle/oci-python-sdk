# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateMultipartUploadDetails(object):

    def __init__(self):

        self.swagger_types = {
            'object': 'str',
            'content_type': 'str',
            'content_language': 'str',
            'content_encoding': 'str',
            'metadata': 'dict(str, str)'
        }

        self.attribute_map = {
            'object': 'object',
            'content_type': 'contentType',
            'content_language': 'contentLanguage',
            'content_encoding': 'contentEncoding',
            'metadata': 'metadata'
        }

        self._object = None
        self._content_type = None
        self._content_language = None
        self._content_encoding = None
        self._metadata = None

    @property
    def object(self):
        """
        Gets the object of this CreateMultipartUploadDetails.
        the name of the object to which this multi-part upload is targetted.


        :return: The object of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this CreateMultipartUploadDetails.
        the name of the object to which this multi-part upload is targetted.


        :param object: The object of this CreateMultipartUploadDetails.
        :type: str
        """
        self._object = object

    @property
    def content_type(self):
        """
        Gets the content_type of this CreateMultipartUploadDetails.
        the content type of the object to upload.


        :return: The content_type of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this CreateMultipartUploadDetails.
        the content type of the object to upload.


        :param content_type: The content_type of this CreateMultipartUploadDetails.
        :type: str
        """
        self._content_type = content_type

    @property
    def content_language(self):
        """
        Gets the content_language of this CreateMultipartUploadDetails.
        the content language of the object to upload.


        :return: The content_language of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._content_language

    @content_language.setter
    def content_language(self, content_language):
        """
        Sets the content_language of this CreateMultipartUploadDetails.
        the content language of the object to upload.


        :param content_language: The content_language of this CreateMultipartUploadDetails.
        :type: str
        """
        self._content_language = content_language

    @property
    def content_encoding(self):
        """
        Gets the content_encoding of this CreateMultipartUploadDetails.
        the content encoding of the object to upload.


        :return: The content_encoding of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._content_encoding

    @content_encoding.setter
    def content_encoding(self, content_encoding):
        """
        Sets the content_encoding of this CreateMultipartUploadDetails.
        the content encoding of the object to upload.


        :param content_encoding: The content_encoding of this CreateMultipartUploadDetails.
        :type: str
        """
        self._content_encoding = content_encoding

    @property
    def metadata(self):
        """
        Gets the metadata of this CreateMultipartUploadDetails.
        Arbitrary string keys and values for the user-defined metadata for the object.
        Keys must be in \"opc-meta-*\" format.


        :return: The metadata of this CreateMultipartUploadDetails.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateMultipartUploadDetails.
        Arbitrary string keys and values for the user-defined metadata for the object.
        Keys must be in \"opc-meta-*\" format.


        :param metadata: The metadata of this CreateMultipartUploadDetails.
        :type: dict(str, str)
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
