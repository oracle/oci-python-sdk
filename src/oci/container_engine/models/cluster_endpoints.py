# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterEndpoints(object):
    """
    The properties that define endpoints for a cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterEndpoints object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kubernetes:
            The value to assign to the kubernetes property of this ClusterEndpoints.
        :type kubernetes: str

        """
        self.swagger_types = {
            'kubernetes': 'str'
        }

        self.attribute_map = {
            'kubernetes': 'kubernetes'
        }

        self._kubernetes = None

    @property
    def kubernetes(self):
        """
        Gets the kubernetes of this ClusterEndpoints.
        The Kubernetes API server endpoint.


        :return: The kubernetes of this ClusterEndpoints.
        :rtype: str
        """
        return self._kubernetes

    @kubernetes.setter
    def kubernetes(self, kubernetes):
        """
        Sets the kubernetes of this ClusterEndpoints.
        The Kubernetes API server endpoint.


        :param kubernetes: The kubernetes of this ClusterEndpoints.
        :type: str
        """
        self._kubernetes = kubernetes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
