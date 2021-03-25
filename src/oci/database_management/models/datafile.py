# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Datafile(object):
    """
    The details of a datafile.
    """

    #: A constant which can be used with the status property of a Datafile.
    #: This constant has a value of "AVAILABLE"
    STATUS_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the status property of a Datafile.
    #: This constant has a value of "INVALID"
    STATUS_INVALID = "INVALID"

    #: A constant which can be used with the status property of a Datafile.
    #: This constant has a value of "OFFLINE"
    STATUS_OFFLINE = "OFFLINE"

    #: A constant which can be used with the status property of a Datafile.
    #: This constant has a value of "ONLINE"
    STATUS_ONLINE = "ONLINE"

    #: A constant which can be used with the status property of a Datafile.
    #: This constant has a value of "UNKNOWN"
    STATUS_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the online_status property of a Datafile.
    #: This constant has a value of "SYSOFF"
    ONLINE_STATUS_SYSOFF = "SYSOFF"

    #: A constant which can be used with the online_status property of a Datafile.
    #: This constant has a value of "SYSTEM"
    ONLINE_STATUS_SYSTEM = "SYSTEM"

    #: A constant which can be used with the online_status property of a Datafile.
    #: This constant has a value of "OFFLINE"
    ONLINE_STATUS_OFFLINE = "OFFLINE"

    #: A constant which can be used with the online_status property of a Datafile.
    #: This constant has a value of "ONLINE"
    ONLINE_STATUS_ONLINE = "ONLINE"

    #: A constant which can be used with the online_status property of a Datafile.
    #: This constant has a value of "RECOVER"
    ONLINE_STATUS_RECOVER = "RECOVER"

    #: A constant which can be used with the lost_write_protect property of a Datafile.
    #: This constant has a value of "ENABLED"
    LOST_WRITE_PROTECT_ENABLED = "ENABLED"

    #: A constant which can be used with the lost_write_protect property of a Datafile.
    #: This constant has a value of "PROTECT_OFF"
    LOST_WRITE_PROTECT_PROTECT_OFF = "PROTECT_OFF"

    #: A constant which can be used with the lost_write_protect property of a Datafile.
    #: This constant has a value of "SUSPEND"
    LOST_WRITE_PROTECT_SUSPEND = "SUSPEND"

    #: A constant which can be used with the shared property of a Datafile.
    #: This constant has a value of "SHARED"
    SHARED_SHARED = "SHARED"

    #: A constant which can be used with the shared property of a Datafile.
    #: This constant has a value of "LOCAL_FOR_RIM"
    SHARED_LOCAL_FOR_RIM = "LOCAL_FOR_RIM"

    #: A constant which can be used with the shared property of a Datafile.
    #: This constant has a value of "LOCAL_FOR_ALL"
    SHARED_LOCAL_FOR_ALL = "LOCAL_FOR_ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new Datafile object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Datafile.
        :type name: str

        :param status:
            The value to assign to the status property of this Datafile.
            Allowed values for this property are: "AVAILABLE", "INVALID", "OFFLINE", "ONLINE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param online_status:
            The value to assign to the online_status property of this Datafile.
            Allowed values for this property are: "SYSOFF", "SYSTEM", "OFFLINE", "ONLINE", "RECOVER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type online_status: str

        :param is_auto_extensible:
            The value to assign to the is_auto_extensible property of this Datafile.
        :type is_auto_extensible: bool

        :param lost_write_protect:
            The value to assign to the lost_write_protect property of this Datafile.
            Allowed values for this property are: "ENABLED", "PROTECT_OFF", "SUSPEND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lost_write_protect: str

        :param shared:
            The value to assign to the shared property of this Datafile.
            Allowed values for this property are: "SHARED", "LOCAL_FOR_RIM", "LOCAL_FOR_ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type shared: str

        :param instance_id:
            The value to assign to the instance_id property of this Datafile.
        :type instance_id: float

        :param max_size_kb:
            The value to assign to the max_size_kb property of this Datafile.
        :type max_size_kb: float

        :param allocated_size_kb:
            The value to assign to the allocated_size_kb property of this Datafile.
        :type allocated_size_kb: float

        :param user_size_kb:
            The value to assign to the user_size_kb property of this Datafile.
        :type user_size_kb: float

        :param increment_by:
            The value to assign to the increment_by property of this Datafile.
        :type increment_by: float

        :param free_space_kb:
            The value to assign to the free_space_kb property of this Datafile.
        :type free_space_kb: float

        :param used_space_kb:
            The value to assign to the used_space_kb property of this Datafile.
        :type used_space_kb: float

        :param used_percent_available:
            The value to assign to the used_percent_available property of this Datafile.
        :type used_percent_available: float

        :param used_percent_allocated:
            The value to assign to the used_percent_allocated property of this Datafile.
        :type used_percent_allocated: float

        """
        self.swagger_types = {
            'name': 'str',
            'status': 'str',
            'online_status': 'str',
            'is_auto_extensible': 'bool',
            'lost_write_protect': 'str',
            'shared': 'str',
            'instance_id': 'float',
            'max_size_kb': 'float',
            'allocated_size_kb': 'float',
            'user_size_kb': 'float',
            'increment_by': 'float',
            'free_space_kb': 'float',
            'used_space_kb': 'float',
            'used_percent_available': 'float',
            'used_percent_allocated': 'float'
        }

        self.attribute_map = {
            'name': 'name',
            'status': 'status',
            'online_status': 'onlineStatus',
            'is_auto_extensible': 'isAutoExtensible',
            'lost_write_protect': 'lostWriteProtect',
            'shared': 'shared',
            'instance_id': 'instanceId',
            'max_size_kb': 'maxSizeKB',
            'allocated_size_kb': 'allocatedSizeKB',
            'user_size_kb': 'userSizeKB',
            'increment_by': 'incrementBy',
            'free_space_kb': 'freeSpaceKB',
            'used_space_kb': 'usedSpaceKB',
            'used_percent_available': 'usedPercentAvailable',
            'used_percent_allocated': 'usedPercentAllocated'
        }

        self._name = None
        self._status = None
        self._online_status = None
        self._is_auto_extensible = None
        self._lost_write_protect = None
        self._shared = None
        self._instance_id = None
        self._max_size_kb = None
        self._allocated_size_kb = None
        self._user_size_kb = None
        self._increment_by = None
        self._free_space_kb = None
        self._used_space_kb = None
        self._used_percent_available = None
        self._used_percent_allocated = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Datafile.
        The filename (including the path) of the datafile or tempfile.


        :return: The name of this Datafile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Datafile.
        The filename (including the path) of the datafile or tempfile.


        :param name: The name of this Datafile.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """
        Gets the status of this Datafile.
        The status of the file. INVALID status is used when the file number is not in use, for example, a file in a tablespace that was dropped.

        Allowed values for this property are: "AVAILABLE", "INVALID", "OFFLINE", "ONLINE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this Datafile.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Datafile.
        The status of the file. INVALID status is used when the file number is not in use, for example, a file in a tablespace that was dropped.


        :param status: The status of this Datafile.
        :type: str
        """
        allowed_values = ["AVAILABLE", "INVALID", "OFFLINE", "ONLINE", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def online_status(self):
        """
        Gets the online_status of this Datafile.
        The online status of the file.

        Allowed values for this property are: "SYSOFF", "SYSTEM", "OFFLINE", "ONLINE", "RECOVER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The online_status of this Datafile.
        :rtype: str
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        """
        Sets the online_status of this Datafile.
        The online status of the file.


        :param online_status: The online_status of this Datafile.
        :type: str
        """
        allowed_values = ["SYSOFF", "SYSTEM", "OFFLINE", "ONLINE", "RECOVER"]
        if not value_allowed_none_or_none_sentinel(online_status, allowed_values):
            online_status = 'UNKNOWN_ENUM_VALUE'
        self._online_status = online_status

    @property
    def is_auto_extensible(self):
        """
        Gets the is_auto_extensible of this Datafile.
        Indicates whether the datafile is auto-extensible.


        :return: The is_auto_extensible of this Datafile.
        :rtype: bool
        """
        return self._is_auto_extensible

    @is_auto_extensible.setter
    def is_auto_extensible(self, is_auto_extensible):
        """
        Sets the is_auto_extensible of this Datafile.
        Indicates whether the datafile is auto-extensible.


        :param is_auto_extensible: The is_auto_extensible of this Datafile.
        :type: bool
        """
        self._is_auto_extensible = is_auto_extensible

    @property
    def lost_write_protect(self):
        """
        Gets the lost_write_protect of this Datafile.
        The lost write protection status of the file.

        Allowed values for this property are: "ENABLED", "PROTECT_OFF", "SUSPEND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lost_write_protect of this Datafile.
        :rtype: str
        """
        return self._lost_write_protect

    @lost_write_protect.setter
    def lost_write_protect(self, lost_write_protect):
        """
        Sets the lost_write_protect of this Datafile.
        The lost write protection status of the file.


        :param lost_write_protect: The lost_write_protect of this Datafile.
        :type: str
        """
        allowed_values = ["ENABLED", "PROTECT_OFF", "SUSPEND"]
        if not value_allowed_none_or_none_sentinel(lost_write_protect, allowed_values):
            lost_write_protect = 'UNKNOWN_ENUM_VALUE'
        self._lost_write_protect = lost_write_protect

    @property
    def shared(self):
        """
        Gets the shared of this Datafile.
        Type of tablespace this file belongs to. If it's for a shared tablespace, for a local temporary tablespace for RIM (read-only) instances, or for local temporary tablespace for all instance types.

        Allowed values for this property are: "SHARED", "LOCAL_FOR_RIM", "LOCAL_FOR_ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The shared of this Datafile.
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """
        Sets the shared of this Datafile.
        Type of tablespace this file belongs to. If it's for a shared tablespace, for a local temporary tablespace for RIM (read-only) instances, or for local temporary tablespace for all instance types.


        :param shared: The shared of this Datafile.
        :type: str
        """
        allowed_values = ["SHARED", "LOCAL_FOR_RIM", "LOCAL_FOR_ALL"]
        if not value_allowed_none_or_none_sentinel(shared, allowed_values):
            shared = 'UNKNOWN_ENUM_VALUE'
        self._shared = shared

    @property
    def instance_id(self):
        """
        Gets the instance_id of this Datafile.
        Instance ID of the instance to which the temp file belongs. This column has a NULL value for temp files that belong to shared tablespaces.


        :return: The instance_id of this Datafile.
        :rtype: float
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this Datafile.
        Instance ID of the instance to which the temp file belongs. This column has a NULL value for temp files that belong to shared tablespaces.


        :param instance_id: The instance_id of this Datafile.
        :type: float
        """
        self._instance_id = instance_id

    @property
    def max_size_kb(self):
        """
        Gets the max_size_kb of this Datafile.
        The maximum file size in KB.


        :return: The max_size_kb of this Datafile.
        :rtype: float
        """
        return self._max_size_kb

    @max_size_kb.setter
    def max_size_kb(self, max_size_kb):
        """
        Sets the max_size_kb of this Datafile.
        The maximum file size in KB.


        :param max_size_kb: The max_size_kb of this Datafile.
        :type: float
        """
        self._max_size_kb = max_size_kb

    @property
    def allocated_size_kb(self):
        """
        Gets the allocated_size_kb of this Datafile.
        The allocated file size in KB.


        :return: The allocated_size_kb of this Datafile.
        :rtype: float
        """
        return self._allocated_size_kb

    @allocated_size_kb.setter
    def allocated_size_kb(self, allocated_size_kb):
        """
        Sets the allocated_size_kb of this Datafile.
        The allocated file size in KB.


        :param allocated_size_kb: The allocated_size_kb of this Datafile.
        :type: float
        """
        self._allocated_size_kb = allocated_size_kb

    @property
    def user_size_kb(self):
        """
        Gets the user_size_kb of this Datafile.
        The size of the file available for user data in KB. The actual size of the file minus the USER_BYTES value is used to store file-related metadata.


        :return: The user_size_kb of this Datafile.
        :rtype: float
        """
        return self._user_size_kb

    @user_size_kb.setter
    def user_size_kb(self, user_size_kb):
        """
        Sets the user_size_kb of this Datafile.
        The size of the file available for user data in KB. The actual size of the file minus the USER_BYTES value is used to store file-related metadata.


        :param user_size_kb: The user_size_kb of this Datafile.
        :type: float
        """
        self._user_size_kb = user_size_kb

    @property
    def increment_by(self):
        """
        Gets the increment_by of this Datafile.
        The number of blocks used as auto-extension increment.


        :return: The increment_by of this Datafile.
        :rtype: float
        """
        return self._increment_by

    @increment_by.setter
    def increment_by(self, increment_by):
        """
        Sets the increment_by of this Datafile.
        The number of blocks used as auto-extension increment.


        :param increment_by: The increment_by of this Datafile.
        :type: float
        """
        self._increment_by = increment_by

    @property
    def free_space_kb(self):
        """
        Gets the free_space_kb of this Datafile.
        The free space available in the datafile in KB.


        :return: The free_space_kb of this Datafile.
        :rtype: float
        """
        return self._free_space_kb

    @free_space_kb.setter
    def free_space_kb(self, free_space_kb):
        """
        Sets the free_space_kb of this Datafile.
        The free space available in the datafile in KB.


        :param free_space_kb: The free_space_kb of this Datafile.
        :type: float
        """
        self._free_space_kb = free_space_kb

    @property
    def used_space_kb(self):
        """
        Gets the used_space_kb of this Datafile.
        The total space used in the datafile in KB.


        :return: The used_space_kb of this Datafile.
        :rtype: float
        """
        return self._used_space_kb

    @used_space_kb.setter
    def used_space_kb(self, used_space_kb):
        """
        Sets the used_space_kb of this Datafile.
        The total space used in the datafile in KB.


        :param used_space_kb: The used_space_kb of this Datafile.
        :type: float
        """
        self._used_space_kb = used_space_kb

    @property
    def used_percent_available(self):
        """
        Gets the used_percent_available of this Datafile.
        The percentage of used space out of the maximum available space in the file.


        :return: The used_percent_available of this Datafile.
        :rtype: float
        """
        return self._used_percent_available

    @used_percent_available.setter
    def used_percent_available(self, used_percent_available):
        """
        Sets the used_percent_available of this Datafile.
        The percentage of used space out of the maximum available space in the file.


        :param used_percent_available: The used_percent_available of this Datafile.
        :type: float
        """
        self._used_percent_available = used_percent_available

    @property
    def used_percent_allocated(self):
        """
        Gets the used_percent_allocated of this Datafile.
        The percentage of used space out of the total allocated space in the file.


        :return: The used_percent_allocated of this Datafile.
        :rtype: float
        """
        return self._used_percent_allocated

    @used_percent_allocated.setter
    def used_percent_allocated(self, used_percent_allocated):
        """
        Sets the used_percent_allocated of this Datafile.
        The percentage of used space out of the total allocated space in the file.


        :param used_percent_allocated: The used_percent_allocated of this Datafile.
        :type: float
        """
        self._used_percent_allocated = used_percent_allocated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
