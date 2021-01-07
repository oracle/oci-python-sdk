# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Attribute(object):
    """
    Details of an entity attribute. An attribute of a data entity describing an item of data,
    with a name and data type. Synonymous with 'column' in a database.
    """

    #: A constant which can be used with the lifecycle_state property of a Attribute.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Attribute.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Attribute.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Attribute.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Attribute.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Attribute.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Attribute.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Attribute.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    #: A constant which can be used with the associated_rule_types property of a Attribute.
    #: This constant has a value of "PRIMARYKEY"
    ASSOCIATED_RULE_TYPES_PRIMARYKEY = "PRIMARYKEY"

    #: A constant which can be used with the associated_rule_types property of a Attribute.
    #: This constant has a value of "FOREIGNKEY"
    ASSOCIATED_RULE_TYPES_FOREIGNKEY = "FOREIGNKEY"

    #: A constant which can be used with the associated_rule_types property of a Attribute.
    #: This constant has a value of "UNIQUEKEY"
    ASSOCIATED_RULE_TYPES_UNIQUEKEY = "UNIQUEKEY"

    def __init__(self, **kwargs):
        """
        Initializes a new Attribute object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Attribute.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this Attribute.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Attribute.
        :type description: str

        :param entity_key:
            The value to assign to the entity_key property of this Attribute.
        :type entity_key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Attribute.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Attribute.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Attribute.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this Attribute.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this Attribute.
        :type updated_by_id: str

        :param external_data_type:
            The value to assign to the external_data_type property of this Attribute.
        :type external_data_type: str

        :param external_key:
            The value to assign to the external_key property of this Attribute.
        :type external_key: str

        :param is_incremental_data:
            The value to assign to the is_incremental_data property of this Attribute.
        :type is_incremental_data: bool

        :param is_nullable:
            The value to assign to the is_nullable property of this Attribute.
        :type is_nullable: bool

        :param min_collection_count:
            The value to assign to the min_collection_count property of this Attribute.
        :type min_collection_count: int

        :param max_collection_count:
            The value to assign to the max_collection_count property of this Attribute.
        :type max_collection_count: int

        :param datatype_entity_key:
            The value to assign to the datatype_entity_key property of this Attribute.
        :type datatype_entity_key: str

        :param external_datatype_entity_key:
            The value to assign to the external_datatype_entity_key property of this Attribute.
        :type external_datatype_entity_key: str

        :param parent_attribute_key:
            The value to assign to the parent_attribute_key property of this Attribute.
        :type parent_attribute_key: str

        :param external_parent_attribute_key:
            The value to assign to the external_parent_attribute_key property of this Attribute.
        :type external_parent_attribute_key: str

        :param length:
            The value to assign to the length property of this Attribute.
        :type length: int

        :param position:
            The value to assign to the position property of this Attribute.
        :type position: int

        :param precision:
            The value to assign to the precision property of this Attribute.
        :type precision: int

        :param scale:
            The value to assign to the scale property of this Attribute.
        :type scale: int

        :param time_external:
            The value to assign to the time_external property of this Attribute.
        :type time_external: datetime

        :param uri:
            The value to assign to the uri property of this Attribute.
        :type uri: str

        :param path:
            The value to assign to the path property of this Attribute.
        :type path: str

        :param custom_property_members:
            The value to assign to the custom_property_members property of this Attribute.
        :type custom_property_members: list[oci.data_catalog.models.CustomPropertyGetUsage]

        :param properties:
            The value to assign to the properties property of this Attribute.
        :type properties: dict(str, dict(str, str))

        :param associated_rule_types:
            The value to assign to the associated_rule_types property of this Attribute.
            Allowed values for items in this list are: "PRIMARYKEY", "FOREIGNKEY", "UNIQUEKEY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type associated_rule_types: list[str]

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'entity_key': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'external_data_type': 'str',
            'external_key': 'str',
            'is_incremental_data': 'bool',
            'is_nullable': 'bool',
            'min_collection_count': 'int',
            'max_collection_count': 'int',
            'datatype_entity_key': 'str',
            'external_datatype_entity_key': 'str',
            'parent_attribute_key': 'str',
            'external_parent_attribute_key': 'str',
            'length': 'int',
            'position': 'int',
            'precision': 'int',
            'scale': 'int',
            'time_external': 'datetime',
            'uri': 'str',
            'path': 'str',
            'custom_property_members': 'list[CustomPropertyGetUsage]',
            'properties': 'dict(str, dict(str, str))',
            'associated_rule_types': 'list[str]'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'entity_key': 'entityKey',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'external_data_type': 'externalDataType',
            'external_key': 'externalKey',
            'is_incremental_data': 'isIncrementalData',
            'is_nullable': 'isNullable',
            'min_collection_count': 'minCollectionCount',
            'max_collection_count': 'maxCollectionCount',
            'datatype_entity_key': 'datatypeEntityKey',
            'external_datatype_entity_key': 'externalDatatypeEntityKey',
            'parent_attribute_key': 'parentAttributeKey',
            'external_parent_attribute_key': 'externalParentAttributeKey',
            'length': 'length',
            'position': 'position',
            'precision': 'precision',
            'scale': 'scale',
            'time_external': 'timeExternal',
            'uri': 'uri',
            'path': 'path',
            'custom_property_members': 'customPropertyMembers',
            'properties': 'properties',
            'associated_rule_types': 'associatedRuleTypes'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._entity_key = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None
        self._external_data_type = None
        self._external_key = None
        self._is_incremental_data = None
        self._is_nullable = None
        self._min_collection_count = None
        self._max_collection_count = None
        self._datatype_entity_key = None
        self._external_datatype_entity_key = None
        self._parent_attribute_key = None
        self._external_parent_attribute_key = None
        self._length = None
        self._position = None
        self._precision = None
        self._scale = None
        self._time_external = None
        self._uri = None
        self._path = None
        self._custom_property_members = None
        self._properties = None
        self._associated_rule_types = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Attribute.
        Unique attribute key that is immutable.


        :return: The key of this Attribute.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Attribute.
        Unique attribute key that is immutable.


        :param key: The key of this Attribute.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this Attribute.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Attribute.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Attribute.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Attribute.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Attribute.
        Detailed description of the attribute.


        :return: The description of this Attribute.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Attribute.
        Detailed description of the attribute.


        :param description: The description of this Attribute.
        :type: str
        """
        self._description = description

    @property
    def entity_key(self):
        """
        Gets the entity_key of this Attribute.
        The unique key of the parent entity.


        :return: The entity_key of this Attribute.
        :rtype: str
        """
        return self._entity_key

    @entity_key.setter
    def entity_key(self, entity_key):
        """
        Sets the entity_key of this Attribute.
        The unique key of the parent entity.


        :param entity_key: The entity_key of this Attribute.
        :type: str
        """
        self._entity_key = entity_key

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Attribute.
        State of the attribute.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Attribute.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Attribute.
        State of the attribute.


        :param lifecycle_state: The lifecycle_state of this Attribute.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Attribute.
        The date and time the attribute was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Attribute.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Attribute.
        The date and time the attribute was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Attribute.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Attribute.
        The last time that any change was made to the attribute. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Attribute.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Attribute.
        The last time that any change was made to the attribute. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Attribute.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this Attribute.
        OCID of the user who created this attribute in the data catalog.


        :return: The created_by_id of this Attribute.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this Attribute.
        OCID of the user who created this attribute in the data catalog.


        :param created_by_id: The created_by_id of this Attribute.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this Attribute.
        OCID of the user who modified this attribute in the data catalog.


        :return: The updated_by_id of this Attribute.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this Attribute.
        OCID of the user who modified this attribute in the data catalog.


        :param updated_by_id: The updated_by_id of this Attribute.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def external_data_type(self):
        """
        Gets the external_data_type of this Attribute.
        Data type of the attribute as defined in the external system. Type mapping across systems can be achieved
        through term associations across domains in the ontology. The attribute can also be tagged to the datatype in
        the domain ontology to resolve any ambiguity arising from type name similarity that can occur with user
        defined types.


        :return: The external_data_type of this Attribute.
        :rtype: str
        """
        return self._external_data_type

    @external_data_type.setter
    def external_data_type(self, external_data_type):
        """
        Sets the external_data_type of this Attribute.
        Data type of the attribute as defined in the external system. Type mapping across systems can be achieved
        through term associations across domains in the ontology. The attribute can also be tagged to the datatype in
        the domain ontology to resolve any ambiguity arising from type name similarity that can occur with user
        defined types.


        :param external_data_type: The external_data_type of this Attribute.
        :type: str
        """
        self._external_data_type = external_data_type

    @property
    def external_key(self):
        """
        Gets the external_key of this Attribute.
        Unique external key of this attribute in the external source system.


        :return: The external_key of this Attribute.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this Attribute.
        Unique external key of this attribute in the external source system.


        :param external_key: The external_key of this Attribute.
        :type: str
        """
        self._external_key = external_key

    @property
    def is_incremental_data(self):
        """
        Gets the is_incremental_data of this Attribute.
        Property that identifies if this attribute can be used as a watermark to extract incremental data.


        :return: The is_incremental_data of this Attribute.
        :rtype: bool
        """
        return self._is_incremental_data

    @is_incremental_data.setter
    def is_incremental_data(self, is_incremental_data):
        """
        Sets the is_incremental_data of this Attribute.
        Property that identifies if this attribute can be used as a watermark to extract incremental data.


        :param is_incremental_data: The is_incremental_data of this Attribute.
        :type: bool
        """
        self._is_incremental_data = is_incremental_data

    @property
    def is_nullable(self):
        """
        Gets the is_nullable of this Attribute.
        Property that identifies if this attribute can be assigned null values.


        :return: The is_nullable of this Attribute.
        :rtype: bool
        """
        return self._is_nullable

    @is_nullable.setter
    def is_nullable(self, is_nullable):
        """
        Sets the is_nullable of this Attribute.
        Property that identifies if this attribute can be assigned null values.


        :param is_nullable: The is_nullable of this Attribute.
        :type: bool
        """
        self._is_nullable = is_nullable

    @property
    def min_collection_count(self):
        """
        Gets the min_collection_count of this Attribute.
        The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.


        :return: The min_collection_count of this Attribute.
        :rtype: int
        """
        return self._min_collection_count

    @min_collection_count.setter
    def min_collection_count(self, min_collection_count):
        """
        Sets the min_collection_count of this Attribute.
        The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.


        :param min_collection_count: The min_collection_count of this Attribute.
        :type: int
        """
        self._min_collection_count = min_collection_count

    @property
    def max_collection_count(self):
        """
        Gets the max_collection_count of this Attribute.
        The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.
        For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\".
        Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in  Xml , maxItems in Json


        :return: The max_collection_count of this Attribute.
        :rtype: int
        """
        return self._max_collection_count

    @max_collection_count.setter
    def max_collection_count(self, max_collection_count):
        """
        Sets the max_collection_count of this Attribute.
        The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.
        For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\".
        Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in  Xml , maxItems in Json


        :param max_collection_count: The max_collection_count of this Attribute.
        :type: int
        """
        self._max_collection_count = max_collection_count

    @property
    def datatype_entity_key(self):
        """
        Gets the datatype_entity_key of this Attribute.
        Entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.


        :return: The datatype_entity_key of this Attribute.
        :rtype: str
        """
        return self._datatype_entity_key

    @datatype_entity_key.setter
    def datatype_entity_key(self, datatype_entity_key):
        """
        Sets the datatype_entity_key of this Attribute.
        Entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.


        :param datatype_entity_key: The datatype_entity_key of this Attribute.
        :type: str
        """
        self._datatype_entity_key = datatype_entity_key

    @property
    def external_datatype_entity_key(self):
        """
        Gets the external_datatype_entity_key of this Attribute.
        External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.


        :return: The external_datatype_entity_key of this Attribute.
        :rtype: str
        """
        return self._external_datatype_entity_key

    @external_datatype_entity_key.setter
    def external_datatype_entity_key(self, external_datatype_entity_key):
        """
        Sets the external_datatype_entity_key of this Attribute.
        External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.


        :param external_datatype_entity_key: The external_datatype_entity_key of this Attribute.
        :type: str
        """
        self._external_datatype_entity_key = external_datatype_entity_key

    @property
    def parent_attribute_key(self):
        """
        Gets the parent_attribute_key of this Attribute.
        Attribute key that represents the parent attribute of this attribute , applicable if the parent attribute is of complex datatype.


        :return: The parent_attribute_key of this Attribute.
        :rtype: str
        """
        return self._parent_attribute_key

    @parent_attribute_key.setter
    def parent_attribute_key(self, parent_attribute_key):
        """
        Sets the parent_attribute_key of this Attribute.
        Attribute key that represents the parent attribute of this attribute , applicable if the parent attribute is of complex datatype.


        :param parent_attribute_key: The parent_attribute_key of this Attribute.
        :type: str
        """
        self._parent_attribute_key = parent_attribute_key

    @property
    def external_parent_attribute_key(self):
        """
        Gets the external_parent_attribute_key of this Attribute.
        External attribute key that represents the parent attribute  of this attribute , applicable if the parent attribute is of complex type.


        :return: The external_parent_attribute_key of this Attribute.
        :rtype: str
        """
        return self._external_parent_attribute_key

    @external_parent_attribute_key.setter
    def external_parent_attribute_key(self, external_parent_attribute_key):
        """
        Sets the external_parent_attribute_key of this Attribute.
        External attribute key that represents the parent attribute  of this attribute , applicable if the parent attribute is of complex type.


        :param external_parent_attribute_key: The external_parent_attribute_key of this Attribute.
        :type: str
        """
        self._external_parent_attribute_key = external_parent_attribute_key

    @property
    def length(self):
        """
        Gets the length of this Attribute.
        Max allowed length of the attribute value.


        :return: The length of this Attribute.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this Attribute.
        Max allowed length of the attribute value.


        :param length: The length of this Attribute.
        :type: int
        """
        self._length = length

    @property
    def position(self):
        """
        Gets the position of this Attribute.
        Position of the attribute in the record definition.


        :return: The position of this Attribute.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this Attribute.
        Position of the attribute in the record definition.


        :param position: The position of this Attribute.
        :type: int
        """
        self._position = position

    @property
    def precision(self):
        """
        Gets the precision of this Attribute.
        Precision of the attribute value usually applies to float data type.


        :return: The precision of this Attribute.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """
        Sets the precision of this Attribute.
        Precision of the attribute value usually applies to float data type.


        :param precision: The precision of this Attribute.
        :type: int
        """
        self._precision = precision

    @property
    def scale(self):
        """
        Gets the scale of this Attribute.
        Scale of the attribute value usually applies to float data type.


        :return: The scale of this Attribute.
        :rtype: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this Attribute.
        Scale of the attribute value usually applies to float data type.


        :param scale: The scale of this Attribute.
        :type: int
        """
        self._scale = scale

    @property
    def time_external(self):
        """
        Gets the time_external of this Attribute.
        Last modified timestamp of this object in the external system.


        :return: The time_external of this Attribute.
        :rtype: datetime
        """
        return self._time_external

    @time_external.setter
    def time_external(self, time_external):
        """
        Sets the time_external of this Attribute.
        Last modified timestamp of this object in the external system.


        :param time_external: The time_external of this Attribute.
        :type: datetime
        """
        self._time_external = time_external

    @property
    def uri(self):
        """
        Gets the uri of this Attribute.
        URI to the attribute instance in the API.


        :return: The uri of this Attribute.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Attribute.
        URI to the attribute instance in the API.


        :param uri: The uri of this Attribute.
        :type: str
        """
        self._uri = uri

    @property
    def path(self):
        """
        Gets the path of this Attribute.
        Full path of the attribute.


        :return: The path of this Attribute.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Attribute.
        Full path of the attribute.


        :param path: The path of this Attribute.
        :type: str
        """
        self._path = path

    @property
    def custom_property_members(self):
        """
        Gets the custom_property_members of this Attribute.
        The list of customized properties along with the values for this object


        :return: The custom_property_members of this Attribute.
        :rtype: list[oci.data_catalog.models.CustomPropertyGetUsage]
        """
        return self._custom_property_members

    @custom_property_members.setter
    def custom_property_members(self, custom_property_members):
        """
        Sets the custom_property_members of this Attribute.
        The list of customized properties along with the values for this object


        :param custom_property_members: The custom_property_members of this Attribute.
        :type: list[oci.data_catalog.models.CustomPropertyGetUsage]
        """
        self._custom_property_members = custom_property_members

    @property
    def properties(self):
        """
        Gets the properties of this Attribute.
        A map of maps that contains the properties which are specific to the attribute type. Each attribute type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        attributes have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :return: The properties of this Attribute.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this Attribute.
        A map of maps that contains the properties which are specific to the attribute type. Each attribute type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        attributes have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :param properties: The properties of this Attribute.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    @property
    def associated_rule_types(self):
        """
        Gets the associated_rule_types of this Attribute.
        Rule types associated with attribute.

        Allowed values for items in this list are: "PRIMARYKEY", "FOREIGNKEY", "UNIQUEKEY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The associated_rule_types of this Attribute.
        :rtype: list[str]
        """
        return self._associated_rule_types

    @associated_rule_types.setter
    def associated_rule_types(self, associated_rule_types):
        """
        Sets the associated_rule_types of this Attribute.
        Rule types associated with attribute.


        :param associated_rule_types: The associated_rule_types of this Attribute.
        :type: list[str]
        """
        allowed_values = ["PRIMARYKEY", "FOREIGNKEY", "UNIQUEKEY"]
        if associated_rule_types:
            associated_rule_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in associated_rule_types]
        self._associated_rule_types = associated_rule_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
