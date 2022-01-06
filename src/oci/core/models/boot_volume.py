# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BootVolume(object):
    """
    A detachable boot volume device that contains the image used to boot a Compute instance. For more information, see
    `Overview of Boot Volumes`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a BootVolume.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a BootVolume.
    #: This constant has a value of "RESTORING"
    LIFECYCLE_STATE_RESTORING = "RESTORING"

    #: A constant which can be used with the lifecycle_state property of a BootVolume.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a BootVolume.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a BootVolume.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a BootVolume.
    #: This constant has a value of "FAULTY"
    LIFECYCLE_STATE_FAULTY = "FAULTY"

    def __init__(self, **kwargs):
        """
        Initializes a new BootVolume object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this BootVolume.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BootVolume.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this BootVolume.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this BootVolume.
        :type system_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this BootVolume.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BootVolume.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this BootVolume.
        :type id: str

        :param image_id:
            The value to assign to the image_id property of this BootVolume.
        :type image_id: str

        :param is_hydrated:
            The value to assign to the is_hydrated property of this BootVolume.
        :type is_hydrated: bool

        :param vpus_per_gb:
            The value to assign to the vpus_per_gb property of this BootVolume.
        :type vpus_per_gb: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BootVolume.
            Allowed values for this property are: "PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this BootVolume.
        :type size_in_gbs: int

        :param size_in_mbs:
            The value to assign to the size_in_mbs property of this BootVolume.
        :type size_in_mbs: int

        :param source_details:
            The value to assign to the source_details property of this BootVolume.
        :type source_details: oci.core.models.BootVolumeSourceDetails

        :param time_created:
            The value to assign to the time_created property of this BootVolume.
        :type time_created: datetime

        :param volume_group_id:
            The value to assign to the volume_group_id property of this BootVolume.
        :type volume_group_id: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this BootVolume.
        :type kms_key_id: str

        :param is_auto_tune_enabled:
            The value to assign to the is_auto_tune_enabled property of this BootVolume.
        :type is_auto_tune_enabled: bool

        :param auto_tuned_vpus_per_gb:
            The value to assign to the auto_tuned_vpus_per_gb property of this BootVolume.
        :type auto_tuned_vpus_per_gb: int

        :param boot_volume_replicas:
            The value to assign to the boot_volume_replicas property of this BootVolume.
        :type boot_volume_replicas: list[oci.core.models.BootVolumeReplicaInfo]

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'image_id': 'str',
            'is_hydrated': 'bool',
            'vpus_per_gb': 'int',
            'lifecycle_state': 'str',
            'size_in_gbs': 'int',
            'size_in_mbs': 'int',
            'source_details': 'BootVolumeSourceDetails',
            'time_created': 'datetime',
            'volume_group_id': 'str',
            'kms_key_id': 'str',
            'is_auto_tune_enabled': 'bool',
            'auto_tuned_vpus_per_gb': 'int',
            'boot_volume_replicas': 'list[BootVolumeReplicaInfo]'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'image_id': 'imageId',
            'is_hydrated': 'isHydrated',
            'vpus_per_gb': 'vpusPerGB',
            'lifecycle_state': 'lifecycleState',
            'size_in_gbs': 'sizeInGBs',
            'size_in_mbs': 'sizeInMBs',
            'source_details': 'sourceDetails',
            'time_created': 'timeCreated',
            'volume_group_id': 'volumeGroupId',
            'kms_key_id': 'kmsKeyId',
            'is_auto_tune_enabled': 'isAutoTuneEnabled',
            'auto_tuned_vpus_per_gb': 'autoTunedVpusPerGB',
            'boot_volume_replicas': 'bootVolumeReplicas'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._defined_tags = None
        self._system_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._image_id = None
        self._is_hydrated = None
        self._vpus_per_gb = None
        self._lifecycle_state = None
        self._size_in_gbs = None
        self._size_in_mbs = None
        self._source_details = None
        self._time_created = None
        self._volume_group_id = None
        self._kms_key_id = None
        self._is_auto_tune_enabled = None
        self._auto_tuned_vpus_per_gb = None
        self._boot_volume_replicas = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this BootVolume.
        The availability domain of the boot volume.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this BootVolume.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this BootVolume.
        The availability domain of the boot volume.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this BootVolume.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BootVolume.
        The OCID of the compartment that contains the boot volume.


        :return: The compartment_id of this BootVolume.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BootVolume.
        The OCID of the compartment that contains the boot volume.


        :param compartment_id: The compartment_id of this BootVolume.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BootVolume.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this BootVolume.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BootVolume.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this BootVolume.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this BootVolume.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The system_tags of this BootVolume.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this BootVolume.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param system_tags: The system_tags of this BootVolume.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this BootVolume.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this BootVolume.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BootVolume.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this BootVolume.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BootVolume.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this BootVolume.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BootVolume.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this BootVolume.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BootVolume.
        The boot volume's Oracle ID (OCID).


        :return: The id of this BootVolume.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BootVolume.
        The boot volume's Oracle ID (OCID).


        :param id: The id of this BootVolume.
        :type: str
        """
        self._id = id

    @property
    def image_id(self):
        """
        Gets the image_id of this BootVolume.
        The image OCID used to create the boot volume.


        :return: The image_id of this BootVolume.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this BootVolume.
        The image OCID used to create the boot volume.


        :param image_id: The image_id of this BootVolume.
        :type: str
        """
        self._image_id = image_id

    @property
    def is_hydrated(self):
        """
        Gets the is_hydrated of this BootVolume.
        Specifies whether the boot volume's data has finished copying
        from the source boot volume or boot volume backup.


        :return: The is_hydrated of this BootVolume.
        :rtype: bool
        """
        return self._is_hydrated

    @is_hydrated.setter
    def is_hydrated(self, is_hydrated):
        """
        Sets the is_hydrated of this BootVolume.
        Specifies whether the boot volume's data has finished copying
        from the source boot volume or boot volume backup.


        :param is_hydrated: The is_hydrated of this BootVolume.
        :type: bool
        """
        self._is_hydrated = is_hydrated

    @property
    def vpus_per_gb(self):
        """
        Gets the vpus_per_gb of this BootVolume.
        The number of volume performance units (VPUs) that will be applied to this boot volume per GB,
        representing the Block Volume service's elastic performance options.
        See `Block Volume Elastic Performance`__ for more information.

        Allowed values:

          * `10`: Represents Balanced option.

          * `20`: Represents Higher Performance option.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeelasticperformance.htm


        :return: The vpus_per_gb of this BootVolume.
        :rtype: int
        """
        return self._vpus_per_gb

    @vpus_per_gb.setter
    def vpus_per_gb(self, vpus_per_gb):
        """
        Sets the vpus_per_gb of this BootVolume.
        The number of volume performance units (VPUs) that will be applied to this boot volume per GB,
        representing the Block Volume service's elastic performance options.
        See `Block Volume Elastic Performance`__ for more information.

        Allowed values:

          * `10`: Represents Balanced option.

          * `20`: Represents Higher Performance option.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeelasticperformance.htm


        :param vpus_per_gb: The vpus_per_gb of this BootVolume.
        :type: int
        """
        self._vpus_per_gb = vpus_per_gb

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BootVolume.
        The current state of a boot volume.

        Allowed values for this property are: "PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BootVolume.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BootVolume.
        The current state of a boot volume.


        :param lifecycle_state: The lifecycle_state of this BootVolume.
        :type: str
        """
        allowed_values = ["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def size_in_gbs(self):
        """
        Gets the size_in_gbs of this BootVolume.
        The size of the boot volume in GBs.


        :return: The size_in_gbs of this BootVolume.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this BootVolume.
        The size of the boot volume in GBs.


        :param size_in_gbs: The size_in_gbs of this BootVolume.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    @property
    def size_in_mbs(self):
        """
        **[Required]** Gets the size_in_mbs of this BootVolume.
        The size of the volume in MBs. The value must be a multiple of 1024.
        This field is deprecated. Please use sizeInGBs.


        :return: The size_in_mbs of this BootVolume.
        :rtype: int
        """
        return self._size_in_mbs

    @size_in_mbs.setter
    def size_in_mbs(self, size_in_mbs):
        """
        Sets the size_in_mbs of this BootVolume.
        The size of the volume in MBs. The value must be a multiple of 1024.
        This field is deprecated. Please use sizeInGBs.


        :param size_in_mbs: The size_in_mbs of this BootVolume.
        :type: int
        """
        self._size_in_mbs = size_in_mbs

    @property
    def source_details(self):
        """
        Gets the source_details of this BootVolume.

        :return: The source_details of this BootVolume.
        :rtype: oci.core.models.BootVolumeSourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this BootVolume.

        :param source_details: The source_details of this BootVolume.
        :type: oci.core.models.BootVolumeSourceDetails
        """
        self._source_details = source_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this BootVolume.
        The date and time the boot volume was created. Format defined
        by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this BootVolume.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BootVolume.
        The date and time the boot volume was created. Format defined
        by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this BootVolume.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def volume_group_id(self):
        """
        Gets the volume_group_id of this BootVolume.
        The OCID of the source volume group.


        :return: The volume_group_id of this BootVolume.
        :rtype: str
        """
        return self._volume_group_id

    @volume_group_id.setter
    def volume_group_id(self, volume_group_id):
        """
        Sets the volume_group_id of this BootVolume.
        The OCID of the source volume group.


        :param volume_group_id: The volume_group_id of this BootVolume.
        :type: str
        """
        self._volume_group_id = volume_group_id

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this BootVolume.
        The OCID of the Key Management master encryption key assigned to the boot volume.


        :return: The kms_key_id of this BootVolume.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this BootVolume.
        The OCID of the Key Management master encryption key assigned to the boot volume.


        :param kms_key_id: The kms_key_id of this BootVolume.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def is_auto_tune_enabled(self):
        """
        Gets the is_auto_tune_enabled of this BootVolume.
        Specifies whether the auto-tune performance is enabled for this boot volume.


        :return: The is_auto_tune_enabled of this BootVolume.
        :rtype: bool
        """
        return self._is_auto_tune_enabled

    @is_auto_tune_enabled.setter
    def is_auto_tune_enabled(self, is_auto_tune_enabled):
        """
        Sets the is_auto_tune_enabled of this BootVolume.
        Specifies whether the auto-tune performance is enabled for this boot volume.


        :param is_auto_tune_enabled: The is_auto_tune_enabled of this BootVolume.
        :type: bool
        """
        self._is_auto_tune_enabled = is_auto_tune_enabled

    @property
    def auto_tuned_vpus_per_gb(self):
        """
        Gets the auto_tuned_vpus_per_gb of this BootVolume.
        The number of Volume Performance Units per GB that this boot volume is effectively tuned to when it's idle.


        :return: The auto_tuned_vpus_per_gb of this BootVolume.
        :rtype: int
        """
        return self._auto_tuned_vpus_per_gb

    @auto_tuned_vpus_per_gb.setter
    def auto_tuned_vpus_per_gb(self, auto_tuned_vpus_per_gb):
        """
        Sets the auto_tuned_vpus_per_gb of this BootVolume.
        The number of Volume Performance Units per GB that this boot volume is effectively tuned to when it's idle.


        :param auto_tuned_vpus_per_gb: The auto_tuned_vpus_per_gb of this BootVolume.
        :type: int
        """
        self._auto_tuned_vpus_per_gb = auto_tuned_vpus_per_gb

    @property
    def boot_volume_replicas(self):
        """
        Gets the boot_volume_replicas of this BootVolume.
        The list of boot volume replicas of this boot volume


        :return: The boot_volume_replicas of this BootVolume.
        :rtype: list[oci.core.models.BootVolumeReplicaInfo]
        """
        return self._boot_volume_replicas

    @boot_volume_replicas.setter
    def boot_volume_replicas(self, boot_volume_replicas):
        """
        Sets the boot_volume_replicas of this BootVolume.
        The list of boot volume replicas of this boot volume


        :param boot_volume_replicas: The boot_volume_replicas of this BootVolume.
        :type: list[oci.core.models.BootVolumeReplicaInfo]
        """
        self._boot_volume_replicas = boot_volume_replicas

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
