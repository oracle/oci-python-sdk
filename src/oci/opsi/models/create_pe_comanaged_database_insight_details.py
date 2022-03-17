# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_database_insight_details import CreateDatabaseInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePeComanagedDatabaseInsightDetails(CreateDatabaseInsightDetails):
    """
    The information about database to be analyzed.
    """

    #: A constant which can be used with the deployment_type property of a CreatePeComanagedDatabaseInsightDetails.
    #: This constant has a value of "VIRTUAL_MACHINE"
    DEPLOYMENT_TYPE_VIRTUAL_MACHINE = "VIRTUAL_MACHINE"

    #: A constant which can be used with the deployment_type property of a CreatePeComanagedDatabaseInsightDetails.
    #: This constant has a value of "BARE_METAL"
    DEPLOYMENT_TYPE_BARE_METAL = "BARE_METAL"

    #: A constant which can be used with the deployment_type property of a CreatePeComanagedDatabaseInsightDetails.
    #: This constant has a value of "EXACS"
    DEPLOYMENT_TYPE_EXACS = "EXACS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePeComanagedDatabaseInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.CreatePeComanagedDatabaseInsightDetails.entity_source` attribute
        of this class is ``PE_COMANAGED_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this CreatePeComanagedDatabaseInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePeComanagedDatabaseInsightDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePeComanagedDatabaseInsightDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePeComanagedDatabaseInsightDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param database_id:
            The value to assign to the database_id property of this CreatePeComanagedDatabaseInsightDetails.
        :type database_id: str

        :param database_resource_type:
            The value to assign to the database_resource_type property of this CreatePeComanagedDatabaseInsightDetails.
        :type database_resource_type: str

        :param opsi_private_endpoint_id:
            The value to assign to the opsi_private_endpoint_id property of this CreatePeComanagedDatabaseInsightDetails.
        :type opsi_private_endpoint_id: str

        :param service_name:
            The value to assign to the service_name property of this CreatePeComanagedDatabaseInsightDetails.
        :type service_name: str

        :param credential_details:
            The value to assign to the credential_details property of this CreatePeComanagedDatabaseInsightDetails.
        :type credential_details: oci.opsi.models.CredentialDetails

        :param deployment_type:
            The value to assign to the deployment_type property of this CreatePeComanagedDatabaseInsightDetails.
            Allowed values for this property are: "VIRTUAL_MACHINE", "BARE_METAL", "EXACS"
        :type deployment_type: str

        :param system_tags:
            The value to assign to the system_tags property of this CreatePeComanagedDatabaseInsightDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'entity_source': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'database_id': 'str',
            'database_resource_type': 'str',
            'opsi_private_endpoint_id': 'str',
            'service_name': 'str',
            'credential_details': 'CredentialDetails',
            'deployment_type': 'str',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'database_id': 'databaseId',
            'database_resource_type': 'databaseResourceType',
            'opsi_private_endpoint_id': 'opsiPrivateEndpointId',
            'service_name': 'serviceName',
            'credential_details': 'credentialDetails',
            'deployment_type': 'deploymentType',
            'system_tags': 'systemTags'
        }

        self._entity_source = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._database_id = None
        self._database_resource_type = None
        self._opsi_private_endpoint_id = None
        self._service_name = None
        self._credential_details = None
        self._deployment_type = None
        self._system_tags = None
        self._entity_source = 'PE_COMANAGED_DATABASE'

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this CreatePeComanagedDatabaseInsightDetails.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The database_id of this CreatePeComanagedDatabaseInsightDetails.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this CreatePeComanagedDatabaseInsightDetails.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this CreatePeComanagedDatabaseInsightDetails.
        :type: str
        """
        self._database_id = database_id

    @property
    def database_resource_type(self):
        """
        **[Required]** Gets the database_resource_type of this CreatePeComanagedDatabaseInsightDetails.
        OCI database resource type


        :return: The database_resource_type of this CreatePeComanagedDatabaseInsightDetails.
        :rtype: str
        """
        return self._database_resource_type

    @database_resource_type.setter
    def database_resource_type(self, database_resource_type):
        """
        Sets the database_resource_type of this CreatePeComanagedDatabaseInsightDetails.
        OCI database resource type


        :param database_resource_type: The database_resource_type of this CreatePeComanagedDatabaseInsightDetails.
        :type: str
        """
        self._database_resource_type = database_resource_type

    @property
    def opsi_private_endpoint_id(self):
        """
        **[Required]** Gets the opsi_private_endpoint_id of this CreatePeComanagedDatabaseInsightDetails.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The opsi_private_endpoint_id of this CreatePeComanagedDatabaseInsightDetails.
        :rtype: str
        """
        return self._opsi_private_endpoint_id

    @opsi_private_endpoint_id.setter
    def opsi_private_endpoint_id(self, opsi_private_endpoint_id):
        """
        Sets the opsi_private_endpoint_id of this CreatePeComanagedDatabaseInsightDetails.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param opsi_private_endpoint_id: The opsi_private_endpoint_id of this CreatePeComanagedDatabaseInsightDetails.
        :type: str
        """
        self._opsi_private_endpoint_id = opsi_private_endpoint_id

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this CreatePeComanagedDatabaseInsightDetails.
        Database service name used for connection requests.


        :return: The service_name of this CreatePeComanagedDatabaseInsightDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this CreatePeComanagedDatabaseInsightDetails.
        Database service name used for connection requests.


        :param service_name: The service_name of this CreatePeComanagedDatabaseInsightDetails.
        :type: str
        """
        self._service_name = service_name

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this CreatePeComanagedDatabaseInsightDetails.

        :return: The credential_details of this CreatePeComanagedDatabaseInsightDetails.
        :rtype: oci.opsi.models.CredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this CreatePeComanagedDatabaseInsightDetails.

        :param credential_details: The credential_details of this CreatePeComanagedDatabaseInsightDetails.
        :type: oci.opsi.models.CredentialDetails
        """
        self._credential_details = credential_details

    @property
    def deployment_type(self):
        """
        **[Required]** Gets the deployment_type of this CreatePeComanagedDatabaseInsightDetails.
        Database Deployment Type

        Allowed values for this property are: "VIRTUAL_MACHINE", "BARE_METAL", "EXACS"


        :return: The deployment_type of this CreatePeComanagedDatabaseInsightDetails.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this CreatePeComanagedDatabaseInsightDetails.
        Database Deployment Type


        :param deployment_type: The deployment_type of this CreatePeComanagedDatabaseInsightDetails.
        :type: str
        """
        allowed_values = ["VIRTUAL_MACHINE", "BARE_METAL", "EXACS"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            raise ValueError(
                "Invalid value for `deployment_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._deployment_type = deployment_type

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CreatePeComanagedDatabaseInsightDetails.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this CreatePeComanagedDatabaseInsightDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CreatePeComanagedDatabaseInsightDetails.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this CreatePeComanagedDatabaseInsightDetails.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
