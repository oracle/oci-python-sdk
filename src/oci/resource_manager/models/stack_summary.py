# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StackSummary(object):
    """
    Returns a list of properties and the defining property values for the specified stack.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StackSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this StackSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this StackSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this StackSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this StackSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this StackSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this StackSummary.
        :type lifecycle_state: str

        :param terraform_version:
            The value to assign to the terraform_version property of this StackSummary.
        :type terraform_version: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this StackSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this StackSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'terraform_version': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'terraform_version': 'terraformVersion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._terraform_version = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this StackSummary.
        Unique identifier of the specified stack.


        :return: The id of this StackSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StackSummary.
        Unique identifier of the specified stack.


        :param id: The id of this StackSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this StackSummary.
        Unique identifier of the compartment in which the stack resides.


        :return: The compartment_id of this StackSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this StackSummary.
        Unique identifier of the compartment in which the stack resides.


        :param compartment_id: The compartment_id of this StackSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this StackSummary.
        Human-readable display name for the stack.


        :return: The display_name of this StackSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this StackSummary.
        Human-readable display name for the stack.


        :param display_name: The display_name of this StackSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this StackSummary.
        General description of the stack.


        :return: The description of this StackSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StackSummary.
        General description of the stack.


        :param description: The description of this StackSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this StackSummary.
        Date and time at which the stack was created.


        :return: The time_created of this StackSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this StackSummary.
        Date and time at which the stack was created.


        :param time_created: The time_created of this StackSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this StackSummary.

        :return: The lifecycle_state of this StackSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this StackSummary.

        :param lifecycle_state: The lifecycle_state of this StackSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def terraform_version(self):
        """
        Gets the terraform_version of this StackSummary.
        The version of Terraform specified for the stack. Example: `0.12.x`


        :return: The terraform_version of this StackSummary.
        :rtype: str
        """
        return self._terraform_version

    @terraform_version.setter
    def terraform_version(self, terraform_version):
        """
        Sets the terraform_version of this StackSummary.
        The version of Terraform specified for the stack. Example: `0.12.x`


        :param terraform_version: The terraform_version of this StackSummary.
        :type: str
        """
        self._terraform_version = terraform_version

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this StackSummary.
        Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this StackSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this StackSummary.
        Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this StackSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this StackSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this StackSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this StackSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this StackSummary.
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
