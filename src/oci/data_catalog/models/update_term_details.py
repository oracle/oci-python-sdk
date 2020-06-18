# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTermDetails(object):
    """
    Properties used in term update operations.
    """

    #: A constant which can be used with the workflow_status property of a UpdateTermDetails.
    #: This constant has a value of "NEW"
    WORKFLOW_STATUS_NEW = "NEW"

    #: A constant which can be used with the workflow_status property of a UpdateTermDetails.
    #: This constant has a value of "APPROVED"
    WORKFLOW_STATUS_APPROVED = "APPROVED"

    #: A constant which can be used with the workflow_status property of a UpdateTermDetails.
    #: This constant has a value of "UNDER_REVIEW"
    WORKFLOW_STATUS_UNDER_REVIEW = "UNDER_REVIEW"

    #: A constant which can be used with the workflow_status property of a UpdateTermDetails.
    #: This constant has a value of "ESCALATED"
    WORKFLOW_STATUS_ESCALATED = "ESCALATED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTermDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateTermDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateTermDetails.
        :type description: str

        :param parent_term_key:
            The value to assign to the parent_term_key property of this UpdateTermDetails.
        :type parent_term_key: str

        :param owner:
            The value to assign to the owner property of this UpdateTermDetails.
        :type owner: str

        :param workflow_status:
            The value to assign to the workflow_status property of this UpdateTermDetails.
            Allowed values for this property are: "NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"
        :type workflow_status: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'parent_term_key': 'str',
            'owner': 'str',
            'workflow_status': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'parent_term_key': 'parentTermKey',
            'owner': 'owner',
            'workflow_status': 'workflowStatus'
        }

        self._display_name = None
        self._description = None
        self._parent_term_key = None
        self._owner = None
        self._workflow_status = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateTermDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateTermDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateTermDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateTermDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateTermDetails.
        Detailed description of the term.


        :return: The description of this UpdateTermDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateTermDetails.
        Detailed description of the term.


        :param description: The description of this UpdateTermDetails.
        :type: str
        """
        self._description = description

    @property
    def parent_term_key(self):
        """
        Gets the parent_term_key of this UpdateTermDetails.
        This terms parent term key. Will be null if the term has no parent term.


        :return: The parent_term_key of this UpdateTermDetails.
        :rtype: str
        """
        return self._parent_term_key

    @parent_term_key.setter
    def parent_term_key(self, parent_term_key):
        """
        Sets the parent_term_key of this UpdateTermDetails.
        This terms parent term key. Will be null if the term has no parent term.


        :param parent_term_key: The parent_term_key of this UpdateTermDetails.
        :type: str
        """
        self._parent_term_key = parent_term_key

    @property
    def owner(self):
        """
        Gets the owner of this UpdateTermDetails.
        OCID of the user who is the owner of this business terminology.


        :return: The owner of this UpdateTermDetails.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this UpdateTermDetails.
        OCID of the user who is the owner of this business terminology.


        :param owner: The owner of this UpdateTermDetails.
        :type: str
        """
        self._owner = owner

    @property
    def workflow_status(self):
        """
        Gets the workflow_status of this UpdateTermDetails.
        Status of the approval process workflow for this business term in the glossary

        Allowed values for this property are: "NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"


        :return: The workflow_status of this UpdateTermDetails.
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """
        Sets the workflow_status of this UpdateTermDetails.
        Status of the approval process workflow for this business term in the glossary


        :param workflow_status: The workflow_status of this UpdateTermDetails.
        :type: str
        """
        allowed_values = ["NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"]
        if not value_allowed_none_or_none_sentinel(workflow_status, allowed_values):
            raise ValueError(
                "Invalid value for `workflow_status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._workflow_status = workflow_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
