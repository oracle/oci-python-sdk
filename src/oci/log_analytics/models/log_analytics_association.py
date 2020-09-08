# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsAssociation(object):
    """
    LogAnalyticsAssociation
    """

    #: A constant which can be used with the life_cycle_state property of a LogAnalyticsAssociation.
    #: This constant has a value of "ACCEPTED"
    LIFE_CYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the life_cycle_state property of a LogAnalyticsAssociation.
    #: This constant has a value of "IN_PROGRESS"
    LIFE_CYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the life_cycle_state property of a LogAnalyticsAssociation.
    #: This constant has a value of "SUCCEEDED"
    LIFE_CYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the life_cycle_state property of a LogAnalyticsAssociation.
    #: This constant has a value of "FAILED"
    LIFE_CYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsAssociation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param failure_message:
            The value to assign to the failure_message property of this LogAnalyticsAssociation.
        :type failure_message: str

        :param agent_id:
            The value to assign to the agent_id property of this LogAnalyticsAssociation.
        :type agent_id: str

        :param time_last_attempted:
            The value to assign to the time_last_attempted property of this LogAnalyticsAssociation.
        :type time_last_attempted: datetime

        :param retry_count:
            The value to assign to the retry_count property of this LogAnalyticsAssociation.
        :type retry_count: int

        :param source_name:
            The value to assign to the source_name property of this LogAnalyticsAssociation.
        :type source_name: str

        :param source_display_name:
            The value to assign to the source_display_name property of this LogAnalyticsAssociation.
        :type source_display_name: str

        :param source_type_name:
            The value to assign to the source_type_name property of this LogAnalyticsAssociation.
        :type source_type_name: str

        :param life_cycle_state:
            The value to assign to the life_cycle_state property of this LogAnalyticsAssociation.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type life_cycle_state: str

        :param entity_id:
            The value to assign to the entity_id property of this LogAnalyticsAssociation.
        :type entity_id: str

        :param entity_name:
            The value to assign to the entity_name property of this LogAnalyticsAssociation.
        :type entity_name: str

        :param entity_type_name:
            The value to assign to the entity_type_name property of this LogAnalyticsAssociation.
        :type entity_type_name: str

        :param host:
            The value to assign to the host property of this LogAnalyticsAssociation.
        :type host: str

        :param agent_entity_name:
            The value to assign to the agent_entity_name property of this LogAnalyticsAssociation.
        :type agent_entity_name: str

        :param entity_type_display_name:
            The value to assign to the entity_type_display_name property of this LogAnalyticsAssociation.
        :type entity_type_display_name: str

        :param log_group_id:
            The value to assign to the log_group_id property of this LogAnalyticsAssociation.
        :type log_group_id: str

        :param log_group_name:
            The value to assign to the log_group_name property of this LogAnalyticsAssociation.
        :type log_group_name: str

        :param log_group_compartment:
            The value to assign to the log_group_compartment property of this LogAnalyticsAssociation.
        :type log_group_compartment: str

        """
        self.swagger_types = {
            'failure_message': 'str',
            'agent_id': 'str',
            'time_last_attempted': 'datetime',
            'retry_count': 'int',
            'source_name': 'str',
            'source_display_name': 'str',
            'source_type_name': 'str',
            'life_cycle_state': 'str',
            'entity_id': 'str',
            'entity_name': 'str',
            'entity_type_name': 'str',
            'host': 'str',
            'agent_entity_name': 'str',
            'entity_type_display_name': 'str',
            'log_group_id': 'str',
            'log_group_name': 'str',
            'log_group_compartment': 'str'
        }

        self.attribute_map = {
            'failure_message': 'failureMessage',
            'agent_id': 'agentId',
            'time_last_attempted': 'timeLastAttempted',
            'retry_count': 'retryCount',
            'source_name': 'sourceName',
            'source_display_name': 'sourceDisplayName',
            'source_type_name': 'sourceTypeName',
            'life_cycle_state': 'lifeCycleState',
            'entity_id': 'entityId',
            'entity_name': 'entityName',
            'entity_type_name': 'entityTypeName',
            'host': 'host',
            'agent_entity_name': 'agentEntityName',
            'entity_type_display_name': 'entityTypeDisplayName',
            'log_group_id': 'logGroupId',
            'log_group_name': 'logGroupName',
            'log_group_compartment': 'logGroupCompartment'
        }

        self._failure_message = None
        self._agent_id = None
        self._time_last_attempted = None
        self._retry_count = None
        self._source_name = None
        self._source_display_name = None
        self._source_type_name = None
        self._life_cycle_state = None
        self._entity_id = None
        self._entity_name = None
        self._entity_type_name = None
        self._host = None
        self._agent_entity_name = None
        self._entity_type_display_name = None
        self._log_group_id = None
        self._log_group_name = None
        self._log_group_compartment = None

    @property
    def failure_message(self):
        """
        Gets the failure_message of this LogAnalyticsAssociation.
        failure message


        :return: The failure_message of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        """
        Sets the failure_message of this LogAnalyticsAssociation.
        failure message


        :param failure_message: The failure_message of this LogAnalyticsAssociation.
        :type: str
        """
        self._failure_message = failure_message

    @property
    def agent_id(self):
        """
        Gets the agent_id of this LogAnalyticsAssociation.
        Lama Idf


        :return: The agent_id of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this LogAnalyticsAssociation.
        Lama Idf


        :param agent_id: The agent_id of this LogAnalyticsAssociation.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def time_last_attempted(self):
        """
        Gets the time_last_attempted of this LogAnalyticsAssociation.
        last attempt date


        :return: The time_last_attempted of this LogAnalyticsAssociation.
        :rtype: datetime
        """
        return self._time_last_attempted

    @time_last_attempted.setter
    def time_last_attempted(self, time_last_attempted):
        """
        Sets the time_last_attempted of this LogAnalyticsAssociation.
        last attempt date


        :param time_last_attempted: The time_last_attempted of this LogAnalyticsAssociation.
        :type: datetime
        """
        self._time_last_attempted = time_last_attempted

    @property
    def retry_count(self):
        """
        Gets the retry_count of this LogAnalyticsAssociation.
        retry count


        :return: The retry_count of this LogAnalyticsAssociation.
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """
        Sets the retry_count of this LogAnalyticsAssociation.
        retry count


        :param retry_count: The retry_count of this LogAnalyticsAssociation.
        :type: int
        """
        self._retry_count = retry_count

    @property
    def source_name(self):
        """
        Gets the source_name of this LogAnalyticsAssociation.
        source name


        :return: The source_name of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this LogAnalyticsAssociation.
        source name


        :param source_name: The source_name of this LogAnalyticsAssociation.
        :type: str
        """
        self._source_name = source_name

    @property
    def source_display_name(self):
        """
        Gets the source_display_name of this LogAnalyticsAssociation.
        source display name


        :return: The source_display_name of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._source_display_name

    @source_display_name.setter
    def source_display_name(self, source_display_name):
        """
        Sets the source_display_name of this LogAnalyticsAssociation.
        source display name


        :param source_display_name: The source_display_name of this LogAnalyticsAssociation.
        :type: str
        """
        self._source_display_name = source_display_name

    @property
    def source_type_name(self):
        """
        Gets the source_type_name of this LogAnalyticsAssociation.
        source type internal name


        :return: The source_type_name of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._source_type_name

    @source_type_name.setter
    def source_type_name(self, source_type_name):
        """
        Sets the source_type_name of this LogAnalyticsAssociation.
        source type internal name


        :param source_type_name: The source_type_name of this LogAnalyticsAssociation.
        :type: str
        """
        self._source_type_name = source_type_name

    @property
    def life_cycle_state(self):
        """
        Gets the life_cycle_state of this LogAnalyticsAssociation.
        lifeCycleState

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The life_cycle_state of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._life_cycle_state

    @life_cycle_state.setter
    def life_cycle_state(self, life_cycle_state):
        """
        Sets the life_cycle_state of this LogAnalyticsAssociation.
        lifeCycleState


        :param life_cycle_state: The life_cycle_state of this LogAnalyticsAssociation.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(life_cycle_state, allowed_values):
            life_cycle_state = 'UNKNOWN_ENUM_VALUE'
        self._life_cycle_state = life_cycle_state

    @property
    def entity_id(self):
        """
        Gets the entity_id of this LogAnalyticsAssociation.
        entity GUID


        :return: The entity_id of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this LogAnalyticsAssociation.
        entity GUID


        :param entity_id: The entity_id of this LogAnalyticsAssociation.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def entity_name(self):
        """
        Gets the entity_name of this LogAnalyticsAssociation.
        entity name


        :return: The entity_name of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this LogAnalyticsAssociation.
        entity name


        :param entity_name: The entity_name of this LogAnalyticsAssociation.
        :type: str
        """
        self._entity_name = entity_name

    @property
    def entity_type_name(self):
        """
        Gets the entity_type_name of this LogAnalyticsAssociation.
        entity type internal name


        :return: The entity_type_name of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._entity_type_name

    @entity_type_name.setter
    def entity_type_name(self, entity_type_name):
        """
        Sets the entity_type_name of this LogAnalyticsAssociation.
        entity type internal name


        :param entity_type_name: The entity_type_name of this LogAnalyticsAssociation.
        :type: str
        """
        self._entity_type_name = entity_type_name

    @property
    def host(self):
        """
        Gets the host of this LogAnalyticsAssociation.
        host name


        :return: The host of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this LogAnalyticsAssociation.
        host name


        :param host: The host of this LogAnalyticsAssociation.
        :type: str
        """
        self._host = host

    @property
    def agent_entity_name(self):
        """
        Gets the agent_entity_name of this LogAnalyticsAssociation.
        Agent entity name


        :return: The agent_entity_name of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._agent_entity_name

    @agent_entity_name.setter
    def agent_entity_name(self, agent_entity_name):
        """
        Sets the agent_entity_name of this LogAnalyticsAssociation.
        Agent entity name


        :param agent_entity_name: The agent_entity_name of this LogAnalyticsAssociation.
        :type: str
        """
        self._agent_entity_name = agent_entity_name

    @property
    def entity_type_display_name(self):
        """
        Gets the entity_type_display_name of this LogAnalyticsAssociation.
        entity type display name


        :return: The entity_type_display_name of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._entity_type_display_name

    @entity_type_display_name.setter
    def entity_type_display_name(self, entity_type_display_name):
        """
        Sets the entity_type_display_name of this LogAnalyticsAssociation.
        entity type display name


        :param entity_type_display_name: The entity_type_display_name of this LogAnalyticsAssociation.
        :type: str
        """
        self._entity_type_display_name = entity_type_display_name

    @property
    def log_group_id(self):
        """
        Gets the log_group_id of this LogAnalyticsAssociation.
        log group ocid


        :return: The log_group_id of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this LogAnalyticsAssociation.
        log group ocid


        :param log_group_id: The log_group_id of this LogAnalyticsAssociation.
        :type: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        """
        Gets the log_group_name of this LogAnalyticsAssociation.
        log group name


        :return: The log_group_name of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """
        Sets the log_group_name of this LogAnalyticsAssociation.
        log group name


        :param log_group_name: The log_group_name of this LogAnalyticsAssociation.
        :type: str
        """
        self._log_group_name = log_group_name

    @property
    def log_group_compartment(self):
        """
        Gets the log_group_compartment of this LogAnalyticsAssociation.
        log group compartment


        :return: The log_group_compartment of this LogAnalyticsAssociation.
        :rtype: str
        """
        return self._log_group_compartment

    @log_group_compartment.setter
    def log_group_compartment(self, log_group_compartment):
        """
        Sets the log_group_compartment of this LogAnalyticsAssociation.
        log group compartment


        :param log_group_compartment: The log_group_compartment of this LogAnalyticsAssociation.
        :type: str
        """
        self._log_group_compartment = log_group_compartment

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
