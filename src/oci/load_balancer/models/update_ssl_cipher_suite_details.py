# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSSLCipherSuiteDetails(object):
    """
    The configuration details for updating an SSL cipher suite.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSSLCipherSuiteDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ciphers:
            The value to assign to the ciphers property of this UpdateSSLCipherSuiteDetails.
        :type ciphers: list[str]

        """
        self.swagger_types = {
            'ciphers': 'list[str]'
        }

        self.attribute_map = {
            'ciphers': 'ciphers'
        }

        self._ciphers = None

    @property
    def ciphers(self):
        """
        **[Required]** Gets the ciphers of this UpdateSSLCipherSuiteDetails.
        A list of SSL ciphers the load balancer must support for HTTPS or SSL connections.

        The following ciphers are valid values for this property:

        *  __TLSv1.2 ciphers__

                \"AES128-GCM-SHA256\"
                \"AES128-SHA256\"
                \"AES256-GCM-SHA384\"
                \"AES256-SHA256\"
                \"DH-DSS-AES128-GCM-SHA256\"
                \"DH-DSS-AES128-SHA256\"
                \"DH-DSS-AES256-GCM-SHA384\"
                \"DH-DSS-AES256-SHA256\"
                \"DH-RSA-AES128-GCM-SHA256\"
                \"DH-RSA-AES128-SHA256\"
                \"DH-RSA-AES256-GCM-SHA384\"
                \"DH-RSA-AES256-SHA256\"
                \"DHE-DSS-AES128-GCM-SHA256\"
                \"DHE-DSS-AES128-SHA256\"
                \"DHE-DSS-AES256-GCM-SHA384\"
                \"DHE-DSS-AES256-SHA256\"
                \"DHE-RSA-AES128-GCM-SHA256\"
                \"DHE-RSA-AES128-SHA256\"
                \"DHE-RSA-AES256-GCM-SHA384\"
                \"DHE-RSA-AES256-SHA256\"
                \"ECDH-ECDSA-AES128-GCM-SHA256\"
                \"ECDH-ECDSA-AES128-SHA256\"
                \"ECDH-ECDSA-AES256-GCM-SHA384\"
                \"ECDH-ECDSA-AES256-SHA384\"
                \"ECDH-RSA-AES128-GCM-SHA256\"
                \"ECDH-RSA-AES128-SHA256\"
                \"ECDH-RSA-AES256-GCM-SHA384\"
                \"ECDH-RSA-AES256-SHA384\"
                \"ECDHE-ECDSA-AES128-GCM-SHA256\"
                \"ECDHE-ECDSA-AES128-SHA256\"
                \"ECDHE-ECDSA-AES256-GCM-SHA384\"
                \"ECDHE-ECDSA-AES256-SHA384\"
                \"ECDHE-RSA-AES128-GCM-SHA256\"
                \"ECDHE-RSA-AES128-SHA256\"
                \"ECDHE-RSA-AES256-GCM-SHA384\"
                \"ECDHE-RSA-AES256-SHA384\"

        *  __TLSv1 ciphers also supported by TLSv1.2__

                \"AES128-SHA\"
                \"AES256-SHA\"
                \"CAMELLIA128-SHA\"
                \"CAMELLIA256-SHA\"
                \"DES-CBC3-SHA\"
                \"DH-DSS-AES128-SHA\"
                \"DH-DSS-AES256-SHA\"
                \"DH-DSS-CAMELLIA128-SHA\"
                \"DH-DSS-CAMELLIA256-SHA\"
                \"DH-DSS-DES-CBC3-SHAv\"
                \"DH-DSS-SEED-SHA\"
                \"DH-RSA-AES128-SHA\"
                \"DH-RSA-AES256-SHA\"
                \"DH-RSA-CAMELLIA128-SHA\"
                \"DH-RSA-CAMELLIA256-SHA\"
                \"DH-RSA-DES-CBC3-SHA\"
                \"DH-RSA-SEED-SHA\"
                \"DHE-DSS-AES128-SHA\"
                \"DHE-DSS-AES256-SHA\"
                \"DHE-DSS-CAMELLIA128-SHA\"
                \"DHE-DSS-CAMELLIA256-SHA\"
                \"DHE-DSS-DES-CBC3-SHA\"
                \"DHE-DSS-SEED-SHA\"
                \"DHE-RSA-AES128-SHA\"
                \"DHE-RSA-AES256-SHA\"
                \"DHE-RSA-CAMELLIA128-SHA\"
                \"DHE-RSA-CAMELLIA256-SHA\"
                \"DHE-RSA-DES-CBC3-SHA\"
                \"DHE-RSA-SEED-SHA\"
                \"ECDH-ECDSA-AES128-SHA\"
                \"ECDH-ECDSA-AES256-SHA\"
                \"ECDH-ECDSA-DES-CBC3-SHA\"
                \"ECDH-ECDSA-RC4-SHA\"
                \"ECDH-RSA-AES128-SHA\"
                \"ECDH-RSA-AES256-SHA\"
                \"ECDH-RSA-DES-CBC3-SHA\"
                \"ECDH-RSA-RC4-SHA\"
                \"ECDHE-ECDSA-AES128-SHA\"
                \"ECDHE-ECDSA-AES256-SHA\"
                \"ECDHE-ECDSA-DES-CBC3-SHA\"
                \"ECDHE-ECDSA-RC4-SHA\"
                \"ECDHE-RSA-AES128-SHA\"
                \"ECDHE-RSA-AES256-SHA\"
                \"ECDHE-RSA-DES-CBC3-SHA\"
                \"ECDHE-RSA-RC4-SHA\"
                \"IDEA-CBC-SHA\"
                \"KRB5-DES-CBC3-MD5\"
                \"KRB5-DES-CBC3-SHA\"
                \"KRB5-IDEA-CBC-MD5\"
                \"KRB5-IDEA-CBC-SHA\"
                \"KRB5-RC4-MD5\"
                \"KRB5-RC4-SHA\"
                \"PSK-3DES-EDE-CBC-SHA\"
                \"PSK-AES128-CBC-SHA\"
                \"PSK-AES256-CBC-SHA\"
                \"PSK-RC4-SHA\"
                \"RC4-MD5\"
                \"RC4-SHA\"
                \"SEED-SHA\"

        example: `[\"ECDHE-RSA-AES256-GCM-SHA384\",\"ECDHE-ECDSA-AES256-GCM-SHA384\",\"ECDHE-RSA-AES128-GCM-SHA256\"]`


        :return: The ciphers of this UpdateSSLCipherSuiteDetails.
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """
        Sets the ciphers of this UpdateSSLCipherSuiteDetails.
        A list of SSL ciphers the load balancer must support for HTTPS or SSL connections.

        The following ciphers are valid values for this property:

        *  __TLSv1.2 ciphers__

                \"AES128-GCM-SHA256\"
                \"AES128-SHA256\"
                \"AES256-GCM-SHA384\"
                \"AES256-SHA256\"
                \"DH-DSS-AES128-GCM-SHA256\"
                \"DH-DSS-AES128-SHA256\"
                \"DH-DSS-AES256-GCM-SHA384\"
                \"DH-DSS-AES256-SHA256\"
                \"DH-RSA-AES128-GCM-SHA256\"
                \"DH-RSA-AES128-SHA256\"
                \"DH-RSA-AES256-GCM-SHA384\"
                \"DH-RSA-AES256-SHA256\"
                \"DHE-DSS-AES128-GCM-SHA256\"
                \"DHE-DSS-AES128-SHA256\"
                \"DHE-DSS-AES256-GCM-SHA384\"
                \"DHE-DSS-AES256-SHA256\"
                \"DHE-RSA-AES128-GCM-SHA256\"
                \"DHE-RSA-AES128-SHA256\"
                \"DHE-RSA-AES256-GCM-SHA384\"
                \"DHE-RSA-AES256-SHA256\"
                \"ECDH-ECDSA-AES128-GCM-SHA256\"
                \"ECDH-ECDSA-AES128-SHA256\"
                \"ECDH-ECDSA-AES256-GCM-SHA384\"
                \"ECDH-ECDSA-AES256-SHA384\"
                \"ECDH-RSA-AES128-GCM-SHA256\"
                \"ECDH-RSA-AES128-SHA256\"
                \"ECDH-RSA-AES256-GCM-SHA384\"
                \"ECDH-RSA-AES256-SHA384\"
                \"ECDHE-ECDSA-AES128-GCM-SHA256\"
                \"ECDHE-ECDSA-AES128-SHA256\"
                \"ECDHE-ECDSA-AES256-GCM-SHA384\"
                \"ECDHE-ECDSA-AES256-SHA384\"
                \"ECDHE-RSA-AES128-GCM-SHA256\"
                \"ECDHE-RSA-AES128-SHA256\"
                \"ECDHE-RSA-AES256-GCM-SHA384\"
                \"ECDHE-RSA-AES256-SHA384\"

        *  __TLSv1 ciphers also supported by TLSv1.2__

                \"AES128-SHA\"
                \"AES256-SHA\"
                \"CAMELLIA128-SHA\"
                \"CAMELLIA256-SHA\"
                \"DES-CBC3-SHA\"
                \"DH-DSS-AES128-SHA\"
                \"DH-DSS-AES256-SHA\"
                \"DH-DSS-CAMELLIA128-SHA\"
                \"DH-DSS-CAMELLIA256-SHA\"
                \"DH-DSS-DES-CBC3-SHAv\"
                \"DH-DSS-SEED-SHA\"
                \"DH-RSA-AES128-SHA\"
                \"DH-RSA-AES256-SHA\"
                \"DH-RSA-CAMELLIA128-SHA\"
                \"DH-RSA-CAMELLIA256-SHA\"
                \"DH-RSA-DES-CBC3-SHA\"
                \"DH-RSA-SEED-SHA\"
                \"DHE-DSS-AES128-SHA\"
                \"DHE-DSS-AES256-SHA\"
                \"DHE-DSS-CAMELLIA128-SHA\"
                \"DHE-DSS-CAMELLIA256-SHA\"
                \"DHE-DSS-DES-CBC3-SHA\"
                \"DHE-DSS-SEED-SHA\"
                \"DHE-RSA-AES128-SHA\"
                \"DHE-RSA-AES256-SHA\"
                \"DHE-RSA-CAMELLIA128-SHA\"
                \"DHE-RSA-CAMELLIA256-SHA\"
                \"DHE-RSA-DES-CBC3-SHA\"
                \"DHE-RSA-SEED-SHA\"
                \"ECDH-ECDSA-AES128-SHA\"
                \"ECDH-ECDSA-AES256-SHA\"
                \"ECDH-ECDSA-DES-CBC3-SHA\"
                \"ECDH-ECDSA-RC4-SHA\"
                \"ECDH-RSA-AES128-SHA\"
                \"ECDH-RSA-AES256-SHA\"
                \"ECDH-RSA-DES-CBC3-SHA\"
                \"ECDH-RSA-RC4-SHA\"
                \"ECDHE-ECDSA-AES128-SHA\"
                \"ECDHE-ECDSA-AES256-SHA\"
                \"ECDHE-ECDSA-DES-CBC3-SHA\"
                \"ECDHE-ECDSA-RC4-SHA\"
                \"ECDHE-RSA-AES128-SHA\"
                \"ECDHE-RSA-AES256-SHA\"
                \"ECDHE-RSA-DES-CBC3-SHA\"
                \"ECDHE-RSA-RC4-SHA\"
                \"IDEA-CBC-SHA\"
                \"KRB5-DES-CBC3-MD5\"
                \"KRB5-DES-CBC3-SHA\"
                \"KRB5-IDEA-CBC-MD5\"
                \"KRB5-IDEA-CBC-SHA\"
                \"KRB5-RC4-MD5\"
                \"KRB5-RC4-SHA\"
                \"PSK-3DES-EDE-CBC-SHA\"
                \"PSK-AES128-CBC-SHA\"
                \"PSK-AES256-CBC-SHA\"
                \"PSK-RC4-SHA\"
                \"RC4-MD5\"
                \"RC4-SHA\"
                \"SEED-SHA\"

        example: `[\"ECDHE-RSA-AES256-GCM-SHA384\",\"ECDHE-ECDSA-AES256-GCM-SHA384\",\"ECDHE-RSA-AES128-GCM-SHA256\"]`


        :param ciphers: The ciphers of this UpdateSSLCipherSuiteDetails.
        :type: list[str]
        """
        self._ciphers = ciphers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
