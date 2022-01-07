# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TunnelPhaseOneDetails(object):
    """
    Tunnel detail information specific to IPSec phase 1.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TunnelPhaseOneDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_custom_phase_one_config:
            The value to assign to the is_custom_phase_one_config property of this TunnelPhaseOneDetails.
        :type is_custom_phase_one_config: bool

        :param lifetime:
            The value to assign to the lifetime property of this TunnelPhaseOneDetails.
        :type lifetime: int

        :param remaining_lifetime:
            The value to assign to the remaining_lifetime property of this TunnelPhaseOneDetails.
        :type remaining_lifetime: int

        :param custom_authentication_algorithm:
            The value to assign to the custom_authentication_algorithm property of this TunnelPhaseOneDetails.
        :type custom_authentication_algorithm: str

        :param negotiated_authentication_algorithm:
            The value to assign to the negotiated_authentication_algorithm property of this TunnelPhaseOneDetails.
        :type negotiated_authentication_algorithm: str

        :param custom_encryption_algorithm:
            The value to assign to the custom_encryption_algorithm property of this TunnelPhaseOneDetails.
        :type custom_encryption_algorithm: str

        :param negotiated_encryption_algorithm:
            The value to assign to the negotiated_encryption_algorithm property of this TunnelPhaseOneDetails.
        :type negotiated_encryption_algorithm: str

        :param custom_dh_group:
            The value to assign to the custom_dh_group property of this TunnelPhaseOneDetails.
        :type custom_dh_group: str

        :param negotiated_dh_group:
            The value to assign to the negotiated_dh_group property of this TunnelPhaseOneDetails.
        :type negotiated_dh_group: str

        :param is_ike_established:
            The value to assign to the is_ike_established property of this TunnelPhaseOneDetails.
        :type is_ike_established: bool

        :param remaining_lifetime_last_retrieved:
            The value to assign to the remaining_lifetime_last_retrieved property of this TunnelPhaseOneDetails.
        :type remaining_lifetime_last_retrieved: datetime

        """
        self.swagger_types = {
            'is_custom_phase_one_config': 'bool',
            'lifetime': 'int',
            'remaining_lifetime': 'int',
            'custom_authentication_algorithm': 'str',
            'negotiated_authentication_algorithm': 'str',
            'custom_encryption_algorithm': 'str',
            'negotiated_encryption_algorithm': 'str',
            'custom_dh_group': 'str',
            'negotiated_dh_group': 'str',
            'is_ike_established': 'bool',
            'remaining_lifetime_last_retrieved': 'datetime'
        }

        self.attribute_map = {
            'is_custom_phase_one_config': 'isCustomPhaseOneConfig',
            'lifetime': 'lifetime',
            'remaining_lifetime': 'remainingLifetime',
            'custom_authentication_algorithm': 'customAuthenticationAlgorithm',
            'negotiated_authentication_algorithm': 'negotiatedAuthenticationAlgorithm',
            'custom_encryption_algorithm': 'customEncryptionAlgorithm',
            'negotiated_encryption_algorithm': 'negotiatedEncryptionAlgorithm',
            'custom_dh_group': 'customDhGroup',
            'negotiated_dh_group': 'negotiatedDhGroup',
            'is_ike_established': 'isIkeEstablished',
            'remaining_lifetime_last_retrieved': 'remainingLifetimeLastRetrieved'
        }

        self._is_custom_phase_one_config = None
        self._lifetime = None
        self._remaining_lifetime = None
        self._custom_authentication_algorithm = None
        self._negotiated_authentication_algorithm = None
        self._custom_encryption_algorithm = None
        self._negotiated_encryption_algorithm = None
        self._custom_dh_group = None
        self._negotiated_dh_group = None
        self._is_ike_established = None
        self._remaining_lifetime_last_retrieved = None

    @property
    def is_custom_phase_one_config(self):
        """
        Gets the is_custom_phase_one_config of this TunnelPhaseOneDetails.
        Indicates whether custom phase one configuration is enabled.


        :return: The is_custom_phase_one_config of this TunnelPhaseOneDetails.
        :rtype: bool
        """
        return self._is_custom_phase_one_config

    @is_custom_phase_one_config.setter
    def is_custom_phase_one_config(self, is_custom_phase_one_config):
        """
        Sets the is_custom_phase_one_config of this TunnelPhaseOneDetails.
        Indicates whether custom phase one configuration is enabled.


        :param is_custom_phase_one_config: The is_custom_phase_one_config of this TunnelPhaseOneDetails.
        :type: bool
        """
        self._is_custom_phase_one_config = is_custom_phase_one_config

    @property
    def lifetime(self):
        """
        Gets the lifetime of this TunnelPhaseOneDetails.
        The total configured lifetime of an IKE security association.


        :return: The lifetime of this TunnelPhaseOneDetails.
        :rtype: int
        """
        return self._lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        """
        Sets the lifetime of this TunnelPhaseOneDetails.
        The total configured lifetime of an IKE security association.


        :param lifetime: The lifetime of this TunnelPhaseOneDetails.
        :type: int
        """
        self._lifetime = lifetime

    @property
    def remaining_lifetime(self):
        """
        Gets the remaining_lifetime of this TunnelPhaseOneDetails.
        The lifetime remaining before the key is refreshed.


        :return: The remaining_lifetime of this TunnelPhaseOneDetails.
        :rtype: int
        """
        return self._remaining_lifetime

    @remaining_lifetime.setter
    def remaining_lifetime(self, remaining_lifetime):
        """
        Sets the remaining_lifetime of this TunnelPhaseOneDetails.
        The lifetime remaining before the key is refreshed.


        :param remaining_lifetime: The remaining_lifetime of this TunnelPhaseOneDetails.
        :type: int
        """
        self._remaining_lifetime = remaining_lifetime

    @property
    def custom_authentication_algorithm(self):
        """
        Gets the custom_authentication_algorithm of this TunnelPhaseOneDetails.
        Custom authentication algorithm


        :return: The custom_authentication_algorithm of this TunnelPhaseOneDetails.
        :rtype: str
        """
        return self._custom_authentication_algorithm

    @custom_authentication_algorithm.setter
    def custom_authentication_algorithm(self, custom_authentication_algorithm):
        """
        Sets the custom_authentication_algorithm of this TunnelPhaseOneDetails.
        Custom authentication algorithm


        :param custom_authentication_algorithm: The custom_authentication_algorithm of this TunnelPhaseOneDetails.
        :type: str
        """
        self._custom_authentication_algorithm = custom_authentication_algorithm

    @property
    def negotiated_authentication_algorithm(self):
        """
        Gets the negotiated_authentication_algorithm of this TunnelPhaseOneDetails.
        The negotiated authentication algorithm.


        :return: The negotiated_authentication_algorithm of this TunnelPhaseOneDetails.
        :rtype: str
        """
        return self._negotiated_authentication_algorithm

    @negotiated_authentication_algorithm.setter
    def negotiated_authentication_algorithm(self, negotiated_authentication_algorithm):
        """
        Sets the negotiated_authentication_algorithm of this TunnelPhaseOneDetails.
        The negotiated authentication algorithm.


        :param negotiated_authentication_algorithm: The negotiated_authentication_algorithm of this TunnelPhaseOneDetails.
        :type: str
        """
        self._negotiated_authentication_algorithm = negotiated_authentication_algorithm

    @property
    def custom_encryption_algorithm(self):
        """
        Gets the custom_encryption_algorithm of this TunnelPhaseOneDetails.
        Custom encryption algorithm.


        :return: The custom_encryption_algorithm of this TunnelPhaseOneDetails.
        :rtype: str
        """
        return self._custom_encryption_algorithm

    @custom_encryption_algorithm.setter
    def custom_encryption_algorithm(self, custom_encryption_algorithm):
        """
        Sets the custom_encryption_algorithm of this TunnelPhaseOneDetails.
        Custom encryption algorithm.


        :param custom_encryption_algorithm: The custom_encryption_algorithm of this TunnelPhaseOneDetails.
        :type: str
        """
        self._custom_encryption_algorithm = custom_encryption_algorithm

    @property
    def negotiated_encryption_algorithm(self):
        """
        Gets the negotiated_encryption_algorithm of this TunnelPhaseOneDetails.
        The negotiated encryption algorithm.


        :return: The negotiated_encryption_algorithm of this TunnelPhaseOneDetails.
        :rtype: str
        """
        return self._negotiated_encryption_algorithm

    @negotiated_encryption_algorithm.setter
    def negotiated_encryption_algorithm(self, negotiated_encryption_algorithm):
        """
        Sets the negotiated_encryption_algorithm of this TunnelPhaseOneDetails.
        The negotiated encryption algorithm.


        :param negotiated_encryption_algorithm: The negotiated_encryption_algorithm of this TunnelPhaseOneDetails.
        :type: str
        """
        self._negotiated_encryption_algorithm = negotiated_encryption_algorithm

    @property
    def custom_dh_group(self):
        """
        Gets the custom_dh_group of this TunnelPhaseOneDetails.
        Custom Diffie-Hellman group.


        :return: The custom_dh_group of this TunnelPhaseOneDetails.
        :rtype: str
        """
        return self._custom_dh_group

    @custom_dh_group.setter
    def custom_dh_group(self, custom_dh_group):
        """
        Sets the custom_dh_group of this TunnelPhaseOneDetails.
        Custom Diffie-Hellman group.


        :param custom_dh_group: The custom_dh_group of this TunnelPhaseOneDetails.
        :type: str
        """
        self._custom_dh_group = custom_dh_group

    @property
    def negotiated_dh_group(self):
        """
        Gets the negotiated_dh_group of this TunnelPhaseOneDetails.
        The negotiated Diffie-Hellman group.


        :return: The negotiated_dh_group of this TunnelPhaseOneDetails.
        :rtype: str
        """
        return self._negotiated_dh_group

    @negotiated_dh_group.setter
    def negotiated_dh_group(self, negotiated_dh_group):
        """
        Sets the negotiated_dh_group of this TunnelPhaseOneDetails.
        The negotiated Diffie-Hellman group.


        :param negotiated_dh_group: The negotiated_dh_group of this TunnelPhaseOneDetails.
        :type: str
        """
        self._negotiated_dh_group = negotiated_dh_group

    @property
    def is_ike_established(self):
        """
        Gets the is_ike_established of this TunnelPhaseOneDetails.
        Indicates whether IKE Phase 1 is established.


        :return: The is_ike_established of this TunnelPhaseOneDetails.
        :rtype: bool
        """
        return self._is_ike_established

    @is_ike_established.setter
    def is_ike_established(self, is_ike_established):
        """
        Sets the is_ike_established of this TunnelPhaseOneDetails.
        Indicates whether IKE Phase 1 is established.


        :param is_ike_established: The is_ike_established of this TunnelPhaseOneDetails.
        :type: bool
        """
        self._is_ike_established = is_ike_established

    @property
    def remaining_lifetime_last_retrieved(self):
        """
        Gets the remaining_lifetime_last_retrieved of this TunnelPhaseOneDetails.
        The date and time we retrieved the remaining lifetime, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The remaining_lifetime_last_retrieved of this TunnelPhaseOneDetails.
        :rtype: datetime
        """
        return self._remaining_lifetime_last_retrieved

    @remaining_lifetime_last_retrieved.setter
    def remaining_lifetime_last_retrieved(self, remaining_lifetime_last_retrieved):
        """
        Sets the remaining_lifetime_last_retrieved of this TunnelPhaseOneDetails.
        The date and time we retrieved the remaining lifetime, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param remaining_lifetime_last_retrieved: The remaining_lifetime_last_retrieved of this TunnelPhaseOneDetails.
        :type: datetime
        """
        self._remaining_lifetime_last_retrieved = remaining_lifetime_last_retrieved

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
