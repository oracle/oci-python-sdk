# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationLaunchOptions(object):
    """
    Options for tuning the compatibility and performance of VM shapes. The values that you specify override any
    default values.
    """

    #: A constant which can be used with the boot_volume_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "ISCSI"
    BOOT_VOLUME_TYPE_ISCSI = "ISCSI"

    #: A constant which can be used with the boot_volume_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "SCSI"
    BOOT_VOLUME_TYPE_SCSI = "SCSI"

    #: A constant which can be used with the boot_volume_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "IDE"
    BOOT_VOLUME_TYPE_IDE = "IDE"

    #: A constant which can be used with the boot_volume_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "VFIO"
    BOOT_VOLUME_TYPE_VFIO = "VFIO"

    #: A constant which can be used with the boot_volume_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "PARAVIRTUALIZED"
    BOOT_VOLUME_TYPE_PARAVIRTUALIZED = "PARAVIRTUALIZED"

    #: A constant which can be used with the firmware property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "BIOS"
    FIRMWARE_BIOS = "BIOS"

    #: A constant which can be used with the firmware property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "UEFI_64"
    FIRMWARE_UEFI_64 = "UEFI_64"

    #: A constant which can be used with the network_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "E1000"
    NETWORK_TYPE_E1000 = "E1000"

    #: A constant which can be used with the network_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "VFIO"
    NETWORK_TYPE_VFIO = "VFIO"

    #: A constant which can be used with the network_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "PARAVIRTUALIZED"
    NETWORK_TYPE_PARAVIRTUALIZED = "PARAVIRTUALIZED"

    #: A constant which can be used with the remote_data_volume_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "ISCSI"
    REMOTE_DATA_VOLUME_TYPE_ISCSI = "ISCSI"

    #: A constant which can be used with the remote_data_volume_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "SCSI"
    REMOTE_DATA_VOLUME_TYPE_SCSI = "SCSI"

    #: A constant which can be used with the remote_data_volume_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "IDE"
    REMOTE_DATA_VOLUME_TYPE_IDE = "IDE"

    #: A constant which can be used with the remote_data_volume_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "VFIO"
    REMOTE_DATA_VOLUME_TYPE_VFIO = "VFIO"

    #: A constant which can be used with the remote_data_volume_type property of a InstanceConfigurationLaunchOptions.
    #: This constant has a value of "PARAVIRTUALIZED"
    REMOTE_DATA_VOLUME_TYPE_PARAVIRTUALIZED = "PARAVIRTUALIZED"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationLaunchOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param boot_volume_type:
            The value to assign to the boot_volume_type property of this InstanceConfigurationLaunchOptions.
            Allowed values for this property are: "ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type boot_volume_type: str

        :param firmware:
            The value to assign to the firmware property of this InstanceConfigurationLaunchOptions.
            Allowed values for this property are: "BIOS", "UEFI_64", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type firmware: str

        :param network_type:
            The value to assign to the network_type property of this InstanceConfigurationLaunchOptions.
            Allowed values for this property are: "E1000", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type network_type: str

        :param remote_data_volume_type:
            The value to assign to the remote_data_volume_type property of this InstanceConfigurationLaunchOptions.
            Allowed values for this property are: "ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type remote_data_volume_type: str

        :param is_pv_encryption_in_transit_enabled:
            The value to assign to the is_pv_encryption_in_transit_enabled property of this InstanceConfigurationLaunchOptions.
        :type is_pv_encryption_in_transit_enabled: bool

        :param is_consistent_volume_naming_enabled:
            The value to assign to the is_consistent_volume_naming_enabled property of this InstanceConfigurationLaunchOptions.
        :type is_consistent_volume_naming_enabled: bool

        """
        self.swagger_types = {
            'boot_volume_type': 'str',
            'firmware': 'str',
            'network_type': 'str',
            'remote_data_volume_type': 'str',
            'is_pv_encryption_in_transit_enabled': 'bool',
            'is_consistent_volume_naming_enabled': 'bool'
        }

        self.attribute_map = {
            'boot_volume_type': 'bootVolumeType',
            'firmware': 'firmware',
            'network_type': 'networkType',
            'remote_data_volume_type': 'remoteDataVolumeType',
            'is_pv_encryption_in_transit_enabled': 'isPvEncryptionInTransitEnabled',
            'is_consistent_volume_naming_enabled': 'isConsistentVolumeNamingEnabled'
        }

        self._boot_volume_type = None
        self._firmware = None
        self._network_type = None
        self._remote_data_volume_type = None
        self._is_pv_encryption_in_transit_enabled = None
        self._is_consistent_volume_naming_enabled = None

    @property
    def boot_volume_type(self):
        """
        Gets the boot_volume_type of this InstanceConfigurationLaunchOptions.
        Emulation type for the boot volume.
        * `ISCSI` - ISCSI attached block storage device.
        * `SCSI` - Emulated SCSI disk.
        * `IDE` - Emulated IDE disk.
        * `VFIO` - Direct attached Virtual Function storage.  This is the default option for local data
        volumes on Oracle provided images.
        * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
        storage volumes on Oracle-provided images.

        Allowed values for this property are: "ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The boot_volume_type of this InstanceConfigurationLaunchOptions.
        :rtype: str
        """
        return self._boot_volume_type

    @boot_volume_type.setter
    def boot_volume_type(self, boot_volume_type):
        """
        Sets the boot_volume_type of this InstanceConfigurationLaunchOptions.
        Emulation type for the boot volume.
        * `ISCSI` - ISCSI attached block storage device.
        * `SCSI` - Emulated SCSI disk.
        * `IDE` - Emulated IDE disk.
        * `VFIO` - Direct attached Virtual Function storage.  This is the default option for local data
        volumes on Oracle provided images.
        * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
        storage volumes on Oracle-provided images.


        :param boot_volume_type: The boot_volume_type of this InstanceConfigurationLaunchOptions.
        :type: str
        """
        allowed_values = ["ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED"]
        if not value_allowed_none_or_none_sentinel(boot_volume_type, allowed_values):
            boot_volume_type = 'UNKNOWN_ENUM_VALUE'
        self._boot_volume_type = boot_volume_type

    @property
    def firmware(self):
        """
        Gets the firmware of this InstanceConfigurationLaunchOptions.
        Firmware used to boot VM.  Select the option that matches your operating system.
        * `BIOS` - Boot VM using BIOS style firmware.  This is compatible with both 32 bit and 64 bit operating
        systems that boot using MBR style bootloaders.
        * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems.  This is the
        default for Oracle-provided images.

        Allowed values for this property are: "BIOS", "UEFI_64", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The firmware of this InstanceConfigurationLaunchOptions.
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """
        Sets the firmware of this InstanceConfigurationLaunchOptions.
        Firmware used to boot VM.  Select the option that matches your operating system.
        * `BIOS` - Boot VM using BIOS style firmware.  This is compatible with both 32 bit and 64 bit operating
        systems that boot using MBR style bootloaders.
        * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems.  This is the
        default for Oracle-provided images.


        :param firmware: The firmware of this InstanceConfigurationLaunchOptions.
        :type: str
        """
        allowed_values = ["BIOS", "UEFI_64"]
        if not value_allowed_none_or_none_sentinel(firmware, allowed_values):
            firmware = 'UNKNOWN_ENUM_VALUE'
        self._firmware = firmware

    @property
    def network_type(self):
        """
        Gets the network_type of this InstanceConfigurationLaunchOptions.
        Emulation type for the physical network interface card (NIC).
        * `E1000` - Emulated Gigabit ethernet controller.  Compatible with Linux e1000 network driver.
        * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
        when you launch an instance using hardware-assisted (SR-IOV) networking.
        * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.

        Allowed values for this property are: "E1000", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The network_type of this InstanceConfigurationLaunchOptions.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """
        Sets the network_type of this InstanceConfigurationLaunchOptions.
        Emulation type for the physical network interface card (NIC).
        * `E1000` - Emulated Gigabit ethernet controller.  Compatible with Linux e1000 network driver.
        * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
        when you launch an instance using hardware-assisted (SR-IOV) networking.
        * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.


        :param network_type: The network_type of this InstanceConfigurationLaunchOptions.
        :type: str
        """
        allowed_values = ["E1000", "VFIO", "PARAVIRTUALIZED"]
        if not value_allowed_none_or_none_sentinel(network_type, allowed_values):
            network_type = 'UNKNOWN_ENUM_VALUE'
        self._network_type = network_type

    @property
    def remote_data_volume_type(self):
        """
        Gets the remote_data_volume_type of this InstanceConfigurationLaunchOptions.
        Emulation type for volume.
        * `ISCSI` - ISCSI attached block storage device.
        * `SCSI` - Emulated SCSI disk.
        * `IDE` - Emulated IDE disk.
        * `VFIO` - Direct attached Virtual Function storage.  This is the default option for local data
        volumes on Oracle provided images.
        * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
        storage volumes on Oracle-provided images.

        Allowed values for this property are: "ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The remote_data_volume_type of this InstanceConfigurationLaunchOptions.
        :rtype: str
        """
        return self._remote_data_volume_type

    @remote_data_volume_type.setter
    def remote_data_volume_type(self, remote_data_volume_type):
        """
        Sets the remote_data_volume_type of this InstanceConfigurationLaunchOptions.
        Emulation type for volume.
        * `ISCSI` - ISCSI attached block storage device.
        * `SCSI` - Emulated SCSI disk.
        * `IDE` - Emulated IDE disk.
        * `VFIO` - Direct attached Virtual Function storage.  This is the default option for local data
        volumes on Oracle provided images.
        * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
        storage volumes on Oracle-provided images.


        :param remote_data_volume_type: The remote_data_volume_type of this InstanceConfigurationLaunchOptions.
        :type: str
        """
        allowed_values = ["ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED"]
        if not value_allowed_none_or_none_sentinel(remote_data_volume_type, allowed_values):
            remote_data_volume_type = 'UNKNOWN_ENUM_VALUE'
        self._remote_data_volume_type = remote_data_volume_type

    @property
    def is_pv_encryption_in_transit_enabled(self):
        """
        Gets the is_pv_encryption_in_transit_enabled of this InstanceConfigurationLaunchOptions.
        Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
        :func:`instance_configuration_launch_instance_details`.


        :return: The is_pv_encryption_in_transit_enabled of this InstanceConfigurationLaunchOptions.
        :rtype: bool
        """
        return self._is_pv_encryption_in_transit_enabled

    @is_pv_encryption_in_transit_enabled.setter
    def is_pv_encryption_in_transit_enabled(self, is_pv_encryption_in_transit_enabled):
        """
        Sets the is_pv_encryption_in_transit_enabled of this InstanceConfigurationLaunchOptions.
        Deprecated. Instead use `isPvEncryptionInTransitEnabled` in
        :func:`instance_configuration_launch_instance_details`.


        :param is_pv_encryption_in_transit_enabled: The is_pv_encryption_in_transit_enabled of this InstanceConfigurationLaunchOptions.
        :type: bool
        """
        self._is_pv_encryption_in_transit_enabled = is_pv_encryption_in_transit_enabled

    @property
    def is_consistent_volume_naming_enabled(self):
        """
        Gets the is_consistent_volume_naming_enabled of this InstanceConfigurationLaunchOptions.
        Whether to enable consistent volume naming feature. Defaults to false.


        :return: The is_consistent_volume_naming_enabled of this InstanceConfigurationLaunchOptions.
        :rtype: bool
        """
        return self._is_consistent_volume_naming_enabled

    @is_consistent_volume_naming_enabled.setter
    def is_consistent_volume_naming_enabled(self, is_consistent_volume_naming_enabled):
        """
        Sets the is_consistent_volume_naming_enabled of this InstanceConfigurationLaunchOptions.
        Whether to enable consistent volume naming feature. Defaults to false.


        :param is_consistent_volume_naming_enabled: The is_consistent_volume_naming_enabled of this InstanceConfigurationLaunchOptions.
        :type: bool
        """
        self._is_consistent_volume_naming_enabled = is_consistent_volume_naming_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
