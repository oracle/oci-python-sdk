# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConsoleConnectionDetails(object):
    """
    The details for creating a Db node console connection.
    The Db node console connection is created in the same compartment as the dbNode.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConsoleConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param public_key:
            The value to assign to the public_key property of this CreateConsoleConnectionDetails.
        :type public_key: str

        """
        self.swagger_types = {
            'public_key': 'str'
        }

        self.attribute_map = {
            'public_key': 'publicKey'
        }

        self._public_key = None

    @property
    def public_key(self):
        """
        **[Required]** Gets the public_key of this CreateConsoleConnectionDetails.
        The SSH public key used to authenticate the console connection.


        :return: The public_key of this CreateConsoleConnectionDetails.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this CreateConsoleConnectionDetails.
        The SSH public key used to authenticate the console connection.


        :param public_key: The public_key of this CreateConsoleConnectionDetails.
        :type: str
        """
        self._public_key = public_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
