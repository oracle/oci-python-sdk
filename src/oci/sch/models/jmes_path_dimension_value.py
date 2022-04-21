# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dimension_value_details import DimensionValueDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JmesPathDimensionValue(DimensionValueDetails):
    """
    Evaluated type of dimension value.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JmesPathDimensionValue object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.JmesPathDimensionValue.kind` attribute
        of this class is ``jmesPath`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this JmesPathDimensionValue.
            Allowed values for this property are: "jmesPath", "static"
        :type kind: str

        :param path:
            The value to assign to the path property of this JmesPathDimensionValue.
        :type path: str

        """
        self.swagger_types = {
            'kind': 'str',
            'path': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'path': 'path'
        }

        self._kind = None
        self._path = None
        self._kind = 'jmesPath'

    @property
    def path(self):
        """
        **[Required]** Gets the path of this JmesPathDimensionValue.
        The location to use for deriving the dimension value (evaluated).
        The path must start with `logContent` in an acceptable notation style with supported `JMESPath selectors`__: expression with dot and index operator (`.` and `:func:`metric_data_details`.
        The returned value depends on the results of evaluation.
        If the evaluated value is valid, then the evaluated value is returned without double quotes. (Any front or trailing double quotes are trimmed before returning the value. For example, the evaluated value `\"compartmentId\"` is returned as `compartmentId`.)
        If the evaluated value is invalid, then the returned value is `SCH_EVAL_INVALID_VALUE`.
        If the evaluated value is empty, then the returned value is `SCH_EVAL_VALUE_EMPTY`.

        __ https://jmespath.org/specification.html


        :return: The path of this JmesPathDimensionValue.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this JmesPathDimensionValue.
        The location to use for deriving the dimension value (evaluated).
        The path must start with `logContent` in an acceptable notation style with supported `JMESPath selectors`__: expression with dot and index operator (`.` and `:func:`metric_data_details`.
        The returned value depends on the results of evaluation.
        If the evaluated value is valid, then the evaluated value is returned without double quotes. (Any front or trailing double quotes are trimmed before returning the value. For example, the evaluated value `\"compartmentId\"` is returned as `compartmentId`.)
        If the evaluated value is invalid, then the returned value is `SCH_EVAL_INVALID_VALUE`.
        If the evaluated value is empty, then the returned value is `SCH_EVAL_VALUE_EMPTY`.

        __ https://jmespath.org/specification.html


        :param path: The path of this JmesPathDimensionValue.
        :type: str
        """
        self._path = path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
