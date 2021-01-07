# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Namespace(object):
    """
    Namespace Definition
    """

    #: A constant which can be used with the lifecycle_state property of a Namespace.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Namespace.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Namespace.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Namespace.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Namespace.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Namespace.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Namespace.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Namespace.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new Namespace object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Namespace.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this Namespace.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Namespace.
        :type description: str

        :param is_service_defined:
            The value to assign to the is_service_defined property of this Namespace.
        :type is_service_defined: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Namespace.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Namespace.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Namespace.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this Namespace.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this Namespace.
        :type updated_by_id: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'is_service_defined': 'bool',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'is_service_defined': 'isServiceDefined',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._is_service_defined = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Namespace.
        Unique namespace key that is immutable.


        :return: The key of this Namespace.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Namespace.
        Unique namespace key that is immutable.


        :param key: The key of this Namespace.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this Namespace.
        Name of the Namespace


        :return: The display_name of this Namespace.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Namespace.
        Name of the Namespace


        :param display_name: The display_name of this Namespace.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Namespace.
        Description for the namespace


        :return: The description of this Namespace.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Namespace.
        Description for the namespace


        :param description: The description of this Namespace.
        :type: str
        """
        self._description = description

    @property
    def is_service_defined(self):
        """
        Gets the is_service_defined of this Namespace.
        If this field is defined by service or by a user


        :return: The is_service_defined of this Namespace.
        :rtype: bool
        """
        return self._is_service_defined

    @is_service_defined.setter
    def is_service_defined(self, is_service_defined):
        """
        Sets the is_service_defined of this Namespace.
        If this field is defined by service or by a user


        :param is_service_defined: The is_service_defined of this Namespace.
        :type: bool
        """
        self._is_service_defined = is_service_defined

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Namespace.
        The current state of the namespace.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Namespace.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Namespace.
        The current state of the namespace.


        :param lifecycle_state: The lifecycle_state of this Namespace.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Namespace.
        The date and time the namespace was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Namespace.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Namespace.
        The date and time the namespace was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Namespace.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Namespace.
        The last time that any change was made to the namespace. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Namespace.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Namespace.
        The last time that any change was made to the namespace. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Namespace.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this Namespace.
        OCID of the user who created the namespace.


        :return: The created_by_id of this Namespace.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this Namespace.
        OCID of the user who created the namespace.


        :param created_by_id: The created_by_id of this Namespace.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this Namespace.
        OCID of the user who last modified the namespace.


        :return: The updated_by_id of this Namespace.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this Namespace.
        OCID of the user who last modified the namespace.


        :param updated_by_id: The updated_by_id of this Namespace.
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
