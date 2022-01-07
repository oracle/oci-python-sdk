# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .listing_package import ListingPackage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OrchestrationListingPackage(ListingPackage):
    """
    A listing package for orchestration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OrchestrationListingPackage object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace.models.OrchestrationListingPackage.package_type` attribute
        of this class is ``ORCHESTRATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this OrchestrationListingPackage.
        :type description: str

        :param listing_id:
            The value to assign to the listing_id property of this OrchestrationListingPackage.
        :type listing_id: str

        :param version:
            The value to assign to the version property of this OrchestrationListingPackage.
        :type version: str

        :param package_type:
            The value to assign to the package_type property of this OrchestrationListingPackage.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE"
        :type package_type: str

        :param pricing:
            The value to assign to the pricing property of this OrchestrationListingPackage.
        :type pricing: oci.marketplace.models.PricingModel

        :param resource_id:
            The value to assign to the resource_id property of this OrchestrationListingPackage.
        :type resource_id: str

        :param time_created:
            The value to assign to the time_created property of this OrchestrationListingPackage.
        :type time_created: datetime

        :param operating_system:
            The value to assign to the operating_system property of this OrchestrationListingPackage.
        :type operating_system: oci.marketplace.models.OperatingSystem

        :param resource_link:
            The value to assign to the resource_link property of this OrchestrationListingPackage.
        :type resource_link: str

        :param variables:
            The value to assign to the variables property of this OrchestrationListingPackage.
        :type variables: list[oci.marketplace.models.OrchestrationVariable]

        :param regions:
            The value to assign to the regions property of this OrchestrationListingPackage.
        :type regions: list[oci.marketplace.models.Region]

        """
        self.swagger_types = {
            'description': 'str',
            'listing_id': 'str',
            'version': 'str',
            'package_type': 'str',
            'pricing': 'PricingModel',
            'resource_id': 'str',
            'time_created': 'datetime',
            'operating_system': 'OperatingSystem',
            'resource_link': 'str',
            'variables': 'list[OrchestrationVariable]',
            'regions': 'list[Region]'
        }

        self.attribute_map = {
            'description': 'description',
            'listing_id': 'listingId',
            'version': 'version',
            'package_type': 'packageType',
            'pricing': 'pricing',
            'resource_id': 'resourceId',
            'time_created': 'timeCreated',
            'operating_system': 'operatingSystem',
            'resource_link': 'resourceLink',
            'variables': 'variables',
            'regions': 'regions'
        }

        self._description = None
        self._listing_id = None
        self._version = None
        self._package_type = None
        self._pricing = None
        self._resource_id = None
        self._time_created = None
        self._operating_system = None
        self._resource_link = None
        self._variables = None
        self._regions = None
        self._package_type = 'ORCHESTRATION'

    @property
    def resource_link(self):
        """
        Gets the resource_link of this OrchestrationListingPackage.
        Link to the orchestration resource.


        :return: The resource_link of this OrchestrationListingPackage.
        :rtype: str
        """
        return self._resource_link

    @resource_link.setter
    def resource_link(self, resource_link):
        """
        Sets the resource_link of this OrchestrationListingPackage.
        Link to the orchestration resource.


        :param resource_link: The resource_link of this OrchestrationListingPackage.
        :type: str
        """
        self._resource_link = resource_link

    @property
    def variables(self):
        """
        Gets the variables of this OrchestrationListingPackage.
        List of variables for the orchestration resource.


        :return: The variables of this OrchestrationListingPackage.
        :rtype: list[oci.marketplace.models.OrchestrationVariable]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this OrchestrationListingPackage.
        List of variables for the orchestration resource.


        :param variables: The variables of this OrchestrationListingPackage.
        :type: list[oci.marketplace.models.OrchestrationVariable]
        """
        self._variables = variables

    @property
    def regions(self):
        """
        Gets the regions of this OrchestrationListingPackage.
        The regions where you can deploy this listing package. (Some packages have restrictions that limit their deployment to United States regions only.)


        :return: The regions of this OrchestrationListingPackage.
        :rtype: list[oci.marketplace.models.Region]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this OrchestrationListingPackage.
        The regions where you can deploy this listing package. (Some packages have restrictions that limit their deployment to United States regions only.)


        :param regions: The regions of this OrchestrationListingPackage.
        :type: list[oci.marketplace.models.Region]
        """
        self._regions = regions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
