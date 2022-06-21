# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityRuleMatchCriteria(object):
    """
    Criteria to evaluate against network traffic.
    A match occurs when at least one item in the array associated with each specified property corresponds with the relevant aspect of the traffic.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityRuleMatchCriteria object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sources:
            The value to assign to the sources property of this SecurityRuleMatchCriteria.
        :type sources: list[str]

        :param destinations:
            The value to assign to the destinations property of this SecurityRuleMatchCriteria.
        :type destinations: list[str]

        :param applications:
            The value to assign to the applications property of this SecurityRuleMatchCriteria.
        :type applications: list[str]

        :param urls:
            The value to assign to the urls property of this SecurityRuleMatchCriteria.
        :type urls: list[str]

        """
        self.swagger_types = {
            'sources': 'list[str]',
            'destinations': 'list[str]',
            'applications': 'list[str]',
            'urls': 'list[str]'
        }

        self.attribute_map = {
            'sources': 'sources',
            'destinations': 'destinations',
            'applications': 'applications',
            'urls': 'urls'
        }

        self._sources = None
        self._destinations = None
        self._applications = None
        self._urls = None

    @property
    def sources(self):
        """
        Gets the sources of this SecurityRuleMatchCriteria.
        An array of IP address list names to be evaluated against the traffic source address.


        :return: The sources of this SecurityRuleMatchCriteria.
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this SecurityRuleMatchCriteria.
        An array of IP address list names to be evaluated against the traffic source address.


        :param sources: The sources of this SecurityRuleMatchCriteria.
        :type: list[str]
        """
        self._sources = sources

    @property
    def destinations(self):
        """
        Gets the destinations of this SecurityRuleMatchCriteria.
        An array of IP address list names to be evaluated against the traffic destination address.


        :return: The destinations of this SecurityRuleMatchCriteria.
        :rtype: list[str]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """
        Sets the destinations of this SecurityRuleMatchCriteria.
        An array of IP address list names to be evaluated against the traffic destination address.


        :param destinations: The destinations of this SecurityRuleMatchCriteria.
        :type: list[str]
        """
        self._destinations = destinations

    @property
    def applications(self):
        """
        Gets the applications of this SecurityRuleMatchCriteria.
        An array of application list names to be evaluated against the traffic protocol and protocol-specific parameters.


        :return: The applications of this SecurityRuleMatchCriteria.
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """
        Sets the applications of this SecurityRuleMatchCriteria.
        An array of application list names to be evaluated against the traffic protocol and protocol-specific parameters.


        :param applications: The applications of this SecurityRuleMatchCriteria.
        :type: list[str]
        """
        self._applications = applications

    @property
    def urls(self):
        """
        Gets the urls of this SecurityRuleMatchCriteria.
        An array of URL pattern list names to be evaluated against the HTTP(S) request target.


        :return: The urls of this SecurityRuleMatchCriteria.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """
        Sets the urls of this SecurityRuleMatchCriteria.
        An array of URL pattern list names to be evaluated against the HTTP(S) request target.


        :param urls: The urls of this SecurityRuleMatchCriteria.
        :type: list[str]
        """
        self._urls = urls

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
