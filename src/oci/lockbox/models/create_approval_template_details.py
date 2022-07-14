# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateApprovalTemplateDetails(object):
    """
    The configuration details for a new approval template.
    """

    #: A constant which can be used with the auto_approval_state property of a CreateApprovalTemplateDetails.
    #: This constant has a value of "ENABLED"
    AUTO_APPROVAL_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the auto_approval_state property of a CreateApprovalTemplateDetails.
    #: This constant has a value of "DISABLED"
    AUTO_APPROVAL_STATE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateApprovalTemplateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateApprovalTemplateDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateApprovalTemplateDetails.
        :type display_name: str

        :param approver_levels:
            The value to assign to the approver_levels property of this CreateApprovalTemplateDetails.
        :type approver_levels: oci.lockbox.models.ApproverLevels

        :param auto_approval_state:
            The value to assign to the auto_approval_state property of this CreateApprovalTemplateDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type auto_approval_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateApprovalTemplateDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateApprovalTemplateDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'approver_levels': 'ApproverLevels',
            'auto_approval_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'approver_levels': 'approverLevels',
            'auto_approval_state': 'autoApprovalState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._approver_levels = None
        self._auto_approval_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateApprovalTemplateDetails.
        The unique identifier (OCID) of the compartment where the resource is located.


        :return: The compartment_id of this CreateApprovalTemplateDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateApprovalTemplateDetails.
        The unique identifier (OCID) of the compartment where the resource is located.


        :param compartment_id: The compartment_id of this CreateApprovalTemplateDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateApprovalTemplateDetails.
        approval template identifier


        :return: The display_name of this CreateApprovalTemplateDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateApprovalTemplateDetails.
        approval template identifier


        :param display_name: The display_name of this CreateApprovalTemplateDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def approver_levels(self):
        """
        **[Required]** Gets the approver_levels of this CreateApprovalTemplateDetails.

        :return: The approver_levels of this CreateApprovalTemplateDetails.
        :rtype: oci.lockbox.models.ApproverLevels
        """
        return self._approver_levels

    @approver_levels.setter
    def approver_levels(self, approver_levels):
        """
        Sets the approver_levels of this CreateApprovalTemplateDetails.

        :param approver_levels: The approver_levels of this CreateApprovalTemplateDetails.
        :type: oci.lockbox.models.ApproverLevels
        """
        self._approver_levels = approver_levels

    @property
    def auto_approval_state(self):
        """
        Gets the auto_approval_state of this CreateApprovalTemplateDetails.
        The auto approval state of the lockbox.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The auto_approval_state of this CreateApprovalTemplateDetails.
        :rtype: str
        """
        return self._auto_approval_state

    @auto_approval_state.setter
    def auto_approval_state(self, auto_approval_state):
        """
        Sets the auto_approval_state of this CreateApprovalTemplateDetails.
        The auto approval state of the lockbox.


        :param auto_approval_state: The auto_approval_state of this CreateApprovalTemplateDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(auto_approval_state, allowed_values):
            raise ValueError(
                "Invalid value for `auto_approval_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._auto_approval_state = auto_approval_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateApprovalTemplateDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateApprovalTemplateDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateApprovalTemplateDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateApprovalTemplateDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateApprovalTemplateDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateApprovalTemplateDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateApprovalTemplateDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateApprovalTemplateDetails.
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
