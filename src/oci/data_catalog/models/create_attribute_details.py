# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAttributeDetails(object):
    """
    Properties used in attribute create operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAttributeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateAttributeDetails.
        :type display_name: str

        :param business_name:
            The value to assign to the business_name property of this CreateAttributeDetails.
        :type business_name: str

        :param description:
            The value to assign to the description property of this CreateAttributeDetails.
        :type description: str

        :param external_data_type:
            The value to assign to the external_data_type property of this CreateAttributeDetails.
        :type external_data_type: str

        :param is_incremental_data:
            The value to assign to the is_incremental_data property of this CreateAttributeDetails.
        :type is_incremental_data: bool

        :param is_nullable:
            The value to assign to the is_nullable property of this CreateAttributeDetails.
        :type is_nullable: bool

        :param length:
            The value to assign to the length property of this CreateAttributeDetails.
        :type length: int

        :param position:
            The value to assign to the position property of this CreateAttributeDetails.
        :type position: int

        :param precision:
            The value to assign to the precision property of this CreateAttributeDetails.
        :type precision: int

        :param scale:
            The value to assign to the scale property of this CreateAttributeDetails.
        :type scale: int

        :param time_external:
            The value to assign to the time_external property of this CreateAttributeDetails.
        :type time_external: datetime

        :param min_collection_count:
            The value to assign to the min_collection_count property of this CreateAttributeDetails.
        :type min_collection_count: int

        :param max_collection_count:
            The value to assign to the max_collection_count property of this CreateAttributeDetails.
        :type max_collection_count: int

        :param external_datatype_entity_key:
            The value to assign to the external_datatype_entity_key property of this CreateAttributeDetails.
        :type external_datatype_entity_key: str

        :param external_parent_attribute_key:
            The value to assign to the external_parent_attribute_key property of this CreateAttributeDetails.
        :type external_parent_attribute_key: str

        :param custom_property_members:
            The value to assign to the custom_property_members property of this CreateAttributeDetails.
        :type custom_property_members: list[oci.data_catalog.models.CustomPropertySetUsage]

        :param properties:
            The value to assign to the properties property of this CreateAttributeDetails.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'display_name': 'str',
            'business_name': 'str',
            'description': 'str',
            'external_data_type': 'str',
            'is_incremental_data': 'bool',
            'is_nullable': 'bool',
            'length': 'int',
            'position': 'int',
            'precision': 'int',
            'scale': 'int',
            'time_external': 'datetime',
            'min_collection_count': 'int',
            'max_collection_count': 'int',
            'external_datatype_entity_key': 'str',
            'external_parent_attribute_key': 'str',
            'custom_property_members': 'list[CustomPropertySetUsage]',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'business_name': 'businessName',
            'description': 'description',
            'external_data_type': 'externalDataType',
            'is_incremental_data': 'isIncrementalData',
            'is_nullable': 'isNullable',
            'length': 'length',
            'position': 'position',
            'precision': 'precision',
            'scale': 'scale',
            'time_external': 'timeExternal',
            'min_collection_count': 'minCollectionCount',
            'max_collection_count': 'maxCollectionCount',
            'external_datatype_entity_key': 'externalDatatypeEntityKey',
            'external_parent_attribute_key': 'externalParentAttributeKey',
            'custom_property_members': 'customPropertyMembers',
            'properties': 'properties'
        }

        self._display_name = None
        self._business_name = None
        self._description = None
        self._external_data_type = None
        self._is_incremental_data = None
        self._is_nullable = None
        self._length = None
        self._position = None
        self._precision = None
        self._scale = None
        self._time_external = None
        self._min_collection_count = None
        self._max_collection_count = None
        self._external_datatype_entity_key = None
        self._external_parent_attribute_key = None
        self._custom_property_members = None
        self._properties = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateAttributeDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateAttributeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAttributeDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateAttributeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def business_name(self):
        """
        Gets the business_name of this CreateAttributeDetails.
        Optional user friendly business name of the attribute. If set, this supplements the harvested display name of the object.


        :return: The business_name of this CreateAttributeDetails.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """
        Sets the business_name of this CreateAttributeDetails.
        Optional user friendly business name of the attribute. If set, this supplements the harvested display name of the object.


        :param business_name: The business_name of this CreateAttributeDetails.
        :type: str
        """
        self._business_name = business_name

    @property
    def description(self):
        """
        Gets the description of this CreateAttributeDetails.
        Detailed description of the attribute.


        :return: The description of this CreateAttributeDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAttributeDetails.
        Detailed description of the attribute.


        :param description: The description of this CreateAttributeDetails.
        :type: str
        """
        self._description = description

    @property
    def external_data_type(self):
        """
        **[Required]** Gets the external_data_type of this CreateAttributeDetails.
        Data type of the attribute as defined in the external system.


        :return: The external_data_type of this CreateAttributeDetails.
        :rtype: str
        """
        return self._external_data_type

    @external_data_type.setter
    def external_data_type(self, external_data_type):
        """
        Sets the external_data_type of this CreateAttributeDetails.
        Data type of the attribute as defined in the external system.


        :param external_data_type: The external_data_type of this CreateAttributeDetails.
        :type: str
        """
        self._external_data_type = external_data_type

    @property
    def is_incremental_data(self):
        """
        Gets the is_incremental_data of this CreateAttributeDetails.
        Property that identifies if this attribute can be used as a watermark to extract incremental data.


        :return: The is_incremental_data of this CreateAttributeDetails.
        :rtype: bool
        """
        return self._is_incremental_data

    @is_incremental_data.setter
    def is_incremental_data(self, is_incremental_data):
        """
        Sets the is_incremental_data of this CreateAttributeDetails.
        Property that identifies if this attribute can be used as a watermark to extract incremental data.


        :param is_incremental_data: The is_incremental_data of this CreateAttributeDetails.
        :type: bool
        """
        self._is_incremental_data = is_incremental_data

    @property
    def is_nullable(self):
        """
        Gets the is_nullable of this CreateAttributeDetails.
        Property that identifies if this attribute can be assigned null values.


        :return: The is_nullable of this CreateAttributeDetails.
        :rtype: bool
        """
        return self._is_nullable

    @is_nullable.setter
    def is_nullable(self, is_nullable):
        """
        Sets the is_nullable of this CreateAttributeDetails.
        Property that identifies if this attribute can be assigned null values.


        :param is_nullable: The is_nullable of this CreateAttributeDetails.
        :type: bool
        """
        self._is_nullable = is_nullable

    @property
    def length(self):
        """
        Gets the length of this CreateAttributeDetails.
        Max allowed length of the attribute value.


        :return: The length of this CreateAttributeDetails.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this CreateAttributeDetails.
        Max allowed length of the attribute value.


        :param length: The length of this CreateAttributeDetails.
        :type: int
        """
        self._length = length

    @property
    def position(self):
        """
        Gets the position of this CreateAttributeDetails.
        Position of the attribute in the record definition.


        :return: The position of this CreateAttributeDetails.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this CreateAttributeDetails.
        Position of the attribute in the record definition.


        :param position: The position of this CreateAttributeDetails.
        :type: int
        """
        self._position = position

    @property
    def precision(self):
        """
        Gets the precision of this CreateAttributeDetails.
        Precision of the attribute value usually applies to float data type.


        :return: The precision of this CreateAttributeDetails.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """
        Sets the precision of this CreateAttributeDetails.
        Precision of the attribute value usually applies to float data type.


        :param precision: The precision of this CreateAttributeDetails.
        :type: int
        """
        self._precision = precision

    @property
    def scale(self):
        """
        Gets the scale of this CreateAttributeDetails.
        Scale of the attribute value usually applies to float data type.


        :return: The scale of this CreateAttributeDetails.
        :rtype: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this CreateAttributeDetails.
        Scale of the attribute value usually applies to float data type.


        :param scale: The scale of this CreateAttributeDetails.
        :type: int
        """
        self._scale = scale

    @property
    def time_external(self):
        """
        **[Required]** Gets the time_external of this CreateAttributeDetails.
        Last modified timestamp of this object in the external system.


        :return: The time_external of this CreateAttributeDetails.
        :rtype: datetime
        """
        return self._time_external

    @time_external.setter
    def time_external(self, time_external):
        """
        Sets the time_external of this CreateAttributeDetails.
        Last modified timestamp of this object in the external system.


        :param time_external: The time_external of this CreateAttributeDetails.
        :type: datetime
        """
        self._time_external = time_external

    @property
    def min_collection_count(self):
        """
        Gets the min_collection_count of this CreateAttributeDetails.
        The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.


        :return: The min_collection_count of this CreateAttributeDetails.
        :rtype: int
        """
        return self._min_collection_count

    @min_collection_count.setter
    def min_collection_count(self, min_collection_count):
        """
        Sets the min_collection_count of this CreateAttributeDetails.
        The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.


        :param min_collection_count: The min_collection_count of this CreateAttributeDetails.
        :type: int
        """
        self._min_collection_count = min_collection_count

    @property
    def max_collection_count(self):
        """
        Gets the max_collection_count of this CreateAttributeDetails.
        The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.
        For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\".
        Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in  Xml , maxItems in Json


        :return: The max_collection_count of this CreateAttributeDetails.
        :rtype: int
        """
        return self._max_collection_count

    @max_collection_count.setter
    def max_collection_count(self, max_collection_count):
        """
        Sets the max_collection_count of this CreateAttributeDetails.
        The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.
        For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\".
        Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in  Xml , maxItems in Json


        :param max_collection_count: The max_collection_count of this CreateAttributeDetails.
        :type: int
        """
        self._max_collection_count = max_collection_count

    @property
    def external_datatype_entity_key(self):
        """
        Gets the external_datatype_entity_key of this CreateAttributeDetails.
        External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.


        :return: The external_datatype_entity_key of this CreateAttributeDetails.
        :rtype: str
        """
        return self._external_datatype_entity_key

    @external_datatype_entity_key.setter
    def external_datatype_entity_key(self, external_datatype_entity_key):
        """
        Sets the external_datatype_entity_key of this CreateAttributeDetails.
        External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.


        :param external_datatype_entity_key: The external_datatype_entity_key of this CreateAttributeDetails.
        :type: str
        """
        self._external_datatype_entity_key = external_datatype_entity_key

    @property
    def external_parent_attribute_key(self):
        """
        Gets the external_parent_attribute_key of this CreateAttributeDetails.
        External attribute key that represents the parent attribute  of this attribute , applicable if the parent attribute is of complex type.


        :return: The external_parent_attribute_key of this CreateAttributeDetails.
        :rtype: str
        """
        return self._external_parent_attribute_key

    @external_parent_attribute_key.setter
    def external_parent_attribute_key(self, external_parent_attribute_key):
        """
        Sets the external_parent_attribute_key of this CreateAttributeDetails.
        External attribute key that represents the parent attribute  of this attribute , applicable if the parent attribute is of complex type.


        :param external_parent_attribute_key: The external_parent_attribute_key of this CreateAttributeDetails.
        :type: str
        """
        self._external_parent_attribute_key = external_parent_attribute_key

    @property
    def custom_property_members(self):
        """
        Gets the custom_property_members of this CreateAttributeDetails.
        The list of customized properties along with the values for this object


        :return: The custom_property_members of this CreateAttributeDetails.
        :rtype: list[oci.data_catalog.models.CustomPropertySetUsage]
        """
        return self._custom_property_members

    @custom_property_members.setter
    def custom_property_members(self, custom_property_members):
        """
        Sets the custom_property_members of this CreateAttributeDetails.
        The list of customized properties along with the values for this object


        :param custom_property_members: The custom_property_members of this CreateAttributeDetails.
        :type: list[oci.data_catalog.models.CustomPropertySetUsage]
        """
        self._custom_property_members = custom_property_members

    @property
    def properties(self):
        """
        Gets the properties of this CreateAttributeDetails.
        A map of maps that contains the properties which are specific to the attribute type. Each attribute type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        attributes have required properties within the \"default\" category. To determine the set of required and
        optional properties for an attribute type, a query can be done on '/types?type=attribute' that returns a
        collection of all attribute types. The appropriate attribute type, which will include definitions of all
        of it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :return: The properties of this CreateAttributeDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CreateAttributeDetails.
        A map of maps that contains the properties which are specific to the attribute type. Each attribute type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        attributes have required properties within the \"default\" category. To determine the set of required and
        optional properties for an attribute type, a query can be done on '/types?type=attribute' that returns a
        collection of all attribute types. The appropriate attribute type, which will include definitions of all
        of it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :param properties: The properties of this CreateAttributeDetails.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
