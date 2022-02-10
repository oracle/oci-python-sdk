# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditArchiveRetrievalSummary(object):
    """
    Summary details of an archive retrieval.
    """

    #: A constant which can be used with the lifecycle_state property of a AuditArchiveRetrievalSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AuditArchiveRetrievalSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AuditArchiveRetrievalSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a AuditArchiveRetrievalSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AuditArchiveRetrievalSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AuditArchiveRetrievalSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new AuditArchiveRetrievalSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AuditArchiveRetrievalSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AuditArchiveRetrievalSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this AuditArchiveRetrievalSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this AuditArchiveRetrievalSummary.
        :type description: str

        :param start_date:
            The value to assign to the start_date property of this AuditArchiveRetrievalSummary.
        :type start_date: datetime

        :param end_date:
            The value to assign to the end_date property of this AuditArchiveRetrievalSummary.
        :type end_date: datetime

        :param target_id:
            The value to assign to the target_id property of this AuditArchiveRetrievalSummary.
        :type target_id: str

        :param time_requested:
            The value to assign to the time_requested property of this AuditArchiveRetrievalSummary.
        :type time_requested: datetime

        :param time_completed:
            The value to assign to the time_completed property of this AuditArchiveRetrievalSummary.
        :type time_completed: datetime

        :param time_of_expiry:
            The value to assign to the time_of_expiry property of this AuditArchiveRetrievalSummary.
        :type time_of_expiry: datetime

        :param audit_event_count:
            The value to assign to the audit_event_count property of this AuditArchiveRetrievalSummary.
        :type audit_event_count: int

        :param error_info:
            The value to assign to the error_info property of this AuditArchiveRetrievalSummary.
        :type error_info: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AuditArchiveRetrievalSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "NEEDS_ATTENTION", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AuditArchiveRetrievalSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AuditArchiveRetrievalSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AuditArchiveRetrievalSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'target_id': 'str',
            'time_requested': 'datetime',
            'time_completed': 'datetime',
            'time_of_expiry': 'datetime',
            'audit_event_count': 'int',
            'error_info': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'target_id': 'targetId',
            'time_requested': 'timeRequested',
            'time_completed': 'timeCompleted',
            'time_of_expiry': 'timeOfExpiry',
            'audit_event_count': 'auditEventCount',
            'error_info': 'errorInfo',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._start_date = None
        self._end_date = None
        self._target_id = None
        self._time_requested = None
        self._time_completed = None
        self._time_of_expiry = None
        self._audit_event_count = None
        self._error_info = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AuditArchiveRetrievalSummary.
        The OCID of the archive retrieval.


        :return: The id of this AuditArchiveRetrievalSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuditArchiveRetrievalSummary.
        The OCID of the archive retrieval.


        :param id: The id of this AuditArchiveRetrievalSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AuditArchiveRetrievalSummary.
        The OCID of the compartment that contains archive retrieval.


        :return: The compartment_id of this AuditArchiveRetrievalSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AuditArchiveRetrievalSummary.
        The OCID of the compartment that contains archive retrieval.


        :param compartment_id: The compartment_id of this AuditArchiveRetrievalSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AuditArchiveRetrievalSummary.
        The display name of the archive retrieval. The name does not have to be unique, and is changeable.


        :return: The display_name of this AuditArchiveRetrievalSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AuditArchiveRetrievalSummary.
        The display name of the archive retrieval. The name does not have to be unique, and is changeable.


        :param display_name: The display_name of this AuditArchiveRetrievalSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this AuditArchiveRetrievalSummary.
        Description of the archive retrieval.


        :return: The description of this AuditArchiveRetrievalSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AuditArchiveRetrievalSummary.
        Description of the archive retrieval.


        :param description: The description of this AuditArchiveRetrievalSummary.
        :type: str
        """
        self._description = description

    @property
    def start_date(self):
        """
        **[Required]** Gets the start_date of this AuditArchiveRetrievalSummary.
        Start month of the archive retrieval, in the format defined by RFC3339.


        :return: The start_date of this AuditArchiveRetrievalSummary.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this AuditArchiveRetrievalSummary.
        Start month of the archive retrieval, in the format defined by RFC3339.


        :param start_date: The start_date of this AuditArchiveRetrievalSummary.
        :type: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        **[Required]** Gets the end_date of this AuditArchiveRetrievalSummary.
        End month of the archive retrieval, in the format defined by RFC3339.


        :return: The end_date of this AuditArchiveRetrievalSummary.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this AuditArchiveRetrievalSummary.
        End month of the archive retrieval, in the format defined by RFC3339.


        :param end_date: The end_date of this AuditArchiveRetrievalSummary.
        :type: datetime
        """
        self._end_date = end_date

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this AuditArchiveRetrievalSummary.
        The OCID of the target associated with the archive retrieval.


        :return: The target_id of this AuditArchiveRetrievalSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this AuditArchiveRetrievalSummary.
        The OCID of the target associated with the archive retrieval.


        :param target_id: The target_id of this AuditArchiveRetrievalSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def time_requested(self):
        """
        Gets the time_requested of this AuditArchiveRetrievalSummary.
        The date time when archive retrieval was requested, in the format defined by RFC3339.


        :return: The time_requested of this AuditArchiveRetrievalSummary.
        :rtype: datetime
        """
        return self._time_requested

    @time_requested.setter
    def time_requested(self, time_requested):
        """
        Sets the time_requested of this AuditArchiveRetrievalSummary.
        The date time when archive retrieval was requested, in the format defined by RFC3339.


        :param time_requested: The time_requested of this AuditArchiveRetrievalSummary.
        :type: datetime
        """
        self._time_requested = time_requested

    @property
    def time_completed(self):
        """
        Gets the time_completed of this AuditArchiveRetrievalSummary.
        The date time when archive retrieval request was fulfilled, in the format defined by RFC3339.


        :return: The time_completed of this AuditArchiveRetrievalSummary.
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this AuditArchiveRetrievalSummary.
        The date time when archive retrieval request was fulfilled, in the format defined by RFC3339.


        :param time_completed: The time_completed of this AuditArchiveRetrievalSummary.
        :type: datetime
        """
        self._time_completed = time_completed

    @property
    def time_of_expiry(self):
        """
        Gets the time_of_expiry of this AuditArchiveRetrievalSummary.
        The date time when retrieved archive data will be deleted from Data Safe and unloaded back into archival.


        :return: The time_of_expiry of this AuditArchiveRetrievalSummary.
        :rtype: datetime
        """
        return self._time_of_expiry

    @time_of_expiry.setter
    def time_of_expiry(self, time_of_expiry):
        """
        Sets the time_of_expiry of this AuditArchiveRetrievalSummary.
        The date time when retrieved archive data will be deleted from Data Safe and unloaded back into archival.


        :param time_of_expiry: The time_of_expiry of this AuditArchiveRetrievalSummary.
        :type: datetime
        """
        self._time_of_expiry = time_of_expiry

    @property
    def audit_event_count(self):
        """
        Gets the audit_event_count of this AuditArchiveRetrievalSummary.
        Total retrieved archive records audit event count.


        :return: The audit_event_count of this AuditArchiveRetrievalSummary.
        :rtype: int
        """
        return self._audit_event_count

    @audit_event_count.setter
    def audit_event_count(self, audit_event_count):
        """
        Sets the audit_event_count of this AuditArchiveRetrievalSummary.
        Total retrieved archive records audit event count.


        :param audit_event_count: The audit_event_count of this AuditArchiveRetrievalSummary.
        :type: int
        """
        self._audit_event_count = audit_event_count

    @property
    def error_info(self):
        """
        Gets the error_info of this AuditArchiveRetrievalSummary.
        Error details of failed archive retrieval.


        :return: The error_info of this AuditArchiveRetrievalSummary.
        :rtype: str
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """
        Sets the error_info of this AuditArchiveRetrievalSummary.
        Error details of failed archive retrieval.


        :param error_info: The error_info of this AuditArchiveRetrievalSummary.
        :type: str
        """
        self._error_info = error_info

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AuditArchiveRetrievalSummary.
        The current state of the archive retrieval.

        Allowed values for this property are: "CREATING", "ACTIVE", "NEEDS_ATTENTION", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AuditArchiveRetrievalSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AuditArchiveRetrievalSummary.
        The current state of the archive retrieval.


        :param lifecycle_state: The lifecycle_state of this AuditArchiveRetrievalSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "NEEDS_ATTENTION", "FAILED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AuditArchiveRetrievalSummary.
        Details about the current state of the archive retrieval.


        :return: The lifecycle_details of this AuditArchiveRetrievalSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AuditArchiveRetrievalSummary.
        Details about the current state of the archive retrieval.


        :param lifecycle_details: The lifecycle_details of this AuditArchiveRetrievalSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AuditArchiveRetrievalSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AuditArchiveRetrievalSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AuditArchiveRetrievalSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AuditArchiveRetrievalSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AuditArchiveRetrievalSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AuditArchiveRetrievalSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AuditArchiveRetrievalSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AuditArchiveRetrievalSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
