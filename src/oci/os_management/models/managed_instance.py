# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstance(object):
    """
    Detail information for an OCI Compute instance that is being managed
    """

    #: A constant which can be used with the status property of a ManagedInstance.
    #: This constant has a value of "NORMAL"
    STATUS_NORMAL = "NORMAL"

    #: A constant which can be used with the status property of a ManagedInstance.
    #: This constant has a value of "UNREACHABLE"
    STATUS_UNREACHABLE = "UNREACHABLE"

    #: A constant which can be used with the status property of a ManagedInstance.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    #: A constant which can be used with the status property of a ManagedInstance.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    #: A constant which can be used with the os_family property of a ManagedInstance.
    #: This constant has a value of "LINUX"
    OS_FAMILY_LINUX = "LINUX"

    #: A constant which can be used with the os_family property of a ManagedInstance.
    #: This constant has a value of "WINDOWS"
    OS_FAMILY_WINDOWS = "WINDOWS"

    #: A constant which can be used with the os_family property of a ManagedInstance.
    #: This constant has a value of "ALL"
    OS_FAMILY_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this ManagedInstance.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ManagedInstance.
        :type id: str

        :param description:
            The value to assign to the description property of this ManagedInstance.
        :type description: str

        :param last_checkin:
            The value to assign to the last_checkin property of this ManagedInstance.
        :type last_checkin: str

        :param last_boot:
            The value to assign to the last_boot property of this ManagedInstance.
        :type last_boot: str

        :param updates_available:
            The value to assign to the updates_available property of this ManagedInstance.
        :type updates_available: int

        :param os_name:
            The value to assign to the os_name property of this ManagedInstance.
        :type os_name: str

        :param os_version:
            The value to assign to the os_version property of this ManagedInstance.
        :type os_version: str

        :param os_kernel_version:
            The value to assign to the os_kernel_version property of this ManagedInstance.
        :type os_kernel_version: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedInstance.
        :type compartment_id: str

        :param status:
            The value to assign to the status property of this ManagedInstance.
            Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param parent_software_source:
            The value to assign to the parent_software_source property of this ManagedInstance.
        :type parent_software_source: oci.os_management.models.SoftwareSourceId

        :param child_software_sources:
            The value to assign to the child_software_sources property of this ManagedInstance.
        :type child_software_sources: list[oci.os_management.models.SoftwareSourceId]

        :param managed_instance_groups:
            The value to assign to the managed_instance_groups property of this ManagedInstance.
        :type managed_instance_groups: list[oci.os_management.models.Id]

        :param os_family:
            The value to assign to the os_family property of this ManagedInstance.
            Allowed values for this property are: "LINUX", "WINDOWS", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param is_reboot_required:
            The value to assign to the is_reboot_required property of this ManagedInstance.
        :type is_reboot_required: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'id': 'str',
            'description': 'str',
            'last_checkin': 'str',
            'last_boot': 'str',
            'updates_available': 'int',
            'os_name': 'str',
            'os_version': 'str',
            'os_kernel_version': 'str',
            'compartment_id': 'str',
            'status': 'str',
            'parent_software_source': 'SoftwareSourceId',
            'child_software_sources': 'list[SoftwareSourceId]',
            'managed_instance_groups': 'list[Id]',
            'os_family': 'str',
            'is_reboot_required': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'id': 'id',
            'description': 'description',
            'last_checkin': 'lastCheckin',
            'last_boot': 'lastBoot',
            'updates_available': 'updatesAvailable',
            'os_name': 'osName',
            'os_version': 'osVersion',
            'os_kernel_version': 'osKernelVersion',
            'compartment_id': 'compartmentId',
            'status': 'status',
            'parent_software_source': 'parentSoftwareSource',
            'child_software_sources': 'childSoftwareSources',
            'managed_instance_groups': 'managedInstanceGroups',
            'os_family': 'osFamily',
            'is_reboot_required': 'isRebootRequired'
        }

        self._display_name = None
        self._id = None
        self._description = None
        self._last_checkin = None
        self._last_boot = None
        self._updates_available = None
        self._os_name = None
        self._os_version = None
        self._os_kernel_version = None
        self._compartment_id = None
        self._status = None
        self._parent_software_source = None
        self._child_software_sources = None
        self._managed_instance_groups = None
        self._os_family = None
        self._is_reboot_required = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagedInstance.
        Managed Instance identifier


        :return: The display_name of this ManagedInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagedInstance.
        Managed Instance identifier


        :param display_name: The display_name of this ManagedInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedInstance.
        OCID for the managed instance


        :return: The id of this ManagedInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedInstance.
        OCID for the managed instance


        :param id: The id of this ManagedInstance.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this ManagedInstance.
        Information specified by the user about the managed instance


        :return: The description of this ManagedInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagedInstance.
        Information specified by the user about the managed instance


        :param description: The description of this ManagedInstance.
        :type: str
        """
        self._description = description

    @property
    def last_checkin(self):
        """
        Gets the last_checkin of this ManagedInstance.
        Time at which the instance last checked in


        :return: The last_checkin of this ManagedInstance.
        :rtype: str
        """
        return self._last_checkin

    @last_checkin.setter
    def last_checkin(self, last_checkin):
        """
        Sets the last_checkin of this ManagedInstance.
        Time at which the instance last checked in


        :param last_checkin: The last_checkin of this ManagedInstance.
        :type: str
        """
        self._last_checkin = last_checkin

    @property
    def last_boot(self):
        """
        Gets the last_boot of this ManagedInstance.
        Time at which the instance last booted


        :return: The last_boot of this ManagedInstance.
        :rtype: str
        """
        return self._last_boot

    @last_boot.setter
    def last_boot(self, last_boot):
        """
        Sets the last_boot of this ManagedInstance.
        Time at which the instance last booted


        :param last_boot: The last_boot of this ManagedInstance.
        :type: str
        """
        self._last_boot = last_boot

    @property
    def updates_available(self):
        """
        Gets the updates_available of this ManagedInstance.
        Number of updates available to be installed


        :return: The updates_available of this ManagedInstance.
        :rtype: int
        """
        return self._updates_available

    @updates_available.setter
    def updates_available(self, updates_available):
        """
        Sets the updates_available of this ManagedInstance.
        Number of updates available to be installed


        :param updates_available: The updates_available of this ManagedInstance.
        :type: int
        """
        self._updates_available = updates_available

    @property
    def os_name(self):
        """
        Gets the os_name of this ManagedInstance.
        Operating System Name


        :return: The os_name of this ManagedInstance.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """
        Sets the os_name of this ManagedInstance.
        Operating System Name


        :param os_name: The os_name of this ManagedInstance.
        :type: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        """
        Gets the os_version of this ManagedInstance.
        Operating System Version


        :return: The os_version of this ManagedInstance.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this ManagedInstance.
        Operating System Version


        :param os_version: The os_version of this ManagedInstance.
        :type: str
        """
        self._os_version = os_version

    @property
    def os_kernel_version(self):
        """
        Gets the os_kernel_version of this ManagedInstance.
        Operating System Kernel Version


        :return: The os_kernel_version of this ManagedInstance.
        :rtype: str
        """
        return self._os_kernel_version

    @os_kernel_version.setter
    def os_kernel_version(self, os_kernel_version):
        """
        Sets the os_kernel_version of this ManagedInstance.
        Operating System Kernel Version


        :param os_kernel_version: The os_kernel_version of this ManagedInstance.
        :type: str
        """
        self._os_kernel_version = os_kernel_version

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedInstance.
        OCID for the Compartment


        :return: The compartment_id of this ManagedInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedInstance.
        OCID for the Compartment


        :param compartment_id: The compartment_id of this ManagedInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def status(self):
        """
        Gets the status of this ManagedInstance.
        status of the managed instance.

        Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ManagedInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ManagedInstance.
        status of the managed instance.


        :param status: The status of this ManagedInstance.
        :type: str
        """
        allowed_values = ["NORMAL", "UNREACHABLE", "ERROR", "WARNING"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def parent_software_source(self):
        """
        Gets the parent_software_source of this ManagedInstance.
        the parent (base) Software Source attached to the Managed Instance


        :return: The parent_software_source of this ManagedInstance.
        :rtype: oci.os_management.models.SoftwareSourceId
        """
        return self._parent_software_source

    @parent_software_source.setter
    def parent_software_source(self, parent_software_source):
        """
        Sets the parent_software_source of this ManagedInstance.
        the parent (base) Software Source attached to the Managed Instance


        :param parent_software_source: The parent_software_source of this ManagedInstance.
        :type: oci.os_management.models.SoftwareSourceId
        """
        self._parent_software_source = parent_software_source

    @property
    def child_software_sources(self):
        """
        Gets the child_software_sources of this ManagedInstance.
        list of child Software Sources attached to the Managed Instance


        :return: The child_software_sources of this ManagedInstance.
        :rtype: list[oci.os_management.models.SoftwareSourceId]
        """
        return self._child_software_sources

    @child_software_sources.setter
    def child_software_sources(self, child_software_sources):
        """
        Sets the child_software_sources of this ManagedInstance.
        list of child Software Sources attached to the Managed Instance


        :param child_software_sources: The child_software_sources of this ManagedInstance.
        :type: list[oci.os_management.models.SoftwareSourceId]
        """
        self._child_software_sources = child_software_sources

    @property
    def managed_instance_groups(self):
        """
        Gets the managed_instance_groups of this ManagedInstance.
        The ids of the managed instance groups of which this instance is a
        member.


        :return: The managed_instance_groups of this ManagedInstance.
        :rtype: list[oci.os_management.models.Id]
        """
        return self._managed_instance_groups

    @managed_instance_groups.setter
    def managed_instance_groups(self, managed_instance_groups):
        """
        Sets the managed_instance_groups of this ManagedInstance.
        The ids of the managed instance groups of which this instance is a
        member.


        :param managed_instance_groups: The managed_instance_groups of this ManagedInstance.
        :type: list[oci.os_management.models.Id]
        """
        self._managed_instance_groups = managed_instance_groups

    @property
    def os_family(self):
        """
        Gets the os_family of this ManagedInstance.
        The Operating System type of the managed instance.

        Allowed values for this property are: "LINUX", "WINDOWS", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this ManagedInstance.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this ManagedInstance.
        The Operating System type of the managed instance.


        :param os_family: The os_family of this ManagedInstance.
        :type: str
        """
        allowed_values = ["LINUX", "WINDOWS", "ALL"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    @property
    def is_reboot_required(self):
        """
        Gets the is_reboot_required of this ManagedInstance.
        Indicates whether a reboot is required to complete installation of updates.


        :return: The is_reboot_required of this ManagedInstance.
        :rtype: bool
        """
        return self._is_reboot_required

    @is_reboot_required.setter
    def is_reboot_required(self, is_reboot_required):
        """
        Sets the is_reboot_required of this ManagedInstance.
        Indicates whether a reboot is required to complete installation of updates.


        :param is_reboot_required: The is_reboot_required of this ManagedInstance.
        :type: bool
        """
        self._is_reboot_required = is_reboot_required

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
