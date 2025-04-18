# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201210


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverNodeRenewCertificateDetails(object):
    """
    The information required to renew a certificate for a roverNode.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RoverNodeRenewCertificateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param csr:
            The value to assign to the csr property of this RoverNodeRenewCertificateDetails.
        :type csr: str

        :param time_cert_validity_end:
            The value to assign to the time_cert_validity_end property of this RoverNodeRenewCertificateDetails.
        :type time_cert_validity_end: datetime

        """
        self.swagger_types = {
            'csr': 'str',
            'time_cert_validity_end': 'datetime'
        }
        self.attribute_map = {
            'csr': 'csr',
            'time_cert_validity_end': 'timeCertValidityEnd'
        }
        self._csr = None
        self._time_cert_validity_end = None

    @property
    def csr(self):
        """
        **[Required]** Gets the csr of this RoverNodeRenewCertificateDetails.
        The certificate signing request (in PEM format), max size 10240.


        :return: The csr of this RoverNodeRenewCertificateDetails.
        :rtype: str
        """
        return self._csr

    @csr.setter
    def csr(self, csr):
        """
        Sets the csr of this RoverNodeRenewCertificateDetails.
        The certificate signing request (in PEM format), max size 10240.


        :param csr: The csr of this RoverNodeRenewCertificateDetails.
        :type: str
        """
        self._csr = csr

    @property
    def time_cert_validity_end(self):
        """
        **[Required]** Gets the time_cert_validity_end of this RoverNodeRenewCertificateDetails.
        Time when the renewed certificate's validity will end.


        :return: The time_cert_validity_end of this RoverNodeRenewCertificateDetails.
        :rtype: datetime
        """
        return self._time_cert_validity_end

    @time_cert_validity_end.setter
    def time_cert_validity_end(self, time_cert_validity_end):
        """
        Sets the time_cert_validity_end of this RoverNodeRenewCertificateDetails.
        Time when the renewed certificate's validity will end.


        :param time_cert_validity_end: The time_cert_validity_end of this RoverNodeRenewCertificateDetails.
        :type: datetime
        """
        self._time_cert_validity_end = time_cert_validity_end

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
