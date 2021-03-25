# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeleteLogAnalyticsAssociation(object):
    """
    DeleteLogAnalyticsAssociation
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeleteLogAnalyticsAssociation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param agent_id:
            The value to assign to the agent_id property of this DeleteLogAnalyticsAssociation.
        :type agent_id: str

        :param source_name:
            The value to assign to the source_name property of this DeleteLogAnalyticsAssociation.
        :type source_name: str

        :param source_type_name:
            The value to assign to the source_type_name property of this DeleteLogAnalyticsAssociation.
        :type source_type_name: str

        :param entity_id:
            The value to assign to the entity_id property of this DeleteLogAnalyticsAssociation.
        :type entity_id: str

        :param entity_type_name:
            The value to assign to the entity_type_name property of this DeleteLogAnalyticsAssociation.
        :type entity_type_name: str

        :param host:
            The value to assign to the host property of this DeleteLogAnalyticsAssociation.
        :type host: str

        :param log_group_id:
            The value to assign to the log_group_id property of this DeleteLogAnalyticsAssociation.
        :type log_group_id: str

        """
        self.swagger_types = {
            'agent_id': 'str',
            'source_name': 'str',
            'source_type_name': 'str',
            'entity_id': 'str',
            'entity_type_name': 'str',
            'host': 'str',
            'log_group_id': 'str'
        }

        self.attribute_map = {
            'agent_id': 'agentId',
            'source_name': 'sourceName',
            'source_type_name': 'sourceTypeName',
            'entity_id': 'entityId',
            'entity_type_name': 'entityTypeName',
            'host': 'host',
            'log_group_id': 'logGroupId'
        }

        self._agent_id = None
        self._source_name = None
        self._source_type_name = None
        self._entity_id = None
        self._entity_type_name = None
        self._host = None
        self._log_group_id = None

    @property
    def agent_id(self):
        """
        Gets the agent_id of this DeleteLogAnalyticsAssociation.
        The agent unique identifier.


        :return: The agent_id of this DeleteLogAnalyticsAssociation.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this DeleteLogAnalyticsAssociation.
        The agent unique identifier.


        :param agent_id: The agent_id of this DeleteLogAnalyticsAssociation.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def source_name(self):
        """
        Gets the source_name of this DeleteLogAnalyticsAssociation.
        The source name.


        :return: The source_name of this DeleteLogAnalyticsAssociation.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this DeleteLogAnalyticsAssociation.
        The source name.


        :param source_name: The source_name of this DeleteLogAnalyticsAssociation.
        :type: str
        """
        self._source_name = source_name

    @property
    def source_type_name(self):
        """
        Gets the source_type_name of this DeleteLogAnalyticsAssociation.
        The source type internal name.


        :return: The source_type_name of this DeleteLogAnalyticsAssociation.
        :rtype: str
        """
        return self._source_type_name

    @source_type_name.setter
    def source_type_name(self, source_type_name):
        """
        Sets the source_type_name of this DeleteLogAnalyticsAssociation.
        The source type internal name.


        :param source_type_name: The source_type_name of this DeleteLogAnalyticsAssociation.
        :type: str
        """
        self._source_type_name = source_type_name

    @property
    def entity_id(self):
        """
        Gets the entity_id of this DeleteLogAnalyticsAssociation.
        The entity unique identifier.


        :return: The entity_id of this DeleteLogAnalyticsAssociation.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this DeleteLogAnalyticsAssociation.
        The entity unique identifier.


        :param entity_id: The entity_id of this DeleteLogAnalyticsAssociation.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def entity_type_name(self):
        """
        Gets the entity_type_name of this DeleteLogAnalyticsAssociation.
        The entity type internal name.


        :return: The entity_type_name of this DeleteLogAnalyticsAssociation.
        :rtype: str
        """
        return self._entity_type_name

    @entity_type_name.setter
    def entity_type_name(self, entity_type_name):
        """
        Sets the entity_type_name of this DeleteLogAnalyticsAssociation.
        The entity type internal name.


        :param entity_type_name: The entity_type_name of this DeleteLogAnalyticsAssociation.
        :type: str
        """
        self._entity_type_name = entity_type_name

    @property
    def host(self):
        """
        Gets the host of this DeleteLogAnalyticsAssociation.
        The host name.


        :return: The host of this DeleteLogAnalyticsAssociation.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this DeleteLogAnalyticsAssociation.
        The host name.


        :param host: The host of this DeleteLogAnalyticsAssociation.
        :type: str
        """
        self._host = host

    @property
    def log_group_id(self):
        """
        Gets the log_group_id of this DeleteLogAnalyticsAssociation.
        The log group unique identifier.


        :return: The log_group_id of this DeleteLogAnalyticsAssociation.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this DeleteLogAnalyticsAssociation.
        The log group unique identifier.


        :param log_group_id: The log_group_id of this DeleteLogAnalyticsAssociation.
        :type: str
        """
        self._log_group_id = log_group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
