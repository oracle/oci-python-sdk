# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LinkSummary(object):
    """
    The summary of a link between a parent tenancy and a child tenancy.
    """

    #: A constant which can be used with the lifecycle_state property of a LinkSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a LinkSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LinkSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LinkSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a LinkSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a LinkSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new LinkSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LinkSummary.
        :type id: str

        :param parent_tenancy_id:
            The value to assign to the parent_tenancy_id property of this LinkSummary.
        :type parent_tenancy_id: str

        :param child_tenancy_id:
            The value to assign to the child_tenancy_id property of this LinkSummary.
        :type child_tenancy_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LinkSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this LinkSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this LinkSummary.
        :type time_updated: datetime

        :param time_terminated:
            The value to assign to the time_terminated property of this LinkSummary.
        :type time_terminated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'parent_tenancy_id': 'str',
            'child_tenancy_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_terminated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'parent_tenancy_id': 'parentTenancyId',
            'child_tenancy_id': 'childTenancyId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_terminated': 'timeTerminated'
        }

        self._id = None
        self._parent_tenancy_id = None
        self._child_tenancy_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._time_terminated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LinkSummary.
        OCID of the link.


        :return: The id of this LinkSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LinkSummary.
        OCID of the link.


        :param id: The id of this LinkSummary.
        :type: str
        """
        self._id = id

    @property
    def parent_tenancy_id(self):
        """
        **[Required]** Gets the parent_tenancy_id of this LinkSummary.
        OCID of the parent tenancy.


        :return: The parent_tenancy_id of this LinkSummary.
        :rtype: str
        """
        return self._parent_tenancy_id

    @parent_tenancy_id.setter
    def parent_tenancy_id(self, parent_tenancy_id):
        """
        Sets the parent_tenancy_id of this LinkSummary.
        OCID of the parent tenancy.


        :param parent_tenancy_id: The parent_tenancy_id of this LinkSummary.
        :type: str
        """
        self._parent_tenancy_id = parent_tenancy_id

    @property
    def child_tenancy_id(self):
        """
        **[Required]** Gets the child_tenancy_id of this LinkSummary.
        OCID of the child tenancy.


        :return: The child_tenancy_id of this LinkSummary.
        :rtype: str
        """
        return self._child_tenancy_id

    @child_tenancy_id.setter
    def child_tenancy_id(self, child_tenancy_id):
        """
        Sets the child_tenancy_id of this LinkSummary.
        OCID of the child tenancy.


        :param child_tenancy_id: The child_tenancy_id of this LinkSummary.
        :type: str
        """
        self._child_tenancy_id = child_tenancy_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this LinkSummary.
        Lifecycle state of the link.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LinkSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LinkSummary.
        Lifecycle state of the link.


        :param lifecycle_state: The lifecycle_state of this LinkSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this LinkSummary.
        Date-time when this link was created


        :return: The time_created of this LinkSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LinkSummary.
        Date-time when this link was created


        :param time_created: The time_created of this LinkSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this LinkSummary.
        Date-time when this link was last updated.


        :return: The time_updated of this LinkSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LinkSummary.
        Date-time when this link was last updated.


        :param time_updated: The time_updated of this LinkSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_terminated(self):
        """
        Gets the time_terminated of this LinkSummary.
        Date-time when this link was terminated.


        :return: The time_terminated of this LinkSummary.
        :rtype: datetime
        """
        return self._time_terminated

    @time_terminated.setter
    def time_terminated(self, time_terminated):
        """
        Sets the time_terminated of this LinkSummary.
        Date-time when this link was terminated.


        :param time_terminated: The time_terminated of this LinkSummary.
        :type: datetime
        """
        self._time_terminated = time_terminated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
