# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_image_pull_secret_details import CreateImagePullSecretDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVaultImagePullSecretDetails(CreateImagePullSecretDetails):
    """
    A CreateVaultImagePullSecretDetails is a ImagePullSecret which accepts secretId as credentials information.
    **Sample Format for username and password in Vault Secret**
    ```
    {
    \"username\": \"xxxxxxxxxx\",
    \"password\": \"xxxxxxxxxx\"
    }
    ```
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVaultImagePullSecretDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.container_instances.models.CreateVaultImagePullSecretDetails.secret_type` attribute
        of this class is ``VAULT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param secret_type:
            The value to assign to the secret_type property of this CreateVaultImagePullSecretDetails.
            Allowed values for this property are: "BASIC", "VAULT"
        :type secret_type: str

        :param registry_endpoint:
            The value to assign to the registry_endpoint property of this CreateVaultImagePullSecretDetails.
        :type registry_endpoint: str

        :param secret_id:
            The value to assign to the secret_id property of this CreateVaultImagePullSecretDetails.
        :type secret_id: str

        """
        self.swagger_types = {
            'secret_type': 'str',
            'registry_endpoint': 'str',
            'secret_id': 'str'
        }

        self.attribute_map = {
            'secret_type': 'secretType',
            'registry_endpoint': 'registryEndpoint',
            'secret_id': 'secretId'
        }

        self._secret_type = None
        self._registry_endpoint = None
        self._secret_id = None
        self._secret_type = 'VAULT'

    @property
    def secret_id(self):
        """
        **[Required]** Gets the secret_id of this CreateVaultImagePullSecretDetails.
        The OCID of the secret for registry credentials.


        :return: The secret_id of this CreateVaultImagePullSecretDetails.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """
        Sets the secret_id of this CreateVaultImagePullSecretDetails.
        The OCID of the secret for registry credentials.


        :param secret_id: The secret_id of this CreateVaultImagePullSecretDetails.
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
