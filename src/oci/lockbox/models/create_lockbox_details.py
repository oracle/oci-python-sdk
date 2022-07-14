# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateLockboxDetails(object):
    """
    The information about new Lockbox.
    """

    #: A constant which can be used with the lockbox_partner property of a CreateLockboxDetails.
    #: This constant has a value of "FAAAS"
    LOCKBOX_PARTNER_FAAAS = "FAAAS"

    #: A constant which can be used with the lockbox_partner property of a CreateLockboxDetails.
    #: This constant has a value of "CANARY"
    LOCKBOX_PARTNER_CANARY = "CANARY"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateLockboxDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateLockboxDetails.
        :type display_name: str

        :param resource_id:
            The value to assign to the resource_id property of this CreateLockboxDetails.
        :type resource_id: str

        :param lockbox_partner:
            The value to assign to the lockbox_partner property of this CreateLockboxDetails.
            Allowed values for this property are: "FAAAS", "CANARY"
        :type lockbox_partner: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateLockboxDetails.
        :type compartment_id: str

        :param partner_compartment_id:
            The value to assign to the partner_compartment_id property of this CreateLockboxDetails.
        :type partner_compartment_id: str

        :param approval_template_id:
            The value to assign to the approval_template_id property of this CreateLockboxDetails.
        :type approval_template_id: str

        :param max_access_duration:
            The value to assign to the max_access_duration property of this CreateLockboxDetails.
        :type max_access_duration: str

        :param access_context_attributes:
            The value to assign to the access_context_attributes property of this CreateLockboxDetails.
        :type access_context_attributes: oci.lockbox.models.AccessContextAttributeCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateLockboxDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateLockboxDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'resource_id': 'str',
            'lockbox_partner': 'str',
            'compartment_id': 'str',
            'partner_compartment_id': 'str',
            'approval_template_id': 'str',
            'max_access_duration': 'str',
            'access_context_attributes': 'AccessContextAttributeCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'resource_id': 'resourceId',
            'lockbox_partner': 'lockboxPartner',
            'compartment_id': 'compartmentId',
            'partner_compartment_id': 'partnerCompartmentId',
            'approval_template_id': 'approvalTemplateId',
            'max_access_duration': 'maxAccessDuration',
            'access_context_attributes': 'accessContextAttributes',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._resource_id = None
        self._lockbox_partner = None
        self._compartment_id = None
        self._partner_compartment_id = None
        self._approval_template_id = None
        self._max_access_duration = None
        self._access_context_attributes = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateLockboxDetails.
        Lockbox Identifier


        :return: The display_name of this CreateLockboxDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateLockboxDetails.
        Lockbox Identifier


        :param display_name: The display_name of this CreateLockboxDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this CreateLockboxDetails.
        The unique identifier (OCID) of the customer's resource.


        :return: The resource_id of this CreateLockboxDetails.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this CreateLockboxDetails.
        The unique identifier (OCID) of the customer's resource.


        :param resource_id: The resource_id of this CreateLockboxDetails.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def lockbox_partner(self):
        """
        **[Required]** Gets the lockbox_partner of this CreateLockboxDetails.
        The partner using this lockbox to lock a resource.

        Allowed values for this property are: "FAAAS", "CANARY"


        :return: The lockbox_partner of this CreateLockboxDetails.
        :rtype: str
        """
        return self._lockbox_partner

    @lockbox_partner.setter
    def lockbox_partner(self, lockbox_partner):
        """
        Sets the lockbox_partner of this CreateLockboxDetails.
        The partner using this lockbox to lock a resource.


        :param lockbox_partner: The lockbox_partner of this CreateLockboxDetails.
        :type: str
        """
        allowed_values = ["FAAAS", "CANARY"]
        if not value_allowed_none_or_none_sentinel(lockbox_partner, allowed_values):
            raise ValueError(
                "Invalid value for `lockbox_partner`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lockbox_partner = lockbox_partner

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateLockboxDetails.
        The unique identifier (OCID) of the compartment where the resource is located.


        :return: The compartment_id of this CreateLockboxDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateLockboxDetails.
        The unique identifier (OCID) of the compartment where the resource is located.


        :param compartment_id: The compartment_id of this CreateLockboxDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def partner_compartment_id(self):
        """
        **[Required]** Gets the partner_compartment_id of this CreateLockboxDetails.
        Compartment Identifier


        :return: The partner_compartment_id of this CreateLockboxDetails.
        :rtype: str
        """
        return self._partner_compartment_id

    @partner_compartment_id.setter
    def partner_compartment_id(self, partner_compartment_id):
        """
        Sets the partner_compartment_id of this CreateLockboxDetails.
        Compartment Identifier


        :param partner_compartment_id: The partner_compartment_id of this CreateLockboxDetails.
        :type: str
        """
        self._partner_compartment_id = partner_compartment_id

    @property
    def approval_template_id(self):
        """
        Gets the approval_template_id of this CreateLockboxDetails.
        Approval template ID


        :return: The approval_template_id of this CreateLockboxDetails.
        :rtype: str
        """
        return self._approval_template_id

    @approval_template_id.setter
    def approval_template_id(self, approval_template_id):
        """
        Sets the approval_template_id of this CreateLockboxDetails.
        Approval template ID


        :param approval_template_id: The approval_template_id of this CreateLockboxDetails.
        :type: str
        """
        self._approval_template_id = approval_template_id

    @property
    def max_access_duration(self):
        """
        Gets the max_access_duration of this CreateLockboxDetails.
        The maximum amount of time operator has access to associated resources.


        :return: The max_access_duration of this CreateLockboxDetails.
        :rtype: str
        """
        return self._max_access_duration

    @max_access_duration.setter
    def max_access_duration(self, max_access_duration):
        """
        Sets the max_access_duration of this CreateLockboxDetails.
        The maximum amount of time operator has access to associated resources.


        :param max_access_duration: The max_access_duration of this CreateLockboxDetails.
        :type: str
        """
        self._max_access_duration = max_access_duration

    @property
    def access_context_attributes(self):
        """
        **[Required]** Gets the access_context_attributes of this CreateLockboxDetails.

        :return: The access_context_attributes of this CreateLockboxDetails.
        :rtype: oci.lockbox.models.AccessContextAttributeCollection
        """
        return self._access_context_attributes

    @access_context_attributes.setter
    def access_context_attributes(self, access_context_attributes):
        """
        Sets the access_context_attributes of this CreateLockboxDetails.

        :param access_context_attributes: The access_context_attributes of this CreateLockboxDetails.
        :type: oci.lockbox.models.AccessContextAttributeCollection
        """
        self._access_context_attributes = access_context_attributes

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateLockboxDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateLockboxDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateLockboxDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateLockboxDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateLockboxDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateLockboxDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateLockboxDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateLockboxDetails.
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
