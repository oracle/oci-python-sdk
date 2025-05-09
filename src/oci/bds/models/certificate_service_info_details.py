# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateServiceInfoDetails(object):
    """
    Details for certificate service info
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateServiceInfoDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param services:
            The value to assign to the services property of this CertificateServiceInfoDetails.
        :type services: list[oci.bds.models.Service]

        """
        self.swagger_types = {
            'services': 'list[Service]'
        }
        self.attribute_map = {
            'services': 'services'
        }
        self._services = None

    @property
    def services(self):
        """
        **[Required]** Gets the services of this CertificateServiceInfoDetails.
        List of services for which TLS/SSL needs to be enabled.


        :return: The services of this CertificateServiceInfoDetails.
        :rtype: list[oci.bds.models.Service]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this CertificateServiceInfoDetails.
        List of services for which TLS/SSL needs to be enabled.


        :param services: The services of this CertificateServiceInfoDetails.
        :type: list[oci.bds.models.Service]
        """
        self._services = services

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
