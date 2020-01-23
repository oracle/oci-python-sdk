# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateGlossaryDetails(object):
    """
    Properties used in glossary create operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateGlossaryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateGlossaryDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateGlossaryDetails.
        :type description: str

        :param workflow_status:
            The value to assign to the workflow_status property of this CreateGlossaryDetails.
        :type workflow_status: str

        :param owner:
            The value to assign to the owner property of this CreateGlossaryDetails.
        :type owner: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'workflow_status': 'str',
            'owner': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'workflow_status': 'workflowStatus',
            'owner': 'owner'
        }

        self._display_name = None
        self._description = None
        self._workflow_status = None
        self._owner = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateGlossaryDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateGlossaryDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateGlossaryDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateGlossaryDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateGlossaryDetails.
        Detailed description of the glossary.


        :return: The description of this CreateGlossaryDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateGlossaryDetails.
        Detailed description of the glossary.


        :param description: The description of this CreateGlossaryDetails.
        :type: str
        """
        self._description = description

    @property
    def workflow_status(self):
        """
        Gets the workflow_status of this CreateGlossaryDetails.
        Status of the approval process workflow for this business glossary.


        :return: The workflow_status of this CreateGlossaryDetails.
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """
        Sets the workflow_status of this CreateGlossaryDetails.
        Status of the approval process workflow for this business glossary.


        :param workflow_status: The workflow_status of this CreateGlossaryDetails.
        :type: str
        """
        self._workflow_status = workflow_status

    @property
    def owner(self):
        """
        Gets the owner of this CreateGlossaryDetails.
        OCID of the user who is the owner of the glossary.


        :return: The owner of this CreateGlossaryDetails.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this CreateGlossaryDetails.
        OCID of the user who is the owner of the glossary.


        :param owner: The owner of this CreateGlossaryDetails.
        :type: str
        """
        self._owner = owner

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
