# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementAgentImage(object):
    """
    Supported Agent downloads
    """

    #: A constant which can be used with the platform_type property of a ManagementAgentImage.
    #: This constant has a value of "LINUX"
    PLATFORM_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the platform_type property of a ManagementAgentImage.
    #: This constant has a value of "WINDOWS"
    PLATFORM_TYPE_WINDOWS = "WINDOWS"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentImage.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentImage.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentImage.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentImage.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentImage.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentImage.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentImage.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentImage.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementAgentImage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagementAgentImage.
        :type id: str

        :param platform_type:
            The value to assign to the platform_type property of this ManagementAgentImage.
            Allowed values for this property are: "LINUX", "WINDOWS"
        :type platform_type: str

        :param platform_name:
            The value to assign to the platform_name property of this ManagementAgentImage.
        :type platform_name: str

        :param version:
            The value to assign to the version property of this ManagementAgentImage.
        :type version: str

        :param size:
            The value to assign to the size property of this ManagementAgentImage.
        :type size: float

        :param checksum:
            The value to assign to the checksum property of this ManagementAgentImage.
        :type checksum: str

        :param object_url:
            The value to assign to the object_url property of this ManagementAgentImage.
        :type object_url: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagementAgentImage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'platform_type': 'str',
            'platform_name': 'str',
            'version': 'str',
            'size': 'float',
            'checksum': 'str',
            'object_url': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'platform_type': 'platformType',
            'platform_name': 'platformName',
            'version': 'version',
            'size': 'size',
            'checksum': 'checksum',
            'object_url': 'objectUrl',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._platform_type = None
        self._platform_name = None
        self._version = None
        self._size = None
        self._checksum = None
        self._object_url = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagementAgentImage.
        Agent image resource id


        :return: The id of this ManagementAgentImage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagementAgentImage.
        Agent image resource id


        :param id: The id of this ManagementAgentImage.
        :type: str
        """
        self._id = id

    @property
    def platform_type(self):
        """
        **[Required]** Gets the platform_type of this ManagementAgentImage.
        Agent image platform type

        Allowed values for this property are: "LINUX", "WINDOWS"


        :return: The platform_type of this ManagementAgentImage.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this ManagementAgentImage.
        Agent image platform type


        :param platform_type: The platform_type of this ManagementAgentImage.
        :type: str
        """
        allowed_values = ["LINUX", "WINDOWS"]
        if not value_allowed_none_or_none_sentinel(platform_type, allowed_values):
            raise ValueError(
                "Invalid value for `platform_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._platform_type = platform_type

    @property
    def platform_name(self):
        """
        Gets the platform_name of this ManagementAgentImage.
        Agent image platform display name


        :return: The platform_name of this ManagementAgentImage.
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """
        Sets the platform_name of this ManagementAgentImage.
        Agent image platform display name


        :param platform_name: The platform_name of this ManagementAgentImage.
        :type: str
        """
        self._platform_name = platform_name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ManagementAgentImage.
        Agent image version


        :return: The version of this ManagementAgentImage.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ManagementAgentImage.
        Agent image version


        :param version: The version of this ManagementAgentImage.
        :type: str
        """
        self._version = version

    @property
    def size(self):
        """
        Gets the size of this ManagementAgentImage.
        Agent image size in bytes


        :return: The size of this ManagementAgentImage.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this ManagementAgentImage.
        Agent image size in bytes


        :param size: The size of this ManagementAgentImage.
        :type: float
        """
        self._size = size

    @property
    def checksum(self):
        """
        Gets the checksum of this ManagementAgentImage.
        Agent image content SHA256 Hash


        :return: The checksum of this ManagementAgentImage.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """
        Sets the checksum of this ManagementAgentImage.
        Agent image content SHA256 Hash


        :param checksum: The checksum of this ManagementAgentImage.
        :type: str
        """
        self._checksum = checksum

    @property
    def object_url(self):
        """
        Gets the object_url of this ManagementAgentImage.
        Object storage URL for download


        :return: The object_url of this ManagementAgentImage.
        :rtype: str
        """
        return self._object_url

    @object_url.setter
    def object_url(self, object_url):
        """
        Sets the object_url of this ManagementAgentImage.
        Object storage URL for download


        :param object_url: The object_url of this ManagementAgentImage.
        :type: str
        """
        self._object_url = object_url

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ManagementAgentImage.
        The current state of Management Agent Image

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"


        :return: The lifecycle_state of this ManagementAgentImage.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagementAgentImage.
        The current state of Management Agent Image


        :param lifecycle_state: The lifecycle_state of this ManagementAgentImage.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
