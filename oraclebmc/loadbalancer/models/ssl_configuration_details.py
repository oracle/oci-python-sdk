# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class SSLConfigurationDetails(object):

    def __init__(self):

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
        Gets the certificate_name of this SSLConfigurationDetails.
        A friendly name for the certificate bundle. It must be unique and it cannot be changed.

        Example: `My certificate bundle`


        :return: The certificate_name of this SSLConfigurationDetails.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """
        Sets the certificate_name of this SSLConfigurationDetails.
        A friendly name for the certificate bundle. It must be unique and it cannot be changed.

        Example: `My certificate bundle`


        :param certificate_name: The certificate_name of this SSLConfigurationDetails.
        :type: str
        """
        self._certificate_name = certificate_name

    @property
    def verify_depth(self):
        """
        Gets the verify_depth of this SSLConfigurationDetails.
        The maximum depth for peer certificate chain verification.

        Example: `3`


        :return: The verify_depth of this SSLConfigurationDetails.
        :rtype: int
        """
        return self._verify_depth

    @verify_depth.setter
    def verify_depth(self, verify_depth):
        """
        Sets the verify_depth of this SSLConfigurationDetails.
        The maximum depth for peer certificate chain verification.

        Example: `3`


        :param verify_depth: The verify_depth of this SSLConfigurationDetails.
        :type: int
        """
        self._verify_depth = verify_depth

    @property
    def verify_peer_certificate(self):
        """
        Gets the verify_peer_certificate of this SSLConfigurationDetails.
        Whether the load balancer listener should verify peer certificates.

        Example: `true`


        :return: The verify_peer_certificate of this SSLConfigurationDetails.
        :rtype: bool
        """
        return self._verify_peer_certificate

    @verify_peer_certificate.setter
    def verify_peer_certificate(self, verify_peer_certificate):
        """
        Sets the verify_peer_certificate of this SSLConfigurationDetails.
        Whether the load balancer listener should verify peer certificates.

        Example: `true`


        :param verify_peer_certificate: The verify_peer_certificate of this SSLConfigurationDetails.
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
