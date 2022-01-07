# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .operator import Operator
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Intersect(Operator):
    """
    The information about a intersect object.
    """

    #: A constant which can be used with the intersect_type property of a Intersect.
    #: This constant has a value of "NAME"
    INTERSECT_TYPE_NAME = "NAME"

    #: A constant which can be used with the intersect_type property of a Intersect.
    #: This constant has a value of "POSITION"
    INTERSECT_TYPE_POSITION = "POSITION"

    def __init__(self, **kwargs):
        """
        Initializes a new Intersect object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.Intersect.model_type` attribute
        of this class is ``INTERSECT_OPERATOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Intersect.
            Allowed values for this property are: "SOURCE_OPERATOR", "FILTER_OPERATOR", "JOINER_OPERATOR", "AGGREGATOR_OPERATOR", "PROJECTION_OPERATOR", "TARGET_OPERATOR", "DISTINCT_OPERATOR", "SORT_OPERATOR", "UNION_OPERATOR", "INTERSECT_OPERATOR", "MINUS_OPERATOR", "MERGE_OPERATOR", "START_OPERATOR", "END_OPERATOR", "PIPELINE_OPERATOR", "TASK_OPERATOR", "EXPRESSION_OPERATOR", "LOOKUP_OPERATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this Intersect.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this Intersect.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Intersect.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this Intersect.
        :type name: str

        :param description:
            The value to assign to the description property of this Intersect.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this Intersect.
        :type object_version: int

        :param input_ports:
            The value to assign to the input_ports property of this Intersect.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this Intersect.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param object_status:
            The value to assign to the object_status property of this Intersect.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this Intersect.
        :type identifier: str

        :param parameters:
            The value to assign to the parameters property of this Intersect.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this Intersect.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param intersect_type:
            The value to assign to the intersect_type property of this Intersect.
            Allowed values for this property are: "NAME", "POSITION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type intersect_type: str

        :param is_all:
            The value to assign to the is_all property of this Intersect.
        :type is_all: bool

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[OutputPort]',
            'object_status': 'int',
            'identifier': 'str',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'intersect_type': 'str',
            'is_all': 'bool'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues',
            'intersect_type': 'intersectType',
            'is_all': 'isAll'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._input_ports = None
        self._output_ports = None
        self._object_status = None
        self._identifier = None
        self._parameters = None
        self._op_config_values = None
        self._intersect_type = None
        self._is_all = None
        self._model_type = 'INTERSECT_OPERATOR'

    @property
    def intersect_type(self):
        """
        Gets the intersect_type of this Intersect.
        intersectType

        Allowed values for this property are: "NAME", "POSITION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The intersect_type of this Intersect.
        :rtype: str
        """
        return self._intersect_type

    @intersect_type.setter
    def intersect_type(self, intersect_type):
        """
        Sets the intersect_type of this Intersect.
        intersectType


        :param intersect_type: The intersect_type of this Intersect.
        :type: str
        """
        allowed_values = ["NAME", "POSITION"]
        if not value_allowed_none_or_none_sentinel(intersect_type, allowed_values):
            intersect_type = 'UNKNOWN_ENUM_VALUE'
        self._intersect_type = intersect_type

    @property
    def is_all(self):
        """
        Gets the is_all of this Intersect.
        The information about the intersect all.


        :return: The is_all of this Intersect.
        :rtype: bool
        """
        return self._is_all

    @is_all.setter
    def is_all(self, is_all):
        """
        Sets the is_all of this Intersect.
        The information about the intersect all.


        :param is_all: The is_all of this Intersect.
        :type: bool
        """
        self._is_all = is_all

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
