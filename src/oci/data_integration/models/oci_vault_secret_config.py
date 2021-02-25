# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .secret_config import SecretConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OciVaultSecretConfig(SecretConfig):
    """
    Properties used for specifying OCI vault configuration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OciVaultSecretConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.OciVaultSecretConfig.model_type` attribute
        of this class is ``OCI_VAULT_SECRET_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this OciVaultSecretConfig.
            Allowed values for this property are: "OCI_VAULT_SECRET_CONFIG"
        :type model_type: str

        :param secret_id:
            The value to assign to the secret_id property of this OciVaultSecretConfig.
        :type secret_id: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'secret_id': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'secret_id': 'secretId'
        }

        self._model_type = None
        self._secret_id = None
        self._model_type = 'OCI_VAULT_SECRET_CONFIG'

    @property
    def secret_id(self):
        """
        Gets the secret_id of this OciVaultSecretConfig.
        OCID of the OCI vault secret


        :return: The secret_id of this OciVaultSecretConfig.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """
        Sets the secret_id of this OciVaultSecretConfig.
        OCID of the OCI vault secret


        :param secret_id: The secret_id of this OciVaultSecretConfig.
        :type: str
        """
        self._secret_id = secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
