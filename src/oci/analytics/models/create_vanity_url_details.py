# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVanityUrlDetails(object):
    """
    Input payload to create a vanity url.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVanityUrlDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateVanityUrlDetails.
        :type description: str

        :param hosts:
            The value to assign to the hosts property of this CreateVanityUrlDetails.
        :type hosts: list[str]

        :param passphrase:
            The value to assign to the passphrase property of this CreateVanityUrlDetails.
        :type passphrase: str

        :param private_key:
            The value to assign to the private_key property of this CreateVanityUrlDetails.
        :type private_key: str

        :param public_certificate:
            The value to assign to the public_certificate property of this CreateVanityUrlDetails.
        :type public_certificate: str

        :param ca_certificate:
            The value to assign to the ca_certificate property of this CreateVanityUrlDetails.
        :type ca_certificate: str

        """
        self.swagger_types = {
            'description': 'str',
            'hosts': 'list[str]',
            'passphrase': 'str',
            'private_key': 'str',
            'public_certificate': 'str',
            'ca_certificate': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'hosts': 'hosts',
            'passphrase': 'passphrase',
            'private_key': 'privateKey',
            'public_certificate': 'publicCertificate',
            'ca_certificate': 'caCertificate'
        }

        self._description = None
        self._hosts = None
        self._passphrase = None
        self._private_key = None
        self._public_certificate = None
        self._ca_certificate = None

    @property
    def description(self):
        """
        Gets the description of this CreateVanityUrlDetails.
        Optional description.


        :return: The description of this CreateVanityUrlDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateVanityUrlDetails.
        Optional description.


        :param description: The description of this CreateVanityUrlDetails.
        :type: str
        """
        self._description = description

    @property
    def hosts(self):
        """
        **[Required]** Gets the hosts of this CreateVanityUrlDetails.
        List of fully qualified hostnames supported by this vanity URL definition (max of 3).


        :return: The hosts of this CreateVanityUrlDetails.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this CreateVanityUrlDetails.
        List of fully qualified hostnames supported by this vanity URL definition (max of 3).


        :param hosts: The hosts of this CreateVanityUrlDetails.
        :type: list[str]
        """
        self._hosts = hosts

    @property
    def passphrase(self):
        """
        Gets the passphrase of this CreateVanityUrlDetails.
        Passphrase for the PEM Private key (if any).


        :return: The passphrase of this CreateVanityUrlDetails.
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """
        Sets the passphrase of this CreateVanityUrlDetails.
        Passphrase for the PEM Private key (if any).


        :param passphrase: The passphrase of this CreateVanityUrlDetails.
        :type: str
        """
        self._passphrase = passphrase

    @property
    def private_key(self):
        """
        **[Required]** Gets the private_key of this CreateVanityUrlDetails.
        PEM Private key for HTTPS connections.


        :return: The private_key of this CreateVanityUrlDetails.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """
        Sets the private_key of this CreateVanityUrlDetails.
        PEM Private key for HTTPS connections.


        :param private_key: The private_key of this CreateVanityUrlDetails.
        :type: str
        """
        self._private_key = private_key

    @property
    def public_certificate(self):
        """
        **[Required]** Gets the public_certificate of this CreateVanityUrlDetails.
        PEM certificate for HTTPS connections.


        :return: The public_certificate of this CreateVanityUrlDetails.
        :rtype: str
        """
        return self._public_certificate

    @public_certificate.setter
    def public_certificate(self, public_certificate):
        """
        Sets the public_certificate of this CreateVanityUrlDetails.
        PEM certificate for HTTPS connections.


        :param public_certificate: The public_certificate of this CreateVanityUrlDetails.
        :type: str
        """
        self._public_certificate = public_certificate

    @property
    def ca_certificate(self):
        """
        **[Required]** Gets the ca_certificate of this CreateVanityUrlDetails.
        PEM CA certificate(s) for HTTPS connections. This may include multiple PEM certificates.


        :return: The ca_certificate of this CreateVanityUrlDetails.
        :rtype: str
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        """
        Sets the ca_certificate of this CreateVanityUrlDetails.
        PEM CA certificate(s) for HTTPS connections. This may include multiple PEM certificates.


        :param ca_certificate: The ca_certificate of this CreateVanityUrlDetails.
        :type: str
        """
        self._ca_certificate = ca_certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
