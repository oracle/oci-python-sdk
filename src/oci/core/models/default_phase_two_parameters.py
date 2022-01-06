# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DefaultPhaseTwoParameters(object):
    """
    Phase Two Parameters
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DefaultPhaseTwoParameters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param default_encryption_algorithms:
            The value to assign to the default_encryption_algorithms property of this DefaultPhaseTwoParameters.
        :type default_encryption_algorithms: list[str]

        :param default_authentication_algorithms:
            The value to assign to the default_authentication_algorithms property of this DefaultPhaseTwoParameters.
        :type default_authentication_algorithms: list[str]

        :param default_pfs_dh_group:
            The value to assign to the default_pfs_dh_group property of this DefaultPhaseTwoParameters.
        :type default_pfs_dh_group: str

        """
        self.swagger_types = {
            'default_encryption_algorithms': 'list[str]',
            'default_authentication_algorithms': 'list[str]',
            'default_pfs_dh_group': 'str'
        }

        self.attribute_map = {
            'default_encryption_algorithms': 'defaultEncryptionAlgorithms',
            'default_authentication_algorithms': 'defaultAuthenticationAlgorithms',
            'default_pfs_dh_group': 'defaultPfsDhGroup'
        }

        self._default_encryption_algorithms = None
        self._default_authentication_algorithms = None
        self._default_pfs_dh_group = None

    @property
    def default_encryption_algorithms(self):
        """
        Gets the default_encryption_algorithms of this DefaultPhaseTwoParameters.
        Default Phase Two Encryption Algorithms


        :return: The default_encryption_algorithms of this DefaultPhaseTwoParameters.
        :rtype: list[str]
        """
        return self._default_encryption_algorithms

    @default_encryption_algorithms.setter
    def default_encryption_algorithms(self, default_encryption_algorithms):
        """
        Sets the default_encryption_algorithms of this DefaultPhaseTwoParameters.
        Default Phase Two Encryption Algorithms


        :param default_encryption_algorithms: The default_encryption_algorithms of this DefaultPhaseTwoParameters.
        :type: list[str]
        """
        self._default_encryption_algorithms = default_encryption_algorithms

    @property
    def default_authentication_algorithms(self):
        """
        Gets the default_authentication_algorithms of this DefaultPhaseTwoParameters.
        Default Phase Two Authentication Algorithms


        :return: The default_authentication_algorithms of this DefaultPhaseTwoParameters.
        :rtype: list[str]
        """
        return self._default_authentication_algorithms

    @default_authentication_algorithms.setter
    def default_authentication_algorithms(self, default_authentication_algorithms):
        """
        Sets the default_authentication_algorithms of this DefaultPhaseTwoParameters.
        Default Phase Two Authentication Algorithms


        :param default_authentication_algorithms: The default_authentication_algorithms of this DefaultPhaseTwoParameters.
        :type: list[str]
        """
        self._default_authentication_algorithms = default_authentication_algorithms

    @property
    def default_pfs_dh_group(self):
        """
        Gets the default_pfs_dh_group of this DefaultPhaseTwoParameters.
        Default PFS DH Group


        :return: The default_pfs_dh_group of this DefaultPhaseTwoParameters.
        :rtype: str
        """
        return self._default_pfs_dh_group

    @default_pfs_dh_group.setter
    def default_pfs_dh_group(self, default_pfs_dh_group):
        """
        Sets the default_pfs_dh_group of this DefaultPhaseTwoParameters.
        Default PFS DH Group


        :param default_pfs_dh_group: The default_pfs_dh_group of this DefaultPhaseTwoParameters.
        :type: str
        """
        self._default_pfs_dh_group = default_pfs_dh_group

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
