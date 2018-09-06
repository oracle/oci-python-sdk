# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BootVolumeAttachment(object):
    """
    Represents an attachment between a boot volume and an instance.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.
    """

    #: A constant which can be used with the lifecycle_state property of a BootVolumeAttachment.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a BootVolumeAttachment.
    #: This constant has a value of "ATTACHED"
    LIFECYCLE_STATE_ATTACHED = "ATTACHED"

    #: A constant which can be used with the lifecycle_state property of a BootVolumeAttachment.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    #: A constant which can be used with the lifecycle_state property of a BootVolumeAttachment.
    #: This constant has a value of "DETACHED"
    LIFECYCLE_STATE_DETACHED = "DETACHED"

    def __init__(self, **kwargs):
        """
        Initializes a new BootVolumeAttachment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this BootVolumeAttachment.
        :type availability_domain: str

        :param boot_volume_id:
            The value to assign to the boot_volume_id property of this BootVolumeAttachment.
        :type boot_volume_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BootVolumeAttachment.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this BootVolumeAttachment.
        :type display_name: str

        :param id:
            The value to assign to the id property of this BootVolumeAttachment.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this BootVolumeAttachment.
        :type instance_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BootVolumeAttachment.
            Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this BootVolumeAttachment.
        :type time_created: datetime

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'boot_volume_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'instance_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'boot_volume_id': 'bootVolumeId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'instance_id': 'instanceId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._boot_volume_id = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._instance_id = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this BootVolumeAttachment.
        The availability domain of an instance.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this BootVolumeAttachment.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this BootVolumeAttachment.
        The availability domain of an instance.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this BootVolumeAttachment.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def boot_volume_id(self):
        """
        **[Required]** Gets the boot_volume_id of this BootVolumeAttachment.
        The OCID of the boot volume.


        :return: The boot_volume_id of this BootVolumeAttachment.
        :rtype: str
        """
        return self._boot_volume_id

    @boot_volume_id.setter
    def boot_volume_id(self, boot_volume_id):
        """
        Sets the boot_volume_id of this BootVolumeAttachment.
        The OCID of the boot volume.


        :param boot_volume_id: The boot_volume_id of this BootVolumeAttachment.
        :type: str
        """
        self._boot_volume_id = boot_volume_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BootVolumeAttachment.
        The OCID of the compartment.


        :return: The compartment_id of this BootVolumeAttachment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BootVolumeAttachment.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this BootVolumeAttachment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this BootVolumeAttachment.
        A user-friendly name. Does not have to be unique, and it cannot be changed.
        Avoid entering confidential information.

        Example: `My boot volume`


        :return: The display_name of this BootVolumeAttachment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BootVolumeAttachment.
        A user-friendly name. Does not have to be unique, and it cannot be changed.
        Avoid entering confidential information.

        Example: `My boot volume`


        :param display_name: The display_name of this BootVolumeAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BootVolumeAttachment.
        The OCID of the boot volume attachment.


        :return: The id of this BootVolumeAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BootVolumeAttachment.
        The OCID of the boot volume attachment.


        :param id: The id of this BootVolumeAttachment.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this BootVolumeAttachment.
        The OCID of the instance the boot volume is attached to.


        :return: The instance_id of this BootVolumeAttachment.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this BootVolumeAttachment.
        The OCID of the instance the boot volume is attached to.


        :param instance_id: The instance_id of this BootVolumeAttachment.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BootVolumeAttachment.
        The current state of the boot volume attachment.

        Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BootVolumeAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BootVolumeAttachment.
        The current state of the boot volume attachment.


        :param lifecycle_state: The lifecycle_state of this BootVolumeAttachment.
        :type: str
        """
        allowed_values = ["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this BootVolumeAttachment.
        The date and time the boot volume was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this BootVolumeAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BootVolumeAttachment.
        The date and time the boot volume was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this BootVolumeAttachment.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
