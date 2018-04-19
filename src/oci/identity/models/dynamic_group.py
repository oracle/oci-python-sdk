# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DynamicGroup(object):
    """
    A dynamic group defines a matching rule. Every bare metal or virtual machine instance is deployed with an instance certificate.
    The certificate contains metadata about the instance. This includes the instance OCID and the compartment OCID, along
    with a few other optional properties. When an API call is made using this instance certificate as the authenticator,
    the certificate can be matched to one or multiple dynamic groups. The instance can then get access to the API
    based on the permissions granted in policies written for the dynamic groups.

    This works like regular user/group membership. But in that case, the membership is a static relationship, whereas
    in a dynamic group, the membership of an instance certificate to a dynamic group is determined during runtime.
    For more information, see `Managing Dynamic Groups`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingdynamicgroups.htm
    """

    #: A constant which can be used with the lifecycle_state property of a DynamicGroup.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DynamicGroup.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DynamicGroup.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DynamicGroup.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DynamicGroup.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new DynamicGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DynamicGroup.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DynamicGroup.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this DynamicGroup.
        :type name: str

        :param description:
            The value to assign to the description property of this DynamicGroup.
        :type description: str

        :param matching_rule:
            The value to assign to the matching_rule property of this DynamicGroup.
        :type matching_rule: str

        :param time_created:
            The value to assign to the time_created property of this DynamicGroup.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DynamicGroup.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this DynamicGroup.
        :type inactive_status: int

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'matching_rule': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'matching_rule': 'matchingRule',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._matching_rule = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DynamicGroup.
        The OCID of the group.


        :return: The id of this DynamicGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DynamicGroup.
        The OCID of the group.


        :param id: The id of this DynamicGroup.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DynamicGroup.
        The OCID of the tenancy containing the group.


        :return: The compartment_id of this DynamicGroup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DynamicGroup.
        The OCID of the tenancy containing the group.


        :param compartment_id: The compartment_id of this DynamicGroup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DynamicGroup.
        The name you assign to the group during creation. The name must be unique across all groups in
        the tenancy and cannot be changed.


        :return: The name of this DynamicGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DynamicGroup.
        The name you assign to the group during creation. The name must be unique across all groups in
        the tenancy and cannot be changed.


        :param name: The name of this DynamicGroup.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this DynamicGroup.
        The description you assign to the group. Does not have to be unique, and it's changeable.


        :return: The description of this DynamicGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DynamicGroup.
        The description you assign to the group. Does not have to be unique, and it's changeable.


        :param description: The description of this DynamicGroup.
        :type: str
        """
        self._description = description

    @property
    def matching_rule(self):
        """
        **[Required]** Gets the matching_rule of this DynamicGroup.
        A rule string that defines which instance certificates will be matched.
        For syntax, see `Managing Dynamic Groups`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingdynamicgroups.htm


        :return: The matching_rule of this DynamicGroup.
        :rtype: str
        """
        return self._matching_rule

    @matching_rule.setter
    def matching_rule(self, matching_rule):
        """
        Sets the matching_rule of this DynamicGroup.
        A rule string that defines which instance certificates will be matched.
        For syntax, see `Managing Dynamic Groups`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingdynamicgroups.htm


        :param matching_rule: The matching_rule of this DynamicGroup.
        :type: str
        """
        self._matching_rule = matching_rule

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DynamicGroup.
        Date and time the group was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this DynamicGroup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DynamicGroup.
        Date and time the group was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this DynamicGroup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DynamicGroup.
        The group's current state. After creating a group, make sure its `lifecycleState` changes from CREATING to
        ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DynamicGroup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DynamicGroup.
        The group's current state. After creating a group, make sure its `lifecycleState` changes from CREATING to
        ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this DynamicGroup.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this DynamicGroup.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this DynamicGroup.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this DynamicGroup.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this DynamicGroup.
        :type: int
        """
        self._inactive_status = inactive_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
