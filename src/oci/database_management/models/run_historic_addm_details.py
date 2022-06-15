# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RunHistoricAddmDetails(object):
    """
    The details of the ADDM task, which include the beginning and ending AWR snapshot IDs.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RunHistoricAddmDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param start_snapshot_id:
            The value to assign to the start_snapshot_id property of this RunHistoricAddmDetails.
        :type start_snapshot_id: int

        :param end_snapshot_id:
            The value to assign to the end_snapshot_id property of this RunHistoricAddmDetails.
        :type end_snapshot_id: int

        """
        self.swagger_types = {
            'start_snapshot_id': 'int',
            'end_snapshot_id': 'int'
        }

        self.attribute_map = {
            'start_snapshot_id': 'startSnapshotId',
            'end_snapshot_id': 'endSnapshotId'
        }

        self._start_snapshot_id = None
        self._end_snapshot_id = None

    @property
    def start_snapshot_id(self):
        """
        **[Required]** Gets the start_snapshot_id of this RunHistoricAddmDetails.
        The ID number of the beginning AWR snapshot.


        :return: The start_snapshot_id of this RunHistoricAddmDetails.
        :rtype: int
        """
        return self._start_snapshot_id

    @start_snapshot_id.setter
    def start_snapshot_id(self, start_snapshot_id):
        """
        Sets the start_snapshot_id of this RunHistoricAddmDetails.
        The ID number of the beginning AWR snapshot.


        :param start_snapshot_id: The start_snapshot_id of this RunHistoricAddmDetails.
        :type: int
        """
        self._start_snapshot_id = start_snapshot_id

    @property
    def end_snapshot_id(self):
        """
        **[Required]** Gets the end_snapshot_id of this RunHistoricAddmDetails.
        The ID of the ending AWR snapshot.


        :return: The end_snapshot_id of this RunHistoricAddmDetails.
        :rtype: int
        """
        return self._end_snapshot_id

    @end_snapshot_id.setter
    def end_snapshot_id(self, end_snapshot_id):
        """
        Sets the end_snapshot_id of this RunHistoricAddmDetails.
        The ID of the ending AWR snapshot.


        :param end_snapshot_id: The end_snapshot_id of this RunHistoricAddmDetails.
        :type: int
        """
        self._end_snapshot_id = end_snapshot_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
