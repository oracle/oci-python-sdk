# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitorResultData(object):
    """
    Details of the monitor result data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitorResultData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this MonitorResultData.
        :type name: str

        :param byte_content:
            The value to assign to the byte_content property of this MonitorResultData.
        :type byte_content: str

        :param string_content:
            The value to assign to the string_content property of this MonitorResultData.
        :type string_content: str

        :param timestamp:
            The value to assign to the timestamp property of this MonitorResultData.
        :type timestamp: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'byte_content': 'str',
            'string_content': 'str',
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'byte_content': 'byteContent',
            'string_content': 'stringContent',
            'timestamp': 'timestamp'
        }

        self._name = None
        self._byte_content = None
        self._string_content = None
        self._timestamp = None

    @property
    def name(self):
        """
        Gets the name of this MonitorResultData.
        Name of the data.


        :return: The name of this MonitorResultData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MonitorResultData.
        Name of the data.


        :param name: The name of this MonitorResultData.
        :type: str
        """
        self._name = name

    @property
    def byte_content(self):
        """
        Gets the byte_content of this MonitorResultData.
        Data content in byte format.
        Example: Zip or Screenshot.


        :return: The byte_content of this MonitorResultData.
        :rtype: str
        """
        return self._byte_content

    @byte_content.setter
    def byte_content(self, byte_content):
        """
        Sets the byte_content of this MonitorResultData.
        Data content in byte format.
        Example: Zip or Screenshot.


        :param byte_content: The byte_content of this MonitorResultData.
        :type: str
        """
        self._byte_content = byte_content

    @property
    def string_content(self):
        """
        Gets the string_content of this MonitorResultData.
        Data content in string format.
        Example: HAR.


        :return: The string_content of this MonitorResultData.
        :rtype: str
        """
        return self._string_content

    @string_content.setter
    def string_content(self, string_content):
        """
        Sets the string_content of this MonitorResultData.
        Data content in string format.
        Example: HAR.


        :param string_content: The string_content of this MonitorResultData.
        :type: str
        """
        self._string_content = string_content

    @property
    def timestamp(self):
        """
        Gets the timestamp of this MonitorResultData.
        The time when the data was generated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The timestamp of this MonitorResultData.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this MonitorResultData.
        The time when the data was generated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param timestamp: The timestamp of this MonitorResultData.
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
