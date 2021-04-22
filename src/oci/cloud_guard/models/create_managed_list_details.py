# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateManagedListDetails(object):
    """
    Create ManagedList
    """

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "CIDR_BLOCK"
    LIST_TYPE_CIDR_BLOCK = "CIDR_BLOCK"

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "USERS"
    LIST_TYPE_USERS = "USERS"

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "GROUPS"
    LIST_TYPE_GROUPS = "GROUPS"

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "IPV4ADDRESS"
    LIST_TYPE_IPV4_ADDRESS = "IPV4ADDRESS"

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "IPV6ADDRESS"
    LIST_TYPE_IPV6_ADDRESS = "IPV6ADDRESS"

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "RESOURCE_OCID"
    LIST_TYPE_RESOURCE_OCID = "RESOURCE_OCID"

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "REGION"
    LIST_TYPE_REGION = "REGION"

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "COUNTRY"
    LIST_TYPE_COUNTRY = "COUNTRY"

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "STATE"
    LIST_TYPE_STATE = "STATE"

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "CITY"
    LIST_TYPE_CITY = "CITY"

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "TAGS"
    LIST_TYPE_TAGS = "TAGS"

    #: A constant which can be used with the list_type property of a CreateManagedListDetails.
    #: This constant has a value of "GENERIC"
    LIST_TYPE_GENERIC = "GENERIC"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateManagedListDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateManagedListDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateManagedListDetails.
        :type compartment_id: str

        :param source_managed_list_id:
            The value to assign to the source_managed_list_id property of this CreateManagedListDetails.
        :type source_managed_list_id: str

        :param description:
            The value to assign to the description property of this CreateManagedListDetails.
        :type description: str

        :param list_type:
            The value to assign to the list_type property of this CreateManagedListDetails.
            Allowed values for this property are: "CIDR_BLOCK", "USERS", "GROUPS", "IPV4ADDRESS", "IPV6ADDRESS", "RESOURCE_OCID", "REGION", "COUNTRY", "STATE", "CITY", "TAGS", "GENERIC"
        :type list_type: str

        :param list_items:
            The value to assign to the list_items property of this CreateManagedListDetails.
        :type list_items: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateManagedListDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateManagedListDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'source_managed_list_id': 'str',
            'description': 'str',
            'list_type': 'str',
            'list_items': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'source_managed_list_id': 'sourceManagedListId',
            'description': 'description',
            'list_type': 'listType',
            'list_items': 'listItems',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._source_managed_list_id = None
        self._description = None
        self._list_type = None
        self._list_items = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateManagedListDetails.
        ManagedList display name


        :return: The display_name of this CreateManagedListDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateManagedListDetails.
        ManagedList display name


        :param display_name: The display_name of this CreateManagedListDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateManagedListDetails.
        Compartment Identifier


        :return: The compartment_id of this CreateManagedListDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateManagedListDetails.
        Compartment Identifier


        :param compartment_id: The compartment_id of this CreateManagedListDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def source_managed_list_id(self):
        """
        Gets the source_managed_list_id of this CreateManagedListDetails.
        OCID of the Source ManagedList


        :return: The source_managed_list_id of this CreateManagedListDetails.
        :rtype: str
        """
        return self._source_managed_list_id

    @source_managed_list_id.setter
    def source_managed_list_id(self, source_managed_list_id):
        """
        Sets the source_managed_list_id of this CreateManagedListDetails.
        OCID of the Source ManagedList


        :param source_managed_list_id: The source_managed_list_id of this CreateManagedListDetails.
        :type: str
        """
        self._source_managed_list_id = source_managed_list_id

    @property
    def description(self):
        """
        Gets the description of this CreateManagedListDetails.
        ManagedList description


        :return: The description of this CreateManagedListDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateManagedListDetails.
        ManagedList description


        :param description: The description of this CreateManagedListDetails.
        :type: str
        """
        self._description = description

    @property
    def list_type(self):
        """
        Gets the list_type of this CreateManagedListDetails.
        type of the list

        Allowed values for this property are: "CIDR_BLOCK", "USERS", "GROUPS", "IPV4ADDRESS", "IPV6ADDRESS", "RESOURCE_OCID", "REGION", "COUNTRY", "STATE", "CITY", "TAGS", "GENERIC"


        :return: The list_type of this CreateManagedListDetails.
        :rtype: str
        """
        return self._list_type

    @list_type.setter
    def list_type(self, list_type):
        """
        Sets the list_type of this CreateManagedListDetails.
        type of the list


        :param list_type: The list_type of this CreateManagedListDetails.
        :type: str
        """
        allowed_values = ["CIDR_BLOCK", "USERS", "GROUPS", "IPV4ADDRESS", "IPV6ADDRESS", "RESOURCE_OCID", "REGION", "COUNTRY", "STATE", "CITY", "TAGS", "GENERIC"]
        if not value_allowed_none_or_none_sentinel(list_type, allowed_values):
            raise ValueError(
                "Invalid value for `list_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._list_type = list_type

    @property
    def list_items(self):
        """
        Gets the list_items of this CreateManagedListDetails.
        List of ManagedListItem


        :return: The list_items of this CreateManagedListDetails.
        :rtype: list[str]
        """
        return self._list_items

    @list_items.setter
    def list_items(self, list_items):
        """
        Sets the list_items of this CreateManagedListDetails.
        List of ManagedListItem


        :param list_items: The list_items of this CreateManagedListDetails.
        :type: list[str]
        """
        self._list_items = list_items

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateManagedListDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateManagedListDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateManagedListDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateManagedListDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateManagedListDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateManagedListDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateManagedListDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateManagedListDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
