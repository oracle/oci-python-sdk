# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDiscoveryJobDetails(object):
    """
    Details to create a new data discovery job.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDiscoveryJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param discovery_type:
            The value to assign to the discovery_type property of this CreateDiscoveryJobDetails.
        :type discovery_type: str

        :param sensitive_data_model_id:
            The value to assign to the sensitive_data_model_id property of this CreateDiscoveryJobDetails.
        :type sensitive_data_model_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDiscoveryJobDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateDiscoveryJobDetails.
        :type display_name: str

        :param schemas_for_discovery:
            The value to assign to the schemas_for_discovery property of this CreateDiscoveryJobDetails.
        :type schemas_for_discovery: list[str]

        :param sensitive_type_ids_for_discovery:
            The value to assign to the sensitive_type_ids_for_discovery property of this CreateDiscoveryJobDetails.
        :type sensitive_type_ids_for_discovery: list[str]

        :param is_sample_data_collection_enabled:
            The value to assign to the is_sample_data_collection_enabled property of this CreateDiscoveryJobDetails.
        :type is_sample_data_collection_enabled: bool

        :param is_app_defined_relation_discovery_enabled:
            The value to assign to the is_app_defined_relation_discovery_enabled property of this CreateDiscoveryJobDetails.
        :type is_app_defined_relation_discovery_enabled: bool

        :param is_include_all_schemas:
            The value to assign to the is_include_all_schemas property of this CreateDiscoveryJobDetails.
        :type is_include_all_schemas: bool

        :param is_include_all_sensitive_types:
            The value to assign to the is_include_all_sensitive_types property of this CreateDiscoveryJobDetails.
        :type is_include_all_sensitive_types: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDiscoveryJobDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDiscoveryJobDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'discovery_type': 'str',
            'sensitive_data_model_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'schemas_for_discovery': 'list[str]',
            'sensitive_type_ids_for_discovery': 'list[str]',
            'is_sample_data_collection_enabled': 'bool',
            'is_app_defined_relation_discovery_enabled': 'bool',
            'is_include_all_schemas': 'bool',
            'is_include_all_sensitive_types': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'discovery_type': 'discoveryType',
            'sensitive_data_model_id': 'sensitiveDataModelId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'schemas_for_discovery': 'schemasForDiscovery',
            'sensitive_type_ids_for_discovery': 'sensitiveTypeIdsForDiscovery',
            'is_sample_data_collection_enabled': 'isSampleDataCollectionEnabled',
            'is_app_defined_relation_discovery_enabled': 'isAppDefinedRelationDiscoveryEnabled',
            'is_include_all_schemas': 'isIncludeAllSchemas',
            'is_include_all_sensitive_types': 'isIncludeAllSensitiveTypes',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._discovery_type = None
        self._sensitive_data_model_id = None
        self._compartment_id = None
        self._display_name = None
        self._schemas_for_discovery = None
        self._sensitive_type_ids_for_discovery = None
        self._is_sample_data_collection_enabled = None
        self._is_app_defined_relation_discovery_enabled = None
        self._is_include_all_schemas = None
        self._is_include_all_sensitive_types = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def discovery_type(self):
        """
        Gets the discovery_type of this CreateDiscoveryJobDetails.
        The type of the discovery job. It defines the job's scope.
        NEW identifies new sensitive columns in the target database that are not in the sensitive data model.
        DELETED identifies columns that are present in the sensitive data model but have been deleted from the target database.
        MODIFIED identifies columns that are present in the target database as well as the sensitive data model but some of their attributes have been modified.
        ALL covers all the above three scenarios and reports new, deleted and modified columns.


        :return: The discovery_type of this CreateDiscoveryJobDetails.
        :rtype: str
        """
        return self._discovery_type

    @discovery_type.setter
    def discovery_type(self, discovery_type):
        """
        Sets the discovery_type of this CreateDiscoveryJobDetails.
        The type of the discovery job. It defines the job's scope.
        NEW identifies new sensitive columns in the target database that are not in the sensitive data model.
        DELETED identifies columns that are present in the sensitive data model but have been deleted from the target database.
        MODIFIED identifies columns that are present in the target database as well as the sensitive data model but some of their attributes have been modified.
        ALL covers all the above three scenarios and reports new, deleted and modified columns.


        :param discovery_type: The discovery_type of this CreateDiscoveryJobDetails.
        :type: str
        """
        self._discovery_type = discovery_type

    @property
    def sensitive_data_model_id(self):
        """
        **[Required]** Gets the sensitive_data_model_id of this CreateDiscoveryJobDetails.
        The OCID of the sensitive data model.


        :return: The sensitive_data_model_id of this CreateDiscoveryJobDetails.
        :rtype: str
        """
        return self._sensitive_data_model_id

    @sensitive_data_model_id.setter
    def sensitive_data_model_id(self, sensitive_data_model_id):
        """
        Sets the sensitive_data_model_id of this CreateDiscoveryJobDetails.
        The OCID of the sensitive data model.


        :param sensitive_data_model_id: The sensitive_data_model_id of this CreateDiscoveryJobDetails.
        :type: str
        """
        self._sensitive_data_model_id = sensitive_data_model_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDiscoveryJobDetails.
        The OCID of the compartment where the discovery job resource should be created.


        :return: The compartment_id of this CreateDiscoveryJobDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDiscoveryJobDetails.
        The OCID of the compartment where the discovery job resource should be created.


        :param compartment_id: The compartment_id of this CreateDiscoveryJobDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDiscoveryJobDetails.
        A user-friendly name for the discovery job. Does not have to be unique, and it is changeable. Avoid entering confidential information.


        :return: The display_name of this CreateDiscoveryJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDiscoveryJobDetails.
        A user-friendly name for the discovery job. Does not have to be unique, and it is changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDiscoveryJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def schemas_for_discovery(self):
        """
        Gets the schemas_for_discovery of this CreateDiscoveryJobDetails.
        The schemas to be scanned by the discovery job. If not provided, the schemasForDiscovery attribute of the sensitive
        data model is used to get the list of schemas.


        :return: The schemas_for_discovery of this CreateDiscoveryJobDetails.
        :rtype: list[str]
        """
        return self._schemas_for_discovery

    @schemas_for_discovery.setter
    def schemas_for_discovery(self, schemas_for_discovery):
        """
        Sets the schemas_for_discovery of this CreateDiscoveryJobDetails.
        The schemas to be scanned by the discovery job. If not provided, the schemasForDiscovery attribute of the sensitive
        data model is used to get the list of schemas.


        :param schemas_for_discovery: The schemas_for_discovery of this CreateDiscoveryJobDetails.
        :type: list[str]
        """
        self._schemas_for_discovery = schemas_for_discovery

    @property
    def sensitive_type_ids_for_discovery(self):
        """
        Gets the sensitive_type_ids_for_discovery of this CreateDiscoveryJobDetails.
        The OCIDs of the sensitive types to be used by the discovery job. If not provided, the sensitiveTypeIdsForDiscovery
        attribute of the sensitive data model is used to get the list of sensitive types.


        :return: The sensitive_type_ids_for_discovery of this CreateDiscoveryJobDetails.
        :rtype: list[str]
        """
        return self._sensitive_type_ids_for_discovery

    @sensitive_type_ids_for_discovery.setter
    def sensitive_type_ids_for_discovery(self, sensitive_type_ids_for_discovery):
        """
        Sets the sensitive_type_ids_for_discovery of this CreateDiscoveryJobDetails.
        The OCIDs of the sensitive types to be used by the discovery job. If not provided, the sensitiveTypeIdsForDiscovery
        attribute of the sensitive data model is used to get the list of sensitive types.


        :param sensitive_type_ids_for_discovery: The sensitive_type_ids_for_discovery of this CreateDiscoveryJobDetails.
        :type: list[str]
        """
        self._sensitive_type_ids_for_discovery = sensitive_type_ids_for_discovery

    @property
    def is_sample_data_collection_enabled(self):
        """
        Gets the is_sample_data_collection_enabled of this CreateDiscoveryJobDetails.
        Indicates if the discovery job should collect and store sample data values for the discovered columns. Sample data
        helps review the discovered columns and ensure that they actually contain sensitive data. As it collects original
        data from the target database, it's disabled by default and should be used only if it's acceptable to store sample
        data in Data Safe's repository in Oracle Cloud. Note that sample data values are not collected for columns with the
        following data types: LONG, LOB, RAW, XMLTYPE and BFILE.


        :return: The is_sample_data_collection_enabled of this CreateDiscoveryJobDetails.
        :rtype: bool
        """
        return self._is_sample_data_collection_enabled

    @is_sample_data_collection_enabled.setter
    def is_sample_data_collection_enabled(self, is_sample_data_collection_enabled):
        """
        Sets the is_sample_data_collection_enabled of this CreateDiscoveryJobDetails.
        Indicates if the discovery job should collect and store sample data values for the discovered columns. Sample data
        helps review the discovered columns and ensure that they actually contain sensitive data. As it collects original
        data from the target database, it's disabled by default and should be used only if it's acceptable to store sample
        data in Data Safe's repository in Oracle Cloud. Note that sample data values are not collected for columns with the
        following data types: LONG, LOB, RAW, XMLTYPE and BFILE.


        :param is_sample_data_collection_enabled: The is_sample_data_collection_enabled of this CreateDiscoveryJobDetails.
        :type: bool
        """
        self._is_sample_data_collection_enabled = is_sample_data_collection_enabled

    @property
    def is_app_defined_relation_discovery_enabled(self):
        """
        Gets the is_app_defined_relation_discovery_enabled of this CreateDiscoveryJobDetails.
        Indicates if the discovery job should identify potential application-level (non-dictionary) referential relationships
        between columns. Note that data discovery automatically identifies and adds database-level (dictionary-defined)
        relationships. This option helps identify application-level relationships that are not defined in the database
        dictionary, which in turn, helps identify additional sensitive columns and preserve referential integrity during
        data masking. It's disabled by default and should be used only if there is a need to identify application-level
        relationships.


        :return: The is_app_defined_relation_discovery_enabled of this CreateDiscoveryJobDetails.
        :rtype: bool
        """
        return self._is_app_defined_relation_discovery_enabled

    @is_app_defined_relation_discovery_enabled.setter
    def is_app_defined_relation_discovery_enabled(self, is_app_defined_relation_discovery_enabled):
        """
        Sets the is_app_defined_relation_discovery_enabled of this CreateDiscoveryJobDetails.
        Indicates if the discovery job should identify potential application-level (non-dictionary) referential relationships
        between columns. Note that data discovery automatically identifies and adds database-level (dictionary-defined)
        relationships. This option helps identify application-level relationships that are not defined in the database
        dictionary, which in turn, helps identify additional sensitive columns and preserve referential integrity during
        data masking. It's disabled by default and should be used only if there is a need to identify application-level
        relationships.


        :param is_app_defined_relation_discovery_enabled: The is_app_defined_relation_discovery_enabled of this CreateDiscoveryJobDetails.
        :type: bool
        """
        self._is_app_defined_relation_discovery_enabled = is_app_defined_relation_discovery_enabled

    @property
    def is_include_all_schemas(self):
        """
        Gets the is_include_all_schemas of this CreateDiscoveryJobDetails.
        Indicates if all the schemas should be scanned by the discovery job. If it's set to true, the schemasForDiscovery
        attribute is ignored and all schemas are used for data discovery. If both attributes are not provided, the configuration
        from the sensitive data model is used.


        :return: The is_include_all_schemas of this CreateDiscoveryJobDetails.
        :rtype: bool
        """
        return self._is_include_all_schemas

    @is_include_all_schemas.setter
    def is_include_all_schemas(self, is_include_all_schemas):
        """
        Sets the is_include_all_schemas of this CreateDiscoveryJobDetails.
        Indicates if all the schemas should be scanned by the discovery job. If it's set to true, the schemasForDiscovery
        attribute is ignored and all schemas are used for data discovery. If both attributes are not provided, the configuration
        from the sensitive data model is used.


        :param is_include_all_schemas: The is_include_all_schemas of this CreateDiscoveryJobDetails.
        :type: bool
        """
        self._is_include_all_schemas = is_include_all_schemas

    @property
    def is_include_all_sensitive_types(self):
        """
        Gets the is_include_all_sensitive_types of this CreateDiscoveryJobDetails.
        Indicates if all the existing sensitive types should be used by the discovery job. If it's set to true, the
        sensitiveTypeIdsForDiscovery attribute is ignored and all sensitive types are used for data discovery. If both
        attributes are not provided, the configuration from the sensitive data model is used.


        :return: The is_include_all_sensitive_types of this CreateDiscoveryJobDetails.
        :rtype: bool
        """
        return self._is_include_all_sensitive_types

    @is_include_all_sensitive_types.setter
    def is_include_all_sensitive_types(self, is_include_all_sensitive_types):
        """
        Sets the is_include_all_sensitive_types of this CreateDiscoveryJobDetails.
        Indicates if all the existing sensitive types should be used by the discovery job. If it's set to true, the
        sensitiveTypeIdsForDiscovery attribute is ignored and all sensitive types are used for data discovery. If both
        attributes are not provided, the configuration from the sensitive data model is used.


        :param is_include_all_sensitive_types: The is_include_all_sensitive_types of this CreateDiscoveryJobDetails.
        :type: bool
        """
        self._is_include_all_sensitive_types = is_include_all_sensitive_types

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDiscoveryJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDiscoveryJobDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDiscoveryJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDiscoveryJobDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDiscoveryJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDiscoveryJobDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDiscoveryJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDiscoveryJobDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
