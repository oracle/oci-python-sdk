# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogSavedSearchSummary(object):
    """
    A summary of a log saved search that can be used to save and share a given search result.
    """

    #: A constant which can be used with the lifecycle_state property of a LogSavedSearchSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LogSavedSearchSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new LogSavedSearchSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LogSavedSearchSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LogSavedSearchSummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this LogSavedSearchSummary.
        :type name: str

        :param time_created:
            The value to assign to the time_created property of this LogSavedSearchSummary.
        :type time_created: datetime

        :param is_quick_start:
            The value to assign to the is_quick_start property of this LogSavedSearchSummary.
        :type is_quick_start: bool

        :param time_last_modified:
            The value to assign to the time_last_modified property of this LogSavedSearchSummary.
        :type time_last_modified: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LogSavedSearchSummary.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'time_created': 'datetime',
            'is_quick_start': 'bool',
            'time_last_modified': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'time_created': 'timeCreated',
            'is_quick_start': 'isQuickStart',
            'time_last_modified': 'timeLastModified',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._time_created = None
        self._is_quick_start = None
        self._time_last_modified = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LogSavedSearchSummary.
        The OCID of the resource.


        :return: The id of this LogSavedSearchSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LogSavedSearchSummary.
        The OCID of the resource.


        :param id: The id of this LogSavedSearchSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LogSavedSearchSummary.
        The OCID of the compartment that the resource belongs to.


        :return: The compartment_id of this LogSavedSearchSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LogSavedSearchSummary.
        The OCID of the compartment that the resource belongs to.


        :param compartment_id: The compartment_id of this LogSavedSearchSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this LogSavedSearchSummary.
        The display name of a user-friendly name. It has to be unique within enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :return: The name of this LogSavedSearchSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogSavedSearchSummary.
        The display name of a user-friendly name. It has to be unique within enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :param name: The name of this LogSavedSearchSummary.
        :type: str
        """
        self._name = name

    @property
    def time_created(self):
        """
        Gets the time_created of this LogSavedSearchSummary.
        Time the resource was created.


        :return: The time_created of this LogSavedSearchSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LogSavedSearchSummary.
        Time the resource was created.


        :param time_created: The time_created of this LogSavedSearchSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def is_quick_start(self):
        """
        **[Required]** Gets the is_quick_start of this LogSavedSearchSummary.
        True if the LogSavedSearch should be show as quickstart in the UI


        :return: The is_quick_start of this LogSavedSearchSummary.
        :rtype: bool
        """
        return self._is_quick_start

    @is_quick_start.setter
    def is_quick_start(self, is_quick_start):
        """
        Sets the is_quick_start of this LogSavedSearchSummary.
        True if the LogSavedSearch should be show as quickstart in the UI


        :param is_quick_start: The is_quick_start of this LogSavedSearchSummary.
        :type: bool
        """
        self._is_quick_start = is_quick_start

    @property
    def time_last_modified(self):
        """
        Gets the time_last_modified of this LogSavedSearchSummary.
        Time the resource was last modified.


        :return: The time_last_modified of this LogSavedSearchSummary.
        :rtype: datetime
        """
        return self._time_last_modified

    @time_last_modified.setter
    def time_last_modified(self, time_last_modified):
        """
        Sets the time_last_modified of this LogSavedSearchSummary.
        Time the resource was last modified.


        :param time_last_modified: The time_last_modified of this LogSavedSearchSummary.
        :type: datetime
        """
        self._time_last_modified = time_last_modified

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this LogSavedSearchSummary.
        The state of the LogSavedSearch

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LogSavedSearchSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LogSavedSearchSummary.
        The state of the LogSavedSearch


        :param lifecycle_state: The lifecycle_state of this LogSavedSearchSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
