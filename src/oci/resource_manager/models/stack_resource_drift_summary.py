# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StackResourceDriftSummary(object):
    """
    Drift status details for the indicated resource and stack. Includes actual and expected (defined) properties.
    """

    #: A constant which can be used with the resource_drift_status property of a StackResourceDriftSummary.
    #: This constant has a value of "NOT_CHECKED"
    RESOURCE_DRIFT_STATUS_NOT_CHECKED = "NOT_CHECKED"

    #: A constant which can be used with the resource_drift_status property of a StackResourceDriftSummary.
    #: This constant has a value of "IN_SYNC"
    RESOURCE_DRIFT_STATUS_IN_SYNC = "IN_SYNC"

    #: A constant which can be used with the resource_drift_status property of a StackResourceDriftSummary.
    #: This constant has a value of "MODIFIED"
    RESOURCE_DRIFT_STATUS_MODIFIED = "MODIFIED"

    #: A constant which can be used with the resource_drift_status property of a StackResourceDriftSummary.
    #: This constant has a value of "DELETED"
    RESOURCE_DRIFT_STATUS_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new StackResourceDriftSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stack_id:
            The value to assign to the stack_id property of this StackResourceDriftSummary.
        :type stack_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this StackResourceDriftSummary.
        :type compartment_id: str

        :param resource_name:
            The value to assign to the resource_name property of this StackResourceDriftSummary.
        :type resource_name: str

        :param resource_id:
            The value to assign to the resource_id property of this StackResourceDriftSummary.
        :type resource_id: str

        :param resource_type:
            The value to assign to the resource_type property of this StackResourceDriftSummary.
        :type resource_type: str

        :param resource_drift_status:
            The value to assign to the resource_drift_status property of this StackResourceDriftSummary.
            Allowed values for this property are: "NOT_CHECKED", "IN_SYNC", "MODIFIED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_drift_status: str

        :param actual_properties:
            The value to assign to the actual_properties property of this StackResourceDriftSummary.
        :type actual_properties: dict(str, str)

        :param expected_properties:
            The value to assign to the expected_properties property of this StackResourceDriftSummary.
        :type expected_properties: dict(str, str)

        :param time_drift_checked:
            The value to assign to the time_drift_checked property of this StackResourceDriftSummary.
        :type time_drift_checked: datetime

        """
        self.swagger_types = {
            'stack_id': 'str',
            'compartment_id': 'str',
            'resource_name': 'str',
            'resource_id': 'str',
            'resource_type': 'str',
            'resource_drift_status': 'str',
            'actual_properties': 'dict(str, str)',
            'expected_properties': 'dict(str, str)',
            'time_drift_checked': 'datetime'
        }

        self.attribute_map = {
            'stack_id': 'stackId',
            'compartment_id': 'compartmentId',
            'resource_name': 'resourceName',
            'resource_id': 'resourceId',
            'resource_type': 'resourceType',
            'resource_drift_status': 'resourceDriftStatus',
            'actual_properties': 'actualProperties',
            'expected_properties': 'expectedProperties',
            'time_drift_checked': 'timeDriftChecked'
        }

        self._stack_id = None
        self._compartment_id = None
        self._resource_name = None
        self._resource_id = None
        self._resource_type = None
        self._resource_drift_status = None
        self._actual_properties = None
        self._expected_properties = None
        self._time_drift_checked = None

    @property
    def stack_id(self):
        """
        Gets the stack_id of this StackResourceDriftSummary.
        The `OCID`__ of the stack.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The stack_id of this StackResourceDriftSummary.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """
        Sets the stack_id of this StackResourceDriftSummary.
        The `OCID`__ of the stack.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param stack_id: The stack_id of this StackResourceDriftSummary.
        :type: str
        """
        self._stack_id = stack_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this StackResourceDriftSummary.
        The `OCID`__ of the compartment where the stack is located.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this StackResourceDriftSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this StackResourceDriftSummary.
        The `OCID`__ of the compartment where the stack is located.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this StackResourceDriftSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resource_name(self):
        """
        Gets the resource_name of this StackResourceDriftSummary.
        The name of the resource as defined in the stack.


        :return: The resource_name of this StackResourceDriftSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this StackResourceDriftSummary.
        The name of the resource as defined in the stack.


        :param resource_name: The resource_name of this StackResourceDriftSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_id(self):
        """
        Gets the resource_id of this StackResourceDriftSummary.
        The `OCID`__ of the resource provisioned by Terraform.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The resource_id of this StackResourceDriftSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this StackResourceDriftSummary.
        The `OCID`__ of the resource provisioned by Terraform.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param resource_id: The resource_id of this StackResourceDriftSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """
        Gets the resource_type of this StackResourceDriftSummary.
        The provider resource type.
        Must be supported by the `Oracle Cloud Infrastructure provider`__.
        Example: `oci_core_instance`

        __ https://www.terraform.io/docs/providers/oci/index.html


        :return: The resource_type of this StackResourceDriftSummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this StackResourceDriftSummary.
        The provider resource type.
        Must be supported by the `Oracle Cloud Infrastructure provider`__.
        Example: `oci_core_instance`

        __ https://www.terraform.io/docs/providers/oci/index.html


        :param resource_type: The resource_type of this StackResourceDriftSummary.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_drift_status(self):
        """
        Gets the resource_drift_status of this StackResourceDriftSummary.
        The drift status of the resource.
        A drift status value indicates whether or not the actual state of the resource differs from the expected (defined) state for that resource.

        Allowed values for this property are: "NOT_CHECKED", "IN_SYNC", "MODIFIED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_drift_status of this StackResourceDriftSummary.
        :rtype: str
        """
        return self._resource_drift_status

    @resource_drift_status.setter
    def resource_drift_status(self, resource_drift_status):
        """
        Sets the resource_drift_status of this StackResourceDriftSummary.
        The drift status of the resource.
        A drift status value indicates whether or not the actual state of the resource differs from the expected (defined) state for that resource.


        :param resource_drift_status: The resource_drift_status of this StackResourceDriftSummary.
        :type: str
        """
        allowed_values = ["NOT_CHECKED", "IN_SYNC", "MODIFIED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(resource_drift_status, allowed_values):
            resource_drift_status = 'UNKNOWN_ENUM_VALUE'
        self._resource_drift_status = resource_drift_status

    @property
    def actual_properties(self):
        """
        Gets the actual_properties of this StackResourceDriftSummary.
        Actual values of properties that the stack defines for the indicated resource.
        Each property and value is provided as a key-value pair.
        The following example shows actual values for the resource's display name and server type:
        `{\"display_name\": \"tf-default-dhcp-options-new\", \"options.0.server_type\": \"VcnLocalPlusInternet\"}`


        :return: The actual_properties of this StackResourceDriftSummary.
        :rtype: dict(str, str)
        """
        return self._actual_properties

    @actual_properties.setter
    def actual_properties(self, actual_properties):
        """
        Sets the actual_properties of this StackResourceDriftSummary.
        Actual values of properties that the stack defines for the indicated resource.
        Each property and value is provided as a key-value pair.
        The following example shows actual values for the resource's display name and server type:
        `{\"display_name\": \"tf-default-dhcp-options-new\", \"options.0.server_type\": \"VcnLocalPlusInternet\"}`


        :param actual_properties: The actual_properties of this StackResourceDriftSummary.
        :type: dict(str, str)
        """
        self._actual_properties = actual_properties

    @property
    def expected_properties(self):
        """
        Gets the expected_properties of this StackResourceDriftSummary.
        Expected values of properties that the stack defines for the indicated resource.
        Each property and value is provided as a key-value pair.
        The following example shows expected (defined) values for the resource's display name and server type:
        `{\"display_name\": \"tf-default-dhcp-options\", \"options.0.server_type\": \"VcnLocalPlusInternet\"}`


        :return: The expected_properties of this StackResourceDriftSummary.
        :rtype: dict(str, str)
        """
        return self._expected_properties

    @expected_properties.setter
    def expected_properties(self, expected_properties):
        """
        Sets the expected_properties of this StackResourceDriftSummary.
        Expected values of properties that the stack defines for the indicated resource.
        Each property and value is provided as a key-value pair.
        The following example shows expected (defined) values for the resource's display name and server type:
        `{\"display_name\": \"tf-default-dhcp-options\", \"options.0.server_type\": \"VcnLocalPlusInternet\"}`


        :param expected_properties: The expected_properties of this StackResourceDriftSummary.
        :type: dict(str, str)
        """
        self._expected_properties = expected_properties

    @property
    def time_drift_checked(self):
        """
        Gets the time_drift_checked of this StackResourceDriftSummary.
        The date and time when the drift detection was executed.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :return: The time_drift_checked of this StackResourceDriftSummary.
        :rtype: datetime
        """
        return self._time_drift_checked

    @time_drift_checked.setter
    def time_drift_checked(self, time_drift_checked):
        """
        Sets the time_drift_checked of this StackResourceDriftSummary.
        The date and time when the drift detection was executed.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :param time_drift_checked: The time_drift_checked of this StackResourceDriftSummary.
        :type: datetime
        """
        self._time_drift_checked = time_drift_checked

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
