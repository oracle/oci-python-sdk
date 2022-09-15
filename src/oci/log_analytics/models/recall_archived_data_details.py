# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecallArchivedDataDetails(object):
    """
    This is the input used to recall archived data
    """

    #: A constant which can be used with the data_type property of a RecallArchivedDataDetails.
    #: This constant has a value of "LOG"
    DATA_TYPE_LOG = "LOG"

    #: A constant which can be used with the data_type property of a RecallArchivedDataDetails.
    #: This constant has a value of "LOOKUP"
    DATA_TYPE_LOOKUP = "LOOKUP"

    def __init__(self, **kwargs):
        """
        Initializes a new RecallArchivedDataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this RecallArchivedDataDetails.
        :type compartment_id: str

        :param time_data_ended:
            The value to assign to the time_data_ended property of this RecallArchivedDataDetails.
        :type time_data_ended: datetime

        :param time_data_started:
            The value to assign to the time_data_started property of this RecallArchivedDataDetails.
        :type time_data_started: datetime

        :param data_type:
            The value to assign to the data_type property of this RecallArchivedDataDetails.
            Allowed values for this property are: "LOG", "LOOKUP"
        :type data_type: str

        :param log_sets:
            The value to assign to the log_sets property of this RecallArchivedDataDetails.
        :type log_sets: str

        :param query:
            The value to assign to the query property of this RecallArchivedDataDetails.
        :type query: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'time_data_ended': 'datetime',
            'time_data_started': 'datetime',
            'data_type': 'str',
            'log_sets': 'str',
            'query': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'time_data_ended': 'timeDataEnded',
            'time_data_started': 'timeDataStarted',
            'data_type': 'dataType',
            'log_sets': 'logSets',
            'query': 'query'
        }

        self._compartment_id = None
        self._time_data_ended = None
        self._time_data_started = None
        self._data_type = None
        self._log_sets = None
        self._query = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RecallArchivedDataDetails.
        This is the compartment OCID for permission checking


        :return: The compartment_id of this RecallArchivedDataDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RecallArchivedDataDetails.
        This is the compartment OCID for permission checking


        :param compartment_id: The compartment_id of this RecallArchivedDataDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_data_ended(self):
        """
        **[Required]** Gets the time_data_ended of this RecallArchivedDataDetails.
        This is the end of the time interval


        :return: The time_data_ended of this RecallArchivedDataDetails.
        :rtype: datetime
        """
        return self._time_data_ended

    @time_data_ended.setter
    def time_data_ended(self, time_data_ended):
        """
        Sets the time_data_ended of this RecallArchivedDataDetails.
        This is the end of the time interval


        :param time_data_ended: The time_data_ended of this RecallArchivedDataDetails.
        :type: datetime
        """
        self._time_data_ended = time_data_ended

    @property
    def time_data_started(self):
        """
        **[Required]** Gets the time_data_started of this RecallArchivedDataDetails.
        This is the start of the time interval


        :return: The time_data_started of this RecallArchivedDataDetails.
        :rtype: datetime
        """
        return self._time_data_started

    @time_data_started.setter
    def time_data_started(self, time_data_started):
        """
        Sets the time_data_started of this RecallArchivedDataDetails.
        This is the start of the time interval


        :param time_data_started: The time_data_started of this RecallArchivedDataDetails.
        :type: datetime
        """
        self._time_data_started = time_data_started

    @property
    def data_type(self):
        """
        Gets the data_type of this RecallArchivedDataDetails.
        This is the type of the log data to be recalled

        Allowed values for this property are: "LOG", "LOOKUP"


        :return: The data_type of this RecallArchivedDataDetails.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this RecallArchivedDataDetails.
        This is the type of the log data to be recalled


        :param data_type: The data_type of this RecallArchivedDataDetails.
        :type: str
        """
        allowed_values = ["LOG", "LOOKUP"]
        if not value_allowed_none_or_none_sentinel(data_type, allowed_values):
            raise ValueError(
                "Invalid value for `data_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._data_type = data_type

    @property
    def log_sets(self):
        """
        Gets the log_sets of this RecallArchivedDataDetails.
        This is a list of comma-separated log sets that recalled data belongs to.


        :return: The log_sets of this RecallArchivedDataDetails.
        :rtype: str
        """
        return self._log_sets

    @log_sets.setter
    def log_sets(self, log_sets):
        """
        Sets the log_sets of this RecallArchivedDataDetails.
        This is a list of comma-separated log sets that recalled data belongs to.


        :param log_sets: The log_sets of this RecallArchivedDataDetails.
        :type: str
        """
        self._log_sets = log_sets

    @property
    def query(self):
        """
        Gets the query of this RecallArchivedDataDetails.
        This is the query that identifies the recalled data.


        :return: The query of this RecallArchivedDataDetails.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this RecallArchivedDataDetails.
        This is the query that identifies the recalled data.


        :param query: The query of this RecallArchivedDataDetails.
        :type: str
        """
        self._query = query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
