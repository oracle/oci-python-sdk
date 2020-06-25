# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSddcDetails(object):
    """
    Details of the SDDC.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSddcDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compute_availability_domain:
            The value to assign to the compute_availability_domain property of this CreateSddcDetails.
        :type compute_availability_domain: str

        :param display_name:
            The value to assign to the display_name property of this CreateSddcDetails.
        :type display_name: str

        :param vmware_software_version:
            The value to assign to the vmware_software_version property of this CreateSddcDetails.
        :type vmware_software_version: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSddcDetails.
        :type compartment_id: str

        :param instance_display_name_prefix:
            The value to assign to the instance_display_name_prefix property of this CreateSddcDetails.
        :type instance_display_name_prefix: str

        :param esxi_hosts_count:
            The value to assign to the esxi_hosts_count property of this CreateSddcDetails.
        :type esxi_hosts_count: int

        :param ssh_authorized_keys:
            The value to assign to the ssh_authorized_keys property of this CreateSddcDetails.
        :type ssh_authorized_keys: str

        :param workload_network_cidr:
            The value to assign to the workload_network_cidr property of this CreateSddcDetails.
        :type workload_network_cidr: str

        :param provisioning_subnet_id:
            The value to assign to the provisioning_subnet_id property of this CreateSddcDetails.
        :type provisioning_subnet_id: str

        :param vsphere_vlan_id:
            The value to assign to the vsphere_vlan_id property of this CreateSddcDetails.
        :type vsphere_vlan_id: str

        :param vmotion_vlan_id:
            The value to assign to the vmotion_vlan_id property of this CreateSddcDetails.
        :type vmotion_vlan_id: str

        :param vsan_vlan_id:
            The value to assign to the vsan_vlan_id property of this CreateSddcDetails.
        :type vsan_vlan_id: str

        :param nsx_v_tep_vlan_id:
            The value to assign to the nsx_v_tep_vlan_id property of this CreateSddcDetails.
        :type nsx_v_tep_vlan_id: str

        :param nsx_edge_v_tep_vlan_id:
            The value to assign to the nsx_edge_v_tep_vlan_id property of this CreateSddcDetails.
        :type nsx_edge_v_tep_vlan_id: str

        :param nsx_edge_uplink1_vlan_id:
            The value to assign to the nsx_edge_uplink1_vlan_id property of this CreateSddcDetails.
        :type nsx_edge_uplink1_vlan_id: str

        :param nsx_edge_uplink2_vlan_id:
            The value to assign to the nsx_edge_uplink2_vlan_id property of this CreateSddcDetails.
        :type nsx_edge_uplink2_vlan_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSddcDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSddcDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compute_availability_domain': 'str',
            'display_name': 'str',
            'vmware_software_version': 'str',
            'compartment_id': 'str',
            'instance_display_name_prefix': 'str',
            'esxi_hosts_count': 'int',
            'ssh_authorized_keys': 'str',
            'workload_network_cidr': 'str',
            'provisioning_subnet_id': 'str',
            'vsphere_vlan_id': 'str',
            'vmotion_vlan_id': 'str',
            'vsan_vlan_id': 'str',
            'nsx_v_tep_vlan_id': 'str',
            'nsx_edge_v_tep_vlan_id': 'str',
            'nsx_edge_uplink1_vlan_id': 'str',
            'nsx_edge_uplink2_vlan_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compute_availability_domain': 'computeAvailabilityDomain',
            'display_name': 'displayName',
            'vmware_software_version': 'vmwareSoftwareVersion',
            'compartment_id': 'compartmentId',
            'instance_display_name_prefix': 'instanceDisplayNamePrefix',
            'esxi_hosts_count': 'esxiHostsCount',
            'ssh_authorized_keys': 'sshAuthorizedKeys',
            'workload_network_cidr': 'workloadNetworkCidr',
            'provisioning_subnet_id': 'provisioningSubnetId',
            'vsphere_vlan_id': 'vsphereVlanId',
            'vmotion_vlan_id': 'vmotionVlanId',
            'vsan_vlan_id': 'vsanVlanId',
            'nsx_v_tep_vlan_id': 'nsxVTepVlanId',
            'nsx_edge_v_tep_vlan_id': 'nsxEdgeVTepVlanId',
            'nsx_edge_uplink1_vlan_id': 'nsxEdgeUplink1VlanId',
            'nsx_edge_uplink2_vlan_id': 'nsxEdgeUplink2VlanId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compute_availability_domain = None
        self._display_name = None
        self._vmware_software_version = None
        self._compartment_id = None
        self._instance_display_name_prefix = None
        self._esxi_hosts_count = None
        self._ssh_authorized_keys = None
        self._workload_network_cidr = None
        self._provisioning_subnet_id = None
        self._vsphere_vlan_id = None
        self._vmotion_vlan_id = None
        self._vsan_vlan_id = None
        self._nsx_v_tep_vlan_id = None
        self._nsx_edge_v_tep_vlan_id = None
        self._nsx_edge_uplink1_vlan_id = None
        self._nsx_edge_uplink2_vlan_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compute_availability_domain(self):
        """
        **[Required]** Gets the compute_availability_domain of this CreateSddcDetails.
        The availability domain to create the SDDC's ESXi hosts in.


        :return: The compute_availability_domain of this CreateSddcDetails.
        :rtype: str
        """
        return self._compute_availability_domain

    @compute_availability_domain.setter
    def compute_availability_domain(self, compute_availability_domain):
        """
        Sets the compute_availability_domain of this CreateSddcDetails.
        The availability domain to create the SDDC's ESXi hosts in.


        :param compute_availability_domain: The compute_availability_domain of this CreateSddcDetails.
        :type: str
        """
        self._compute_availability_domain = compute_availability_domain

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateSddcDetails.
        A descriptive name for the SDDC. It must be unique, start with a letter, and contain only letters, digits,
        whitespaces, dashes and underscores.
        Avoid entering confidential information.


        :return: The display_name of this CreateSddcDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSddcDetails.
        A descriptive name for the SDDC. It must be unique, start with a letter, and contain only letters, digits,
        whitespaces, dashes and underscores.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateSddcDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def vmware_software_version(self):
        """
        **[Required]** Gets the vmware_software_version of this CreateSddcDetails.
        The VMware software bundle to install on the ESXi hosts in the SDDC. To get a
        list of the available versions, use
        :func:`
        _list_supported_vmware_software_versions`.


        :return: The vmware_software_version of this CreateSddcDetails.
        :rtype: str
        """
        return self._vmware_software_version

    @vmware_software_version.setter
    def vmware_software_version(self, vmware_software_version):
        """
        Sets the vmware_software_version of this CreateSddcDetails.
        The VMware software bundle to install on the ESXi hosts in the SDDC. To get a
        list of the available versions, use
        :func:`
        _list_supported_vmware_software_versions`.


        :param vmware_software_version: The vmware_software_version of this CreateSddcDetails.
        :type: str
        """
        self._vmware_software_version = vmware_software_version

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSddcDetails.
        The `OCID`__ of the compartment to contain the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateSddcDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSddcDetails.
        The `OCID`__ of the compartment to contain the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateSddcDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def instance_display_name_prefix(self):
        """
        Gets the instance_display_name_prefix of this CreateSddcDetails.
        A prefix used in the name of each ESXi host and Compute instance in the SDDC.
        If this isn't set, the SDDC's `displayName` is used as the prefix.

        For example, if the value is `mySDDC`, the ESXi hosts are named `mySDDC-1`,
        `mySDDC-2`, and so on.


        :return: The instance_display_name_prefix of this CreateSddcDetails.
        :rtype: str
        """
        return self._instance_display_name_prefix

    @instance_display_name_prefix.setter
    def instance_display_name_prefix(self, instance_display_name_prefix):
        """
        Sets the instance_display_name_prefix of this CreateSddcDetails.
        A prefix used in the name of each ESXi host and Compute instance in the SDDC.
        If this isn't set, the SDDC's `displayName` is used as the prefix.

        For example, if the value is `mySDDC`, the ESXi hosts are named `mySDDC-1`,
        `mySDDC-2`, and so on.


        :param instance_display_name_prefix: The instance_display_name_prefix of this CreateSddcDetails.
        :type: str
        """
        self._instance_display_name_prefix = instance_display_name_prefix

    @property
    def esxi_hosts_count(self):
        """
        **[Required]** Gets the esxi_hosts_count of this CreateSddcDetails.
        The number of ESXi hosts to create in the SDDC. You can add more hosts later
        (see :func:`create_esxi_host`).

        **Note:** If you later delete EXSi hosts from the SDDC to total less than 3,
        you are still billed for the 3 minimum recommended EXSi hosts. Also,
        you cannot add more VMware workloads to the SDDC until it again has at least
        3 ESXi hosts.


        :return: The esxi_hosts_count of this CreateSddcDetails.
        :rtype: int
        """
        return self._esxi_hosts_count

    @esxi_hosts_count.setter
    def esxi_hosts_count(self, esxi_hosts_count):
        """
        Sets the esxi_hosts_count of this CreateSddcDetails.
        The number of ESXi hosts to create in the SDDC. You can add more hosts later
        (see :func:`create_esxi_host`).

        **Note:** If you later delete EXSi hosts from the SDDC to total less than 3,
        you are still billed for the 3 minimum recommended EXSi hosts. Also,
        you cannot add more VMware workloads to the SDDC until it again has at least
        3 ESXi hosts.


        :param esxi_hosts_count: The esxi_hosts_count of this CreateSddcDetails.
        :type: int
        """
        self._esxi_hosts_count = esxi_hosts_count

    @property
    def ssh_authorized_keys(self):
        """
        **[Required]** Gets the ssh_authorized_keys of this CreateSddcDetails.
        One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for
        the default user on each ESXi host. Use a newline character to separate multiple keys.
        The SSH keys must be in the format required for the `authorized_keys` file


        :return: The ssh_authorized_keys of this CreateSddcDetails.
        :rtype: str
        """
        return self._ssh_authorized_keys

    @ssh_authorized_keys.setter
    def ssh_authorized_keys(self, ssh_authorized_keys):
        """
        Sets the ssh_authorized_keys of this CreateSddcDetails.
        One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for
        the default user on each ESXi host. Use a newline character to separate multiple keys.
        The SSH keys must be in the format required for the `authorized_keys` file


        :param ssh_authorized_keys: The ssh_authorized_keys of this CreateSddcDetails.
        :type: str
        """
        self._ssh_authorized_keys = ssh_authorized_keys

    @property
    def workload_network_cidr(self):
        """
        Gets the workload_network_cidr of this CreateSddcDetails.
        The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application
        workloads.


        :return: The workload_network_cidr of this CreateSddcDetails.
        :rtype: str
        """
        return self._workload_network_cidr

    @workload_network_cidr.setter
    def workload_network_cidr(self, workload_network_cidr):
        """
        Sets the workload_network_cidr of this CreateSddcDetails.
        The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application
        workloads.


        :param workload_network_cidr: The workload_network_cidr of this CreateSddcDetails.
        :type: str
        """
        self._workload_network_cidr = workload_network_cidr

    @property
    def provisioning_subnet_id(self):
        """
        **[Required]** Gets the provisioning_subnet_id of this CreateSddcDetails.
        The `OCID`__ of the management subnet to use
        for provisioning the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The provisioning_subnet_id of this CreateSddcDetails.
        :rtype: str
        """
        return self._provisioning_subnet_id

    @provisioning_subnet_id.setter
    def provisioning_subnet_id(self, provisioning_subnet_id):
        """
        Sets the provisioning_subnet_id of this CreateSddcDetails.
        The `OCID`__ of the management subnet to use
        for provisioning the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param provisioning_subnet_id: The provisioning_subnet_id of this CreateSddcDetails.
        :type: str
        """
        self._provisioning_subnet_id = provisioning_subnet_id

    @property
    def vsphere_vlan_id(self):
        """
        **[Required]** Gets the vsphere_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the vSphere
        component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vsphere_vlan_id of this CreateSddcDetails.
        :rtype: str
        """
        return self._vsphere_vlan_id

    @vsphere_vlan_id.setter
    def vsphere_vlan_id(self, vsphere_vlan_id):
        """
        Sets the vsphere_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the vSphere
        component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vsphere_vlan_id: The vsphere_vlan_id of this CreateSddcDetails.
        :type: str
        """
        self._vsphere_vlan_id = vsphere_vlan_id

    @property
    def vmotion_vlan_id(self):
        """
        **[Required]** Gets the vmotion_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the vMotion
        component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vmotion_vlan_id of this CreateSddcDetails.
        :rtype: str
        """
        return self._vmotion_vlan_id

    @vmotion_vlan_id.setter
    def vmotion_vlan_id(self, vmotion_vlan_id):
        """
        Sets the vmotion_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the vMotion
        component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vmotion_vlan_id: The vmotion_vlan_id of this CreateSddcDetails.
        :type: str
        """
        self._vmotion_vlan_id = vmotion_vlan_id

    @property
    def vsan_vlan_id(self):
        """
        **[Required]** Gets the vsan_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the vSAN
        component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vsan_vlan_id of this CreateSddcDetails.
        :rtype: str
        """
        return self._vsan_vlan_id

    @vsan_vlan_id.setter
    def vsan_vlan_id(self, vsan_vlan_id):
        """
        Sets the vsan_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the vSAN
        component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vsan_vlan_id: The vsan_vlan_id of this CreateSddcDetails.
        :type: str
        """
        self._vsan_vlan_id = vsan_vlan_id

    @property
    def nsx_v_tep_vlan_id(self):
        """
        **[Required]** Gets the nsx_v_tep_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the NSX VTEP
        component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_v_tep_vlan_id of this CreateSddcDetails.
        :rtype: str
        """
        return self._nsx_v_tep_vlan_id

    @nsx_v_tep_vlan_id.setter
    def nsx_v_tep_vlan_id(self, nsx_v_tep_vlan_id):
        """
        Sets the nsx_v_tep_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the NSX VTEP
        component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_v_tep_vlan_id: The nsx_v_tep_vlan_id of this CreateSddcDetails.
        :type: str
        """
        self._nsx_v_tep_vlan_id = nsx_v_tep_vlan_id

    @property
    def nsx_edge_v_tep_vlan_id(self):
        """
        **[Required]** Gets the nsx_edge_v_tep_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the NSX Edge VTEP
        component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_v_tep_vlan_id of this CreateSddcDetails.
        :rtype: str
        """
        return self._nsx_edge_v_tep_vlan_id

    @nsx_edge_v_tep_vlan_id.setter
    def nsx_edge_v_tep_vlan_id(self, nsx_edge_v_tep_vlan_id):
        """
        Sets the nsx_edge_v_tep_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the NSX Edge VTEP
        component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_v_tep_vlan_id: The nsx_edge_v_tep_vlan_id of this CreateSddcDetails.
        :type: str
        """
        self._nsx_edge_v_tep_vlan_id = nsx_edge_v_tep_vlan_id

    @property
    def nsx_edge_uplink1_vlan_id(self):
        """
        **[Required]** Gets the nsx_edge_uplink1_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the NSX Edge
        Uplink 1 component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_uplink1_vlan_id of this CreateSddcDetails.
        :rtype: str
        """
        return self._nsx_edge_uplink1_vlan_id

    @nsx_edge_uplink1_vlan_id.setter
    def nsx_edge_uplink1_vlan_id(self, nsx_edge_uplink1_vlan_id):
        """
        Sets the nsx_edge_uplink1_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the NSX Edge
        Uplink 1 component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_uplink1_vlan_id: The nsx_edge_uplink1_vlan_id of this CreateSddcDetails.
        :type: str
        """
        self._nsx_edge_uplink1_vlan_id = nsx_edge_uplink1_vlan_id

    @property
    def nsx_edge_uplink2_vlan_id(self):
        """
        **[Required]** Gets the nsx_edge_uplink2_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the NSX Edge
        Uplink 2 component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_uplink2_vlan_id of this CreateSddcDetails.
        :rtype: str
        """
        return self._nsx_edge_uplink2_vlan_id

    @nsx_edge_uplink2_vlan_id.setter
    def nsx_edge_uplink2_vlan_id(self, nsx_edge_uplink2_vlan_id):
        """
        Sets the nsx_edge_uplink2_vlan_id of this CreateSddcDetails.
        The `OCID`__ of the VLAN to use for the NSX Edge
        Uplink 2 component of the VMware environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_uplink2_vlan_id: The nsx_edge_uplink2_vlan_id of this CreateSddcDetails.
        :type: str
        """
        self._nsx_edge_uplink2_vlan_id = nsx_edge_uplink2_vlan_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSddcDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateSddcDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSddcDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateSddcDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSddcDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateSddcDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSddcDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateSddcDetails.
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
