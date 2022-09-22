# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMonitoredResourceDetails(object):
    """
    The information about new monitored resource. The combination of monitored resource name and type should be unique across tenancy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMonitoredResourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateMonitoredResourceDetails.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this CreateMonitoredResourceDetails.
        :type display_name: str

        :param type:
            The value to assign to the type property of this CreateMonitoredResourceDetails.
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMonitoredResourceDetails.
        :type compartment_id: str

        :param host_name:
            The value to assign to the host_name property of this CreateMonitoredResourceDetails.
        :type host_name: str

        :param external_id:
            The value to assign to the external_id property of this CreateMonitoredResourceDetails.
        :type external_id: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this CreateMonitoredResourceDetails.
        :type management_agent_id: str

        :param resource_time_zone:
            The value to assign to the resource_time_zone property of this CreateMonitoredResourceDetails.
        :type resource_time_zone: str

        :param properties:
            The value to assign to the properties property of this CreateMonitoredResourceDetails.
        :type properties: list[oci.stack_monitoring.models.MonitoredResourceProperty]

        :param database_connection_details:
            The value to assign to the database_connection_details property of this CreateMonitoredResourceDetails.
        :type database_connection_details: oci.stack_monitoring.models.ConnectionDetails

        :param credentials:
            The value to assign to the credentials property of this CreateMonitoredResourceDetails.
        :type credentials: oci.stack_monitoring.models.MonitoredResourceCredential

        :param aliases:
            The value to assign to the aliases property of this CreateMonitoredResourceDetails.
        :type aliases: oci.stack_monitoring.models.MonitoredResourceAliasCredential

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'type': 'str',
            'compartment_id': 'str',
            'host_name': 'str',
            'external_id': 'str',
            'management_agent_id': 'str',
            'resource_time_zone': 'str',
            'properties': 'list[MonitoredResourceProperty]',
            'database_connection_details': 'ConnectionDetails',
            'credentials': 'MonitoredResourceCredential',
            'aliases': 'MonitoredResourceAliasCredential'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'type': 'type',
            'compartment_id': 'compartmentId',
            'host_name': 'hostName',
            'external_id': 'externalId',
            'management_agent_id': 'managementAgentId',
            'resource_time_zone': 'resourceTimeZone',
            'properties': 'properties',
            'database_connection_details': 'databaseConnectionDetails',
            'credentials': 'credentials',
            'aliases': 'aliases'
        }

        self._name = None
        self._display_name = None
        self._type = None
        self._compartment_id = None
        self._host_name = None
        self._external_id = None
        self._management_agent_id = None
        self._resource_time_zone = None
        self._properties = None
        self._database_connection_details = None
        self._credentials = None
        self._aliases = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateMonitoredResourceDetails.
        Monitored resource name


        :return: The name of this CreateMonitoredResourceDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateMonitoredResourceDetails.
        Monitored resource name


        :param name: The name of this CreateMonitoredResourceDetails.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateMonitoredResourceDetails.
        Monitored resource display name.


        :return: The display_name of this CreateMonitoredResourceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMonitoredResourceDetails.
        Monitored resource display name.


        :param display_name: The display_name of this CreateMonitoredResourceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateMonitoredResourceDetails.
        Monitored resource type


        :return: The type of this CreateMonitoredResourceDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateMonitoredResourceDetails.
        Monitored resource type


        :param type: The type of this CreateMonitoredResourceDetails.
        :type: str
        """
        self._type = type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMonitoredResourceDetails.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateMonitoredResourceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMonitoredResourceDetails.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateMonitoredResourceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def host_name(self):
        """
        Gets the host_name of this CreateMonitoredResourceDetails.
        Host name of the monitored resource


        :return: The host_name of this CreateMonitoredResourceDetails.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this CreateMonitoredResourceDetails.
        Host name of the monitored resource


        :param host_name: The host_name of this CreateMonitoredResourceDetails.
        :type: str
        """
        self._host_name = host_name

    @property
    def external_id(self):
        """
        Gets the external_id of this CreateMonitoredResourceDetails.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.
        Currently supports only OCI compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_id of this CreateMonitoredResourceDetails.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this CreateMonitoredResourceDetails.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.
        Currently supports only OCI compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_id: The external_id of this CreateMonitoredResourceDetails.
        :type: str
        """
        self._external_id = external_id

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this CreateMonitoredResourceDetails.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this CreateMonitoredResourceDetails.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this CreateMonitoredResourceDetails.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this CreateMonitoredResourceDetails.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def resource_time_zone(self):
        """
        Gets the resource_time_zone of this CreateMonitoredResourceDetails.
        Time zone in the form of tz database canonical zone ID.


        :return: The resource_time_zone of this CreateMonitoredResourceDetails.
        :rtype: str
        """
        return self._resource_time_zone

    @resource_time_zone.setter
    def resource_time_zone(self, resource_time_zone):
        """
        Sets the resource_time_zone of this CreateMonitoredResourceDetails.
        Time zone in the form of tz database canonical zone ID.


        :param resource_time_zone: The resource_time_zone of this CreateMonitoredResourceDetails.
        :type: str
        """
        self._resource_time_zone = resource_time_zone

    @property
    def properties(self):
        """
        Gets the properties of this CreateMonitoredResourceDetails.
        List of monitored resource properties


        :return: The properties of this CreateMonitoredResourceDetails.
        :rtype: list[oci.stack_monitoring.models.MonitoredResourceProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CreateMonitoredResourceDetails.
        List of monitored resource properties


        :param properties: The properties of this CreateMonitoredResourceDetails.
        :type: list[oci.stack_monitoring.models.MonitoredResourceProperty]
        """
        self._properties = properties

    @property
    def database_connection_details(self):
        """
        Gets the database_connection_details of this CreateMonitoredResourceDetails.

        :return: The database_connection_details of this CreateMonitoredResourceDetails.
        :rtype: oci.stack_monitoring.models.ConnectionDetails
        """
        return self._database_connection_details

    @database_connection_details.setter
    def database_connection_details(self, database_connection_details):
        """
        Sets the database_connection_details of this CreateMonitoredResourceDetails.

        :param database_connection_details: The database_connection_details of this CreateMonitoredResourceDetails.
        :type: oci.stack_monitoring.models.ConnectionDetails
        """
        self._database_connection_details = database_connection_details

    @property
    def credentials(self):
        """
        Gets the credentials of this CreateMonitoredResourceDetails.

        :return: The credentials of this CreateMonitoredResourceDetails.
        :rtype: oci.stack_monitoring.models.MonitoredResourceCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this CreateMonitoredResourceDetails.

        :param credentials: The credentials of this CreateMonitoredResourceDetails.
        :type: oci.stack_monitoring.models.MonitoredResourceCredential
        """
        self._credentials = credentials

    @property
    def aliases(self):
        """
        Gets the aliases of this CreateMonitoredResourceDetails.

        :return: The aliases of this CreateMonitoredResourceDetails.
        :rtype: oci.stack_monitoring.models.MonitoredResourceAliasCredential
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this CreateMonitoredResourceDetails.

        :param aliases: The aliases of this CreateMonitoredResourceDetails.
        :type: oci.stack_monitoring.models.MonitoredResourceAliasCredential
        """
        self._aliases = aliases

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
