# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalPublicationSummary(object):
    """
    The external publication summary contains the audit summary information and the definition of the external object.
    """

    #: A constant which can be used with the status property of a ExternalPublicationSummary.
    #: This constant has a value of "SUCCESSFUL"
    STATUS_SUCCESSFUL = "SUCCESSFUL"

    #: A constant which can be used with the status property of a ExternalPublicationSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a ExternalPublicationSummary.
    #: This constant has a value of "PUBLISHING"
    STATUS_PUBLISHING = "PUBLISHING"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalPublicationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param application_id:
            The value to assign to the application_id property of this ExternalPublicationSummary.
        :type application_id: str

        :param application_compartment_id:
            The value to assign to the application_compartment_id property of this ExternalPublicationSummary.
        :type application_compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalPublicationSummary.
        :type display_name: str

        :param resource_configuration:
            The value to assign to the resource_configuration property of this ExternalPublicationSummary.
        :type resource_configuration: oci.data_integration.models.ResourceConfiguration

        :param configuration_details:
            The value to assign to the configuration_details property of this ExternalPublicationSummary.
        :type configuration_details: oci.data_integration.models.ConfigurationDetails

        :param status:
            The value to assign to the status property of this ExternalPublicationSummary.
            Allowed values for this property are: "SUCCESSFUL", "FAILED", "PUBLISHING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param error_message:
            The value to assign to the error_message property of this ExternalPublicationSummary.
        :type error_message: str

        :param key:
            The value to assign to the key property of this ExternalPublicationSummary.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this ExternalPublicationSummary.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this ExternalPublicationSummary.
        :type model_version: str

        :param name:
            The value to assign to the name property of this ExternalPublicationSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this ExternalPublicationSummary.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this ExternalPublicationSummary.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this ExternalPublicationSummary.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this ExternalPublicationSummary.
        :type identifier: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ExternalPublicationSummary.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param metadata:
            The value to assign to the metadata property of this ExternalPublicationSummary.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this ExternalPublicationSummary.
        :type key_map: dict(str, str)

        """
        self.swagger_types = {
            'application_id': 'str',
            'application_compartment_id': 'str',
            'display_name': 'str',
            'resource_configuration': 'ResourceConfiguration',
            'configuration_details': 'ConfigurationDetails',
            'status': 'str',
            'error_message': 'str',
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'parent_ref': 'ParentReference',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)'
        }

        self.attribute_map = {
            'application_id': 'applicationId',
            'application_compartment_id': 'applicationCompartmentId',
            'display_name': 'displayName',
            'resource_configuration': 'resourceConfiguration',
            'configuration_details': 'configurationDetails',
            'status': 'status',
            'error_message': 'errorMessage',
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'parent_ref': 'parentRef',
            'metadata': 'metadata',
            'key_map': 'keyMap'
        }

        self._application_id = None
        self._application_compartment_id = None
        self._display_name = None
        self._resource_configuration = None
        self._configuration_details = None
        self._status = None
        self._error_message = None
        self._key = None
        self._model_type = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._parent_ref = None
        self._metadata = None
        self._key_map = None

    @property
    def application_id(self):
        """
        Gets the application_id of this ExternalPublicationSummary.
        The unique OCID of the identifier that is returned after creating the Oracle Cloud Infrastructure Data Flow application.


        :return: The application_id of this ExternalPublicationSummary.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """
        Sets the application_id of this ExternalPublicationSummary.
        The unique OCID of the identifier that is returned after creating the Oracle Cloud Infrastructure Data Flow application.


        :param application_id: The application_id of this ExternalPublicationSummary.
        :type: str
        """
        self._application_id = application_id

    @property
    def application_compartment_id(self):
        """
        Gets the application_compartment_id of this ExternalPublicationSummary.
        The OCID of the compartment where the application is created in the Oracle Cloud Infrastructure Data Flow Service.


        :return: The application_compartment_id of this ExternalPublicationSummary.
        :rtype: str
        """
        return self._application_compartment_id

    @application_compartment_id.setter
    def application_compartment_id(self, application_compartment_id):
        """
        Sets the application_compartment_id of this ExternalPublicationSummary.
        The OCID of the compartment where the application is created in the Oracle Cloud Infrastructure Data Flow Service.


        :param application_compartment_id: The application_compartment_id of this ExternalPublicationSummary.
        :type: str
        """
        self._application_compartment_id = application_compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this ExternalPublicationSummary.
        The name of the application.


        :return: The display_name of this ExternalPublicationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExternalPublicationSummary.
        The name of the application.


        :param display_name: The display_name of this ExternalPublicationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def resource_configuration(self):
        """
        Gets the resource_configuration of this ExternalPublicationSummary.

        :return: The resource_configuration of this ExternalPublicationSummary.
        :rtype: oci.data_integration.models.ResourceConfiguration
        """
        return self._resource_configuration

    @resource_configuration.setter
    def resource_configuration(self, resource_configuration):
        """
        Sets the resource_configuration of this ExternalPublicationSummary.

        :param resource_configuration: The resource_configuration of this ExternalPublicationSummary.
        :type: oci.data_integration.models.ResourceConfiguration
        """
        self._resource_configuration = resource_configuration

    @property
    def configuration_details(self):
        """
        Gets the configuration_details of this ExternalPublicationSummary.

        :return: The configuration_details of this ExternalPublicationSummary.
        :rtype: oci.data_integration.models.ConfigurationDetails
        """
        return self._configuration_details

    @configuration_details.setter
    def configuration_details(self, configuration_details):
        """
        Sets the configuration_details of this ExternalPublicationSummary.

        :param configuration_details: The configuration_details of this ExternalPublicationSummary.
        :type: oci.data_integration.models.ConfigurationDetails
        """
        self._configuration_details = configuration_details

    @property
    def status(self):
        """
        Gets the status of this ExternalPublicationSummary.
        The status of the publishing action to Oracle Cloud Infrastructure Data Flow.

        Allowed values for this property are: "SUCCESSFUL", "FAILED", "PUBLISHING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ExternalPublicationSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ExternalPublicationSummary.
        The status of the publishing action to Oracle Cloud Infrastructure Data Flow.


        :param status: The status of this ExternalPublicationSummary.
        :type: str
        """
        allowed_values = ["SUCCESSFUL", "FAILED", "PUBLISHING"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def error_message(self):
        """
        Gets the error_message of this ExternalPublicationSummary.
        The error of the published object in the application.


        :return: The error_message of this ExternalPublicationSummary.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ExternalPublicationSummary.
        The error of the published object in the application.


        :param error_message: The error_message of this ExternalPublicationSummary.
        :type: str
        """
        self._error_message = error_message

    @property
    def key(self):
        """
        Gets the key of this ExternalPublicationSummary.
        The object key.


        :return: The key of this ExternalPublicationSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ExternalPublicationSummary.
        The object key.


        :param key: The key of this ExternalPublicationSummary.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this ExternalPublicationSummary.
        The object type.


        :return: The model_type of this ExternalPublicationSummary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this ExternalPublicationSummary.
        The object type.


        :param model_type: The model_type of this ExternalPublicationSummary.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this ExternalPublicationSummary.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :return: The model_version of this ExternalPublicationSummary.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this ExternalPublicationSummary.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :param model_version: The model_version of this ExternalPublicationSummary.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this ExternalPublicationSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this ExternalPublicationSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExternalPublicationSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this ExternalPublicationSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ExternalPublicationSummary.
        Detailed description for the object.


        :return: The description of this ExternalPublicationSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExternalPublicationSummary.
        Detailed description for the object.


        :param description: The description of this ExternalPublicationSummary.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this ExternalPublicationSummary.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this ExternalPublicationSummary.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this ExternalPublicationSummary.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this ExternalPublicationSummary.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this ExternalPublicationSummary.
        The status of an object that can be set to value 1 for shallow references across objects. Other values are reserved.


        :return: The object_status of this ExternalPublicationSummary.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this ExternalPublicationSummary.
        The status of an object that can be set to value 1 for shallow references across objects. Other values are reserved.


        :param object_status: The object_status of this ExternalPublicationSummary.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this ExternalPublicationSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this ExternalPublicationSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ExternalPublicationSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this ExternalPublicationSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this ExternalPublicationSummary.

        :return: The parent_ref of this ExternalPublicationSummary.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this ExternalPublicationSummary.

        :param parent_ref: The parent_ref of this ExternalPublicationSummary.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def metadata(self):
        """
        Gets the metadata of this ExternalPublicationSummary.

        :return: The metadata of this ExternalPublicationSummary.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this ExternalPublicationSummary.

        :param metadata: The metadata of this ExternalPublicationSummary.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    @property
    def key_map(self):
        """
        Gets the key_map of this ExternalPublicationSummary.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :return: The key_map of this ExternalPublicationSummary.
        :rtype: dict(str, str)
        """
        return self._key_map

    @key_map.setter
    def key_map(self, key_map):
        """
        Sets the key_map of this ExternalPublicationSummary.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :param key_map: The key_map of this ExternalPublicationSummary.
        :type: dict(str, str)
        """
        self._key_map = key_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
