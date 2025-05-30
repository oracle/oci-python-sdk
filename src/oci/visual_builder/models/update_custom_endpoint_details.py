# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCustomEndpointDetails(object):
    """
    Details for a custom endpoint for the vb instance (update).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCustomEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname:
            The value to assign to the hostname property of this UpdateCustomEndpointDetails.
        :type hostname: str

        :param certificate_secret_id:
            The value to assign to the certificate_secret_id property of this UpdateCustomEndpointDetails.
        :type certificate_secret_id: str

        """
        self.swagger_types = {
            'hostname': 'str',
            'certificate_secret_id': 'str'
        }
        self.attribute_map = {
            'hostname': 'hostname',
            'certificate_secret_id': 'certificateSecretId'
        }
        self._hostname = None
        self._certificate_secret_id = None

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this UpdateCustomEndpointDetails.
        A custom hostname to be used for the vb instance URL, in FQDN format.


        :return: The hostname of this UpdateCustomEndpointDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this UpdateCustomEndpointDetails.
        A custom hostname to be used for the vb instance URL, in FQDN format.


        :param hostname: The hostname of this UpdateCustomEndpointDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def certificate_secret_id(self):
        """
        Gets the certificate_secret_id of this UpdateCustomEndpointDetails.
        Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
        All certificates should be stored in a single base64 encoded secret.
        Note the update will fail if this is not a valid certificate.


        :return: The certificate_secret_id of this UpdateCustomEndpointDetails.
        :rtype: str
        """
        return self._certificate_secret_id

    @certificate_secret_id.setter
    def certificate_secret_id(self, certificate_secret_id):
        """
        Sets the certificate_secret_id of this UpdateCustomEndpointDetails.
        Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
        All certificates should be stored in a single base64 encoded secret.
        Note the update will fail if this is not a valid certificate.


        :param certificate_secret_id: The certificate_secret_id of this UpdateCustomEndpointDetails.
        :type: str
        """
        self._certificate_secret_id = certificate_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
