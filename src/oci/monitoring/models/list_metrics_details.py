# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListMetricsDetails(object):
    """
    The request details for retrieving metric definitions. Specify optional properties to filter the returned results.
    Use an asterisk (&#42;) as a wildcard character, placed anywhere in the string.
    For example, to search for all metrics with names that begin with \"disk\", specify \"name\" as \"disk&#42;\".
    If no properties are specified, then all metric definitions within the request scope are returned.
    """

    #: A constant which can be used with the sort_by property of a ListMetricsDetails.
    #: This constant has a value of "NAMESPACE"
    SORT_BY_NAMESPACE = "NAMESPACE"

    #: A constant which can be used with the sort_by property of a ListMetricsDetails.
    #: This constant has a value of "NAME"
    SORT_BY_NAME = "NAME"

    #: A constant which can be used with the sort_by property of a ListMetricsDetails.
    #: This constant has a value of "RESOURCEGROUP"
    SORT_BY_RESOURCEGROUP = "RESOURCEGROUP"

    #: A constant which can be used with the sort_order property of a ListMetricsDetails.
    #: This constant has a value of "ASC"
    SORT_ORDER_ASC = "ASC"

    #: A constant which can be used with the sort_order property of a ListMetricsDetails.
    #: This constant has a value of "DESC"
    SORT_ORDER_DESC = "DESC"

    def __init__(self, **kwargs):
        """
        Initializes a new ListMetricsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ListMetricsDetails.
        :type name: str

        :param namespace:
            The value to assign to the namespace property of this ListMetricsDetails.
        :type namespace: str

        :param resource_group:
            The value to assign to the resource_group property of this ListMetricsDetails.
        :type resource_group: str

        :param dimension_filters:
            The value to assign to the dimension_filters property of this ListMetricsDetails.
        :type dimension_filters: dict(str, str)

        :param group_by:
            The value to assign to the group_by property of this ListMetricsDetails.
        :type group_by: list[str]

        :param sort_by:
            The value to assign to the sort_by property of this ListMetricsDetails.
            Allowed values for this property are: "NAMESPACE", "NAME", "RESOURCEGROUP"
        :type sort_by: str

        :param sort_order:
            The value to assign to the sort_order property of this ListMetricsDetails.
            Allowed values for this property are: "ASC", "DESC"
        :type sort_order: str

        """
        self.swagger_types = {
            'name': 'str',
            'namespace': 'str',
            'resource_group': 'str',
            'dimension_filters': 'dict(str, str)',
            'group_by': 'list[str]',
            'sort_by': 'str',
            'sort_order': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'namespace': 'namespace',
            'resource_group': 'resourceGroup',
            'dimension_filters': 'dimensionFilters',
            'group_by': 'groupBy',
            'sort_by': 'sortBy',
            'sort_order': 'sortOrder'
        }

        self._name = None
        self._namespace = None
        self._resource_group = None
        self._dimension_filters = None
        self._group_by = None
        self._sort_by = None
        self._sort_order = None

    @property
    def name(self):
        """
        Gets the name of this ListMetricsDetails.
        The metric name to use when searching for metric definitions.

        Example: `CpuUtilization`


        :return: The name of this ListMetricsDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ListMetricsDetails.
        The metric name to use when searching for metric definitions.

        Example: `CpuUtilization`


        :param name: The name of this ListMetricsDetails.
        :type: str
        """
        self._name = name

    @property
    def namespace(self):
        """
        Gets the namespace of this ListMetricsDetails.
        The source service or application to use when searching for metric definitions.

        Example: `oci_computeagent`


        :return: The namespace of this ListMetricsDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this ListMetricsDetails.
        The source service or application to use when searching for metric definitions.

        Example: `oci_computeagent`


        :param namespace: The namespace of this ListMetricsDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def resource_group(self):
        """
        Gets the resource_group of this ListMetricsDetails.
        Resource group that you want to use as a filter. The specified resource group must exist in the definition of the posted metric. Only one resource group can be applied per metric.
        A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
        Avoid entering confidential information.

        Example: `frontend-fleet`


        :return: The resource_group of this ListMetricsDetails.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """
        Sets the resource_group of this ListMetricsDetails.
        Resource group that you want to use as a filter. The specified resource group must exist in the definition of the posted metric. Only one resource group can be applied per metric.
        A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
        Avoid entering confidential information.

        Example: `frontend-fleet`


        :param resource_group: The resource_group of this ListMetricsDetails.
        :type: str
        """
        self._resource_group = resource_group

    @property
    def dimension_filters(self):
        """
        Gets the dimension_filters of this ListMetricsDetails.
        Qualifiers that you want to use when searching for metric definitions.
        Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair.

        Example: { \"resourceId\": \"<var>&lt;instance_OCID&gt;</var>\" }


        :return: The dimension_filters of this ListMetricsDetails.
        :rtype: dict(str, str)
        """
        return self._dimension_filters

    @dimension_filters.setter
    def dimension_filters(self, dimension_filters):
        """
        Sets the dimension_filters of this ListMetricsDetails.
        Qualifiers that you want to use when searching for metric definitions.
        Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair.

        Example: { \"resourceId\": \"<var>&lt;instance_OCID&gt;</var>\" }


        :param dimension_filters: The dimension_filters of this ListMetricsDetails.
        :type: dict(str, str)
        """
        self._dimension_filters = dimension_filters

    @property
    def group_by(self):
        """
        Gets the group_by of this ListMetricsDetails.
        Group metrics by these fields in the response. For example, to list all metric namespaces available
                  in a compartment, groupBy the \"namespace\" field. Supported fields: namespace, name, resourceGroup.

        Example - group by namespace:
        `[ \"namespace\" ]`


        :return: The group_by of this ListMetricsDetails.
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """
        Sets the group_by of this ListMetricsDetails.
        Group metrics by these fields in the response. For example, to list all metric namespaces available
                  in a compartment, groupBy the \"namespace\" field. Supported fields: namespace, name, resourceGroup.

        Example - group by namespace:
        `[ \"namespace\" ]`


        :param group_by: The group_by of this ListMetricsDetails.
        :type: list[str]
        """
        self._group_by = group_by

    @property
    def sort_by(self):
        """
        Gets the sort_by of this ListMetricsDetails.
        The field to use when sorting returned metric definitions. Only one sorting level is provided.

        Example: `NAMESPACE`

        Allowed values for this property are: "NAMESPACE", "NAME", "RESOURCEGROUP"


        :return: The sort_by of this ListMetricsDetails.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """
        Sets the sort_by of this ListMetricsDetails.
        The field to use when sorting returned metric definitions. Only one sorting level is provided.

        Example: `NAMESPACE`


        :param sort_by: The sort_by of this ListMetricsDetails.
        :type: str
        """
        allowed_values = ["NAMESPACE", "NAME", "RESOURCEGROUP"]
        if not value_allowed_none_or_none_sentinel(sort_by, allowed_values):
            raise ValueError(
                "Invalid value for `sort_by`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sort_by = sort_by

    @property
    def sort_order(self):
        """
        Gets the sort_order of this ListMetricsDetails.
        The sort order to use when sorting returned metric definitions. Ascending (ASC) or
        descending (DESC).

        Example: `ASC`

        Allowed values for this property are: "ASC", "DESC"


        :return: The sort_order of this ListMetricsDetails.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this ListMetricsDetails.
        The sort order to use when sorting returned metric definitions. Ascending (ASC) or
        descending (DESC).

        Example: `ASC`


        :param sort_order: The sort_order of this ListMetricsDetails.
        :type: str
        """
        allowed_values = ["ASC", "DESC"]
        if not value_allowed_none_or_none_sentinel(sort_order, allowed_values):
            raise ValueError(
                "Invalid value for `sort_order`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sort_order = sort_order

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
