# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TrailSequenceSummary(object):
    """
    Summary of the TrailSequences.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TrailSequenceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sequence_id:
            The value to assign to the sequence_id property of this TrailSequenceSummary.
        :type sequence_id: str

        :param display_name:
            The value to assign to the display_name property of this TrailSequenceSummary.
        :type display_name: str

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this TrailSequenceSummary.
        :type size_in_bytes: float

        :param time_last_updated:
            The value to assign to the time_last_updated property of this TrailSequenceSummary.
        :type time_last_updated: datetime

        """
        self.swagger_types = {
            'sequence_id': 'str',
            'display_name': 'str',
            'size_in_bytes': 'float',
            'time_last_updated': 'datetime'
        }

        self.attribute_map = {
            'sequence_id': 'sequenceId',
            'display_name': 'displayName',
            'size_in_bytes': 'sizeInBytes',
            'time_last_updated': 'timeLastUpdated'
        }

        self._sequence_id = None
        self._display_name = None
        self._size_in_bytes = None
        self._time_last_updated = None

    @property
    def sequence_id(self):
        """
        **[Required]** Gets the sequence_id of this TrailSequenceSummary.
        Sequence Id


        :return: The sequence_id of this TrailSequenceSummary.
        :rtype: str
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        """
        Sets the sequence_id of this TrailSequenceSummary.
        Sequence Id


        :param sequence_id: The sequence_id of this TrailSequenceSummary.
        :type: str
        """
        self._sequence_id = sequence_id

    @property
    def display_name(self):
        """
        Gets the display_name of this TrailSequenceSummary.
        An object's Display Name.


        :return: The display_name of this TrailSequenceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TrailSequenceSummary.
        An object's Display Name.


        :param display_name: The display_name of this TrailSequenceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def size_in_bytes(self):
        """
        Gets the size_in_bytes of this TrailSequenceSummary.
        The size of the backup stored in object storage (in bytes)


        :return: The size_in_bytes of this TrailSequenceSummary.
        :rtype: float
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this TrailSequenceSummary.
        The size of the backup stored in object storage (in bytes)


        :param size_in_bytes: The size_in_bytes of this TrailSequenceSummary.
        :type: float
        """
        self._size_in_bytes = size_in_bytes

    @property
    def time_last_updated(self):
        """
        Gets the time_last_updated of this TrailSequenceSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_last_updated of this TrailSequenceSummary.
        :rtype: datetime
        """
        return self._time_last_updated

    @time_last_updated.setter
    def time_last_updated(self, time_last_updated):
        """
        Sets the time_last_updated of this TrailSequenceSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_last_updated: The time_last_updated of this TrailSequenceSummary.
        :type: datetime
        """
        self._time_last_updated = time_last_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
