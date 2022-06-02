# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TerraformAdvancedOptions(object):
    """
    Specifies advanced options for Terraform commands. These options are not necessary for normal usage of Terraform.
    """

    #: A constant which can be used with the detailed_log_level property of a TerraformAdvancedOptions.
    #: This constant has a value of "ERROR"
    DETAILED_LOG_LEVEL_ERROR = "ERROR"

    #: A constant which can be used with the detailed_log_level property of a TerraformAdvancedOptions.
    #: This constant has a value of "WARN"
    DETAILED_LOG_LEVEL_WARN = "WARN"

    #: A constant which can be used with the detailed_log_level property of a TerraformAdvancedOptions.
    #: This constant has a value of "INFO"
    DETAILED_LOG_LEVEL_INFO = "INFO"

    #: A constant which can be used with the detailed_log_level property of a TerraformAdvancedOptions.
    #: This constant has a value of "DEBUG"
    DETAILED_LOG_LEVEL_DEBUG = "DEBUG"

    #: A constant which can be used with the detailed_log_level property of a TerraformAdvancedOptions.
    #: This constant has a value of "TRACE"
    DETAILED_LOG_LEVEL_TRACE = "TRACE"

    def __init__(self, **kwargs):
        """
        Initializes a new TerraformAdvancedOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_refresh_required:
            The value to assign to the is_refresh_required property of this TerraformAdvancedOptions.
        :type is_refresh_required: bool

        :param parallelism:
            The value to assign to the parallelism property of this TerraformAdvancedOptions.
        :type parallelism: int

        :param detailed_log_level:
            The value to assign to the detailed_log_level property of this TerraformAdvancedOptions.
            Allowed values for this property are: "ERROR", "WARN", "INFO", "DEBUG", "TRACE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type detailed_log_level: str

        """
        self.swagger_types = {
            'is_refresh_required': 'bool',
            'parallelism': 'int',
            'detailed_log_level': 'str'
        }

        self.attribute_map = {
            'is_refresh_required': 'isRefreshRequired',
            'parallelism': 'parallelism',
            'detailed_log_level': 'detailedLogLevel'
        }

        self._is_refresh_required = None
        self._parallelism = None
        self._detailed_log_level = None

    @property
    def is_refresh_required(self):
        """
        Gets the is_refresh_required of this TerraformAdvancedOptions.
        Specifies whether to refresh the state for each resource before running the job (operation).
        Refreshing the state can affect performance. Consider setting to `false` if the configuration includes several resources.
        Used with the following operations: `PLAN`, `APPLY`, `DESTROY`.


        :return: The is_refresh_required of this TerraformAdvancedOptions.
        :rtype: bool
        """
        return self._is_refresh_required

    @is_refresh_required.setter
    def is_refresh_required(self, is_refresh_required):
        """
        Sets the is_refresh_required of this TerraformAdvancedOptions.
        Specifies whether to refresh the state for each resource before running the job (operation).
        Refreshing the state can affect performance. Consider setting to `false` if the configuration includes several resources.
        Used with the following operations: `PLAN`, `APPLY`, `DESTROY`.


        :param is_refresh_required: The is_refresh_required of this TerraformAdvancedOptions.
        :type: bool
        """
        self._is_refresh_required = is_refresh_required

    @property
    def parallelism(self):
        """
        Gets the parallelism of this TerraformAdvancedOptions.
        Limits the number of concurrent Terraform operations when `walking the graph`__.
        Use this parameter to help debug Terraform issues or to accomplish certain special use cases.
        A higher value might cause resources to be throttled.
        Used with the following operations: `PLAN`, `APPLY`, `DESTROY`.

        __ https://www.terraform.io/docs/internals/graph.html#walking-the-graph


        :return: The parallelism of this TerraformAdvancedOptions.
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """
        Sets the parallelism of this TerraformAdvancedOptions.
        Limits the number of concurrent Terraform operations when `walking the graph`__.
        Use this parameter to help debug Terraform issues or to accomplish certain special use cases.
        A higher value might cause resources to be throttled.
        Used with the following operations: `PLAN`, `APPLY`, `DESTROY`.

        __ https://www.terraform.io/docs/internals/graph.html#walking-the-graph


        :param parallelism: The parallelism of this TerraformAdvancedOptions.
        :type: int
        """
        self._parallelism = parallelism

    @property
    def detailed_log_level(self):
        """
        Gets the detailed_log_level of this TerraformAdvancedOptions.
        Enables detailed logs at the specified verbosity for running the job (operation).

        Allowed values for this property are: "ERROR", "WARN", "INFO", "DEBUG", "TRACE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The detailed_log_level of this TerraformAdvancedOptions.
        :rtype: str
        """
        return self._detailed_log_level

    @detailed_log_level.setter
    def detailed_log_level(self, detailed_log_level):
        """
        Sets the detailed_log_level of this TerraformAdvancedOptions.
        Enables detailed logs at the specified verbosity for running the job (operation).


        :param detailed_log_level: The detailed_log_level of this TerraformAdvancedOptions.
        :type: str
        """
        allowed_values = ["ERROR", "WARN", "INFO", "DEBUG", "TRACE"]
        if not value_allowed_none_or_none_sentinel(detailed_log_level, allowed_values):
            detailed_log_level = 'UNKNOWN_ENUM_VALUE'
        self._detailed_log_level = detailed_log_level

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
