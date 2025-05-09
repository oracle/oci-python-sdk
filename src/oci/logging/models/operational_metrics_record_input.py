# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperationalMetricsRecordInput(object):
    """
    Record section of OperationalMetricsSource object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OperationalMetricsRecordInput object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this OperationalMetricsRecordInput.
        :type namespace: str

        :param resource_group:
            The value to assign to the resource_group property of this OperationalMetricsRecordInput.
        :type resource_group: str

        """
        self.swagger_types = {
            'namespace': 'str',
            'resource_group': 'str'
        }
        self.attribute_map = {
            'namespace': 'namespace',
            'resource_group': 'resourceGroup'
        }
        self._namespace = None
        self._resource_group = None

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this OperationalMetricsRecordInput.
        Namespace to emit the operational metrics.


        :return: The namespace of this OperationalMetricsRecordInput.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this OperationalMetricsRecordInput.
        Namespace to emit the operational metrics.


        :param namespace: The namespace of this OperationalMetricsRecordInput.
        :type: str
        """
        self._namespace = namespace

    @property
    def resource_group(self):
        """
        Gets the resource_group of this OperationalMetricsRecordInput.
        Resource group to emit the operational metrics.


        :return: The resource_group of this OperationalMetricsRecordInput.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """
        Sets the resource_group of this OperationalMetricsRecordInput.
        Resource group to emit the operational metrics.


        :param resource_group: The resource_group of this OperationalMetricsRecordInput.
        :type: str
        """
        self._resource_group = resource_group

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
