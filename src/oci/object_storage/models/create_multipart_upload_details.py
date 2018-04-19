# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMultipartUploadDetails(object):
    """
    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMultipartUploadDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object:
            The value to assign to the object property of this CreateMultipartUploadDetails.
        :type object: str

        :param content_type:
            The value to assign to the content_type property of this CreateMultipartUploadDetails.
        :type content_type: str

        :param content_language:
            The value to assign to the content_language property of this CreateMultipartUploadDetails.
        :type content_language: str

        :param content_encoding:
            The value to assign to the content_encoding property of this CreateMultipartUploadDetails.
        :type content_encoding: str

        :param metadata:
            The value to assign to the metadata property of this CreateMultipartUploadDetails.
        :type metadata: dict(str, str)

        """
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
        **[Required]** Gets the object of this CreateMultipartUploadDetails.
        The name of the object to which this multi-part upload is targeted. Avoid entering confidential information.
        Example: test/object1.log


        :return: The object of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this CreateMultipartUploadDetails.
        The name of the object to which this multi-part upload is targeted. Avoid entering confidential information.
        Example: test/object1.log


        :param object: The object of this CreateMultipartUploadDetails.
        :type: str
        """
        self._object = object

    @property
    def content_type(self):
        """
        Gets the content_type of this CreateMultipartUploadDetails.
        The content type of the object to upload.


        :return: The content_type of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this CreateMultipartUploadDetails.
        The content type of the object to upload.


        :param content_type: The content_type of this CreateMultipartUploadDetails.
        :type: str
        """
        self._content_type = content_type

    @property
    def content_language(self):
        """
        Gets the content_language of this CreateMultipartUploadDetails.
        The content language of the object to upload.


        :return: The content_language of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._content_language

    @content_language.setter
    def content_language(self, content_language):
        """
        Sets the content_language of this CreateMultipartUploadDetails.
        The content language of the object to upload.


        :param content_language: The content_language of this CreateMultipartUploadDetails.
        :type: str
        """
        self._content_language = content_language

    @property
    def content_encoding(self):
        """
        Gets the content_encoding of this CreateMultipartUploadDetails.
        The content encoding of the object to upload.


        :return: The content_encoding of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._content_encoding

    @content_encoding.setter
    def content_encoding(self, content_encoding):
        """
        Sets the content_encoding of this CreateMultipartUploadDetails.
        The content encoding of the object to upload.


        :param content_encoding: The content_encoding of this CreateMultipartUploadDetails.
        :type: str
        """
        self._content_encoding = content_encoding

    @property
    def metadata(self):
        """
        Gets the metadata of this CreateMultipartUploadDetails.
        Arbitrary string keys and values for the user-defined metadata for the object.
        Keys must be in \"opc-meta-*\" format. Avoid entering confidential information.


        :return: The metadata of this CreateMultipartUploadDetails.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateMultipartUploadDetails.
        Arbitrary string keys and values for the user-defined metadata for the object.
        Keys must be in \"opc-meta-*\" format. Avoid entering confidential information.


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
