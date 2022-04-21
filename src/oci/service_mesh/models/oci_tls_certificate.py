# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .tls_certificate import TlsCertificate
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OciTlsCertificate(TlsCertificate):
    """
    TLS certificate from OCI Certificates service.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OciTlsCertificate object with values from keyword arguments. The default value of the :py:attr:`~oci.service_mesh.models.OciTlsCertificate.type` attribute
        of this class is ``OCI_CERTIFICATES`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this OciTlsCertificate.
            Allowed values for this property are: "OCI_CERTIFICATES", "LOCAL_FILE"
        :type type: str

        :param certificate_id:
            The value to assign to the certificate_id property of this OciTlsCertificate.
        :type certificate_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'certificate_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'certificate_id': 'certificateId'
        }

        self._type = None
        self._certificate_id = None
        self._type = 'OCI_CERTIFICATES'

    @property
    def certificate_id(self):
        """
        Gets the certificate_id of this OciTlsCertificate.
        The OCID of the leaf certificate resource.


        :return: The certificate_id of this OciTlsCertificate.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this OciTlsCertificate.
        The OCID of the leaf certificate resource.


        :param certificate_id: The certificate_id of this OciTlsCertificate.
        :type: str
        """
        self._certificate_id = certificate_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
