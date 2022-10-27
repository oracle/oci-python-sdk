# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TrailFileSummary(object):
    """
    Summary of the TrailFiles.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TrailFileSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param trail_file_id:
            The value to assign to the trail_file_id property of this TrailFileSummary.
        :type trail_file_id: str

        :param display_name:
            The value to assign to the display_name property of this TrailFileSummary.
        :type display_name: str

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this TrailFileSummary.
        :type size_in_bytes: float

        :param time_last_updated:
            The value to assign to the time_last_updated property of this TrailFileSummary.
        :type time_last_updated: datetime

        :param number_of_sequences:
            The value to assign to the number_of_sequences property of this TrailFileSummary.
        :type number_of_sequences: int

        :param min_sequence_number:
            The value to assign to the min_sequence_number property of this TrailFileSummary.
        :type min_sequence_number: str

        :param max_sequence_number:
            The value to assign to the max_sequence_number property of this TrailFileSummary.
        :type max_sequence_number: str

        :param producer:
            The value to assign to the producer property of this TrailFileSummary.
        :type producer: str

        :param consumers:
            The value to assign to the consumers property of this TrailFileSummary.
        :type consumers: list[str]

        """
        self.swagger_types = {
            'trail_file_id': 'str',
            'display_name': 'str',
            'size_in_bytes': 'float',
            'time_last_updated': 'datetime',
            'number_of_sequences': 'int',
            'min_sequence_number': 'str',
            'max_sequence_number': 'str',
            'producer': 'str',
            'consumers': 'list[str]'
        }

        self.attribute_map = {
            'trail_file_id': 'trailFileId',
            'display_name': 'displayName',
            'size_in_bytes': 'sizeInBytes',
            'time_last_updated': 'timeLastUpdated',
            'number_of_sequences': 'numberOfSequences',
            'min_sequence_number': 'minSequenceNumber',
            'max_sequence_number': 'maxSequenceNumber',
            'producer': 'producer',
            'consumers': 'consumers'
        }

        self._trail_file_id = None
        self._display_name = None
        self._size_in_bytes = None
        self._time_last_updated = None
        self._number_of_sequences = None
        self._min_sequence_number = None
        self._max_sequence_number = None
        self._producer = None
        self._consumers = None

    @property
    def trail_file_id(self):
        """
        **[Required]** Gets the trail_file_id of this TrailFileSummary.
        The TrailFile Id.


        :return: The trail_file_id of this TrailFileSummary.
        :rtype: str
        """
        return self._trail_file_id

    @trail_file_id.setter
    def trail_file_id(self, trail_file_id):
        """
        Sets the trail_file_id of this TrailFileSummary.
        The TrailFile Id.


        :param trail_file_id: The trail_file_id of this TrailFileSummary.
        :type: str
        """
        self._trail_file_id = trail_file_id

    @property
    def display_name(self):
        """
        Gets the display_name of this TrailFileSummary.
        An object's Display Name.


        :return: The display_name of this TrailFileSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TrailFileSummary.
        An object's Display Name.


        :param display_name: The display_name of this TrailFileSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def size_in_bytes(self):
        """
        Gets the size_in_bytes of this TrailFileSummary.
        The size of the backup stored in object storage (in bytes)


        :return: The size_in_bytes of this TrailFileSummary.
        :rtype: float
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this TrailFileSummary.
        The size of the backup stored in object storage (in bytes)


        :param size_in_bytes: The size_in_bytes of this TrailFileSummary.
        :type: float
        """
        self._size_in_bytes = size_in_bytes

    @property
    def time_last_updated(self):
        """
        Gets the time_last_updated of this TrailFileSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_last_updated of this TrailFileSummary.
        :rtype: datetime
        """
        return self._time_last_updated

    @time_last_updated.setter
    def time_last_updated(self, time_last_updated):
        """
        Sets the time_last_updated of this TrailFileSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_last_updated: The time_last_updated of this TrailFileSummary.
        :type: datetime
        """
        self._time_last_updated = time_last_updated

    @property
    def number_of_sequences(self):
        """
        Gets the number_of_sequences of this TrailFileSummary.
        Number of sequences for a specific trail file


        :return: The number_of_sequences of this TrailFileSummary.
        :rtype: int
        """
        return self._number_of_sequences

    @number_of_sequences.setter
    def number_of_sequences(self, number_of_sequences):
        """
        Sets the number_of_sequences of this TrailFileSummary.
        Number of sequences for a specific trail file


        :param number_of_sequences: The number_of_sequences of this TrailFileSummary.
        :type: int
        """
        self._number_of_sequences = number_of_sequences

    @property
    def min_sequence_number(self):
        """
        Gets the min_sequence_number of this TrailFileSummary.
        Minimum sequence number


        :return: The min_sequence_number of this TrailFileSummary.
        :rtype: str
        """
        return self._min_sequence_number

    @min_sequence_number.setter
    def min_sequence_number(self, min_sequence_number):
        """
        Sets the min_sequence_number of this TrailFileSummary.
        Minimum sequence number


        :param min_sequence_number: The min_sequence_number of this TrailFileSummary.
        :type: str
        """
        self._min_sequence_number = min_sequence_number

    @property
    def max_sequence_number(self):
        """
        Gets the max_sequence_number of this TrailFileSummary.
        Maximum sequence number


        :return: The max_sequence_number of this TrailFileSummary.
        :rtype: str
        """
        return self._max_sequence_number

    @max_sequence_number.setter
    def max_sequence_number(self, max_sequence_number):
        """
        Sets the max_sequence_number of this TrailFileSummary.
        Maximum sequence number


        :param max_sequence_number: The max_sequence_number of this TrailFileSummary.
        :type: str
        """
        self._max_sequence_number = max_sequence_number

    @property
    def producer(self):
        """
        Gets the producer of this TrailFileSummary.
        Producer Process Name if any.


        :return: The producer of this TrailFileSummary.
        :rtype: str
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """
        Sets the producer of this TrailFileSummary.
        Producer Process Name if any.


        :param producer: The producer of this TrailFileSummary.
        :type: str
        """
        self._producer = producer

    @property
    def consumers(self):
        """
        Gets the consumers of this TrailFileSummary.
        array of consumer process names


        :return: The consumers of this TrailFileSummary.
        :rtype: list[str]
        """
        return self._consumers

    @consumers.setter
    def consumers(self, consumers):
        """
        Sets the consumers of this TrailFileSummary.
        array of consumer process names


        :param consumers: The consumers of this TrailFileSummary.
        :type: list[str]
        """
        self._consumers = consumers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
