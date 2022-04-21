# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .source_details import SourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoggingSourceDetails(SourceDetails):
    """
    The Logging source.
    For configuration instructions, see
    `To create a service connector`__.

    __ https://docs.cloud.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LoggingSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.LoggingSourceDetails.kind` attribute
        of this class is ``logging`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this LoggingSourceDetails.
            Allowed values for this property are: "logging", "monitoring", "streaming"
        :type kind: str

        :param log_sources:
            The value to assign to the log_sources property of this LoggingSourceDetails.
        :type log_sources: list[oci.sch.models.LogSource]

        """
        self.swagger_types = {
            'kind': 'str',
            'log_sources': 'list[LogSource]'
        }

        self.attribute_map = {
            'kind': 'kind',
            'log_sources': 'logSources'
        }

        self._kind = None
        self._log_sources = None
        self._kind = 'logging'

    @property
    def log_sources(self):
        """
        **[Required]** Gets the log_sources of this LoggingSourceDetails.
        The logs for this Logging source.


        :return: The log_sources of this LoggingSourceDetails.
        :rtype: list[oci.sch.models.LogSource]
        """
        return self._log_sources

    @log_sources.setter
    def log_sources(self, log_sources):
        """
        Sets the log_sources of this LoggingSourceDetails.
        The logs for this Logging source.


        :param log_sources: The log_sources of this LoggingSourceDetails.
        :type: list[oci.sch.models.LogSource]
        """
        self._log_sources = log_sources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
