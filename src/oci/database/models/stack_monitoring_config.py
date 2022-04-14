# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StackMonitoringConfig(object):
    """
    The configuration of Stack Monitoring for the external database.
    """

    #: A constant which can be used with the stack_monitoring_status property of a StackMonitoringConfig.
    #: This constant has a value of "ENABLING"
    STACK_MONITORING_STATUS_ENABLING = "ENABLING"

    #: A constant which can be used with the stack_monitoring_status property of a StackMonitoringConfig.
    #: This constant has a value of "ENABLED"
    STACK_MONITORING_STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the stack_monitoring_status property of a StackMonitoringConfig.
    #: This constant has a value of "DISABLING"
    STACK_MONITORING_STATUS_DISABLING = "DISABLING"

    #: A constant which can be used with the stack_monitoring_status property of a StackMonitoringConfig.
    #: This constant has a value of "NOT_ENABLED"
    STACK_MONITORING_STATUS_NOT_ENABLED = "NOT_ENABLED"

    #: A constant which can be used with the stack_monitoring_status property of a StackMonitoringConfig.
    #: This constant has a value of "FAILED_ENABLING"
    STACK_MONITORING_STATUS_FAILED_ENABLING = "FAILED_ENABLING"

    #: A constant which can be used with the stack_monitoring_status property of a StackMonitoringConfig.
    #: This constant has a value of "FAILED_DISABLING"
    STACK_MONITORING_STATUS_FAILED_DISABLING = "FAILED_DISABLING"

    def __init__(self, **kwargs):
        """
        Initializes a new StackMonitoringConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stack_monitoring_status:
            The value to assign to the stack_monitoring_status property of this StackMonitoringConfig.
            Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type stack_monitoring_status: str

        :param stack_monitoring_connector_id:
            The value to assign to the stack_monitoring_connector_id property of this StackMonitoringConfig.
        :type stack_monitoring_connector_id: str

        """
        self.swagger_types = {
            'stack_monitoring_status': 'str',
            'stack_monitoring_connector_id': 'str'
        }

        self.attribute_map = {
            'stack_monitoring_status': 'stackMonitoringStatus',
            'stack_monitoring_connector_id': 'stackMonitoringConnectorId'
        }

        self._stack_monitoring_status = None
        self._stack_monitoring_connector_id = None

    @property
    def stack_monitoring_status(self):
        """
        **[Required]** Gets the stack_monitoring_status of this StackMonitoringConfig.
        The status of Stack Monitoring.

        Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The stack_monitoring_status of this StackMonitoringConfig.
        :rtype: str
        """
        return self._stack_monitoring_status

    @stack_monitoring_status.setter
    def stack_monitoring_status(self, stack_monitoring_status):
        """
        Sets the stack_monitoring_status of this StackMonitoringConfig.
        The status of Stack Monitoring.


        :param stack_monitoring_status: The stack_monitoring_status of this StackMonitoringConfig.
        :type: str
        """
        allowed_values = ["ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING"]
        if not value_allowed_none_or_none_sentinel(stack_monitoring_status, allowed_values):
            stack_monitoring_status = 'UNKNOWN_ENUM_VALUE'
        self._stack_monitoring_status = stack_monitoring_status

    @property
    def stack_monitoring_connector_id(self):
        """
        Gets the stack_monitoring_connector_id of this StackMonitoringConfig.
        The `OCID`__ of the
        :func:`create_external_database_connector_details`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The stack_monitoring_connector_id of this StackMonitoringConfig.
        :rtype: str
        """
        return self._stack_monitoring_connector_id

    @stack_monitoring_connector_id.setter
    def stack_monitoring_connector_id(self, stack_monitoring_connector_id):
        """
        Sets the stack_monitoring_connector_id of this StackMonitoringConfig.
        The `OCID`__ of the
        :func:`create_external_database_connector_details`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param stack_monitoring_connector_id: The stack_monitoring_connector_id of this StackMonitoringConfig.
        :type: str
        """
        self._stack_monitoring_connector_id = stack_monitoring_connector_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
