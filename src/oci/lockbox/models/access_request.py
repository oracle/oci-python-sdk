# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessRequest(object):
    """
    An access request to a customer's resource.
    An access request is a subsidiary resource of the Lockbox entity.
    """

    #: A constant which can be used with the lifecycle_state property of a AccessRequest.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AccessRequest.
    #: This constant has a value of "WAITING"
    LIFECYCLE_STATE_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_state property of a AccessRequest.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequest.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a AccessRequest.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequest.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state_details property of a AccessRequest.
    #: This constant has a value of "PROCESSING"
    LIFECYCLE_STATE_DETAILS_PROCESSING = "PROCESSING"

    #: A constant which can be used with the lifecycle_state_details property of a AccessRequest.
    #: This constant has a value of "WAITING_FOR_APPROVALS"
    LIFECYCLE_STATE_DETAILS_WAITING_FOR_APPROVALS = "WAITING_FOR_APPROVALS"

    #: A constant which can be used with the lifecycle_state_details property of a AccessRequest.
    #: This constant has a value of "APPROVED"
    LIFECYCLE_STATE_DETAILS_APPROVED = "APPROVED"

    #: A constant which can be used with the lifecycle_state_details property of a AccessRequest.
    #: This constant has a value of "AUTO_APPROVED"
    LIFECYCLE_STATE_DETAILS_AUTO_APPROVED = "AUTO_APPROVED"

    #: A constant which can be used with the lifecycle_state_details property of a AccessRequest.
    #: This constant has a value of "CANCELLING_ACCESS"
    LIFECYCLE_STATE_DETAILS_CANCELLING_ACCESS = "CANCELLING_ACCESS"

    #: A constant which can be used with the lifecycle_state_details property of a AccessRequest.
    #: This constant has a value of "EXPIRED"
    LIFECYCLE_STATE_DETAILS_EXPIRED = "EXPIRED"

    #: A constant which can be used with the lifecycle_state_details property of a AccessRequest.
    #: This constant has a value of "REVOKED"
    LIFECYCLE_STATE_DETAILS_REVOKED = "REVOKED"

    #: A constant which can be used with the lifecycle_state_details property of a AccessRequest.
    #: This constant has a value of "DENIED"
    LIFECYCLE_STATE_DETAILS_DENIED = "DENIED"

    #: A constant which can be used with the lifecycle_state_details property of a AccessRequest.
    #: This constant has a value of "ERROR"
    LIFECYCLE_STATE_DETAILS_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new AccessRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AccessRequest.
        :type id: str

        :param lockbox_id:
            The value to assign to the lockbox_id property of this AccessRequest.
        :type lockbox_id: str

        :param display_name:
            The value to assign to the display_name property of this AccessRequest.
        :type display_name: str

        :param description:
            The value to assign to the description property of this AccessRequest.
        :type description: str

        :param requestor_id:
            The value to assign to the requestor_id property of this AccessRequest.
        :type requestor_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AccessRequest.
            Allowed values for this property are: "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this AccessRequest.
            Allowed values for this property are: "PROCESSING", "WAITING_FOR_APPROVALS", "APPROVED", "AUTO_APPROVED", "CANCELLING_ACCESS", "EXPIRED", "REVOKED", "DENIED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state_details: str

        :param access_duration:
            The value to assign to the access_duration property of this AccessRequest.
        :type access_duration: str

        :param context:
            The value to assign to the context property of this AccessRequest.
        :type context: dict(str, str)

        :param activity_logs:
            The value to assign to the activity_logs property of this AccessRequest.
        :type activity_logs: list[oci.lockbox.models.ActivityLog]

        :param time_created:
            The value to assign to the time_created property of this AccessRequest.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AccessRequest.
        :type time_updated: datetime

        :param time_expired:
            The value to assign to the time_expired property of this AccessRequest.
        :type time_expired: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'lockbox_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'requestor_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'access_duration': 'str',
            'context': 'dict(str, str)',
            'activity_logs': 'list[ActivityLog]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_expired': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'lockbox_id': 'lockboxId',
            'display_name': 'displayName',
            'description': 'description',
            'requestor_id': 'requestorId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'access_duration': 'accessDuration',
            'context': 'context',
            'activity_logs': 'activityLogs',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_expired': 'timeExpired'
        }

        self._id = None
        self._lockbox_id = None
        self._display_name = None
        self._description = None
        self._requestor_id = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._access_duration = None
        self._context = None
        self._activity_logs = None
        self._time_created = None
        self._time_updated = None
        self._time_expired = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AccessRequest.
        The unique identifier (OCID) of the access request, which can't be changed after creation.


        :return: The id of this AccessRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AccessRequest.
        The unique identifier (OCID) of the access request, which can't be changed after creation.


        :param id: The id of this AccessRequest.
        :type: str
        """
        self._id = id

    @property
    def lockbox_id(self):
        """
        **[Required]** Gets the lockbox_id of this AccessRequest.
        The unique identifier (OCID) of the lockbox box that the access request is associated with, which can't be changed after creation.


        :return: The lockbox_id of this AccessRequest.
        :rtype: str
        """
        return self._lockbox_id

    @lockbox_id.setter
    def lockbox_id(self, lockbox_id):
        """
        Sets the lockbox_id of this AccessRequest.
        The unique identifier (OCID) of the lockbox box that the access request is associated with, which can't be changed after creation.


        :param lockbox_id: The lockbox_id of this AccessRequest.
        :type: str
        """
        self._lockbox_id = lockbox_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AccessRequest.
        The name of the access request.


        :return: The display_name of this AccessRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AccessRequest.
        The name of the access request.


        :param display_name: The display_name of this AccessRequest.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this AccessRequest.
        The rationale for requesting the access request and any other related details..


        :return: The description of this AccessRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AccessRequest.
        The rationale for requesting the access request and any other related details..


        :param description: The description of this AccessRequest.
        :type: str
        """
        self._description = description

    @property
    def requestor_id(self):
        """
        **[Required]** Gets the requestor_id of this AccessRequest.
        The unique identifier of the requestor.


        :return: The requestor_id of this AccessRequest.
        :rtype: str
        """
        return self._requestor_id

    @requestor_id.setter
    def requestor_id(self, requestor_id):
        """
        Sets the requestor_id of this AccessRequest.
        The unique identifier of the requestor.


        :param requestor_id: The requestor_id of this AccessRequest.
        :type: str
        """
        self._requestor_id = requestor_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AccessRequest.
        Possible access request lifecycle states.

        Allowed values for this property are: "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AccessRequest.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AccessRequest.
        Possible access request lifecycle states.


        :param lifecycle_state: The lifecycle_state of this AccessRequest.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        **[Required]** Gets the lifecycle_state_details of this AccessRequest.
        Details of access request lifecycle state.

        Allowed values for this property are: "PROCESSING", "WAITING_FOR_APPROVALS", "APPROVED", "AUTO_APPROVED", "CANCELLING_ACCESS", "EXPIRED", "REVOKED", "DENIED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state_details of this AccessRequest.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this AccessRequest.
        Details of access request lifecycle state.


        :param lifecycle_state_details: The lifecycle_state_details of this AccessRequest.
        :type: str
        """
        allowed_values = ["PROCESSING", "WAITING_FOR_APPROVALS", "APPROVED", "AUTO_APPROVED", "CANCELLING_ACCESS", "EXPIRED", "REVOKED", "DENIED", "ERROR"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state_details, allowed_values):
            lifecycle_state_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def access_duration(self):
        """
        **[Required]** Gets the access_duration of this AccessRequest.
        The maximum amount of time operator has access to associated resources.


        :return: The access_duration of this AccessRequest.
        :rtype: str
        """
        return self._access_duration

    @access_duration.setter
    def access_duration(self, access_duration):
        """
        Sets the access_duration of this AccessRequest.
        The maximum amount of time operator has access to associated resources.


        :param access_duration: The access_duration of this AccessRequest.
        :type: str
        """
        self._access_duration = access_duration

    @property
    def context(self):
        """
        Gets the context of this AccessRequest.
        The context object containing the access request specific details.


        :return: The context of this AccessRequest.
        :rtype: dict(str, str)
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this AccessRequest.
        The context object containing the access request specific details.


        :param context: The context of this AccessRequest.
        :type: dict(str, str)
        """
        self._context = context

    @property
    def activity_logs(self):
        """
        **[Required]** Gets the activity_logs of this AccessRequest.
        The actions taken by different persona on the access request, e.g. approve/deny/revoke


        :return: The activity_logs of this AccessRequest.
        :rtype: list[oci.lockbox.models.ActivityLog]
        """
        return self._activity_logs

    @activity_logs.setter
    def activity_logs(self, activity_logs):
        """
        Sets the activity_logs of this AccessRequest.
        The actions taken by different persona on the access request, e.g. approve/deny/revoke


        :param activity_logs: The activity_logs of this AccessRequest.
        :type: list[oci.lockbox.models.ActivityLog]
        """
        self._activity_logs = activity_logs

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AccessRequest.
        The time the access request was created. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this AccessRequest.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AccessRequest.
        The time the access request was created. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this AccessRequest.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AccessRequest.
        The time the access request was last updated. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this AccessRequest.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AccessRequest.
        The time the access request was last updated. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this AccessRequest.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_expired(self):
        """
        **[Required]** Gets the time_expired of this AccessRequest.
        The time the access request expired. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_expired of this AccessRequest.
        :rtype: datetime
        """
        return self._time_expired

    @time_expired.setter
    def time_expired(self, time_expired):
        """
        Sets the time_expired of this AccessRequest.
        The time the access request expired. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_expired: The time_expired of this AccessRequest.
        :type: datetime
        """
        self._time_expired = time_expired

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
