# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSenderInvitationDetails(object):
    """
    The parameters for creating a sender invitation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSenderInvitationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSenderInvitationDetails.
        :type compartment_id: str

        :param recipient_tenancy_id:
            The value to assign to the recipient_tenancy_id property of this CreateSenderInvitationDetails.
        :type recipient_tenancy_id: str

        :param recipient_email_address:
            The value to assign to the recipient_email_address property of this CreateSenderInvitationDetails.
        :type recipient_email_address: str

        :param display_name:
            The value to assign to the display_name property of this CreateSenderInvitationDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSenderInvitationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSenderInvitationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'recipient_tenancy_id': 'str',
            'recipient_email_address': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'recipient_tenancy_id': 'recipientTenancyId',
            'recipient_email_address': 'recipientEmailAddress',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._recipient_tenancy_id = None
        self._recipient_email_address = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSenderInvitationDetails.
        OCID of the sender tenancy.


        :return: The compartment_id of this CreateSenderInvitationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSenderInvitationDetails.
        OCID of the sender tenancy.


        :param compartment_id: The compartment_id of this CreateSenderInvitationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def recipient_tenancy_id(self):
        """
        **[Required]** Gets the recipient_tenancy_id of this CreateSenderInvitationDetails.
        OCID of the recipient tenancy.


        :return: The recipient_tenancy_id of this CreateSenderInvitationDetails.
        :rtype: str
        """
        return self._recipient_tenancy_id

    @recipient_tenancy_id.setter
    def recipient_tenancy_id(self, recipient_tenancy_id):
        """
        Sets the recipient_tenancy_id of this CreateSenderInvitationDetails.
        OCID of the recipient tenancy.


        :param recipient_tenancy_id: The recipient_tenancy_id of this CreateSenderInvitationDetails.
        :type: str
        """
        self._recipient_tenancy_id = recipient_tenancy_id

    @property
    def recipient_email_address(self):
        """
        Gets the recipient_email_address of this CreateSenderInvitationDetails.
        Email address of the recipient.


        :return: The recipient_email_address of this CreateSenderInvitationDetails.
        :rtype: str
        """
        return self._recipient_email_address

    @recipient_email_address.setter
    def recipient_email_address(self, recipient_email_address):
        """
        Sets the recipient_email_address of this CreateSenderInvitationDetails.
        Email address of the recipient.


        :param recipient_email_address: The recipient_email_address of this CreateSenderInvitationDetails.
        :type: str
        """
        self._recipient_email_address = recipient_email_address

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateSenderInvitationDetails.
        A user-created name to describe the invitation. Avoid entering confidential information.


        :return: The display_name of this CreateSenderInvitationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSenderInvitationDetails.
        A user-created name to describe the invitation. Avoid entering confidential information.


        :param display_name: The display_name of this CreateSenderInvitationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSenderInvitationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateSenderInvitationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSenderInvitationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateSenderInvitationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSenderInvitationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateSenderInvitationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSenderInvitationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateSenderInvitationDetails.
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
