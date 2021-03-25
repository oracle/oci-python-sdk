# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StatusSummary(object):
    """
    StatusSummary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StatusSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param chunks_processed:
            The value to assign to the chunks_processed property of this StatusSummary.
        :type chunks_processed: int

        :param failure_details:
            The value to assign to the failure_details property of this StatusSummary.
        :type failure_details: str

        :param filename:
            The value to assign to the filename property of this StatusSummary.
        :type filename: str

        :param status:
            The value to assign to the status property of this StatusSummary.
        :type status: str

        :param total_chunks:
            The value to assign to the total_chunks property of this StatusSummary.
        :type total_chunks: int

        """
        self.swagger_types = {
            'chunks_processed': 'int',
            'failure_details': 'str',
            'filename': 'str',
            'status': 'str',
            'total_chunks': 'int'
        }

        self.attribute_map = {
            'chunks_processed': 'chunksProcessed',
            'failure_details': 'failureDetails',
            'filename': 'filename',
            'status': 'status',
            'total_chunks': 'totalChunks'
        }

        self._chunks_processed = None
        self._failure_details = None
        self._filename = None
        self._status = None
        self._total_chunks = None

    @property
    def chunks_processed(self):
        """
        Gets the chunks_processed of this StatusSummary.
        The number of chunks processed.


        :return: The chunks_processed of this StatusSummary.
        :rtype: int
        """
        return self._chunks_processed

    @chunks_processed.setter
    def chunks_processed(self, chunks_processed):
        """
        Sets the chunks_processed of this StatusSummary.
        The number of chunks processed.


        :param chunks_processed: The chunks_processed of this StatusSummary.
        :type: int
        """
        self._chunks_processed = chunks_processed

    @property
    def failure_details(self):
        """
        Gets the failure_details of this StatusSummary.
        The failure details, if any.


        :return: The failure_details of this StatusSummary.
        :rtype: str
        """
        return self._failure_details

    @failure_details.setter
    def failure_details(self, failure_details):
        """
        Sets the failure_details of this StatusSummary.
        The failure details, if any.


        :param failure_details: The failure_details of this StatusSummary.
        :type: str
        """
        self._failure_details = failure_details

    @property
    def filename(self):
        """
        Gets the filename of this StatusSummary.
        The filename.


        :return: The filename of this StatusSummary.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this StatusSummary.
        The filename.


        :param filename: The filename of this StatusSummary.
        :type: str
        """
        self._filename = filename

    @property
    def status(self):
        """
        Gets the status of this StatusSummary.
        The status.


        :return: The status of this StatusSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this StatusSummary.
        The status.


        :param status: The status of this StatusSummary.
        :type: str
        """
        self._status = status

    @property
    def total_chunks(self):
        """
        Gets the total_chunks of this StatusSummary.
        The total number of chunks.


        :return: The total_chunks of this StatusSummary.
        :rtype: int
        """
        return self._total_chunks

    @total_chunks.setter
    def total_chunks(self, total_chunks):
        """
        Sets the total_chunks of this StatusSummary.
        The total number of chunks.


        :param total_chunks: The total_chunks of this StatusSummary.
        :type: int
        """
        self._total_chunks = total_chunks

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
