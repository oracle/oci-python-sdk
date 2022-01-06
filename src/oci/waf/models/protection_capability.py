# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProtectionCapability(object):
    """
    References an OCI-managed protection capability. Checks if HTTP requests/responses are malicious.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProtectionCapability object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ProtectionCapability.
        :type key: str

        :param version:
            The value to assign to the version property of this ProtectionCapability.
        :type version: int

        :param exclusions:
            The value to assign to the exclusions property of this ProtectionCapability.
        :type exclusions: oci.waf.models.ProtectionCapabilityExclusions

        :param action_name:
            The value to assign to the action_name property of this ProtectionCapability.
        :type action_name: str

        :param collaborative_action_threshold:
            The value to assign to the collaborative_action_threshold property of this ProtectionCapability.
        :type collaborative_action_threshold: int

        :param collaborative_weights:
            The value to assign to the collaborative_weights property of this ProtectionCapability.
        :type collaborative_weights: list[oci.waf.models.CollaborativeCapabilityWeightOverride]

        """
        self.swagger_types = {
            'key': 'str',
            'version': 'int',
            'exclusions': 'ProtectionCapabilityExclusions',
            'action_name': 'str',
            'collaborative_action_threshold': 'int',
            'collaborative_weights': 'list[CollaborativeCapabilityWeightOverride]'
        }

        self.attribute_map = {
            'key': 'key',
            'version': 'version',
            'exclusions': 'exclusions',
            'action_name': 'actionName',
            'collaborative_action_threshold': 'collaborativeActionThreshold',
            'collaborative_weights': 'collaborativeWeights'
        }

        self._key = None
        self._version = None
        self._exclusions = None
        self._action_name = None
        self._collaborative_action_threshold = None
        self._collaborative_weights = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this ProtectionCapability.
        Unique key of referenced protection capability.


        :return: The key of this ProtectionCapability.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ProtectionCapability.
        Unique key of referenced protection capability.


        :param key: The key of this ProtectionCapability.
        :type: str
        """
        self._key = key

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ProtectionCapability.
        Version of referenced protection capability.


        :return: The version of this ProtectionCapability.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ProtectionCapability.
        Version of referenced protection capability.


        :param version: The version of this ProtectionCapability.
        :type: int
        """
        self._version = version

    @property
    def exclusions(self):
        """
        Gets the exclusions of this ProtectionCapability.

        :return: The exclusions of this ProtectionCapability.
        :rtype: oci.waf.models.ProtectionCapabilityExclusions
        """
        return self._exclusions

    @exclusions.setter
    def exclusions(self, exclusions):
        """
        Sets the exclusions of this ProtectionCapability.

        :param exclusions: The exclusions of this ProtectionCapability.
        :type: oci.waf.models.ProtectionCapabilityExclusions
        """
        self._exclusions = exclusions

    @property
    def action_name(self):
        """
        Gets the action_name of this ProtectionCapability.
        Override action to take if capability was triggered, defined in Protection Rule for this capability.
        Only actions of type CHECK are allowed.


        :return: The action_name of this ProtectionCapability.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """
        Sets the action_name of this ProtectionCapability.
        Override action to take if capability was triggered, defined in Protection Rule for this capability.
        Only actions of type CHECK are allowed.


        :param action_name: The action_name of this ProtectionCapability.
        :type: str
        """
        self._action_name = action_name

    @property
    def collaborative_action_threshold(self):
        """
        Gets the collaborative_action_threshold of this ProtectionCapability.
        The minimum sum of weights of associated collaborative protection capabilities that have triggered which
        must be reached in order for _this_ capability to trigger.
        This field is ignored for non-collaborative capabilities.


        :return: The collaborative_action_threshold of this ProtectionCapability.
        :rtype: int
        """
        return self._collaborative_action_threshold

    @collaborative_action_threshold.setter
    def collaborative_action_threshold(self, collaborative_action_threshold):
        """
        Sets the collaborative_action_threshold of this ProtectionCapability.
        The minimum sum of weights of associated collaborative protection capabilities that have triggered which
        must be reached in order for _this_ capability to trigger.
        This field is ignored for non-collaborative capabilities.


        :param collaborative_action_threshold: The collaborative_action_threshold of this ProtectionCapability.
        :type: int
        """
        self._collaborative_action_threshold = collaborative_action_threshold

    @property
    def collaborative_weights(self):
        """
        Gets the collaborative_weights of this ProtectionCapability.
        Explicit weight values to use for associated collaborative protection capabilities.


        :return: The collaborative_weights of this ProtectionCapability.
        :rtype: list[oci.waf.models.CollaborativeCapabilityWeightOverride]
        """
        return self._collaborative_weights

    @collaborative_weights.setter
    def collaborative_weights(self, collaborative_weights):
        """
        Sets the collaborative_weights of this ProtectionCapability.
        Explicit weight values to use for associated collaborative protection capabilities.


        :param collaborative_weights: The collaborative_weights of this ProtectionCapability.
        :type: list[oci.waf.models.CollaborativeCapabilityWeightOverride]
        """
        self._collaborative_weights = collaborative_weights

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
