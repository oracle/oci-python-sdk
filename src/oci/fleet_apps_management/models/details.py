# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Details(object):
    """
    The details of the task.
    """

    #: A constant which can be used with the os_type property of a Details.
    #: This constant has a value of "WINDOWS"
    OS_TYPE_WINDOWS = "WINDOWS"

    #: A constant which can be used with the os_type property of a Details.
    #: This constant has a value of "LINUX"
    OS_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the os_type property of a Details.
    #: This constant has a value of "GENERIC"
    OS_TYPE_GENERIC = "GENERIC"

    #: A constant which can be used with the scope property of a Details.
    #: This constant has a value of "LOCAL"
    SCOPE_LOCAL = "LOCAL"

    #: A constant which can be used with the scope property of a Details.
    #: This constant has a value of "SHARED"
    SCOPE_SHARED = "SHARED"

    def __init__(self, **kwargs):
        """
        Initializes a new Details object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param execution_details:
            The value to assign to the execution_details property of this Details.
        :type execution_details: oci.fleet_apps_management.models.ExecutionDetails

        :param platform:
            The value to assign to the platform property of this Details.
        :type platform: str

        :param os_type:
            The value to assign to the os_type property of this Details.
            Allowed values for this property are: "WINDOWS", "LINUX", "GENERIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_type: str

        :param scope:
            The value to assign to the scope property of this Details.
            Allowed values for this property are: "LOCAL", "SHARED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scope: str

        :param properties:
            The value to assign to the properties property of this Details.
        :type properties: oci.fleet_apps_management.models.Properties

        :param is_discovery_output_task:
            The value to assign to the is_discovery_output_task property of this Details.
        :type is_discovery_output_task: bool

        :param is_apply_subject_task:
            The value to assign to the is_apply_subject_task property of this Details.
        :type is_apply_subject_task: bool

        :param operation:
            The value to assign to the operation property of this Details.
        :type operation: str

        """
        self.swagger_types = {
            'execution_details': 'ExecutionDetails',
            'platform': 'str',
            'os_type': 'str',
            'scope': 'str',
            'properties': 'Properties',
            'is_discovery_output_task': 'bool',
            'is_apply_subject_task': 'bool',
            'operation': 'str'
        }
        self.attribute_map = {
            'execution_details': 'executionDetails',
            'platform': 'platform',
            'os_type': 'osType',
            'scope': 'scope',
            'properties': 'properties',
            'is_discovery_output_task': 'isDiscoveryOutputTask',
            'is_apply_subject_task': 'isApplySubjectTask',
            'operation': 'operation'
        }
        self._execution_details = None
        self._platform = None
        self._os_type = None
        self._scope = None
        self._properties = None
        self._is_discovery_output_task = None
        self._is_apply_subject_task = None
        self._operation = None

    @property
    def execution_details(self):
        """
        **[Required]** Gets the execution_details of this Details.

        :return: The execution_details of this Details.
        :rtype: oci.fleet_apps_management.models.ExecutionDetails
        """
        return self._execution_details

    @execution_details.setter
    def execution_details(self, execution_details):
        """
        Sets the execution_details of this Details.

        :param execution_details: The execution_details of this Details.
        :type: oci.fleet_apps_management.models.ExecutionDetails
        """
        self._execution_details = execution_details

    @property
    def platform(self):
        """
        Gets the platform of this Details.
        The platform of the runbook.


        :return: The platform of this Details.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this Details.
        The platform of the runbook.


        :param platform: The platform of this Details.
        :type: str
        """
        self._platform = platform

    @property
    def os_type(self):
        """
        Gets the os_type of this Details.
        The OS for the task

        Allowed values for this property are: "WINDOWS", "LINUX", "GENERIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_type of this Details.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """
        Sets the os_type of this Details.
        The OS for the task


        :param os_type: The os_type of this Details.
        :type: str
        """
        allowed_values = ["WINDOWS", "LINUX", "GENERIC"]
        if not value_allowed_none_or_none_sentinel(os_type, allowed_values):
            os_type = 'UNKNOWN_ENUM_VALUE'
        self._os_type = os_type

    @property
    def scope(self):
        """
        **[Required]** Gets the scope of this Details.
        The scope of the task

        Allowed values for this property are: "LOCAL", "SHARED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The scope of this Details.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this Details.
        The scope of the task


        :param scope: The scope of this Details.
        :type: str
        """
        allowed_values = ["LOCAL", "SHARED"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            scope = 'UNKNOWN_ENUM_VALUE'
        self._scope = scope

    @property
    def properties(self):
        """
        Gets the properties of this Details.

        :return: The properties of this Details.
        :rtype: oci.fleet_apps_management.models.Properties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this Details.

        :param properties: The properties of this Details.
        :type: oci.fleet_apps_management.models.Properties
        """
        self._properties = properties

    @property
    def is_discovery_output_task(self):
        """
        Gets the is_discovery_output_task of this Details.
        Is this a discovery output task?


        :return: The is_discovery_output_task of this Details.
        :rtype: bool
        """
        return self._is_discovery_output_task

    @is_discovery_output_task.setter
    def is_discovery_output_task(self, is_discovery_output_task):
        """
        Sets the is_discovery_output_task of this Details.
        Is this a discovery output task?


        :param is_discovery_output_task: The is_discovery_output_task of this Details.
        :type: bool
        """
        self._is_discovery_output_task = is_discovery_output_task

    @property
    def is_apply_subject_task(self):
        """
        Gets the is_apply_subject_task of this Details.
        Is this an Apply Subject Task?
        Set this to true for a Patch Execution Task which applies patches(subjects) on a target.


        :return: The is_apply_subject_task of this Details.
        :rtype: bool
        """
        return self._is_apply_subject_task

    @is_apply_subject_task.setter
    def is_apply_subject_task(self, is_apply_subject_task):
        """
        Sets the is_apply_subject_task of this Details.
        Is this an Apply Subject Task?
        Set this to true for a Patch Execution Task which applies patches(subjects) on a target.


        :param is_apply_subject_task: The is_apply_subject_task of this Details.
        :type: bool
        """
        self._is_apply_subject_task = is_apply_subject_task

    @property
    def operation(self):
        """
        Gets the operation of this Details.
        The lifecycle operation performed by the runbook.


        :return: The operation of this Details.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this Details.
        The lifecycle operation performed by the runbook.


        :param operation: The operation of this Details.
        :type: str
        """
        self._operation = operation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
