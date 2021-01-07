# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogEntryBatch(object):
    """
    A single batch of Log Entries.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogEntryBatch object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entries:
            The value to assign to the entries property of this LogEntryBatch.
        :type entries: list[oci.loggingingestion.models.LogEntry]

        :param source:
            The value to assign to the source property of this LogEntryBatch.
        :type source: str

        :param type:
            The value to assign to the type property of this LogEntryBatch.
        :type type: str

        :param subject:
            The value to assign to the subject property of this LogEntryBatch.
        :type subject: str

        :param defaultlogentrytime:
            The value to assign to the defaultlogentrytime property of this LogEntryBatch.
        :type defaultlogentrytime: datetime

        """
        self.swagger_types = {
            'entries': 'list[LogEntry]',
            'source': 'str',
            'type': 'str',
            'subject': 'str',
            'defaultlogentrytime': 'datetime'
        }

        self.attribute_map = {
            'entries': 'entries',
            'source': 'source',
            'type': 'type',
            'subject': 'subject',
            'defaultlogentrytime': 'defaultlogentrytime'
        }

        self._entries = None
        self._source = None
        self._type = None
        self._subject = None
        self._defaultlogentrytime = None

    @property
    def entries(self):
        """
        **[Required]** Gets the entries of this LogEntryBatch.
        List of data entries.


        :return: The entries of this LogEntryBatch.
        :rtype: list[oci.loggingingestion.models.LogEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """
        Sets the entries of this LogEntryBatch.
        List of data entries.


        :param entries: The entries of this LogEntryBatch.
        :type: list[oci.loggingingestion.models.LogEntry]
        """
        self._entries = entries

    @property
    def source(self):
        """
        **[Required]** Gets the source of this LogEntryBatch.
        Source of the logs that generated the message. This could be the
        instance name, hostname, or the source used to read the event. For example, \"ServerA\".


        :return: The source of this LogEntryBatch.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this LogEntryBatch.
        Source of the logs that generated the message. This could be the
        instance name, hostname, or the source used to read the event. For example, \"ServerA\".


        :param source: The source of this LogEntryBatch.
        :type: str
        """
        self._source = source

    @property
    def type(self):
        """
        **[Required]** Gets the type of this LogEntryBatch.
        This field signifies the type of logs being ingested.
        For example: ServerA.requestLogs.


        :return: The type of this LogEntryBatch.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LogEntryBatch.
        This field signifies the type of logs being ingested.
        For example: ServerA.requestLogs.


        :param type: The type of this LogEntryBatch.
        :type: str
        """
        self._type = type

    @property
    def subject(self):
        """
        Gets the subject of this LogEntryBatch.
        This optional field is useful for specifying the specific sub-resource
        or input file used to read the event.
        For example: \"/var/log/application.log\".


        :return: The subject of this LogEntryBatch.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this LogEntryBatch.
        This optional field is useful for specifying the specific sub-resource
        or input file used to read the event.
        For example: \"/var/log/application.log\".


        :param subject: The subject of this LogEntryBatch.
        :type: str
        """
        self._subject = subject

    @property
    def defaultlogentrytime(self):
        """
        **[Required]** Gets the defaultlogentrytime of this LogEntryBatch.
        The timestamp for all log entries in this batch. This can be
        considered as the default timestamp for each entry, unless it is
        overwritten by the entry time. An RFC3339-formatted date-time
        string.


        :return: The defaultlogentrytime of this LogEntryBatch.
        :rtype: datetime
        """
        return self._defaultlogentrytime

    @defaultlogentrytime.setter
    def defaultlogentrytime(self, defaultlogentrytime):
        """
        Sets the defaultlogentrytime of this LogEntryBatch.
        The timestamp for all log entries in this batch. This can be
        considered as the default timestamp for each entry, unless it is
        overwritten by the entry time. An RFC3339-formatted date-time
        string.


        :param defaultlogentrytime: The defaultlogentrytime of this LogEntryBatch.
        :type: datetime
        """
        self._defaultlogentrytime = defaultlogentrytime

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
