# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OciFunction(object):
    """
    The information about the OCI Function.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OciFunction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param function_id:
            The value to assign to the function_id property of this OciFunction.
        :type function_id: str

        :param region_id:
            The value to assign to the region_id property of this OciFunction.
        :type region_id: str

        :param fn_config_definition:
            The value to assign to the fn_config_definition property of this OciFunction.
        :type fn_config_definition: oci.data_integration.models.ConfigDefinition

        :param input_shape:
            The value to assign to the input_shape property of this OciFunction.
        :type input_shape: oci.data_integration.models.Shape

        :param output_shape:
            The value to assign to the output_shape property of this OciFunction.
        :type output_shape: oci.data_integration.models.Shape

        """
        self.swagger_types = {
            'function_id': 'str',
            'region_id': 'str',
            'fn_config_definition': 'ConfigDefinition',
            'input_shape': 'Shape',
            'output_shape': 'Shape'
        }

        self.attribute_map = {
            'function_id': 'functionId',
            'region_id': 'regionId',
            'fn_config_definition': 'fnConfigDefinition',
            'input_shape': 'inputShape',
            'output_shape': 'outputShape'
        }

        self._function_id = None
        self._region_id = None
        self._fn_config_definition = None
        self._input_shape = None
        self._output_shape = None

    @property
    def function_id(self):
        """
        Gets the function_id of this OciFunction.
        Ocid of the OCI Function.


        :return: The function_id of this OciFunction.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this OciFunction.
        Ocid of the OCI Function.


        :param function_id: The function_id of this OciFunction.
        :type: str
        """
        self._function_id = function_id

    @property
    def region_id(self):
        """
        Gets the region_id of this OciFunction.
        Region where the OCI Function is deployed.


        :return: The region_id of this OciFunction.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this OciFunction.
        Region where the OCI Function is deployed.


        :param region_id: The region_id of this OciFunction.
        :type: str
        """
        self._region_id = region_id

    @property
    def fn_config_definition(self):
        """
        Gets the fn_config_definition of this OciFunction.

        :return: The fn_config_definition of this OciFunction.
        :rtype: oci.data_integration.models.ConfigDefinition
        """
        return self._fn_config_definition

    @fn_config_definition.setter
    def fn_config_definition(self, fn_config_definition):
        """
        Sets the fn_config_definition of this OciFunction.

        :param fn_config_definition: The fn_config_definition of this OciFunction.
        :type: oci.data_integration.models.ConfigDefinition
        """
        self._fn_config_definition = fn_config_definition

    @property
    def input_shape(self):
        """
        Gets the input_shape of this OciFunction.

        :return: The input_shape of this OciFunction.
        :rtype: oci.data_integration.models.Shape
        """
        return self._input_shape

    @input_shape.setter
    def input_shape(self, input_shape):
        """
        Sets the input_shape of this OciFunction.

        :param input_shape: The input_shape of this OciFunction.
        :type: oci.data_integration.models.Shape
        """
        self._input_shape = input_shape

    @property
    def output_shape(self):
        """
        Gets the output_shape of this OciFunction.

        :return: The output_shape of this OciFunction.
        :rtype: oci.data_integration.models.Shape
        """
        return self._output_shape

    @output_shape.setter
    def output_shape(self, output_shape):
        """
        Sets the output_shape of this OciFunction.

        :param output_shape: The output_shape of this OciFunction.
        :type: oci.data_integration.models.Shape
        """
        self._output_shape = output_shape

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
