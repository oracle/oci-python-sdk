# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateGroupCursorDetails(object):
    """
    Object used to create a group cursor.
    """

    #: A constant which can be used with the type property of a CreateGroupCursorDetails.
    #: This constant has a value of "AT_TIME"
    TYPE_AT_TIME = "AT_TIME"

    #: A constant which can be used with the type property of a CreateGroupCursorDetails.
    #: This constant has a value of "LATEST"
    TYPE_LATEST = "LATEST"

    #: A constant which can be used with the type property of a CreateGroupCursorDetails.
    #: This constant has a value of "TRIM_HORIZON"
    TYPE_TRIM_HORIZON = "TRIM_HORIZON"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateGroupCursorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreateGroupCursorDetails.
            Allowed values for this property are: "AT_TIME", "LATEST", "TRIM_HORIZON"
        :type type: str

        :param time:
            The value to assign to the time property of this CreateGroupCursorDetails.
        :type time: datetime

        :param group_name:
            The value to assign to the group_name property of this CreateGroupCursorDetails.
        :type group_name: str

        :param instance_name:
            The value to assign to the instance_name property of this CreateGroupCursorDetails.
        :type instance_name: str

        :param timeout_in_ms:
            The value to assign to the timeout_in_ms property of this CreateGroupCursorDetails.
        :type timeout_in_ms: int

        :param commit_on_get:
            The value to assign to the commit_on_get property of this CreateGroupCursorDetails.
        :type commit_on_get: bool

        """
        self.swagger_types = {
            'type': 'str',
            'time': 'datetime',
            'group_name': 'str',
            'instance_name': 'str',
            'timeout_in_ms': 'int',
            'commit_on_get': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'time': 'time',
            'group_name': 'groupName',
            'instance_name': 'instanceName',
            'timeout_in_ms': 'timeoutInMs',
            'commit_on_get': 'commitOnGet'
        }

        self._type = None
        self._time = None
        self._group_name = None
        self._instance_name = None
        self._timeout_in_ms = None
        self._commit_on_get = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateGroupCursorDetails.
        The type of the cursor. This value is only used when the group is created.

        Allowed values for this property are: "AT_TIME", "LATEST", "TRIM_HORIZON"


        :return: The type of this CreateGroupCursorDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateGroupCursorDetails.
        The type of the cursor. This value is only used when the group is created.


        :param type: The type of this CreateGroupCursorDetails.
        :type: str
        """
        allowed_values = ["AT_TIME", "LATEST", "TRIM_HORIZON"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def time(self):
        """
        Gets the time of this CreateGroupCursorDetails.
        The time to consume from if type is AT_TIME.


        :return: The time of this CreateGroupCursorDetails.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this CreateGroupCursorDetails.
        The time to consume from if type is AT_TIME.


        :param time: The time of this CreateGroupCursorDetails.
        :type: datetime
        """
        self._time = time

    @property
    def group_name(self):
        """
        **[Required]** Gets the group_name of this CreateGroupCursorDetails.
        Name of the consumer group.


        :return: The group_name of this CreateGroupCursorDetails.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this CreateGroupCursorDetails.
        Name of the consumer group.


        :param group_name: The group_name of this CreateGroupCursorDetails.
        :type: str
        """
        self._group_name = group_name

    @property
    def instance_name(self):
        """
        Gets the instance_name of this CreateGroupCursorDetails.
        A unique identifier for the instance joining the consumer group. If an instanceName is not provided, a UUID will be generated and used.


        :return: The instance_name of this CreateGroupCursorDetails.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """
        Sets the instance_name of this CreateGroupCursorDetails.
        A unique identifier for the instance joining the consumer group. If an instanceName is not provided, a UUID will be generated and used.


        :param instance_name: The instance_name of this CreateGroupCursorDetails.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def timeout_in_ms(self):
        """
        Gets the timeout_in_ms of this CreateGroupCursorDetails.
        The amount of a consumer instance inactivity time, before partition reservations are released.


        :return: The timeout_in_ms of this CreateGroupCursorDetails.
        :rtype: int
        """
        return self._timeout_in_ms

    @timeout_in_ms.setter
    def timeout_in_ms(self, timeout_in_ms):
        """
        Sets the timeout_in_ms of this CreateGroupCursorDetails.
        The amount of a consumer instance inactivity time, before partition reservations are released.


        :param timeout_in_ms: The timeout_in_ms of this CreateGroupCursorDetails.
        :type: int
        """
        self._timeout_in_ms = timeout_in_ms

    @property
    def commit_on_get(self):
        """
        Gets the commit_on_get of this CreateGroupCursorDetails.
        When using consumer-groups, the default commit-on-get behaviour can be overriden by setting this value to false.
        If disabled, a consumer must manually commit their cursors.


        :return: The commit_on_get of this CreateGroupCursorDetails.
        :rtype: bool
        """
        return self._commit_on_get

    @commit_on_get.setter
    def commit_on_get(self, commit_on_get):
        """
        Sets the commit_on_get of this CreateGroupCursorDetails.
        When using consumer-groups, the default commit-on-get behaviour can be overriden by setting this value to false.
        If disabled, a consumer must manually commit their cursors.


        :param commit_on_get: The commit_on_get of this CreateGroupCursorDetails.
        :type: bool
        """
        self._commit_on_get = commit_on_get

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
