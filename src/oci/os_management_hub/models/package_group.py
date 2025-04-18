# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PackageGroup(object):
    """
    Yum or DNF package group, category, or environment.
    """

    #: A constant which can be used with the group_type property of a PackageGroup.
    #: This constant has a value of "GROUP"
    GROUP_TYPE_GROUP = "GROUP"

    #: A constant which can be used with the group_type property of a PackageGroup.
    #: This constant has a value of "ENVIRONMENT"
    GROUP_TYPE_ENVIRONMENT = "ENVIRONMENT"

    #: A constant which can be used with the group_type property of a PackageGroup.
    #: This constant has a value of "CATEGORY"
    GROUP_TYPE_CATEGORY = "CATEGORY"

    def __init__(self, **kwargs):
        """
        Initializes a new PackageGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PackageGroup.
        :type id: str

        :param name:
            The value to assign to the name property of this PackageGroup.
        :type name: str

        :param repositories:
            The value to assign to the repositories property of this PackageGroup.
        :type repositories: list[str]

        :param description:
            The value to assign to the description property of this PackageGroup.
        :type description: str

        :param is_user_visible:
            The value to assign to the is_user_visible property of this PackageGroup.
        :type is_user_visible: bool

        :param is_default:
            The value to assign to the is_default property of this PackageGroup.
        :type is_default: bool

        :param group_type:
            The value to assign to the group_type property of this PackageGroup.
            Allowed values for this property are: "GROUP", "ENVIRONMENT", "CATEGORY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type group_type: str

        :param display_order:
            The value to assign to the display_order property of this PackageGroup.
        :type display_order: int

        :param packages:
            The value to assign to the packages property of this PackageGroup.
        :type packages: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'repositories': 'list[str]',
            'description': 'str',
            'is_user_visible': 'bool',
            'is_default': 'bool',
            'group_type': 'str',
            'display_order': 'int',
            'packages': 'list[str]'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'repositories': 'repositories',
            'description': 'description',
            'is_user_visible': 'isUserVisible',
            'is_default': 'isDefault',
            'group_type': 'groupType',
            'display_order': 'displayOrder',
            'packages': 'packages'
        }
        self._id = None
        self._name = None
        self._repositories = None
        self._description = None
        self._is_user_visible = None
        self._is_default = None
        self._group_type = None
        self._display_order = None
        self._packages = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PackageGroup.
        Package group identifier.


        :return: The id of this PackageGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PackageGroup.
        Package group identifier.


        :param id: The id of this PackageGroup.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PackageGroup.
        Package group name.


        :return: The name of this PackageGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PackageGroup.
        Package group name.


        :param name: The name of this PackageGroup.
        :type: str
        """
        self._name = name

    @property
    def repositories(self):
        """
        Gets the repositories of this PackageGroup.
        The repository IDs of the package group's repositories.


        :return: The repositories of this PackageGroup.
        :rtype: list[str]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        """
        Sets the repositories of this PackageGroup.
        The repository IDs of the package group's repositories.


        :param repositories: The repositories of this PackageGroup.
        :type: list[str]
        """
        self._repositories = repositories

    @property
    def description(self):
        """
        Gets the description of this PackageGroup.
        Description of the package group.


        :return: The description of this PackageGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PackageGroup.
        Description of the package group.


        :param description: The description of this PackageGroup.
        :type: str
        """
        self._description = description

    @property
    def is_user_visible(self):
        """
        Gets the is_user_visible of this PackageGroup.
        Indicates if this package group is visible to users.


        :return: The is_user_visible of this PackageGroup.
        :rtype: bool
        """
        return self._is_user_visible

    @is_user_visible.setter
    def is_user_visible(self, is_user_visible):
        """
        Sets the is_user_visible of this PackageGroup.
        Indicates if this package group is visible to users.


        :param is_user_visible: The is_user_visible of this PackageGroup.
        :type: bool
        """
        self._is_user_visible = is_user_visible

    @property
    def is_default(self):
        """
        Gets the is_default of this PackageGroup.
        Indicates if this package group is the default.


        :return: The is_default of this PackageGroup.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this PackageGroup.
        Indicates if this package group is the default.


        :param is_default: The is_default of this PackageGroup.
        :type: bool
        """
        self._is_default = is_default

    @property
    def group_type(self):
        """
        Gets the group_type of this PackageGroup.
        Indicates if this is a group, category, or environment.

        Allowed values for this property are: "GROUP", "ENVIRONMENT", "CATEGORY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The group_type of this PackageGroup.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """
        Sets the group_type of this PackageGroup.
        Indicates if this is a group, category, or environment.


        :param group_type: The group_type of this PackageGroup.
        :type: str
        """
        allowed_values = ["GROUP", "ENVIRONMENT", "CATEGORY"]
        if not value_allowed_none_or_none_sentinel(group_type, allowed_values):
            group_type = 'UNKNOWN_ENUM_VALUE'
        self._group_type = group_type

    @property
    def display_order(self):
        """
        Gets the display_order of this PackageGroup.
        Indicates the order to display category or environment.


        :return: The display_order of this PackageGroup.
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """
        Sets the display_order of this PackageGroup.
        Indicates the order to display category or environment.


        :param display_order: The display_order of this PackageGroup.
        :type: int
        """
        self._display_order = display_order

    @property
    def packages(self):
        """
        **[Required]** Gets the packages of this PackageGroup.
        The list of packages in the package group.


        :return: The packages of this PackageGroup.
        :rtype: list[str]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """
        Sets the packages of this PackageGroup.
        The list of packages in the package group.


        :param packages: The packages of this PackageGroup.
        :type: list[str]
        """
        self._packages = packages

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
