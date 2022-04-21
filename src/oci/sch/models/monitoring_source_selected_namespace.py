# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoringSourceSelectedNamespace(object):
    """
    A metric namespace for the compartment-specific list.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoringSourceSelectedNamespace object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this MonitoringSourceSelectedNamespace.
        :type namespace: str

        :param metrics:
            The value to assign to the metrics property of this MonitoringSourceSelectedNamespace.
        :type metrics: oci.sch.models.MonitoringSourceMetricDetails

        """
        self.swagger_types = {
            'namespace': 'str',
            'metrics': 'MonitoringSourceMetricDetails'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'metrics': 'metrics'
        }

        self._namespace = None
        self._metrics = None

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this MonitoringSourceSelectedNamespace.
        The source service or application to use when querying for metric data points. Must begin with `oci_`.

        Example: `oci_computeagent`


        :return: The namespace of this MonitoringSourceSelectedNamespace.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this MonitoringSourceSelectedNamespace.
        The source service or application to use when querying for metric data points. Must begin with `oci_`.

        Example: `oci_computeagent`


        :param namespace: The namespace of this MonitoringSourceSelectedNamespace.
        :type: str
        """
        self._namespace = namespace

    @property
    def metrics(self):
        """
        **[Required]** Gets the metrics of this MonitoringSourceSelectedNamespace.

        :return: The metrics of this MonitoringSourceSelectedNamespace.
        :rtype: oci.sch.models.MonitoringSourceMetricDetails
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this MonitoringSourceSelectedNamespace.

        :param metrics: The metrics of this MonitoringSourceSelectedNamespace.
        :type: oci.sch.models.MonitoringSourceMetricDetails
        """
        self._metrics = metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
