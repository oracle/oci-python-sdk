# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DecryptionRuleMatchCriteria(object):
    """
    Match criteria used in Decryption Rule used on the firewall policy rules.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DecryptionRuleMatchCriteria object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sources:
            The value to assign to the sources property of this DecryptionRuleMatchCriteria.
        :type sources: list[str]

        :param destinations:
            The value to assign to the destinations property of this DecryptionRuleMatchCriteria.
        :type destinations: list[str]

        """
        self.swagger_types = {
            'sources': 'list[str]',
            'destinations': 'list[str]'
        }

        self.attribute_map = {
            'sources': 'sources',
            'destinations': 'destinations'
        }

        self._sources = None
        self._destinations = None

    @property
    def sources(self):
        """
        Gets the sources of this DecryptionRuleMatchCriteria.
        An array of IP address list names to be evaluated against the traffic source address.


        :return: The sources of this DecryptionRuleMatchCriteria.
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this DecryptionRuleMatchCriteria.
        An array of IP address list names to be evaluated against the traffic source address.


        :param sources: The sources of this DecryptionRuleMatchCriteria.
        :type: list[str]
        """
        self._sources = sources

    @property
    def destinations(self):
        """
        Gets the destinations of this DecryptionRuleMatchCriteria.
        An array of IP address list names to be evaluated against the traffic destination address.


        :return: The destinations of this DecryptionRuleMatchCriteria.
        :rtype: list[str]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """
        Sets the destinations of this DecryptionRuleMatchCriteria.
        An array of IP address list names to be evaluated against the traffic destination address.


        :param destinations: The destinations of this DecryptionRuleMatchCriteria.
        :type: list[str]
        """
        self._destinations = destinations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
