# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateGlossaryDetails(object):
    """
    Properties used in glossary update operations.
    """

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
        :type workflow_status: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'owner': 'str',
            'workflow_status': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'owner': 'owner',
            'workflow_status': 'workflowStatus'
        }

        self._display_name = None
        self._description = None
        self._owner = None
        self._workflow_status = None

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
        self._workflow_status = workflow_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
