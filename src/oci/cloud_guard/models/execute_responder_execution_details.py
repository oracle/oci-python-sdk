# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecuteResponderExecutionDetails(object):
    """
    The configuration details for a responder rule execution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExecuteResponderExecutionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param configurations:
            The value to assign to the configurations property of this ExecuteResponderExecutionDetails.
        :type configurations: list[oci.cloud_guard.models.ResponderConfiguration]

        """
        self.swagger_types = {
            'configurations': 'list[ResponderConfiguration]'
        }
        self.attribute_map = {
            'configurations': 'configurations'
        }
        self._configurations = None

    @property
    def configurations(self):
        """
        Gets the configurations of this ExecuteResponderExecutionDetails.
        List of responder rule configurations


        :return: The configurations of this ExecuteResponderExecutionDetails.
        :rtype: list[oci.cloud_guard.models.ResponderConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this ExecuteResponderExecutionDetails.
        List of responder rule configurations


        :param configurations: The configurations of this ExecuteResponderExecutionDetails.
        :type: list[oci.cloud_guard.models.ResponderConfiguration]
        """
        self._configurations = configurations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
