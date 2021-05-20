# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublicKeyDetails(object):
    """
    Public key details for a bastion session.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PublicKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param public_key_content:
            The value to assign to the public_key_content property of this PublicKeyDetails.
        :type public_key_content: str

        """
        self.swagger_types = {
            'public_key_content': 'str'
        }

        self.attribute_map = {
            'public_key_content': 'publicKeyContent'
        }

        self._public_key_content = None

    @property
    def public_key_content(self):
        """
        **[Required]** Gets the public_key_content of this PublicKeyDetails.
        The public key in OpenSSH format of the SSH key pair for the session. When you connect to the session, you must provide the private key of the same SSH key pair.


        :return: The public_key_content of this PublicKeyDetails.
        :rtype: str
        """
        return self._public_key_content

    @public_key_content.setter
    def public_key_content(self, public_key_content):
        """
        Sets the public_key_content of this PublicKeyDetails.
        The public key in OpenSSH format of the SSH key pair for the session. When you connect to the session, you must provide the private key of the same SSH key pair.


        :param public_key_content: The public_key_content of this PublicKeyDetails.
        :type: str
        """
        self._public_key_content = public_key_content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
