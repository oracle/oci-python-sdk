# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTermDetails(object):
    """
    Properties used in term create operations.
    """

    #: A constant which can be used with the workflow_status property of a CreateTermDetails.
    #: This constant has a value of "NEW"
    WORKFLOW_STATUS_NEW = "NEW"

    #: A constant which can be used with the workflow_status property of a CreateTermDetails.
    #: This constant has a value of "APPROVED"
    WORKFLOW_STATUS_APPROVED = "APPROVED"

    #: A constant which can be used with the workflow_status property of a CreateTermDetails.
    #: This constant has a value of "UNDER_REVIEW"
    WORKFLOW_STATUS_UNDER_REVIEW = "UNDER_REVIEW"

    #: A constant which can be used with the workflow_status property of a CreateTermDetails.
    #: This constant has a value of "ESCALATED"
    WORKFLOW_STATUS_ESCALATED = "ESCALATED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTermDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateTermDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateTermDetails.
        :type description: str

        :param is_allowed_to_have_child_terms:
            The value to assign to the is_allowed_to_have_child_terms property of this CreateTermDetails.
        :type is_allowed_to_have_child_terms: bool

        :param parent_term_key:
            The value to assign to the parent_term_key property of this CreateTermDetails.
        :type parent_term_key: str

        :param owner:
            The value to assign to the owner property of this CreateTermDetails.
        :type owner: str

        :param workflow_status:
            The value to assign to the workflow_status property of this CreateTermDetails.
            Allowed values for this property are: "NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"
        :type workflow_status: str

        :param custom_property_members:
            The value to assign to the custom_property_members property of this CreateTermDetails.
        :type custom_property_members: list[oci.data_catalog.models.CustomPropertySetUsage]

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'is_allowed_to_have_child_terms': 'bool',
            'parent_term_key': 'str',
            'owner': 'str',
            'workflow_status': 'str',
            'custom_property_members': 'list[CustomPropertySetUsage]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'is_allowed_to_have_child_terms': 'isAllowedToHaveChildTerms',
            'parent_term_key': 'parentTermKey',
            'owner': 'owner',
            'workflow_status': 'workflowStatus',
            'custom_property_members': 'customPropertyMembers'
        }

        self._display_name = None
        self._description = None
        self._is_allowed_to_have_child_terms = None
        self._parent_term_key = None
        self._owner = None
        self._workflow_status = None
        self._custom_property_members = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateTermDetails.
        A user-friendly display name. Is changeable. The combination of 'displayName' and 'parentTermKey'
        must be unique. Avoid entering confidential information.


        :return: The display_name of this CreateTermDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateTermDetails.
        A user-friendly display name. Is changeable. The combination of 'displayName' and 'parentTermKey'
        must be unique. Avoid entering confidential information.


        :param display_name: The display_name of this CreateTermDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateTermDetails.
        Detailed description of the term.


        :return: The description of this CreateTermDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTermDetails.
        Detailed description of the term.


        :param description: The description of this CreateTermDetails.
        :type: str
        """
        self._description = description

    @property
    def is_allowed_to_have_child_terms(self):
        """
        Gets the is_allowed_to_have_child_terms of this CreateTermDetails.
        Indicates whether a term may contain child terms.


        :return: The is_allowed_to_have_child_terms of this CreateTermDetails.
        :rtype: bool
        """
        return self._is_allowed_to_have_child_terms

    @is_allowed_to_have_child_terms.setter
    def is_allowed_to_have_child_terms(self, is_allowed_to_have_child_terms):
        """
        Sets the is_allowed_to_have_child_terms of this CreateTermDetails.
        Indicates whether a term may contain child terms.


        :param is_allowed_to_have_child_terms: The is_allowed_to_have_child_terms of this CreateTermDetails.
        :type: bool
        """
        self._is_allowed_to_have_child_terms = is_allowed_to_have_child_terms

    @property
    def parent_term_key(self):
        """
        Gets the parent_term_key of this CreateTermDetails.
        The terms parent term key. Will be null if the term has no parent term.


        :return: The parent_term_key of this CreateTermDetails.
        :rtype: str
        """
        return self._parent_term_key

    @parent_term_key.setter
    def parent_term_key(self, parent_term_key):
        """
        Sets the parent_term_key of this CreateTermDetails.
        The terms parent term key. Will be null if the term has no parent term.


        :param parent_term_key: The parent_term_key of this CreateTermDetails.
        :type: str
        """
        self._parent_term_key = parent_term_key

    @property
    def owner(self):
        """
        Gets the owner of this CreateTermDetails.
        OCID of the user who is the owner of this business terminology.


        :return: The owner of this CreateTermDetails.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this CreateTermDetails.
        OCID of the user who is the owner of this business terminology.


        :param owner: The owner of this CreateTermDetails.
        :type: str
        """
        self._owner = owner

    @property
    def workflow_status(self):
        """
        Gets the workflow_status of this CreateTermDetails.
        Status of the approval process workflow for this business term in the glossary.

        Allowed values for this property are: "NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"


        :return: The workflow_status of this CreateTermDetails.
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """
        Sets the workflow_status of this CreateTermDetails.
        Status of the approval process workflow for this business term in the glossary.


        :param workflow_status: The workflow_status of this CreateTermDetails.
        :type: str
        """
        allowed_values = ["NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"]
        if not value_allowed_none_or_none_sentinel(workflow_status, allowed_values):
            raise ValueError(
                "Invalid value for `workflow_status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._workflow_status = workflow_status

    @property
    def custom_property_members(self):
        """
        Gets the custom_property_members of this CreateTermDetails.
        The list of customized properties along with the values for this object


        :return: The custom_property_members of this CreateTermDetails.
        :rtype: list[oci.data_catalog.models.CustomPropertySetUsage]
        """
        return self._custom_property_members

    @custom_property_members.setter
    def custom_property_members(self, custom_property_members):
        """
        Sets the custom_property_members of this CreateTermDetails.
        The list of customized properties along with the values for this object


        :param custom_property_members: The custom_property_members of this CreateTermDetails.
        :type: list[oci.data_catalog.models.CustomPropertySetUsage]
        """
        self._custom_property_members = custom_property_members

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
