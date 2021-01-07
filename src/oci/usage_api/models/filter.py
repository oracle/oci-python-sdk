# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Filter(object):
    """
    The filter object for query usage.
    """

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "AND"
    OPERATOR_AND = "AND"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "NOT"
    OPERATOR_NOT = "NOT"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "OR"
    OPERATOR_OR = "OR"

    def __init__(self, **kwargs):
        """
        Initializes a new Filter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operator:
            The value to assign to the operator property of this Filter.
            Allowed values for this property are: "AND", "NOT", "OR"
        :type operator: str

        :param dimensions:
            The value to assign to the dimensions property of this Filter.
        :type dimensions: list[oci.usage_api.models.Dimension]

        :param tags:
            The value to assign to the tags property of this Filter.
        :type tags: list[oci.usage_api.models.Tag]

        :param filters:
            The value to assign to the filters property of this Filter.
        :type filters: list[oci.usage_api.models.Filter]

        """
        self.swagger_types = {
            'operator': 'str',
            'dimensions': 'list[Dimension]',
            'tags': 'list[Tag]',
            'filters': 'list[Filter]'
        }

        self.attribute_map = {
            'operator': 'operator',
            'dimensions': 'dimensions',
            'tags': 'tags',
            'filters': 'filters'
        }

        self._operator = None
        self._dimensions = None
        self._tags = None
        self._filters = None

    @property
    def operator(self):
        """
        Gets the operator of this Filter.
        The filter operator. Example: 'AND', 'OR', 'NOT'.

        Allowed values for this property are: "AND", "NOT", "OR"


        :return: The operator of this Filter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this Filter.
        The filter operator. Example: 'AND', 'OR', 'NOT'.


        :param operator: The operator of this Filter.
        :type: str
        """
        allowed_values = ["AND", "NOT", "OR"]
        if not value_allowed_none_or_none_sentinel(operator, allowed_values):
            raise ValueError(
                "Invalid value for `operator`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._operator = operator

    @property
    def dimensions(self):
        """
        Gets the dimensions of this Filter.
        The dimensions to filter on.


        :return: The dimensions of this Filter.
        :rtype: list[oci.usage_api.models.Dimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this Filter.
        The dimensions to filter on.


        :param dimensions: The dimensions of this Filter.
        :type: list[oci.usage_api.models.Dimension]
        """
        self._dimensions = dimensions

    @property
    def tags(self):
        """
        Gets the tags of this Filter.
        The tags to filter on.


        :return: The tags of this Filter.
        :rtype: list[oci.usage_api.models.Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Filter.
        The tags to filter on.


        :param tags: The tags of this Filter.
        :type: list[oci.usage_api.models.Tag]
        """
        self._tags = tags

    @property
    def filters(self):
        """
        Gets the filters of this Filter.
        The nested filter object.


        :return: The filters of this Filter.
        :rtype: list[oci.usage_api.models.Filter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this Filter.
        The nested filter object.


        :param filters: The filters of this Filter.
        :type: list[oci.usage_api.models.Filter]
        """
        self._filters = filters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
