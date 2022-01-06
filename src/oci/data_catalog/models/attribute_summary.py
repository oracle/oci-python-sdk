# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttributeSummary(object):
    """
    Summary of an entity attribute.
    """

    #: A constant which can be used with the lifecycle_state property of a AttributeSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AttributeSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AttributeSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AttributeSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AttributeSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AttributeSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AttributeSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AttributeSummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    #: A constant which can be used with the associated_rule_types property of a AttributeSummary.
    #: This constant has a value of "PRIMARYKEY"
    ASSOCIATED_RULE_TYPES_PRIMARYKEY = "PRIMARYKEY"

    #: A constant which can be used with the associated_rule_types property of a AttributeSummary.
    #: This constant has a value of "FOREIGNKEY"
    ASSOCIATED_RULE_TYPES_FOREIGNKEY = "FOREIGNKEY"

    #: A constant which can be used with the associated_rule_types property of a AttributeSummary.
    #: This constant has a value of "UNIQUEKEY"
    ASSOCIATED_RULE_TYPES_UNIQUEKEY = "UNIQUEKEY"

    def __init__(self, **kwargs):
        """
        Initializes a new AttributeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this AttributeSummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this AttributeSummary.
        :type display_name: str

        :param business_name:
            The value to assign to the business_name property of this AttributeSummary.
        :type business_name: str

        :param description:
            The value to assign to the description property of this AttributeSummary.
        :type description: str

        :param entity_key:
            The value to assign to the entity_key property of this AttributeSummary.
        :type entity_key: str

        :param external_key:
            The value to assign to the external_key property of this AttributeSummary.
        :type external_key: str

        :param length:
            The value to assign to the length property of this AttributeSummary.
        :type length: int

        :param position:
            The value to assign to the position property of this AttributeSummary.
        :type position: int

        :param precision:
            The value to assign to the precision property of this AttributeSummary.
        :type precision: int

        :param scale:
            The value to assign to the scale property of this AttributeSummary.
        :type scale: int

        :param is_nullable:
            The value to assign to the is_nullable property of this AttributeSummary.
        :type is_nullable: bool

        :param uri:
            The value to assign to the uri property of this AttributeSummary.
        :type uri: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AttributeSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this AttributeSummary.
        :type time_created: datetime

        :param external_data_type:
            The value to assign to the external_data_type property of this AttributeSummary.
        :type external_data_type: str

        :param type_key:
            The value to assign to the type_key property of this AttributeSummary.
        :type type_key: str

        :param min_collection_count:
            The value to assign to the min_collection_count property of this AttributeSummary.
        :type min_collection_count: int

        :param max_collection_count:
            The value to assign to the max_collection_count property of this AttributeSummary.
        :type max_collection_count: int

        :param datatype_entity_key:
            The value to assign to the datatype_entity_key property of this AttributeSummary.
        :type datatype_entity_key: str

        :param external_datatype_entity_key:
            The value to assign to the external_datatype_entity_key property of this AttributeSummary.
        :type external_datatype_entity_key: str

        :param parent_attribute_key:
            The value to assign to the parent_attribute_key property of this AttributeSummary.
        :type parent_attribute_key: str

        :param external_parent_attribute_key:
            The value to assign to the external_parent_attribute_key property of this AttributeSummary.
        :type external_parent_attribute_key: str

        :param path:
            The value to assign to the path property of this AttributeSummary.
        :type path: str

        :param custom_property_members:
            The value to assign to the custom_property_members property of this AttributeSummary.
        :type custom_property_members: list[oci.data_catalog.models.CustomPropertyGetUsage]

        :param associated_rule_types:
            The value to assign to the associated_rule_types property of this AttributeSummary.
            Allowed values for items in this list are: "PRIMARYKEY", "FOREIGNKEY", "UNIQUEKEY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type associated_rule_types: list[str]

        :param is_derived_attribute:
            The value to assign to the is_derived_attribute property of this AttributeSummary.
        :type is_derived_attribute: bool

        :param time_updated:
            The value to assign to the time_updated property of this AttributeSummary.
        :type time_updated: datetime

        :param properties:
            The value to assign to the properties property of this AttributeSummary.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'business_name': 'str',
            'description': 'str',
            'entity_key': 'str',
            'external_key': 'str',
            'length': 'int',
            'position': 'int',
            'precision': 'int',
            'scale': 'int',
            'is_nullable': 'bool',
            'uri': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'external_data_type': 'str',
            'type_key': 'str',
            'min_collection_count': 'int',
            'max_collection_count': 'int',
            'datatype_entity_key': 'str',
            'external_datatype_entity_key': 'str',
            'parent_attribute_key': 'str',
            'external_parent_attribute_key': 'str',
            'path': 'str',
            'custom_property_members': 'list[CustomPropertyGetUsage]',
            'associated_rule_types': 'list[str]',
            'is_derived_attribute': 'bool',
            'time_updated': 'datetime',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'business_name': 'businessName',
            'description': 'description',
            'entity_key': 'entityKey',
            'external_key': 'externalKey',
            'length': 'length',
            'position': 'position',
            'precision': 'precision',
            'scale': 'scale',
            'is_nullable': 'isNullable',
            'uri': 'uri',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'external_data_type': 'externalDataType',
            'type_key': 'typeKey',
            'min_collection_count': 'minCollectionCount',
            'max_collection_count': 'maxCollectionCount',
            'datatype_entity_key': 'datatypeEntityKey',
            'external_datatype_entity_key': 'externalDatatypeEntityKey',
            'parent_attribute_key': 'parentAttributeKey',
            'external_parent_attribute_key': 'externalParentAttributeKey',
            'path': 'path',
            'custom_property_members': 'customPropertyMembers',
            'associated_rule_types': 'associatedRuleTypes',
            'is_derived_attribute': 'isDerivedAttribute',
            'time_updated': 'timeUpdated',
            'properties': 'properties'
        }

        self._key = None
        self._display_name = None
        self._business_name = None
        self._description = None
        self._entity_key = None
        self._external_key = None
        self._length = None
        self._position = None
        self._precision = None
        self._scale = None
        self._is_nullable = None
        self._uri = None
        self._lifecycle_state = None
        self._time_created = None
        self._external_data_type = None
        self._type_key = None
        self._min_collection_count = None
        self._max_collection_count = None
        self._datatype_entity_key = None
        self._external_datatype_entity_key = None
        self._parent_attribute_key = None
        self._external_parent_attribute_key = None
        self._path = None
        self._custom_property_members = None
        self._associated_rule_types = None
        self._is_derived_attribute = None
        self._time_updated = None
        self._properties = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this AttributeSummary.
        Unique attribute key that is immutable.


        :return: The key of this AttributeSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this AttributeSummary.
        Unique attribute key that is immutable.


        :param key: The key of this AttributeSummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this AttributeSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this AttributeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AttributeSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this AttributeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def business_name(self):
        """
        Gets the business_name of this AttributeSummary.
        Optional user friendly business name of the attribute. If set, this supplements the harvested display name of the object.


        :return: The business_name of this AttributeSummary.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """
        Sets the business_name of this AttributeSummary.
        Optional user friendly business name of the attribute. If set, this supplements the harvested display name of the object.


        :param business_name: The business_name of this AttributeSummary.
        :type: str
        """
        self._business_name = business_name

    @property
    def description(self):
        """
        Gets the description of this AttributeSummary.
        Detailed description of the attribute.


        :return: The description of this AttributeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AttributeSummary.
        Detailed description of the attribute.


        :param description: The description of this AttributeSummary.
        :type: str
        """
        self._description = description

    @property
    def entity_key(self):
        """
        Gets the entity_key of this AttributeSummary.
        The unique key of the parent entity.


        :return: The entity_key of this AttributeSummary.
        :rtype: str
        """
        return self._entity_key

    @entity_key.setter
    def entity_key(self, entity_key):
        """
        Sets the entity_key of this AttributeSummary.
        The unique key of the parent entity.


        :param entity_key: The entity_key of this AttributeSummary.
        :type: str
        """
        self._entity_key = entity_key

    @property
    def external_key(self):
        """
        Gets the external_key of this AttributeSummary.
        Unique external key of this attribute in the external source system.


        :return: The external_key of this AttributeSummary.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this AttributeSummary.
        Unique external key of this attribute in the external source system.


        :param external_key: The external_key of this AttributeSummary.
        :type: str
        """
        self._external_key = external_key

    @property
    def length(self):
        """
        Gets the length of this AttributeSummary.
        Max allowed length of the attribute value.


        :return: The length of this AttributeSummary.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this AttributeSummary.
        Max allowed length of the attribute value.


        :param length: The length of this AttributeSummary.
        :type: int
        """
        self._length = length

    @property
    def position(self):
        """
        Gets the position of this AttributeSummary.
        Position of the attribute in the record definition.


        :return: The position of this AttributeSummary.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this AttributeSummary.
        Position of the attribute in the record definition.


        :param position: The position of this AttributeSummary.
        :type: int
        """
        self._position = position

    @property
    def precision(self):
        """
        Gets the precision of this AttributeSummary.
        Precision of the attribute value usually applies to float data type.


        :return: The precision of this AttributeSummary.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """
        Sets the precision of this AttributeSummary.
        Precision of the attribute value usually applies to float data type.


        :param precision: The precision of this AttributeSummary.
        :type: int
        """
        self._precision = precision

    @property
    def scale(self):
        """
        Gets the scale of this AttributeSummary.
        Scale of the attribute value usually applies to float data type.


        :return: The scale of this AttributeSummary.
        :rtype: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this AttributeSummary.
        Scale of the attribute value usually applies to float data type.


        :param scale: The scale of this AttributeSummary.
        :type: int
        """
        self._scale = scale

    @property
    def is_nullable(self):
        """
        Gets the is_nullable of this AttributeSummary.
        Property that identifies if this attribute can be assigned null values.


        :return: The is_nullable of this AttributeSummary.
        :rtype: bool
        """
        return self._is_nullable

    @is_nullable.setter
    def is_nullable(self, is_nullable):
        """
        Sets the is_nullable of this AttributeSummary.
        Property that identifies if this attribute can be assigned null values.


        :param is_nullable: The is_nullable of this AttributeSummary.
        :type: bool
        """
        self._is_nullable = is_nullable

    @property
    def uri(self):
        """
        Gets the uri of this AttributeSummary.
        URI to the attribute instance in the API.


        :return: The uri of this AttributeSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this AttributeSummary.
        URI to the attribute instance in the API.


        :param uri: The uri of this AttributeSummary.
        :type: str
        """
        self._uri = uri

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AttributeSummary.
        State of the attribute.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AttributeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AttributeSummary.
        State of the attribute.


        :param lifecycle_state: The lifecycle_state of this AttributeSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this AttributeSummary.
        The date and time the attribute was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this AttributeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AttributeSummary.
        The date and time the attribute was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this AttributeSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def external_data_type(self):
        """
        Gets the external_data_type of this AttributeSummary.
        Data type of the attribute as defined in the external source system.


        :return: The external_data_type of this AttributeSummary.
        :rtype: str
        """
        return self._external_data_type

    @external_data_type.setter
    def external_data_type(self, external_data_type):
        """
        Sets the external_data_type of this AttributeSummary.
        Data type of the attribute as defined in the external source system.


        :param external_data_type: The external_data_type of this AttributeSummary.
        :type: str
        """
        self._external_data_type = external_data_type

    @property
    def type_key(self):
        """
        Gets the type_key of this AttributeSummary.
        The type of the attribute. Type keys can be found via the '/types' endpoint.


        :return: The type_key of this AttributeSummary.
        :rtype: str
        """
        return self._type_key

    @type_key.setter
    def type_key(self, type_key):
        """
        Sets the type_key of this AttributeSummary.
        The type of the attribute. Type keys can be found via the '/types' endpoint.


        :param type_key: The type_key of this AttributeSummary.
        :type: str
        """
        self._type_key = type_key

    @property
    def min_collection_count(self):
        """
        Gets the min_collection_count of this AttributeSummary.
        The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.


        :return: The min_collection_count of this AttributeSummary.
        :rtype: int
        """
        return self._min_collection_count

    @min_collection_count.setter
    def min_collection_count(self, min_collection_count):
        """
        Sets the min_collection_count of this AttributeSummary.
        The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.


        :param min_collection_count: The min_collection_count of this AttributeSummary.
        :type: int
        """
        self._min_collection_count = min_collection_count

    @property
    def max_collection_count(self):
        """
        Gets the max_collection_count of this AttributeSummary.
        The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.
        For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\".
        Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in  Xml , maxItems in Json


        :return: The max_collection_count of this AttributeSummary.
        :rtype: int
        """
        return self._max_collection_count

    @max_collection_count.setter
    def max_collection_count(self, max_collection_count):
        """
        Sets the max_collection_count of this AttributeSummary.
        The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.
        For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\".
        Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in  Xml , maxItems in Json


        :param max_collection_count: The max_collection_count of this AttributeSummary.
        :type: int
        """
        self._max_collection_count = max_collection_count

    @property
    def datatype_entity_key(self):
        """
        Gets the datatype_entity_key of this AttributeSummary.
        Entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.


        :return: The datatype_entity_key of this AttributeSummary.
        :rtype: str
        """
        return self._datatype_entity_key

    @datatype_entity_key.setter
    def datatype_entity_key(self, datatype_entity_key):
        """
        Sets the datatype_entity_key of this AttributeSummary.
        Entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.


        :param datatype_entity_key: The datatype_entity_key of this AttributeSummary.
        :type: str
        """
        self._datatype_entity_key = datatype_entity_key

    @property
    def external_datatype_entity_key(self):
        """
        Gets the external_datatype_entity_key of this AttributeSummary.
        External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.


        :return: The external_datatype_entity_key of this AttributeSummary.
        :rtype: str
        """
        return self._external_datatype_entity_key

    @external_datatype_entity_key.setter
    def external_datatype_entity_key(self, external_datatype_entity_key):
        """
        Sets the external_datatype_entity_key of this AttributeSummary.
        External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.


        :param external_datatype_entity_key: The external_datatype_entity_key of this AttributeSummary.
        :type: str
        """
        self._external_datatype_entity_key = external_datatype_entity_key

    @property
    def parent_attribute_key(self):
        """
        Gets the parent_attribute_key of this AttributeSummary.
        Attribute key that represents the parent attribute of this attribute , applicable if the parent attribute is of complex datatype.


        :return: The parent_attribute_key of this AttributeSummary.
        :rtype: str
        """
        return self._parent_attribute_key

    @parent_attribute_key.setter
    def parent_attribute_key(self, parent_attribute_key):
        """
        Sets the parent_attribute_key of this AttributeSummary.
        Attribute key that represents the parent attribute of this attribute , applicable if the parent attribute is of complex datatype.


        :param parent_attribute_key: The parent_attribute_key of this AttributeSummary.
        :type: str
        """
        self._parent_attribute_key = parent_attribute_key

    @property
    def external_parent_attribute_key(self):
        """
        Gets the external_parent_attribute_key of this AttributeSummary.
        External attribute key that represents the parent attribute  of this attribute , applicable if the parent attribute is of complex type.


        :return: The external_parent_attribute_key of this AttributeSummary.
        :rtype: str
        """
        return self._external_parent_attribute_key

    @external_parent_attribute_key.setter
    def external_parent_attribute_key(self, external_parent_attribute_key):
        """
        Sets the external_parent_attribute_key of this AttributeSummary.
        External attribute key that represents the parent attribute  of this attribute , applicable if the parent attribute is of complex type.


        :param external_parent_attribute_key: The external_parent_attribute_key of this AttributeSummary.
        :type: str
        """
        self._external_parent_attribute_key = external_parent_attribute_key

    @property
    def path(self):
        """
        Gets the path of this AttributeSummary.
        Full path of the attribute.


        :return: The path of this AttributeSummary.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this AttributeSummary.
        Full path of the attribute.


        :param path: The path of this AttributeSummary.
        :type: str
        """
        self._path = path

    @property
    def custom_property_members(self):
        """
        Gets the custom_property_members of this AttributeSummary.
        The list of customized properties along with the values for this object


        :return: The custom_property_members of this AttributeSummary.
        :rtype: list[oci.data_catalog.models.CustomPropertyGetUsage]
        """
        return self._custom_property_members

    @custom_property_members.setter
    def custom_property_members(self, custom_property_members):
        """
        Sets the custom_property_members of this AttributeSummary.
        The list of customized properties along with the values for this object


        :param custom_property_members: The custom_property_members of this AttributeSummary.
        :type: list[oci.data_catalog.models.CustomPropertyGetUsage]
        """
        self._custom_property_members = custom_property_members

    @property
    def associated_rule_types(self):
        """
        Gets the associated_rule_types of this AttributeSummary.
        Rule types associated with attribute.

        Allowed values for items in this list are: "PRIMARYKEY", "FOREIGNKEY", "UNIQUEKEY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The associated_rule_types of this AttributeSummary.
        :rtype: list[str]
        """
        return self._associated_rule_types

    @associated_rule_types.setter
    def associated_rule_types(self, associated_rule_types):
        """
        Sets the associated_rule_types of this AttributeSummary.
        Rule types associated with attribute.


        :param associated_rule_types: The associated_rule_types of this AttributeSummary.
        :type: list[str]
        """
        allowed_values = ["PRIMARYKEY", "FOREIGNKEY", "UNIQUEKEY"]
        if associated_rule_types:
            associated_rule_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in associated_rule_types]
        self._associated_rule_types = associated_rule_types

    @property
    def is_derived_attribute(self):
        """
        Gets the is_derived_attribute of this AttributeSummary.
        Whether a column is derived or not.


        :return: The is_derived_attribute of this AttributeSummary.
        :rtype: bool
        """
        return self._is_derived_attribute

    @is_derived_attribute.setter
    def is_derived_attribute(self, is_derived_attribute):
        """
        Sets the is_derived_attribute of this AttributeSummary.
        Whether a column is derived or not.


        :param is_derived_attribute: The is_derived_attribute of this AttributeSummary.
        :type: bool
        """
        self._is_derived_attribute = is_derived_attribute

    @property
    def time_updated(self):
        """
        Gets the time_updated of this AttributeSummary.
        The last time that any change was made to the attribute. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this AttributeSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AttributeSummary.
        The last time that any change was made to the attribute. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this AttributeSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def properties(self):
        """
        Gets the properties of this AttributeSummary.
        A map of maps that contains the properties which are specific to the attribute type. Each attribute type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        attributes have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :return: The properties of this AttributeSummary.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this AttributeSummary.
        A map of maps that contains the properties which are specific to the attribute type. Each attribute type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        attributes have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :param properties: The properties of this AttributeSummary.
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
