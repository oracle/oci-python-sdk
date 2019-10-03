# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVolumeBackupPolicyDetails(object):
    """
    Contains properties for updating a scheduled backup policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVolumeBackupPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateVolumeBackupPolicyDetails.
        :type display_name: str

        :param schedules:
            The value to assign to the schedules property of this UpdateVolumeBackupPolicyDetails.
        :type schedules: list[VolumeBackupSchedule]

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateVolumeBackupPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateVolumeBackupPolicyDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'display_name': 'str',
            'schedules': 'list[VolumeBackupSchedule]',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'schedules': 'schedules',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._display_name = None
        self._schedules = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateVolumeBackupPolicyDetails.
        A user-friendly name for the volume backup policy. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateVolumeBackupPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateVolumeBackupPolicyDetails.
        A user-friendly name for the volume backup policy. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateVolumeBackupPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def schedules(self):
        """
        Gets the schedules of this UpdateVolumeBackupPolicyDetails.
        The collection of schedules that this policy will apply.


        :return: The schedules of this UpdateVolumeBackupPolicyDetails.
        :rtype: list[VolumeBackupSchedule]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """
        Sets the schedules of this UpdateVolumeBackupPolicyDetails.
        The collection of schedules that this policy will apply.


        :param schedules: The schedules of this UpdateVolumeBackupPolicyDetails.
        :type: list[VolumeBackupSchedule]
        """
        self._schedules = schedules

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateVolumeBackupPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateVolumeBackupPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateVolumeBackupPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateVolumeBackupPolicyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateVolumeBackupPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateVolumeBackupPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateVolumeBackupPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateVolumeBackupPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
