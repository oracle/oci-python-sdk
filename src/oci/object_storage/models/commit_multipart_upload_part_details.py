# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CommitMultipartUploadPartDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CommitMultipartUploadPartDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param part_num:
            The value to assign to the part_num property of this CommitMultipartUploadPartDetails.
        :type part_num: int

        :param etag:
            The value to assign to the etag property of this CommitMultipartUploadPartDetails.
        :type etag: str

        """
        self.swagger_types = {
            'part_num': 'int',
            'etag': 'str'
        }

        self.attribute_map = {
            'part_num': 'partNum',
            'etag': 'etag'
        }

        self._part_num = None
        self._etag = None

    @property
    def part_num(self):
        """
        **[Required]** Gets the part_num of this CommitMultipartUploadPartDetails.
        The part number for this part.


        :return: The part_num of this CommitMultipartUploadPartDetails.
        :rtype: int
        """
        return self._part_num

    @part_num.setter
    def part_num(self, part_num):
        """
        Sets the part_num of this CommitMultipartUploadPartDetails.
        The part number for this part.


        :param part_num: The part_num of this CommitMultipartUploadPartDetails.
        :type: int
        """
        self._part_num = part_num

    @property
    def etag(self):
        """
        **[Required]** Gets the etag of this CommitMultipartUploadPartDetails.
        The ETag returned when this part was uploaded.


        :return: The etag of this CommitMultipartUploadPartDetails.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this CommitMultipartUploadPartDetails.
        The ETag returned when this part was uploaded.


        :param etag: The etag of this CommitMultipartUploadPartDetails.
        :type: str
        """
        self._etag = etag

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
