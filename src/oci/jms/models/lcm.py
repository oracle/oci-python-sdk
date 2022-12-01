# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Lcm(object):
    """
    Enable lifecycle management and set post action configurations
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Lcm object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this Lcm.
        :type is_enabled: bool

        :param post_installation_actions:
            The value to assign to the post_installation_actions property of this Lcm.
        :type post_installation_actions: oci.jms.models.PostInstallationActionSettings

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'post_installation_actions': 'PostInstallationActionSettings'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'post_installation_actions': 'postInstallationActions'
        }

        self._is_enabled = None
        self._post_installation_actions = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this Lcm.
        Lcm flag to store enabled or disabled status


        :return: The is_enabled of this Lcm.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this Lcm.
        Lcm flag to store enabled or disabled status


        :param is_enabled: The is_enabled of this Lcm.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def post_installation_actions(self):
        """
        Gets the post_installation_actions of this Lcm.

        :return: The post_installation_actions of this Lcm.
        :rtype: oci.jms.models.PostInstallationActionSettings
        """
        return self._post_installation_actions

    @post_installation_actions.setter
    def post_installation_actions(self, post_installation_actions):
        """
        Sets the post_installation_actions of this Lcm.

        :param post_installation_actions: The post_installation_actions of this Lcm.
        :type: oci.jms.models.PostInstallationActionSettings
        """
        self._post_installation_actions = post_installation_actions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
