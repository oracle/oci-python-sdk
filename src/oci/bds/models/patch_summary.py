# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchSummary(object):
    """
    The patch that is currently available for the cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PatchSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this PatchSummary.
        :type version: str

        :param time_released:
            The value to assign to the time_released property of this PatchSummary.
        :type time_released: datetime

        """
        self.swagger_types = {
            'version': 'str',
            'time_released': 'datetime'
        }

        self.attribute_map = {
            'version': 'version',
            'time_released': 'timeReleased'
        }

        self._version = None
        self._time_released = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this PatchSummary.
        The version of the patch.


        :return: The version of this PatchSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PatchSummary.
        The version of the patch.


        :param version: The version of this PatchSummary.
        :type: str
        """
        self._version = version

    @property
    def time_released(self):
        """
        **[Required]** Gets the time_released of this PatchSummary.
        The time when the patch was released.


        :return: The time_released of this PatchSummary.
        :rtype: datetime
        """
        return self._time_released

    @time_released.setter
    def time_released(self, time_released):
        """
        Sets the time_released of this PatchSummary.
        The time when the patch was released.


        :param time_released: The time_released of this PatchSummary.
        :type: datetime
        """
        self._time_released = time_released

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
