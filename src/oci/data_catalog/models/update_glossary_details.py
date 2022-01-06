# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateGlossaryDetails(object):
    """
    Properties used in glossary update operations.
    """

    #: A constant which can be used with the workflow_status property of a UpdateGlossaryDetails.
    #: This constant has a value of "NEW"
    WORKFLOW_STATUS_NEW = "NEW"

    #: A constant which can be used with the workflow_status property of a UpdateGlossaryDetails.
    #: This constant has a value of "APPROVED"
    WORKFLOW_STATUS_APPROVED = "APPROVED"

    #: A constant which can be used with the workflow_status property of a UpdateGlossaryDetails.
    #: This constant has a value of "UNDER_REVIEW"
    WORKFLOW_STATUS_UNDER_REVIEW = "UNDER_REVIEW"

    #: A constant which can be used with the workflow_status property of a UpdateGlossaryDetails.
    #: This constant has a value of "ESCALATED"
    WORKFLOW_STATUS_ESCALATED = "ESCALATED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateGlossaryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateGlossaryDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateGlossaryDetails.
        :type description: str

        :param owner:
            The value to assign to the owner property of this UpdateGlossaryDetails.
        :type owner: str

        :param workflow_status:
            The value to assign to the workflow_status property of this UpdateGlossaryDetails.
            Allowed values for this property are: "NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"
        :type workflow_status: str

        :param custom_property_members:
            The value to assign to the custom_property_members property of this UpdateGlossaryDetails.
        :type custom_property_members: list[oci.data_catalog.models.CustomPropertySetUsage]

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'owner': 'str',
            'workflow_status': 'str',
            'custom_property_members': 'list[CustomPropertySetUsage]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'owner': 'owner',
            'workflow_status': 'workflowStatus',
            'custom_property_members': 'customPropertyMembers'
        }

        self._display_name = None
        self._description = None
        self._owner = None
        self._workflow_status = None
        self._custom_property_members = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateGlossaryDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateGlossaryDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateGlossaryDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateGlossaryDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateGlossaryDetails.
        Detailed description of the glossary.


        :return: The description of this UpdateGlossaryDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateGlossaryDetails.
        Detailed description of the glossary.


        :param description: The description of this UpdateGlossaryDetails.
        :type: str
        """
        self._description = description

    @property
    def owner(self):
        """
        Gets the owner of this UpdateGlossaryDetails.
        OCID of the user who is the owner of the glossary.


        :return: The owner of this UpdateGlossaryDetails.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this UpdateGlossaryDetails.
        OCID of the user who is the owner of the glossary.


        :param owner: The owner of this UpdateGlossaryDetails.
        :type: str
        """
        self._owner = owner

    @property
    def workflow_status(self):
        """
        Gets the workflow_status of this UpdateGlossaryDetails.
        Status of the approval process workflow for this business glossary.

        Allowed values for this property are: "NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"


        :return: The workflow_status of this UpdateGlossaryDetails.
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """
        Sets the workflow_status of this UpdateGlossaryDetails.
        Status of the approval process workflow for this business glossary.


        :param workflow_status: The workflow_status of this UpdateGlossaryDetails.
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
        Gets the custom_property_members of this UpdateGlossaryDetails.
        The list of customized properties along with the values for this object


        :return: The custom_property_members of this UpdateGlossaryDetails.
        :rtype: list[oci.data_catalog.models.CustomPropertySetUsage]
        """
        return self._custom_property_members

    @custom_property_members.setter
    def custom_property_members(self, custom_property_members):
        """
        Sets the custom_property_members of this UpdateGlossaryDetails.
        The list of customized properties along with the values for this object


        :param custom_property_members: The custom_property_members of this UpdateGlossaryDetails.
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
