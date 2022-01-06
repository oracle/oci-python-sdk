# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SessionSummary(object):
    """
    Summary information for a bastion session resource.
    """

    #: A constant which can be used with the lifecycle_state property of a SessionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SessionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SessionSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SessionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SessionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SessionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SessionSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this SessionSummary.
        :type display_name: str

        :param bastion_name:
            The value to assign to the bastion_name property of this SessionSummary.
        :type bastion_name: str

        :param bastion_id:
            The value to assign to the bastion_id property of this SessionSummary.
        :type bastion_id: str

        :param target_resource_details:
            The value to assign to the target_resource_details property of this SessionSummary.
        :type target_resource_details: oci.bastion.models.TargetResourceDetails

        :param time_created:
            The value to assign to the time_created property of this SessionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SessionSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SessionSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SessionSummary.
        :type lifecycle_details: str

        :param session_ttl_in_seconds:
            The value to assign to the session_ttl_in_seconds property of this SessionSummary.
        :type session_ttl_in_seconds: int

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'bastion_name': 'str',
            'bastion_id': 'str',
            'target_resource_details': 'TargetResourceDetails',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'session_ttl_in_seconds': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'bastion_name': 'bastionName',
            'bastion_id': 'bastionId',
            'target_resource_details': 'targetResourceDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'session_ttl_in_seconds': 'sessionTtlInSeconds'
        }

        self._id = None
        self._display_name = None
        self._bastion_name = None
        self._bastion_id = None
        self._target_resource_details = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._session_ttl_in_seconds = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SessionSummary.
        The unique identifier (OCID) of the session, which can't be changed after creation.


        :return: The id of this SessionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SessionSummary.
        The unique identifier (OCID) of the session, which can't be changed after creation.


        :param id: The id of this SessionSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this SessionSummary.
        The name of the session.


        :return: The display_name of this SessionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SessionSummary.
        The name of the session.


        :param display_name: The display_name of this SessionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def bastion_name(self):
        """
        **[Required]** Gets the bastion_name of this SessionSummary.
        The name of the bastion that is hosting this session.


        :return: The bastion_name of this SessionSummary.
        :rtype: str
        """
        return self._bastion_name

    @bastion_name.setter
    def bastion_name(self, bastion_name):
        """
        Sets the bastion_name of this SessionSummary.
        The name of the bastion that is hosting this session.


        :param bastion_name: The bastion_name of this SessionSummary.
        :type: str
        """
        self._bastion_name = bastion_name

    @property
    def bastion_id(self):
        """
        **[Required]** Gets the bastion_id of this SessionSummary.
        The unique identifier (OCID) of the bastion that is hosting this session.


        :return: The bastion_id of this SessionSummary.
        :rtype: str
        """
        return self._bastion_id

    @bastion_id.setter
    def bastion_id(self, bastion_id):
        """
        Sets the bastion_id of this SessionSummary.
        The unique identifier (OCID) of the bastion that is hosting this session.


        :param bastion_id: The bastion_id of this SessionSummary.
        :type: str
        """
        self._bastion_id = bastion_id

    @property
    def target_resource_details(self):
        """
        **[Required]** Gets the target_resource_details of this SessionSummary.

        :return: The target_resource_details of this SessionSummary.
        :rtype: oci.bastion.models.TargetResourceDetails
        """
        return self._target_resource_details

    @target_resource_details.setter
    def target_resource_details(self, target_resource_details):
        """
        Sets the target_resource_details of this SessionSummary.

        :param target_resource_details: The target_resource_details of this SessionSummary.
        :type: oci.bastion.models.TargetResourceDetails
        """
        self._target_resource_details = target_resource_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SessionSummary.
        The time the session was created. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this SessionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SessionSummary.
        The time the session was created. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this SessionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this SessionSummary.
        The time the session was updated. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this SessionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SessionSummary.
        The time the session was updated. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this SessionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SessionSummary.
        The current state of the session.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SessionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SessionSummary.
        The current state of the session.


        :param lifecycle_state: The lifecycle_state of this SessionSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this SessionSummary.
        A message describing the current session state in more detail.


        :return: The lifecycle_details of this SessionSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SessionSummary.
        A message describing the current session state in more detail.


        :param lifecycle_details: The lifecycle_details of this SessionSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def session_ttl_in_seconds(self):
        """
        **[Required]** Gets the session_ttl_in_seconds of this SessionSummary.
        The amount of time the session can remain active.


        :return: The session_ttl_in_seconds of this SessionSummary.
        :rtype: int
        """
        return self._session_ttl_in_seconds

    @session_ttl_in_seconds.setter
    def session_ttl_in_seconds(self, session_ttl_in_seconds):
        """
        Sets the session_ttl_in_seconds of this SessionSummary.
        The amount of time the session can remain active.


        :param session_ttl_in_seconds: The session_ttl_in_seconds of this SessionSummary.
        :type: int
        """
        self._session_ttl_in_seconds = session_ttl_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
