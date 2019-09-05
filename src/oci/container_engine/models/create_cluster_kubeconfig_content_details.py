# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateClusterKubeconfigContentDetails(object):
    """
    The properties that define a request to create a cluster kubeconfig.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateClusterKubeconfigContentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param token_version:
            The value to assign to the token_version property of this CreateClusterKubeconfigContentDetails.
        :type token_version: str

        :param expiration:
            The value to assign to the expiration property of this CreateClusterKubeconfigContentDetails.
        :type expiration: int

        """
        self.swagger_types = {
            'token_version': 'str',
            'expiration': 'int'
        }

        self.attribute_map = {
            'token_version': 'tokenVersion',
            'expiration': 'expiration'
        }

        self._token_version = None
        self._expiration = None

    @property
    def token_version(self):
        """
        Gets the token_version of this CreateClusterKubeconfigContentDetails.
        The version of the kubeconfig token. Supported values 1.0.0 and 2.0.0


        :return: The token_version of this CreateClusterKubeconfigContentDetails.
        :rtype: str
        """
        return self._token_version

    @token_version.setter
    def token_version(self, token_version):
        """
        Sets the token_version of this CreateClusterKubeconfigContentDetails.
        The version of the kubeconfig token. Supported values 1.0.0 and 2.0.0


        :param token_version: The token_version of this CreateClusterKubeconfigContentDetails.
        :type: str
        """
        self._token_version = token_version

    @property
    def expiration(self):
        """
        Gets the expiration of this CreateClusterKubeconfigContentDetails.
        The desired expiration, in seconds, to use for the kubeconfig token.
        Important Note, expiration field is only honored for token version 1.0.0


        :return: The expiration of this CreateClusterKubeconfigContentDetails.
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """
        Sets the expiration of this CreateClusterKubeconfigContentDetails.
        The desired expiration, in seconds, to use for the kubeconfig token.
        Important Note, expiration field is only honored for token version 1.0.0


        :param expiration: The expiration of this CreateClusterKubeconfigContentDetails.
        :type: int
        """
        self._expiration = expiration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
