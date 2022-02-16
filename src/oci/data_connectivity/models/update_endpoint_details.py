# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateEndpointDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this UpdateEndpointDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateEndpointDetails.
        :type display_name: str

        :param endpoint_size:
            The value to assign to the endpoint_size property of this UpdateEndpointDetails.
        :type endpoint_size: int

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateEndpointDetails.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'description': 'str',
            'display_name': 'str',
            'endpoint_size': 'int',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'description': 'description',
            'display_name': 'displayName',
            'endpoint_size': 'endpointSize',
            'nsg_ids': 'nsgIds'
        }

        self._freeform_tags = None
        self._defined_tags = None
        self._description = None
        self._display_name = None
        self._endpoint_size = None
        self._nsg_ids = None

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateEndpointDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateEndpointDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateEndpointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this UpdateEndpointDetails.
        Data Connectivity Management Registry description


        :return: The description of this UpdateEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateEndpointDetails.
        Data Connectivity Management Registry description


        :param description: The description of this UpdateEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateEndpointDetails.
        Data Connectivity Management Registry display name, registries can be renamed


        :return: The display_name of this UpdateEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateEndpointDetails.
        Data Connectivity Management Registry display name, registries can be renamed


        :param display_name: The display_name of this UpdateEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def endpoint_size(self):
        """
        Gets the endpoint_size of this UpdateEndpointDetails.
        Update Endpoint size for reverse connection capacity.


        :return: The endpoint_size of this UpdateEndpointDetails.
        :rtype: int
        """
        return self._endpoint_size

    @endpoint_size.setter
    def endpoint_size(self, endpoint_size):
        """
        Sets the endpoint_size of this UpdateEndpointDetails.
        Update Endpoint size for reverse connection capacity.


        :param endpoint_size: The endpoint_size of this UpdateEndpointDetails.
        :type: int
        """
        self._endpoint_size = endpoint_size

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateEndpointDetails.
        List of NSGs to which the Private Endpoint VNIC must be added.


        :return: The nsg_ids of this UpdateEndpointDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateEndpointDetails.
        List of NSGs to which the Private Endpoint VNIC must be added.


        :param nsg_ids: The nsg_ids of this UpdateEndpointDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
