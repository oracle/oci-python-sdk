# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseConnectionStrings(object):
    """
    Connection strings to connect to an Oracle Autonomous Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseConnectionStrings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param all_connection_strings:
            The value to assign to the all_connection_strings property of this AutonomousDatabaseConnectionStrings.
        :type all_connection_strings: dict(str, str)

        :param high:
            The value to assign to the high property of this AutonomousDatabaseConnectionStrings.
        :type high: str

        :param low:
            The value to assign to the low property of this AutonomousDatabaseConnectionStrings.
        :type low: str

        :param medium:
            The value to assign to the medium property of this AutonomousDatabaseConnectionStrings.
        :type medium: str

        """
        self.swagger_types = {
            'all_connection_strings': 'dict(str, str)',
            'high': 'str',
            'low': 'str',
            'medium': 'str'
        }

        self.attribute_map = {
            'all_connection_strings': 'allConnectionStrings',
            'high': 'high',
            'low': 'low',
            'medium': 'medium'
        }

        self._all_connection_strings = None
        self._high = None
        self._low = None
        self._medium = None

    @property
    def all_connection_strings(self):
        """
        Gets the all_connection_strings of this AutonomousDatabaseConnectionStrings.
        All connection strings to use to connect to the Autonomous Database.


        :return: The all_connection_strings of this AutonomousDatabaseConnectionStrings.
        :rtype: dict(str, str)
        """
        return self._all_connection_strings

    @all_connection_strings.setter
    def all_connection_strings(self, all_connection_strings):
        """
        Sets the all_connection_strings of this AutonomousDatabaseConnectionStrings.
        All connection strings to use to connect to the Autonomous Database.


        :param all_connection_strings: The all_connection_strings of this AutonomousDatabaseConnectionStrings.
        :type: dict(str, str)
        """
        self._all_connection_strings = all_connection_strings

    @property
    def high(self):
        """
        Gets the high of this AutonomousDatabaseConnectionStrings.
        The High database service provides the highest level of resources to each SQL statement resulting in the highest performance, but supports the fewest number of concurrent SQL statements.


        :return: The high of this AutonomousDatabaseConnectionStrings.
        :rtype: str
        """
        return self._high

    @high.setter
    def high(self, high):
        """
        Sets the high of this AutonomousDatabaseConnectionStrings.
        The High database service provides the highest level of resources to each SQL statement resulting in the highest performance, but supports the fewest number of concurrent SQL statements.


        :param high: The high of this AutonomousDatabaseConnectionStrings.
        :type: str
        """
        self._high = high

    @property
    def low(self):
        """
        Gets the low of this AutonomousDatabaseConnectionStrings.
        The Low database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.


        :return: The low of this AutonomousDatabaseConnectionStrings.
        :rtype: str
        """
        return self._low

    @low.setter
    def low(self, low):
        """
        Sets the low of this AutonomousDatabaseConnectionStrings.
        The Low database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.


        :param low: The low of this AutonomousDatabaseConnectionStrings.
        :type: str
        """
        self._low = low

    @property
    def medium(self):
        """
        Gets the medium of this AutonomousDatabaseConnectionStrings.
        The Medium database service provides a lower level of resources to each SQL statement potentially resulting a lower level of performance, but supports more concurrent SQL statements.


        :return: The medium of this AutonomousDatabaseConnectionStrings.
        :rtype: str
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """
        Sets the medium of this AutonomousDatabaseConnectionStrings.
        The Medium database service provides a lower level of resources to each SQL statement potentially resulting a lower level of performance, but supports more concurrent SQL statements.


        :param medium: The medium of this AutonomousDatabaseConnectionStrings.
        :type: str
        """
        self._medium = medium

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
