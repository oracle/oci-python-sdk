# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceLock(object):
    """
    Resource locks prevent certain APIs from being called for the resource.
    A full lock prevents both updating and deleting the resource. A lock delete
    prevents deleting the resource.
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

        """
        self.swagger_types = {
            'type': 'str',
            'related_resource_id': 'str',
            'message': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'type': 'type',
            'related_resource_id': 'relatedResourceId',
            'message': 'message',
            'time_created': 'timeCreated'
        }

        self._type = None
        self._related_resource_id = None
        self._message = None
        self._time_created = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ResourceLock.
        Lock type.

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
        Lock type.


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
        The resource ID that is locking this resource. Indicates that deleting this resource removes the lock.


        :return: The related_resource_id of this ResourceLock.
        :rtype: str
        """
        return self._related_resource_id

    @related_resource_id.setter
    def related_resource_id(self, related_resource_id):
        """
        Sets the related_resource_id of this ResourceLock.
        The resource ID that is locking this resource. Indicates that deleting this resource removes the lock.


        :param related_resource_id: The related_resource_id of this ResourceLock.
        :type: str
        """
        self._related_resource_id = related_resource_id

    @property
    def message(self):
        """
        Gets the message of this ResourceLock.
        A message added by the lock creator. The message typically gives an
        indication of why the resource is locked.


        :return: The message of this ResourceLock.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ResourceLock.
        A message added by the lock creator. The message typically gives an
        indication of why the resource is locked.


        :param message: The message of this ResourceLock.
        :type: str
        """
        self._message = message

    @property
    def time_created(self):
        """
        Gets the time_created of this ResourceLock.
        Indicates when the lock was created, in the format defined by RFC 3339.


        :return: The time_created of this ResourceLock.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ResourceLock.
        Indicates when the lock was created, in the format defined by RFC 3339.


        :param time_created: The time_created of this ResourceLock.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
