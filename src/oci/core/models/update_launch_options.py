# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateLaunchOptions(object):
    """
    Options for tuning the compatibility and performance of VM shapes.
    """

    #: A constant which can be used with the boot_volume_type property of a UpdateLaunchOptions.
    #: This constant has a value of "ISCSI"
    BOOT_VOLUME_TYPE_ISCSI = "ISCSI"

    #: A constant which can be used with the boot_volume_type property of a UpdateLaunchOptions.
    #: This constant has a value of "PARAVIRTUALIZED"
    BOOT_VOLUME_TYPE_PARAVIRTUALIZED = "PARAVIRTUALIZED"

    #: A constant which can be used with the network_type property of a UpdateLaunchOptions.
    #: This constant has a value of "VFIO"
    NETWORK_TYPE_VFIO = "VFIO"

    #: A constant which can be used with the network_type property of a UpdateLaunchOptions.
    #: This constant has a value of "PARAVIRTUALIZED"
    NETWORK_TYPE_PARAVIRTUALIZED = "PARAVIRTUALIZED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateLaunchOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param boot_volume_type:
            The value to assign to the boot_volume_type property of this UpdateLaunchOptions.
            Allowed values for this property are: "ISCSI", "PARAVIRTUALIZED"
        :type boot_volume_type: str

        :param network_type:
            The value to assign to the network_type property of this UpdateLaunchOptions.
            Allowed values for this property are: "VFIO", "PARAVIRTUALIZED"
        :type network_type: str

        :param is_pv_encryption_in_transit_enabled:
            The value to assign to the is_pv_encryption_in_transit_enabled property of this UpdateLaunchOptions.
        :type is_pv_encryption_in_transit_enabled: bool

        """
        self.swagger_types = {
            'boot_volume_type': 'str',
            'network_type': 'str',
            'is_pv_encryption_in_transit_enabled': 'bool'
        }

        self.attribute_map = {
            'boot_volume_type': 'bootVolumeType',
            'network_type': 'networkType',
            'is_pv_encryption_in_transit_enabled': 'isPvEncryptionInTransitEnabled'
        }

        self._boot_volume_type = None
        self._network_type = None
        self._is_pv_encryption_in_transit_enabled = None

    @property
    def boot_volume_type(self):
        """
        Gets the boot_volume_type of this UpdateLaunchOptions.
        Emulation type for the boot volume.
        * `ISCSI` - ISCSI attached block storage device.
        * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
        storage volumes on Oracle-provided plaform images.

        Before you change the boot volume attachment type, detach all block volumes and VNICs except for
        the boot volume and the primary VNIC.

        If the instance is running when you change the boot volume attachment type, it will be rebooted.

        **Note:** Some instances might not function properly if you change the boot volume attachment type. After
        the instance reboots and is running, connect to it. If the connection fails or the OS doesn't behave
        as expected, the changes are not supported. Revert the instance to the original boot volume attachment type.

        Allowed values for this property are: "ISCSI", "PARAVIRTUALIZED"


        :return: The boot_volume_type of this UpdateLaunchOptions.
        :rtype: str
        """
        return self._boot_volume_type

    @boot_volume_type.setter
    def boot_volume_type(self, boot_volume_type):
        """
        Sets the boot_volume_type of this UpdateLaunchOptions.
        Emulation type for the boot volume.
        * `ISCSI` - ISCSI attached block storage device.
        * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block
        storage volumes on Oracle-provided plaform images.

        Before you change the boot volume attachment type, detach all block volumes and VNICs except for
        the boot volume and the primary VNIC.

        If the instance is running when you change the boot volume attachment type, it will be rebooted.

        **Note:** Some instances might not function properly if you change the boot volume attachment type. After
        the instance reboots and is running, connect to it. If the connection fails or the OS doesn't behave
        as expected, the changes are not supported. Revert the instance to the original boot volume attachment type.


        :param boot_volume_type: The boot_volume_type of this UpdateLaunchOptions.
        :type: str
        """
        allowed_values = ["ISCSI", "PARAVIRTUALIZED"]
        if not value_allowed_none_or_none_sentinel(boot_volume_type, allowed_values):
            raise ValueError(
                "Invalid value for `boot_volume_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._boot_volume_type = boot_volume_type

    @property
    def network_type(self):
        """
        Gets the network_type of this UpdateLaunchOptions.
        Emulation type for the physical network interface card (NIC).
        * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
        when you launch an instance using hardware-assisted (SR-IOV) networking.
        * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.

        Before you change the networking type, detach all VNICs and block volumes except for the primary
        VNIC and the boot volume.

        The image must have paravirtualized drivers installed. For more information, see
        `Editing an Instance`__.

        If the instance is running when you change the network type, it will be rebooted.

        **Note:** Some instances might not function properly if you change the networking type. After
        the instance reboots and is running, connect to it. If the connection fails or the OS doesn't behave
        as expected, the changes are not supported. Revert the instance to the original networking type.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm

        Allowed values for this property are: "VFIO", "PARAVIRTUALIZED"


        :return: The network_type of this UpdateLaunchOptions.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """
        Sets the network_type of this UpdateLaunchOptions.
        Emulation type for the physical network interface card (NIC).
        * `VFIO` - Direct attached Virtual Function network controller. This is the networking type
        when you launch an instance using hardware-assisted (SR-IOV) networking.
        * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.

        Before you change the networking type, detach all VNICs and block volumes except for the primary
        VNIC and the boot volume.

        The image must have paravirtualized drivers installed. For more information, see
        `Editing an Instance`__.

        If the instance is running when you change the network type, it will be rebooted.

        **Note:** Some instances might not function properly if you change the networking type. After
        the instance reboots and is running, connect to it. If the connection fails or the OS doesn't behave
        as expected, the changes are not supported. Revert the instance to the original networking type.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm


        :param network_type: The network_type of this UpdateLaunchOptions.
        :type: str
        """
        allowed_values = ["VFIO", "PARAVIRTUALIZED"]
        if not value_allowed_none_or_none_sentinel(network_type, allowed_values):
            raise ValueError(
                "Invalid value for `network_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._network_type = network_type

    @property
    def is_pv_encryption_in_transit_enabled(self):
        """
        Gets the is_pv_encryption_in_transit_enabled of this UpdateLaunchOptions.
        Whether to enable in-transit encryption for the boot volume's paravirtualized attachment.

        Data in transit is transferred over an internal and highly secure network. If you have specific
        compliance requirements related to the encryption of the data while it is moving between the
        instance and the boot volume, you can enable in-transit encryption. In-transit encryption is
        not enabled by default.

        All boot volumes are encrypted at rest.

        For more information, see `Block Volume Encryption`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/overview.htm#Encrypti


        :return: The is_pv_encryption_in_transit_enabled of this UpdateLaunchOptions.
        :rtype: bool
        """
        return self._is_pv_encryption_in_transit_enabled

    @is_pv_encryption_in_transit_enabled.setter
    def is_pv_encryption_in_transit_enabled(self, is_pv_encryption_in_transit_enabled):
        """
        Sets the is_pv_encryption_in_transit_enabled of this UpdateLaunchOptions.
        Whether to enable in-transit encryption for the boot volume's paravirtualized attachment.

        Data in transit is transferred over an internal and highly secure network. If you have specific
        compliance requirements related to the encryption of the data while it is moving between the
        instance and the boot volume, you can enable in-transit encryption. In-transit encryption is
        not enabled by default.

        All boot volumes are encrypted at rest.

        For more information, see `Block Volume Encryption`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/overview.htm#Encrypti


        :param is_pv_encryption_in_transit_enabled: The is_pv_encryption_in_transit_enabled of this UpdateLaunchOptions.
        :type: bool
        """
        self._is_pv_encryption_in_transit_enabled = is_pv_encryption_in_transit_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
