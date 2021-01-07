# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .ca_certificate import CaCertificate
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PemCaCertificate(CaCertificate):
    """
    The CA certificate in PEM format.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PemCaCertificate object with values from keyword arguments. The default value of the :py:attr:`~oci.mysql.models.PemCaCertificate.certificate_type` attribute
        of this class is ``PEM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_type:
            The value to assign to the certificate_type property of this PemCaCertificate.
            Allowed values for this property are: "PEM"
        :type certificate_type: str

        :param contents:
            The value to assign to the contents property of this PemCaCertificate.
        :type contents: str

        """
        self.swagger_types = {
            'certificate_type': 'str',
            'contents': 'str'
        }

        self.attribute_map = {
            'certificate_type': 'certificateType',
            'contents': 'contents'
        }

        self._certificate_type = None
        self._contents = None
        self._certificate_type = 'PEM'

    @property
    def contents(self):
        """
        **[Required]** Gets the contents of this PemCaCertificate.
        The string containing the CA certificate in PEM format.


        :return: The contents of this PemCaCertificate.
        :rtype: str
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """
        Sets the contents of this PemCaCertificate.
        The string containing the CA certificate in PEM format.


        :param contents: The contents of this PemCaCertificate.
        :type: str
        """
        self._contents = contents

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
