# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


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

        :param public_endpoint:
            The value to assign to the public_endpoint property of this ClusterEndpoints.
        :type public_endpoint: str

        :param private_endpoint:
            The value to assign to the private_endpoint property of this ClusterEndpoints.
        :type private_endpoint: str

        :param vcn_hostname_endpoint:
            The value to assign to the vcn_hostname_endpoint property of this ClusterEndpoints.
        :type vcn_hostname_endpoint: str

        """
        self.swagger_types = {
            'kubernetes': 'str',
            'public_endpoint': 'str',
            'private_endpoint': 'str',
            'vcn_hostname_endpoint': 'str'
        }

        self.attribute_map = {
            'kubernetes': 'kubernetes',
            'public_endpoint': 'publicEndpoint',
            'private_endpoint': 'privateEndpoint',
            'vcn_hostname_endpoint': 'vcnHostnameEndpoint'
        }

        self._kubernetes = None
        self._public_endpoint = None
        self._private_endpoint = None
        self._vcn_hostname_endpoint = None

    @property
    def kubernetes(self):
        """
        Gets the kubernetes of this ClusterEndpoints.
        The non-native networking Kubernetes API server endpoint.


        :return: The kubernetes of this ClusterEndpoints.
        :rtype: str
        """
        return self._kubernetes

    @kubernetes.setter
    def kubernetes(self, kubernetes):
        """
        Sets the kubernetes of this ClusterEndpoints.
        The non-native networking Kubernetes API server endpoint.


        :param kubernetes: The kubernetes of this ClusterEndpoints.
        :type: str
        """
        self._kubernetes = kubernetes

    @property
    def public_endpoint(self):
        """
        Gets the public_endpoint of this ClusterEndpoints.
        The public native networking Kubernetes API server endpoint, if one was requested.


        :return: The public_endpoint of this ClusterEndpoints.
        :rtype: str
        """
        return self._public_endpoint

    @public_endpoint.setter
    def public_endpoint(self, public_endpoint):
        """
        Sets the public_endpoint of this ClusterEndpoints.
        The public native networking Kubernetes API server endpoint, if one was requested.


        :param public_endpoint: The public_endpoint of this ClusterEndpoints.
        :type: str
        """
        self._public_endpoint = public_endpoint

    @property
    def private_endpoint(self):
        """
        Gets the private_endpoint of this ClusterEndpoints.
        The private native networking Kubernetes API server endpoint.


        :return: The private_endpoint of this ClusterEndpoints.
        :rtype: str
        """
        return self._private_endpoint

    @private_endpoint.setter
    def private_endpoint(self, private_endpoint):
        """
        Sets the private_endpoint of this ClusterEndpoints.
        The private native networking Kubernetes API server endpoint.


        :param private_endpoint: The private_endpoint of this ClusterEndpoints.
        :type: str
        """
        self._private_endpoint = private_endpoint

    @property
    def vcn_hostname_endpoint(self):
        """
        Gets the vcn_hostname_endpoint of this ClusterEndpoints.
        The FQDN assigned to the Kubernetes API private endpoint.
        Example: 'https://yourVcnHostnameEndpoint'


        :return: The vcn_hostname_endpoint of this ClusterEndpoints.
        :rtype: str
        """
        return self._vcn_hostname_endpoint

    @vcn_hostname_endpoint.setter
    def vcn_hostname_endpoint(self, vcn_hostname_endpoint):
        """
        Sets the vcn_hostname_endpoint of this ClusterEndpoints.
        The FQDN assigned to the Kubernetes API private endpoint.
        Example: 'https://yourVcnHostnameEndpoint'


        :param vcn_hostname_endpoint: The vcn_hostname_endpoint of this ClusterEndpoints.
        :type: str
        """
        self._vcn_hostname_endpoint = vcn_hostname_endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
