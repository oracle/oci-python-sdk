# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeProperties(object):
    """
    Compute related properties.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeProperties object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param primary_ip:
            The value to assign to the primary_ip property of this ComputeProperties.
        :type primary_ip: str

        :param dns_name:
            The value to assign to the dns_name property of this ComputeProperties.
        :type dns_name: str

        :param description:
            The value to assign to the description property of this ComputeProperties.
        :type description: str

        :param cores_count:
            The value to assign to the cores_count property of this ComputeProperties.
        :type cores_count: int

        :param cpu_model:
            The value to assign to the cpu_model property of this ComputeProperties.
        :type cpu_model: str

        :param gpu_devices_count:
            The value to assign to the gpu_devices_count property of this ComputeProperties.
        :type gpu_devices_count: int

        :param gpu_devices:
            The value to assign to the gpu_devices property of this ComputeProperties.
        :type gpu_devices: list[oci.cloud_bridge.models.GpuDevice]

        :param threads_per_core_count:
            The value to assign to the threads_per_core_count property of this ComputeProperties.
        :type threads_per_core_count: int

        :param memory_in_mbs:
            The value to assign to the memory_in_mbs property of this ComputeProperties.
        :type memory_in_mbs: int

        :param is_pmem_enabled:
            The value to assign to the is_pmem_enabled property of this ComputeProperties.
        :type is_pmem_enabled: bool

        :param pmem_in_mbs:
            The value to assign to the pmem_in_mbs property of this ComputeProperties.
        :type pmem_in_mbs: int

        :param operating_system:
            The value to assign to the operating_system property of this ComputeProperties.
        :type operating_system: str

        :param operating_system_version:
            The value to assign to the operating_system_version property of this ComputeProperties.
        :type operating_system_version: str

        :param host_name:
            The value to assign to the host_name property of this ComputeProperties.
        :type host_name: str

        :param power_state:
            The value to assign to the power_state property of this ComputeProperties.
        :type power_state: str

        :param guest_state:
            The value to assign to the guest_state property of this ComputeProperties.
        :type guest_state: str

        :param is_tpm_enabled:
            The value to assign to the is_tpm_enabled property of this ComputeProperties.
        :type is_tpm_enabled: bool

        :param connected_networks:
            The value to assign to the connected_networks property of this ComputeProperties.
        :type connected_networks: int

        :param nics_count:
            The value to assign to the nics_count property of this ComputeProperties.
        :type nics_count: int

        :param nics:
            The value to assign to the nics property of this ComputeProperties.
        :type nics: list[oci.cloud_bridge.models.Nic]

        :param storage_provisioned_in_mbs:
            The value to assign to the storage_provisioned_in_mbs property of this ComputeProperties.
        :type storage_provisioned_in_mbs: int

        :param disks_count:
            The value to assign to the disks_count property of this ComputeProperties.
        :type disks_count: int

        :param disks:
            The value to assign to the disks property of this ComputeProperties.
        :type disks: list[oci.cloud_bridge.models.Disk]

        :param firmware:
            The value to assign to the firmware property of this ComputeProperties.
        :type firmware: str

        :param latency_sensitivity:
            The value to assign to the latency_sensitivity property of this ComputeProperties.
        :type latency_sensitivity: str

        :param nvdimms:
            The value to assign to the nvdimms property of this ComputeProperties.
        :type nvdimms: list[oci.cloud_bridge.models.Nvdimm]

        :param nvdimm_controller:
            The value to assign to the nvdimm_controller property of this ComputeProperties.
        :type nvdimm_controller: oci.cloud_bridge.models.NvdimmController

        :param scsi_controller:
            The value to assign to the scsi_controller property of this ComputeProperties.
        :type scsi_controller: oci.cloud_bridge.models.ScsiController

        :param hardware_version:
            The value to assign to the hardware_version property of this ComputeProperties.
        :type hardware_version: str

        """
        self.swagger_types = {
            'primary_ip': 'str',
            'dns_name': 'str',
            'description': 'str',
            'cores_count': 'int',
            'cpu_model': 'str',
            'gpu_devices_count': 'int',
            'gpu_devices': 'list[GpuDevice]',
            'threads_per_core_count': 'int',
            'memory_in_mbs': 'int',
            'is_pmem_enabled': 'bool',
            'pmem_in_mbs': 'int',
            'operating_system': 'str',
            'operating_system_version': 'str',
            'host_name': 'str',
            'power_state': 'str',
            'guest_state': 'str',
            'is_tpm_enabled': 'bool',
            'connected_networks': 'int',
            'nics_count': 'int',
            'nics': 'list[Nic]',
            'storage_provisioned_in_mbs': 'int',
            'disks_count': 'int',
            'disks': 'list[Disk]',
            'firmware': 'str',
            'latency_sensitivity': 'str',
            'nvdimms': 'list[Nvdimm]',
            'nvdimm_controller': 'NvdimmController',
            'scsi_controller': 'ScsiController',
            'hardware_version': 'str'
        }

        self.attribute_map = {
            'primary_ip': 'primaryIp',
            'dns_name': 'dnsName',
            'description': 'description',
            'cores_count': 'coresCount',
            'cpu_model': 'cpuModel',
            'gpu_devices_count': 'gpuDevicesCount',
            'gpu_devices': 'gpuDevices',
            'threads_per_core_count': 'threadsPerCoreCount',
            'memory_in_mbs': 'memoryInMBs',
            'is_pmem_enabled': 'isPmemEnabled',
            'pmem_in_mbs': 'pmemInMBs',
            'operating_system': 'operatingSystem',
            'operating_system_version': 'operatingSystemVersion',
            'host_name': 'hostName',
            'power_state': 'powerState',
            'guest_state': 'guestState',
            'is_tpm_enabled': 'isTpmEnabled',
            'connected_networks': 'connectedNetworks',
            'nics_count': 'nicsCount',
            'nics': 'nics',
            'storage_provisioned_in_mbs': 'storageProvisionedInMBs',
            'disks_count': 'disksCount',
            'disks': 'disks',
            'firmware': 'firmware',
            'latency_sensitivity': 'latencySensitivity',
            'nvdimms': 'nvdimms',
            'nvdimm_controller': 'nvdimmController',
            'scsi_controller': 'scsiController',
            'hardware_version': 'hardwareVersion'
        }

        self._primary_ip = None
        self._dns_name = None
        self._description = None
        self._cores_count = None
        self._cpu_model = None
        self._gpu_devices_count = None
        self._gpu_devices = None
        self._threads_per_core_count = None
        self._memory_in_mbs = None
        self._is_pmem_enabled = None
        self._pmem_in_mbs = None
        self._operating_system = None
        self._operating_system_version = None
        self._host_name = None
        self._power_state = None
        self._guest_state = None
        self._is_tpm_enabled = None
        self._connected_networks = None
        self._nics_count = None
        self._nics = None
        self._storage_provisioned_in_mbs = None
        self._disks_count = None
        self._disks = None
        self._firmware = None
        self._latency_sensitivity = None
        self._nvdimms = None
        self._nvdimm_controller = None
        self._scsi_controller = None
        self._hardware_version = None

    @property
    def primary_ip(self):
        """
        Gets the primary_ip of this ComputeProperties.
        Primary IP address of the compute instance.


        :return: The primary_ip of this ComputeProperties.
        :rtype: str
        """
        return self._primary_ip

    @primary_ip.setter
    def primary_ip(self, primary_ip):
        """
        Sets the primary_ip of this ComputeProperties.
        Primary IP address of the compute instance.


        :param primary_ip: The primary_ip of this ComputeProperties.
        :type: str
        """
        self._primary_ip = primary_ip

    @property
    def dns_name(self):
        """
        Gets the dns_name of this ComputeProperties.
        Fully Qualified DNS Name.


        :return: The dns_name of this ComputeProperties.
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """
        Sets the dns_name of this ComputeProperties.
        Fully Qualified DNS Name.


        :param dns_name: The dns_name of this ComputeProperties.
        :type: str
        """
        self._dns_name = dns_name

    @property
    def description(self):
        """
        Gets the description of this ComputeProperties.
        Information about the asset.


        :return: The description of this ComputeProperties.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ComputeProperties.
        Information about the asset.


        :param description: The description of this ComputeProperties.
        :type: str
        """
        self._description = description

    @property
    def cores_count(self):
        """
        Gets the cores_count of this ComputeProperties.
        Number of CPUs.


        :return: The cores_count of this ComputeProperties.
        :rtype: int
        """
        return self._cores_count

    @cores_count.setter
    def cores_count(self, cores_count):
        """
        Sets the cores_count of this ComputeProperties.
        Number of CPUs.


        :param cores_count: The cores_count of this ComputeProperties.
        :type: int
        """
        self._cores_count = cores_count

    @property
    def cpu_model(self):
        """
        Gets the cpu_model of this ComputeProperties.
        CPU model name.


        :return: The cpu_model of this ComputeProperties.
        :rtype: str
        """
        return self._cpu_model

    @cpu_model.setter
    def cpu_model(self, cpu_model):
        """
        Sets the cpu_model of this ComputeProperties.
        CPU model name.


        :param cpu_model: The cpu_model of this ComputeProperties.
        :type: str
        """
        self._cpu_model = cpu_model

    @property
    def gpu_devices_count(self):
        """
        Gets the gpu_devices_count of this ComputeProperties.
        Number of GPU devices.


        :return: The gpu_devices_count of this ComputeProperties.
        :rtype: int
        """
        return self._gpu_devices_count

    @gpu_devices_count.setter
    def gpu_devices_count(self, gpu_devices_count):
        """
        Sets the gpu_devices_count of this ComputeProperties.
        Number of GPU devices.


        :param gpu_devices_count: The gpu_devices_count of this ComputeProperties.
        :type: int
        """
        self._gpu_devices_count = gpu_devices_count

    @property
    def gpu_devices(self):
        """
        Gets the gpu_devices of this ComputeProperties.
        List of GPU devices attached to a virtual machine.


        :return: The gpu_devices of this ComputeProperties.
        :rtype: list[oci.cloud_bridge.models.GpuDevice]
        """
        return self._gpu_devices

    @gpu_devices.setter
    def gpu_devices(self, gpu_devices):
        """
        Sets the gpu_devices of this ComputeProperties.
        List of GPU devices attached to a virtual machine.


        :param gpu_devices: The gpu_devices of this ComputeProperties.
        :type: list[oci.cloud_bridge.models.GpuDevice]
        """
        self._gpu_devices = gpu_devices

    @property
    def threads_per_core_count(self):
        """
        Gets the threads_per_core_count of this ComputeProperties.
        Number of threads per core.


        :return: The threads_per_core_count of this ComputeProperties.
        :rtype: int
        """
        return self._threads_per_core_count

    @threads_per_core_count.setter
    def threads_per_core_count(self, threads_per_core_count):
        """
        Sets the threads_per_core_count of this ComputeProperties.
        Number of threads per core.


        :param threads_per_core_count: The threads_per_core_count of this ComputeProperties.
        :type: int
        """
        self._threads_per_core_count = threads_per_core_count

    @property
    def memory_in_mbs(self):
        """
        Gets the memory_in_mbs of this ComputeProperties.
        Memory size in MBs.


        :return: The memory_in_mbs of this ComputeProperties.
        :rtype: int
        """
        return self._memory_in_mbs

    @memory_in_mbs.setter
    def memory_in_mbs(self, memory_in_mbs):
        """
        Sets the memory_in_mbs of this ComputeProperties.
        Memory size in MBs.


        :param memory_in_mbs: The memory_in_mbs of this ComputeProperties.
        :type: int
        """
        self._memory_in_mbs = memory_in_mbs

    @property
    def is_pmem_enabled(self):
        """
        Gets the is_pmem_enabled of this ComputeProperties.
        Whether Pmem is enabled. Decides if NVDIMMs are used as a permanent memory.


        :return: The is_pmem_enabled of this ComputeProperties.
        :rtype: bool
        """
        return self._is_pmem_enabled

    @is_pmem_enabled.setter
    def is_pmem_enabled(self, is_pmem_enabled):
        """
        Sets the is_pmem_enabled of this ComputeProperties.
        Whether Pmem is enabled. Decides if NVDIMMs are used as a permanent memory.


        :param is_pmem_enabled: The is_pmem_enabled of this ComputeProperties.
        :type: bool
        """
        self._is_pmem_enabled = is_pmem_enabled

    @property
    def pmem_in_mbs(self):
        """
        Gets the pmem_in_mbs of this ComputeProperties.
        Pmem size in MBs.


        :return: The pmem_in_mbs of this ComputeProperties.
        :rtype: int
        """
        return self._pmem_in_mbs

    @pmem_in_mbs.setter
    def pmem_in_mbs(self, pmem_in_mbs):
        """
        Sets the pmem_in_mbs of this ComputeProperties.
        Pmem size in MBs.


        :param pmem_in_mbs: The pmem_in_mbs of this ComputeProperties.
        :type: int
        """
        self._pmem_in_mbs = pmem_in_mbs

    @property
    def operating_system(self):
        """
        Gets the operating_system of this ComputeProperties.
        Operating system.


        :return: The operating_system of this ComputeProperties.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this ComputeProperties.
        Operating system.


        :param operating_system: The operating_system of this ComputeProperties.
        :type: str
        """
        self._operating_system = operating_system

    @property
    def operating_system_version(self):
        """
        Gets the operating_system_version of this ComputeProperties.
        Operating system version.


        :return: The operating_system_version of this ComputeProperties.
        :rtype: str
        """
        return self._operating_system_version

    @operating_system_version.setter
    def operating_system_version(self, operating_system_version):
        """
        Sets the operating_system_version of this ComputeProperties.
        Operating system version.


        :param operating_system_version: The operating_system_version of this ComputeProperties.
        :type: str
        """
        self._operating_system_version = operating_system_version

    @property
    def host_name(self):
        """
        Gets the host_name of this ComputeProperties.
        Host name of the VM.


        :return: The host_name of this ComputeProperties.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this ComputeProperties.
        Host name of the VM.


        :param host_name: The host_name of this ComputeProperties.
        :type: str
        """
        self._host_name = host_name

    @property
    def power_state(self):
        """
        Gets the power_state of this ComputeProperties.
        The current power state of the virtual machine.


        :return: The power_state of this ComputeProperties.
        :rtype: str
        """
        return self._power_state

    @power_state.setter
    def power_state(self, power_state):
        """
        Sets the power_state of this ComputeProperties.
        The current power state of the virtual machine.


        :param power_state: The power_state of this ComputeProperties.
        :type: str
        """
        self._power_state = power_state

    @property
    def guest_state(self):
        """
        Gets the guest_state of this ComputeProperties.
        Guest state.


        :return: The guest_state of this ComputeProperties.
        :rtype: str
        """
        return self._guest_state

    @guest_state.setter
    def guest_state(self, guest_state):
        """
        Sets the guest_state of this ComputeProperties.
        Guest state.


        :param guest_state: The guest_state of this ComputeProperties.
        :type: str
        """
        self._guest_state = guest_state

    @property
    def is_tpm_enabled(self):
        """
        Gets the is_tpm_enabled of this ComputeProperties.
        Whether Trusted Platform Module (TPM) is enabled.


        :return: The is_tpm_enabled of this ComputeProperties.
        :rtype: bool
        """
        return self._is_tpm_enabled

    @is_tpm_enabled.setter
    def is_tpm_enabled(self, is_tpm_enabled):
        """
        Sets the is_tpm_enabled of this ComputeProperties.
        Whether Trusted Platform Module (TPM) is enabled.


        :param is_tpm_enabled: The is_tpm_enabled of this ComputeProperties.
        :type: bool
        """
        self._is_tpm_enabled = is_tpm_enabled

    @property
    def connected_networks(self):
        """
        Gets the connected_networks of this ComputeProperties.
        Number of connected networks.


        :return: The connected_networks of this ComputeProperties.
        :rtype: int
        """
        return self._connected_networks

    @connected_networks.setter
    def connected_networks(self, connected_networks):
        """
        Sets the connected_networks of this ComputeProperties.
        Number of connected networks.


        :param connected_networks: The connected_networks of this ComputeProperties.
        :type: int
        """
        self._connected_networks = connected_networks

    @property
    def nics_count(self):
        """
        Gets the nics_count of this ComputeProperties.
        Number of network ethernet cards.


        :return: The nics_count of this ComputeProperties.
        :rtype: int
        """
        return self._nics_count

    @nics_count.setter
    def nics_count(self, nics_count):
        """
        Sets the nics_count of this ComputeProperties.
        Number of network ethernet cards.


        :param nics_count: The nics_count of this ComputeProperties.
        :type: int
        """
        self._nics_count = nics_count

    @property
    def nics(self):
        """
        Gets the nics of this ComputeProperties.
        List of network ethernet cards attached to a virtual machine.


        :return: The nics of this ComputeProperties.
        :rtype: list[oci.cloud_bridge.models.Nic]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """
        Sets the nics of this ComputeProperties.
        List of network ethernet cards attached to a virtual machine.


        :param nics: The nics of this ComputeProperties.
        :type: list[oci.cloud_bridge.models.Nic]
        """
        self._nics = nics

    @property
    def storage_provisioned_in_mbs(self):
        """
        Gets the storage_provisioned_in_mbs of this ComputeProperties.
        Provision storage size in MBs.


        :return: The storage_provisioned_in_mbs of this ComputeProperties.
        :rtype: int
        """
        return self._storage_provisioned_in_mbs

    @storage_provisioned_in_mbs.setter
    def storage_provisioned_in_mbs(self, storage_provisioned_in_mbs):
        """
        Sets the storage_provisioned_in_mbs of this ComputeProperties.
        Provision storage size in MBs.


        :param storage_provisioned_in_mbs: The storage_provisioned_in_mbs of this ComputeProperties.
        :type: int
        """
        self._storage_provisioned_in_mbs = storage_provisioned_in_mbs

    @property
    def disks_count(self):
        """
        Gets the disks_count of this ComputeProperties.
        Number of disks.


        :return: The disks_count of this ComputeProperties.
        :rtype: int
        """
        return self._disks_count

    @disks_count.setter
    def disks_count(self, disks_count):
        """
        Sets the disks_count of this ComputeProperties.
        Number of disks.


        :param disks_count: The disks_count of this ComputeProperties.
        :type: int
        """
        self._disks_count = disks_count

    @property
    def disks(self):
        """
        Gets the disks of this ComputeProperties.
        Lists the set of disks belonging to the virtual machine. This list is unordered.


        :return: The disks of this ComputeProperties.
        :rtype: list[oci.cloud_bridge.models.Disk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """
        Sets the disks of this ComputeProperties.
        Lists the set of disks belonging to the virtual machine. This list is unordered.


        :param disks: The disks of this ComputeProperties.
        :type: list[oci.cloud_bridge.models.Disk]
        """
        self._disks = disks

    @property
    def firmware(self):
        """
        Gets the firmware of this ComputeProperties.
        Information about firmware type for this virtual machine.


        :return: The firmware of this ComputeProperties.
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """
        Sets the firmware of this ComputeProperties.
        Information about firmware type for this virtual machine.


        :param firmware: The firmware of this ComputeProperties.
        :type: str
        """
        self._firmware = firmware

    @property
    def latency_sensitivity(self):
        """
        Gets the latency_sensitivity of this ComputeProperties.
        Latency sensitivity.


        :return: The latency_sensitivity of this ComputeProperties.
        :rtype: str
        """
        return self._latency_sensitivity

    @latency_sensitivity.setter
    def latency_sensitivity(self, latency_sensitivity):
        """
        Sets the latency_sensitivity of this ComputeProperties.
        Latency sensitivity.


        :param latency_sensitivity: The latency_sensitivity of this ComputeProperties.
        :type: str
        """
        self._latency_sensitivity = latency_sensitivity

    @property
    def nvdimms(self):
        """
        Gets the nvdimms of this ComputeProperties.
        The properties of the NVDIMMs attached to a virtual machine.


        :return: The nvdimms of this ComputeProperties.
        :rtype: list[oci.cloud_bridge.models.Nvdimm]
        """
        return self._nvdimms

    @nvdimms.setter
    def nvdimms(self, nvdimms):
        """
        Sets the nvdimms of this ComputeProperties.
        The properties of the NVDIMMs attached to a virtual machine.


        :param nvdimms: The nvdimms of this ComputeProperties.
        :type: list[oci.cloud_bridge.models.Nvdimm]
        """
        self._nvdimms = nvdimms

    @property
    def nvdimm_controller(self):
        """
        Gets the nvdimm_controller of this ComputeProperties.

        :return: The nvdimm_controller of this ComputeProperties.
        :rtype: oci.cloud_bridge.models.NvdimmController
        """
        return self._nvdimm_controller

    @nvdimm_controller.setter
    def nvdimm_controller(self, nvdimm_controller):
        """
        Sets the nvdimm_controller of this ComputeProperties.

        :param nvdimm_controller: The nvdimm_controller of this ComputeProperties.
        :type: oci.cloud_bridge.models.NvdimmController
        """
        self._nvdimm_controller = nvdimm_controller

    @property
    def scsi_controller(self):
        """
        Gets the scsi_controller of this ComputeProperties.

        :return: The scsi_controller of this ComputeProperties.
        :rtype: oci.cloud_bridge.models.ScsiController
        """
        return self._scsi_controller

    @scsi_controller.setter
    def scsi_controller(self, scsi_controller):
        """
        Sets the scsi_controller of this ComputeProperties.

        :param scsi_controller: The scsi_controller of this ComputeProperties.
        :type: oci.cloud_bridge.models.ScsiController
        """
        self._scsi_controller = scsi_controller

    @property
    def hardware_version(self):
        """
        Gets the hardware_version of this ComputeProperties.
        Hardware version.


        :return: The hardware_version of this ComputeProperties.
        :rtype: str
        """
        return self._hardware_version

    @hardware_version.setter
    def hardware_version(self, hardware_version):
        """
        Sets the hardware_version of this ComputeProperties.
        Hardware version.


        :param hardware_version: The hardware_version of this ComputeProperties.
        :type: str
        """
        self._hardware_version = hardware_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
