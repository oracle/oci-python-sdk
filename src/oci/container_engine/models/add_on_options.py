# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddOnOptions(object):
    """
    The properties that define options for supported add-ons.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddOnOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_kubernetes_dashboard_enabled:
            The value to assign to the is_kubernetes_dashboard_enabled property of this AddOnOptions.
        :type is_kubernetes_dashboard_enabled: bool

        :param is_tiller_enabled:
            The value to assign to the is_tiller_enabled property of this AddOnOptions.
        :type is_tiller_enabled: bool

        """
        self.swagger_types = {
            'is_kubernetes_dashboard_enabled': 'bool',
            'is_tiller_enabled': 'bool'
        }

        self.attribute_map = {
            'is_kubernetes_dashboard_enabled': 'isKubernetesDashboardEnabled',
            'is_tiller_enabled': 'isTillerEnabled'
        }

        self._is_kubernetes_dashboard_enabled = None
        self._is_tiller_enabled = None

    @property
    def is_kubernetes_dashboard_enabled(self):
        """
        Gets the is_kubernetes_dashboard_enabled of this AddOnOptions.
        Whether or not to enable the Kubernetes Dashboard add-on.


        :return: The is_kubernetes_dashboard_enabled of this AddOnOptions.
        :rtype: bool
        """
        return self._is_kubernetes_dashboard_enabled

    @is_kubernetes_dashboard_enabled.setter
    def is_kubernetes_dashboard_enabled(self, is_kubernetes_dashboard_enabled):
        """
        Sets the is_kubernetes_dashboard_enabled of this AddOnOptions.
        Whether or not to enable the Kubernetes Dashboard add-on.


        :param is_kubernetes_dashboard_enabled: The is_kubernetes_dashboard_enabled of this AddOnOptions.
        :type: bool
        """
        self._is_kubernetes_dashboard_enabled = is_kubernetes_dashboard_enabled

    @property
    def is_tiller_enabled(self):
        """
        Gets the is_tiller_enabled of this AddOnOptions.
        Whether or not to enable the Tiller add-on.


        :return: The is_tiller_enabled of this AddOnOptions.
        :rtype: bool
        """
        return self._is_tiller_enabled

    @is_tiller_enabled.setter
    def is_tiller_enabled(self, is_tiller_enabled):
        """
        Sets the is_tiller_enabled of this AddOnOptions.
        Whether or not to enable the Tiller add-on.


        :param is_tiller_enabled: The is_tiller_enabled of this AddOnOptions.
        :type: bool
        """
        self._is_tiller_enabled = is_tiller_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
