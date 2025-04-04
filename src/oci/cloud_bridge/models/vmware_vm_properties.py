# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220509


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmwareVmProperties(object):
    """
    VMware virtual machine related properties.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VmwareVmProperties object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster:
            The value to assign to the cluster property of this VmwareVmProperties.
        :type cluster: str

        :param customer_fields:
            The value to assign to the customer_fields property of this VmwareVmProperties.
        :type customer_fields: list[str]

        :param customer_tags:
            The value to assign to the customer_tags property of this VmwareVmProperties.
        :type customer_tags: list[oci.cloud_bridge.models.CustomerTag]

        :param instance_uuid:
            The value to assign to the instance_uuid property of this VmwareVmProperties.
        :type instance_uuid: str

        :param path:
            The value to assign to the path property of this VmwareVmProperties.
        :type path: str

        :param vmware_tools_status:
            The value to assign to the vmware_tools_status property of this VmwareVmProperties.
        :type vmware_tools_status: str

        :param is_disks_uuid_enabled:
            The value to assign to the is_disks_uuid_enabled property of this VmwareVmProperties.
        :type is_disks_uuid_enabled: bool

        :param is_disks_cbt_enabled:
            The value to assign to the is_disks_cbt_enabled property of this VmwareVmProperties.
        :type is_disks_cbt_enabled: bool

        :param fault_tolerance_state:
            The value to assign to the fault_tolerance_state property of this VmwareVmProperties.
        :type fault_tolerance_state: str

        :param fault_tolerance_bandwidth:
            The value to assign to the fault_tolerance_bandwidth property of this VmwareVmProperties.
        :type fault_tolerance_bandwidth: int

        :param fault_tolerance_secondary_latency:
            The value to assign to the fault_tolerance_secondary_latency property of this VmwareVmProperties.
        :type fault_tolerance_secondary_latency: int

        """
        self.swagger_types = {
            'cluster': 'str',
            'customer_fields': 'list[str]',
            'customer_tags': 'list[CustomerTag]',
            'instance_uuid': 'str',
            'path': 'str',
            'vmware_tools_status': 'str',
            'is_disks_uuid_enabled': 'bool',
            'is_disks_cbt_enabled': 'bool',
            'fault_tolerance_state': 'str',
            'fault_tolerance_bandwidth': 'int',
            'fault_tolerance_secondary_latency': 'int'
        }
        self.attribute_map = {
            'cluster': 'cluster',
            'customer_fields': 'customerFields',
            'customer_tags': 'customerTags',
            'instance_uuid': 'instanceUuid',
            'path': 'path',
            'vmware_tools_status': 'vmwareToolsStatus',
            'is_disks_uuid_enabled': 'isDisksUuidEnabled',
            'is_disks_cbt_enabled': 'isDisksCbtEnabled',
            'fault_tolerance_state': 'faultToleranceState',
            'fault_tolerance_bandwidth': 'faultToleranceBandwidth',
            'fault_tolerance_secondary_latency': 'faultToleranceSecondaryLatency'
        }
        self._cluster = None
        self._customer_fields = None
        self._customer_tags = None
        self._instance_uuid = None
        self._path = None
        self._vmware_tools_status = None
        self._is_disks_uuid_enabled = None
        self._is_disks_cbt_enabled = None
        self._fault_tolerance_state = None
        self._fault_tolerance_bandwidth = None
        self._fault_tolerance_secondary_latency = None

    @property
    def cluster(self):
        """
        Gets the cluster of this VmwareVmProperties.
        Cluster name.


        :return: The cluster of this VmwareVmProperties.
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """
        Sets the cluster of this VmwareVmProperties.
        Cluster name.


        :param cluster: The cluster of this VmwareVmProperties.
        :type: str
        """
        self._cluster = cluster

    @property
    def customer_fields(self):
        """
        Gets the customer_fields of this VmwareVmProperties.
        Customer fields.


        :return: The customer_fields of this VmwareVmProperties.
        :rtype: list[str]
        """
        return self._customer_fields

    @customer_fields.setter
    def customer_fields(self, customer_fields):
        """
        Sets the customer_fields of this VmwareVmProperties.
        Customer fields.


        :param customer_fields: The customer_fields of this VmwareVmProperties.
        :type: list[str]
        """
        self._customer_fields = customer_fields

    @property
    def customer_tags(self):
        """
        Gets the customer_tags of this VmwareVmProperties.
        Customer defined tags.


        :return: The customer_tags of this VmwareVmProperties.
        :rtype: list[oci.cloud_bridge.models.CustomerTag]
        """
        return self._customer_tags

    @customer_tags.setter
    def customer_tags(self, customer_tags):
        """
        Sets the customer_tags of this VmwareVmProperties.
        Customer defined tags.


        :param customer_tags: The customer_tags of this VmwareVmProperties.
        :type: list[oci.cloud_bridge.models.CustomerTag]
        """
        self._customer_tags = customer_tags

    @property
    def instance_uuid(self):
        """
        Gets the instance_uuid of this VmwareVmProperties.
        vCenter-specific identifier of the virtual machine.


        :return: The instance_uuid of this VmwareVmProperties.
        :rtype: str
        """
        return self._instance_uuid

    @instance_uuid.setter
    def instance_uuid(self, instance_uuid):
        """
        Sets the instance_uuid of this VmwareVmProperties.
        vCenter-specific identifier of the virtual machine.


        :param instance_uuid: The instance_uuid of this VmwareVmProperties.
        :type: str
        """
        self._instance_uuid = instance_uuid

    @property
    def path(self):
        """
        Gets the path of this VmwareVmProperties.
        Path directory of the asset.


        :return: The path of this VmwareVmProperties.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this VmwareVmProperties.
        Path directory of the asset.


        :param path: The path of this VmwareVmProperties.
        :type: str
        """
        self._path = path

    @property
    def vmware_tools_status(self):
        """
        Gets the vmware_tools_status of this VmwareVmProperties.
        VMware tools status.


        :return: The vmware_tools_status of this VmwareVmProperties.
        :rtype: str
        """
        return self._vmware_tools_status

    @vmware_tools_status.setter
    def vmware_tools_status(self, vmware_tools_status):
        """
        Sets the vmware_tools_status of this VmwareVmProperties.
        VMware tools status.


        :param vmware_tools_status: The vmware_tools_status of this VmwareVmProperties.
        :type: str
        """
        self._vmware_tools_status = vmware_tools_status

    @property
    def is_disks_uuid_enabled(self):
        """
        Gets the is_disks_uuid_enabled of this VmwareVmProperties.
        Whether changed block tracking for this VM's disk is active.


        :return: The is_disks_uuid_enabled of this VmwareVmProperties.
        :rtype: bool
        """
        return self._is_disks_uuid_enabled

    @is_disks_uuid_enabled.setter
    def is_disks_uuid_enabled(self, is_disks_uuid_enabled):
        """
        Sets the is_disks_uuid_enabled of this VmwareVmProperties.
        Whether changed block tracking for this VM's disk is active.


        :param is_disks_uuid_enabled: The is_disks_uuid_enabled of this VmwareVmProperties.
        :type: bool
        """
        self._is_disks_uuid_enabled = is_disks_uuid_enabled

    @property
    def is_disks_cbt_enabled(self):
        """
        Gets the is_disks_cbt_enabled of this VmwareVmProperties.
        Indicates that change tracking is supported for virtual disks of this virtual machine.
        However, even if change tracking is supported, it might not be available for all disks of the virtual machine.


        :return: The is_disks_cbt_enabled of this VmwareVmProperties.
        :rtype: bool
        """
        return self._is_disks_cbt_enabled

    @is_disks_cbt_enabled.setter
    def is_disks_cbt_enabled(self, is_disks_cbt_enabled):
        """
        Sets the is_disks_cbt_enabled of this VmwareVmProperties.
        Indicates that change tracking is supported for virtual disks of this virtual machine.
        However, even if change tracking is supported, it might not be available for all disks of the virtual machine.


        :param is_disks_cbt_enabled: The is_disks_cbt_enabled of this VmwareVmProperties.
        :type: bool
        """
        self._is_disks_cbt_enabled = is_disks_cbt_enabled

    @property
    def fault_tolerance_state(self):
        """
        Gets the fault_tolerance_state of this VmwareVmProperties.
        Fault tolerance state.


        :return: The fault_tolerance_state of this VmwareVmProperties.
        :rtype: str
        """
        return self._fault_tolerance_state

    @fault_tolerance_state.setter
    def fault_tolerance_state(self, fault_tolerance_state):
        """
        Sets the fault_tolerance_state of this VmwareVmProperties.
        Fault tolerance state.


        :param fault_tolerance_state: The fault_tolerance_state of this VmwareVmProperties.
        :type: str
        """
        self._fault_tolerance_state = fault_tolerance_state

    @property
    def fault_tolerance_bandwidth(self):
        """
        Gets the fault_tolerance_bandwidth of this VmwareVmProperties.
        Fault tolerance bandwidth.


        :return: The fault_tolerance_bandwidth of this VmwareVmProperties.
        :rtype: int
        """
        return self._fault_tolerance_bandwidth

    @fault_tolerance_bandwidth.setter
    def fault_tolerance_bandwidth(self, fault_tolerance_bandwidth):
        """
        Sets the fault_tolerance_bandwidth of this VmwareVmProperties.
        Fault tolerance bandwidth.


        :param fault_tolerance_bandwidth: The fault_tolerance_bandwidth of this VmwareVmProperties.
        :type: int
        """
        self._fault_tolerance_bandwidth = fault_tolerance_bandwidth

    @property
    def fault_tolerance_secondary_latency(self):
        """
        Gets the fault_tolerance_secondary_latency of this VmwareVmProperties.
        Fault tolerance to secondary latency.


        :return: The fault_tolerance_secondary_latency of this VmwareVmProperties.
        :rtype: int
        """
        return self._fault_tolerance_secondary_latency

    @fault_tolerance_secondary_latency.setter
    def fault_tolerance_secondary_latency(self, fault_tolerance_secondary_latency):
        """
        Sets the fault_tolerance_secondary_latency of this VmwareVmProperties.
        Fault tolerance to secondary latency.


        :param fault_tolerance_secondary_latency: The fault_tolerance_secondary_latency of this VmwareVmProperties.
        :type: int
        """
        self._fault_tolerance_secondary_latency = fault_tolerance_secondary_latency

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
