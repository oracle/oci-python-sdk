# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchOptions(object):
    """
    Options for tuning compatibility and performance of VM shapes.
    """

    #: A constant which can be used with the boot_volume_type property of a LaunchOptions.
    #: This constant has a value of "ISCSI"
    BOOT_VOLUME_TYPE_ISCSI = "ISCSI"

    #: A constant which can be used with the boot_volume_type property of a LaunchOptions.
    #: This constant has a value of "SCSI"
    BOOT_VOLUME_TYPE_SCSI = "SCSI"

    #: A constant which can be used with the boot_volume_type property of a LaunchOptions.
    #: This constant has a value of "IDE"
    BOOT_VOLUME_TYPE_IDE = "IDE"

    #: A constant which can be used with the boot_volume_type property of a LaunchOptions.
    #: This constant has a value of "VFIO"
    BOOT_VOLUME_TYPE_VFIO = "VFIO"

    #: A constant which can be used with the boot_volume_type property of a LaunchOptions.
    #: This constant has a value of "PARAVIRTUALIZED"
    BOOT_VOLUME_TYPE_PARAVIRTUALIZED = "PARAVIRTUALIZED"

    #: A constant which can be used with the firmware property of a LaunchOptions.
    #: This constant has a value of "BIOS"
    FIRMWARE_BIOS = "BIOS"

    #: A constant which can be used with the firmware property of a LaunchOptions.
    #: This constant has a value of "UEFI_64"
    FIRMWARE_UEFI_64 = "UEFI_64"

    #: A constant which can be used with the network_type property of a LaunchOptions.
    #: This constant has a value of "E1000"
    NETWORK_TYPE_E1000 = "E1000"

    #: A constant which can be used with the network_type property of a LaunchOptions.
    #: This constant has a value of "VFIO"
    NETWORK_TYPE_VFIO = "VFIO"

    #: A constant which can be used with the network_type property of a LaunchOptions.
    #: This constant has a value of "PARAVIRTUALIZED"
    NETWORK_TYPE_PARAVIRTUALIZED = "PARAVIRTUALIZED"

    #: A constant which can be used with the remote_data_volume_type property of a LaunchOptions.
    #: This constant has a value of "ISCSI"
    REMOTE_DATA_VOLUME_TYPE_ISCSI = "ISCSI"

    #: A constant which can be used with the remote_data_volume_type property of a LaunchOptions.
    #: This constant has a value of "SCSI"
    REMOTE_DATA_VOLUME_TYPE_SCSI = "SCSI"

    #: A constant which can be used with the remote_data_volume_type property of a LaunchOptions.
    #: This constant has a value of "IDE"
    REMOTE_DATA_VOLUME_TYPE_IDE = "IDE"

    #: A constant which can be used with the remote_data_volume_type property of a LaunchOptions.
    #: This constant has a value of "VFIO"
    REMOTE_DATA_VOLUME_TYPE_VFIO = "VFIO"

    #: A constant which can be used with the remote_data_volume_type property of a LaunchOptions.
    #: This constant has a value of "PARAVIRTUALIZED"
    REMOTE_DATA_VOLUME_TYPE_PARAVIRTUALIZED = "PARAVIRTUALIZED"

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param boot_volume_type:
            The value to assign to the boot_volume_type property of this LaunchOptions.
            Allowed values for this property are: "ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type boot_volume_type: str

        :param firmware:
            The value to assign to the firmware property of this LaunchOptions.
            Allowed values for this property are: "BIOS", "UEFI_64", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type firmware: str

        :param network_type:
            The value to assign to the network_type property of this LaunchOptions.
            Allowed values for this property are: "E1000", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type network_type: str

        :param remote_data_volume_type:
            The value to assign to the remote_data_volume_type property of this LaunchOptions.
            Allowed values for this property are: "ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type remote_data_volume_type: str

        """
        self.swagger_types = {
            'boot_volume_type': 'str',
            'firmware': 'str',
            'network_type': 'str',
            'remote_data_volume_type': 'str'
        }

        self.attribute_map = {
            'boot_volume_type': 'bootVolumeType',
            'firmware': 'firmware',
            'network_type': 'networkType',
            'remote_data_volume_type': 'remoteDataVolumeType'
        }

        self._boot_volume_type = None
        self._firmware = None
        self._network_type = None
        self._remote_data_volume_type = None

    @property
    def boot_volume_type(self):
        """
        **[Required]** Gets the boot_volume_type of this LaunchOptions.
        Emulation type for volume.
        * `ISCSI` - ISCSI attached block storage device. This is the default for Boot Volumes and Remote Block
        Storage volumes on Oracle provided images.
        * `SCSI` - Emulated SCSI disk.
        * `IDE` - Emulated IDE disk.
        * `VFIO` - Direct attached Virtual Function storage.  This is the default option for Local data
        volumes on Oracle provided images.
        * `PARAVIRTUALIZED` - Paravirtualized disk.

        Allowed values for this property are: "ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The boot_volume_type of this LaunchOptions.
        :rtype: str
        """
        return self._boot_volume_type

    @boot_volume_type.setter
    def boot_volume_type(self, boot_volume_type):
        """
        Sets the boot_volume_type of this LaunchOptions.
        Emulation type for volume.
        * `ISCSI` - ISCSI attached block storage device. This is the default for Boot Volumes and Remote Block
        Storage volumes on Oracle provided images.
        * `SCSI` - Emulated SCSI disk.
        * `IDE` - Emulated IDE disk.
        * `VFIO` - Direct attached Virtual Function storage.  This is the default option for Local data
        volumes on Oracle provided images.
        * `PARAVIRTUALIZED` - Paravirtualized disk.


        :param boot_volume_type: The boot_volume_type of this LaunchOptions.
        :type: str
        """
        allowed_values = ["ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED"]
        if not value_allowed_none_or_none_sentinel(boot_volume_type, allowed_values):
            boot_volume_type = 'UNKNOWN_ENUM_VALUE'
        self._boot_volume_type = boot_volume_type

    @property
    def firmware(self):
        """
        **[Required]** Gets the firmware of this LaunchOptions.
        Firmware used to boot VM.  Select the option that matches your operating system.
        * `BIOS` - Boot VM using BIOS style firmware.  This is compatible with both 32 bit and 64 bit operating
        systems that boot using MBR style bootloaders.
        * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems.  This is the
        default for Oracle provided images.

        Allowed values for this property are: "BIOS", "UEFI_64", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The firmware of this LaunchOptions.
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """
        Sets the firmware of this LaunchOptions.
        Firmware used to boot VM.  Select the option that matches your operating system.
        * `BIOS` - Boot VM using BIOS style firmware.  This is compatible with both 32 bit and 64 bit operating
        systems that boot using MBR style bootloaders.
        * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems.  This is the
        default for Oracle provided images.


        :param firmware: The firmware of this LaunchOptions.
        :type: str
        """
        allowed_values = ["BIOS", "UEFI_64"]
        if not value_allowed_none_or_none_sentinel(firmware, allowed_values):
            firmware = 'UNKNOWN_ENUM_VALUE'
        self._firmware = firmware

    @property
    def network_type(self):
        """
        **[Required]** Gets the network_type of this LaunchOptions.
        Emulation type for NIC.
        * `E1000` - Emulated Gigabit ethernet controller.  Compatible with Linux e1000 network driver.
        * `VFIO` - Direct attached Virtual Function network controller.  Default for Oracle provided images.
        * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using virtio drivers.

        Allowed values for this property are: "E1000", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The network_type of this LaunchOptions.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """
        Sets the network_type of this LaunchOptions.
        Emulation type for NIC.
        * `E1000` - Emulated Gigabit ethernet controller.  Compatible with Linux e1000 network driver.
        * `VFIO` - Direct attached Virtual Function network controller.  Default for Oracle provided images.
        * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using virtio drivers.


        :param network_type: The network_type of this LaunchOptions.
        :type: str
        """
        allowed_values = ["E1000", "VFIO", "PARAVIRTUALIZED"]
        if not value_allowed_none_or_none_sentinel(network_type, allowed_values):
            network_type = 'UNKNOWN_ENUM_VALUE'
        self._network_type = network_type

    @property
    def remote_data_volume_type(self):
        """
        **[Required]** Gets the remote_data_volume_type of this LaunchOptions.
        Emulation type for volume.
        * `ISCSI` - ISCSI attached block storage device. This is the default for Boot Volumes and Remote Block
        Storage volumes on Oracle provided images.
        * `SCSI` - Emulated SCSI disk.
        * `IDE` - Emulated IDE disk.
        * `VFIO` - Direct attached Virtual Function storage.  This is the default option for Local data
        volumes on Oracle provided images.
        * `PARAVIRTUALIZED` - Paravirtualized disk.

        Allowed values for this property are: "ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The remote_data_volume_type of this LaunchOptions.
        :rtype: str
        """
        return self._remote_data_volume_type

    @remote_data_volume_type.setter
    def remote_data_volume_type(self, remote_data_volume_type):
        """
        Sets the remote_data_volume_type of this LaunchOptions.
        Emulation type for volume.
        * `ISCSI` - ISCSI attached block storage device. This is the default for Boot Volumes and Remote Block
        Storage volumes on Oracle provided images.
        * `SCSI` - Emulated SCSI disk.
        * `IDE` - Emulated IDE disk.
        * `VFIO` - Direct attached Virtual Function storage.  This is the default option for Local data
        volumes on Oracle provided images.
        * `PARAVIRTUALIZED` - Paravirtualized disk.


        :param remote_data_volume_type: The remote_data_volume_type of this LaunchOptions.
        :type: str
        """
        allowed_values = ["ISCSI", "SCSI", "IDE", "VFIO", "PARAVIRTUALIZED"]
        if not value_allowed_none_or_none_sentinel(remote_data_volume_type, allowed_values):
            remote_data_volume_type = 'UNKNOWN_ENUM_VALUE'
        self._remote_data_volume_type = remote_data_volume_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
