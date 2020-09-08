# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsAssociationParameter(object):
    """
    LogAnalyticsAssociationParameter
    """

    #: A constant which can be used with the status property of a LogAnalyticsAssociationParameter.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a LogAnalyticsAssociationParameter.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsAssociationParameter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param agent_id:
            The value to assign to the agent_id property of this LogAnalyticsAssociationParameter.
        :type agent_id: str

        :param entity_type:
            The value to assign to the entity_type property of this LogAnalyticsAssociationParameter.
        :type entity_type: str

        :param entity_id:
            The value to assign to the entity_id property of this LogAnalyticsAssociationParameter.
        :type entity_id: str

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsAssociationParameter.
        :type source_id: str

        :param source_display_name:
            The value to assign to the source_display_name property of this LogAnalyticsAssociationParameter.
        :type source_display_name: str

        :param source_type:
            The value to assign to the source_type property of this LogAnalyticsAssociationParameter.
        :type source_type: str

        :param status:
            The value to assign to the status property of this LogAnalyticsAssociationParameter.
            Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param missing_properties:
            The value to assign to the missing_properties property of this LogAnalyticsAssociationParameter.
        :type missing_properties: list[str]

        :param required_properties:
            The value to assign to the required_properties property of this LogAnalyticsAssociationParameter.
        :type required_properties: list[str]

        """
        self.swagger_types = {
            'agent_id': 'str',
            'entity_type': 'str',
            'entity_id': 'str',
            'source_id': 'str',
            'source_display_name': 'str',
            'source_type': 'str',
            'status': 'str',
            'missing_properties': 'list[str]',
            'required_properties': 'list[str]'
        }

        self.attribute_map = {
            'agent_id': 'agentId',
            'entity_type': 'entityType',
            'entity_id': 'entityId',
            'source_id': 'sourceId',
            'source_display_name': 'sourceDisplayName',
            'source_type': 'sourceType',
            'status': 'status',
            'missing_properties': 'missingProperties',
            'required_properties': 'requiredProperties'
        }

        self._agent_id = None
        self._entity_type = None
        self._entity_id = None
        self._source_id = None
        self._source_display_name = None
        self._source_type = None
        self._status = None
        self._missing_properties = None
        self._required_properties = None

    @property
    def agent_id(self):
        """
        Gets the agent_id of this LogAnalyticsAssociationParameter.
        agent guid


        :return: The agent_id of this LogAnalyticsAssociationParameter.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this LogAnalyticsAssociationParameter.
        agent guid


        :param agent_id: The agent_id of this LogAnalyticsAssociationParameter.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this LogAnalyticsAssociationParameter.
        entity type


        :return: The entity_type of this LogAnalyticsAssociationParameter.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this LogAnalyticsAssociationParameter.
        entity type


        :param entity_type: The entity_type of this LogAnalyticsAssociationParameter.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def entity_id(self):
        """
        Gets the entity_id of this LogAnalyticsAssociationParameter.
        entity guid


        :return: The entity_id of this LogAnalyticsAssociationParameter.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this LogAnalyticsAssociationParameter.
        entity guid


        :param entity_id: The entity_id of this LogAnalyticsAssociationParameter.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsAssociationParameter.
        source name


        :return: The source_id of this LogAnalyticsAssociationParameter.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsAssociationParameter.
        source name


        :param source_id: The source_id of this LogAnalyticsAssociationParameter.
        :type: str
        """
        self._source_id = source_id

    @property
    def source_display_name(self):
        """
        Gets the source_display_name of this LogAnalyticsAssociationParameter.
        source display name


        :return: The source_display_name of this LogAnalyticsAssociationParameter.
        :rtype: str
        """
        return self._source_display_name

    @source_display_name.setter
    def source_display_name(self, source_display_name):
        """
        Sets the source_display_name of this LogAnalyticsAssociationParameter.
        source display name


        :param source_display_name: The source_display_name of this LogAnalyticsAssociationParameter.
        :type: str
        """
        self._source_display_name = source_display_name

    @property
    def source_type(self):
        """
        Gets the source_type of this LogAnalyticsAssociationParameter.
        source type


        :return: The source_type of this LogAnalyticsAssociationParameter.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this LogAnalyticsAssociationParameter.
        source type


        :param source_type: The source_type of this LogAnalyticsAssociationParameter.
        :type: str
        """
        self._source_type = source_type

    @property
    def status(self):
        """
        Gets the status of this LogAnalyticsAssociationParameter.
        status

        Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this LogAnalyticsAssociationParameter.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LogAnalyticsAssociationParameter.
        status


        :param status: The status of this LogAnalyticsAssociationParameter.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def missing_properties(self):
        """
        Gets the missing_properties of this LogAnalyticsAssociationParameter.
        missingProperties


        :return: The missing_properties of this LogAnalyticsAssociationParameter.
        :rtype: list[str]
        """
        return self._missing_properties

    @missing_properties.setter
    def missing_properties(self, missing_properties):
        """
        Sets the missing_properties of this LogAnalyticsAssociationParameter.
        missingProperties


        :param missing_properties: The missing_properties of this LogAnalyticsAssociationParameter.
        :type: list[str]
        """
        self._missing_properties = missing_properties

    @property
    def required_properties(self):
        """
        Gets the required_properties of this LogAnalyticsAssociationParameter.
        requiredProperties


        :return: The required_properties of this LogAnalyticsAssociationParameter.
        :rtype: list[str]
        """
        return self._required_properties

    @required_properties.setter
    def required_properties(self, required_properties):
        """
        Sets the required_properties of this LogAnalyticsAssociationParameter.
        requiredProperties


        :param required_properties: The required_properties of this LogAnalyticsAssociationParameter.
        :type: list[str]
        """
        self._required_properties = required_properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
