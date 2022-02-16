# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PhaseOneConfigDetails(object):
    """
    Configuration details for IKE phase one (ISAKMP) configuration parameters.
    """

    #: A constant which can be used with the authentication_algorithm property of a PhaseOneConfigDetails.
    #: This constant has a value of "SHA2_384"
    AUTHENTICATION_ALGORITHM_SHA2_384 = "SHA2_384"

    #: A constant which can be used with the authentication_algorithm property of a PhaseOneConfigDetails.
    #: This constant has a value of "SHA2_256"
    AUTHENTICATION_ALGORITHM_SHA2_256 = "SHA2_256"

    #: A constant which can be used with the authentication_algorithm property of a PhaseOneConfigDetails.
    #: This constant has a value of "SHA1_96"
    AUTHENTICATION_ALGORITHM_SHA1_96 = "SHA1_96"

    #: A constant which can be used with the encryption_algorithm property of a PhaseOneConfigDetails.
    #: This constant has a value of "AES_256_CBC"
    ENCRYPTION_ALGORITHM_AES_256_CBC = "AES_256_CBC"

    #: A constant which can be used with the encryption_algorithm property of a PhaseOneConfigDetails.
    #: This constant has a value of "AES_192_CBC"
    ENCRYPTION_ALGORITHM_AES_192_CBC = "AES_192_CBC"

    #: A constant which can be used with the encryption_algorithm property of a PhaseOneConfigDetails.
    #: This constant has a value of "AES_128_CBC"
    ENCRYPTION_ALGORITHM_AES_128_CBC = "AES_128_CBC"

    #: A constant which can be used with the diffie_helman_group property of a PhaseOneConfigDetails.
    #: This constant has a value of "GROUP2"
    DIFFIE_HELMAN_GROUP_GROUP2 = "GROUP2"

    #: A constant which can be used with the diffie_helman_group property of a PhaseOneConfigDetails.
    #: This constant has a value of "GROUP5"
    DIFFIE_HELMAN_GROUP_GROUP5 = "GROUP5"

    #: A constant which can be used with the diffie_helman_group property of a PhaseOneConfigDetails.
    #: This constant has a value of "GROUP14"
    DIFFIE_HELMAN_GROUP_GROUP14 = "GROUP14"

    #: A constant which can be used with the diffie_helman_group property of a PhaseOneConfigDetails.
    #: This constant has a value of "GROUP19"
    DIFFIE_HELMAN_GROUP_GROUP19 = "GROUP19"

    #: A constant which can be used with the diffie_helman_group property of a PhaseOneConfigDetails.
    #: This constant has a value of "GROUP20"
    DIFFIE_HELMAN_GROUP_GROUP20 = "GROUP20"

    #: A constant which can be used with the diffie_helman_group property of a PhaseOneConfigDetails.
    #: This constant has a value of "GROUP24"
    DIFFIE_HELMAN_GROUP_GROUP24 = "GROUP24"

    def __init__(self, **kwargs):
        """
        Initializes a new PhaseOneConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_custom_phase_one_config:
            The value to assign to the is_custom_phase_one_config property of this PhaseOneConfigDetails.
        :type is_custom_phase_one_config: bool

        :param authentication_algorithm:
            The value to assign to the authentication_algorithm property of this PhaseOneConfigDetails.
            Allowed values for this property are: "SHA2_384", "SHA2_256", "SHA1_96"
        :type authentication_algorithm: str

        :param encryption_algorithm:
            The value to assign to the encryption_algorithm property of this PhaseOneConfigDetails.
            Allowed values for this property are: "AES_256_CBC", "AES_192_CBC", "AES_128_CBC"
        :type encryption_algorithm: str

        :param diffie_helman_group:
            The value to assign to the diffie_helman_group property of this PhaseOneConfigDetails.
            Allowed values for this property are: "GROUP2", "GROUP5", "GROUP14", "GROUP19", "GROUP20", "GROUP24"
        :type diffie_helman_group: str

        :param lifetime_in_seconds:
            The value to assign to the lifetime_in_seconds property of this PhaseOneConfigDetails.
        :type lifetime_in_seconds: int

        """
        self.swagger_types = {
            'is_custom_phase_one_config': 'bool',
            'authentication_algorithm': 'str',
            'encryption_algorithm': 'str',
            'diffie_helman_group': 'str',
            'lifetime_in_seconds': 'int'
        }

        self.attribute_map = {
            'is_custom_phase_one_config': 'isCustomPhaseOneConfig',
            'authentication_algorithm': 'authenticationAlgorithm',
            'encryption_algorithm': 'encryptionAlgorithm',
            'diffie_helman_group': 'diffieHelmanGroup',
            'lifetime_in_seconds': 'lifetimeInSeconds'
        }

        self._is_custom_phase_one_config = None
        self._authentication_algorithm = None
        self._encryption_algorithm = None
        self._diffie_helman_group = None
        self._lifetime_in_seconds = None

    @property
    def is_custom_phase_one_config(self):
        """
        Gets the is_custom_phase_one_config of this PhaseOneConfigDetails.
        Indicates whether custom configuration is enabled for phase one options.


        :return: The is_custom_phase_one_config of this PhaseOneConfigDetails.
        :rtype: bool
        """
        return self._is_custom_phase_one_config

    @is_custom_phase_one_config.setter
    def is_custom_phase_one_config(self, is_custom_phase_one_config):
        """
        Sets the is_custom_phase_one_config of this PhaseOneConfigDetails.
        Indicates whether custom configuration is enabled for phase one options.


        :param is_custom_phase_one_config: The is_custom_phase_one_config of this PhaseOneConfigDetails.
        :type: bool
        """
        self._is_custom_phase_one_config = is_custom_phase_one_config

    @property
    def authentication_algorithm(self):
        """
        Gets the authentication_algorithm of this PhaseOneConfigDetails.
        The custom authentication algorithm proposed during phase one tunnel negotiation.

        Allowed values for this property are: "SHA2_384", "SHA2_256", "SHA1_96"


        :return: The authentication_algorithm of this PhaseOneConfigDetails.
        :rtype: str
        """
        return self._authentication_algorithm

    @authentication_algorithm.setter
    def authentication_algorithm(self, authentication_algorithm):
        """
        Sets the authentication_algorithm of this PhaseOneConfigDetails.
        The custom authentication algorithm proposed during phase one tunnel negotiation.


        :param authentication_algorithm: The authentication_algorithm of this PhaseOneConfigDetails.
        :type: str
        """
        allowed_values = ["SHA2_384", "SHA2_256", "SHA1_96"]
        if not value_allowed_none_or_none_sentinel(authentication_algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `authentication_algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._authentication_algorithm = authentication_algorithm

    @property
    def encryption_algorithm(self):
        """
        Gets the encryption_algorithm of this PhaseOneConfigDetails.
        The custom encryption algorithm proposed during phase one tunnel negotiation.

        Allowed values for this property are: "AES_256_CBC", "AES_192_CBC", "AES_128_CBC"


        :return: The encryption_algorithm of this PhaseOneConfigDetails.
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """
        Sets the encryption_algorithm of this PhaseOneConfigDetails.
        The custom encryption algorithm proposed during phase one tunnel negotiation.


        :param encryption_algorithm: The encryption_algorithm of this PhaseOneConfigDetails.
        :type: str
        """
        allowed_values = ["AES_256_CBC", "AES_192_CBC", "AES_128_CBC"]
        if not value_allowed_none_or_none_sentinel(encryption_algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `encryption_algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._encryption_algorithm = encryption_algorithm

    @property
    def diffie_helman_group(self):
        """
        Gets the diffie_helman_group of this PhaseOneConfigDetails.
        The custom Diffie-Hellman group proposed during phase one tunnel negotiation.

        Allowed values for this property are: "GROUP2", "GROUP5", "GROUP14", "GROUP19", "GROUP20", "GROUP24"


        :return: The diffie_helman_group of this PhaseOneConfigDetails.
        :rtype: str
        """
        return self._diffie_helman_group

    @diffie_helman_group.setter
    def diffie_helman_group(self, diffie_helman_group):
        """
        Sets the diffie_helman_group of this PhaseOneConfigDetails.
        The custom Diffie-Hellman group proposed during phase one tunnel negotiation.


        :param diffie_helman_group: The diffie_helman_group of this PhaseOneConfigDetails.
        :type: str
        """
        allowed_values = ["GROUP2", "GROUP5", "GROUP14", "GROUP19", "GROUP20", "GROUP24"]
        if not value_allowed_none_or_none_sentinel(diffie_helman_group, allowed_values):
            raise ValueError(
                "Invalid value for `diffie_helman_group`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._diffie_helman_group = diffie_helman_group

    @property
    def lifetime_in_seconds(self):
        """
        Gets the lifetime_in_seconds of this PhaseOneConfigDetails.
        Internet key association (IKE) session key lifetime in seconds for IPSec phase one. The default is 28800 which is equivalent to 8 hours.


        :return: The lifetime_in_seconds of this PhaseOneConfigDetails.
        :rtype: int
        """
        return self._lifetime_in_seconds

    @lifetime_in_seconds.setter
    def lifetime_in_seconds(self, lifetime_in_seconds):
        """
        Sets the lifetime_in_seconds of this PhaseOneConfigDetails.
        Internet key association (IKE) session key lifetime in seconds for IPSec phase one. The default is 28800 which is equivalent to 8 hours.


        :param lifetime_in_seconds: The lifetime_in_seconds of this PhaseOneConfigDetails.
        :type: int
        """
        self._lifetime_in_seconds = lifetime_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
