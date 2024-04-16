# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateWorkerDetails(object):
    """
    Details of the request body used to create a new worker for an On-premise vantage point.
    """

    #: A constant which can be used with the worker_type property of a CreateWorkerDetails.
    #: This constant has a value of "DOCKER"
    WORKER_TYPE_DOCKER = "DOCKER"

    #: A constant which can be used with the status property of a CreateWorkerDetails.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a CreateWorkerDetails.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateWorkerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateWorkerDetails.
        :type name: str

        :param version:
            The value to assign to the version property of this CreateWorkerDetails.
        :type version: str

        :param resource_principal_token_public_key:
            The value to assign to the resource_principal_token_public_key property of this CreateWorkerDetails.
        :type resource_principal_token_public_key: str

        :param configuration_details:
            The value to assign to the configuration_details property of this CreateWorkerDetails.
        :type configuration_details: object

        :param worker_type:
            The value to assign to the worker_type property of this CreateWorkerDetails.
            Allowed values for this property are: "DOCKER"
        :type worker_type: str

        :param status:
            The value to assign to the status property of this CreateWorkerDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type status: str

        :param priority:
            The value to assign to the priority property of this CreateWorkerDetails.
        :type priority: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateWorkerDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateWorkerDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'version': 'str',
            'resource_principal_token_public_key': 'str',
            'configuration_details': 'object',
            'worker_type': 'str',
            'status': 'str',
            'priority': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'resource_principal_token_public_key': 'resourcePrincipalTokenPublicKey',
            'configuration_details': 'configurationDetails',
            'worker_type': 'workerType',
            'status': 'status',
            'priority': 'priority',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._version = None
        self._resource_principal_token_public_key = None
        self._configuration_details = None
        self._worker_type = None
        self._status = None
        self._priority = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateWorkerDetails.
        Unique On-premise VP worker name that cannot be edited. The name should not contain any confidential information.


        :return: The name of this CreateWorkerDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateWorkerDetails.
        Unique On-premise VP worker name that cannot be edited. The name should not contain any confidential information.


        :param name: The name of this CreateWorkerDetails.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this CreateWorkerDetails.
        Image version of the On-premise VP worker.


        :return: The version of this CreateWorkerDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CreateWorkerDetails.
        Image version of the On-premise VP worker.


        :param version: The version of this CreateWorkerDetails.
        :type: str
        """
        self._version = version

    @property
    def resource_principal_token_public_key(self):
        """
        **[Required]** Gets the resource_principal_token_public_key of this CreateWorkerDetails.
        public key for resource Principal Token based validation to be used in further calls.


        :return: The resource_principal_token_public_key of this CreateWorkerDetails.
        :rtype: str
        """
        return self._resource_principal_token_public_key

    @resource_principal_token_public_key.setter
    def resource_principal_token_public_key(self, resource_principal_token_public_key):
        """
        Sets the resource_principal_token_public_key of this CreateWorkerDetails.
        public key for resource Principal Token based validation to be used in further calls.


        :param resource_principal_token_public_key: The resource_principal_token_public_key of this CreateWorkerDetails.
        :type: str
        """
        self._resource_principal_token_public_key = resource_principal_token_public_key

    @property
    def configuration_details(self):
        """
        Gets the configuration_details of this CreateWorkerDetails.
        Configuration details of the On-premise VP worker.


        :return: The configuration_details of this CreateWorkerDetails.
        :rtype: object
        """
        return self._configuration_details

    @configuration_details.setter
    def configuration_details(self, configuration_details):
        """
        Sets the configuration_details of this CreateWorkerDetails.
        Configuration details of the On-premise VP worker.


        :param configuration_details: The configuration_details of this CreateWorkerDetails.
        :type: object
        """
        self._configuration_details = configuration_details

    @property
    def worker_type(self):
        """
        Gets the worker_type of this CreateWorkerDetails.
        Type of the On-premise VP worker.

        Allowed values for this property are: "DOCKER"


        :return: The worker_type of this CreateWorkerDetails.
        :rtype: str
        """
        return self._worker_type

    @worker_type.setter
    def worker_type(self, worker_type):
        """
        Sets the worker_type of this CreateWorkerDetails.
        Type of the On-premise VP worker.


        :param worker_type: The worker_type of this CreateWorkerDetails.
        :type: str
        """
        allowed_values = ["DOCKER"]
        if not value_allowed_none_or_none_sentinel(worker_type, allowed_values):
            raise ValueError(
                f"Invalid value for `worker_type`, must be None or one of {allowed_values}"
            )
        self._worker_type = worker_type

    @property
    def status(self):
        """
        Gets the status of this CreateWorkerDetails.
        Enables or disables the On-premise VP worker.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The status of this CreateWorkerDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CreateWorkerDetails.
        Enables or disables the On-premise VP worker.


        :param status: The status of this CreateWorkerDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                f"Invalid value for `status`, must be None or one of {allowed_values}"
            )
        self._status = status

    @property
    def priority(self):
        """
        Gets the priority of this CreateWorkerDetails.
        Priority of the On-premise VP worker to schedule monitors.


        :return: The priority of this CreateWorkerDetails.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this CreateWorkerDetails.
        Priority of the On-premise VP worker to schedule monitors.


        :param priority: The priority of this CreateWorkerDetails.
        :type: int
        """
        self._priority = priority

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateWorkerDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateWorkerDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateWorkerDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateWorkerDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateWorkerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateWorkerDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateWorkerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateWorkerDetails.
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