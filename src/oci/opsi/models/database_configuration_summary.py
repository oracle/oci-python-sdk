# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseConfigurationSummary(object):
    """
    Summary of a database configuration for a resource.
    """

    #: A constant which can be used with the entity_source property of a DatabaseConfigurationSummary.
    #: This constant has a value of "AUTONOMOUS_DATABASE"
    ENTITY_SOURCE_AUTONOMOUS_DATABASE = "AUTONOMOUS_DATABASE"

    #: A constant which can be used with the entity_source property of a DatabaseConfigurationSummary.
    #: This constant has a value of "EM_MANAGED_EXTERNAL_DATABASE"
    ENTITY_SOURCE_EM_MANAGED_EXTERNAL_DATABASE = "EM_MANAGED_EXTERNAL_DATABASE"

    #: A constant which can be used with the entity_source property of a DatabaseConfigurationSummary.
    #: This constant has a value of "MACS_MANAGED_EXTERNAL_DATABASE"
    ENTITY_SOURCE_MACS_MANAGED_EXTERNAL_DATABASE = "MACS_MANAGED_EXTERNAL_DATABASE"

    #: A constant which can be used with the entity_source property of a DatabaseConfigurationSummary.
    #: This constant has a value of "PE_COMANAGED_DATABASE"
    ENTITY_SOURCE_PE_COMANAGED_DATABASE = "PE_COMANAGED_DATABASE"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseConfigurationSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.EmManagedExternalDatabaseConfigurationSummary`
        * :class:`~oci.opsi.models.AutonomousDatabaseConfigurationSummary`
        * :class:`~oci.opsi.models.MacsManagedExternalDatabaseConfigurationSummary`
        * :class:`~oci.opsi.models.PeComanagedManagedExternalDatabaseConfigurationSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_insight_id:
            The value to assign to the database_insight_id property of this DatabaseConfigurationSummary.
        :type database_insight_id: str

        :param entity_source:
            The value to assign to the entity_source property of this DatabaseConfigurationSummary.
            Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseConfigurationSummary.
        :type compartment_id: str

        :param database_name:
            The value to assign to the database_name property of this DatabaseConfigurationSummary.
        :type database_name: str

        :param database_display_name:
            The value to assign to the database_display_name property of this DatabaseConfigurationSummary.
        :type database_display_name: str

        :param database_type:
            The value to assign to the database_type property of this DatabaseConfigurationSummary.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this DatabaseConfigurationSummary.
        :type database_version: str

        :param cdb_name:
            The value to assign to the cdb_name property of this DatabaseConfigurationSummary.
        :type cdb_name: str

        :param defined_tags:
            The value to assign to the defined_tags property of this DatabaseConfigurationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DatabaseConfigurationSummary.
        :type freeform_tags: dict(str, str)

        :param processor_count:
            The value to assign to the processor_count property of this DatabaseConfigurationSummary.
        :type processor_count: int

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
            'processor_count': 'int'
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
            'processor_count': 'processorCount'
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

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entitySource']

        if type == 'EM_MANAGED_EXTERNAL_DATABASE':
            return 'EmManagedExternalDatabaseConfigurationSummary'

        if type == 'AUTONOMOUS_DATABASE':
            return 'AutonomousDatabaseConfigurationSummary'

        if type == 'MACS_MANAGED_EXTERNAL_DATABASE':
            return 'MacsManagedExternalDatabaseConfigurationSummary'

        if type == 'PE_COMANAGED_DATABASE':
            return 'PeComanagedManagedExternalDatabaseConfigurationSummary'
        else:
            return 'DatabaseConfigurationSummary'

    @property
    def database_insight_id(self):
        """
        **[Required]** Gets the database_insight_id of this DatabaseConfigurationSummary.
        The `OCID`__ of the database insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The database_insight_id of this DatabaseConfigurationSummary.
        :rtype: str
        """
        return self._database_insight_id

    @database_insight_id.setter
    def database_insight_id(self, database_insight_id):
        """
        Sets the database_insight_id of this DatabaseConfigurationSummary.
        The `OCID`__ of the database insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param database_insight_id: The database_insight_id of this DatabaseConfigurationSummary.
        :type: str
        """
        self._database_insight_id = database_insight_id

    @property
    def entity_source(self):
        """
        **[Required]** Gets the entity_source of this DatabaseConfigurationSummary.
        Source of the database entity.

        Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_source of this DatabaseConfigurationSummary.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this DatabaseConfigurationSummary.
        Source of the database entity.


        :param entity_source: The entity_source of this DatabaseConfigurationSummary.
        :type: str
        """
        allowed_values = ["AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"]
        if not value_allowed_none_or_none_sentinel(entity_source, allowed_values):
            entity_source = 'UNKNOWN_ENUM_VALUE'
        self._entity_source = entity_source

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DatabaseConfigurationSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DatabaseConfigurationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DatabaseConfigurationSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DatabaseConfigurationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def database_name(self):
        """
        **[Required]** Gets the database_name of this DatabaseConfigurationSummary.
        The database name. The database name is unique within the tenancy.


        :return: The database_name of this DatabaseConfigurationSummary.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this DatabaseConfigurationSummary.
        The database name. The database name is unique within the tenancy.


        :param database_name: The database_name of this DatabaseConfigurationSummary.
        :type: str
        """
        self._database_name = database_name

    @property
    def database_display_name(self):
        """
        **[Required]** Gets the database_display_name of this DatabaseConfigurationSummary.
        The user-friendly name for the database. The name does not have to be unique.


        :return: The database_display_name of this DatabaseConfigurationSummary.
        :rtype: str
        """
        return self._database_display_name

    @database_display_name.setter
    def database_display_name(self, database_display_name):
        """
        Sets the database_display_name of this DatabaseConfigurationSummary.
        The user-friendly name for the database. The name does not have to be unique.


        :param database_display_name: The database_display_name of this DatabaseConfigurationSummary.
        :type: str
        """
        self._database_display_name = database_display_name

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this DatabaseConfigurationSummary.
        Operations Insights internal representation of the database type.


        :return: The database_type of this DatabaseConfigurationSummary.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this DatabaseConfigurationSummary.
        Operations Insights internal representation of the database type.


        :param database_type: The database_type of this DatabaseConfigurationSummary.
        :type: str
        """
        self._database_type = database_type

    @property
    def database_version(self):
        """
        **[Required]** Gets the database_version of this DatabaseConfigurationSummary.
        The version of the database.


        :return: The database_version of this DatabaseConfigurationSummary.
        :rtype: str
        """
        return self._database_version

    @database_version.setter
    def database_version(self, database_version):
        """
        Sets the database_version of this DatabaseConfigurationSummary.
        The version of the database.


        :param database_version: The database_version of this DatabaseConfigurationSummary.
        :type: str
        """
        self._database_version = database_version

    @property
    def cdb_name(self):
        """
        **[Required]** Gets the cdb_name of this DatabaseConfigurationSummary.
        Name of the CDB.Only applies to PDB.


        :return: The cdb_name of this DatabaseConfigurationSummary.
        :rtype: str
        """
        return self._cdb_name

    @cdb_name.setter
    def cdb_name(self, cdb_name):
        """
        Sets the cdb_name of this DatabaseConfigurationSummary.
        Name of the CDB.Only applies to PDB.


        :param cdb_name: The cdb_name of this DatabaseConfigurationSummary.
        :type: str
        """
        self._cdb_name = cdb_name

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this DatabaseConfigurationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DatabaseConfigurationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DatabaseConfigurationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DatabaseConfigurationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this DatabaseConfigurationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DatabaseConfigurationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DatabaseConfigurationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DatabaseConfigurationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def processor_count(self):
        """
        Gets the processor_count of this DatabaseConfigurationSummary.
        Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.


        :return: The processor_count of this DatabaseConfigurationSummary.
        :rtype: int
        """
        return self._processor_count

    @processor_count.setter
    def processor_count(self, processor_count):
        """
        Sets the processor_count of this DatabaseConfigurationSummary.
        Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.


        :param processor_count: The processor_count of this DatabaseConfigurationSummary.
        :type: int
        """
        self._processor_count = processor_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
