# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class BackendSetHealth(object):

    def __init__(self):

        self.swagger_types = {
            'is_healthy': 'bool',
            'unhealthy_backends': 'list[str]'
        }

        self.attribute_map = {
            'is_healthy': 'isHealthy',
            'unhealthy_backends': 'unhealthyBackends'
        }

        self._is_healthy = None
        self._unhealthy_backends = None

    @property
    def is_healthy(self):
        """
        Gets the is_healthy of this BackendSetHealth.
        A healthy/unhealthy boolean to quickly describe backend set health.


        :return: The is_healthy of this BackendSetHealth.
        :rtype: bool
        """
        return self._is_healthy

    @is_healthy.setter
    def is_healthy(self, is_healthy):
        """
        Sets the is_healthy of this BackendSetHealth.
        A healthy/unhealthy boolean to quickly describe backend set health.


        :param is_healthy: The is_healthy of this BackendSetHealth.
        :type: bool
        """
        self._is_healthy = is_healthy

    @property
    def unhealthy_backends(self):
        """
        Gets the unhealthy_backends of this BackendSetHealth.
        A list of unhealthy backend identifiers.


        :return: The unhealthy_backends of this BackendSetHealth.
        :rtype: list[str]
        """
        return self._unhealthy_backends

    @unhealthy_backends.setter
    def unhealthy_backends(self, unhealthy_backends):
        """
        Sets the unhealthy_backends of this BackendSetHealth.
        A list of unhealthy backend identifiers.


        :param unhealthy_backends: The unhealthy_backends of this BackendSetHealth.
        :type: list[str]
        """
        self._unhealthy_backends = unhealthy_backends

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
