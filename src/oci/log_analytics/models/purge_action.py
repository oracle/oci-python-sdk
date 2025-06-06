# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601

from .action import Action
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PurgeAction(Action):
    """
    Purge action for scheduled task.
    """

    #: A constant which can be used with the data_type property of a PurgeAction.
    #: This constant has a value of "LOG"
    DATA_TYPE_LOG = "LOG"

    #: A constant which can be used with the data_type property of a PurgeAction.
    #: This constant has a value of "LOOKUP"
    DATA_TYPE_LOOKUP = "LOOKUP"

    def __init__(self, **kwargs):
        """
        Initializes a new PurgeAction object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.PurgeAction.type` attribute
        of this class is ``PURGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this PurgeAction.
            Allowed values for this property are: "STREAM", "PURGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param query_string:
            The value to assign to the query_string property of this PurgeAction.
        :type query_string: str

        :param data_type:
            The value to assign to the data_type property of this PurgeAction.
            Allowed values for this property are: "LOG", "LOOKUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_type: str

        :param purge_duration:
            The value to assign to the purge_duration property of this PurgeAction.
        :type purge_duration: str

        :param purge_compartment_id:
            The value to assign to the purge_compartment_id property of this PurgeAction.
        :type purge_compartment_id: str

        :param compartment_id_in_subtree:
            The value to assign to the compartment_id_in_subtree property of this PurgeAction.
        :type compartment_id_in_subtree: bool

        """
        self.swagger_types = {
            'type': 'str',
            'query_string': 'str',
            'data_type': 'str',
            'purge_duration': 'str',
            'purge_compartment_id': 'str',
            'compartment_id_in_subtree': 'bool'
        }
        self.attribute_map = {
            'type': 'type',
            'query_string': 'queryString',
            'data_type': 'dataType',
            'purge_duration': 'purgeDuration',
            'purge_compartment_id': 'purgeCompartmentId',
            'compartment_id_in_subtree': 'compartmentIdInSubtree'
        }
        self._type = None
        self._query_string = None
        self._data_type = None
        self._purge_duration = None
        self._purge_compartment_id = None
        self._compartment_id_in_subtree = None
        self._type = 'PURGE'

    @property
    def query_string(self):
        """
        **[Required]** Gets the query_string of this PurgeAction.
        Purge query string.


        :return: The query_string of this PurgeAction.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """
        Sets the query_string of this PurgeAction.
        Purge query string.


        :param query_string: The query_string of this PurgeAction.
        :type: str
        """
        self._query_string = query_string

    @property
    def data_type(self):
        """
        **[Required]** Gets the data_type of this PurgeAction.
        the type of the log data to be purged

        Allowed values for this property are: "LOG", "LOOKUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_type of this PurgeAction.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this PurgeAction.
        the type of the log data to be purged


        :param data_type: The data_type of this PurgeAction.
        :type: str
        """
        allowed_values = ["LOG", "LOOKUP"]
        if not value_allowed_none_or_none_sentinel(data_type, allowed_values):
            data_type = 'UNKNOWN_ENUM_VALUE'
        self._data_type = data_type

    @property
    def purge_duration(self):
        """
        **[Required]** Gets the purge_duration of this PurgeAction.
        The duration of data to be retained, which is used to
        calculate the timeDataEnded when the task fires.
        The value should be negative.
        Purge duration in ISO 8601 extended format as described in
        https://en.wikipedia.org/wiki/ISO_8601#Durations.
        The largest supported unit is D, e.g. -P365D (not -P1Y) or -P14D (not -P2W).


        :return: The purge_duration of this PurgeAction.
        :rtype: str
        """
        return self._purge_duration

    @purge_duration.setter
    def purge_duration(self, purge_duration):
        """
        Sets the purge_duration of this PurgeAction.
        The duration of data to be retained, which is used to
        calculate the timeDataEnded when the task fires.
        The value should be negative.
        Purge duration in ISO 8601 extended format as described in
        https://en.wikipedia.org/wiki/ISO_8601#Durations.
        The largest supported unit is D, e.g. -P365D (not -P1Y) or -P14D (not -P2W).


        :param purge_duration: The purge_duration of this PurgeAction.
        :type: str
        """
        self._purge_duration = purge_duration

    @property
    def purge_compartment_id(self):
        """
        **[Required]** Gets the purge_compartment_id of this PurgeAction.
        the compartment OCID under which the data will be purged


        :return: The purge_compartment_id of this PurgeAction.
        :rtype: str
        """
        return self._purge_compartment_id

    @purge_compartment_id.setter
    def purge_compartment_id(self, purge_compartment_id):
        """
        Sets the purge_compartment_id of this PurgeAction.
        the compartment OCID under which the data will be purged


        :param purge_compartment_id: The purge_compartment_id of this PurgeAction.
        :type: str
        """
        self._purge_compartment_id = purge_compartment_id

    @property
    def compartment_id_in_subtree(self):
        """
        Gets the compartment_id_in_subtree of this PurgeAction.
        if true, purge child compartments data


        :return: The compartment_id_in_subtree of this PurgeAction.
        :rtype: bool
        """
        return self._compartment_id_in_subtree

    @compartment_id_in_subtree.setter
    def compartment_id_in_subtree(self, compartment_id_in_subtree):
        """
        Sets the compartment_id_in_subtree of this PurgeAction.
        if true, purge child compartments data


        :param compartment_id_in_subtree: The compartment_id_in_subtree of this PurgeAction.
        :type: bool
        """
        self._compartment_id_in_subtree = compartment_id_in_subtree

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
