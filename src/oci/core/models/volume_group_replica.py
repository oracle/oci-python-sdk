# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeGroupReplica(object):
    """
    An asynchronous replica of a volume group that can then be used to create a new volume group
    or recover a volume group. For more information, see `Volume Group Replication`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroupreplication.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupReplica.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupReplica.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupReplica.
    #: This constant has a value of "ACTIVATING"
    LIFECYCLE_STATE_ACTIVATING = "ACTIVATING"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupReplica.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupReplica.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupReplica.
    #: This constant has a value of "FAULTY"
    LIFECYCLE_STATE_FAULTY = "FAULTY"

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeGroupReplica object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this VolumeGroupReplica.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VolumeGroupReplica.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this VolumeGroupReplica.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this VolumeGroupReplica.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VolumeGroupReplica.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this VolumeGroupReplica.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VolumeGroupReplica.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this VolumeGroupReplica.
        :type size_in_gbs: int

        :param volume_group_id:
            The value to assign to the volume_group_id property of this VolumeGroupReplica.
        :type volume_group_id: str

        :param time_created:
            The value to assign to the time_created property of this VolumeGroupReplica.
        :type time_created: datetime

        :param member_replicas:
            The value to assign to the member_replicas property of this VolumeGroupReplica.
        :type member_replicas: list[oci.core.models.MemberReplica]

        :param time_last_synced:
            The value to assign to the time_last_synced property of this VolumeGroupReplica.
        :type time_last_synced: datetime

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'size_in_gbs': 'int',
            'volume_group_id': 'str',
            'time_created': 'datetime',
            'member_replicas': 'list[MemberReplica]',
            'time_last_synced': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'size_in_gbs': 'sizeInGBs',
            'volume_group_id': 'volumeGroupId',
            'time_created': 'timeCreated',
            'member_replicas': 'memberReplicas',
            'time_last_synced': 'timeLastSynced'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._size_in_gbs = None
        self._volume_group_id = None
        self._time_created = None
        self._member_replicas = None
        self._time_last_synced = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this VolumeGroupReplica.
        The availability domain of the volume group replica.


        :return: The availability_domain of this VolumeGroupReplica.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this VolumeGroupReplica.
        The availability domain of the volume group replica.


        :param availability_domain: The availability_domain of this VolumeGroupReplica.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this VolumeGroupReplica.
        The OCID of the compartment that contains the volume group replica.


        :return: The compartment_id of this VolumeGroupReplica.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VolumeGroupReplica.
        The OCID of the compartment that contains the volume group replica.


        :param compartment_id: The compartment_id of this VolumeGroupReplica.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this VolumeGroupReplica.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this VolumeGroupReplica.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VolumeGroupReplica.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this VolumeGroupReplica.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this VolumeGroupReplica.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this VolumeGroupReplica.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VolumeGroupReplica.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this VolumeGroupReplica.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VolumeGroupReplica.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this VolumeGroupReplica.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VolumeGroupReplica.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this VolumeGroupReplica.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VolumeGroupReplica.
        The OCID for the volume group replica.


        :return: The id of this VolumeGroupReplica.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeGroupReplica.
        The OCID for the volume group replica.


        :param id: The id of this VolumeGroupReplica.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VolumeGroupReplica.
        The current state of a volume group.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VolumeGroupReplica.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VolumeGroupReplica.
        The current state of a volume group.


        :param lifecycle_state: The lifecycle_state of this VolumeGroupReplica.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def size_in_gbs(self):
        """
        **[Required]** Gets the size_in_gbs of this VolumeGroupReplica.
        The aggregate size of the volume group replica in GBs.


        :return: The size_in_gbs of this VolumeGroupReplica.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this VolumeGroupReplica.
        The aggregate size of the volume group replica in GBs.


        :param size_in_gbs: The size_in_gbs of this VolumeGroupReplica.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    @property
    def volume_group_id(self):
        """
        **[Required]** Gets the volume_group_id of this VolumeGroupReplica.
        The OCID of the source volume group.


        :return: The volume_group_id of this VolumeGroupReplica.
        :rtype: str
        """
        return self._volume_group_id

    @volume_group_id.setter
    def volume_group_id(self, volume_group_id):
        """
        Sets the volume_group_id of this VolumeGroupReplica.
        The OCID of the source volume group.


        :param volume_group_id: The volume_group_id of this VolumeGroupReplica.
        :type: str
        """
        self._volume_group_id = volume_group_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this VolumeGroupReplica.
        The date and time the volume group replica was created. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this VolumeGroupReplica.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VolumeGroupReplica.
        The date and time the volume group replica was created. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this VolumeGroupReplica.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def member_replicas(self):
        """
        **[Required]** Gets the member_replicas of this VolumeGroupReplica.
        Volume replicas within this volume group replica.


        :return: The member_replicas of this VolumeGroupReplica.
        :rtype: list[oci.core.models.MemberReplica]
        """
        return self._member_replicas

    @member_replicas.setter
    def member_replicas(self, member_replicas):
        """
        Sets the member_replicas of this VolumeGroupReplica.
        Volume replicas within this volume group replica.


        :param member_replicas: The member_replicas of this VolumeGroupReplica.
        :type: list[oci.core.models.MemberReplica]
        """
        self._member_replicas = member_replicas

    @property
    def time_last_synced(self):
        """
        **[Required]** Gets the time_last_synced of this VolumeGroupReplica.
        The date and time the volume group replica was last synced from the source volume group.
        Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_last_synced of this VolumeGroupReplica.
        :rtype: datetime
        """
        return self._time_last_synced

    @time_last_synced.setter
    def time_last_synced(self, time_last_synced):
        """
        Sets the time_last_synced of this VolumeGroupReplica.
        The date and time the volume group replica was last synced from the source volume group.
        Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_last_synced: The time_last_synced of this VolumeGroupReplica.
        :type: datetime
        """
        self._time_last_synced = time_last_synced

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
