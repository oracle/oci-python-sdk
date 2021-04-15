# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperationsInsightsConfig(object):
    """
    The configuration of Operations Insights for the external database
    """

    #: A constant which can be used with the operations_insights_status property of a OperationsInsightsConfig.
    #: This constant has a value of "ENABLING"
    OPERATIONS_INSIGHTS_STATUS_ENABLING = "ENABLING"

    #: A constant which can be used with the operations_insights_status property of a OperationsInsightsConfig.
    #: This constant has a value of "ENABLED"
    OPERATIONS_INSIGHTS_STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the operations_insights_status property of a OperationsInsightsConfig.
    #: This constant has a value of "DISABLING"
    OPERATIONS_INSIGHTS_STATUS_DISABLING = "DISABLING"

    #: A constant which can be used with the operations_insights_status property of a OperationsInsightsConfig.
    #: This constant has a value of "NOT_ENABLED"
    OPERATIONS_INSIGHTS_STATUS_NOT_ENABLED = "NOT_ENABLED"

    #: A constant which can be used with the operations_insights_status property of a OperationsInsightsConfig.
    #: This constant has a value of "FAILED_ENABLING"
    OPERATIONS_INSIGHTS_STATUS_FAILED_ENABLING = "FAILED_ENABLING"

    #: A constant which can be used with the operations_insights_status property of a OperationsInsightsConfig.
    #: This constant has a value of "FAILED_DISABLING"
    OPERATIONS_INSIGHTS_STATUS_FAILED_DISABLING = "FAILED_DISABLING"

    def __init__(self, **kwargs):
        """
        Initializes a new OperationsInsightsConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operations_insights_status:
            The value to assign to the operations_insights_status property of this OperationsInsightsConfig.
            Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operations_insights_status: str

        :param operations_insights_connector_id:
            The value to assign to the operations_insights_connector_id property of this OperationsInsightsConfig.
        :type operations_insights_connector_id: str

        """
        self.swagger_types = {
            'operations_insights_status': 'str',
            'operations_insights_connector_id': 'str'
        }

        self.attribute_map = {
            'operations_insights_status': 'operationsInsightsStatus',
            'operations_insights_connector_id': 'operationsInsightsConnectorId'
        }

        self._operations_insights_status = None
        self._operations_insights_connector_id = None

    @property
    def operations_insights_status(self):
        """
        **[Required]** Gets the operations_insights_status of this OperationsInsightsConfig.
        The status of Operations Insights

        Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operations_insights_status of this OperationsInsightsConfig.
        :rtype: str
        """
        return self._operations_insights_status

    @operations_insights_status.setter
    def operations_insights_status(self, operations_insights_status):
        """
        Sets the operations_insights_status of this OperationsInsightsConfig.
        The status of Operations Insights


        :param operations_insights_status: The operations_insights_status of this OperationsInsightsConfig.
        :type: str
        """
        allowed_values = ["ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING"]
        if not value_allowed_none_or_none_sentinel(operations_insights_status, allowed_values):
            operations_insights_status = 'UNKNOWN_ENUM_VALUE'
        self._operations_insights_status = operations_insights_status

    @property
    def operations_insights_connector_id(self):
        """
        Gets the operations_insights_connector_id of this OperationsInsightsConfig.
        The `OCID`__ of the
        :func:`create_external_database_connector_details`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The operations_insights_connector_id of this OperationsInsightsConfig.
        :rtype: str
        """
        return self._operations_insights_connector_id

    @operations_insights_connector_id.setter
    def operations_insights_connector_id(self, operations_insights_connector_id):
        """
        Sets the operations_insights_connector_id of this OperationsInsightsConfig.
        The `OCID`__ of the
        :func:`create_external_database_connector_details`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param operations_insights_connector_id: The operations_insights_connector_id of this OperationsInsightsConfig.
        :type: str
        """
        self._operations_insights_connector_id = operations_insights_connector_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
