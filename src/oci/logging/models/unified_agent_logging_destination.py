# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentLoggingDestination(object):
    """
    Logging destination object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentLoggingDestination object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param log_object_id:
            The value to assign to the log_object_id property of this UnifiedAgentLoggingDestination.
        :type log_object_id: str

        :param operational_metrics_configuration:
            The value to assign to the operational_metrics_configuration property of this UnifiedAgentLoggingDestination.
        :type operational_metrics_configuration: oci.logging.models.OperationalMetricsConfiguration

        """
        self.swagger_types = {
            'log_object_id': 'str',
            'operational_metrics_configuration': 'OperationalMetricsConfiguration'
        }
        self.attribute_map = {
            'log_object_id': 'logObjectId',
            'operational_metrics_configuration': 'operationalMetricsConfiguration'
        }
        self._log_object_id = None
        self._operational_metrics_configuration = None

    @property
    def log_object_id(self):
        """
        **[Required]** Gets the log_object_id of this UnifiedAgentLoggingDestination.
        The OCID of the resource.


        :return: The log_object_id of this UnifiedAgentLoggingDestination.
        :rtype: str
        """
        return self._log_object_id

    @log_object_id.setter
    def log_object_id(self, log_object_id):
        """
        Sets the log_object_id of this UnifiedAgentLoggingDestination.
        The OCID of the resource.


        :param log_object_id: The log_object_id of this UnifiedAgentLoggingDestination.
        :type: str
        """
        self._log_object_id = log_object_id

    @property
    def operational_metrics_configuration(self):
        """
        Gets the operational_metrics_configuration of this UnifiedAgentLoggingDestination.

        :return: The operational_metrics_configuration of this UnifiedAgentLoggingDestination.
        :rtype: oci.logging.models.OperationalMetricsConfiguration
        """
        return self._operational_metrics_configuration

    @operational_metrics_configuration.setter
    def operational_metrics_configuration(self, operational_metrics_configuration):
        """
        Sets the operational_metrics_configuration of this UnifiedAgentLoggingDestination.

        :param operational_metrics_configuration: The operational_metrics_configuration of this UnifiedAgentLoggingDestination.
        :type: oci.logging.models.OperationalMetricsConfiguration
        """
        self._operational_metrics_configuration = operational_metrics_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
