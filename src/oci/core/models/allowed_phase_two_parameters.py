# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AllowedPhaseTwoParameters(object):
    """
    Allowed phase two parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AllowedPhaseTwoParameters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param encryption_algorithms:
            The value to assign to the encryption_algorithms property of this AllowedPhaseTwoParameters.
        :type encryption_algorithms: list[str]

        :param authentication_algorithms:
            The value to assign to the authentication_algorithms property of this AllowedPhaseTwoParameters.
        :type authentication_algorithms: list[str]

        :param pfs_dh_groups:
            The value to assign to the pfs_dh_groups property of this AllowedPhaseTwoParameters.
        :type pfs_dh_groups: list[str]

        """
        self.swagger_types = {
            'encryption_algorithms': 'list[str]',
            'authentication_algorithms': 'list[str]',
            'pfs_dh_groups': 'list[str]'
        }

        self.attribute_map = {
            'encryption_algorithms': 'encryptionAlgorithms',
            'authentication_algorithms': 'authenticationAlgorithms',
            'pfs_dh_groups': 'pfsDhGroups'
        }

        self._encryption_algorithms = None
        self._authentication_algorithms = None
        self._pfs_dh_groups = None

    @property
    def encryption_algorithms(self):
        """
        Gets the encryption_algorithms of this AllowedPhaseTwoParameters.
        Allowed phase two encryption algorithms.


        :return: The encryption_algorithms of this AllowedPhaseTwoParameters.
        :rtype: list[str]
        """
        return self._encryption_algorithms

    @encryption_algorithms.setter
    def encryption_algorithms(self, encryption_algorithms):
        """
        Sets the encryption_algorithms of this AllowedPhaseTwoParameters.
        Allowed phase two encryption algorithms.


        :param encryption_algorithms: The encryption_algorithms of this AllowedPhaseTwoParameters.
        :type: list[str]
        """
        self._encryption_algorithms = encryption_algorithms

    @property
    def authentication_algorithms(self):
        """
        Gets the authentication_algorithms of this AllowedPhaseTwoParameters.
        Allowed phase two authentication algorithms.


        :return: The authentication_algorithms of this AllowedPhaseTwoParameters.
        :rtype: list[str]
        """
        return self._authentication_algorithms

    @authentication_algorithms.setter
    def authentication_algorithms(self, authentication_algorithms):
        """
        Sets the authentication_algorithms of this AllowedPhaseTwoParameters.
        Allowed phase two authentication algorithms.


        :param authentication_algorithms: The authentication_algorithms of this AllowedPhaseTwoParameters.
        :type: list[str]
        """
        self._authentication_algorithms = authentication_algorithms

    @property
    def pfs_dh_groups(self):
        """
        Gets the pfs_dh_groups of this AllowedPhaseTwoParameters.
        Allowed perfect forward secrecy Diffie-Hellman groups.


        :return: The pfs_dh_groups of this AllowedPhaseTwoParameters.
        :rtype: list[str]
        """
        return self._pfs_dh_groups

    @pfs_dh_groups.setter
    def pfs_dh_groups(self, pfs_dh_groups):
        """
        Sets the pfs_dh_groups of this AllowedPhaseTwoParameters.
        Allowed perfect forward secrecy Diffie-Hellman groups.


        :param pfs_dh_groups: The pfs_dh_groups of this AllowedPhaseTwoParameters.
        :type: list[str]
        """
        self._pfs_dh_groups = pfs_dh_groups

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
