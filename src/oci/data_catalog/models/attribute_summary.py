# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'entity_key': 'str',
            'external_key': 'str',
            'length': 'int',
            'is_nullable': 'bool',
            'uri': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'external_data_type': 'str',
            'min_collection_count': 'int',
            'max_collection_count': 'int',
            'datatype_entity_key': 'str',
            'external_datatype_entity_key': 'str',
            'parent_attribute_key': 'str',
            'external_parent_attribute_key': 'str',
            'path': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'entity_key': 'entityKey',
            'external_key': 'externalKey',
            'length': 'length',
            'is_nullable': 'isNullable',
            'uri': 'uri',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'external_data_type': 'externalDataType',
            'min_collection_count': 'minCollectionCount',
            'max_collection_count': 'maxCollectionCount',
            'datatype_entity_key': 'datatypeEntityKey',
            'external_datatype_entity_key': 'externalDatatypeEntityKey',
            'parent_attribute_key': 'parentAttributeKey',
            'external_parent_attribute_key': 'externalParentAttributeKey',
            'path': 'path'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._entity_key = None
        self._external_key = None
        self._length = None
        self._is_nullable = None
        self._uri = None
        self._lifecycle_state = None
        self._time_created = None
        self._external_data_type = None
        self._min_collection_count = None
        self._max_collection_count = None
        self._datatype_entity_key = None
        self._external_datatype_entity_key = None
        self._parent_attribute_key = None
        self._external_parent_attribute_key = None
        self._path = None

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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
