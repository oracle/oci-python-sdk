# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchHistorySummary(object):
    """
    Patch history of this cluster.
    """

    #: A constant which can be used with the lifecycle_state property of a PatchHistorySummary.
    #: This constant has a value of "INSTALLING"
    LIFECYCLE_STATE_INSTALLING = "INSTALLING"

    #: A constant which can be used with the lifecycle_state property of a PatchHistorySummary.
    #: This constant has a value of "INSTALLED"
    LIFECYCLE_STATE_INSTALLED = "INSTALLED"

    #: A constant which can be used with the lifecycle_state property of a PatchHistorySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new PatchHistorySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this PatchHistorySummary.
        :type version: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PatchHistorySummary.
            Allowed values for this property are: "INSTALLING", "INSTALLED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_updated:
            The value to assign to the time_updated property of this PatchHistorySummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'version': 'str',
            'lifecycle_state': 'str',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'version': 'version',
            'lifecycle_state': 'lifecycleState',
            'time_updated': 'timeUpdated'
        }

        self._version = None
        self._lifecycle_state = None
        self._time_updated = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this PatchHistorySummary.
        The version of the patch.


        :return: The version of this PatchHistorySummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PatchHistorySummary.
        The version of the patch.


        :param version: The version of this PatchHistorySummary.
        :type: str
        """
        self._version = version

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PatchHistorySummary.
        The status of this patch.

        Allowed values for this property are: "INSTALLING", "INSTALLED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PatchHistorySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PatchHistorySummary.
        The status of this patch.


        :param lifecycle_state: The lifecycle_state of this PatchHistorySummary.
        :type: str
        """
        allowed_values = ["INSTALLING", "INSTALLED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this PatchHistorySummary.
        The time when the patch history was last updated.


        :return: The time_updated of this PatchHistorySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this PatchHistorySummary.
        The time when the patch history was last updated.


        :param time_updated: The time_updated of this PatchHistorySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
