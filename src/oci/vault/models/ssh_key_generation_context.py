# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180608

from .secret_generation_context import SecretGenerationContext
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SshKeyGenerationContext(SecretGenerationContext):
    """
    Generates ssh keys. By default, the keys are stored as - {\"publicKey\": \"%GENERATED_PUBLIC_KEY%\", \"privateKey\": \"%GENERATED_PRIVATE_KEY%\"} in PEM format.
    The SecretTemplate must have both %GENERATED_PUBLIC_KEY% and %GENERATED_PRIVATE_KEY% keywords which is later replaced with the respective keys, if provided.
    """

    #: A constant which can be used with the generation_template property of a SshKeyGenerationContext.
    #: This constant has a value of "RSA_2048"
    GENERATION_TEMPLATE_RSA_2048 = "RSA_2048"

    #: A constant which can be used with the generation_template property of a SshKeyGenerationContext.
    #: This constant has a value of "RSA_3072"
    GENERATION_TEMPLATE_RSA_3072 = "RSA_3072"

    #: A constant which can be used with the generation_template property of a SshKeyGenerationContext.
    #: This constant has a value of "RSA_4096"
    GENERATION_TEMPLATE_RSA_4096 = "RSA_4096"

    def __init__(self, **kwargs):
        """
        Initializes a new SshKeyGenerationContext object with values from keyword arguments. The default value of the :py:attr:`~oci.vault.models.SshKeyGenerationContext.generation_type` attribute
        of this class is ``SSH_KEY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param generation_type:
            The value to assign to the generation_type property of this SshKeyGenerationContext.
            Allowed values for this property are: "PASSPHRASE", "SSH_KEY", "BYTES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type generation_type: str

        :param secret_template:
            The value to assign to the secret_template property of this SshKeyGenerationContext.
        :type secret_template: str

        :param generation_template:
            The value to assign to the generation_template property of this SshKeyGenerationContext.
            Allowed values for this property are: "RSA_2048", "RSA_3072", "RSA_4096", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type generation_template: str

        """
        self.swagger_types = {
            'generation_type': 'str',
            'secret_template': 'str',
            'generation_template': 'str'
        }
        self.attribute_map = {
            'generation_type': 'generationType',
            'secret_template': 'secretTemplate',
            'generation_template': 'generationTemplate'
        }
        self._generation_type = None
        self._secret_template = None
        self._generation_template = None
        self._generation_type = 'SSH_KEY'

    @property
    def generation_template(self):
        """
        **[Required]** Gets the generation_template of this SshKeyGenerationContext.
        Name of SSH key generation template to generate SSH key type secret.

        Allowed values for this property are: "RSA_2048", "RSA_3072", "RSA_4096", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The generation_template of this SshKeyGenerationContext.
        :rtype: str
        """
        return self._generation_template

    @generation_template.setter
    def generation_template(self, generation_template):
        """
        Sets the generation_template of this SshKeyGenerationContext.
        Name of SSH key generation template to generate SSH key type secret.


        :param generation_template: The generation_template of this SshKeyGenerationContext.
        :type: str
        """
        allowed_values = ["RSA_2048", "RSA_3072", "RSA_4096"]
        if not value_allowed_none_or_none_sentinel(generation_template, allowed_values):
            generation_template = 'UNKNOWN_ENUM_VALUE'
        self._generation_template = generation_template

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
