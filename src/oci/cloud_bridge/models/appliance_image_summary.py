# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplianceImageSummary(object):
    """
    Description of the ApplianceImage.
    """

    #: A constant which can be used with the lifecycle_state property of a ApplianceImageSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ApplianceImageSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ApplianceImageSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ApplianceImageSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ApplianceImageSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ApplianceImageSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ApplianceImageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ApplianceImageSummary.
        :type id: str

        :param file_name:
            The value to assign to the file_name property of this ApplianceImageSummary.
        :type file_name: str

        :param display_name:
            The value to assign to the display_name property of this ApplianceImageSummary.
        :type display_name: str

        :param version:
            The value to assign to the version property of this ApplianceImageSummary.
        :type version: str

        :param size_in_mbs:
            The value to assign to the size_in_mbs property of this ApplianceImageSummary.
        :type size_in_mbs: str

        :param checksum:
            The value to assign to the checksum property of this ApplianceImageSummary.
        :type checksum: str

        :param platform:
            The value to assign to the platform property of this ApplianceImageSummary.
        :type platform: str

        :param format:
            The value to assign to the format property of this ApplianceImageSummary.
        :type format: str

        :param time_created:
            The value to assign to the time_created property of this ApplianceImageSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ApplianceImageSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ApplianceImageSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param download_url:
            The value to assign to the download_url property of this ApplianceImageSummary.
        :type download_url: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ApplianceImageSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ApplianceImageSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'file_name': 'str',
            'display_name': 'str',
            'version': 'str',
            'size_in_mbs': 'str',
            'checksum': 'str',
            'platform': 'str',
            'format': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'download_url': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'file_name': 'fileName',
            'display_name': 'displayName',
            'version': 'version',
            'size_in_mbs': 'sizeInMBs',
            'checksum': 'checksum',
            'platform': 'platform',
            'format': 'format',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'download_url': 'downloadUrl',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._file_name = None
        self._display_name = None
        self._version = None
        self._size_in_mbs = None
        self._checksum = None
        self._platform = None
        self._format = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._download_url = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ApplianceImageSummary.
        Unique identifier that is immutable on creation.


        :return: The id of this ApplianceImageSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ApplianceImageSummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this ApplianceImageSummary.
        :type: str
        """
        self._id = id

    @property
    def file_name(self):
        """
        **[Required]** Gets the file_name of this ApplianceImageSummary.
        The name of the appliance Image file.


        :return: The file_name of this ApplianceImageSummary.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this ApplianceImageSummary.
        The name of the appliance Image file.


        :param file_name: The file_name of this ApplianceImageSummary.
        :type: str
        """
        self._file_name = file_name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ApplianceImageSummary.
        The name of the image to be displayed.


        :return: The display_name of this ApplianceImageSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApplianceImageSummary.
        The name of the image to be displayed.


        :param display_name: The display_name of this ApplianceImageSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ApplianceImageSummary.
        The version of the image file.


        :return: The version of this ApplianceImageSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ApplianceImageSummary.
        The version of the image file.


        :param version: The version of this ApplianceImageSummary.
        :type: str
        """
        self._version = version

    @property
    def size_in_mbs(self):
        """
        **[Required]** Gets the size_in_mbs of this ApplianceImageSummary.
        The size of the image file in megabytes.


        :return: The size_in_mbs of this ApplianceImageSummary.
        :rtype: str
        """
        return self._size_in_mbs

    @size_in_mbs.setter
    def size_in_mbs(self, size_in_mbs):
        """
        Sets the size_in_mbs of this ApplianceImageSummary.
        The size of the image file in megabytes.


        :param size_in_mbs: The size_in_mbs of this ApplianceImageSummary.
        :type: str
        """
        self._size_in_mbs = size_in_mbs

    @property
    def checksum(self):
        """
        **[Required]** Gets the checksum of this ApplianceImageSummary.
        The checksum of the image file.


        :return: The checksum of this ApplianceImageSummary.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """
        Sets the checksum of this ApplianceImageSummary.
        The checksum of the image file.


        :param checksum: The checksum of this ApplianceImageSummary.
        :type: str
        """
        self._checksum = checksum

    @property
    def platform(self):
        """
        **[Required]** Gets the platform of this ApplianceImageSummary.
        The virtualization platform that the image file supports.


        :return: The platform of this ApplianceImageSummary.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this ApplianceImageSummary.
        The virtualization platform that the image file supports.


        :param platform: The platform of this ApplianceImageSummary.
        :type: str
        """
        self._platform = platform

    @property
    def format(self):
        """
        **[Required]** Gets the format of this ApplianceImageSummary.
        The file format of the image file.


        :return: The format of this ApplianceImageSummary.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this ApplianceImageSummary.
        The file format of the image file.


        :param format: The format of this ApplianceImageSummary.
        :type: str
        """
        self._format = format

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ApplianceImageSummary.
        The time when the appliance image was created.An RFC3339 formatted datetime string.


        :return: The time_created of this ApplianceImageSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ApplianceImageSummary.
        The time when the appliance image was created.An RFC3339 formatted datetime string.


        :param time_created: The time_created of this ApplianceImageSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ApplianceImageSummary.
        The time when the appliance image was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this ApplianceImageSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ApplianceImageSummary.
        The time when the appliance image was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this ApplianceImageSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ApplianceImageSummary.
        The current state of the appliance image.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ApplianceImageSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ApplianceImageSummary.
        The current state of the appliance image.


        :param lifecycle_state: The lifecycle_state of this ApplianceImageSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def download_url(self):
        """
        **[Required]** Gets the download_url of this ApplianceImageSummary.
        The URL from which the appliance image can be downloaded.


        :return: The download_url of this ApplianceImageSummary.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url of this ApplianceImageSummary.
        The URL from which the appliance image can be downloaded.


        :param download_url: The download_url of this ApplianceImageSummary.
        :type: str
        """
        self._download_url = download_url

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ApplianceImageSummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ApplianceImageSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ApplianceImageSummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ApplianceImageSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ApplianceImageSummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ApplianceImageSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ApplianceImageSummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ApplianceImageSummary.
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
