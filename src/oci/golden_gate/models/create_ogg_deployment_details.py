# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOggDeploymentDetails(object):
    """
    Deployment Data for creating an OggDeployment
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOggDeploymentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deployment_name:
            The value to assign to the deployment_name property of this CreateOggDeploymentDetails.
        :type deployment_name: str

        :param admin_username:
            The value to assign to the admin_username property of this CreateOggDeploymentDetails.
        :type admin_username: str

        :param admin_password:
            The value to assign to the admin_password property of this CreateOggDeploymentDetails.
        :type admin_password: str

        :param certificate:
            The value to assign to the certificate property of this CreateOggDeploymentDetails.
        :type certificate: str

        :param key:
            The value to assign to the key property of this CreateOggDeploymentDetails.
        :type key: str

        """
        self.swagger_types = {
            'deployment_name': 'str',
            'admin_username': 'str',
            'admin_password': 'str',
            'certificate': 'str',
            'key': 'str'
        }

        self.attribute_map = {
            'deployment_name': 'deploymentName',
            'admin_username': 'adminUsername',
            'admin_password': 'adminPassword',
            'certificate': 'certificate',
            'key': 'key'
        }

        self._deployment_name = None
        self._admin_username = None
        self._admin_password = None
        self._certificate = None
        self._key = None

    @property
    def deployment_name(self):
        """
        **[Required]** Gets the deployment_name of this CreateOggDeploymentDetails.
        The name given to the GoldenGate service deployment.
        The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.


        :return: The deployment_name of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        """
        Sets the deployment_name of this CreateOggDeploymentDetails.
        The name given to the GoldenGate service deployment.
        The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.


        :param deployment_name: The deployment_name of this CreateOggDeploymentDetails.
        :type: str
        """
        self._deployment_name = deployment_name

    @property
    def admin_username(self):
        """
        **[Required]** Gets the admin_username of this CreateOggDeploymentDetails.
        The GoldenGate deployment console username.


        :return: The admin_username of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._admin_username

    @admin_username.setter
    def admin_username(self, admin_username):
        """
        Sets the admin_username of this CreateOggDeploymentDetails.
        The GoldenGate deployment console username.


        :param admin_username: The admin_username of this CreateOggDeploymentDetails.
        :type: str
        """
        self._admin_username = admin_username

    @property
    def admin_password(self):
        """
        **[Required]** Gets the admin_password of this CreateOggDeploymentDetails.
        The password associated with the GoldenGate deployment console username.
        The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric,
        and 1 special character. Special characters such as \u2018$\u2019, \u2018^\u2019, or \u2018?\u2019 are not allowed.


        :return: The admin_password of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this CreateOggDeploymentDetails.
        The password associated with the GoldenGate deployment console username.
        The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric,
        and 1 special character. Special characters such as \u2018$\u2019, \u2018^\u2019, or \u2018?\u2019 are not allowed.


        :param admin_password: The admin_password of this CreateOggDeploymentDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def certificate(self):
        """
        Gets the certificate of this CreateOggDeploymentDetails.
        A PEM-encoded SSL certificate.


        :return: The certificate of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this CreateOggDeploymentDetails.
        A PEM-encoded SSL certificate.


        :param certificate: The certificate of this CreateOggDeploymentDetails.
        :type: str
        """
        self._certificate = certificate

    @property
    def key(self):
        """
        Gets the key of this CreateOggDeploymentDetails.
        A PEM-encoded private key.


        :return: The key of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateOggDeploymentDetails.
        A PEM-encoded private key.


        :param key: The key of this CreateOggDeploymentDetails.
        :type: str
        """
        self._key = key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
