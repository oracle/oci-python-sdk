# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecipientInvitation(object):
    """
    The invitation model that the recipient owns.
    """

    #: A constant which can be used with the lifecycle_state property of a RecipientInvitation.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a RecipientInvitation.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RecipientInvitation.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RecipientInvitation.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a RecipientInvitation.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a RecipientInvitation.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the status property of a RecipientInvitation.
    #: This constant has a value of "PENDING"
    STATUS_PENDING = "PENDING"

    #: A constant which can be used with the status property of a RecipientInvitation.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a RecipientInvitation.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a RecipientInvitation.
    #: This constant has a value of "IGNORED"
    STATUS_IGNORED = "IGNORED"

    #: A constant which can be used with the status property of a RecipientInvitation.
    #: This constant has a value of "EXPIRED"
    STATUS_EXPIRED = "EXPIRED"

    #: A constant which can be used with the status property of a RecipientInvitation.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new RecipientInvitation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RecipientInvitation.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RecipientInvitation.
        :type compartment_id: str

        :param sender_invitation_id:
            The value to assign to the sender_invitation_id property of this RecipientInvitation.
        :type sender_invitation_id: str

        :param sender_tenancy_id:
            The value to assign to the sender_tenancy_id property of this RecipientInvitation.
        :type sender_tenancy_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RecipientInvitation.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param status:
            The value to assign to the status property of this RecipientInvitation.
            Allowed values for this property are: "PENDING", "CANCELED", "ACCEPTED", "IGNORED", "EXPIRED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param display_name:
            The value to assign to the display_name property of this RecipientInvitation.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this RecipientInvitation.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RecipientInvitation.
        :type time_updated: datetime

        :param recipient_email_address:
            The value to assign to the recipient_email_address property of this RecipientInvitation.
        :type recipient_email_address: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RecipientInvitation.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RecipientInvitation.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this RecipientInvitation.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'sender_invitation_id': 'str',
            'sender_tenancy_id': 'str',
            'lifecycle_state': 'str',
            'status': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'recipient_email_address': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'sender_invitation_id': 'senderInvitationId',
            'sender_tenancy_id': 'senderTenancyId',
            'lifecycle_state': 'lifecycleState',
            'status': 'status',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'recipient_email_address': 'recipientEmailAddress',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._sender_invitation_id = None
        self._sender_tenancy_id = None
        self._lifecycle_state = None
        self._status = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._recipient_email_address = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RecipientInvitation.
        OCID of the recipient invitation.


        :return: The id of this RecipientInvitation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RecipientInvitation.
        OCID of the recipient invitation.


        :param id: The id of this RecipientInvitation.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RecipientInvitation.
        OCID of the recipient tenancy.


        :return: The compartment_id of this RecipientInvitation.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RecipientInvitation.
        OCID of the recipient tenancy.


        :param compartment_id: The compartment_id of this RecipientInvitation.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def sender_invitation_id(self):
        """
        **[Required]** Gets the sender_invitation_id of this RecipientInvitation.
        OCID of the corresponding sender invitation.


        :return: The sender_invitation_id of this RecipientInvitation.
        :rtype: str
        """
        return self._sender_invitation_id

    @sender_invitation_id.setter
    def sender_invitation_id(self, sender_invitation_id):
        """
        Sets the sender_invitation_id of this RecipientInvitation.
        OCID of the corresponding sender invitation.


        :param sender_invitation_id: The sender_invitation_id of this RecipientInvitation.
        :type: str
        """
        self._sender_invitation_id = sender_invitation_id

    @property
    def sender_tenancy_id(self):
        """
        **[Required]** Gets the sender_tenancy_id of this RecipientInvitation.
        OCID of the sender tenancy.


        :return: The sender_tenancy_id of this RecipientInvitation.
        :rtype: str
        """
        return self._sender_tenancy_id

    @sender_tenancy_id.setter
    def sender_tenancy_id(self, sender_tenancy_id):
        """
        Sets the sender_tenancy_id of this RecipientInvitation.
        OCID of the sender tenancy.


        :param sender_tenancy_id: The sender_tenancy_id of this RecipientInvitation.
        :type: str
        """
        self._sender_tenancy_id = sender_tenancy_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RecipientInvitation.
        Lifecycle state of the recipient invitation.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RecipientInvitation.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RecipientInvitation.
        Lifecycle state of the recipient invitation.


        :param lifecycle_state: The lifecycle_state of this RecipientInvitation.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def status(self):
        """
        **[Required]** Gets the status of this RecipientInvitation.
        Status of the recipient invitation.

        Allowed values for this property are: "PENDING", "CANCELED", "ACCEPTED", "IGNORED", "EXPIRED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this RecipientInvitation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RecipientInvitation.
        Status of the recipient invitation.


        :param status: The status of this RecipientInvitation.
        :type: str
        """
        allowed_values = ["PENDING", "CANCELED", "ACCEPTED", "IGNORED", "EXPIRED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def display_name(self):
        """
        Gets the display_name of this RecipientInvitation.
        A user-created name to describe the invitation.


        :return: The display_name of this RecipientInvitation.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RecipientInvitation.
        A user-created name to describe the invitation.


        :param display_name: The display_name of this RecipientInvitation.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this RecipientInvitation.
        Date-time when this recipient invitation was created.


        :return: The time_created of this RecipientInvitation.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RecipientInvitation.
        Date-time when this recipient invitation was created.


        :param time_created: The time_created of this RecipientInvitation.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this RecipientInvitation.
        Date-time when this recipient invitation was last updated.


        :return: The time_updated of this RecipientInvitation.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RecipientInvitation.
        Date-time when this recipient invitation was last updated.


        :param time_updated: The time_updated of this RecipientInvitation.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def recipient_email_address(self):
        """
        Gets the recipient_email_address of this RecipientInvitation.
        Email address of the recipient.


        :return: The recipient_email_address of this RecipientInvitation.
        :rtype: str
        """
        return self._recipient_email_address

    @recipient_email_address.setter
    def recipient_email_address(self, recipient_email_address):
        """
        Sets the recipient_email_address of this RecipientInvitation.
        Email address of the recipient.


        :param recipient_email_address: The recipient_email_address of this RecipientInvitation.
        :type: str
        """
        self._recipient_email_address = recipient_email_address

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RecipientInvitation.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this RecipientInvitation.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RecipientInvitation.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this RecipientInvitation.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RecipientInvitation.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this RecipientInvitation.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RecipientInvitation.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this RecipientInvitation.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this RecipientInvitation.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this RecipientInvitation.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this RecipientInvitation.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this RecipientInvitation.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
