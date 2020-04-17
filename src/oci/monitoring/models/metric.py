# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Metric(object):
    """
    The properties that define a metric.
    For information about metrics, see `Metrics Overview`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MetricsOverview
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Metric object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Metric.
        :type name: str

        :param namespace:
            The value to assign to the namespace property of this Metric.
        :type namespace: str

        :param resource_group:
            The value to assign to the resource_group property of this Metric.
        :type resource_group: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Metric.
        :type compartment_id: str

        :param dimensions:
            The value to assign to the dimensions property of this Metric.
        :type dimensions: dict(str, str)

        """
        self.swagger_types = {
            'name': 'str',
            'namespace': 'str',
            'resource_group': 'str',
            'compartment_id': 'str',
            'dimensions': 'dict(str, str)'
        }

        self.attribute_map = {
            'name': 'name',
            'namespace': 'namespace',
            'resource_group': 'resourceGroup',
            'compartment_id': 'compartmentId',
            'dimensions': 'dimensions'
        }

        self._name = None
        self._namespace = None
        self._resource_group = None
        self._compartment_id = None
        self._dimensions = None

    @property
    def name(self):
        """
        Gets the name of this Metric.
        The name of the metric.

        Example: `CpuUtilization`


        :return: The name of this Metric.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Metric.
        The name of the metric.

        Example: `CpuUtilization`


        :param name: The name of this Metric.
        :type: str
        """
        self._name = name

    @property
    def namespace(self):
        """
        Gets the namespace of this Metric.
        The source service or application emitting the metric.

        Example: `oci_computeagent`


        :return: The namespace of this Metric.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this Metric.
        The source service or application emitting the metric.

        Example: `oci_computeagent`


        :param namespace: The namespace of this Metric.
        :type: str
        """
        self._namespace = namespace

    @property
    def resource_group(self):
        """
        Gets the resource_group of this Metric.
        Resource group provided with the posted metric. A resource group is a custom string that can be used as a filter. Only one resource group can be applied per metric.
        A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
        Avoid entering confidential information.

        Example: `frontend-fleet`


        :return: The resource_group of this Metric.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """
        Sets the resource_group of this Metric.
        Resource group provided with the posted metric. A resource group is a custom string that can be used as a filter. Only one resource group can be applied per metric.
        A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
        Avoid entering confidential information.

        Example: `frontend-fleet`


        :param resource_group: The resource_group of this Metric.
        :type: str
        """
        self._resource_group = resource_group

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Metric.
        The `OCID`__ of the compartment containing
        the resources monitored by the metric.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Metric.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Metric.
        The `OCID`__ of the compartment containing
        the resources monitored by the metric.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Metric.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def dimensions(self):
        """
        Gets the dimensions of this Metric.
        Qualifiers provided in a metric definition. Available dimensions vary by metric namespace.
        Each dimension takes the form of a key-value pair.

        Example: `\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"`


        :return: The dimensions of this Metric.
        :rtype: dict(str, str)
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this Metric.
        Qualifiers provided in a metric definition. Available dimensions vary by metric namespace.
        Each dimension takes the form of a key-value pair.

        Example: `\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"`


        :param dimensions: The dimensions of this Metric.
        :type: dict(str, str)
        """
        self._dimensions = dimensions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
