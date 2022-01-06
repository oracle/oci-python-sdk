# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceEnvironment(object):
    """
    Detailed information about a service environment.

    **Note:** Service URL formats may vary from the provided example.
    """

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "INITIALIZED"
    STATUS_INITIALIZED = "INITIALIZED"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_ACTIVATION"
    STATUS_BEGIN_ACTIVATION = "BEGIN_ACTIVATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "ACTIVE"
    STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_SOFT_TERMINATION"
    STATUS_BEGIN_SOFT_TERMINATION = "BEGIN_SOFT_TERMINATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "SOFT_TERMINATED"
    STATUS_SOFT_TERMINATED = "SOFT_TERMINATED"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_TERMINATION"
    STATUS_BEGIN_TERMINATION = "BEGIN_TERMINATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "TERMINATED"
    STATUS_TERMINATED = "TERMINATED"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_DISABLING"
    STATUS_BEGIN_DISABLING = "BEGIN_DISABLING"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_ENABLING"
    STATUS_BEGIN_ENABLING = "BEGIN_ENABLING"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_MIGRATION"
    STATUS_BEGIN_MIGRATION = "BEGIN_MIGRATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_SUSPENSION"
    STATUS_BEGIN_SUSPENSION = "BEGIN_SUSPENSION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_RESUMPTION"
    STATUS_BEGIN_RESUMPTION = "BEGIN_RESUMPTION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "SUSPENDED"
    STATUS_SUSPENDED = "SUSPENDED"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_LOCK_RELOCATION"
    STATUS_BEGIN_LOCK_RELOCATION = "BEGIN_LOCK_RELOCATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "LOCKED_RELOCATION"
    STATUS_LOCKED_RELOCATION = "LOCKED_RELOCATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_RELOCATION"
    STATUS_BEGIN_RELOCATION = "BEGIN_RELOCATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "RELOCATED"
    STATUS_RELOCATED = "RELOCATED"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_UNLOCK_RELOCATION"
    STATUS_BEGIN_UNLOCK_RELOCATION = "BEGIN_UNLOCK_RELOCATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "UNLOCKED_RELOCATION"
    STATUS_UNLOCKED_RELOCATION = "UNLOCKED_RELOCATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "FAILED_LOCK_RELOCATION"
    STATUS_FAILED_LOCK_RELOCATION = "FAILED_LOCK_RELOCATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "FAILED_ACTIVATION"
    STATUS_FAILED_ACTIVATION = "FAILED_ACTIVATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "FAILED_MIGRATION"
    STATUS_FAILED_MIGRATION = "FAILED_MIGRATION"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "ACCESS_DISABLED"
    STATUS_ACCESS_DISABLED = "ACCESS_DISABLED"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_DISABLING_ACCESS"
    STATUS_BEGIN_DISABLING_ACCESS = "BEGIN_DISABLING_ACCESS"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "BEGIN_ENABLING_ACCESS"
    STATUS_BEGIN_ENABLING_ACCESS = "BEGIN_ENABLING_ACCESS"

    #: A constant which can be used with the status property of a ServiceEnvironment.
    #: This constant has a value of "TRA_UNKNOWN"
    STATUS_TRA_UNKNOWN = "TRA_UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceEnvironment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ServiceEnvironment.
        :type id: str

        :param subscription_id:
            The value to assign to the subscription_id property of this ServiceEnvironment.
        :type subscription_id: str

        :param status:
            The value to assign to the status property of this ServiceEnvironment.
            Allowed values for this property are: "INITIALIZED", "BEGIN_ACTIVATION", "ACTIVE", "BEGIN_SOFT_TERMINATION", "SOFT_TERMINATED", "BEGIN_TERMINATION", "CANCELED", "TERMINATED", "BEGIN_DISABLING", "BEGIN_ENABLING", "BEGIN_MIGRATION", "DISABLED", "BEGIN_SUSPENSION", "BEGIN_RESUMPTION", "SUSPENDED", "BEGIN_LOCK_RELOCATION", "LOCKED_RELOCATION", "BEGIN_RELOCATION", "RELOCATED", "BEGIN_UNLOCK_RELOCATION", "UNLOCKED_RELOCATION", "FAILED_LOCK_RELOCATION", "FAILED_ACTIVATION", "FAILED_MIGRATION", "ACCESS_DISABLED", "BEGIN_DISABLING_ACCESS", "BEGIN_ENABLING_ACCESS", "TRA_UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ServiceEnvironment.
        :type compartment_id: str

        :param service_definition:
            The value to assign to the service_definition property of this ServiceEnvironment.
        :type service_definition: oci.service_manager_proxy.models.ServiceDefinition

        :param console_url:
            The value to assign to the console_url property of this ServiceEnvironment.
        :type console_url: str

        :param service_environment_endpoints:
            The value to assign to the service_environment_endpoints property of this ServiceEnvironment.
        :type service_environment_endpoints: list[oci.service_manager_proxy.models.ServiceEnvironmentEndPointOverview]

        """
        self.swagger_types = {
            'id': 'str',
            'subscription_id': 'str',
            'status': 'str',
            'compartment_id': 'str',
            'service_definition': 'ServiceDefinition',
            'console_url': 'str',
            'service_environment_endpoints': 'list[ServiceEnvironmentEndPointOverview]'
        }

        self.attribute_map = {
            'id': 'id',
            'subscription_id': 'subscriptionId',
            'status': 'status',
            'compartment_id': 'compartmentId',
            'service_definition': 'serviceDefinition',
            'console_url': 'consoleUrl',
            'service_environment_endpoints': 'serviceEnvironmentEndpoints'
        }

        self._id = None
        self._subscription_id = None
        self._status = None
        self._compartment_id = None
        self._service_definition = None
        self._console_url = None
        self._service_environment_endpoints = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ServiceEnvironment.
        Unqiue identifier for the entitlement related to the environment.

        **Note:** Not an `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ServiceEnvironment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ServiceEnvironment.
        Unqiue identifier for the entitlement related to the environment.

        **Note:** Not an `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ServiceEnvironment.
        :type: str
        """
        self._id = id

    @property
    def subscription_id(self):
        """
        **[Required]** Gets the subscription_id of this ServiceEnvironment.
        The unique subscription ID associated with the service environment ID.

        **Note:** Not an `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subscription_id of this ServiceEnvironment.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this ServiceEnvironment.
        The unique subscription ID associated with the service environment ID.

        **Note:** Not an `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subscription_id: The subscription_id of this ServiceEnvironment.
        :type: str
        """
        self._subscription_id = subscription_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ServiceEnvironment.
        Status of the entitlement registration for the service.

        Allowed values for this property are: "INITIALIZED", "BEGIN_ACTIVATION", "ACTIVE", "BEGIN_SOFT_TERMINATION", "SOFT_TERMINATED", "BEGIN_TERMINATION", "CANCELED", "TERMINATED", "BEGIN_DISABLING", "BEGIN_ENABLING", "BEGIN_MIGRATION", "DISABLED", "BEGIN_SUSPENSION", "BEGIN_RESUMPTION", "SUSPENDED", "BEGIN_LOCK_RELOCATION", "LOCKED_RELOCATION", "BEGIN_RELOCATION", "RELOCATED", "BEGIN_UNLOCK_RELOCATION", "UNLOCKED_RELOCATION", "FAILED_LOCK_RELOCATION", "FAILED_ACTIVATION", "FAILED_MIGRATION", "ACCESS_DISABLED", "BEGIN_DISABLING_ACCESS", "BEGIN_ENABLING_ACCESS", "TRA_UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ServiceEnvironment.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ServiceEnvironment.
        Status of the entitlement registration for the service.


        :param status: The status of this ServiceEnvironment.
        :type: str
        """
        allowed_values = ["INITIALIZED", "BEGIN_ACTIVATION", "ACTIVE", "BEGIN_SOFT_TERMINATION", "SOFT_TERMINATED", "BEGIN_TERMINATION", "CANCELED", "TERMINATED", "BEGIN_DISABLING", "BEGIN_ENABLING", "BEGIN_MIGRATION", "DISABLED", "BEGIN_SUSPENSION", "BEGIN_RESUMPTION", "SUSPENDED", "BEGIN_LOCK_RELOCATION", "LOCKED_RELOCATION", "BEGIN_RELOCATION", "RELOCATED", "BEGIN_UNLOCK_RELOCATION", "UNLOCKED_RELOCATION", "FAILED_LOCK_RELOCATION", "FAILED_ACTIVATION", "FAILED_MIGRATION", "ACCESS_DISABLED", "BEGIN_DISABLING_ACCESS", "BEGIN_ENABLING_ACCESS", "TRA_UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ServiceEnvironment.
        The `OCID`__ for the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ServiceEnvironment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ServiceEnvironment.
        The `OCID`__ for the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ServiceEnvironment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def service_definition(self):
        """
        **[Required]** Gets the service_definition of this ServiceEnvironment.

        :return: The service_definition of this ServiceEnvironment.
        :rtype: oci.service_manager_proxy.models.ServiceDefinition
        """
        return self._service_definition

    @service_definition.setter
    def service_definition(self, service_definition):
        """
        Sets the service_definition of this ServiceEnvironment.

        :param service_definition: The service_definition of this ServiceEnvironment.
        :type: oci.service_manager_proxy.models.ServiceDefinition
        """
        self._service_definition = service_definition

    @property
    def console_url(self):
        """
        Gets the console_url of this ServiceEnvironment.
        The URL for the console.


        :return: The console_url of this ServiceEnvironment.
        :rtype: str
        """
        return self._console_url

    @console_url.setter
    def console_url(self, console_url):
        """
        Sets the console_url of this ServiceEnvironment.
        The URL for the console.


        :param console_url: The console_url of this ServiceEnvironment.
        :type: str
        """
        self._console_url = console_url

    @property
    def service_environment_endpoints(self):
        """
        Gets the service_environment_endpoints of this ServiceEnvironment.
        Array of service environment end points.


        :return: The service_environment_endpoints of this ServiceEnvironment.
        :rtype: list[oci.service_manager_proxy.models.ServiceEnvironmentEndPointOverview]
        """
        return self._service_environment_endpoints

    @service_environment_endpoints.setter
    def service_environment_endpoints(self, service_environment_endpoints):
        """
        Sets the service_environment_endpoints of this ServiceEnvironment.
        Array of service environment end points.


        :param service_environment_endpoints: The service_environment_endpoints of this ServiceEnvironment.
        :type: list[oci.service_manager_proxy.models.ServiceEnvironmentEndPointOverview]
        """
        self._service_environment_endpoints = service_environment_endpoints

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
