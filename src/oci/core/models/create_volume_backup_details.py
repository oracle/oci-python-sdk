# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVolumeBackupDetails(object):
    """
    CreateVolumeBackupDetails model.
    """

    #: A constant which can be used with the type property of a CreateVolumeBackupDetails.
    #: This constant has a value of "FULL"
    TYPE_FULL = "FULL"

    #: A constant which can be used with the type property of a CreateVolumeBackupDetails.
    #: This constant has a value of "INCREMENTAL"
    TYPE_INCREMENTAL = "INCREMENTAL"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVolumeBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVolumeBackupDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateVolumeBackupDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVolumeBackupDetails.
        :type freeform_tags: dict(str, str)

        :param type:
            The value to assign to the type property of this CreateVolumeBackupDetails.
            Allowed values for this property are: "FULL", "INCREMENTAL"
        :type type: str

        :param volume_id:
            The value to assign to the volume_id property of this CreateVolumeBackupDetails.
        :type volume_id: str

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'type': 'str',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'type': 'type',
            'volume_id': 'volumeId'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._type = None
        self._volume_id = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVolumeBackupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateVolumeBackupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVolumeBackupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateVolumeBackupDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVolumeBackupDetails.
        A user-friendly name for the volume backup. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateVolumeBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVolumeBackupDetails.
        A user-friendly name for the volume backup. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateVolumeBackupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVolumeBackupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateVolumeBackupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVolumeBackupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateVolumeBackupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def type(self):
        """
        Gets the type of this CreateVolumeBackupDetails.
        The type of backup to create. If omitted, defaults to INCREMENTAL.

        Allowed values for this property are: "FULL", "INCREMENTAL"


        :return: The type of this CreateVolumeBackupDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateVolumeBackupDetails.
        The type of backup to create. If omitted, defaults to INCREMENTAL.


        :param type: The type of this CreateVolumeBackupDetails.
        :type: str
        """
        allowed_values = ["FULL", "INCREMENTAL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def volume_id(self):
        """
        **[Required]** Gets the volume_id of this CreateVolumeBackupDetails.
        The OCID of the volume that needs to be backed up.


        :return: The volume_id of this CreateVolumeBackupDetails.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this CreateVolumeBackupDetails.
        The OCID of the volume that needs to be backed up.


        :param volume_id: The volume_id of this CreateVolumeBackupDetails.
        :type: str
        """
        self._volume_id = volume_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
