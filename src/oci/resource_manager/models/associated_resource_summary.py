# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociatedResourceSummary(object):
    """
    Summary information for a resource associated with a stack or job.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssociatedResourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this AssociatedResourceSummary.
        :type resource_id: str

        :param resource_name:
            The value to assign to the resource_name property of this AssociatedResourceSummary.
        :type resource_name: str

        :param resource_type:
            The value to assign to the resource_type property of this AssociatedResourceSummary.
        :type resource_type: str

        :param attributes:
            The value to assign to the attributes property of this AssociatedResourceSummary.
        :type attributes: dict(str, str)

        :param time_created:
            The value to assign to the time_created property of this AssociatedResourceSummary.
        :type time_created: datetime

        :param region:
            The value to assign to the region property of this AssociatedResourceSummary.
        :type region: str

        :param resource_address:
            The value to assign to the resource_address property of this AssociatedResourceSummary.
        :type resource_address: str

        """
        self.swagger_types = {
            'resource_id': 'str',
            'resource_name': 'str',
            'resource_type': 'str',
            'attributes': 'dict(str, str)',
            'time_created': 'datetime',
            'region': 'str',
            'resource_address': 'str'
        }

        self.attribute_map = {
            'resource_id': 'resourceId',
            'resource_name': 'resourceName',
            'resource_type': 'resourceType',
            'attributes': 'attributes',
            'time_created': 'timeCreated',
            'region': 'region',
            'resource_address': 'resourceAddress'
        }

        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._attributes = None
        self._time_created = None
        self._region = None
        self._resource_address = None

    @property
    def resource_id(self):
        """
        Gets the resource_id of this AssociatedResourceSummary.
        Unique identifier for the resource.


        :return: The resource_id of this AssociatedResourceSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this AssociatedResourceSummary.
        Unique identifier for the resource.


        :param resource_id: The resource_id of this AssociatedResourceSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """
        Gets the resource_name of this AssociatedResourceSummary.
        Name of the resource.


        :return: The resource_name of this AssociatedResourceSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this AssociatedResourceSummary.
        Name of the resource.


        :param resource_name: The resource_name of this AssociatedResourceSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """
        Gets the resource_type of this AssociatedResourceSummary.
        Resource type. For more information about resource types supported for the Oracle Cloud Infrastructure (OCI) provider, see `Oracle Cloud Infrastructure Provider`__.

        __ https://registry.terraform.io/providers/oracle/oci/latest/docs


        :return: The resource_type of this AssociatedResourceSummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this AssociatedResourceSummary.
        Resource type. For more information about resource types supported for the Oracle Cloud Infrastructure (OCI) provider, see `Oracle Cloud Infrastructure Provider`__.

        __ https://registry.terraform.io/providers/oracle/oci/latest/docs


        :param resource_type: The resource_type of this AssociatedResourceSummary.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def attributes(self):
        """
        Gets the attributes of this AssociatedResourceSummary.
        Resource attribute values. Each value is represented as a key-value pair.
        Example: `{\"state\": \"AVAILABLE\"}`


        :return: The attributes of this AssociatedResourceSummary.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this AssociatedResourceSummary.
        Resource attribute values. Each value is represented as a key-value pair.
        Example: `{\"state\": \"AVAILABLE\"}`


        :param attributes: The attributes of this AssociatedResourceSummary.
        :type: dict(str, str)
        """
        self._attributes = attributes

    @property
    def time_created(self):
        """
        Gets the time_created of this AssociatedResourceSummary.
        The date and time when the stack was created.
        Format is defined by RFC3339.
        Example: `2022-07-25T21:10:29.600Z`


        :return: The time_created of this AssociatedResourceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AssociatedResourceSummary.
        The date and time when the stack was created.
        Format is defined by RFC3339.
        Example: `2022-07-25T21:10:29.600Z`


        :param time_created: The time_created of this AssociatedResourceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def region(self):
        """
        Gets the region of this AssociatedResourceSummary.
        Resource region.
        For information about regions, see `Regions and Availability Domains`__.
        Example: `us-phoenix-1`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm


        :return: The region of this AssociatedResourceSummary.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this AssociatedResourceSummary.
        Resource region.
        For information about regions, see `Regions and Availability Domains`__.
        Example: `us-phoenix-1`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm


        :param region: The region of this AssociatedResourceSummary.
        :type: str
        """
        self._region = region

    @property
    def resource_address(self):
        """
        Gets the resource_address of this AssociatedResourceSummary.
        Terraform resource address.


        :return: The resource_address of this AssociatedResourceSummary.
        :rtype: str
        """
        return self._resource_address

    @resource_address.setter
    def resource_address(self, resource_address):
        """
        Sets the resource_address of this AssociatedResourceSummary.
        Terraform resource address.


        :param resource_address: The resource_address of this AssociatedResourceSummary.
        :type: str
        """
        self._resource_address = resource_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
