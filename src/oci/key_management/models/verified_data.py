# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VerifiedData(object):
    """
    VerifiedData model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VerifiedData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_signature_valid:
            The value to assign to the is_signature_valid property of this VerifiedData.
        :type is_signature_valid: bool

        """
        self.swagger_types = {
            'is_signature_valid': 'bool'
        }

        self.attribute_map = {
            'is_signature_valid': 'isSignatureValid'
        }

        self._is_signature_valid = None

    @property
    def is_signature_valid(self):
        """
        **[Required]** Gets the is_signature_valid of this VerifiedData.
        A Boolean value that indicates whether the signature was verified.


        :return: The is_signature_valid of this VerifiedData.
        :rtype: bool
        """
        return self._is_signature_valid

    @is_signature_valid.setter
    def is_signature_valid(self, is_signature_valid):
        """
        Sets the is_signature_valid of this VerifiedData.
        A Boolean value that indicates whether the signature was verified.


        :param is_signature_valid: The is_signature_valid of this VerifiedData.
        :type: bool
        """
        self._is_signature_valid = is_signature_valid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
