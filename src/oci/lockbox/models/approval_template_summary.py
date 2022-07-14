# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApprovalTemplateSummary(object):
    """
    Summary info for an approval tmeplate.
    """

    #: A constant which can be used with the auto_approval_state property of a ApprovalTemplateSummary.
    #: This constant has a value of "ENABLED"
    AUTO_APPROVAL_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the auto_approval_state property of a ApprovalTemplateSummary.
    #: This constant has a value of "DISABLED"
    AUTO_APPROVAL_STATE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new ApprovalTemplateSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ApprovalTemplateSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ApprovalTemplateSummary.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ApprovalTemplateSummary.
        :type lifecycle_state: str

        :param approver_levels:
            The value to assign to the approver_levels property of this ApprovalTemplateSummary.
        :type approver_levels: oci.lockbox.models.ApproverLevels

        :param compartment_id:
            The value to assign to the compartment_id property of this ApprovalTemplateSummary.
        :type compartment_id: str

        :param auto_approval_state:
            The value to assign to the auto_approval_state property of this ApprovalTemplateSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type auto_approval_state: str

        :param time_created:
            The value to assign to the time_created property of this ApprovalTemplateSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ApprovalTemplateSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ApprovalTemplateSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ApprovalTemplateSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ApprovalTemplateSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'approver_levels': 'ApproverLevels',
            'compartment_id': 'str',
            'auto_approval_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'approver_levels': 'approverLevels',
            'compartment_id': 'compartmentId',
            'auto_approval_state': 'autoApprovalState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._lifecycle_state = None
        self._approver_levels = None
        self._compartment_id = None
        self._auto_approval_state = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ApprovalTemplateSummary.
        The unique identifier (OCID) of the approval template, which can't be changed after creation.


        :return: The id of this ApprovalTemplateSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ApprovalTemplateSummary.
        The unique identifier (OCID) of the approval template, which can't be changed after creation.


        :param id: The id of this ApprovalTemplateSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ApprovalTemplateSummary.
        The approval template display name.


        :return: The display_name of this ApprovalTemplateSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApprovalTemplateSummary.
        The approval template display name.


        :param display_name: The display_name of this ApprovalTemplateSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ApprovalTemplateSummary.
        The current state of the approval template.


        :return: The lifecycle_state of this ApprovalTemplateSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ApprovalTemplateSummary.
        The current state of the approval template.


        :param lifecycle_state: The lifecycle_state of this ApprovalTemplateSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def approver_levels(self):
        """
        **[Required]** Gets the approver_levels of this ApprovalTemplateSummary.

        :return: The approver_levels of this ApprovalTemplateSummary.
        :rtype: oci.lockbox.models.ApproverLevels
        """
        return self._approver_levels

    @approver_levels.setter
    def approver_levels(self, approver_levels):
        """
        Sets the approver_levels of this ApprovalTemplateSummary.

        :param approver_levels: The approver_levels of this ApprovalTemplateSummary.
        :type: oci.lockbox.models.ApproverLevels
        """
        self._approver_levels = approver_levels

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ApprovalTemplateSummary.
        The unique identifier (OCID) of the customer compartment where the approval template is located.


        :return: The compartment_id of this ApprovalTemplateSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ApprovalTemplateSummary.
        The unique identifier (OCID) of the customer compartment where the approval template is located.


        :param compartment_id: The compartment_id of this ApprovalTemplateSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def auto_approval_state(self):
        """
        Gets the auto_approval_state of this ApprovalTemplateSummary.
        The auto approval state of the lockbox.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The auto_approval_state of this ApprovalTemplateSummary.
        :rtype: str
        """
        return self._auto_approval_state

    @auto_approval_state.setter
    def auto_approval_state(self, auto_approval_state):
        """
        Sets the auto_approval_state of this ApprovalTemplateSummary.
        The auto approval state of the lockbox.


        :param auto_approval_state: The auto_approval_state of this ApprovalTemplateSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(auto_approval_state, allowed_values):
            auto_approval_state = 'UNKNOWN_ENUM_VALUE'
        self._auto_approval_state = auto_approval_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ApprovalTemplateSummary.
        The time the the approval template was created. An RFC3339 formatted datetime string


        :return: The time_created of this ApprovalTemplateSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ApprovalTemplateSummary.
        The time the the approval template was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this ApprovalTemplateSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ApprovalTemplateSummary.
        The time the approval template was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this ApprovalTemplateSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ApprovalTemplateSummary.
        The time the approval template was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this ApprovalTemplateSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ApprovalTemplateSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ApprovalTemplateSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ApprovalTemplateSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ApprovalTemplateSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ApprovalTemplateSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ApprovalTemplateSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ApprovalTemplateSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ApprovalTemplateSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ApprovalTemplateSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ApprovalTemplateSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ApprovalTemplateSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ApprovalTemplateSummary.
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
