# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PhaseTwoConfigDetails(object):
    """
    Configuration details for IPSec phase two configuration parameters.
    """

    #: A constant which can be used with the authentication_algorithm property of a PhaseTwoConfigDetails.
    #: This constant has a value of "HMAC_SHA2_256_128"
    AUTHENTICATION_ALGORITHM_HMAC_SHA2_256_128 = "HMAC_SHA2_256_128"

    #: A constant which can be used with the authentication_algorithm property of a PhaseTwoConfigDetails.
    #: This constant has a value of "HMAC_SHA1_128"
    AUTHENTICATION_ALGORITHM_HMAC_SHA1_128 = "HMAC_SHA1_128"

    #: A constant which can be used with the encryption_algorithm property of a PhaseTwoConfigDetails.
    #: This constant has a value of "AES_256_GCM"
    ENCRYPTION_ALGORITHM_AES_256_GCM = "AES_256_GCM"

    #: A constant which can be used with the encryption_algorithm property of a PhaseTwoConfigDetails.
    #: This constant has a value of "AES_192_GCM"
    ENCRYPTION_ALGORITHM_AES_192_GCM = "AES_192_GCM"

    #: A constant which can be used with the encryption_algorithm property of a PhaseTwoConfigDetails.
    #: This constant has a value of "AES_128_GCM"
    ENCRYPTION_ALGORITHM_AES_128_GCM = "AES_128_GCM"

    #: A constant which can be used with the encryption_algorithm property of a PhaseTwoConfigDetails.
    #: This constant has a value of "AES_256_CBC"
    ENCRYPTION_ALGORITHM_AES_256_CBC = "AES_256_CBC"

    #: A constant which can be used with the encryption_algorithm property of a PhaseTwoConfigDetails.
    #: This constant has a value of "AES_192_CBC"
    ENCRYPTION_ALGORITHM_AES_192_CBC = "AES_192_CBC"

    #: A constant which can be used with the encryption_algorithm property of a PhaseTwoConfigDetails.
    #: This constant has a value of "AES_128_CBC"
    ENCRYPTION_ALGORITHM_AES_128_CBC = "AES_128_CBC"

    #: A constant which can be used with the pfs_dh_group property of a PhaseTwoConfigDetails.
    #: This constant has a value of "GROUP2"
    PFS_DH_GROUP_GROUP2 = "GROUP2"

    #: A constant which can be used with the pfs_dh_group property of a PhaseTwoConfigDetails.
    #: This constant has a value of "GROUP5"
    PFS_DH_GROUP_GROUP5 = "GROUP5"

    #: A constant which can be used with the pfs_dh_group property of a PhaseTwoConfigDetails.
    #: This constant has a value of "GROUP14"
    PFS_DH_GROUP_GROUP14 = "GROUP14"

    #: A constant which can be used with the pfs_dh_group property of a PhaseTwoConfigDetails.
    #: This constant has a value of "GROUP19"
    PFS_DH_GROUP_GROUP19 = "GROUP19"

    #: A constant which can be used with the pfs_dh_group property of a PhaseTwoConfigDetails.
    #: This constant has a value of "GROUP20"
    PFS_DH_GROUP_GROUP20 = "GROUP20"

    #: A constant which can be used with the pfs_dh_group property of a PhaseTwoConfigDetails.
    #: This constant has a value of "GROUP24"
    PFS_DH_GROUP_GROUP24 = "GROUP24"

    def __init__(self, **kwargs):
        """
        Initializes a new PhaseTwoConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_custom_phase_two_config:
            The value to assign to the is_custom_phase_two_config property of this PhaseTwoConfigDetails.
        :type is_custom_phase_two_config: bool

        :param authentication_algorithm:
            The value to assign to the authentication_algorithm property of this PhaseTwoConfigDetails.
            Allowed values for this property are: "HMAC_SHA2_256_128", "HMAC_SHA1_128"
        :type authentication_algorithm: str

        :param encryption_algorithm:
            The value to assign to the encryption_algorithm property of this PhaseTwoConfigDetails.
            Allowed values for this property are: "AES_256_GCM", "AES_192_GCM", "AES_128_GCM", "AES_256_CBC", "AES_192_CBC", "AES_128_CBC"
        :type encryption_algorithm: str

        :param lifetime_in_seconds:
            The value to assign to the lifetime_in_seconds property of this PhaseTwoConfigDetails.
        :type lifetime_in_seconds: int

        :param is_pfs_enabled:
            The value to assign to the is_pfs_enabled property of this PhaseTwoConfigDetails.
        :type is_pfs_enabled: bool

        :param pfs_dh_group:
            The value to assign to the pfs_dh_group property of this PhaseTwoConfigDetails.
            Allowed values for this property are: "GROUP2", "GROUP5", "GROUP14", "GROUP19", "GROUP20", "GROUP24"
        :type pfs_dh_group: str

        """
        self.swagger_types = {
            'is_custom_phase_two_config': 'bool',
            'authentication_algorithm': 'str',
            'encryption_algorithm': 'str',
            'lifetime_in_seconds': 'int',
            'is_pfs_enabled': 'bool',
            'pfs_dh_group': 'str'
        }

        self.attribute_map = {
            'is_custom_phase_two_config': 'isCustomPhaseTwoConfig',
            'authentication_algorithm': 'authenticationAlgorithm',
            'encryption_algorithm': 'encryptionAlgorithm',
            'lifetime_in_seconds': 'lifetimeInSeconds',
            'is_pfs_enabled': 'isPfsEnabled',
            'pfs_dh_group': 'pfsDhGroup'
        }

        self._is_custom_phase_two_config = None
        self._authentication_algorithm = None
        self._encryption_algorithm = None
        self._lifetime_in_seconds = None
        self._is_pfs_enabled = None
        self._pfs_dh_group = None

    @property
    def is_custom_phase_two_config(self):
        """
        Gets the is_custom_phase_two_config of this PhaseTwoConfigDetails.
        Indicates whether custom configuration is enabled for phase two options.


        :return: The is_custom_phase_two_config of this PhaseTwoConfigDetails.
        :rtype: bool
        """
        return self._is_custom_phase_two_config

    @is_custom_phase_two_config.setter
    def is_custom_phase_two_config(self, is_custom_phase_two_config):
        """
        Sets the is_custom_phase_two_config of this PhaseTwoConfigDetails.
        Indicates whether custom configuration is enabled for phase two options.


        :param is_custom_phase_two_config: The is_custom_phase_two_config of this PhaseTwoConfigDetails.
        :type: bool
        """
        self._is_custom_phase_two_config = is_custom_phase_two_config

    @property
    def authentication_algorithm(self):
        """
        Gets the authentication_algorithm of this PhaseTwoConfigDetails.
        The authentication algorithm proposed during phase two tunnel negotiation.

        Allowed values for this property are: "HMAC_SHA2_256_128", "HMAC_SHA1_128"


        :return: The authentication_algorithm of this PhaseTwoConfigDetails.
        :rtype: str
        """
        return self._authentication_algorithm

    @authentication_algorithm.setter
    def authentication_algorithm(self, authentication_algorithm):
        """
        Sets the authentication_algorithm of this PhaseTwoConfigDetails.
        The authentication algorithm proposed during phase two tunnel negotiation.


        :param authentication_algorithm: The authentication_algorithm of this PhaseTwoConfigDetails.
        :type: str
        """
        allowed_values = ["HMAC_SHA2_256_128", "HMAC_SHA1_128"]
        if not value_allowed_none_or_none_sentinel(authentication_algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `authentication_algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._authentication_algorithm = authentication_algorithm

    @property
    def encryption_algorithm(self):
        """
        Gets the encryption_algorithm of this PhaseTwoConfigDetails.
        The encryption algorithm proposed during phase two tunnel negotiation.

        Allowed values for this property are: "AES_256_GCM", "AES_192_GCM", "AES_128_GCM", "AES_256_CBC", "AES_192_CBC", "AES_128_CBC"


        :return: The encryption_algorithm of this PhaseTwoConfigDetails.
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """
        Sets the encryption_algorithm of this PhaseTwoConfigDetails.
        The encryption algorithm proposed during phase two tunnel negotiation.


        :param encryption_algorithm: The encryption_algorithm of this PhaseTwoConfigDetails.
        :type: str
        """
        allowed_values = ["AES_256_GCM", "AES_192_GCM", "AES_128_GCM", "AES_256_CBC", "AES_192_CBC", "AES_128_CBC"]
        if not value_allowed_none_or_none_sentinel(encryption_algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `encryption_algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._encryption_algorithm = encryption_algorithm

    @property
    def lifetime_in_seconds(self):
        """
        Gets the lifetime_in_seconds of this PhaseTwoConfigDetails.
        Lifetime in seconds for the IPSec session key set in phase two. The default is 3600 which is equivalent to 1 hour.


        :return: The lifetime_in_seconds of this PhaseTwoConfigDetails.
        :rtype: int
        """
        return self._lifetime_in_seconds

    @lifetime_in_seconds.setter
    def lifetime_in_seconds(self, lifetime_in_seconds):
        """
        Sets the lifetime_in_seconds of this PhaseTwoConfigDetails.
        Lifetime in seconds for the IPSec session key set in phase two. The default is 3600 which is equivalent to 1 hour.


        :param lifetime_in_seconds: The lifetime_in_seconds of this PhaseTwoConfigDetails.
        :type: int
        """
        self._lifetime_in_seconds = lifetime_in_seconds

    @property
    def is_pfs_enabled(self):
        """
        Gets the is_pfs_enabled of this PhaseTwoConfigDetails.
        Indicates whether perfect forward secrecy (PFS) is enabled.


        :return: The is_pfs_enabled of this PhaseTwoConfigDetails.
        :rtype: bool
        """
        return self._is_pfs_enabled

    @is_pfs_enabled.setter
    def is_pfs_enabled(self, is_pfs_enabled):
        """
        Sets the is_pfs_enabled of this PhaseTwoConfigDetails.
        Indicates whether perfect forward secrecy (PFS) is enabled.


        :param is_pfs_enabled: The is_pfs_enabled of this PhaseTwoConfigDetails.
        :type: bool
        """
        self._is_pfs_enabled = is_pfs_enabled

    @property
    def pfs_dh_group(self):
        """
        Gets the pfs_dh_group of this PhaseTwoConfigDetails.
        The Diffie-Hellman group used for PFS, if PFS is enabled.

        Allowed values for this property are: "GROUP2", "GROUP5", "GROUP14", "GROUP19", "GROUP20", "GROUP24"


        :return: The pfs_dh_group of this PhaseTwoConfigDetails.
        :rtype: str
        """
        return self._pfs_dh_group

    @pfs_dh_group.setter
    def pfs_dh_group(self, pfs_dh_group):
        """
        Sets the pfs_dh_group of this PhaseTwoConfigDetails.
        The Diffie-Hellman group used for PFS, if PFS is enabled.


        :param pfs_dh_group: The pfs_dh_group of this PhaseTwoConfigDetails.
        :type: str
        """
        allowed_values = ["GROUP2", "GROUP5", "GROUP14", "GROUP19", "GROUP20", "GROUP24"]
        if not value_allowed_none_or_none_sentinel(pfs_dh_group, allowed_values):
            raise ValueError(
                "Invalid value for `pfs_dh_group`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._pfs_dh_group = pfs_dh_group

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
