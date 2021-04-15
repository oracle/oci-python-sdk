# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConnectionDetails(object):
    """
    Properties used in connection update operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateConnectionDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateConnectionDetails.
        :type display_name: str

        :param custom_property_members:
            The value to assign to the custom_property_members property of this UpdateConnectionDetails.
        :type custom_property_members: list[oci.data_catalog.models.CustomPropertySetUsage]

        :param properties:
            The value to assign to the properties property of this UpdateConnectionDetails.
        :type properties: dict(str, dict(str, str))

        :param enc_properties:
            The value to assign to the enc_properties property of this UpdateConnectionDetails.
        :type enc_properties: dict(str, dict(str, str))

        :param is_default:
            The value to assign to the is_default property of this UpdateConnectionDetails.
        :type is_default: bool

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'custom_property_members': 'list[CustomPropertySetUsage]',
            'properties': 'dict(str, dict(str, str))',
            'enc_properties': 'dict(str, dict(str, str))',
            'is_default': 'bool'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'custom_property_members': 'customPropertyMembers',
            'properties': 'properties',
            'enc_properties': 'encProperties',
            'is_default': 'isDefault'
        }

        self._description = None
        self._display_name = None
        self._custom_property_members = None
        self._properties = None
        self._enc_properties = None
        self._is_default = None

    @property
    def description(self):
        """
        Gets the description of this UpdateConnectionDetails.
        A description of the connection.


        :return: The description of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateConnectionDetails.
        A description of the connection.


        :param description: The description of this UpdateConnectionDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateConnectionDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateConnectionDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def custom_property_members(self):
        """
        Gets the custom_property_members of this UpdateConnectionDetails.
        The list of customized properties along with the values for this object


        :return: The custom_property_members of this UpdateConnectionDetails.
        :rtype: list[oci.data_catalog.models.CustomPropertySetUsage]
        """
        return self._custom_property_members

    @custom_property_members.setter
    def custom_property_members(self, custom_property_members):
        """
        Sets the custom_property_members of this UpdateConnectionDetails.
        The list of customized properties along with the values for this object


        :param custom_property_members: The custom_property_members of this UpdateConnectionDetails.
        :type: list[oci.data_catalog.models.CustomPropertySetUsage]
        """
        self._custom_property_members = custom_property_members

    @property
    def properties(self):
        """
        Gets the properties of this UpdateConnectionDetails.
        A map of maps that contains the properties which are specific to the connection type. Each connection type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        connections have required properties within the \"default\" category. To determine the set of optional and
        required properties for a connection type, a query can be done on '/types?type=connection' that returns a
        collection of all connection types. The appropriate connection type, which will include definitions of all
        of it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"username\": \"user1\"}}}`


        :return: The properties of this UpdateConnectionDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this UpdateConnectionDetails.
        A map of maps that contains the properties which are specific to the connection type. Each connection type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        connections have required properties within the \"default\" category. To determine the set of optional and
        required properties for a connection type, a query can be done on '/types?type=connection' that returns a
        collection of all connection types. The appropriate connection type, which will include definitions of all
        of it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"username\": \"user1\"}}}`


        :param properties: The properties of this UpdateConnectionDetails.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    @property
    def enc_properties(self):
        """
        Gets the enc_properties of this UpdateConnectionDetails.
        A map of maps that contains the encrypted values for sensitive properties which are specific to the
        connection type. Each connection type definition defines it's set of required and optional properties.
        The map keys are category names and the values are maps of property name to property value. Every property is
        contained inside of a category. Most connections have required properties within the \"default\" category.
        To determine the set of optional and required properties for a connection type, a query can be done
        on '/types?type=connection' that returns a collection of all connection types. The appropriate connection
        type, which will include definitions of all of it's properties, can be identified from this collection.
        Example: `{\"encProperties\": { \"default\": { \"password\": \"example-password\"}}}`


        :return: The enc_properties of this UpdateConnectionDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._enc_properties

    @enc_properties.setter
    def enc_properties(self, enc_properties):
        """
        Sets the enc_properties of this UpdateConnectionDetails.
        A map of maps that contains the encrypted values for sensitive properties which are specific to the
        connection type. Each connection type definition defines it's set of required and optional properties.
        The map keys are category names and the values are maps of property name to property value. Every property is
        contained inside of a category. Most connections have required properties within the \"default\" category.
        To determine the set of optional and required properties for a connection type, a query can be done
        on '/types?type=connection' that returns a collection of all connection types. The appropriate connection
        type, which will include definitions of all of it's properties, can be identified from this collection.
        Example: `{\"encProperties\": { \"default\": { \"password\": \"example-password\"}}}`


        :param enc_properties: The enc_properties of this UpdateConnectionDetails.
        :type: dict(str, dict(str, str))
        """
        self._enc_properties = enc_properties

    @property
    def is_default(self):
        """
        Gets the is_default of this UpdateConnectionDetails.
        Indicates whether this connection is the default connection.


        :return: The is_default of this UpdateConnectionDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this UpdateConnectionDetails.
        Indicates whether this connection is the default connection.


        :param is_default: The is_default of this UpdateConnectionDetails.
        :type: bool
        """
        self._is_default = is_default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
