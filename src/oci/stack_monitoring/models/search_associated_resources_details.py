# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchAssociatedResourcesDetails(object):
    """
    The criteria for searching associated monitored resources.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SearchAssociatedResourcesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this SearchAssociatedResourcesDetails.
        :type compartment_id: str

        :param resource_type:
            The value to assign to the resource_type property of this SearchAssociatedResourcesDetails.
        :type resource_type: str

        :param resource_id:
            The value to assign to the resource_id property of this SearchAssociatedResourcesDetails.
        :type resource_id: str

        :param limit_level:
            The value to assign to the limit_level property of this SearchAssociatedResourcesDetails.
        :type limit_level: int

        :param association_types:
            The value to assign to the association_types property of this SearchAssociatedResourcesDetails.
        :type association_types: list[str]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'resource_type': 'str',
            'resource_id': 'str',
            'limit_level': 'int',
            'association_types': 'list[str]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'resource_type': 'resourceType',
            'resource_id': 'resourceId',
            'limit_level': 'limitLevel',
            'association_types': 'associationTypes'
        }

        self._compartment_id = None
        self._resource_type = None
        self._resource_id = None
        self._limit_level = None
        self._association_types = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SearchAssociatedResourcesDetails.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this SearchAssociatedResourcesDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SearchAssociatedResourcesDetails.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this SearchAssociatedResourcesDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resource_type(self):
        """
        Gets the resource_type of this SearchAssociatedResourcesDetails.
        A filter to return associated resources that match resources of type.
        Either resourceId or resourceType should be provided.


        :return: The resource_type of this SearchAssociatedResourcesDetails.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this SearchAssociatedResourcesDetails.
        A filter to return associated resources that match resources of type.
        Either resourceId or resourceType should be provided.


        :param resource_type: The resource_type of this SearchAssociatedResourcesDetails.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """
        Gets the resource_id of this SearchAssociatedResourcesDetails.
        Monitored resource identifier for which the associated resources should be fetched.
        Either resourceId or resourceType should be provided.


        :return: The resource_id of this SearchAssociatedResourcesDetails.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this SearchAssociatedResourcesDetails.
        Monitored resource identifier for which the associated resources should be fetched.
        Either resourceId or resourceType should be provided.


        :param resource_id: The resource_id of this SearchAssociatedResourcesDetails.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def limit_level(self):
        """
        Gets the limit_level of this SearchAssociatedResourcesDetails.
        The field which determines the depth of hierarchy while searching for associated resources.
        Possible values - 0 for all levels. And positive number to indicate different levels.
        Default value is 1, which indicates 1st level associations.


        :return: The limit_level of this SearchAssociatedResourcesDetails.
        :rtype: int
        """
        return self._limit_level

    @limit_level.setter
    def limit_level(self, limit_level):
        """
        Sets the limit_level of this SearchAssociatedResourcesDetails.
        The field which determines the depth of hierarchy while searching for associated resources.
        Possible values - 0 for all levels. And positive number to indicate different levels.
        Default value is 1, which indicates 1st level associations.


        :param limit_level: The limit_level of this SearchAssociatedResourcesDetails.
        :type: int
        """
        self._limit_level = limit_level

    @property
    def association_types(self):
        """
        Gets the association_types of this SearchAssociatedResourcesDetails.
        List of association types to be searched for finding associated resources


        :return: The association_types of this SearchAssociatedResourcesDetails.
        :rtype: list[str]
        """
        return self._association_types

    @association_types.setter
    def association_types(self, association_types):
        """
        Sets the association_types of this SearchAssociatedResourcesDetails.
        List of association types to be searched for finding associated resources


        :param association_types: The association_types of this SearchAssociatedResourcesDetails.
        :type: list[str]
        """
        self._association_types = association_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
