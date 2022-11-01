# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OggDeployment(object):
    """
    Deployment Data for an OggDeployment
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OggDeployment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deployment_name:
            The value to assign to the deployment_name property of this OggDeployment.
        :type deployment_name: str

        :param admin_username:
            The value to assign to the admin_username property of this OggDeployment.
        :type admin_username: str

        :param ogg_version:
            The value to assign to the ogg_version property of this OggDeployment.
        :type ogg_version: str

        :param certificate:
            The value to assign to the certificate property of this OggDeployment.
        :type certificate: str

        """
        self.swagger_types = {
            'deployment_name': 'str',
            'admin_username': 'str',
            'ogg_version': 'str',
            'certificate': 'str'
        }

        self.attribute_map = {
            'deployment_name': 'deploymentName',
            'admin_username': 'adminUsername',
            'ogg_version': 'oggVersion',
            'certificate': 'certificate'
        }

        self._deployment_name = None
        self._admin_username = None
        self._ogg_version = None
        self._certificate = None

    @property
    def deployment_name(self):
        """
        **[Required]** Gets the deployment_name of this OggDeployment.
        The name given to the GoldenGate service deployment.
        The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.


        :return: The deployment_name of this OggDeployment.
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        """
        Sets the deployment_name of this OggDeployment.
        The name given to the GoldenGate service deployment.
        The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.


        :param deployment_name: The deployment_name of this OggDeployment.
        :type: str
        """
        self._deployment_name = deployment_name

    @property
    def admin_username(self):
        """
        **[Required]** Gets the admin_username of this OggDeployment.
        The GoldenGate deployment console username.


        :return: The admin_username of this OggDeployment.
        :rtype: str
        """
        return self._admin_username

    @admin_username.setter
    def admin_username(self, admin_username):
        """
        Sets the admin_username of this OggDeployment.
        The GoldenGate deployment console username.


        :param admin_username: The admin_username of this OggDeployment.
        :type: str
        """
        self._admin_username = admin_username

    @property
    def ogg_version(self):
        """
        Gets the ogg_version of this OggDeployment.
        Version of OGG


        :return: The ogg_version of this OggDeployment.
        :rtype: str
        """
        return self._ogg_version

    @ogg_version.setter
    def ogg_version(self, ogg_version):
        """
        Sets the ogg_version of this OggDeployment.
        Version of OGG


        :param ogg_version: The ogg_version of this OggDeployment.
        :type: str
        """
        self._ogg_version = ogg_version

    @property
    def certificate(self):
        """
        Gets the certificate of this OggDeployment.
        A PEM-encoded SSL certificate.


        :return: The certificate of this OggDeployment.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this OggDeployment.
        A PEM-encoded SSL certificate.


        :param certificate: The certificate of this OggDeployment.
        :type: str
        """
        self._certificate = certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
