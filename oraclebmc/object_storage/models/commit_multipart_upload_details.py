# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CommitMultipartUploadDetails(object):

    def __init__(self):

        self.swagger_types = {
            'parts_to_commit': 'list[CommitMultipartUploadPartDetails]',
            'parts_to_exclude': 'list[int]'
        }

        self.attribute_map = {
            'parts_to_commit': 'partsToCommit',
            'parts_to_exclude': 'partsToExclude'
        }

        self._parts_to_commit = None
        self._parts_to_exclude = None

    @property
    def parts_to_commit(self):
        """
        Gets the parts_to_commit of this CommitMultipartUploadDetails.
        The part numbers and ETags for the parts to be committed.


        :return: The parts_to_commit of this CommitMultipartUploadDetails.
        :rtype: list[CommitMultipartUploadPartDetails]
        """
        return self._parts_to_commit

    @parts_to_commit.setter
    def parts_to_commit(self, parts_to_commit):
        """
        Sets the parts_to_commit of this CommitMultipartUploadDetails.
        The part numbers and ETags for the parts to be committed.


        :param parts_to_commit: The parts_to_commit of this CommitMultipartUploadDetails.
        :type: list[CommitMultipartUploadPartDetails]
        """
        self._parts_to_commit = parts_to_commit

    @property
    def parts_to_exclude(self):
        """
        Gets the parts_to_exclude of this CommitMultipartUploadDetails.
        The part numbers for the parts to be excluded from the completed object.
        Each part created for this upload must be in either partsToExclude or partsToCommit, but cannot be in both.


        :return: The parts_to_exclude of this CommitMultipartUploadDetails.
        :rtype: list[int]
        """
        return self._parts_to_exclude

    @parts_to_exclude.setter
    def parts_to_exclude(self, parts_to_exclude):
        """
        Sets the parts_to_exclude of this CommitMultipartUploadDetails.
        The part numbers for the parts to be excluded from the completed object.
        Each part created for this upload must be in either partsToExclude or partsToCommit, but cannot be in both.


        :param parts_to_exclude: The parts_to_exclude of this CommitMultipartUploadDetails.
        :type: list[int]
        """
        self._parts_to_exclude = parts_to_exclude

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
