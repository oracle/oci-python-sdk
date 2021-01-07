# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateServiceConnectorDetails(object):
    """
    The configuration details for updating a service connector.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateServiceConnectorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateServiceConnectorDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateServiceConnectorDetails.
        :type description: str

        :param source:
            The value to assign to the source property of this UpdateServiceConnectorDetails.
        :type source: oci.sch.models.SourceDetails

        :param tasks:
            The value to assign to the tasks property of this UpdateServiceConnectorDetails.
        :type tasks: list[oci.sch.models.TaskDetails]

        :param target:
            The value to assign to the target property of this UpdateServiceConnectorDetails.
        :type target: oci.sch.models.TargetDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateServiceConnectorDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateServiceConnectorDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'source': 'SourceDetails',
            'tasks': 'list[TaskDetails]',
            'target': 'TargetDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'source': 'source',
            'tasks': 'tasks',
            'target': 'target',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._source = None
        self._tasks = None
        self._target = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateServiceConnectorDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateServiceConnectorDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateServiceConnectorDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateServiceConnectorDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateServiceConnectorDetails.
        The description of the resource. Avoid entering confidential information.


        :return: The description of this UpdateServiceConnectorDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateServiceConnectorDetails.
        The description of the resource. Avoid entering confidential information.


        :param description: The description of this UpdateServiceConnectorDetails.
        :type: str
        """
        self._description = description

    @property
    def source(self):
        """
        Gets the source of this UpdateServiceConnectorDetails.

        :return: The source of this UpdateServiceConnectorDetails.
        :rtype: oci.sch.models.SourceDetails
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this UpdateServiceConnectorDetails.

        :param source: The source of this UpdateServiceConnectorDetails.
        :type: oci.sch.models.SourceDetails
        """
        self._source = source

    @property
    def tasks(self):
        """
        Gets the tasks of this UpdateServiceConnectorDetails.
        The list of the tasks.


        :return: The tasks of this UpdateServiceConnectorDetails.
        :rtype: list[oci.sch.models.TaskDetails]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """
        Sets the tasks of this UpdateServiceConnectorDetails.
        The list of the tasks.


        :param tasks: The tasks of this UpdateServiceConnectorDetails.
        :type: list[oci.sch.models.TaskDetails]
        """
        self._tasks = tasks

    @property
    def target(self):
        """
        Gets the target of this UpdateServiceConnectorDetails.

        :return: The target of this UpdateServiceConnectorDetails.
        :rtype: oci.sch.models.TargetDetails
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this UpdateServiceConnectorDetails.

        :param target: The target of this UpdateServiceConnectorDetails.
        :type: oci.sch.models.TargetDetails
        """
        self._target = target

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateServiceConnectorDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateServiceConnectorDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateServiceConnectorDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateServiceConnectorDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateServiceConnectorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateServiceConnectorDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateServiceConnectorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateServiceConnectorDetails.
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
