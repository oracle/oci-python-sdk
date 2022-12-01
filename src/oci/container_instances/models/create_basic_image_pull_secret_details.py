# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_image_pull_secret_details import CreateImagePullSecretDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBasicImagePullSecretDetails(CreateImagePullSecretDetails):
    """
    A CreateBasicImagePullSecretDetails is a ImagePullSecret which accepts username and password as credentials information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBasicImagePullSecretDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.container_instances.models.CreateBasicImagePullSecretDetails.secret_type` attribute
        of this class is ``BASIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param secret_type:
            The value to assign to the secret_type property of this CreateBasicImagePullSecretDetails.
            Allowed values for this property are: "BASIC", "VAULT"
        :type secret_type: str

        :param registry_endpoint:
            The value to assign to the registry_endpoint property of this CreateBasicImagePullSecretDetails.
        :type registry_endpoint: str

        :param username:
            The value to assign to the username property of this CreateBasicImagePullSecretDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this CreateBasicImagePullSecretDetails.
        :type password: str

        """
        self.swagger_types = {
            'secret_type': 'str',
            'registry_endpoint': 'str',
            'username': 'str',
            'password': 'str'
        }

        self.attribute_map = {
            'secret_type': 'secretType',
            'registry_endpoint': 'registryEndpoint',
            'username': 'username',
            'password': 'password'
        }

        self._secret_type = None
        self._registry_endpoint = None
        self._username = None
        self._password = None
        self._secret_type = 'BASIC'

    @property
    def username(self):
        """
        **[Required]** Gets the username of this CreateBasicImagePullSecretDetails.
        The username which should be used with the registry for authentication. The value is expected in base64 format.


        :return: The username of this CreateBasicImagePullSecretDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateBasicImagePullSecretDetails.
        The username which should be used with the registry for authentication. The value is expected in base64 format.


        :param username: The username of this CreateBasicImagePullSecretDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        **[Required]** Gets the password of this CreateBasicImagePullSecretDetails.
        The password which should be used with the registry for authentication. The value is expected in base64 format.


        :return: The password of this CreateBasicImagePullSecretDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateBasicImagePullSecretDetails.
        The password which should be used with the registry for authentication. The value is expected in base64 format.


        :param password: The password of this CreateBasicImagePullSecretDetails.
        :type: str
        """
        self._password = password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
