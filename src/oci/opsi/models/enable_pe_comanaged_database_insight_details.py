# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .enable_database_insight_details import EnableDatabaseInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnablePeComanagedDatabaseInsightDetails(EnableDatabaseInsightDetails):
    """
    The information about database to be analyzed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnablePeComanagedDatabaseInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.EnablePeComanagedDatabaseInsightDetails.entity_source` attribute
        of this class is ``PE_COMANAGED_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this EnablePeComanagedDatabaseInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EnablePeComanagedDatabaseInsightDetails.
        :type compartment_id: str

        :param opsi_private_endpoint_id:
            The value to assign to the opsi_private_endpoint_id property of this EnablePeComanagedDatabaseInsightDetails.
        :type opsi_private_endpoint_id: str

        :param service_name:
            The value to assign to the service_name property of this EnablePeComanagedDatabaseInsightDetails.
        :type service_name: str

        :param credential_details:
            The value to assign to the credential_details property of this EnablePeComanagedDatabaseInsightDetails.
        :type credential_details: oci.opsi.models.CredentialDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EnablePeComanagedDatabaseInsightDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EnablePeComanagedDatabaseInsightDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EnablePeComanagedDatabaseInsightDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'entity_source': 'str',
            'compartment_id': 'str',
            'opsi_private_endpoint_id': 'str',
            'service_name': 'str',
            'credential_details': 'CredentialDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'opsi_private_endpoint_id': 'opsiPrivateEndpointId',
            'service_name': 'serviceName',
            'credential_details': 'credentialDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._entity_source = None
        self._compartment_id = None
        self._opsi_private_endpoint_id = None
        self._service_name = None
        self._credential_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._entity_source = 'PE_COMANAGED_DATABASE'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EnablePeComanagedDatabaseInsightDetails.
        The compartment `OCID`__ of the Private service accessed database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this EnablePeComanagedDatabaseInsightDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EnablePeComanagedDatabaseInsightDetails.
        The compartment `OCID`__ of the Private service accessed database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this EnablePeComanagedDatabaseInsightDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def opsi_private_endpoint_id(self):
        """
        **[Required]** Gets the opsi_private_endpoint_id of this EnablePeComanagedDatabaseInsightDetails.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The opsi_private_endpoint_id of this EnablePeComanagedDatabaseInsightDetails.
        :rtype: str
        """
        return self._opsi_private_endpoint_id

    @opsi_private_endpoint_id.setter
    def opsi_private_endpoint_id(self, opsi_private_endpoint_id):
        """
        Sets the opsi_private_endpoint_id of this EnablePeComanagedDatabaseInsightDetails.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param opsi_private_endpoint_id: The opsi_private_endpoint_id of this EnablePeComanagedDatabaseInsightDetails.
        :type: str
        """
        self._opsi_private_endpoint_id = opsi_private_endpoint_id

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this EnablePeComanagedDatabaseInsightDetails.
        Database service name used for connection requests.


        :return: The service_name of this EnablePeComanagedDatabaseInsightDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this EnablePeComanagedDatabaseInsightDetails.
        Database service name used for connection requests.


        :param service_name: The service_name of this EnablePeComanagedDatabaseInsightDetails.
        :type: str
        """
        self._service_name = service_name

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this EnablePeComanagedDatabaseInsightDetails.

        :return: The credential_details of this EnablePeComanagedDatabaseInsightDetails.
        :rtype: oci.opsi.models.CredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this EnablePeComanagedDatabaseInsightDetails.

        :param credential_details: The credential_details of this EnablePeComanagedDatabaseInsightDetails.
        :type: oci.opsi.models.CredentialDetails
        """
        self._credential_details = credential_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this EnablePeComanagedDatabaseInsightDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this EnablePeComanagedDatabaseInsightDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EnablePeComanagedDatabaseInsightDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this EnablePeComanagedDatabaseInsightDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this EnablePeComanagedDatabaseInsightDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this EnablePeComanagedDatabaseInsightDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EnablePeComanagedDatabaseInsightDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this EnablePeComanagedDatabaseInsightDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this EnablePeComanagedDatabaseInsightDetails.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this EnablePeComanagedDatabaseInsightDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this EnablePeComanagedDatabaseInsightDetails.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this EnablePeComanagedDatabaseInsightDetails.
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
