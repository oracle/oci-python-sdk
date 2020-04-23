# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceGroup(object):
    """
    Detail information for a managed instance group
    """

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the os_family property of a ManagedInstanceGroup.
    #: This constant has a value of "LINUX"
    OS_FAMILY_LINUX = "LINUX"

    #: A constant which can be used with the os_family property of a ManagedInstanceGroup.
    #: This constant has a value of "WINDOWS"
    OS_FAMILY_WINDOWS = "WINDOWS"

    #: A constant which can be used with the os_family property of a ManagedInstanceGroup.
    #: This constant has a value of "ALL"
    OS_FAMILY_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this ManagedInstanceGroup.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ManagedInstanceGroup.
        :type id: str

        :param description:
            The value to assign to the description property of this ManagedInstanceGroup.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedInstanceGroup.
        :type compartment_id: str

        :param managed_instances:
            The value to assign to the managed_instances property of this ManagedInstanceGroup.
        :type managed_instances: list[Id]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagedInstanceGroup.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ManagedInstanceGroup.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ManagedInstanceGroup.
        :type defined_tags: dict(str, dict(str, object))

        :param os_family:
            The value to assign to the os_family property of this ManagedInstanceGroup.
            Allowed values for this property are: "LINUX", "WINDOWS", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'id': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'managed_instances': 'list[Id]',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'os_family': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'id': 'id',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'managed_instances': 'managedInstances',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'os_family': 'osFamily'
        }

        self._display_name = None
        self._id = None
        self._description = None
        self._compartment_id = None
        self._managed_instances = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._os_family = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagedInstanceGroup.
        Managed Instance Group identifier


        :return: The display_name of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagedInstanceGroup.
        Managed Instance Group identifier


        :param display_name: The display_name of this ManagedInstanceGroup.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedInstanceGroup.
        OCID for the managed instance group


        :return: The id of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedInstanceGroup.
        OCID for the managed instance group


        :param id: The id of this ManagedInstanceGroup.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this ManagedInstanceGroup.
        Information specified by the user about the managed instance group


        :return: The description of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagedInstanceGroup.
        Information specified by the user about the managed instance group


        :param description: The description of this ManagedInstanceGroup.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedInstanceGroup.
        OCID for the Compartment


        :return: The compartment_id of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedInstanceGroup.
        OCID for the Compartment


        :param compartment_id: The compartment_id of this ManagedInstanceGroup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def managed_instances(self):
        """
        Gets the managed_instances of this ManagedInstanceGroup.
        list of Managed Instances in the group


        :return: The managed_instances of this ManagedInstanceGroup.
        :rtype: list[Id]
        """
        return self._managed_instances

    @managed_instances.setter
    def managed_instances(self, managed_instances):
        """
        Sets the managed_instances of this ManagedInstanceGroup.
        list of Managed Instances in the group


        :param managed_instances: The managed_instances of this ManagedInstanceGroup.
        :type: list[Id]
        """
        self._managed_instances = managed_instances

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ManagedInstanceGroup.
        The current state of the Software Source.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagedInstanceGroup.
        The current state of the Software Source.


        :param lifecycle_state: The lifecycle_state of this ManagedInstanceGroup.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ManagedInstanceGroup.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ManagedInstanceGroup.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ManagedInstanceGroup.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ManagedInstanceGroup.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ManagedInstanceGroup.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ManagedInstanceGroup.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ManagedInstanceGroup.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ManagedInstanceGroup.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def os_family(self):
        """
        Gets the os_family of this ManagedInstanceGroup.
        The Operating System type of the managed instance.

        Allowed values for this property are: "LINUX", "WINDOWS", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this ManagedInstanceGroup.
        The Operating System type of the managed instance.


        :param os_family: The os_family of this ManagedInstanceGroup.
        :type: str
        """
        allowed_values = ["LINUX", "WINDOWS", "ALL"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
