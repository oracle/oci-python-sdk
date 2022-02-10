# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AggregatedSnapshot(object):
    """
    Aggregated snapshots of all spans.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AggregatedSnapshot object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param details:
            The value to assign to the details property of this AggregatedSnapshot.
        :type details: list[oci.apm_traces.models.SnapshotDetail]

        :param aggregated_stack_traces:
            The value to assign to the aggregated_stack_traces property of this AggregatedSnapshot.
        :type aggregated_stack_traces: list[oci.apm_traces.models.AggregatedStackTrace]

        """
        self.swagger_types = {
            'details': 'list[SnapshotDetail]',
            'aggregated_stack_traces': 'list[AggregatedStackTrace]'
        }

        self.attribute_map = {
            'details': 'details',
            'aggregated_stack_traces': 'aggregatedStackTraces'
        }

        self._details = None
        self._aggregated_stack_traces = None

    @property
    def details(self):
        """
        **[Required]** Gets the details of this AggregatedSnapshot.
        Aggregated snapshot details.


        :return: The details of this AggregatedSnapshot.
        :rtype: list[oci.apm_traces.models.SnapshotDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this AggregatedSnapshot.
        Aggregated snapshot details.


        :param details: The details of this AggregatedSnapshot.
        :type: list[oci.apm_traces.models.SnapshotDetail]
        """
        self._details = details

    @property
    def aggregated_stack_traces(self):
        """
        **[Required]** Gets the aggregated_stack_traces of this AggregatedSnapshot.
        List of aggregated stack trace.


        :return: The aggregated_stack_traces of this AggregatedSnapshot.
        :rtype: list[oci.apm_traces.models.AggregatedStackTrace]
        """
        return self._aggregated_stack_traces

    @aggregated_stack_traces.setter
    def aggregated_stack_traces(self, aggregated_stack_traces):
        """
        Sets the aggregated_stack_traces of this AggregatedSnapshot.
        List of aggregated stack trace.


        :param aggregated_stack_traces: The aggregated_stack_traces of this AggregatedSnapshot.
        :type: list[oci.apm_traces.models.AggregatedStackTrace]
        """
        self._aggregated_stack_traces = aggregated_stack_traces

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
