# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WindowsUpdate(object):
    """
    An update available for a Windows managed instance.
    """

    #: A constant which can be used with the update_type property of a WindowsUpdate.
    #: This constant has a value of "SECURITY"
    UPDATE_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the update_type property of a WindowsUpdate.
    #: This constant has a value of "BUG"
    UPDATE_TYPE_BUG = "BUG"

    #: A constant which can be used with the update_type property of a WindowsUpdate.
    #: This constant has a value of "ENHANCEMENT"
    UPDATE_TYPE_ENHANCEMENT = "ENHANCEMENT"

    #: A constant which can be used with the update_type property of a WindowsUpdate.
    #: This constant has a value of "OTHER"
    UPDATE_TYPE_OTHER = "OTHER"

    #: A constant which can be used with the is_eligible_for_installation property of a WindowsUpdate.
    #: This constant has a value of "INSTALLABLE"
    IS_ELIGIBLE_FOR_INSTALLATION_INSTALLABLE = "INSTALLABLE"

    #: A constant which can be used with the is_eligible_for_installation property of a WindowsUpdate.
    #: This constant has a value of "NOT_INSTALLABLE"
    IS_ELIGIBLE_FOR_INSTALLATION_NOT_INSTALLABLE = "NOT_INSTALLABLE"

    #: A constant which can be used with the is_eligible_for_installation property of a WindowsUpdate.
    #: This constant has a value of "UNKNOWN"
    IS_ELIGIBLE_FOR_INSTALLATION_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the installation_requirements property of a WindowsUpdate.
    #: This constant has a value of "EULA_ACCEPTANCE_REQUIRED"
    INSTALLATION_REQUIREMENTS_EULA_ACCEPTANCE_REQUIRED = "EULA_ACCEPTANCE_REQUIRED"

    #: A constant which can be used with the installation_requirements property of a WindowsUpdate.
    #: This constant has a value of "SOFTWARE_MEDIA_REQUIRED"
    INSTALLATION_REQUIREMENTS_SOFTWARE_MEDIA_REQUIRED = "SOFTWARE_MEDIA_REQUIRED"

    #: A constant which can be used with the installation_requirements property of a WindowsUpdate.
    #: This constant has a value of "USER_INTERACTION_REQUIRED"
    INSTALLATION_REQUIREMENTS_USER_INTERACTION_REQUIRED = "USER_INTERACTION_REQUIRED"

    def __init__(self, **kwargs):
        """
        Initializes a new WindowsUpdate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this WindowsUpdate.
        :type display_name: str

        :param name:
            The value to assign to the name property of this WindowsUpdate.
        :type name: str

        :param description:
            The value to assign to the description property of this WindowsUpdate.
        :type description: str

        :param update_type:
            The value to assign to the update_type property of this WindowsUpdate.
            Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type update_type: str

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this WindowsUpdate.
        :type size_in_bytes: int

        :param is_eligible_for_installation:
            The value to assign to the is_eligible_for_installation property of this WindowsUpdate.
            Allowed values for this property are: "INSTALLABLE", "NOT_INSTALLABLE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type is_eligible_for_installation: str

        :param installation_requirements:
            The value to assign to the installation_requirements property of this WindowsUpdate.
            Allowed values for items in this list are: "EULA_ACCEPTANCE_REQUIRED", "SOFTWARE_MEDIA_REQUIRED", "USER_INTERACTION_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type installation_requirements: list[str]

        :param is_reboot_required_for_installation:
            The value to assign to the is_reboot_required_for_installation property of this WindowsUpdate.
        :type is_reboot_required_for_installation: bool

        :param kb_article_ids:
            The value to assign to the kb_article_ids property of this WindowsUpdate.
        :type kb_article_ids: list[str]

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'description': 'str',
            'update_type': 'str',
            'size_in_bytes': 'int',
            'is_eligible_for_installation': 'str',
            'installation_requirements': 'list[str]',
            'is_reboot_required_for_installation': 'bool',
            'kb_article_ids': 'list[str]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'description': 'description',
            'update_type': 'updateType',
            'size_in_bytes': 'sizeInBytes',
            'is_eligible_for_installation': 'isEligibleForInstallation',
            'installation_requirements': 'installationRequirements',
            'is_reboot_required_for_installation': 'isRebootRequiredForInstallation',
            'kb_article_ids': 'kbArticleIds'
        }

        self._display_name = None
        self._name = None
        self._description = None
        self._update_type = None
        self._size_in_bytes = None
        self._is_eligible_for_installation = None
        self._installation_requirements = None
        self._is_reboot_required_for_installation = None
        self._kb_article_ids = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this WindowsUpdate.
        Windows Update name.


        :return: The display_name of this WindowsUpdate.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this WindowsUpdate.
        Windows Update name.


        :param display_name: The display_name of this WindowsUpdate.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this WindowsUpdate.
        Unique identifier for the Windows update. NOTE - This is not an OCID,
        but is a unique identifier assigned by Microsoft.
        Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`


        :return: The name of this WindowsUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WindowsUpdate.
        Unique identifier for the Windows update. NOTE - This is not an OCID,
        but is a unique identifier assigned by Microsoft.
        Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`


        :param name: The name of this WindowsUpdate.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this WindowsUpdate.
        Information about the Windows Update.


        :return: The description of this WindowsUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WindowsUpdate.
        Information about the Windows Update.


        :param description: The description of this WindowsUpdate.
        :type: str
        """
        self._description = description

    @property
    def update_type(self):
        """
        **[Required]** Gets the update_type of this WindowsUpdate.
        The purpose of this update.

        Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The update_type of this WindowsUpdate.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """
        Sets the update_type of this WindowsUpdate.
        The purpose of this update.


        :param update_type: The update_type of this WindowsUpdate.
        :type: str
        """
        allowed_values = ["SECURITY", "BUG", "ENHANCEMENT", "OTHER"]
        if not value_allowed_none_or_none_sentinel(update_type, allowed_values):
            update_type = 'UNKNOWN_ENUM_VALUE'
        self._update_type = update_type

    @property
    def size_in_bytes(self):
        """
        Gets the size_in_bytes of this WindowsUpdate.
        size of the package in bytes


        :return: The size_in_bytes of this WindowsUpdate.
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this WindowsUpdate.
        size of the package in bytes


        :param size_in_bytes: The size_in_bytes of this WindowsUpdate.
        :type: int
        """
        self._size_in_bytes = size_in_bytes

    @property
    def is_eligible_for_installation(self):
        """
        Gets the is_eligible_for_installation of this WindowsUpdate.
        Indicates whether the update can be installed using OSMS.

        Allowed values for this property are: "INSTALLABLE", "NOT_INSTALLABLE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The is_eligible_for_installation of this WindowsUpdate.
        :rtype: str
        """
        return self._is_eligible_for_installation

    @is_eligible_for_installation.setter
    def is_eligible_for_installation(self, is_eligible_for_installation):
        """
        Sets the is_eligible_for_installation of this WindowsUpdate.
        Indicates whether the update can be installed using OSMS.


        :param is_eligible_for_installation: The is_eligible_for_installation of this WindowsUpdate.
        :type: str
        """
        allowed_values = ["INSTALLABLE", "NOT_INSTALLABLE", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(is_eligible_for_installation, allowed_values):
            is_eligible_for_installation = 'UNKNOWN_ENUM_VALUE'
        self._is_eligible_for_installation = is_eligible_for_installation

    @property
    def installation_requirements(self):
        """
        Gets the installation_requirements of this WindowsUpdate.
        List of requirements forinstalling on a managed instances

        Allowed values for items in this list are: "EULA_ACCEPTANCE_REQUIRED", "SOFTWARE_MEDIA_REQUIRED", "USER_INTERACTION_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The installation_requirements of this WindowsUpdate.
        :rtype: list[str]
        """
        return self._installation_requirements

    @installation_requirements.setter
    def installation_requirements(self, installation_requirements):
        """
        Sets the installation_requirements of this WindowsUpdate.
        List of requirements forinstalling on a managed instances


        :param installation_requirements: The installation_requirements of this WindowsUpdate.
        :type: list[str]
        """
        allowed_values = ["EULA_ACCEPTANCE_REQUIRED", "SOFTWARE_MEDIA_REQUIRED", "USER_INTERACTION_REQUIRED"]
        if installation_requirements:
            installation_requirements[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in installation_requirements]
        self._installation_requirements = installation_requirements

    @property
    def is_reboot_required_for_installation(self):
        """
        Gets the is_reboot_required_for_installation of this WindowsUpdate.
        Indicates whether a reboot may be required to complete installation of this update.


        :return: The is_reboot_required_for_installation of this WindowsUpdate.
        :rtype: bool
        """
        return self._is_reboot_required_for_installation

    @is_reboot_required_for_installation.setter
    def is_reboot_required_for_installation(self, is_reboot_required_for_installation):
        """
        Sets the is_reboot_required_for_installation of this WindowsUpdate.
        Indicates whether a reboot may be required to complete installation of this update.


        :param is_reboot_required_for_installation: The is_reboot_required_for_installation of this WindowsUpdate.
        :type: bool
        """
        self._is_reboot_required_for_installation = is_reboot_required_for_installation

    @property
    def kb_article_ids(self):
        """
        Gets the kb_article_ids of this WindowsUpdate.
        List of the Microsoft Knowledge Base Article Ids related to this Windows Update.


        :return: The kb_article_ids of this WindowsUpdate.
        :rtype: list[str]
        """
        return self._kb_article_ids

    @kb_article_ids.setter
    def kb_article_ids(self, kb_article_ids):
        """
        Sets the kb_article_ids of this WindowsUpdate.
        List of the Microsoft Knowledge Base Article Ids related to this Windows Update.


        :param kb_article_ids: The kb_article_ids of this WindowsUpdate.
        :type: list[str]
        """
        self._kb_article_ids = kb_article_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
