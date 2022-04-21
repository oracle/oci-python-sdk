# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngressListenerClientValidationConfig(object):
    """
    Resource representing the TLS configuration used for validating client certificates.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IngressListenerClientValidationConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param trusted_ca_bundle:
            The value to assign to the trusted_ca_bundle property of this IngressListenerClientValidationConfig.
        :type trusted_ca_bundle: oci.service_mesh.models.CaBundle

        :param subject_alternate_names:
            The value to assign to the subject_alternate_names property of this IngressListenerClientValidationConfig.
        :type subject_alternate_names: list[str]

        """
        self.swagger_types = {
            'trusted_ca_bundle': 'CaBundle',
            'subject_alternate_names': 'list[str]'
        }

        self.attribute_map = {
            'trusted_ca_bundle': 'trustedCaBundle',
            'subject_alternate_names': 'subjectAlternateNames'
        }

        self._trusted_ca_bundle = None
        self._subject_alternate_names = None

    @property
    def trusted_ca_bundle(self):
        """
        Gets the trusted_ca_bundle of this IngressListenerClientValidationConfig.

        :return: The trusted_ca_bundle of this IngressListenerClientValidationConfig.
        :rtype: oci.service_mesh.models.CaBundle
        """
        return self._trusted_ca_bundle

    @trusted_ca_bundle.setter
    def trusted_ca_bundle(self, trusted_ca_bundle):
        """
        Sets the trusted_ca_bundle of this IngressListenerClientValidationConfig.

        :param trusted_ca_bundle: The trusted_ca_bundle of this IngressListenerClientValidationConfig.
        :type: oci.service_mesh.models.CaBundle
        """
        self._trusted_ca_bundle = trusted_ca_bundle

    @property
    def subject_alternate_names(self):
        """
        Gets the subject_alternate_names of this IngressListenerClientValidationConfig.
        A list of alternate names to verify the subject identity in the certificate presented by the client.


        :return: The subject_alternate_names of this IngressListenerClientValidationConfig.
        :rtype: list[str]
        """
        return self._subject_alternate_names

    @subject_alternate_names.setter
    def subject_alternate_names(self, subject_alternate_names):
        """
        Sets the subject_alternate_names of this IngressListenerClientValidationConfig.
        A list of alternate names to verify the subject identity in the certificate presented by the client.


        :param subject_alternate_names: The subject_alternate_names of this IngressListenerClientValidationConfig.
        :type: list[str]
        """
        self._subject_alternate_names = subject_alternate_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
