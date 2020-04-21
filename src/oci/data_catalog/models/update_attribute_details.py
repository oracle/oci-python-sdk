# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAttributeDetails(object):
    """
    Properties used in attribute update operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAttributeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAttributeDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateAttributeDetails.
        :type description: str

        :param external_data_type:
            The value to assign to the external_data_type property of this UpdateAttributeDetails.
        :type external_data_type: str

        :param is_incremental_data:
            The value to assign to the is_incremental_data property of this UpdateAttributeDetails.
        :type is_incremental_data: bool

        :param is_nullable:
            The value to assign to the is_nullable property of this UpdateAttributeDetails.
        :type is_nullable: bool

        :param length:
            The value to assign to the length property of this UpdateAttributeDetails.
        :type length: int

        :param position:
            The value to assign to the position property of this UpdateAttributeDetails.
        :type position: int

        :param precision:
            The value to assign to the precision property of this UpdateAttributeDetails.
        :type precision: int

        :param scale:
            The value to assign to the scale property of this UpdateAttributeDetails.
        :type scale: int

        :param time_external:
            The value to assign to the time_external property of this UpdateAttributeDetails.
        :type time_external: datetime

        :param properties:
            The value to assign to the properties property of this UpdateAttributeDetails.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'external_data_type': 'str',
            'is_incremental_data': 'bool',
            'is_nullable': 'bool',
            'length': 'int',
            'position': 'int',
            'precision': 'int',
            'scale': 'int',
            'time_external': 'datetime',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'external_data_type': 'externalDataType',
            'is_incremental_data': 'isIncrementalData',
            'is_nullable': 'isNullable',
            'length': 'length',
            'position': 'position',
            'precision': 'precision',
            'scale': 'scale',
            'time_external': 'timeExternal',
            'properties': 'properties'
        }

        self._display_name = None
        self._description = None
        self._external_data_type = None
        self._is_incremental_data = None
        self._is_nullable = None
        self._length = None
        self._position = None
        self._precision = None
        self._scale = None
        self._time_external = None
        self._properties = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAttributeDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateAttributeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAttributeDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateAttributeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateAttributeDetails.
        Detailed description of the attribute.


        :return: The description of this UpdateAttributeDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateAttributeDetails.
        Detailed description of the attribute.


        :param description: The description of this UpdateAttributeDetails.
        :type: str
        """
        self._description = description

    @property
    def external_data_type(self):
        """
        Gets the external_data_type of this UpdateAttributeDetails.
        Data type of the attribute as defined in the external system.


        :return: The external_data_type of this UpdateAttributeDetails.
        :rtype: str
        """
        return self._external_data_type

    @external_data_type.setter
    def external_data_type(self, external_data_type):
        """
        Sets the external_data_type of this UpdateAttributeDetails.
        Data type of the attribute as defined in the external system.


        :param external_data_type: The external_data_type of this UpdateAttributeDetails.
        :type: str
        """
        self._external_data_type = external_data_type

    @property
    def is_incremental_data(self):
        """
        Gets the is_incremental_data of this UpdateAttributeDetails.
        Property that identifies if this attribute can be used as a watermark to extract incremental data.


        :return: The is_incremental_data of this UpdateAttributeDetails.
        :rtype: bool
        """
        return self._is_incremental_data

    @is_incremental_data.setter
    def is_incremental_data(self, is_incremental_data):
        """
        Sets the is_incremental_data of this UpdateAttributeDetails.
        Property that identifies if this attribute can be used as a watermark to extract incremental data.


        :param is_incremental_data: The is_incremental_data of this UpdateAttributeDetails.
        :type: bool
        """
        self._is_incremental_data = is_incremental_data

    @property
    def is_nullable(self):
        """
        Gets the is_nullable of this UpdateAttributeDetails.
        Property that identifies if this attribute can be assigned nullable values.


        :return: The is_nullable of this UpdateAttributeDetails.
        :rtype: bool
        """
        return self._is_nullable

    @is_nullable.setter
    def is_nullable(self, is_nullable):
        """
        Sets the is_nullable of this UpdateAttributeDetails.
        Property that identifies if this attribute can be assigned nullable values.


        :param is_nullable: The is_nullable of this UpdateAttributeDetails.
        :type: bool
        """
        self._is_nullable = is_nullable

    @property
    def length(self):
        """
        Gets the length of this UpdateAttributeDetails.
        Max allowed length of the attribute value.


        :return: The length of this UpdateAttributeDetails.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this UpdateAttributeDetails.
        Max allowed length of the attribute value.


        :param length: The length of this UpdateAttributeDetails.
        :type: int
        """
        self._length = length

    @property
    def position(self):
        """
        Gets the position of this UpdateAttributeDetails.
        Position of the attribute in the record definition.


        :return: The position of this UpdateAttributeDetails.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this UpdateAttributeDetails.
        Position of the attribute in the record definition.


        :param position: The position of this UpdateAttributeDetails.
        :type: int
        """
        self._position = position

    @property
    def precision(self):
        """
        Gets the precision of this UpdateAttributeDetails.
        Precision of the attribute value usually applies to float data type.


        :return: The precision of this UpdateAttributeDetails.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """
        Sets the precision of this UpdateAttributeDetails.
        Precision of the attribute value usually applies to float data type.


        :param precision: The precision of this UpdateAttributeDetails.
        :type: int
        """
        self._precision = precision

    @property
    def scale(self):
        """
        Gets the scale of this UpdateAttributeDetails.
        Scale of the attribute value usually applies to float data type.


        :return: The scale of this UpdateAttributeDetails.
        :rtype: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this UpdateAttributeDetails.
        Scale of the attribute value usually applies to float data type.


        :param scale: The scale of this UpdateAttributeDetails.
        :type: int
        """
        self._scale = scale

    @property
    def time_external(self):
        """
        Gets the time_external of this UpdateAttributeDetails.
        Last modified timestamp of this object in the external system.


        :return: The time_external of this UpdateAttributeDetails.
        :rtype: datetime
        """
        return self._time_external

    @time_external.setter
    def time_external(self, time_external):
        """
        Sets the time_external of this UpdateAttributeDetails.
        Last modified timestamp of this object in the external system.


        :param time_external: The time_external of this UpdateAttributeDetails.
        :type: datetime
        """
        self._time_external = time_external

    @property
    def properties(self):
        """
        Gets the properties of this UpdateAttributeDetails.
        A map of maps that contains the properties which are specific to the attribute type. Each attribute type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        attributes have required properties within the \"default\" category. To determine the set of required and
        optional properties for an Attribute type, a query can be done on '/types?type=attribute' which returns a
        collection of all attribute types. The appropriate attribute type, which will include definitions of all
        of it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :return: The properties of this UpdateAttributeDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this UpdateAttributeDetails.
        A map of maps that contains the properties which are specific to the attribute type. Each attribute type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        attributes have required properties within the \"default\" category. To determine the set of required and
        optional properties for an Attribute type, a query can be done on '/types?type=attribute' which returns a
        collection of all attribute types. The appropriate attribute type, which will include definitions of all
        of it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :param properties: The properties of this UpdateAttributeDetails.
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
