# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectionDetails(object):
    """
    Properties used in connection create operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateConnectionDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateConnectionDetails.
        :type display_name: str

        :param type_key:
            The value to assign to the type_key property of this CreateConnectionDetails.
        :type type_key: str

        :param custom_property_members:
            The value to assign to the custom_property_members property of this CreateConnectionDetails.
        :type custom_property_members: list[oci.data_catalog.models.CustomPropertySetUsage]

        :param properties:
            The value to assign to the properties property of this CreateConnectionDetails.
        :type properties: dict(str, dict(str, str))

        :param enc_properties:
            The value to assign to the enc_properties property of this CreateConnectionDetails.
        :type enc_properties: dict(str, dict(str, str))

        :param is_default:
            The value to assign to the is_default property of this CreateConnectionDetails.
        :type is_default: bool

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'type_key': 'str',
            'custom_property_members': 'list[CustomPropertySetUsage]',
            'properties': 'dict(str, dict(str, str))',
            'enc_properties': 'dict(str, dict(str, str))',
            'is_default': 'bool'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'type_key': 'typeKey',
            'custom_property_members': 'customPropertyMembers',
            'properties': 'properties',
            'enc_properties': 'encProperties',
            'is_default': 'isDefault'
        }

        self._description = None
        self._display_name = None
        self._type_key = None
        self._custom_property_members = None
        self._properties = None
        self._enc_properties = None
        self._is_default = None

    @property
    def description(self):
        """
        Gets the description of this CreateConnectionDetails.
        A description of the connection.


        :return: The description of this CreateConnectionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateConnectionDetails.
        A description of the connection.


        :param description: The description of this CreateConnectionDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateConnectionDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateConnectionDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def type_key(self):
        """
        **[Required]** Gets the type_key of this CreateConnectionDetails.
        The key of the object type. Type key's can be found via the '/types' endpoint.


        :return: The type_key of this CreateConnectionDetails.
        :rtype: str
        """
        return self._type_key

    @type_key.setter
    def type_key(self, type_key):
        """
        Sets the type_key of this CreateConnectionDetails.
        The key of the object type. Type key's can be found via the '/types' endpoint.


        :param type_key: The type_key of this CreateConnectionDetails.
        :type: str
        """
        self._type_key = type_key

    @property
    def custom_property_members(self):
        """
        Gets the custom_property_members of this CreateConnectionDetails.
        The list of customized properties along with the values for this object


        :return: The custom_property_members of this CreateConnectionDetails.
        :rtype: list[oci.data_catalog.models.CustomPropertySetUsage]
        """
        return self._custom_property_members

    @custom_property_members.setter
    def custom_property_members(self, custom_property_members):
        """
        Sets the custom_property_members of this CreateConnectionDetails.
        The list of customized properties along with the values for this object


        :param custom_property_members: The custom_property_members of this CreateConnectionDetails.
        :type: list[oci.data_catalog.models.CustomPropertySetUsage]
        """
        self._custom_property_members = custom_property_members

    @property
    def properties(self):
        """
        **[Required]** Gets the properties of this CreateConnectionDetails.
        A map of maps that contains the properties which are specific to the connection type. Each connection type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        connections have required properties within the \"default\" category. To determine the set of optional and
        required properties for a connection type, a query can be done on '/types?type=connection' that returns a
        collection of all connection types. The appropriate connection type, which will include definitions of all
        of it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"username\": \"user1\"}}}`


        :return: The properties of this CreateConnectionDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CreateConnectionDetails.
        A map of maps that contains the properties which are specific to the connection type. Each connection type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        connections have required properties within the \"default\" category. To determine the set of optional and
        required properties for a connection type, a query can be done on '/types?type=connection' that returns a
        collection of all connection types. The appropriate connection type, which will include definitions of all
        of it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"username\": \"user1\"}}}`


        :param properties: The properties of this CreateConnectionDetails.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    @property
    def enc_properties(self):
        """
        Gets the enc_properties of this CreateConnectionDetails.
        A map of maps that contains the encrypted values for sensitive properties which are specific to the
        connection type. Each connection type definition defines it's set of required and optional properties.
        The map keys are category names and the values are maps of property name to property value. Every property is
        contained inside of a category. Most connections have required properties within the \"default\" category.
        To determine the set of optional and required properties for a connection type, a query can be done
        on '/types?type=connection' that returns a collection of all connection types. The appropriate connection
        type, which will include definitions of all of it's properties, can be identified from this collection.
        Example: `{\"encProperties\": { \"default\": { \"password\": \"example-password\"}}}`


        :return: The enc_properties of this CreateConnectionDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._enc_properties

    @enc_properties.setter
    def enc_properties(self, enc_properties):
        """
        Sets the enc_properties of this CreateConnectionDetails.
        A map of maps that contains the encrypted values for sensitive properties which are specific to the
        connection type. Each connection type definition defines it's set of required and optional properties.
        The map keys are category names and the values are maps of property name to property value. Every property is
        contained inside of a category. Most connections have required properties within the \"default\" category.
        To determine the set of optional and required properties for a connection type, a query can be done
        on '/types?type=connection' that returns a collection of all connection types. The appropriate connection
        type, which will include definitions of all of it's properties, can be identified from this collection.
        Example: `{\"encProperties\": { \"default\": { \"password\": \"example-password\"}}}`


        :param enc_properties: The enc_properties of this CreateConnectionDetails.
        :type: dict(str, dict(str, str))
        """
        self._enc_properties = enc_properties

    @property
    def is_default(self):
        """
        Gets the is_default of this CreateConnectionDetails.
        Indicates whether this connection is the default connection. The first connection of a data asset defaults
        to being the default, subsequent connections default to not being the default. If a default connection already
        exists, then trying to create a connection as the default will fail. In this case the default connection would
        need to be updated not to be the default and then the new connection can then be created as the default.


        :return: The is_default of this CreateConnectionDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this CreateConnectionDetails.
        Indicates whether this connection is the default connection. The first connection of a data asset defaults
        to being the default, subsequent connections default to not being the default. If a default connection already
        exists, then trying to create a connection as the default will fail. In this case the default connection would
        need to be updated not to be the default and then the new connection can then be created as the default.


        :param is_default: The is_default of this CreateConnectionDetails.
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
