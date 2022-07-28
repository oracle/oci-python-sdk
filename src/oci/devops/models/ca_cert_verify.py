# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .tls_verify_config import TlsVerifyConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CaCertVerify(TlsVerifyConfig):
    """
    Enable TLS verification with CA certificate.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CaCertVerify object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CaCertVerify.tls_verify_mode` attribute
        of this class is ``CA_CERTIFICATE_VERIFY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tls_verify_mode:
            The value to assign to the tls_verify_mode property of this CaCertVerify.
            Allowed values for this property are: "CA_CERTIFICATE_VERIFY"
        :type tls_verify_mode: str

        :param ca_certificate_bundle_id:
            The value to assign to the ca_certificate_bundle_id property of this CaCertVerify.
        :type ca_certificate_bundle_id: str

        """
        self.swagger_types = {
            'tls_verify_mode': 'str',
            'ca_certificate_bundle_id': 'str'
        }

        self.attribute_map = {
            'tls_verify_mode': 'tlsVerifyMode',
            'ca_certificate_bundle_id': 'caCertificateBundleId'
        }

        self._tls_verify_mode = None
        self._ca_certificate_bundle_id = None
        self._tls_verify_mode = 'CA_CERTIFICATE_VERIFY'

    @property
    def ca_certificate_bundle_id(self):
        """
        **[Required]** Gets the ca_certificate_bundle_id of this CaCertVerify.
        The OCID of OCI certificate service CA bundle.


        :return: The ca_certificate_bundle_id of this CaCertVerify.
        :rtype: str
        """
        return self._ca_certificate_bundle_id

    @ca_certificate_bundle_id.setter
    def ca_certificate_bundle_id(self, ca_certificate_bundle_id):
        """
        Sets the ca_certificate_bundle_id of this CaCertVerify.
        The OCID of OCI certificate service CA bundle.


        :param ca_certificate_bundle_id: The ca_certificate_bundle_id of this CaCertVerify.
        :type: str
        """
        self._ca_certificate_bundle_id = ca_certificate_bundle_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
