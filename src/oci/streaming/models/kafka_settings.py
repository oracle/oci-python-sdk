# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KafkaSettings(object):
    """
    Settings for the Kafka compatibility layer.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KafkaSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bootstrap_servers:
            The value to assign to the bootstrap_servers property of this KafkaSettings.
        :type bootstrap_servers: str

        :param auto_create_topics_enable:
            The value to assign to the auto_create_topics_enable property of this KafkaSettings.
        :type auto_create_topics_enable: bool

        :param log_retention_hours:
            The value to assign to the log_retention_hours property of this KafkaSettings.
        :type log_retention_hours: int

        :param num_partitions:
            The value to assign to the num_partitions property of this KafkaSettings.
        :type num_partitions: int

        """
        self.swagger_types = {
            'bootstrap_servers': 'str',
            'auto_create_topics_enable': 'bool',
            'log_retention_hours': 'int',
            'num_partitions': 'int'
        }

        self.attribute_map = {
            'bootstrap_servers': 'bootstrapServers',
            'auto_create_topics_enable': 'autoCreateTopicsEnable',
            'log_retention_hours': 'logRetentionHours',
            'num_partitions': 'numPartitions'
        }

        self._bootstrap_servers = None
        self._auto_create_topics_enable = None
        self._log_retention_hours = None
        self._num_partitions = None

    @property
    def bootstrap_servers(self):
        """
        Gets the bootstrap_servers of this KafkaSettings.
        Bootstrap servers.


        :return: The bootstrap_servers of this KafkaSettings.
        :rtype: str
        """
        return self._bootstrap_servers

    @bootstrap_servers.setter
    def bootstrap_servers(self, bootstrap_servers):
        """
        Sets the bootstrap_servers of this KafkaSettings.
        Bootstrap servers.


        :param bootstrap_servers: The bootstrap_servers of this KafkaSettings.
        :type: str
        """
        self._bootstrap_servers = bootstrap_servers

    @property
    def auto_create_topics_enable(self):
        """
        Gets the auto_create_topics_enable of this KafkaSettings.
        Enable auto creation of topic on the server.


        :return: The auto_create_topics_enable of this KafkaSettings.
        :rtype: bool
        """
        return self._auto_create_topics_enable

    @auto_create_topics_enable.setter
    def auto_create_topics_enable(self, auto_create_topics_enable):
        """
        Sets the auto_create_topics_enable of this KafkaSettings.
        Enable auto creation of topic on the server.


        :param auto_create_topics_enable: The auto_create_topics_enable of this KafkaSettings.
        :type: bool
        """
        self._auto_create_topics_enable = auto_create_topics_enable

    @property
    def log_retention_hours(self):
        """
        Gets the log_retention_hours of this KafkaSettings.
        The number of hours to keep a log file before deleting it (in hours).


        :return: The log_retention_hours of this KafkaSettings.
        :rtype: int
        """
        return self._log_retention_hours

    @log_retention_hours.setter
    def log_retention_hours(self, log_retention_hours):
        """
        Sets the log_retention_hours of this KafkaSettings.
        The number of hours to keep a log file before deleting it (in hours).


        :param log_retention_hours: The log_retention_hours of this KafkaSettings.
        :type: int
        """
        self._log_retention_hours = log_retention_hours

    @property
    def num_partitions(self):
        """
        Gets the num_partitions of this KafkaSettings.
        The default number of log partitions per topic.


        :return: The num_partitions of this KafkaSettings.
        :rtype: int
        """
        return self._num_partitions

    @num_partitions.setter
    def num_partitions(self, num_partitions):
        """
        Sets the num_partitions of this KafkaSettings.
        The default number of log partitions per topic.


        :param num_partitions: The num_partitions of this KafkaSettings.
        :type: int
        """
        self._num_partitions = num_partitions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
