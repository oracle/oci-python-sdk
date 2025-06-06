# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployPipelineParameter(object):
    """
    Parameter name for which the values will be supplied at the time of deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeployPipelineParameter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DeployPipelineParameter.
        :type name: str

        :param default_value:
            The value to assign to the default_value property of this DeployPipelineParameter.
        :type default_value: str

        :param description:
            The value to assign to the description property of this DeployPipelineParameter.
        :type description: str

        """
        self.swagger_types = {
            'name': 'str',
            'default_value': 'str',
            'description': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'default_value': 'defaultValue',
            'description': 'description'
        }
        self._name = None
        self._default_value = None
        self._description = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DeployPipelineParameter.
        Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$.


        :return: The name of this DeployPipelineParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeployPipelineParameter.
        Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$.


        :param name: The name of this DeployPipelineParameter.
        :type: str
        """
        self._name = name

    @property
    def default_value(self):
        """
        Gets the default_value of this DeployPipelineParameter.
        Default value of the parameter.


        :return: The default_value of this DeployPipelineParameter.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this DeployPipelineParameter.
        Default value of the parameter.


        :param default_value: The default_value of this DeployPipelineParameter.
        :type: str
        """
        self._default_value = default_value

    @property
    def description(self):
        """
        Gets the description of this DeployPipelineParameter.
        Description of the parameter.


        :return: The description of this DeployPipelineParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeployPipelineParameter.
        Description of the parameter.


        :param description: The description of this DeployPipelineParameter.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
