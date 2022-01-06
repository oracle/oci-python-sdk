# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnrollmentStatus(object):
    """
    The metadata associated with the enrollment status.
    """

    #: A constant which can be used with the lifecycle_state property of a EnrollmentStatus.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a EnrollmentStatus.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a EnrollmentStatus.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a EnrollmentStatus.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a EnrollmentStatus.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    #: A constant which can be used with the lifecycle_state property of a EnrollmentStatus.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a EnrollmentStatus.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a EnrollmentStatus.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a EnrollmentStatus.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the status property of a EnrollmentStatus.
    #: This constant has a value of "ACTIVE"
    STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the status property of a EnrollmentStatus.
    #: This constant has a value of "INACTIVE"
    STATUS_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new EnrollmentStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this EnrollmentStatus.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EnrollmentStatus.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EnrollmentStatus.
            Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param status:
            The value to assign to the status property of this EnrollmentStatus.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param status_reason:
            The value to assign to the status_reason property of this EnrollmentStatus.
        :type status_reason: str

        :param time_created:
            The value to assign to the time_created property of this EnrollmentStatus.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EnrollmentStatus.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'status': 'str',
            'status_reason': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'status': 'status',
            'status_reason': 'statusReason',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._status = None
        self._status_reason = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this EnrollmentStatus.
        The OCID of the enrollment status.


        :return: The id of this EnrollmentStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EnrollmentStatus.
        The OCID of the enrollment status.


        :param id: The id of this EnrollmentStatus.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EnrollmentStatus.
        The OCID of the compartment.


        :return: The compartment_id of this EnrollmentStatus.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EnrollmentStatus.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this EnrollmentStatus.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this EnrollmentStatus.
        The enrollment status' current state.

        Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this EnrollmentStatus.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EnrollmentStatus.
        The enrollment status' current state.


        :param lifecycle_state: The lifecycle_state of this EnrollmentStatus.
        :type: str
        """
        allowed_values = ["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def status(self):
        """
        **[Required]** Gets the status of this EnrollmentStatus.
        The current Cloud Advisor enrollment status.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this EnrollmentStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this EnrollmentStatus.
        The current Cloud Advisor enrollment status.


        :param status: The status of this EnrollmentStatus.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def status_reason(self):
        """
        Gets the status_reason of this EnrollmentStatus.
        The reason for the enrollment status of the tenancy.


        :return: The status_reason of this EnrollmentStatus.
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """
        Sets the status_reason of this EnrollmentStatus.
        The reason for the enrollment status of the tenancy.


        :param status_reason: The status_reason of this EnrollmentStatus.
        :type: str
        """
        self._status_reason = status_reason

    @property
    def time_created(self):
        """
        Gets the time_created of this EnrollmentStatus.
        The date and time the enrollment status was created, in the format defined by RFC3339.


        :return: The time_created of this EnrollmentStatus.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EnrollmentStatus.
        The date and time the enrollment status was created, in the format defined by RFC3339.


        :param time_created: The time_created of this EnrollmentStatus.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this EnrollmentStatus.
        The date and time the enrollment status was last updated, in the format defined by RFC3339.


        :return: The time_updated of this EnrollmentStatus.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EnrollmentStatus.
        The date and time the enrollment status was last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this EnrollmentStatus.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
