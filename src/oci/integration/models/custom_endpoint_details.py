# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomEndpointDetails(object):
    """
    Details for a custom endpoint for the integration instance.
    """

    #: A constant which can be used with the managed_type property of a CustomEndpointDetails.
    #: This constant has a value of "ORACLE_MANAGED"
    MANAGED_TYPE_ORACLE_MANAGED = "ORACLE_MANAGED"

    #: A constant which can be used with the managed_type property of a CustomEndpointDetails.
    #: This constant has a value of "CUSTOMER_MANAGED"
    MANAGED_TYPE_CUSTOMER_MANAGED = "CUSTOMER_MANAGED"

    #: A constant which can be used with the dns_type property of a CustomEndpointDetails.
    #: This constant has a value of "OCI"
    DNS_TYPE_OCI = "OCI"

    def __init__(self, **kwargs):
        """
        Initializes a new CustomEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname:
            The value to assign to the hostname property of this CustomEndpointDetails.
        :type hostname: str

        :param managed_type:
            The value to assign to the managed_type property of this CustomEndpointDetails.
            Allowed values for this property are: "ORACLE_MANAGED", "CUSTOMER_MANAGED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type managed_type: str

        :param dns_zone_name:
            The value to assign to the dns_zone_name property of this CustomEndpointDetails.
        :type dns_zone_name: str

        :param dns_type:
            The value to assign to the dns_type property of this CustomEndpointDetails.
            Allowed values for this property are: "OCI", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type dns_type: str

        :param certificate_secret_id:
            The value to assign to the certificate_secret_id property of this CustomEndpointDetails.
        :type certificate_secret_id: str

        :param certificate_secret_version:
            The value to assign to the certificate_secret_version property of this CustomEndpointDetails.
        :type certificate_secret_version: int

        :param alias:
            The value to assign to the alias property of this CustomEndpointDetails.
        :type alias: str

        """
        self.swagger_types = {
            'hostname': 'str',
            'managed_type': 'str',
            'dns_zone_name': 'str',
            'dns_type': 'str',
            'certificate_secret_id': 'str',
            'certificate_secret_version': 'int',
            'alias': 'str'
        }
        self.attribute_map = {
            'hostname': 'hostname',
            'managed_type': 'managedType',
            'dns_zone_name': 'dnsZoneName',
            'dns_type': 'dnsType',
            'certificate_secret_id': 'certificateSecretId',
            'certificate_secret_version': 'certificateSecretVersion',
            'alias': 'alias'
        }
        self._hostname = None
        self._managed_type = None
        self._dns_zone_name = None
        self._dns_type = None
        self._certificate_secret_id = None
        self._certificate_secret_version = None
        self._alias = None

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this CustomEndpointDetails.
        A custom hostname to be used for the integration instance URL, in FQDN format.


        :return: The hostname of this CustomEndpointDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CustomEndpointDetails.
        A custom hostname to be used for the integration instance URL, in FQDN format.


        :param hostname: The hostname of this CustomEndpointDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def managed_type(self):
        """
        Gets the managed_type of this CustomEndpointDetails.
        Indicates if custom endpoint is managed by oracle or customer.

        Allowed values for this property are: "ORACLE_MANAGED", "CUSTOMER_MANAGED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The managed_type of this CustomEndpointDetails.
        :rtype: str
        """
        return self._managed_type

    @managed_type.setter
    def managed_type(self, managed_type):
        """
        Sets the managed_type of this CustomEndpointDetails.
        Indicates if custom endpoint is managed by oracle or customer.


        :param managed_type: The managed_type of this CustomEndpointDetails.
        :type: str
        """
        allowed_values = ["ORACLE_MANAGED", "CUSTOMER_MANAGED"]
        if not value_allowed_none_or_none_sentinel(managed_type, allowed_values):
            managed_type = 'UNKNOWN_ENUM_VALUE'
        self._managed_type = managed_type

    @property
    def dns_zone_name(self):
        """
        Gets the dns_zone_name of this CustomEndpointDetails.
        DNS Zone name


        :return: The dns_zone_name of this CustomEndpointDetails.
        :rtype: str
        """
        return self._dns_zone_name

    @dns_zone_name.setter
    def dns_zone_name(self, dns_zone_name):
        """
        Sets the dns_zone_name of this CustomEndpointDetails.
        DNS Zone name


        :param dns_zone_name: The dns_zone_name of this CustomEndpointDetails.
        :type: str
        """
        self._dns_zone_name = dns_zone_name

    @property
    def dns_type(self):
        """
        Gets the dns_type of this CustomEndpointDetails.
        Type of DNS.

        Allowed values for this property are: "OCI", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The dns_type of this CustomEndpointDetails.
        :rtype: str
        """
        return self._dns_type

    @dns_type.setter
    def dns_type(self, dns_type):
        """
        Sets the dns_type of this CustomEndpointDetails.
        Type of DNS.


        :param dns_type: The dns_type of this CustomEndpointDetails.
        :type: str
        """
        allowed_values = ["OCI"]
        if not value_allowed_none_or_none_sentinel(dns_type, allowed_values):
            dns_type = 'UNKNOWN_ENUM_VALUE'
        self._dns_type = dns_type

    @property
    def certificate_secret_id(self):
        """
        Gets the certificate_secret_id of this CustomEndpointDetails.
        Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.


        :return: The certificate_secret_id of this CustomEndpointDetails.
        :rtype: str
        """
        return self._certificate_secret_id

    @certificate_secret_id.setter
    def certificate_secret_id(self, certificate_secret_id):
        """
        Sets the certificate_secret_id of this CustomEndpointDetails.
        Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.


        :param certificate_secret_id: The certificate_secret_id of this CustomEndpointDetails.
        :type: str
        """
        self._certificate_secret_id = certificate_secret_id

    @property
    def certificate_secret_version(self):
        """
        Gets the certificate_secret_version of this CustomEndpointDetails.
        The secret version used for the certificate-secret-id (if certificate-secret-id is specified).


        :return: The certificate_secret_version of this CustomEndpointDetails.
        :rtype: int
        """
        return self._certificate_secret_version

    @certificate_secret_version.setter
    def certificate_secret_version(self, certificate_secret_version):
        """
        Sets the certificate_secret_version of this CustomEndpointDetails.
        The secret version used for the certificate-secret-id (if certificate-secret-id is specified).


        :param certificate_secret_version: The certificate_secret_version of this CustomEndpointDetails.
        :type: int
        """
        self._certificate_secret_version = certificate_secret_version

    @property
    def alias(self):
        """
        Gets the alias of this CustomEndpointDetails.
        When creating the DNS CNAME record for the custom hostname, this value must be specified in the rdata.


        :return: The alias of this CustomEndpointDetails.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this CustomEndpointDetails.
        When creating the DNS CNAME record for the custom hostname, this value must be specified in the rdata.


        :param alias: The alias of this CustomEndpointDetails.
        :type: str
        """
        self._alias = alias

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
