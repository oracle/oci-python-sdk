# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSensitiveDataModelDetails(object):
    """
    Details to update a sensitive data model. Note that updating any attribute of a sensitive data model does not perform data discovery.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSensitiveDataModelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateSensitiveDataModelDetails.
        :type display_name: str

        :param target_id:
            The value to assign to the target_id property of this UpdateSensitiveDataModelDetails.
        :type target_id: str

        :param app_suite_name:
            The value to assign to the app_suite_name property of this UpdateSensitiveDataModelDetails.
        :type app_suite_name: str

        :param description:
            The value to assign to the description property of this UpdateSensitiveDataModelDetails.
        :type description: str

        :param schemas_for_discovery:
            The value to assign to the schemas_for_discovery property of this UpdateSensitiveDataModelDetails.
        :type schemas_for_discovery: list[str]

        :param sensitive_type_ids_for_discovery:
            The value to assign to the sensitive_type_ids_for_discovery property of this UpdateSensitiveDataModelDetails.
        :type sensitive_type_ids_for_discovery: list[str]

        :param is_sample_data_collection_enabled:
            The value to assign to the is_sample_data_collection_enabled property of this UpdateSensitiveDataModelDetails.
        :type is_sample_data_collection_enabled: bool

        :param is_app_defined_relation_discovery_enabled:
            The value to assign to the is_app_defined_relation_discovery_enabled property of this UpdateSensitiveDataModelDetails.
        :type is_app_defined_relation_discovery_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSensitiveDataModelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSensitiveDataModelDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'target_id': 'str',
            'app_suite_name': 'str',
            'description': 'str',
            'schemas_for_discovery': 'list[str]',
            'sensitive_type_ids_for_discovery': 'list[str]',
            'is_sample_data_collection_enabled': 'bool',
            'is_app_defined_relation_discovery_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'target_id': 'targetId',
            'app_suite_name': 'appSuiteName',
            'description': 'description',
            'schemas_for_discovery': 'schemasForDiscovery',
            'sensitive_type_ids_for_discovery': 'sensitiveTypeIdsForDiscovery',
            'is_sample_data_collection_enabled': 'isSampleDataCollectionEnabled',
            'is_app_defined_relation_discovery_enabled': 'isAppDefinedRelationDiscoveryEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._target_id = None
        self._app_suite_name = None
        self._description = None
        self._schemas_for_discovery = None
        self._sensitive_type_ids_for_discovery = None
        self._is_sample_data_collection_enabled = None
        self._is_app_defined_relation_discovery_enabled = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateSensitiveDataModelDetails.
        The display name of the sensitive data model. The name does not have to be unique, and it's changeable.


        :return: The display_name of this UpdateSensitiveDataModelDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateSensitiveDataModelDetails.
        The display name of the sensitive data model. The name does not have to be unique, and it's changeable.


        :param display_name: The display_name of this UpdateSensitiveDataModelDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def target_id(self):
        """
        Gets the target_id of this UpdateSensitiveDataModelDetails.
        The OCID of the reference target database to be associated with the sensitive data model. All operations such as
        performing data discovery and adding columns manually are done in the context of the associated target database.
        Note that updating the targetId attribute does not perform data discovery automatically.


        :return: The target_id of this UpdateSensitiveDataModelDetails.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this UpdateSensitiveDataModelDetails.
        The OCID of the reference target database to be associated with the sensitive data model. All operations such as
        performing data discovery and adding columns manually are done in the context of the associated target database.
        Note that updating the targetId attribute does not perform data discovery automatically.


        :param target_id: The target_id of this UpdateSensitiveDataModelDetails.
        :type: str
        """
        self._target_id = target_id

    @property
    def app_suite_name(self):
        """
        Gets the app_suite_name of this UpdateSensitiveDataModelDetails.
        The application suite name identifying a collection of applications. It's useful only if maintaining a sensitive data model for a suite of applications.


        :return: The app_suite_name of this UpdateSensitiveDataModelDetails.
        :rtype: str
        """
        return self._app_suite_name

    @app_suite_name.setter
    def app_suite_name(self, app_suite_name):
        """
        Sets the app_suite_name of this UpdateSensitiveDataModelDetails.
        The application suite name identifying a collection of applications. It's useful only if maintaining a sensitive data model for a suite of applications.


        :param app_suite_name: The app_suite_name of this UpdateSensitiveDataModelDetails.
        :type: str
        """
        self._app_suite_name = app_suite_name

    @property
    def description(self):
        """
        Gets the description of this UpdateSensitiveDataModelDetails.
        The description of the sensitive data model.


        :return: The description of this UpdateSensitiveDataModelDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateSensitiveDataModelDetails.
        The description of the sensitive data model.


        :param description: The description of this UpdateSensitiveDataModelDetails.
        :type: str
        """
        self._description = description

    @property
    def schemas_for_discovery(self):
        """
        Gets the schemas_for_discovery of this UpdateSensitiveDataModelDetails.
        The schemas to be used for future data discovery jobs.


        :return: The schemas_for_discovery of this UpdateSensitiveDataModelDetails.
        :rtype: list[str]
        """
        return self._schemas_for_discovery

    @schemas_for_discovery.setter
    def schemas_for_discovery(self, schemas_for_discovery):
        """
        Sets the schemas_for_discovery of this UpdateSensitiveDataModelDetails.
        The schemas to be used for future data discovery jobs.


        :param schemas_for_discovery: The schemas_for_discovery of this UpdateSensitiveDataModelDetails.
        :type: list[str]
        """
        self._schemas_for_discovery = schemas_for_discovery

    @property
    def sensitive_type_ids_for_discovery(self):
        """
        Gets the sensitive_type_ids_for_discovery of this UpdateSensitiveDataModelDetails.
        The OCIDs of the sensitive types to be used for future data discovery jobs. If OCID of a sensitive category is
        provided, all its child sensitive types are used for data discovery.


        :return: The sensitive_type_ids_for_discovery of this UpdateSensitiveDataModelDetails.
        :rtype: list[str]
        """
        return self._sensitive_type_ids_for_discovery

    @sensitive_type_ids_for_discovery.setter
    def sensitive_type_ids_for_discovery(self, sensitive_type_ids_for_discovery):
        """
        Sets the sensitive_type_ids_for_discovery of this UpdateSensitiveDataModelDetails.
        The OCIDs of the sensitive types to be used for future data discovery jobs. If OCID of a sensitive category is
        provided, all its child sensitive types are used for data discovery.


        :param sensitive_type_ids_for_discovery: The sensitive_type_ids_for_discovery of this UpdateSensitiveDataModelDetails.
        :type: list[str]
        """
        self._sensitive_type_ids_for_discovery = sensitive_type_ids_for_discovery

    @property
    def is_sample_data_collection_enabled(self):
        """
        Gets the is_sample_data_collection_enabled of this UpdateSensitiveDataModelDetails.
        Indicates if data discovery jobs should collect and store sample data values for the discovered columns.
        Sample data helps review the discovered columns and ensure that they actually contain sensitive data.
        As it collects original data from the target database, it's disabled by default and should be used only
        if it's acceptable to store sample data in Data Safe's repository in Oracle Cloud. Note that sample data
        values are not collected for columns with the following data types: LONG, LOB, RAW, XMLTYPE and BFILE.


        :return: The is_sample_data_collection_enabled of this UpdateSensitiveDataModelDetails.
        :rtype: bool
        """
        return self._is_sample_data_collection_enabled

    @is_sample_data_collection_enabled.setter
    def is_sample_data_collection_enabled(self, is_sample_data_collection_enabled):
        """
        Sets the is_sample_data_collection_enabled of this UpdateSensitiveDataModelDetails.
        Indicates if data discovery jobs should collect and store sample data values for the discovered columns.
        Sample data helps review the discovered columns and ensure that they actually contain sensitive data.
        As it collects original data from the target database, it's disabled by default and should be used only
        if it's acceptable to store sample data in Data Safe's repository in Oracle Cloud. Note that sample data
        values are not collected for columns with the following data types: LONG, LOB, RAW, XMLTYPE and BFILE.


        :param is_sample_data_collection_enabled: The is_sample_data_collection_enabled of this UpdateSensitiveDataModelDetails.
        :type: bool
        """
        self._is_sample_data_collection_enabled = is_sample_data_collection_enabled

    @property
    def is_app_defined_relation_discovery_enabled(self):
        """
        Gets the is_app_defined_relation_discovery_enabled of this UpdateSensitiveDataModelDetails.
        Indicates if data discovery jobs should identify potential application-level (non-dictionary) referential
        relationships between columns. Note that data discovery automatically identifies and adds database-level
        (dictionary-defined) relationships. This option helps identify application-level relationships that are not
        defined in the database dictionary, which in turn, helps identify additional sensitive columns and preserve
        referential integrity during data masking. It's disabled by default and should be used only if there is a
        need to identify application-level relationships.


        :return: The is_app_defined_relation_discovery_enabled of this UpdateSensitiveDataModelDetails.
        :rtype: bool
        """
        return self._is_app_defined_relation_discovery_enabled

    @is_app_defined_relation_discovery_enabled.setter
    def is_app_defined_relation_discovery_enabled(self, is_app_defined_relation_discovery_enabled):
        """
        Sets the is_app_defined_relation_discovery_enabled of this UpdateSensitiveDataModelDetails.
        Indicates if data discovery jobs should identify potential application-level (non-dictionary) referential
        relationships between columns. Note that data discovery automatically identifies and adds database-level
        (dictionary-defined) relationships. This option helps identify application-level relationships that are not
        defined in the database dictionary, which in turn, helps identify additional sensitive columns and preserve
        referential integrity during data masking. It's disabled by default and should be used only if there is a
        need to identify application-level relationships.


        :param is_app_defined_relation_discovery_enabled: The is_app_defined_relation_discovery_enabled of this UpdateSensitiveDataModelDetails.
        :type: bool
        """
        self._is_app_defined_relation_discovery_enabled = is_app_defined_relation_discovery_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSensitiveDataModelDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateSensitiveDataModelDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSensitiveDataModelDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateSensitiveDataModelDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSensitiveDataModelDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateSensitiveDataModelDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSensitiveDataModelDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateSensitiveDataModelDetails.
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
