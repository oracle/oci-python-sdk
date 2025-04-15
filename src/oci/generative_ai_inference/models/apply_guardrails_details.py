# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplyGuardrailsDetails(object):
    """
    Details for applying guardrails to the input text.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplyGuardrailsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input:
            The value to assign to the input property of this ApplyGuardrailsDetails.
        :type input: oci.generative_ai_inference.models.GuardrailsInput

        :param guardrail_configs:
            The value to assign to the guardrail_configs property of this ApplyGuardrailsDetails.
        :type guardrail_configs: oci.generative_ai_inference.models.GuardrailConfigs

        :param compartment_id:
            The value to assign to the compartment_id property of this ApplyGuardrailsDetails.
        :type compartment_id: str

        """
        self.swagger_types = {
            'input': 'GuardrailsInput',
            'guardrail_configs': 'GuardrailConfigs',
            'compartment_id': 'str'
        }
        self.attribute_map = {
            'input': 'input',
            'guardrail_configs': 'guardrailConfigs',
            'compartment_id': 'compartmentId'
        }
        self._input = None
        self._guardrail_configs = None
        self._compartment_id = None

    @property
    def input(self):
        """
        **[Required]** Gets the input of this ApplyGuardrailsDetails.

        :return: The input of this ApplyGuardrailsDetails.
        :rtype: oci.generative_ai_inference.models.GuardrailsInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """
        Sets the input of this ApplyGuardrailsDetails.

        :param input: The input of this ApplyGuardrailsDetails.
        :type: oci.generative_ai_inference.models.GuardrailsInput
        """
        self._input = input

    @property
    def guardrail_configs(self):
        """
        **[Required]** Gets the guardrail_configs of this ApplyGuardrailsDetails.

        :return: The guardrail_configs of this ApplyGuardrailsDetails.
        :rtype: oci.generative_ai_inference.models.GuardrailConfigs
        """
        return self._guardrail_configs

    @guardrail_configs.setter
    def guardrail_configs(self, guardrail_configs):
        """
        Sets the guardrail_configs of this ApplyGuardrailsDetails.

        :param guardrail_configs: The guardrail_configs of this ApplyGuardrailsDetails.
        :type: oci.generative_ai_inference.models.GuardrailConfigs
        """
        self._guardrail_configs = guardrail_configs

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ApplyGuardrailsDetails.
        The OCID of the compartment to apply guardrails.


        :return: The compartment_id of this ApplyGuardrailsDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ApplyGuardrailsDetails.
        The OCID of the compartment to apply guardrails.


        :param compartment_id: The compartment_id of this ApplyGuardrailsDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
