# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateDetails(object):
    """
    The details of Oracle Cloud Infrastructure certificate created
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_id:
            The value to assign to the certificate_id property of this CertificateDetails.
        :type certificate_id: str

        :param certificate_name:
            The value to assign to the certificate_name property of this CertificateDetails.
        :type certificate_name: str

        """
        self.swagger_types = {
            'certificate_id': 'str',
            'certificate_name': 'str'
        }

        self.attribute_map = {
            'certificate_id': 'certificateId',
            'certificate_name': 'certificateName'
        }

        self._certificate_id = None
        self._certificate_name = None

    @property
    def certificate_id(self):
        """
        Gets the certificate_id of this CertificateDetails.
        The id of the certificate.


        :return: The certificate_id of this CertificateDetails.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this CertificateDetails.
        The id of the certificate.


        :param certificate_id: The certificate_id of this CertificateDetails.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def certificate_name(self):
        """
        Gets the certificate_name of this CertificateDetails.
        The name of the certificate.


        :return: The certificate_name of this CertificateDetails.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """
        Sets the certificate_name of this CertificateDetails.
        The name of the certificate.


        :param certificate_name: The certificate_name of this CertificateDetails.
        :type: str
        """
        self._certificate_name = certificate_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other