# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class Certificate(object):

    def __init__(self):

        self.swagger_types = {
            'ca_certificate': 'str',
            'certificate_name': 'str',
            'public_certificate': 'str'
        }

        self.attribute_map = {
            'ca_certificate': 'caCertificate',
            'certificate_name': 'certificateName',
            'public_certificate': 'publicCertificate'
        }

        self._ca_certificate = None
        self._certificate_name = None
        self._public_certificate = None

    @property
    def ca_certificate(self):
        """
        Gets the ca_certificate of this Certificate.
        The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.

        Example:

            -----BEGIN CERTIFICATE-----
            MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix
            EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD
            VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y
            aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy
            ...
            -----END CERTIFICATE-----


        :return: The ca_certificate of this Certificate.
        :rtype: str
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        """
        Sets the ca_certificate of this Certificate.
        The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.

        Example:

            -----BEGIN CERTIFICATE-----
            MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix
            EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD
            VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y
            aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy
            ...
            -----END CERTIFICATE-----


        :param ca_certificate: The ca_certificate of this Certificate.
        :type: str
        """
        self._ca_certificate = ca_certificate

    @property
    def certificate_name(self):
        """
        Gets the certificate_name of this Certificate.
        A friendly name for the certificate bundle. It must be unique and it cannot be changed.

        Example: `My certificate bundle`


        :return: The certificate_name of this Certificate.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """
        Sets the certificate_name of this Certificate.
        A friendly name for the certificate bundle. It must be unique and it cannot be changed.

        Example: `My certificate bundle`


        :param certificate_name: The certificate_name of this Certificate.
        :type: str
        """
        self._certificate_name = certificate_name

    @property
    def public_certificate(self):
        """
        Gets the public_certificate of this Certificate.
        The public certificate, in PEM format, that you received from your SSL certificate provider.

        Example:

            -----BEGIN CERTIFICATE-----
            MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG
            A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE
            MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl
            YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw
            ...
            -----END CERTIFICATE-----


        :return: The public_certificate of this Certificate.
        :rtype: str
        """
        return self._public_certificate

    @public_certificate.setter
    def public_certificate(self, public_certificate):
        """
        Sets the public_certificate of this Certificate.
        The public certificate, in PEM format, that you received from your SSL certificate provider.

        Example:

            -----BEGIN CERTIFICATE-----
            MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG
            A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE
            MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl
            YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw
            ...
            -----END CERTIFICATE-----


        :param public_certificate: The public_certificate of this Certificate.
        :type: str
        """
        self._public_certificate = public_certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
