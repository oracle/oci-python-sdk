# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SSLConfiguration(object):
    """
    A listener's SSL handling configuration.

    To use SSL, a listener must be associated with a :class:`Certificate`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SSLConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_name:
            The value to assign to the certificate_name property of this SSLConfiguration.
        :type certificate_name: str

        :param verify_depth:
            The value to assign to the verify_depth property of this SSLConfiguration.
        :type verify_depth: int

        :param verify_peer_certificate:
            The value to assign to the verify_peer_certificate property of this SSLConfiguration.
        :type verify_peer_certificate: bool

        """
        self.swagger_types = {
            'certificate_name': 'str',
            'verify_depth': 'int',
            'verify_peer_certificate': 'bool'
        }

        self.attribute_map = {
            'certificate_name': 'certificateName',
            'verify_depth': 'verifyDepth',
            'verify_peer_certificate': 'verifyPeerCertificate'
        }

        self._certificate_name = None
        self._verify_depth = None
        self._verify_peer_certificate = None

    @property
    def certificate_name(self):
        """
        **[Required]** Gets the certificate_name of this SSLConfiguration.
        A friendly name for the certificate bundle. It must be unique and it cannot be changed.
        Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
        Certificate bundle names cannot contain spaces. Avoid entering confidential information.

        Example: `example_certificate_bundle`


        :return: The certificate_name of this SSLConfiguration.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """
        Sets the certificate_name of this SSLConfiguration.
        A friendly name for the certificate bundle. It must be unique and it cannot be changed.
        Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
        Certificate bundle names cannot contain spaces. Avoid entering confidential information.

        Example: `example_certificate_bundle`


        :param certificate_name: The certificate_name of this SSLConfiguration.
        :type: str
        """
        self._certificate_name = certificate_name

    @property
    def verify_depth(self):
        """
        **[Required]** Gets the verify_depth of this SSLConfiguration.
        The maximum depth for peer certificate chain verification.

        Example: `3`


        :return: The verify_depth of this SSLConfiguration.
        :rtype: int
        """
        return self._verify_depth

    @verify_depth.setter
    def verify_depth(self, verify_depth):
        """
        Sets the verify_depth of this SSLConfiguration.
        The maximum depth for peer certificate chain verification.

        Example: `3`


        :param verify_depth: The verify_depth of this SSLConfiguration.
        :type: int
        """
        self._verify_depth = verify_depth

    @property
    def verify_peer_certificate(self):
        """
        **[Required]** Gets the verify_peer_certificate of this SSLConfiguration.
        Whether the load balancer listener should verify peer certificates.

        Example: `true`


        :return: The verify_peer_certificate of this SSLConfiguration.
        :rtype: bool
        """
        return self._verify_peer_certificate

    @verify_peer_certificate.setter
    def verify_peer_certificate(self, verify_peer_certificate):
        """
        Sets the verify_peer_certificate of this SSLConfiguration.
        Whether the load balancer listener should verify peer certificates.

        Example: `true`


        :param verify_peer_certificate: The verify_peer_certificate of this SSLConfiguration.
        :type: bool
        """
        self._verify_peer_certificate = verify_peer_certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
