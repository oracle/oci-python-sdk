# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class BackendSetDetails(object):

    def __init__(self):

        self.swagger_types = {
            'backends': 'list[BackendDetails]',
            'health_checker': 'HealthCheckerDetails',
            'policy': 'str',
            'session_persistence_configuration': 'SessionPersistenceConfigurationDetails',
            'ssl_configuration': 'SSLConfigurationDetails'
        }

        self.attribute_map = {
            'backends': 'backends',
            'health_checker': 'healthChecker',
            'policy': 'policy',
            'session_persistence_configuration': 'sessionPersistenceConfiguration',
            'ssl_configuration': 'sslConfiguration'
        }

        self._backends = None
        self._health_checker = None
        self._policy = None
        self._session_persistence_configuration = None
        self._ssl_configuration = None

    @property
    def backends(self):
        """
        Gets the backends of this BackendSetDetails.

        :return: The backends of this BackendSetDetails.
        :rtype: list[BackendDetails]
        """
        return self._backends

    @backends.setter
    def backends(self, backends):
        """
        Sets the backends of this BackendSetDetails.

        :param backends: The backends of this BackendSetDetails.
        :type: list[BackendDetails]
        """
        self._backends = backends

    @property
    def health_checker(self):
        """
        Gets the health_checker of this BackendSetDetails.

        :return: The health_checker of this BackendSetDetails.
        :rtype: HealthCheckerDetails
        """
        return self._health_checker

    @health_checker.setter
    def health_checker(self, health_checker):
        """
        Sets the health_checker of this BackendSetDetails.

        :param health_checker: The health_checker of this BackendSetDetails.
        :type: HealthCheckerDetails
        """
        self._health_checker = health_checker

    @property
    def policy(self):
        """
        Gets the policy of this BackendSetDetails.
        The load balancer policy for the backend set. The default load balancing policy is 'ROUND_ROBIN'
        To get a list of available policies, use the :func:`list_policies`
        operation.

        Example: `LEAST_CONNECTIONS`


        :return: The policy of this BackendSetDetails.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this BackendSetDetails.
        The load balancer policy for the backend set. The default load balancing policy is 'ROUND_ROBIN'
        To get a list of available policies, use the :func:`list_policies`
        operation.

        Example: `LEAST_CONNECTIONS`


        :param policy: The policy of this BackendSetDetails.
        :type: str
        """
        self._policy = policy

    @property
    def session_persistence_configuration(self):
        """
        Gets the session_persistence_configuration of this BackendSetDetails.

        :return: The session_persistence_configuration of this BackendSetDetails.
        :rtype: SessionPersistenceConfigurationDetails
        """
        return self._session_persistence_configuration

    @session_persistence_configuration.setter
    def session_persistence_configuration(self, session_persistence_configuration):
        """
        Sets the session_persistence_configuration of this BackendSetDetails.

        :param session_persistence_configuration: The session_persistence_configuration of this BackendSetDetails.
        :type: SessionPersistenceConfigurationDetails
        """
        self._session_persistence_configuration = session_persistence_configuration

    @property
    def ssl_configuration(self):
        """
        Gets the ssl_configuration of this BackendSetDetails.

        :return: The ssl_configuration of this BackendSetDetails.
        :rtype: SSLConfigurationDetails
        """
        return self._ssl_configuration

    @ssl_configuration.setter
    def ssl_configuration(self, ssl_configuration):
        """
        Sets the ssl_configuration of this BackendSetDetails.

        :param ssl_configuration: The ssl_configuration of this BackendSetDetails.
        :type: SSLConfigurationDetails
        """
        self._ssl_configuration = ssl_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
