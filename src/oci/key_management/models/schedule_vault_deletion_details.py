# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleVaultDeletionDetails(object):
    """
    Details for scheduling Vault deletion
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleVaultDeletionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this ScheduleVaultDeletionDetails.
        :type time_of_deletion: datetime

        """
        self.swagger_types = {
            'time_of_deletion': 'datetime'
        }

        self.attribute_map = {
            'time_of_deletion': 'timeOfDeletion'
        }

        self._time_of_deletion = None

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this ScheduleVaultDeletionDetails.
        An optional property to indicate the deletion time of the Vault.
        The time format should comply with RFC-3339 standards. This time must be between 7 to 30 days from the time
        when the request is received. If the property is missing, it will be set to 30 days from request time by default.


        :return: The time_of_deletion of this ScheduleVaultDeletionDetails.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this ScheduleVaultDeletionDetails.
        An optional property to indicate the deletion time of the Vault.
        The time format should comply with RFC-3339 standards. This time must be between 7 to 30 days from the time
        when the request is received. If the property is missing, it will be set to 30 days from request time by default.


        :param time_of_deletion: The time_of_deletion of this ScheduleVaultDeletionDetails.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
