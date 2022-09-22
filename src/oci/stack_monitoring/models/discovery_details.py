# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiscoveryDetails(object):
    """
    The request of DiscoveryJob Resource details.
    """

    #: A constant which can be used with the resource_type property of a DiscoveryDetails.
    #: This constant has a value of "WEBLOGIC_DOMAIN"
    RESOURCE_TYPE_WEBLOGIC_DOMAIN = "WEBLOGIC_DOMAIN"

    #: A constant which can be used with the resource_type property of a DiscoveryDetails.
    #: This constant has a value of "EBS_INSTANCE"
    RESOURCE_TYPE_EBS_INSTANCE = "EBS_INSTANCE"

    #: A constant which can be used with the resource_type property of a DiscoveryDetails.
    #: This constant has a value of "ORACLE_DATABASE"
    RESOURCE_TYPE_ORACLE_DATABASE = "ORACLE_DATABASE"

    #: A constant which can be used with the resource_type property of a DiscoveryDetails.
    #: This constant has a value of "OCI_ORACLE_DB"
    RESOURCE_TYPE_OCI_ORACLE_DB = "OCI_ORACLE_DB"

    #: A constant which can be used with the resource_type property of a DiscoveryDetails.
    #: This constant has a value of "OCI_ORACLE_CDB"
    RESOURCE_TYPE_OCI_ORACLE_CDB = "OCI_ORACLE_CDB"

    #: A constant which can be used with the resource_type property of a DiscoveryDetails.
    #: This constant has a value of "OCI_ORACLE_PDB"
    RESOURCE_TYPE_OCI_ORACLE_PDB = "OCI_ORACLE_PDB"

    #: A constant which can be used with the resource_type property of a DiscoveryDetails.
    #: This constant has a value of "HOST"
    RESOURCE_TYPE_HOST = "HOST"

    def __init__(self, **kwargs):
        """
        Initializes a new DiscoveryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param agent_id:
            The value to assign to the agent_id property of this DiscoveryDetails.
        :type agent_id: str

        :param resource_type:
            The value to assign to the resource_type property of this DiscoveryDetails.
            Allowed values for this property are: "WEBLOGIC_DOMAIN", "EBS_INSTANCE", "ORACLE_DATABASE", "OCI_ORACLE_DB", "OCI_ORACLE_CDB", "OCI_ORACLE_PDB", "HOST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param resource_name:
            The value to assign to the resource_name property of this DiscoveryDetails.
        :type resource_name: str

        :param properties:
            The value to assign to the properties property of this DiscoveryDetails.
        :type properties: oci.stack_monitoring.models.PropertyDetails

        :param credentials:
            The value to assign to the credentials property of this DiscoveryDetails.
        :type credentials: oci.stack_monitoring.models.CredentialCollection

        :param tags:
            The value to assign to the tags property of this DiscoveryDetails.
        :type tags: oci.stack_monitoring.models.PropertyDetails

        """
        self.swagger_types = {
            'agent_id': 'str',
            'resource_type': 'str',
            'resource_name': 'str',
            'properties': 'PropertyDetails',
            'credentials': 'CredentialCollection',
            'tags': 'PropertyDetails'
        }

        self.attribute_map = {
            'agent_id': 'agentId',
            'resource_type': 'resourceType',
            'resource_name': 'resourceName',
            'properties': 'properties',
            'credentials': 'credentials',
            'tags': 'tags'
        }

        self._agent_id = None
        self._resource_type = None
        self._resource_name = None
        self._properties = None
        self._credentials = None
        self._tags = None

    @property
    def agent_id(self):
        """
        **[Required]** Gets the agent_id of this DiscoveryDetails.
        The OCID of Management Agent


        :return: The agent_id of this DiscoveryDetails.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this DiscoveryDetails.
        The OCID of Management Agent


        :param agent_id: The agent_id of this DiscoveryDetails.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this DiscoveryDetails.
        Resource Type.

        Allowed values for this property are: "WEBLOGIC_DOMAIN", "EBS_INSTANCE", "ORACLE_DATABASE", "OCI_ORACLE_DB", "OCI_ORACLE_CDB", "OCI_ORACLE_PDB", "HOST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_type of this DiscoveryDetails.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this DiscoveryDetails.
        Resource Type.


        :param resource_type: The resource_type of this DiscoveryDetails.
        :type: str
        """
        allowed_values = ["WEBLOGIC_DOMAIN", "EBS_INSTANCE", "ORACLE_DATABASE", "OCI_ORACLE_DB", "OCI_ORACLE_CDB", "OCI_ORACLE_PDB", "HOST"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            resource_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_type = resource_type

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this DiscoveryDetails.
        The Name of resource type


        :return: The resource_name of this DiscoveryDetails.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this DiscoveryDetails.
        The Name of resource type


        :param resource_name: The resource_name of this DiscoveryDetails.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def properties(self):
        """
        **[Required]** Gets the properties of this DiscoveryDetails.

        :return: The properties of this DiscoveryDetails.
        :rtype: oci.stack_monitoring.models.PropertyDetails
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this DiscoveryDetails.

        :param properties: The properties of this DiscoveryDetails.
        :type: oci.stack_monitoring.models.PropertyDetails
        """
        self._properties = properties

    @property
    def credentials(self):
        """
        Gets the credentials of this DiscoveryDetails.

        :return: The credentials of this DiscoveryDetails.
        :rtype: oci.stack_monitoring.models.CredentialCollection
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this DiscoveryDetails.

        :param credentials: The credentials of this DiscoveryDetails.
        :type: oci.stack_monitoring.models.CredentialCollection
        """
        self._credentials = credentials

    @property
    def tags(self):
        """
        Gets the tags of this DiscoveryDetails.

        :return: The tags of this DiscoveryDetails.
        :rtype: oci.stack_monitoring.models.PropertyDetails
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this DiscoveryDetails.

        :param tags: The tags of this DiscoveryDetails.
        :type: oci.stack_monitoring.models.PropertyDetails
        """
        self._tags = tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
