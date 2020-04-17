# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTermDetails(object):
    """
    Properties used in term create operations.
    """

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
        :type workflow_status: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'is_allowed_to_have_child_terms': 'bool',
            'parent_term_key': 'str',
            'owner': 'str',
            'workflow_status': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'is_allowed_to_have_child_terms': 'isAllowedToHaveChildTerms',
            'parent_term_key': 'parentTermKey',
            'owner': 'owner',
            'workflow_status': 'workflowStatus'
        }

        self._display_name = None
        self._description = None
        self._is_allowed_to_have_child_terms = None
        self._parent_term_key = None
        self._owner = None
        self._workflow_status = None

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
        self._workflow_status = workflow_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
