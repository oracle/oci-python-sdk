# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTriggerDetails(object):
    """
    The information about new Trigger.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTriggerDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.CreateGithubTriggerDetails`
        * :class:`~oci.devops.models.CreateDevopsCodeRepositoryTriggerDetails`
        * :class:`~oci.devops.models.CreateGitlabTriggerDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateTriggerDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateTriggerDetails.
        :type description: str

        :param project_id:
            The value to assign to the project_id property of this CreateTriggerDetails.
        :type project_id: str

        :param trigger_source:
            The value to assign to the trigger_source property of this CreateTriggerDetails.
        :type trigger_source: str

        :param actions:
            The value to assign to the actions property of this CreateTriggerDetails.
        :type actions: list[oci.devops.models.TriggerAction]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateTriggerDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateTriggerDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'project_id': 'str',
            'trigger_source': 'str',
            'actions': 'list[TriggerAction]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'project_id': 'projectId',
            'trigger_source': 'triggerSource',
            'actions': 'actions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._project_id = None
        self._trigger_source = None
        self._actions = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['triggerSource']

        if type == 'GITHUB':
            return 'CreateGithubTriggerDetails'

        if type == 'DEVOPS_CODE_REPOSITORY':
            return 'CreateDevopsCodeRepositoryTriggerDetails'

        if type == 'GITLAB':
            return 'CreateGitlabTriggerDetails'
        else:
            return 'CreateTriggerDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateTriggerDetails.
        Name of the Trigger


        :return: The display_name of this CreateTriggerDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateTriggerDetails.
        Name of the Trigger


        :param display_name: The display_name of this CreateTriggerDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateTriggerDetails.
        Optional description about the Trigger


        :return: The description of this CreateTriggerDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTriggerDetails.
        Optional description about the Trigger


        :param description: The description of this CreateTriggerDetails.
        :type: str
        """
        self._description = description

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateTriggerDetails.
        Project to which the Trigger will belong


        :return: The project_id of this CreateTriggerDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateTriggerDetails.
        Project to which the Trigger will belong


        :param project_id: The project_id of this CreateTriggerDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def trigger_source(self):
        """
        **[Required]** Gets the trigger_source of this CreateTriggerDetails.
        Source of the Trigger (allowed values are - GITHUB, GITLAB)


        :return: The trigger_source of this CreateTriggerDetails.
        :rtype: str
        """
        return self._trigger_source

    @trigger_source.setter
    def trigger_source(self, trigger_source):
        """
        Sets the trigger_source of this CreateTriggerDetails.
        Source of the Trigger (allowed values are - GITHUB, GITLAB)


        :param trigger_source: The trigger_source of this CreateTriggerDetails.
        :type: str
        """
        self._trigger_source = trigger_source

    @property
    def actions(self):
        """
        **[Required]** Gets the actions of this CreateTriggerDetails.
        The list of actions that are to be performed for this Trigger


        :return: The actions of this CreateTriggerDetails.
        :rtype: list[oci.devops.models.TriggerAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this CreateTriggerDetails.
        The list of actions that are to be performed for this Trigger


        :param actions: The actions of this CreateTriggerDetails.
        :type: list[oci.devops.models.TriggerAction]
        """
        self._actions = actions

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateTriggerDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateTriggerDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateTriggerDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateTriggerDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateTriggerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateTriggerDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateTriggerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateTriggerDetails.
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
