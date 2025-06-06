# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601

from .log_analytics_endpoint import LogAnalyticsEndpoint
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogTypeEndpoint(LogAnalyticsEndpoint):
    """
    The LOG type endpoint configuration. Logs are fetched from the specified endpoint.
    For time based incremental collection, specify the START_TIME macro with the desired time format,
    example: {START_TIME:yyMMddHHmmssZ}.
    For offset based incremental collection, specify the START_OFFSET macro with offset identifier in the API response,
    example: {START_OFFSET:$.offset}
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogTypeEndpoint object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.LogTypeEndpoint.endpoint_type` attribute
        of this class is ``LOG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param endpoint_type:
            The value to assign to the endpoint_type property of this LogTypeEndpoint.
            Allowed values for this property are: "LOG_LIST", "LOG"
        :type endpoint_type: str

        :param log_endpoint:
            The value to assign to the log_endpoint property of this LogTypeEndpoint.
        :type log_endpoint: oci.log_analytics.models.LogEndpoint

        """
        self.swagger_types = {
            'endpoint_type': 'str',
            'log_endpoint': 'LogEndpoint'
        }
        self.attribute_map = {
            'endpoint_type': 'endpointType',
            'log_endpoint': 'logEndpoint'
        }
        self._endpoint_type = None
        self._log_endpoint = None
        self._endpoint_type = 'LOG'

    @property
    def log_endpoint(self):
        """
        **[Required]** Gets the log_endpoint of this LogTypeEndpoint.

        :return: The log_endpoint of this LogTypeEndpoint.
        :rtype: oci.log_analytics.models.LogEndpoint
        """
        return self._log_endpoint

    @log_endpoint.setter
    def log_endpoint(self, log_endpoint):
        """
        Sets the log_endpoint of this LogTypeEndpoint.

        :param log_endpoint: The log_endpoint of this LogTypeEndpoint.
        :type: oci.log_analytics.models.LogEndpoint
        """
        self._log_endpoint = log_endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
