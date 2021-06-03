# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BlockVolumeReplica(object):
    """
    An asynchronous replica of a block volume that can then be used to create
    a new block volume or recover a block volume. For more information, see `Overview
    of Cross-Region Volume Replication`__
    To use any of the API operations, you must be authorized in an IAM policy.
    If you're not authorized, talk to an administrator. If you're an administrator
    who needs to write policies to give users access, see `Getting Started with
    Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumereplication.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a BlockVolumeReplica.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a BlockVolumeReplica.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a BlockVolumeReplica.
    #: This constant has a value of "ACTIVATING"
    LIFECYCLE_STATE_ACTIVATING = "ACTIVATING"

    #: A constant which can be used with the lifecycle_state property of a BlockVolumeReplica.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a BlockVolumeReplica.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a BlockVolumeReplica.
    #: This constant has a value of "FAULTY"
    LIFECYCLE_STATE_FAULTY = "FAULTY"

    def __init__(self, **kwargs):
        """
        Initializes a new BlockVolumeReplica object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this BlockVolumeReplica.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BlockVolumeReplica.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this BlockVolumeReplica.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this BlockVolumeReplica.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BlockVolumeReplica.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this BlockVolumeReplica.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BlockVolumeReplica.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this BlockVolumeReplica.
        :type size_in_gbs: int

        :param time_created:
            The value to assign to the time_created property of this BlockVolumeReplica.
        :type time_created: datetime

        :param time_last_synced:
            The value to assign to the time_last_synced property of this BlockVolumeReplica.
        :type time_last_synced: datetime

        :param block_volume_id:
            The value to assign to the block_volume_id property of this BlockVolumeReplica.
        :type block_volume_id: str

        :param total_data_transferred_in_gbs:
            The value to assign to the total_data_transferred_in_gbs property of this BlockVolumeReplica.
        :type total_data_transferred_in_gbs: int

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
            'time_created': 'datetime',
            'time_last_synced': 'datetime',
            'block_volume_id': 'str',
            'total_data_transferred_in_gbs': 'int'
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
            'time_created': 'timeCreated',
            'time_last_synced': 'timeLastSynced',
            'block_volume_id': 'blockVolumeId',
            'total_data_transferred_in_gbs': 'totalDataTransferredInGBs'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._size_in_gbs = None
        self._time_created = None
        self._time_last_synced = None
        self._block_volume_id = None
        self._total_data_transferred_in_gbs = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this BlockVolumeReplica.
        The availability domain of the block volume replica.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this BlockVolumeReplica.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this BlockVolumeReplica.
        The availability domain of the block volume replica.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this BlockVolumeReplica.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BlockVolumeReplica.
        The OCID of the compartment that contains the block volume replica.


        :return: The compartment_id of this BlockVolumeReplica.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BlockVolumeReplica.
        The OCID of the compartment that contains the block volume replica.


        :param compartment_id: The compartment_id of this BlockVolumeReplica.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BlockVolumeReplica.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this BlockVolumeReplica.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BlockVolumeReplica.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this BlockVolumeReplica.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BlockVolumeReplica.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this BlockVolumeReplica.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BlockVolumeReplica.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this BlockVolumeReplica.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BlockVolumeReplica.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this BlockVolumeReplica.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BlockVolumeReplica.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this BlockVolumeReplica.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BlockVolumeReplica.
        The block volume replica's Oracle ID (OCID).


        :return: The id of this BlockVolumeReplica.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BlockVolumeReplica.
        The block volume replica's Oracle ID (OCID).


        :param id: The id of this BlockVolumeReplica.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BlockVolumeReplica.
        The current state of a block volume replica.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BlockVolumeReplica.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BlockVolumeReplica.
        The current state of a block volume replica.


        :param lifecycle_state: The lifecycle_state of this BlockVolumeReplica.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def size_in_gbs(self):
        """
        **[Required]** Gets the size_in_gbs of this BlockVolumeReplica.
        The size of the source block volume, in GBs.


        :return: The size_in_gbs of this BlockVolumeReplica.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this BlockVolumeReplica.
        The size of the source block volume, in GBs.


        :param size_in_gbs: The size_in_gbs of this BlockVolumeReplica.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this BlockVolumeReplica.
        The date and time the block volume replica was created. Format defined
        by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this BlockVolumeReplica.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BlockVolumeReplica.
        The date and time the block volume replica was created. Format defined
        by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this BlockVolumeReplica.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_synced(self):
        """
        **[Required]** Gets the time_last_synced of this BlockVolumeReplica.
        The date and time the block volume replica was last synced from the source block volume.
        Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_last_synced of this BlockVolumeReplica.
        :rtype: datetime
        """
        return self._time_last_synced

    @time_last_synced.setter
    def time_last_synced(self, time_last_synced):
        """
        Sets the time_last_synced of this BlockVolumeReplica.
        The date and time the block volume replica was last synced from the source block volume.
        Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_last_synced: The time_last_synced of this BlockVolumeReplica.
        :type: datetime
        """
        self._time_last_synced = time_last_synced

    @property
    def block_volume_id(self):
        """
        **[Required]** Gets the block_volume_id of this BlockVolumeReplica.
        The OCID of the source block volume.


        :return: The block_volume_id of this BlockVolumeReplica.
        :rtype: str
        """
        return self._block_volume_id

    @block_volume_id.setter
    def block_volume_id(self, block_volume_id):
        """
        Sets the block_volume_id of this BlockVolumeReplica.
        The OCID of the source block volume.


        :param block_volume_id: The block_volume_id of this BlockVolumeReplica.
        :type: str
        """
        self._block_volume_id = block_volume_id

    @property
    def total_data_transferred_in_gbs(self):
        """
        Gets the total_data_transferred_in_gbs of this BlockVolumeReplica.
        The total size of the data transferred from the source block volume to the block volume replica, in GBs.


        :return: The total_data_transferred_in_gbs of this BlockVolumeReplica.
        :rtype: int
        """
        return self._total_data_transferred_in_gbs

    @total_data_transferred_in_gbs.setter
    def total_data_transferred_in_gbs(self, total_data_transferred_in_gbs):
        """
        Sets the total_data_transferred_in_gbs of this BlockVolumeReplica.
        The total size of the data transferred from the source block volume to the block volume replica, in GBs.


        :param total_data_transferred_in_gbs: The total_data_transferred_in_gbs of this BlockVolumeReplica.
        :type: int
        """
        self._total_data_transferred_in_gbs = total_data_transferred_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
