# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecallArchivedDataDetails(object):
    """
    Work request details to recall archived data
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

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'time_data_ended': 'datetime',
            'time_data_started': 'datetime',
            'data_type': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'time_data_ended': 'timeDataEnded',
            'time_data_started': 'timeDataStarted',
            'data_type': 'dataType'
        }

        self._compartment_id = None
        self._time_data_ended = None
        self._time_data_started = None
        self._data_type = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RecallArchivedDataDetails.
        the compartment OCID for permission checking


        :return: The compartment_id of this RecallArchivedDataDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RecallArchivedDataDetails.
        the compartment OCID for permission checking


        :param compartment_id: The compartment_id of this RecallArchivedDataDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_data_ended(self):
        """
        **[Required]** Gets the time_data_ended of this RecallArchivedDataDetails.
        the end of the time interval


        :return: The time_data_ended of this RecallArchivedDataDetails.
        :rtype: datetime
        """
        return self._time_data_ended

    @time_data_ended.setter
    def time_data_ended(self, time_data_ended):
        """
        Sets the time_data_ended of this RecallArchivedDataDetails.
        the end of the time interval


        :param time_data_ended: The time_data_ended of this RecallArchivedDataDetails.
        :type: datetime
        """
        self._time_data_ended = time_data_ended

    @property
    def time_data_started(self):
        """
        **[Required]** Gets the time_data_started of this RecallArchivedDataDetails.
        the start of the time interval


        :return: The time_data_started of this RecallArchivedDataDetails.
        :rtype: datetime
        """
        return self._time_data_started

    @time_data_started.setter
    def time_data_started(self, time_data_started):
        """
        Sets the time_data_started of this RecallArchivedDataDetails.
        the start of the time interval


        :param time_data_started: The time_data_started of this RecallArchivedDataDetails.
        :type: datetime
        """
        self._time_data_started = time_data_started

    @property
    def data_type(self):
        """
        Gets the data_type of this RecallArchivedDataDetails.
        the type of the log data to be purged

        Allowed values for this property are: "LOG", "LOOKUP"


        :return: The data_type of this RecallArchivedDataDetails.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this RecallArchivedDataDetails.
        the type of the log data to be purged


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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
