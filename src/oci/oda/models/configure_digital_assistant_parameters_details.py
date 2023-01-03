# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigureDigitalAssistantParametersDetails(object):
    """
    Properties for configuring the Digital Assistant Parameters in a Digital Assistant instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigureDigitalAssistantParametersDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parameters:
            The value to assign to the parameters property of this ConfigureDigitalAssistantParametersDetails.
        :type parameters: list[oci.oda.models.DigitalAssistantParameterValue]

        """
        self.swagger_types = {
            'parameters': 'list[DigitalAssistantParameterValue]'
        }

        self.attribute_map = {
            'parameters': 'parameters'
        }

        self._parameters = None

    @property
    def parameters(self):
        """
        **[Required]** Gets the parameters of this ConfigureDigitalAssistantParametersDetails.
        The values to use to configure the Digital Assistant Parameters.


        :return: The parameters of this ConfigureDigitalAssistantParametersDetails.
        :rtype: list[oci.oda.models.DigitalAssistantParameterValue]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this ConfigureDigitalAssistantParametersDetails.
        The values to use to configure the Digital Assistant Parameters.


        :param parameters: The parameters of this ConfigureDigitalAssistantParametersDetails.
        :type: list[oci.oda.models.DigitalAssistantParameterValue]
        """
        self._parameters = parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
