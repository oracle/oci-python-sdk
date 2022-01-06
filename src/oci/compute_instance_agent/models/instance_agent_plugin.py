# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentPlugin(object):
    """
    The agent plugin
    """

    #: A constant which can be used with the status property of a InstanceAgentPlugin.
    #: This constant has a value of "RUNNING"
    STATUS_RUNNING = "RUNNING"

    #: A constant which can be used with the status property of a InstanceAgentPlugin.
    #: This constant has a value of "STOPPED"
    STATUS_STOPPED = "STOPPED"

    #: A constant which can be used with the status property of a InstanceAgentPlugin.
    #: This constant has a value of "NOT_SUPPORTED"
    STATUS_NOT_SUPPORTED = "NOT_SUPPORTED"

    #: A constant which can be used with the status property of a InstanceAgentPlugin.
    #: This constant has a value of "INVALID"
    STATUS_INVALID = "INVALID"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentPlugin object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this InstanceAgentPlugin.
        :type name: str

        :param status:
            The value to assign to the status property of this InstanceAgentPlugin.
            Allowed values for this property are: "RUNNING", "STOPPED", "NOT_SUPPORTED", "INVALID", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_last_updated_utc:
            The value to assign to the time_last_updated_utc property of this InstanceAgentPlugin.
        :type time_last_updated_utc: datetime

        :param message:
            The value to assign to the message property of this InstanceAgentPlugin.
        :type message: str

        """
        self.swagger_types = {
            'name': 'str',
            'status': 'str',
            'time_last_updated_utc': 'datetime',
            'message': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'status': 'status',
            'time_last_updated_utc': 'timeLastUpdatedUtc',
            'message': 'message'
        }

        self._name = None
        self._status = None
        self._time_last_updated_utc = None
        self._message = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this InstanceAgentPlugin.
        The plugin name


        :return: The name of this InstanceAgentPlugin.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InstanceAgentPlugin.
        The plugin name


        :param name: The name of this InstanceAgentPlugin.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this InstanceAgentPlugin.
        The plugin status Specified the plugin state on the instance * `RUNNING` - The plugin is in running state * `STOPPED` - The plugin is in stopped state * `NOT_SUPPORTED` - The plugin is not supported on this platform * `INVALID` - The plugin state is not recognizable by the service

        Allowed values for this property are: "RUNNING", "STOPPED", "NOT_SUPPORTED", "INVALID", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this InstanceAgentPlugin.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InstanceAgentPlugin.
        The plugin status Specified the plugin state on the instance * `RUNNING` - The plugin is in running state * `STOPPED` - The plugin is in stopped state * `NOT_SUPPORTED` - The plugin is not supported on this platform * `INVALID` - The plugin state is not recognizable by the service


        :param status: The status of this InstanceAgentPlugin.
        :type: str
        """
        allowed_values = ["RUNNING", "STOPPED", "NOT_SUPPORTED", "INVALID"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_last_updated_utc(self):
        """
        **[Required]** Gets the time_last_updated_utc of this InstanceAgentPlugin.
        The last update time of the plugin in UTC


        :return: The time_last_updated_utc of this InstanceAgentPlugin.
        :rtype: datetime
        """
        return self._time_last_updated_utc

    @time_last_updated_utc.setter
    def time_last_updated_utc(self, time_last_updated_utc):
        """
        Sets the time_last_updated_utc of this InstanceAgentPlugin.
        The last update time of the plugin in UTC


        :param time_last_updated_utc: The time_last_updated_utc of this InstanceAgentPlugin.
        :type: datetime
        """
        self._time_last_updated_utc = time_last_updated_utc

    @property
    def message(self):
        """
        Gets the message of this InstanceAgentPlugin.
        The optional message from the agent plugin


        :return: The message of this InstanceAgentPlugin.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InstanceAgentPlugin.
        The optional message from the agent plugin


        :param message: The message of this InstanceAgentPlugin.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
