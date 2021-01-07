# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBootVolumeBackupDetails(object):
    """
    CreateBootVolumeBackupDetails model.
    """

    #: A constant which can be used with the type property of a CreateBootVolumeBackupDetails.
    #: This constant has a value of "FULL"
    TYPE_FULL = "FULL"

    #: A constant which can be used with the type property of a CreateBootVolumeBackupDetails.
    #: This constant has a value of "INCREMENTAL"
    TYPE_INCREMENTAL = "INCREMENTAL"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBootVolumeBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param boot_volume_id:
            The value to assign to the boot_volume_id property of this CreateBootVolumeBackupDetails.
        :type boot_volume_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBootVolumeBackupDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateBootVolumeBackupDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBootVolumeBackupDetails.
        :type freeform_tags: dict(str, str)

        :param type:
            The value to assign to the type property of this CreateBootVolumeBackupDetails.
            Allowed values for this property are: "FULL", "INCREMENTAL"
        :type type: str

        """
        self.swagger_types = {
            'boot_volume_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'type': 'str'
        }

        self.attribute_map = {
            'boot_volume_id': 'bootVolumeId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'type': 'type'
        }

        self._boot_volume_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._type = None

    @property
    def boot_volume_id(self):
        """
        **[Required]** Gets the boot_volume_id of this CreateBootVolumeBackupDetails.
        The OCID of the boot volume that needs to be backed up.


        :return: The boot_volume_id of this CreateBootVolumeBackupDetails.
        :rtype: str
        """
        return self._boot_volume_id

    @boot_volume_id.setter
    def boot_volume_id(self, boot_volume_id):
        """
        Sets the boot_volume_id of this CreateBootVolumeBackupDetails.
        The OCID of the boot volume that needs to be backed up.


        :param boot_volume_id: The boot_volume_id of this CreateBootVolumeBackupDetails.
        :type: str
        """
        self._boot_volume_id = boot_volume_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateBootVolumeBackupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateBootVolumeBackupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateBootVolumeBackupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateBootVolumeBackupDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateBootVolumeBackupDetails.
        A user-friendly name for the boot volume backup. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateBootVolumeBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateBootVolumeBackupDetails.
        A user-friendly name for the boot volume backup. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateBootVolumeBackupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateBootVolumeBackupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateBootVolumeBackupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateBootVolumeBackupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateBootVolumeBackupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def type(self):
        """
        Gets the type of this CreateBootVolumeBackupDetails.
        The type of backup to create. If omitted, defaults to incremental.

        Allowed values for this property are: "FULL", "INCREMENTAL"


        :return: The type of this CreateBootVolumeBackupDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateBootVolumeBackupDetails.
        The type of backup to create. If omitted, defaults to incremental.


        :param type: The type of this CreateBootVolumeBackupDetails.
        :type: str
        """
        allowed_values = ["FULL", "INCREMENTAL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
