# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceLock(object):
    """
    Resource locks are used to prevent certain APIs from being called for the resource.
    A full lock prevents both updating the resource and deleting the resource. A delete
    lock prevents deleting the resource.
    """

    #: A constant which can be used with the type property of a ResourceLock.
    #: This constant has a value of "FULL"
    TYPE_FULL = "FULL"

    #: A constant which can be used with the type property of a ResourceLock.
    #: This constant has a value of "DELETE"
    TYPE_DELETE = "DELETE"

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceLock object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ResourceLock.
            Allowed values for this property are: "FULL", "DELETE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param related_resource_id:
            The value to assign to the related_resource_id property of this ResourceLock.
        :type related_resource_id: str

        :param message:
            The value to assign to the message property of this ResourceLock.
        :type message: str

        :param time_created:
            The value to assign to the time_created property of this ResourceLock.
        :type time_created: datetime

        :param is_active:
            The value to assign to the is_active property of this ResourceLock.
        :type is_active: bool

        """
        self.swagger_types = {
            'type': 'str',
            'related_resource_id': 'str',
            'message': 'str',
            'time_created': 'datetime',
            'is_active': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'related_resource_id': 'relatedResourceId',
            'message': 'message',
            'time_created': 'timeCreated',
            'is_active': 'isActive'
        }

        self._type = None
        self._related_resource_id = None
        self._message = None
        self._time_created = None
        self._is_active = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ResourceLock.
        Type of the lock.

        Allowed values for this property are: "FULL", "DELETE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ResourceLock.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ResourceLock.
        Type of the lock.


        :param type: The type of this ResourceLock.
        :type: str
        """
        allowed_values = ["FULL", "DELETE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def related_resource_id(self):
        """
        Gets the related_resource_id of this ResourceLock.
        The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.


        :return: The related_resource_id of this ResourceLock.
        :rtype: str
        """
        return self._related_resource_id

    @related_resource_id.setter
    def related_resource_id(self, related_resource_id):
        """
        Sets the related_resource_id of this ResourceLock.
        The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.


        :param related_resource_id: The related_resource_id of this ResourceLock.
        :type: str
        """
        self._related_resource_id = related_resource_id

    @property
    def message(self):
        """
        Gets the message of this ResourceLock.
        A message added by the creator of the lock. This is typically used to give an
        indication of why the resource is locked.


        :return: The message of this ResourceLock.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ResourceLock.
        A message added by the creator of the lock. This is typically used to give an
        indication of why the resource is locked.


        :param message: The message of this ResourceLock.
        :type: str
        """
        self._message = message

    @property
    def time_created(self):
        """
        Gets the time_created of this ResourceLock.
        When the lock was created.


        :return: The time_created of this ResourceLock.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ResourceLock.
        When the lock was created.


        :param time_created: The time_created of this ResourceLock.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def is_active(self):
        """
        Gets the is_active of this ResourceLock.
        Indicates if the lock is active or not. For example, if there are mutliple FULL locks, the first-created FULL lock will be effective.


        :return: The is_active of this ResourceLock.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this ResourceLock.
        Indicates if the lock is active or not. For example, if there are mutliple FULL locks, the first-created FULL lock will be effective.


        :param is_active: The is_active of this ResourceLock.
        :type: bool
        """
        self._is_active = is_active

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
