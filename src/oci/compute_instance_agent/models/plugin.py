# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180530


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Plugin(object):
    """
    An Oracle Cloud Agent plugin.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Plugin object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Plugin.
        :type name: str

        :param version:
            The value to assign to the version property of this Plugin.
        :type version: str

        :param status:
            The value to assign to the status property of this Plugin.
        :type status: str

        :param last_update_time:
            The value to assign to the last_update_time property of this Plugin.
        :type last_update_time: datetime

        :param message:
            The value to assign to the message property of this Plugin.
        :type message: str

        """
        self.swagger_types = {
            'name': 'str',
            'version': 'str',
            'status': 'str',
            'last_update_time': 'datetime',
            'message': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'status': 'status',
            'last_update_time': 'lastUpdateTime',
            'message': 'message'
        }
        self._name = None
        self._version = None
        self._status = None
        self._last_update_time = None
        self._message = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Plugin.
        The plugin name.


        :return: The name of this Plugin.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Plugin.
        The plugin name.


        :param name: The name of this Plugin.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this Plugin.
        The plugin version.


        :return: The version of this Plugin.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Plugin.
        The plugin version.


        :param version: The version of this Plugin.
        :type: str
        """
        self._version = version

    @property
    def status(self):
        """
        **[Required]** Gets the status of this Plugin.
        The plugin status.


        :return: The status of this Plugin.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Plugin.
        The plugin status.


        :param status: The status of this Plugin.
        :type: str
        """
        self._status = status

    @property
    def last_update_time(self):
        """
        Gets the last_update_time of this Plugin.
        The last updated time of the plugin, in UTC.


        :return: The last_update_time of this Plugin.
        :rtype: datetime
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """
        Sets the last_update_time of this Plugin.
        The last updated time of the plugin, in UTC.


        :param last_update_time: The last_update_time of this Plugin.
        :type: datetime
        """
        self._last_update_time = last_update_time

    @property
    def message(self):
        """
        Gets the message of this Plugin.
        An optional message from the plugin.


        :return: The message of this Plugin.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Plugin.
        An optional message from the plugin.


        :param message: The message of this Plugin.
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
