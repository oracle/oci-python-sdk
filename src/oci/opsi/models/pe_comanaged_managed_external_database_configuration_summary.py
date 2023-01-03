# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_configuration_summary import DatabaseConfigurationSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PeComanagedManagedExternalDatabaseConfigurationSummary(DatabaseConfigurationSummary):
    """
    Configuration Summary of a Private Endpoint Co-managed External database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PeComanagedManagedExternalDatabaseConfigurationSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.PeComanagedManagedExternalDatabaseConfigurationSummary.entity_source` attribute
        of this class is ``PE_COMANAGED_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_insight_id:
            The value to assign to the database_insight_id property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type database_insight_id: str

        :param entity_source:
            The value to assign to the entity_source property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
            Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type compartment_id: str

        :param database_name:
            The value to assign to the database_name property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type database_name: str

        :param database_display_name:
            The value to assign to the database_display_name property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type database_display_name: str

        :param database_type:
            The value to assign to the database_type property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type database_version: str

        :param cdb_name:
            The value to assign to the cdb_name property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type cdb_name: str

        :param defined_tags:
            The value to assign to the defined_tags property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type freeform_tags: dict(str, str)

        :param processor_count:
            The value to assign to the processor_count property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type processor_count: int

        :param database_id:
            The value to assign to the database_id property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type database_id: str

        :param parent_id:
            The value to assign to the parent_id property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type parent_id: str

        :param opsi_private_endpoint_id:
            The value to assign to the opsi_private_endpoint_id property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type opsi_private_endpoint_id: str

        :param instances:
            The value to assign to the instances property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type instances: list[oci.opsi.models.HostInstanceMap]

        :param exadata_details:
            The value to assign to the exadata_details property of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type exadata_details: oci.opsi.models.ExadataDetails

        """
        self.swagger_types = {
            'database_insight_id': 'str',
            'entity_source': 'str',
            'compartment_id': 'str',
            'database_name': 'str',
            'database_display_name': 'str',
            'database_type': 'str',
            'database_version': 'str',
            'cdb_name': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'processor_count': 'int',
            'database_id': 'str',
            'parent_id': 'str',
            'opsi_private_endpoint_id': 'str',
            'instances': 'list[HostInstanceMap]',
            'exadata_details': 'ExadataDetails'
        }

        self.attribute_map = {
            'database_insight_id': 'databaseInsightId',
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'database_name': 'databaseName',
            'database_display_name': 'databaseDisplayName',
            'database_type': 'databaseType',
            'database_version': 'databaseVersion',
            'cdb_name': 'cdbName',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'processor_count': 'processorCount',
            'database_id': 'databaseId',
            'parent_id': 'parentId',
            'opsi_private_endpoint_id': 'opsiPrivateEndpointId',
            'instances': 'instances',
            'exadata_details': 'exadataDetails'
        }

        self._database_insight_id = None
        self._entity_source = None
        self._compartment_id = None
        self._database_name = None
        self._database_display_name = None
        self._database_type = None
        self._database_version = None
        self._cdb_name = None
        self._defined_tags = None
        self._freeform_tags = None
        self._processor_count = None
        self._database_id = None
        self._parent_id = None
        self._opsi_private_endpoint_id = None
        self._instances = None
        self._exadata_details = None
        self._entity_source = 'PE_COMANAGED_DATABASE'

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The database_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type: str
        """
        self._database_id = database_id

    @property
    def parent_id(self):
        """
        **[Required]** Gets the parent_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The parent_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param parent_id: The parent_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def opsi_private_endpoint_id(self):
        """
        **[Required]** Gets the opsi_private_endpoint_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The opsi_private_endpoint_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :rtype: str
        """
        return self._opsi_private_endpoint_id

    @opsi_private_endpoint_id.setter
    def opsi_private_endpoint_id(self, opsi_private_endpoint_id):
        """
        Sets the opsi_private_endpoint_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param opsi_private_endpoint_id: The opsi_private_endpoint_id of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type: str
        """
        self._opsi_private_endpoint_id = opsi_private_endpoint_id

    @property
    def instances(self):
        """
        **[Required]** Gets the instances of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        Array of hostname and instance name.


        :return: The instances of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :rtype: list[oci.opsi.models.HostInstanceMap]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """
        Sets the instances of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        Array of hostname and instance name.


        :param instances: The instances of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type: list[oci.opsi.models.HostInstanceMap]
        """
        self._instances = instances

    @property
    def exadata_details(self):
        """
        **[Required]** Gets the exadata_details of this PeComanagedManagedExternalDatabaseConfigurationSummary.

        :return: The exadata_details of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :rtype: oci.opsi.models.ExadataDetails
        """
        return self._exadata_details

    @exadata_details.setter
    def exadata_details(self, exadata_details):
        """
        Sets the exadata_details of this PeComanagedManagedExternalDatabaseConfigurationSummary.

        :param exadata_details: The exadata_details of this PeComanagedManagedExternalDatabaseConfigurationSummary.
        :type: oci.opsi.models.ExadataDetails
        """
        self._exadata_details = exadata_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
