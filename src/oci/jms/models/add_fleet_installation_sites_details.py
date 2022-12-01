# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddFleetInstallationSitesDetails(object):
    """
    The list of Java installation sites to add.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddFleetInstallationSitesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param installation_sites:
            The value to assign to the installation_sites property of this AddFleetInstallationSitesDetails.
        :type installation_sites: list[oci.jms.models.NewInstallationSite]

        :param post_installation_actions:
            The value to assign to the post_installation_actions property of this AddFleetInstallationSitesDetails.
        :type post_installation_actions: list[oci.jms.models.PostInstallationActions]

        """
        self.swagger_types = {
            'installation_sites': 'list[NewInstallationSite]',
            'post_installation_actions': 'list[PostInstallationActions]'
        }

        self.attribute_map = {
            'installation_sites': 'installationSites',
            'post_installation_actions': 'postInstallationActions'
        }

        self._installation_sites = None
        self._post_installation_actions = None

    @property
    def installation_sites(self):
        """
        **[Required]** Gets the installation_sites of this AddFleetInstallationSitesDetails.
        The list of installation sites to add.


        :return: The installation_sites of this AddFleetInstallationSitesDetails.
        :rtype: list[oci.jms.models.NewInstallationSite]
        """
        return self._installation_sites

    @installation_sites.setter
    def installation_sites(self, installation_sites):
        """
        Sets the installation_sites of this AddFleetInstallationSitesDetails.
        The list of installation sites to add.


        :param installation_sites: The installation_sites of this AddFleetInstallationSitesDetails.
        :type: list[oci.jms.models.NewInstallationSite]
        """
        self._installation_sites = installation_sites

    @property
    def post_installation_actions(self):
        """
        Gets the post_installation_actions of this AddFleetInstallationSitesDetails.
        Optional list of post java installation actions


        :return: The post_installation_actions of this AddFleetInstallationSitesDetails.
        :rtype: list[oci.jms.models.PostInstallationActions]
        """
        return self._post_installation_actions

    @post_installation_actions.setter
    def post_installation_actions(self, post_installation_actions):
        """
        Sets the post_installation_actions of this AddFleetInstallationSitesDetails.
        Optional list of post java installation actions


        :param post_installation_actions: The post_installation_actions of this AddFleetInstallationSitesDetails.
        :type: list[oci.jms.models.PostInstallationActions]
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
