# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PutLogsDetails(object):
    """
    The request body for the PutLogs request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PutLogsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param specversion:
            The value to assign to the specversion property of this PutLogsDetails.
        :type specversion: str

        :param log_entry_batches:
            The value to assign to the log_entry_batches property of this PutLogsDetails.
        :type log_entry_batches: list[oci.loggingingestion.models.LogEntryBatch]

        """
        self.swagger_types = {
            'specversion': 'str',
            'log_entry_batches': 'list[LogEntryBatch]'
        }

        self.attribute_map = {
            'specversion': 'specversion',
            'log_entry_batches': 'logEntryBatches'
        }

        self._specversion = None
        self._log_entry_batches = None

    @property
    def specversion(self):
        """
        **[Required]** Gets the specversion of this PutLogsDetails.
        Required for identifying the version of the data format being used.
        Permitted values include: \"1.0\"


        :return: The specversion of this PutLogsDetails.
        :rtype: str
        """
        return self._specversion

    @specversion.setter
    def specversion(self, specversion):
        """
        Sets the specversion of this PutLogsDetails.
        Required for identifying the version of the data format being used.
        Permitted values include: \"1.0\"


        :param specversion: The specversion of this PutLogsDetails.
        :type: str
        """
        self._specversion = specversion

    @property
    def log_entry_batches(self):
        """
        **[Required]** Gets the log_entry_batches of this PutLogsDetails.
        List of log-batches. Each batch has a single source, type and subject.


        :return: The log_entry_batches of this PutLogsDetails.
        :rtype: list[oci.loggingingestion.models.LogEntryBatch]
        """
        return self._log_entry_batches

    @log_entry_batches.setter
    def log_entry_batches(self, log_entry_batches):
        """
        Sets the log_entry_batches of this PutLogsDetails.
        List of log-batches. Each batch has a single source, type and subject.


        :param log_entry_batches: The log_entry_batches of this PutLogsDetails.
        :type: list[oci.loggingingestion.models.LogEntryBatch]
        """
        self._log_entry_batches = log_entry_batches

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
