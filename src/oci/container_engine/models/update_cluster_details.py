# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateClusterDetails(object):
    """
    The properties that define a request to update a cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UpdateClusterDetails.
        :type name: str

        :param kubernetes_version:
            The value to assign to the kubernetes_version property of this UpdateClusterDetails.
        :type kubernetes_version: str

        :param options:
            The value to assign to the options property of this UpdateClusterDetails.
        :type options: UpdateClusterOptionsDetails

        """
        self.swagger_types = {
            'name': 'str',
            'kubernetes_version': 'str',
            'options': 'UpdateClusterOptionsDetails'
        }

        self.attribute_map = {
            'name': 'name',
            'kubernetes_version': 'kubernetesVersion',
            'options': 'options'
        }

        self._name = None
        self._kubernetes_version = None
        self._options = None

    @property
    def name(self):
        """
        Gets the name of this UpdateClusterDetails.
        The new name for the cluster. Avoid entering confidential information.


        :return: The name of this UpdateClusterDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateClusterDetails.
        The new name for the cluster. Avoid entering confidential information.


        :param name: The name of this UpdateClusterDetails.
        :type: str
        """
        self._name = name

    @property
    def kubernetes_version(self):
        """
        Gets the kubernetes_version of this UpdateClusterDetails.
        The version of Kubernetes to which the cluster masters should be upgraded.


        :return: The kubernetes_version of this UpdateClusterDetails.
        :rtype: str
        """
        return self._kubernetes_version

    @kubernetes_version.setter
    def kubernetes_version(self, kubernetes_version):
        """
        Sets the kubernetes_version of this UpdateClusterDetails.
        The version of Kubernetes to which the cluster masters should be upgraded.


        :param kubernetes_version: The kubernetes_version of this UpdateClusterDetails.
        :type: str
        """
        self._kubernetes_version = kubernetes_version

    @property
    def options(self):
        """
        Gets the options of this UpdateClusterDetails.

        :return: The options of this UpdateClusterDetails.
        :rtype: UpdateClusterOptionsDetails
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this UpdateClusterDetails.

        :param options: The options of this UpdateClusterDetails.
        :type: UpdateClusterOptionsDetails
        """
        self._options = options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
