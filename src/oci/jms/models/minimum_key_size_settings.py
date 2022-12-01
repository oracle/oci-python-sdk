# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MinimumKeySizeSettings(object):
    """
    test
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MinimumKeySizeSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tls:
            The value to assign to the tls property of this MinimumKeySizeSettings.
        :type tls: list[oci.jms.models.KeySizeAlgorithm]

        :param jar:
            The value to assign to the jar property of this MinimumKeySizeSettings.
        :type jar: list[oci.jms.models.KeySizeAlgorithm]

        :param certpath:
            The value to assign to the certpath property of this MinimumKeySizeSettings.
        :type certpath: list[oci.jms.models.KeySizeAlgorithm]

        """
        self.swagger_types = {
            'tls': 'list[KeySizeAlgorithm]',
            'jar': 'list[KeySizeAlgorithm]',
            'certpath': 'list[KeySizeAlgorithm]'
        }

        self.attribute_map = {
            'tls': 'tls',
            'jar': 'jar',
            'certpath': 'certpath'
        }

        self._tls = None
        self._jar = None
        self._certpath = None

    @property
    def tls(self):
        """
        Gets the tls of this MinimumKeySizeSettings.
        Updates the minimum key size for the specified encryption algorithm.
        The JDK property jdk.tls.disabledAlgorithms will be updated with the following supported actions:
        - Changing minimum key length for Diffie-Hellman


        :return: The tls of this MinimumKeySizeSettings.
        :rtype: list[oci.jms.models.KeySizeAlgorithm]
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """
        Sets the tls of this MinimumKeySizeSettings.
        Updates the minimum key size for the specified encryption algorithm.
        The JDK property jdk.tls.disabledAlgorithms will be updated with the following supported actions:
        - Changing minimum key length for Diffie-Hellman


        :param tls: The tls of this MinimumKeySizeSettings.
        :type: list[oci.jms.models.KeySizeAlgorithm]
        """
        self._tls = tls

    @property
    def jar(self):
        """
        Gets the jar of this MinimumKeySizeSettings.
        Updates the minimum key size for the specified encryption algorithm.
        The JDK property jdk.jar.disabledAlgorithms will be updated with the following supported actions:
        - Changing minimum key length for RSA signed jars
        - Changing minimum key length for EC
        - Changing minimum key length for DSA


        :return: The jar of this MinimumKeySizeSettings.
        :rtype: list[oci.jms.models.KeySizeAlgorithm]
        """
        return self._jar

    @jar.setter
    def jar(self, jar):
        """
        Sets the jar of this MinimumKeySizeSettings.
        Updates the minimum key size for the specified encryption algorithm.
        The JDK property jdk.jar.disabledAlgorithms will be updated with the following supported actions:
        - Changing minimum key length for RSA signed jars
        - Changing minimum key length for EC
        - Changing minimum key length for DSA


        :param jar: The jar of this MinimumKeySizeSettings.
        :type: list[oci.jms.models.KeySizeAlgorithm]
        """
        self._jar = jar

    @property
    def certpath(self):
        """
        Gets the certpath of this MinimumKeySizeSettings.
        Updates the minimum key size for the specified encryption algorithm.
        The JDK property jdk.certpath.disabledAlgorithms will be updated with the following supported actions:
        - Changing minimum key length for RSA signed jars
        - Changing minimum key length for EC
        - Changing minimum key length for DSA


        :return: The certpath of this MinimumKeySizeSettings.
        :rtype: list[oci.jms.models.KeySizeAlgorithm]
        """
        return self._certpath

    @certpath.setter
    def certpath(self, certpath):
        """
        Sets the certpath of this MinimumKeySizeSettings.
        Updates the minimum key size for the specified encryption algorithm.
        The JDK property jdk.certpath.disabledAlgorithms will be updated with the following supported actions:
        - Changing minimum key length for RSA signed jars
        - Changing minimum key length for EC
        - Changing minimum key length for DSA


        :param certpath: The certpath of this MinimumKeySizeSettings.
        :type: list[oci.jms.models.KeySizeAlgorithm]
        """
        self._certpath = certpath

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
