# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MultipartUploadPartSummary(object):

    def __init__(self, **kwargs):
        """
        Initializes a new MultipartUploadPartSummary object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param etag:
            The value to assign to the etag property of this MultipartUploadPartSummary.
        :type etag: str

        :param md5:
            The value to assign to the md5 property of this MultipartUploadPartSummary.
        :type md5: str

        :param size:
            The value to assign to the size property of this MultipartUploadPartSummary.
        :type size: int

        :param part_number:
            The value to assign to the part_number property of this MultipartUploadPartSummary.
        :type part_number: int

        """
        self.swagger_types = {
            'etag': 'str',
            'md5': 'str',
            'size': 'int',
            'part_number': 'int'
        }

        self.attribute_map = {
            'etag': 'etag',
            'md5': 'md5',
            'size': 'size',
            'part_number': 'partNumber'
        }

        self._etag = None
        self._md5 = None
        self._size = None
        self._part_number = None

    @property
    def etag(self):
        """
        **[Required]** Gets the etag of this MultipartUploadPartSummary.
        The current entity tag for the part.


        :return: The etag of this MultipartUploadPartSummary.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this MultipartUploadPartSummary.
        The current entity tag for the part.


        :param etag: The etag of this MultipartUploadPartSummary.
        :type: str
        """
        self._etag = etag

    @property
    def md5(self):
        """
        **[Required]** Gets the md5 of this MultipartUploadPartSummary.
        The MD5 hash of the bytes of the part.


        :return: The md5 of this MultipartUploadPartSummary.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """
        Sets the md5 of this MultipartUploadPartSummary.
        The MD5 hash of the bytes of the part.


        :param md5: The md5 of this MultipartUploadPartSummary.
        :type: str
        """
        self._md5 = md5

    @property
    def size(self):
        """
        **[Required]** Gets the size of this MultipartUploadPartSummary.
        The size of the part in bytes.


        :return: The size of this MultipartUploadPartSummary.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this MultipartUploadPartSummary.
        The size of the part in bytes.


        :param size: The size of this MultipartUploadPartSummary.
        :type: int
        """
        self._size = size

    @property
    def part_number(self):
        """
        **[Required]** Gets the part_number of this MultipartUploadPartSummary.
        The part number for this part.


        :return: The part_number of this MultipartUploadPartSummary.
        :rtype: int
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this MultipartUploadPartSummary.
        The part number for this part.


        :param part_number: The part_number of this MultipartUploadPartSummary.
        :type: int
        """
        self._part_number = part_number

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
