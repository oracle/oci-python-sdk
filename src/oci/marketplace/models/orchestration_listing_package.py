# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

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

        :param pricing:
            The value to assign to the pricing property of this OrchestrationListingPackage.
        :type pricing: PricingModel

        :param resource_id:
            The value to assign to the resource_id property of this OrchestrationListingPackage.
        :type resource_id: str

        :param time_created:
            The value to assign to the time_created property of this OrchestrationListingPackage.
        :type time_created: datetime

        :param resource_link:
            The value to assign to the resource_link property of this OrchestrationListingPackage.
        :type resource_link: str

        :param variables:
            The value to assign to the variables property of this OrchestrationListingPackage.
        :type variables: list[OrchestrationVariable]

        """
        self.swagger_types = {
            'description': 'str',
            'listing_id': 'str',
            'version': 'str',
            'pricing': 'PricingModel',
            'resource_id': 'str',
            'time_created': 'datetime',
            'resource_link': 'str',
            'variables': 'list[OrchestrationVariable]'
        }

        self.attribute_map = {
            'description': 'description',
            'listing_id': 'listingId',
            'version': 'version',
            'pricing': 'pricing',
            'resource_id': 'resourceId',
            'time_created': 'timeCreated',
            'resource_link': 'resourceLink',
            'variables': 'variables'
        }

        self._description = None
        self._listing_id = None
        self._version = None
        self._pricing = None
        self._resource_id = None
        self._time_created = None
        self._resource_link = None
        self._variables = None
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
        :rtype: list[OrchestrationVariable]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this OrchestrationListingPackage.
        List of variables for the orchestration resource.


        :param variables: The variables of this OrchestrationListingPackage.
        :type: list[OrchestrationVariable]
        """
        self._variables = variables

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
