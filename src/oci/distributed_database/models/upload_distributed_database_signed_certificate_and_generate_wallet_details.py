# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UploadDistributedDatabaseSignedCertificateAndGenerateWalletDetails(object):
    """
    Details of the request to upload the CA signed certificates to GSMs and generate wallets for
    GSMs of the Globally distributed database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UploadDistributedDatabaseSignedCertificateAndGenerateWalletDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ca_signed_certificate:
            The value to assign to the ca_signed_certificate property of this UploadDistributedDatabaseSignedCertificateAndGenerateWalletDetails.
        :type ca_signed_certificate: str

        """
        self.swagger_types = {
            'ca_signed_certificate': 'str'
        }
        self.attribute_map = {
            'ca_signed_certificate': 'caSignedCertificate'
        }
        self._ca_signed_certificate = None

    @property
    def ca_signed_certificate(self):
        """
        **[Required]** Gets the ca_signed_certificate of this UploadDistributedDatabaseSignedCertificateAndGenerateWalletDetails.
        The CA signed certificate key.


        :return: The ca_signed_certificate of this UploadDistributedDatabaseSignedCertificateAndGenerateWalletDetails.
        :rtype: str
        """
        return self._ca_signed_certificate

    @ca_signed_certificate.setter
    def ca_signed_certificate(self, ca_signed_certificate):
        """
        Sets the ca_signed_certificate of this UploadDistributedDatabaseSignedCertificateAndGenerateWalletDetails.
        The CA signed certificate key.


        :param ca_signed_certificate: The ca_signed_certificate of this UploadDistributedDatabaseSignedCertificateAndGenerateWalletDetails.
        :type: str
        """
        self._ca_signed_certificate = ca_signed_certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
