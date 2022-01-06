# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SSLConfiguration(object):
    """
    A listener's SSL handling configuration.

    To use SSL, a listener must be associated with a :class:`Certificate`.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the server_order_preference property of a SSLConfiguration.
    #: This constant has a value of "ENABLED"
    SERVER_ORDER_PREFERENCE_ENABLED = "ENABLED"

    #: A constant which can be used with the server_order_preference property of a SSLConfiguration.
    #: This constant has a value of "DISABLED"
    SERVER_ORDER_PREFERENCE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new SSLConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param verify_depth:
            The value to assign to the verify_depth property of this SSLConfiguration.
        :type verify_depth: int

        :param verify_peer_certificate:
            The value to assign to the verify_peer_certificate property of this SSLConfiguration.
        :type verify_peer_certificate: bool

        :param trusted_certificate_authority_ids:
            The value to assign to the trusted_certificate_authority_ids property of this SSLConfiguration.
        :type trusted_certificate_authority_ids: list[str]

        :param certificate_ids:
            The value to assign to the certificate_ids property of this SSLConfiguration.
        :type certificate_ids: list[str]

        :param certificate_name:
            The value to assign to the certificate_name property of this SSLConfiguration.
        :type certificate_name: str

        :param server_order_preference:
            The value to assign to the server_order_preference property of this SSLConfiguration.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type server_order_preference: str

        :param cipher_suite_name:
            The value to assign to the cipher_suite_name property of this SSLConfiguration.
        :type cipher_suite_name: str

        :param protocols:
            The value to assign to the protocols property of this SSLConfiguration.
        :type protocols: list[str]

        """
        self.swagger_types = {
            'verify_depth': 'int',
            'verify_peer_certificate': 'bool',
            'trusted_certificate_authority_ids': 'list[str]',
            'certificate_ids': 'list[str]',
            'certificate_name': 'str',
            'server_order_preference': 'str',
            'cipher_suite_name': 'str',
            'protocols': 'list[str]'
        }

        self.attribute_map = {
            'verify_depth': 'verifyDepth',
            'verify_peer_certificate': 'verifyPeerCertificate',
            'trusted_certificate_authority_ids': 'trustedCertificateAuthorityIds',
            'certificate_ids': 'certificateIds',
            'certificate_name': 'certificateName',
            'server_order_preference': 'serverOrderPreference',
            'cipher_suite_name': 'cipherSuiteName',
            'protocols': 'protocols'
        }

        self._verify_depth = None
        self._verify_peer_certificate = None
        self._trusted_certificate_authority_ids = None
        self._certificate_ids = None
        self._certificate_name = None
        self._server_order_preference = None
        self._cipher_suite_name = None
        self._protocols = None

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

    @property
    def trusted_certificate_authority_ids(self):
        """
        Gets the trusted_certificate_authority_ids of this SSLConfiguration.
        Ids for OCI certificates service CA or CA bundles for the load balancer to trust.

        Example: `[ocid1.cabundle.oc1.us-ashburn-1.amaaaaaaav3bgsaagl4zzyqdop5i2vuwoqewdvauuw34llqa74otq2jdsfyq]`


        :return: The trusted_certificate_authority_ids of this SSLConfiguration.
        :rtype: list[str]
        """
        return self._trusted_certificate_authority_ids

    @trusted_certificate_authority_ids.setter
    def trusted_certificate_authority_ids(self, trusted_certificate_authority_ids):
        """
        Sets the trusted_certificate_authority_ids of this SSLConfiguration.
        Ids for OCI certificates service CA or CA bundles for the load balancer to trust.

        Example: `[ocid1.cabundle.oc1.us-ashburn-1.amaaaaaaav3bgsaagl4zzyqdop5i2vuwoqewdvauuw34llqa74otq2jdsfyq]`


        :param trusted_certificate_authority_ids: The trusted_certificate_authority_ids of this SSLConfiguration.
        :type: list[str]
        """
        self._trusted_certificate_authority_ids = trusted_certificate_authority_ids

    @property
    def certificate_ids(self):
        """
        Gets the certificate_ids of this SSLConfiguration.
        Ids for OCI certificates service certificates. Currently only a single Id may be passed.

        Example: `[ocid1.certificate.oc1.us-ashburn-1.amaaaaaaav3bgsaa5o2q7rh5nfmkkukfkogasqhk6af2opufhjlqg7m6jqzq]`


        :return: The certificate_ids of this SSLConfiguration.
        :rtype: list[str]
        """
        return self._certificate_ids

    @certificate_ids.setter
    def certificate_ids(self, certificate_ids):
        """
        Sets the certificate_ids of this SSLConfiguration.
        Ids for OCI certificates service certificates. Currently only a single Id may be passed.

        Example: `[ocid1.certificate.oc1.us-ashburn-1.amaaaaaaav3bgsaa5o2q7rh5nfmkkukfkogasqhk6af2opufhjlqg7m6jqzq]`


        :param certificate_ids: The certificate_ids of this SSLConfiguration.
        :type: list[str]
        """
        self._certificate_ids = certificate_ids

    @property
    def certificate_name(self):
        """
        Gets the certificate_name of this SSLConfiguration.
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
    def server_order_preference(self):
        """
        Gets the server_order_preference of this SSLConfiguration.
        When this attribute is set to ENABLED, the system gives preference to the server ciphers over the client
        ciphers.

        **Note:** This configuration is applicable only when the load balancer is acting as an SSL/HTTPS server. This
                  field is ignored when the `SSLConfiguration` object is associated with a backend set.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The server_order_preference of this SSLConfiguration.
        :rtype: str
        """
        return self._server_order_preference

    @server_order_preference.setter
    def server_order_preference(self, server_order_preference):
        """
        Sets the server_order_preference of this SSLConfiguration.
        When this attribute is set to ENABLED, the system gives preference to the server ciphers over the client
        ciphers.

        **Note:** This configuration is applicable only when the load balancer is acting as an SSL/HTTPS server. This
                  field is ignored when the `SSLConfiguration` object is associated with a backend set.


        :param server_order_preference: The server_order_preference of this SSLConfiguration.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(server_order_preference, allowed_values):
            server_order_preference = 'UNKNOWN_ENUM_VALUE'
        self._server_order_preference = server_order_preference

    @property
    def cipher_suite_name(self):
        """
        Gets the cipher_suite_name of this SSLConfiguration.
        The name of the cipher suite to use for HTTPS or SSL connections.

        If this field is not specified, the default is `oci-default-ssl-cipher-suite-v1`.

        **Notes:**

        *  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher
           suite. Clients cannot perform an SSL handshake if there is an incompatible configuration.
        *  You must ensure compatibility between the ciphers configured in the cipher suite and the configured
           certificates. For example, RSA-based ciphers require RSA certificates and ECDSA-based ciphers require ECDSA
           certificates.
        *  If the cipher configuration is not modified after load balancer creation, the `GET` operation returns
           `oci-default-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing listeners
           that predate this feature.
        *  If the cipher configuration was modified using Oracle operations after load balancer creation, the `GET`
           operation returns `oci-customized-ssl-cipher-suite` as the value of this field in the SSL configuration for
           existing listeners that predate this feature.
        *  The `GET` operation returns `oci-wider-compatible-ssl-cipher-suite-v1` as the value of this field in the SSL
           configuration for existing backend sets that predate this feature.
        *  If the `GET` operation on a listener returns `oci-customized-ssl-cipher-suite` as the value of this field,
           you must specify an appropriate predefined or custom cipher suite name when updating the resource.
        *  The `oci-customized-ssl-cipher-suite` Oracle reserved cipher suite name is not accepted as valid input for
           this field.

        example: `example_cipher_suite`


        :return: The cipher_suite_name of this SSLConfiguration.
        :rtype: str
        """
        return self._cipher_suite_name

    @cipher_suite_name.setter
    def cipher_suite_name(self, cipher_suite_name):
        """
        Sets the cipher_suite_name of this SSLConfiguration.
        The name of the cipher suite to use for HTTPS or SSL connections.

        If this field is not specified, the default is `oci-default-ssl-cipher-suite-v1`.

        **Notes:**

        *  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher
           suite. Clients cannot perform an SSL handshake if there is an incompatible configuration.
        *  You must ensure compatibility between the ciphers configured in the cipher suite and the configured
           certificates. For example, RSA-based ciphers require RSA certificates and ECDSA-based ciphers require ECDSA
           certificates.
        *  If the cipher configuration is not modified after load balancer creation, the `GET` operation returns
           `oci-default-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing listeners
           that predate this feature.
        *  If the cipher configuration was modified using Oracle operations after load balancer creation, the `GET`
           operation returns `oci-customized-ssl-cipher-suite` as the value of this field in the SSL configuration for
           existing listeners that predate this feature.
        *  The `GET` operation returns `oci-wider-compatible-ssl-cipher-suite-v1` as the value of this field in the SSL
           configuration for existing backend sets that predate this feature.
        *  If the `GET` operation on a listener returns `oci-customized-ssl-cipher-suite` as the value of this field,
           you must specify an appropriate predefined or custom cipher suite name when updating the resource.
        *  The `oci-customized-ssl-cipher-suite` Oracle reserved cipher suite name is not accepted as valid input for
           this field.

        example: `example_cipher_suite`


        :param cipher_suite_name: The cipher_suite_name of this SSLConfiguration.
        :type: str
        """
        self._cipher_suite_name = cipher_suite_name

    @property
    def protocols(self):
        """
        Gets the protocols of this SSLConfiguration.
        A list of SSL protocols the load balancer must support for HTTPS or SSL connections.

        The load balancer uses SSL protocols to establish a secure connection between a client and a server. A secure
        connection ensures that all data passed between the client and the server is private.

        The Load Balancing service supports the following protocols:

        *  TLSv1
        *  TLSv1.1
        *  TLSv1.2

        If this field is not specified, TLSv1.2 is the default.

        **Warning:** All SSL listeners created on a given port must use the same set of SSL protocols.

        **Notes:**

        *  The handshake to establish an SSL connection fails if the client supports none of the specified protocols.
        *  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher
           suite.
        *  For all existing load balancer listeners and backend sets that predate this feature, the `GET` operation
           displays a list of SSL protocols currently used by those resources.

        example: `[\"TLSv1.1\", \"TLSv1.2\"]`


        :return: The protocols of this SSLConfiguration.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """
        Sets the protocols of this SSLConfiguration.
        A list of SSL protocols the load balancer must support for HTTPS or SSL connections.

        The load balancer uses SSL protocols to establish a secure connection between a client and a server. A secure
        connection ensures that all data passed between the client and the server is private.

        The Load Balancing service supports the following protocols:

        *  TLSv1
        *  TLSv1.1
        *  TLSv1.2

        If this field is not specified, TLSv1.2 is the default.

        **Warning:** All SSL listeners created on a given port must use the same set of SSL protocols.

        **Notes:**

        *  The handshake to establish an SSL connection fails if the client supports none of the specified protocols.
        *  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher
           suite.
        *  For all existing load balancer listeners and backend sets that predate this feature, the `GET` operation
           displays a list of SSL protocols currently used by those resources.

        example: `[\"TLSv1.1\", \"TLSv1.2\"]`


        :param protocols: The protocols of this SSLConfiguration.
        :type: list[str]
        """
        self._protocols = protocols

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
