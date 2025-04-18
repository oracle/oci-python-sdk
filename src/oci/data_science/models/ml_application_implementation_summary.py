# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MlApplicationImplementationSummary(object):
    """
    Summary of the MlApplicationImplementation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MlApplicationImplementationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MlApplicationImplementationSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this MlApplicationImplementationSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this MlApplicationImplementationSummary.
        :type description: str

        :param ml_application_id:
            The value to assign to the ml_application_id property of this MlApplicationImplementationSummary.
        :type ml_application_id: str

        :param ml_application_name:
            The value to assign to the ml_application_name property of this MlApplicationImplementationSummary.
        :type ml_application_name: str

        :param package_version:
            The value to assign to the package_version property of this MlApplicationImplementationSummary.
        :type package_version: str

        :param configuration_schema:
            The value to assign to the configuration_schema property of this MlApplicationImplementationSummary.
        :type configuration_schema: list[oci.data_science.models.ConfigurationPropertySchema]

        :param allowed_migration_destinations:
            The value to assign to the allowed_migration_destinations property of this MlApplicationImplementationSummary.
        :type allowed_migration_destinations: list[str]

        :param compartment_id:
            The value to assign to the compartment_id property of this MlApplicationImplementationSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this MlApplicationImplementationSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MlApplicationImplementationSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MlApplicationImplementationSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MlApplicationImplementationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MlApplicationImplementationSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'ml_application_id': 'str',
            'ml_application_name': 'str',
            'package_version': 'str',
            'configuration_schema': 'list[ConfigurationPropertySchema]',
            'allowed_migration_destinations': 'list[str]',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'ml_application_id': 'mlApplicationId',
            'ml_application_name': 'mlApplicationName',
            'package_version': 'packageVersion',
            'configuration_schema': 'configurationSchema',
            'allowed_migration_destinations': 'allowedMigrationDestinations',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._name = None
        self._description = None
        self._ml_application_id = None
        self._ml_application_name = None
        self._package_version = None
        self._configuration_schema = None
        self._allowed_migration_destinations = None
        self._compartment_id = None
        self._time_created = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MlApplicationImplementationSummary.
        The OCID of the MlApplicationImplementation. Unique identifier that is immutable after creation.


        :return: The id of this MlApplicationImplementationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MlApplicationImplementationSummary.
        The OCID of the MlApplicationImplementation. Unique identifier that is immutable after creation.


        :param id: The id of this MlApplicationImplementationSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MlApplicationImplementationSummary.
        ML Application Implementation name which is unique for given ML Application.


        :return: The name of this MlApplicationImplementationSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MlApplicationImplementationSummary.
        ML Application Implementation name which is unique for given ML Application.


        :param name: The name of this MlApplicationImplementationSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this MlApplicationImplementationSummary.
        Description of ML Application Implementation defined in ML Application package descriptor


        :return: The description of this MlApplicationImplementationSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MlApplicationImplementationSummary.
        Description of ML Application Implementation defined in ML Application package descriptor


        :param description: The description of this MlApplicationImplementationSummary.
        :type: str
        """
        self._description = description

    @property
    def ml_application_id(self):
        """
        **[Required]** Gets the ml_application_id of this MlApplicationImplementationSummary.
        The OCID of the ML Application implemented by this ML Application Implementation.


        :return: The ml_application_id of this MlApplicationImplementationSummary.
        :rtype: str
        """
        return self._ml_application_id

    @ml_application_id.setter
    def ml_application_id(self, ml_application_id):
        """
        Sets the ml_application_id of this MlApplicationImplementationSummary.
        The OCID of the ML Application implemented by this ML Application Implementation.


        :param ml_application_id: The ml_application_id of this MlApplicationImplementationSummary.
        :type: str
        """
        self._ml_application_id = ml_application_id

    @property
    def ml_application_name(self):
        """
        **[Required]** Gets the ml_application_name of this MlApplicationImplementationSummary.
        The name of ML Application (based on mlApplicationId).


        :return: The ml_application_name of this MlApplicationImplementationSummary.
        :rtype: str
        """
        return self._ml_application_name

    @ml_application_name.setter
    def ml_application_name(self, ml_application_name):
        """
        Sets the ml_application_name of this MlApplicationImplementationSummary.
        The name of ML Application (based on mlApplicationId).


        :param ml_application_name: The ml_application_name of this MlApplicationImplementationSummary.
        :type: str
        """
        self._ml_application_name = ml_application_name

    @property
    def package_version(self):
        """
        Gets the package_version of this MlApplicationImplementationSummary.
        The version of ML Application Package (e.g. \"1.2\" or \"2.0.4\") defined in ML Application package descriptor. Value is not mandatory only for CREATING state otherwise it must be always presented.


        :return: The package_version of this MlApplicationImplementationSummary.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this MlApplicationImplementationSummary.
        The version of ML Application Package (e.g. \"1.2\" or \"2.0.4\") defined in ML Application package descriptor. Value is not mandatory only for CREATING state otherwise it must be always presented.


        :param package_version: The package_version of this MlApplicationImplementationSummary.
        :type: str
        """
        self._package_version = package_version

    @property
    def configuration_schema(self):
        """
        Gets the configuration_schema of this MlApplicationImplementationSummary.
        Schema of configuration which needs to be provided for each ML Application Instance. It is defined in the ML Application package descriptor.


        :return: The configuration_schema of this MlApplicationImplementationSummary.
        :rtype: list[oci.data_science.models.ConfigurationPropertySchema]
        """
        return self._configuration_schema

    @configuration_schema.setter
    def configuration_schema(self, configuration_schema):
        """
        Sets the configuration_schema of this MlApplicationImplementationSummary.
        Schema of configuration which needs to be provided for each ML Application Instance. It is defined in the ML Application package descriptor.


        :param configuration_schema: The configuration_schema of this MlApplicationImplementationSummary.
        :type: list[oci.data_science.models.ConfigurationPropertySchema]
        """
        self._configuration_schema = configuration_schema

    @property
    def allowed_migration_destinations(self):
        """
        Gets the allowed_migration_destinations of this MlApplicationImplementationSummary.
        List of ML Application Implementation OCIDs for which migration from this implementation is allowed. Migration means that if consumers change implementation for their instances to implementation with OCID from this list, instance components will be updated in place otherwise new instance components are created based on the new implementation and old instance components are removed.


        :return: The allowed_migration_destinations of this MlApplicationImplementationSummary.
        :rtype: list[str]
        """
        return self._allowed_migration_destinations

    @allowed_migration_destinations.setter
    def allowed_migration_destinations(self, allowed_migration_destinations):
        """
        Sets the allowed_migration_destinations of this MlApplicationImplementationSummary.
        List of ML Application Implementation OCIDs for which migration from this implementation is allowed. Migration means that if consumers change implementation for their instances to implementation with OCID from this list, instance components will be updated in place otherwise new instance components are created based on the new implementation and old instance components are removed.


        :param allowed_migration_destinations: The allowed_migration_destinations of this MlApplicationImplementationSummary.
        :type: list[str]
        """
        self._allowed_migration_destinations = allowed_migration_destinations

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MlApplicationImplementationSummary.
        The OCID of the compartment where the MlApplicationImplementation is created.


        :return: The compartment_id of this MlApplicationImplementationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MlApplicationImplementationSummary.
        The OCID of the compartment where the MlApplicationImplementation is created.


        :param compartment_id: The compartment_id of this MlApplicationImplementationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MlApplicationImplementationSummary.
        The time the MlApplicationImplementation was created. An RFC3339 formatted datetime string


        :return: The time_created of this MlApplicationImplementationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MlApplicationImplementationSummary.
        The time the MlApplicationImplementation was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this MlApplicationImplementationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MlApplicationImplementationSummary.
        The current state of the ML Application Implementation.


        :return: The lifecycle_state of this MlApplicationImplementationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MlApplicationImplementationSummary.
        The current state of the ML Application Implementation.


        :param lifecycle_state: The lifecycle_state of this MlApplicationImplementationSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this MlApplicationImplementationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this MlApplicationImplementationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MlApplicationImplementationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this MlApplicationImplementationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this MlApplicationImplementationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this MlApplicationImplementationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MlApplicationImplementationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this MlApplicationImplementationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MlApplicationImplementationSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MlApplicationImplementationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MlApplicationImplementationSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MlApplicationImplementationSummary.
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
