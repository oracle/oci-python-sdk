# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CaCertificate(object):
    """
    The CA certificate of the server used for VERIFY_IDENTITY and VERIFY_CA ssl modes.
    """

    #: A constant which can be used with the certificate_type property of a CaCertificate.
    #: This constant has a value of "PEM"
    CERTIFICATE_TYPE_PEM = "PEM"

    def __init__(self, **kwargs):
        """
        Initializes a new CaCertificate object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.mysql.models.PemCaCertificate`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_type:
            The value to assign to the certificate_type property of this CaCertificate.
            Allowed values for this property are: "PEM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type certificate_type: str

        """
        self.swagger_types = {
            'certificate_type': 'str'
        }

        self.attribute_map = {
            'certificate_type': 'certificateType'
        }

        self._certificate_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['certificateType']

        if type == 'PEM':
            return 'PemCaCertificate'
        else:
            return 'CaCertificate'

    @property
    def certificate_type(self):
        """
        **[Required]** Gets the certificate_type of this CaCertificate.
        The type of CA certificate.

        Allowed values for this property are: "PEM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The certificate_type of this CaCertificate.
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """
        Sets the certificate_type of this CaCertificate.
        The type of CA certificate.


        :param certificate_type: The certificate_type of this CaCertificate.
        :type: str
        """
        allowed_values = ["PEM"]
        if not value_allowed_none_or_none_sentinel(certificate_type, allowed_values):
            certificate_type = 'UNKNOWN_ENUM_VALUE'
        self._certificate_type = certificate_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
