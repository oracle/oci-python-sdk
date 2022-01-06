# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Compartment(object):
    """
    A collection of related resources. Compartments are a fundamental component of Oracle Cloud Infrastructure
    for organizing and isolating your cloud resources. You use them to clearly separate resources for the purposes
    of measuring usage and billing, access (through the use of IAM Service policies), and isolation (separating the
    resources for one project or business unit from another). A common approach is to create a compartment for each
    major part of your organization. For more information, see
    `Overview of the IAM Service`__ and also
    `Setting Up Your Tenancy`__.

    To place a resource in a compartment, simply specify the compartment ID in the \"Create\" request object when
    initially creating the resource. For example, to launch an instance into a particular compartment, specify
    that compartment's OCID in the `LaunchInstance` request. You can't move an existing resource from one
    compartment to another.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access,
    see `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values
    using the API.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
    __ https://docs.cloud.oracle.com/Content/GSG/Concepts/settinguptenancy.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Compartment.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Compartment.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Compartment.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Compartment.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Compartment.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Compartment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Compartment.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Compartment.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this Compartment.
        :type name: str

        :param description:
            The value to assign to the description property of this Compartment.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this Compartment.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Compartment.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this Compartment.
        :type inactive_status: int

        :param is_accessible:
            The value to assign to the is_accessible property of this Compartment.
        :type is_accessible: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Compartment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Compartment.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int',
            'is_accessible': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus',
            'is_accessible': 'isAccessible',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None
        self._is_accessible = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Compartment.
        The OCID of the compartment.


        :return: The id of this Compartment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Compartment.
        The OCID of the compartment.


        :param id: The id of this Compartment.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Compartment.
        The OCID of the parent compartment containing the compartment.


        :return: The compartment_id of this Compartment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Compartment.
        The OCID of the parent compartment containing the compartment.


        :param compartment_id: The compartment_id of this Compartment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Compartment.
        The name you assign to the compartment during creation. The name must be unique across all
        compartments in the parent. Avoid entering confidential information.


        :return: The name of this Compartment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Compartment.
        The name you assign to the compartment during creation. The name must be unique across all
        compartments in the parent. Avoid entering confidential information.


        :param name: The name of this Compartment.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this Compartment.
        The description you assign to the compartment. Does not have to be unique, and it's changeable.


        :return: The description of this Compartment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Compartment.
        The description you assign to the compartment. Does not have to be unique, and it's changeable.


        :param description: The description of this Compartment.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Compartment.
        Date and time the compartment was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this Compartment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Compartment.
        Date and time the compartment was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this Compartment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Compartment.
        The compartment's current state. After creating a compartment, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Compartment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Compartment.
        The compartment's current state. After creating a compartment, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this Compartment.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this Compartment.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this Compartment.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this Compartment.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this Compartment.
        :type: int
        """
        self._inactive_status = inactive_status

    @property
    def is_accessible(self):
        """
        Gets the is_accessible of this Compartment.
        Indicates whether or not the compartment is accessible for the user making the request.
        Returns true when the user has INSPECT permissions directly on a resource in the
        compartment or indirectly (permissions can be on a resource in a subcompartment).


        :return: The is_accessible of this Compartment.
        :rtype: bool
        """
        return self._is_accessible

    @is_accessible.setter
    def is_accessible(self, is_accessible):
        """
        Sets the is_accessible of this Compartment.
        Indicates whether or not the compartment is accessible for the user making the request.
        Returns true when the user has INSPECT permissions directly on a resource in the
        compartment or indirectly (permissions can be on a resource in a subcompartment).


        :param is_accessible: The is_accessible of this Compartment.
        :type: bool
        """
        self._is_accessible = is_accessible

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Compartment.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Compartment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Compartment.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Compartment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Compartment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Compartment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Compartment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Compartment.
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
