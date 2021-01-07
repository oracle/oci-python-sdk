# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EstimatePurgeDataSizeDetails(object):
    """
    This is the input used to estimate the size of data that might be purged
    """

    #: A constant which can be used with the data_type property of a EstimatePurgeDataSizeDetails.
    #: This constant has a value of "LOG"
    DATA_TYPE_LOG = "LOG"

    #: A constant which can be used with the data_type property of a EstimatePurgeDataSizeDetails.
    #: This constant has a value of "LOOKUP"
    DATA_TYPE_LOOKUP = "LOOKUP"

    def __init__(self, **kwargs):
        """
        Initializes a new EstimatePurgeDataSizeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this EstimatePurgeDataSizeDetails.
        :type compartment_id: str

        :param compartment_id_in_subtree:
            The value to assign to the compartment_id_in_subtree property of this EstimatePurgeDataSizeDetails.
        :type compartment_id_in_subtree: bool

        :param time_data_ended:
            The value to assign to the time_data_ended property of this EstimatePurgeDataSizeDetails.
        :type time_data_ended: datetime

        :param purge_query_string:
            The value to assign to the purge_query_string property of this EstimatePurgeDataSizeDetails.
        :type purge_query_string: str

        :param data_type:
            The value to assign to the data_type property of this EstimatePurgeDataSizeDetails.
            Allowed values for this property are: "LOG", "LOOKUP"
        :type data_type: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'compartment_id_in_subtree': 'bool',
            'time_data_ended': 'datetime',
            'purge_query_string': 'str',
            'data_type': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'compartment_id_in_subtree': 'compartmentIdInSubtree',
            'time_data_ended': 'timeDataEnded',
            'purge_query_string': 'purgeQueryString',
            'data_type': 'dataType'
        }

        self._compartment_id = None
        self._compartment_id_in_subtree = None
        self._time_data_ended = None
        self._purge_query_string = None
        self._data_type = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EstimatePurgeDataSizeDetails.
        This is the compartment OCID under which the data will be purged


        :return: The compartment_id of this EstimatePurgeDataSizeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EstimatePurgeDataSizeDetails.
        This is the compartment OCID under which the data will be purged


        :param compartment_id: The compartment_id of this EstimatePurgeDataSizeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compartment_id_in_subtree(self):
        """
        Gets the compartment_id_in_subtree of this EstimatePurgeDataSizeDetails.
        If true, purge child compartments data


        :return: The compartment_id_in_subtree of this EstimatePurgeDataSizeDetails.
        :rtype: bool
        """
        return self._compartment_id_in_subtree

    @compartment_id_in_subtree.setter
    def compartment_id_in_subtree(self, compartment_id_in_subtree):
        """
        Sets the compartment_id_in_subtree of this EstimatePurgeDataSizeDetails.
        If true, purge child compartments data


        :param compartment_id_in_subtree: The compartment_id_in_subtree of this EstimatePurgeDataSizeDetails.
        :type: bool
        """
        self._compartment_id_in_subtree = compartment_id_in_subtree

    @property
    def time_data_ended(self):
        """
        **[Required]** Gets the time_data_ended of this EstimatePurgeDataSizeDetails.
        This is the time before which data will be purged


        :return: The time_data_ended of this EstimatePurgeDataSizeDetails.
        :rtype: datetime
        """
        return self._time_data_ended

    @time_data_ended.setter
    def time_data_ended(self, time_data_ended):
        """
        Sets the time_data_ended of this EstimatePurgeDataSizeDetails.
        This is the time before which data will be purged


        :param time_data_ended: The time_data_ended of this EstimatePurgeDataSizeDetails.
        :type: datetime
        """
        self._time_data_ended = time_data_ended

    @property
    def purge_query_string(self):
        """
        Gets the purge_query_string of this EstimatePurgeDataSizeDetails.
        This is the solr data filter query, '*' means all


        :return: The purge_query_string of this EstimatePurgeDataSizeDetails.
        :rtype: str
        """
        return self._purge_query_string

    @purge_query_string.setter
    def purge_query_string(self, purge_query_string):
        """
        Sets the purge_query_string of this EstimatePurgeDataSizeDetails.
        This is the solr data filter query, '*' means all


        :param purge_query_string: The purge_query_string of this EstimatePurgeDataSizeDetails.
        :type: str
        """
        self._purge_query_string = purge_query_string

    @property
    def data_type(self):
        """
        Gets the data_type of this EstimatePurgeDataSizeDetails.
        This is the type of the log data to be purged

        Allowed values for this property are: "LOG", "LOOKUP"


        :return: The data_type of this EstimatePurgeDataSizeDetails.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this EstimatePurgeDataSizeDetails.
        This is the type of the log data to be purged


        :param data_type: The data_type of this EstimatePurgeDataSizeDetails.
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
