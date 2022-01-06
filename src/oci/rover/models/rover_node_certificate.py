# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverNodeCertificate(object):
    """
    The certificate response
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RoverNodeCertificate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate:
            The value to assign to the certificate property of this RoverNodeCertificate.
        :type certificate: str

        """
        self.swagger_types = {
            'certificate': 'str'
        }

        self.attribute_map = {
            'certificate': 'certificate'
        }

        self._certificate = None

    @property
    def certificate(self):
        """
        **[Required]** Gets the certificate of this RoverNodeCertificate.
        The certificate that can be installed on a client to do TLS communication to the node


        :return: The certificate of this RoverNodeCertificate.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this RoverNodeCertificate.
        The certificate that can be installed on a client to do TLS communication to the node


        :param certificate: The certificate of this RoverNodeCertificate.
        :type: str
        """
        self._certificate = certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
