# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RestoreAutonomousDatabaseDetails(object):
    """
    Details to restore an Oracle Autonomous Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RestoreAutonomousDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param timestamp:
            The value to assign to the timestamp property of this RestoreAutonomousDatabaseDetails.
        :type timestamp: datetime

        """
        self.swagger_types = {
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'timestamp': 'timestamp'
        }

        self._timestamp = None

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this RestoreAutonomousDatabaseDetails.
        The time to restore the database to.


        :return: The timestamp of this RestoreAutonomousDatabaseDetails.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this RestoreAutonomousDatabaseDetails.
        The time to restore the database to.


        :param timestamp: The timestamp of this RestoreAutonomousDatabaseDetails.
        :type: datetime
        """
        self._timestamp = timestamp

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
