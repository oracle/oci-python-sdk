# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstallationSiteCollection(object):
    """
    Results of an installation site search. Contains installation sites.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstallationSiteCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this InstallationSiteCollection.
        :type items: list[oci.jms.models.InstallationSiteSummary]

        """
        self.swagger_types = {
            'items': 'list[InstallationSiteSummary]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this InstallationSiteCollection.
        A list of Java installation sites.


        :return: The items of this InstallationSiteCollection.
        :rtype: list[oci.jms.models.InstallationSiteSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this InstallationSiteCollection.
        A list of Java installation sites.


        :param items: The items of this InstallationSiteCollection.
        :type: list[oci.jms.models.InstallationSiteSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
