# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMigrationDetails(object):
    """
    An application being migrated from a source environment to OCI.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMigrationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMigrationDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateMigrationDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateMigrationDetails.
        :type description: str

        :param source_id:
            The value to assign to the source_id property of this CreateMigrationDetails.
        :type source_id: str

        :param application_name:
            The value to assign to the application_name property of this CreateMigrationDetails.
        :type application_name: str

        :param discovery_details:
            The value to assign to the discovery_details property of this CreateMigrationDetails.
        :type discovery_details: DiscoveryDetails

        :param service_config:
            The value to assign to the service_config property of this CreateMigrationDetails.
        :type service_config: dict(str, ConfigurationField)

        :param application_config:
            The value to assign to the application_config property of this CreateMigrationDetails.
        :type application_config: dict(str, ConfigurationField)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMigrationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMigrationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'source_id': 'str',
            'application_name': 'str',
            'discovery_details': 'DiscoveryDetails',
            'service_config': 'dict(str, ConfigurationField)',
            'application_config': 'dict(str, ConfigurationField)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'source_id': 'sourceId',
            'application_name': 'applicationName',
            'discovery_details': 'discoveryDetails',
            'service_config': 'serviceConfig',
            'application_config': 'applicationConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._source_id = None
        self._application_name = None
        self._discovery_details = None
        self._service_config = None
        self._application_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMigrationDetails.
        Unique idenfifier (OCID) for the compartment where the Source is located.


        :return: The compartment_id of this CreateMigrationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMigrationDetails.
        Unique idenfifier (OCID) for the compartment where the Source is located.


        :param compartment_id: The compartment_id of this CreateMigrationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateMigrationDetails.
        Human-readable name of the application.


        :return: The display_name of this CreateMigrationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMigrationDetails.
        Human-readable name of the application.


        :param display_name: The display_name of this CreateMigrationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateMigrationDetails.
        Description of the application.


        :return: The description of this CreateMigrationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateMigrationDetails.
        Description of the application.


        :param description: The description of this CreateMigrationDetails.
        :type: str
        """
        self._description = description

    @property
    def source_id(self):
        """
        **[Required]** Gets the source_id of this CreateMigrationDetails.
        Unique identifier (OCID) of the application source.


        :return: The source_id of this CreateMigrationDetails.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this CreateMigrationDetails.
        Unique identifier (OCID) of the application source.


        :param source_id: The source_id of this CreateMigrationDetails.
        :type: str
        """
        self._source_id = source_id

    @property
    def application_name(self):
        """
        **[Required]** Gets the application_name of this CreateMigrationDetails.
        Name of the application being migrated from the source.


        :return: The application_name of this CreateMigrationDetails.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """
        Sets the application_name of this CreateMigrationDetails.
        Name of the application being migrated from the source.


        :param application_name: The application_name of this CreateMigrationDetails.
        :type: str
        """
        self._application_name = application_name

    @property
    def discovery_details(self):
        """
        **[Required]** Gets the discovery_details of this CreateMigrationDetails.

        :return: The discovery_details of this CreateMigrationDetails.
        :rtype: DiscoveryDetails
        """
        return self._discovery_details

    @discovery_details.setter
    def discovery_details(self, discovery_details):
        """
        Sets the discovery_details of this CreateMigrationDetails.

        :param discovery_details: The discovery_details of this CreateMigrationDetails.
        :type: DiscoveryDetails
        """
        self._discovery_details = discovery_details

    @property
    def service_config(self):
        """
        Gets the service_config of this CreateMigrationDetails.
        Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.


        :return: The service_config of this CreateMigrationDetails.
        :rtype: dict(str, ConfigurationField)
        """
        return self._service_config

    @service_config.setter
    def service_config(self, service_config):
        """
        Sets the service_config of this CreateMigrationDetails.
        Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.


        :param service_config: The service_config of this CreateMigrationDetails.
        :type: dict(str, ConfigurationField)
        """
        self._service_config = service_config

    @property
    def application_config(self):
        """
        Gets the application_config of this CreateMigrationDetails.
        Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.


        :return: The application_config of this CreateMigrationDetails.
        :rtype: dict(str, ConfigurationField)
        """
        return self._application_config

    @application_config.setter
    def application_config(self, application_config):
        """
        Sets the application_config of this CreateMigrationDetails.
        Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.


        :param application_config: The application_config of this CreateMigrationDetails.
        :type: dict(str, ConfigurationField)
        """
        self._application_config = application_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMigrationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateMigrationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMigrationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateMigrationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateMigrationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateMigrationDetails.
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
