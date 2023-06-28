# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181001

from .publication_package import PublicationPackage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OrchestrationPublicationPackage(PublicationPackage):
    """
    A publication package for stack publications.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OrchestrationPublicationPackage object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace.models.OrchestrationPublicationPackage.package_type` attribute
        of this class is ``ORCHESTRATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this OrchestrationPublicationPackage.
        :type description: str

        :param listing_id:
            The value to assign to the listing_id property of this OrchestrationPublicationPackage.
        :type listing_id: str

        :param version:
            The value to assign to the version property of this OrchestrationPublicationPackage.
        :type version: str

        :param package_type:
            The value to assign to the package_type property of this OrchestrationPublicationPackage.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE"
        :type package_type: str

        :param resource_id:
            The value to assign to the resource_id property of this OrchestrationPublicationPackage.
        :type resource_id: str

        :param time_created:
            The value to assign to the time_created property of this OrchestrationPublicationPackage.
        :type time_created: datetime

        :param operating_system:
            The value to assign to the operating_system property of this OrchestrationPublicationPackage.
        :type operating_system: oci.marketplace.models.OperatingSystem

        :param resource_link:
            The value to assign to the resource_link property of this OrchestrationPublicationPackage.
        :type resource_link: str

        :param variables:
            The value to assign to the variables property of this OrchestrationPublicationPackage.
        :type variables: list[oci.marketplace.models.OrchestrationVariable]

        """
        self.swagger_types = {
            'description': 'str',
            'listing_id': 'str',
            'version': 'str',
            'package_type': 'str',
            'resource_id': 'str',
            'time_created': 'datetime',
            'operating_system': 'OperatingSystem',
            'resource_link': 'str',
            'variables': 'list[OrchestrationVariable]'
        }

        self.attribute_map = {
            'description': 'description',
            'listing_id': 'listingId',
            'version': 'version',
            'package_type': 'packageType',
            'resource_id': 'resourceId',
            'time_created': 'timeCreated',
            'operating_system': 'operatingSystem',
            'resource_link': 'resourceLink',
            'variables': 'variables'
        }

        self._description = None
        self._listing_id = None
        self._version = None
        self._package_type = None
        self._resource_id = None
        self._time_created = None
        self._operating_system = None
        self._resource_link = None
        self._variables = None
        self._package_type = 'ORCHESTRATION'

    @property
    def resource_link(self):
        """
        Gets the resource_link of this OrchestrationPublicationPackage.
        A link to the stack resource.


        :return: The resource_link of this OrchestrationPublicationPackage.
        :rtype: str
        """
        return self._resource_link

    @resource_link.setter
    def resource_link(self, resource_link):
        """
        Sets the resource_link of this OrchestrationPublicationPackage.
        A link to the stack resource.


        :param resource_link: The resource_link of this OrchestrationPublicationPackage.
        :type: str
        """
        self._resource_link = resource_link

    @property
    def variables(self):
        """
        Gets the variables of this OrchestrationPublicationPackage.
        A list of variables for the stack resource.


        :return: The variables of this OrchestrationPublicationPackage.
        :rtype: list[oci.marketplace.models.OrchestrationVariable]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this OrchestrationPublicationPackage.
        A list of variables for the stack resource.


        :param variables: The variables of this OrchestrationPublicationPackage.
        :type: list[oci.marketplace.models.OrchestrationVariable]
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
