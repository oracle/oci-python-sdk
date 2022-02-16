# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DefaultPhaseOneParameters(object):
    """
    Default phase one parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DefaultPhaseOneParameters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param default_encryption_algorithms:
            The value to assign to the default_encryption_algorithms property of this DefaultPhaseOneParameters.
        :type default_encryption_algorithms: list[str]

        :param default_authentication_algorithms:
            The value to assign to the default_authentication_algorithms property of this DefaultPhaseOneParameters.
        :type default_authentication_algorithms: list[str]

        :param default_dh_groups:
            The value to assign to the default_dh_groups property of this DefaultPhaseOneParameters.
        :type default_dh_groups: list[str]

        """
        self.swagger_types = {
            'default_encryption_algorithms': 'list[str]',
            'default_authentication_algorithms': 'list[str]',
            'default_dh_groups': 'list[str]'
        }

        self.attribute_map = {
            'default_encryption_algorithms': 'defaultEncryptionAlgorithms',
            'default_authentication_algorithms': 'defaultAuthenticationAlgorithms',
            'default_dh_groups': 'defaultDhGroups'
        }

        self._default_encryption_algorithms = None
        self._default_authentication_algorithms = None
        self._default_dh_groups = None

    @property
    def default_encryption_algorithms(self):
        """
        Gets the default_encryption_algorithms of this DefaultPhaseOneParameters.
        Default phase one encryption algorithms.


        :return: The default_encryption_algorithms of this DefaultPhaseOneParameters.
        :rtype: list[str]
        """
        return self._default_encryption_algorithms

    @default_encryption_algorithms.setter
    def default_encryption_algorithms(self, default_encryption_algorithms):
        """
        Sets the default_encryption_algorithms of this DefaultPhaseOneParameters.
        Default phase one encryption algorithms.


        :param default_encryption_algorithms: The default_encryption_algorithms of this DefaultPhaseOneParameters.
        :type: list[str]
        """
        self._default_encryption_algorithms = default_encryption_algorithms

    @property
    def default_authentication_algorithms(self):
        """
        Gets the default_authentication_algorithms of this DefaultPhaseOneParameters.
        Default phase one authentication algorithms.


        :return: The default_authentication_algorithms of this DefaultPhaseOneParameters.
        :rtype: list[str]
        """
        return self._default_authentication_algorithms

    @default_authentication_algorithms.setter
    def default_authentication_algorithms(self, default_authentication_algorithms):
        """
        Sets the default_authentication_algorithms of this DefaultPhaseOneParameters.
        Default phase one authentication algorithms.


        :param default_authentication_algorithms: The default_authentication_algorithms of this DefaultPhaseOneParameters.
        :type: list[str]
        """
        self._default_authentication_algorithms = default_authentication_algorithms

    @property
    def default_dh_groups(self):
        """
        Gets the default_dh_groups of this DefaultPhaseOneParameters.
        Default phase one Diffie-Hellman groups.


        :return: The default_dh_groups of this DefaultPhaseOneParameters.
        :rtype: list[str]
        """
        return self._default_dh_groups

    @default_dh_groups.setter
    def default_dh_groups(self, default_dh_groups):
        """
        Sets the default_dh_groups of this DefaultPhaseOneParameters.
        Default phase one Diffie-Hellman groups.


        :param default_dh_groups: The default_dh_groups of this DefaultPhaseOneParameters.
        :type: list[str]
        """
        self._default_dh_groups = default_dh_groups

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
