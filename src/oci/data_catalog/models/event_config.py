# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EventConfig(object):
    """
    Describes an event configuration, for a given object type and property. Primarily, whether a property change will result in an event being emitted.
    """

    #: A constant which can be used with the event_config_status property of a EventConfig.
    #: This constant has a value of "ENABLED"
    EVENT_CONFIG_STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the event_config_status property of a EventConfig.
    #: This constant has a value of "DISABLED"
    EVENT_CONFIG_STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new EventConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type_id:
            The value to assign to the type_id property of this EventConfig.
        :type type_id: str

        :param type_name:
            The value to assign to the type_name property of this EventConfig.
        :type type_name: str

        :param property_id:
            The value to assign to the property_id property of this EventConfig.
        :type property_id: str

        :param property_name:
            The value to assign to the property_name property of this EventConfig.
        :type property_name: str

        :param event_config_status:
            The value to assign to the event_config_status property of this EventConfig.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type event_config_status: str

        :param time_created:
            The value to assign to the time_created property of this EventConfig.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EventConfig.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this EventConfig.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this EventConfig.
        :type updated_by_id: str

        """
        self.swagger_types = {
            'type_id': 'str',
            'type_name': 'str',
            'property_id': 'str',
            'property_name': 'str',
            'event_config_status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str'
        }

        self.attribute_map = {
            'type_id': 'typeId',
            'type_name': 'typeName',
            'property_id': 'propertyId',
            'property_name': 'propertyName',
            'event_config_status': 'eventConfigStatus',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById'
        }

        self._type_id = None
        self._type_name = None
        self._property_id = None
        self._property_name = None
        self._event_config_status = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None

    @property
    def type_id(self):
        """
        Gets the type_id of this EventConfig.
        Unique type key identifier.


        :return: The type_id of this EventConfig.
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this EventConfig.
        Unique type key identifier.


        :param type_id: The type_id of this EventConfig.
        :type: str
        """
        self._type_id = type_id

    @property
    def type_name(self):
        """
        Gets the type_name of this EventConfig.
        Name of the type.


        :return: The type_name of this EventConfig.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """
        Sets the type_name of this EventConfig.
        Name of the type.


        :param type_name: The type_name of this EventConfig.
        :type: str
        """
        self._type_name = type_name

    @property
    def property_id(self):
        """
        Gets the property_id of this EventConfig.
        Unique property key identifier.


        :return: The property_id of this EventConfig.
        :rtype: str
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """
        Sets the property_id of this EventConfig.
        Unique property key identifier.


        :param property_id: The property_id of this EventConfig.
        :type: str
        """
        self._property_id = property_id

    @property
    def property_name(self):
        """
        Gets the property_name of this EventConfig.
        Name of the property.


        :return: The property_name of this EventConfig.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """
        Sets the property_name of this EventConfig.
        Name of the property.


        :param property_name: The property_name of this EventConfig.
        :type: str
        """
        self._property_name = property_name

    @property
    def event_config_status(self):
        """
        Gets the event_config_status of this EventConfig.
        Status of the configuration.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The event_config_status of this EventConfig.
        :rtype: str
        """
        return self._event_config_status

    @event_config_status.setter
    def event_config_status(self, event_config_status):
        """
        Sets the event_config_status of this EventConfig.
        Status of the configuration.


        :param event_config_status: The event_config_status of this EventConfig.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(event_config_status, allowed_values):
            event_config_status = 'UNKNOWN_ENUM_VALUE'
        self._event_config_status = event_config_status

    @property
    def time_created(self):
        """
        Gets the time_created of this EventConfig.
        The date and time the event was configured, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this EventConfig.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EventConfig.
        The date and time the event was configured, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this EventConfig.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this EventConfig.
        The last time that any change was made to the configuration. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this EventConfig.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EventConfig.
        The last time that any change was made to the configuration. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this EventConfig.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this EventConfig.
        OCID of the user who created the configuration.


        :return: The created_by_id of this EventConfig.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this EventConfig.
        OCID of the user who created the configuration.


        :param created_by_id: The created_by_id of this EventConfig.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this EventConfig.
        OCID of the user who last modified the configuration.


        :return: The updated_by_id of this EventConfig.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this EventConfig.
        OCID of the user who last modified the configuration.


        :param updated_by_id: The updated_by_id of this EventConfig.
        :type: str
        """
        self._updated_by_id = updated_by_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
