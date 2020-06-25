# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Sddc(object):
    """
    A software-defined data center (SDDC) contains the resources required for a
    functional VMware environment. Instances in an SDDC
    (see :class:`EsxiHost`) run in a virtual cloud network (VCN)
    and are preconfigured with VMware and storage. Use the vCenter utility to manage
    and deploy VMware virtual machines (VMs) in the SDDC.

    The SDDC uses a single management subnet for provisioning the SDDC. It also uses a
    set of VLANs for various components of the VMware environment (vSphere, vMotion,
    vSAN, and so on). See the Core Services API for information about VCN subnets and VLANs.
    """

    #: A constant which can be used with the lifecycle_state property of a Sddc.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Sddc.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Sddc.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Sddc.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Sddc.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Sddc.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Sddc object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Sddc.
        :type id: str

        :param compute_availability_domain:
            The value to assign to the compute_availability_domain property of this Sddc.
        :type compute_availability_domain: str

        :param display_name:
            The value to assign to the display_name property of this Sddc.
        :type display_name: str

        :param instance_display_name_prefix:
            The value to assign to the instance_display_name_prefix property of this Sddc.
        :type instance_display_name_prefix: str

        :param vmware_software_version:
            The value to assign to the vmware_software_version property of this Sddc.
        :type vmware_software_version: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Sddc.
        :type compartment_id: str

        :param esxi_hosts_count:
            The value to assign to the esxi_hosts_count property of this Sddc.
        :type esxi_hosts_count: int

        :param vcenter_fqdn:
            The value to assign to the vcenter_fqdn property of this Sddc.
        :type vcenter_fqdn: str

        :param nsx_manager_fqdn:
            The value to assign to the nsx_manager_fqdn property of this Sddc.
        :type nsx_manager_fqdn: str

        :param vcenter_private_ip_id:
            The value to assign to the vcenter_private_ip_id property of this Sddc.
        :type vcenter_private_ip_id: str

        :param nsx_manager_private_ip_id:
            The value to assign to the nsx_manager_private_ip_id property of this Sddc.
        :type nsx_manager_private_ip_id: str

        :param vcenter_initial_password:
            The value to assign to the vcenter_initial_password property of this Sddc.
        :type vcenter_initial_password: str

        :param nsx_manager_initial_password:
            The value to assign to the nsx_manager_initial_password property of this Sddc.
        :type nsx_manager_initial_password: str

        :param vcenter_username:
            The value to assign to the vcenter_username property of this Sddc.
        :type vcenter_username: str

        :param nsx_manager_username:
            The value to assign to the nsx_manager_username property of this Sddc.
        :type nsx_manager_username: str

        :param ssh_authorized_keys:
            The value to assign to the ssh_authorized_keys property of this Sddc.
        :type ssh_authorized_keys: str

        :param workload_network_cidr:
            The value to assign to the workload_network_cidr property of this Sddc.
        :type workload_network_cidr: str

        :param nsx_overlay_segment_name:
            The value to assign to the nsx_overlay_segment_name property of this Sddc.
        :type nsx_overlay_segment_name: str

        :param nsx_edge_uplink_ip_id:
            The value to assign to the nsx_edge_uplink_ip_id property of this Sddc.
        :type nsx_edge_uplink_ip_id: str

        :param provisioning_subnet_id:
            The value to assign to the provisioning_subnet_id property of this Sddc.
        :type provisioning_subnet_id: str

        :param vsphere_vlan_id:
            The value to assign to the vsphere_vlan_id property of this Sddc.
        :type vsphere_vlan_id: str

        :param vmotion_vlan_id:
            The value to assign to the vmotion_vlan_id property of this Sddc.
        :type vmotion_vlan_id: str

        :param vsan_vlan_id:
            The value to assign to the vsan_vlan_id property of this Sddc.
        :type vsan_vlan_id: str

        :param nsx_v_tep_vlan_id:
            The value to assign to the nsx_v_tep_vlan_id property of this Sddc.
        :type nsx_v_tep_vlan_id: str

        :param nsx_edge_v_tep_vlan_id:
            The value to assign to the nsx_edge_v_tep_vlan_id property of this Sddc.
        :type nsx_edge_v_tep_vlan_id: str

        :param nsx_edge_uplink1_vlan_id:
            The value to assign to the nsx_edge_uplink1_vlan_id property of this Sddc.
        :type nsx_edge_uplink1_vlan_id: str

        :param nsx_edge_uplink2_vlan_id:
            The value to assign to the nsx_edge_uplink2_vlan_id property of this Sddc.
        :type nsx_edge_uplink2_vlan_id: str

        :param time_created:
            The value to assign to the time_created property of this Sddc.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Sddc.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Sddc.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Sddc.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Sddc.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compute_availability_domain': 'str',
            'display_name': 'str',
            'instance_display_name_prefix': 'str',
            'vmware_software_version': 'str',
            'compartment_id': 'str',
            'esxi_hosts_count': 'int',
            'vcenter_fqdn': 'str',
            'nsx_manager_fqdn': 'str',
            'vcenter_private_ip_id': 'str',
            'nsx_manager_private_ip_id': 'str',
            'vcenter_initial_password': 'str',
            'nsx_manager_initial_password': 'str',
            'vcenter_username': 'str',
            'nsx_manager_username': 'str',
            'ssh_authorized_keys': 'str',
            'workload_network_cidr': 'str',
            'nsx_overlay_segment_name': 'str',
            'nsx_edge_uplink_ip_id': 'str',
            'provisioning_subnet_id': 'str',
            'vsphere_vlan_id': 'str',
            'vmotion_vlan_id': 'str',
            'vsan_vlan_id': 'str',
            'nsx_v_tep_vlan_id': 'str',
            'nsx_edge_v_tep_vlan_id': 'str',
            'nsx_edge_uplink1_vlan_id': 'str',
            'nsx_edge_uplink2_vlan_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compute_availability_domain': 'computeAvailabilityDomain',
            'display_name': 'displayName',
            'instance_display_name_prefix': 'instanceDisplayNamePrefix',
            'vmware_software_version': 'vmwareSoftwareVersion',
            'compartment_id': 'compartmentId',
            'esxi_hosts_count': 'esxiHostsCount',
            'vcenter_fqdn': 'vcenterFqdn',
            'nsx_manager_fqdn': 'nsxManagerFqdn',
            'vcenter_private_ip_id': 'vcenterPrivateIpId',
            'nsx_manager_private_ip_id': 'nsxManagerPrivateIpId',
            'vcenter_initial_password': 'vcenterInitialPassword',
            'nsx_manager_initial_password': 'nsxManagerInitialPassword',
            'vcenter_username': 'vcenterUsername',
            'nsx_manager_username': 'nsxManagerUsername',
            'ssh_authorized_keys': 'sshAuthorizedKeys',
            'workload_network_cidr': 'workloadNetworkCidr',
            'nsx_overlay_segment_name': 'nsxOverlaySegmentName',
            'nsx_edge_uplink_ip_id': 'nsxEdgeUplinkIpId',
            'provisioning_subnet_id': 'provisioningSubnetId',
            'vsphere_vlan_id': 'vsphereVlanId',
            'vmotion_vlan_id': 'vmotionVlanId',
            'vsan_vlan_id': 'vsanVlanId',
            'nsx_v_tep_vlan_id': 'nsxVTepVlanId',
            'nsx_edge_v_tep_vlan_id': 'nsxEdgeVTepVlanId',
            'nsx_edge_uplink1_vlan_id': 'nsxEdgeUplink1VlanId',
            'nsx_edge_uplink2_vlan_id': 'nsxEdgeUplink2VlanId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compute_availability_domain = None
        self._display_name = None
        self._instance_display_name_prefix = None
        self._vmware_software_version = None
        self._compartment_id = None
        self._esxi_hosts_count = None
        self._vcenter_fqdn = None
        self._nsx_manager_fqdn = None
        self._vcenter_private_ip_id = None
        self._nsx_manager_private_ip_id = None
        self._vcenter_initial_password = None
        self._nsx_manager_initial_password = None
        self._vcenter_username = None
        self._nsx_manager_username = None
        self._ssh_authorized_keys = None
        self._workload_network_cidr = None
        self._nsx_overlay_segment_name = None
        self._nsx_edge_uplink_ip_id = None
        self._provisioning_subnet_id = None
        self._vsphere_vlan_id = None
        self._vmotion_vlan_id = None
        self._vsan_vlan_id = None
        self._nsx_v_tep_vlan_id = None
        self._nsx_edge_v_tep_vlan_id = None
        self._nsx_edge_uplink1_vlan_id = None
        self._nsx_edge_uplink2_vlan_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Sddc.
        The `OCID`__ of the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Sddc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Sddc.
        The `OCID`__ of the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Sddc.
        :type: str
        """
        self._id = id

    @property
    def compute_availability_domain(self):
        """
        **[Required]** Gets the compute_availability_domain of this Sddc.
        The availability domain the ESXi hosts are running in.

        Example: `Uocm:PHX-AD-1`


        :return: The compute_availability_domain of this Sddc.
        :rtype: str
        """
        return self._compute_availability_domain

    @compute_availability_domain.setter
    def compute_availability_domain(self, compute_availability_domain):
        """
        Sets the compute_availability_domain of this Sddc.
        The availability domain the ESXi hosts are running in.

        Example: `Uocm:PHX-AD-1`


        :param compute_availability_domain: The compute_availability_domain of this Sddc.
        :type: str
        """
        self._compute_availability_domain = compute_availability_domain

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Sddc.
        A descriptive name for the SDDC. It must be unique, start with a letter, and contain only letters, digits,
        whitespaces, dashes and underscores.
        Avoid entering confidential information.


        :return: The display_name of this Sddc.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Sddc.
        A descriptive name for the SDDC. It must be unique, start with a letter, and contain only letters, digits,
        whitespaces, dashes and underscores.
        Avoid entering confidential information.


        :param display_name: The display_name of this Sddc.
        :type: str
        """
        self._display_name = display_name

    @property
    def instance_display_name_prefix(self):
        """
        Gets the instance_display_name_prefix of this Sddc.
        A prefix used in the name of each ESXi host and Compute instance in the SDDC.
        If this isn't set, the SDDC's `displayName` is used as the prefix.

        For example, if the value is `MySDDC`, the ESXi hosts are named `MySDDC-1`,
        `MySDDC-2`, and so on.


        :return: The instance_display_name_prefix of this Sddc.
        :rtype: str
        """
        return self._instance_display_name_prefix

    @instance_display_name_prefix.setter
    def instance_display_name_prefix(self, instance_display_name_prefix):
        """
        Sets the instance_display_name_prefix of this Sddc.
        A prefix used in the name of each ESXi host and Compute instance in the SDDC.
        If this isn't set, the SDDC's `displayName` is used as the prefix.

        For example, if the value is `MySDDC`, the ESXi hosts are named `MySDDC-1`,
        `MySDDC-2`, and so on.


        :param instance_display_name_prefix: The instance_display_name_prefix of this Sddc.
        :type: str
        """
        self._instance_display_name_prefix = instance_display_name_prefix

    @property
    def vmware_software_version(self):
        """
        **[Required]** Gets the vmware_software_version of this Sddc.
        In general, this is a specific version of bundled VMware software supported by
        Oracle Cloud VMware Solution (see
        :func:`
        _list_supported_vmware_software_versions`).

        This attribute is not guaranteed to reflect the version of
        software currently installed on the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the version of software that the Oracle
        Cloud VMware Solution will install on any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you upgrade the existing ESXi hosts in the SDDC to use a newer
        version of bundled VMware software supported by the Oracle Cloud VMware Solution, you
        should use :func:`update_sddc` to update the SDDC's
        `vmwareSoftwareVersion` with that new version.


        :return: The vmware_software_version of this Sddc.
        :rtype: str
        """
        return self._vmware_software_version

    @vmware_software_version.setter
    def vmware_software_version(self, vmware_software_version):
        """
        Sets the vmware_software_version of this Sddc.
        In general, this is a specific version of bundled VMware software supported by
        Oracle Cloud VMware Solution (see
        :func:`
        _list_supported_vmware_software_versions`).

        This attribute is not guaranteed to reflect the version of
        software currently installed on the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the version of software that the Oracle
        Cloud VMware Solution will install on any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you upgrade the existing ESXi hosts in the SDDC to use a newer
        version of bundled VMware software supported by the Oracle Cloud VMware Solution, you
        should use :func:`update_sddc` to update the SDDC's
        `vmwareSoftwareVersion` with that new version.


        :param vmware_software_version: The vmware_software_version of this Sddc.
        :type: str
        """
        self._vmware_software_version = vmware_software_version

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Sddc.
        The `OCID`__ of the compartment that
        contains the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Sddc.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Sddc.
        The `OCID`__ of the compartment that
        contains the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Sddc.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def esxi_hosts_count(self):
        """
        **[Required]** Gets the esxi_hosts_count of this Sddc.
        The number of ESXi hosts in the SDDC.


        :return: The esxi_hosts_count of this Sddc.
        :rtype: int
        """
        return self._esxi_hosts_count

    @esxi_hosts_count.setter
    def esxi_hosts_count(self, esxi_hosts_count):
        """
        Sets the esxi_hosts_count of this Sddc.
        The number of ESXi hosts in the SDDC.


        :param esxi_hosts_count: The esxi_hosts_count of this Sddc.
        :type: int
        """
        self._esxi_hosts_count = esxi_hosts_count

    @property
    def vcenter_fqdn(self):
        """
        **[Required]** Gets the vcenter_fqdn of this Sddc.
        FQDN for vCenter

        Example: `vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com`


        :return: The vcenter_fqdn of this Sddc.
        :rtype: str
        """
        return self._vcenter_fqdn

    @vcenter_fqdn.setter
    def vcenter_fqdn(self, vcenter_fqdn):
        """
        Sets the vcenter_fqdn of this Sddc.
        FQDN for vCenter

        Example: `vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com`


        :param vcenter_fqdn: The vcenter_fqdn of this Sddc.
        :type: str
        """
        self._vcenter_fqdn = vcenter_fqdn

    @property
    def nsx_manager_fqdn(self):
        """
        **[Required]** Gets the nsx_manager_fqdn of this Sddc.
        FQDN for NSX Manager

        Example: `nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com`


        :return: The nsx_manager_fqdn of this Sddc.
        :rtype: str
        """
        return self._nsx_manager_fqdn

    @nsx_manager_fqdn.setter
    def nsx_manager_fqdn(self, nsx_manager_fqdn):
        """
        Sets the nsx_manager_fqdn of this Sddc.
        FQDN for NSX Manager

        Example: `nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com`


        :param nsx_manager_fqdn: The nsx_manager_fqdn of this Sddc.
        :type: str
        """
        self._nsx_manager_fqdn = nsx_manager_fqdn

    @property
    def vcenter_private_ip_id(self):
        """
        **[Required]** Gets the vcenter_private_ip_id of this Sddc.
        The `OCID`__ of the `PrivateIp` object that is
        the virtual IP (VIP) for vCenter. For information about `PrivateIp` objects, see the
        Core Services API.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vcenter_private_ip_id of this Sddc.
        :rtype: str
        """
        return self._vcenter_private_ip_id

    @vcenter_private_ip_id.setter
    def vcenter_private_ip_id(self, vcenter_private_ip_id):
        """
        Sets the vcenter_private_ip_id of this Sddc.
        The `OCID`__ of the `PrivateIp` object that is
        the virtual IP (VIP) for vCenter. For information about `PrivateIp` objects, see the
        Core Services API.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vcenter_private_ip_id: The vcenter_private_ip_id of this Sddc.
        :type: str
        """
        self._vcenter_private_ip_id = vcenter_private_ip_id

    @property
    def nsx_manager_private_ip_id(self):
        """
        **[Required]** Gets the nsx_manager_private_ip_id of this Sddc.
        The `OCID`__ of the `PrivateIp` object that is
        the virtual IP (VIP) for NSX Manager. For information about `PrivateIp` objects, see the
        Core Services API.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_manager_private_ip_id of this Sddc.
        :rtype: str
        """
        return self._nsx_manager_private_ip_id

    @nsx_manager_private_ip_id.setter
    def nsx_manager_private_ip_id(self, nsx_manager_private_ip_id):
        """
        Sets the nsx_manager_private_ip_id of this Sddc.
        The `OCID`__ of the `PrivateIp` object that is
        the virtual IP (VIP) for NSX Manager. For information about `PrivateIp` objects, see the
        Core Services API.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_manager_private_ip_id: The nsx_manager_private_ip_id of this Sddc.
        :type: str
        """
        self._nsx_manager_private_ip_id = nsx_manager_private_ip_id

    @property
    def vcenter_initial_password(self):
        """
        Gets the vcenter_initial_password of this Sddc.
        The SDDC includes an administrator username and initial password for vCenter. Make sure
        to change this initial vCenter password to a different value.


        :return: The vcenter_initial_password of this Sddc.
        :rtype: str
        """
        return self._vcenter_initial_password

    @vcenter_initial_password.setter
    def vcenter_initial_password(self, vcenter_initial_password):
        """
        Sets the vcenter_initial_password of this Sddc.
        The SDDC includes an administrator username and initial password for vCenter. Make sure
        to change this initial vCenter password to a different value.


        :param vcenter_initial_password: The vcenter_initial_password of this Sddc.
        :type: str
        """
        self._vcenter_initial_password = vcenter_initial_password

    @property
    def nsx_manager_initial_password(self):
        """
        Gets the nsx_manager_initial_password of this Sddc.
        The SDDC includes an administrator username and initial password for NSX Manager. Make sure
        to change this initial NSX Manager password to a different value.


        :return: The nsx_manager_initial_password of this Sddc.
        :rtype: str
        """
        return self._nsx_manager_initial_password

    @nsx_manager_initial_password.setter
    def nsx_manager_initial_password(self, nsx_manager_initial_password):
        """
        Sets the nsx_manager_initial_password of this Sddc.
        The SDDC includes an administrator username and initial password for NSX Manager. Make sure
        to change this initial NSX Manager password to a different value.


        :param nsx_manager_initial_password: The nsx_manager_initial_password of this Sddc.
        :type: str
        """
        self._nsx_manager_initial_password = nsx_manager_initial_password

    @property
    def vcenter_username(self):
        """
        Gets the vcenter_username of this Sddc.
        The SDDC includes an administrator username and initial password for vCenter. You can
        change this initial username to a different value in vCenter.


        :return: The vcenter_username of this Sddc.
        :rtype: str
        """
        return self._vcenter_username

    @vcenter_username.setter
    def vcenter_username(self, vcenter_username):
        """
        Sets the vcenter_username of this Sddc.
        The SDDC includes an administrator username and initial password for vCenter. You can
        change this initial username to a different value in vCenter.


        :param vcenter_username: The vcenter_username of this Sddc.
        :type: str
        """
        self._vcenter_username = vcenter_username

    @property
    def nsx_manager_username(self):
        """
        Gets the nsx_manager_username of this Sddc.
        The SDDC includes an administrator username and initial password for NSX Manager. You
        can change this initial username to a different value in NSX Manager.


        :return: The nsx_manager_username of this Sddc.
        :rtype: str
        """
        return self._nsx_manager_username

    @nsx_manager_username.setter
    def nsx_manager_username(self, nsx_manager_username):
        """
        Sets the nsx_manager_username of this Sddc.
        The SDDC includes an administrator username and initial password for NSX Manager. You
        can change this initial username to a different value in NSX Manager.


        :param nsx_manager_username: The nsx_manager_username of this Sddc.
        :type: str
        """
        self._nsx_manager_username = nsx_manager_username

    @property
    def ssh_authorized_keys(self):
        """
        **[Required]** Gets the ssh_authorized_keys of this Sddc.
        One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for
        the default user on each ESXi host. Use a newline character to separate multiple keys.
        The SSH keys must be in the format required for the `authorized_keys` file.

        This attribute is not guaranteed to reflect the public SSH keys
        currently installed on the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the public SSH keys that Oracle
        Cloud VMware Solution will install on any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you upgrade the existing ESXi hosts in the SDDC to use different
        SSH keys, you should use :func:`update_sddc` to update
        the SDDC's `sshAuthorizedKeys` with the new public keys.


        :return: The ssh_authorized_keys of this Sddc.
        :rtype: str
        """
        return self._ssh_authorized_keys

    @ssh_authorized_keys.setter
    def ssh_authorized_keys(self, ssh_authorized_keys):
        """
        Sets the ssh_authorized_keys of this Sddc.
        One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for
        the default user on each ESXi host. Use a newline character to separate multiple keys.
        The SSH keys must be in the format required for the `authorized_keys` file.

        This attribute is not guaranteed to reflect the public SSH keys
        currently installed on the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the public SSH keys that Oracle
        Cloud VMware Solution will install on any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you upgrade the existing ESXi hosts in the SDDC to use different
        SSH keys, you should use :func:`update_sddc` to update
        the SDDC's `sshAuthorizedKeys` with the new public keys.


        :param ssh_authorized_keys: The ssh_authorized_keys of this Sddc.
        :type: str
        """
        self._ssh_authorized_keys = ssh_authorized_keys

    @property
    def workload_network_cidr(self):
        """
        Gets the workload_network_cidr of this Sddc.
        The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application
        workloads.


        :return: The workload_network_cidr of this Sddc.
        :rtype: str
        """
        return self._workload_network_cidr

    @workload_network_cidr.setter
    def workload_network_cidr(self, workload_network_cidr):
        """
        Sets the workload_network_cidr of this Sddc.
        The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application
        workloads.


        :param workload_network_cidr: The workload_network_cidr of this Sddc.
        :type: str
        """
        self._workload_network_cidr = workload_network_cidr

    @property
    def nsx_overlay_segment_name(self):
        """
        Gets the nsx_overlay_segment_name of this Sddc.
        The VMware NSX overlay workload segment to host your application. Connect to workload
        portgroup in vCenter to access this overlay segment.


        :return: The nsx_overlay_segment_name of this Sddc.
        :rtype: str
        """
        return self._nsx_overlay_segment_name

    @nsx_overlay_segment_name.setter
    def nsx_overlay_segment_name(self, nsx_overlay_segment_name):
        """
        Sets the nsx_overlay_segment_name of this Sddc.
        The VMware NSX overlay workload segment to host your application. Connect to workload
        portgroup in vCenter to access this overlay segment.


        :param nsx_overlay_segment_name: The nsx_overlay_segment_name of this Sddc.
        :type: str
        """
        self._nsx_overlay_segment_name = nsx_overlay_segment_name

    @property
    def nsx_edge_uplink_ip_id(self):
        """
        Gets the nsx_edge_uplink_ip_id of this Sddc.
        The `OCID`__ of the `PrivateIp` object that is
        the virtual IP (VIP) for the NSX Edge Uplink. Use this OCID as the route target for
        route table rules when setting up connectivity between the SDDC and other networks.
        For information about `PrivateIp` objects, see the Core Services API.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_uplink_ip_id of this Sddc.
        :rtype: str
        """
        return self._nsx_edge_uplink_ip_id

    @nsx_edge_uplink_ip_id.setter
    def nsx_edge_uplink_ip_id(self, nsx_edge_uplink_ip_id):
        """
        Sets the nsx_edge_uplink_ip_id of this Sddc.
        The `OCID`__ of the `PrivateIp` object that is
        the virtual IP (VIP) for the NSX Edge Uplink. Use this OCID as the route target for
        route table rules when setting up connectivity between the SDDC and other networks.
        For information about `PrivateIp` objects, see the Core Services API.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_uplink_ip_id: The nsx_edge_uplink_ip_id of this Sddc.
        :type: str
        """
        self._nsx_edge_uplink_ip_id = nsx_edge_uplink_ip_id

    @property
    def provisioning_subnet_id(self):
        """
        **[Required]** Gets the provisioning_subnet_id of this Sddc.
        The `OCID`__ of the management subnet used
        to provision the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The provisioning_subnet_id of this Sddc.
        :rtype: str
        """
        return self._provisioning_subnet_id

    @provisioning_subnet_id.setter
    def provisioning_subnet_id(self, provisioning_subnet_id):
        """
        Sets the provisioning_subnet_id of this Sddc.
        The `OCID`__ of the management subnet used
        to provision the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param provisioning_subnet_id: The provisioning_subnet_id of this Sddc.
        :type: str
        """
        self._provisioning_subnet_id = provisioning_subnet_id

    @property
    def vsphere_vlan_id(self):
        """
        **[Required]** Gets the vsphere_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the vSphere component of the VMware environment.

        This attribute is not guaranteed to reflect the vSphere VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the vSphere VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the vSphere component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `vsphereVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vsphere_vlan_id of this Sddc.
        :rtype: str
        """
        return self._vsphere_vlan_id

    @vsphere_vlan_id.setter
    def vsphere_vlan_id(self, vsphere_vlan_id):
        """
        Sets the vsphere_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the vSphere component of the VMware environment.

        This attribute is not guaranteed to reflect the vSphere VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the vSphere VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the vSphere component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `vsphereVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vsphere_vlan_id: The vsphere_vlan_id of this Sddc.
        :type: str
        """
        self._vsphere_vlan_id = vsphere_vlan_id

    @property
    def vmotion_vlan_id(self):
        """
        **[Required]** Gets the vmotion_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the vMotion component of the VMware environment.

        This attribute is not guaranteed to reflect the vMotion VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the vMotion VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the vMotion component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `vmotionVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vmotion_vlan_id of this Sddc.
        :rtype: str
        """
        return self._vmotion_vlan_id

    @vmotion_vlan_id.setter
    def vmotion_vlan_id(self, vmotion_vlan_id):
        """
        Sets the vmotion_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the vMotion component of the VMware environment.

        This attribute is not guaranteed to reflect the vMotion VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the vMotion VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the vMotion component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `vmotionVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vmotion_vlan_id: The vmotion_vlan_id of this Sddc.
        :type: str
        """
        self._vmotion_vlan_id = vmotion_vlan_id

    @property
    def vsan_vlan_id(self):
        """
        **[Required]** Gets the vsan_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the vSAN component of the VMware environment.

        This attribute is not guaranteed to reflect the vSAN VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the vSAN VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the vSAN component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `vsanVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vsan_vlan_id of this Sddc.
        :rtype: str
        """
        return self._vsan_vlan_id

    @vsan_vlan_id.setter
    def vsan_vlan_id(self, vsan_vlan_id):
        """
        Sets the vsan_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the vSAN component of the VMware environment.

        This attribute is not guaranteed to reflect the vSAN VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the vSAN VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the vSAN component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `vsanVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vsan_vlan_id: The vsan_vlan_id of this Sddc.
        :type: str
        """
        self._vsan_vlan_id = vsan_vlan_id

    @property
    def nsx_v_tep_vlan_id(self):
        """
        **[Required]** Gets the nsx_v_tep_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX VTEP component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX VTEP VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the NSX VTEP VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the NSX VTEP component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `nsxVTepVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_v_tep_vlan_id of this Sddc.
        :rtype: str
        """
        return self._nsx_v_tep_vlan_id

    @nsx_v_tep_vlan_id.setter
    def nsx_v_tep_vlan_id(self, nsx_v_tep_vlan_id):
        """
        Sets the nsx_v_tep_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX VTEP component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX VTEP VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the NSX VTEP VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the NSX VTEP component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `nsxVTepVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_v_tep_vlan_id: The nsx_v_tep_vlan_id of this Sddc.
        :type: str
        """
        self._nsx_v_tep_vlan_id = nsx_v_tep_vlan_id

    @property
    def nsx_edge_v_tep_vlan_id(self):
        """
        **[Required]** Gets the nsx_edge_v_tep_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX Edge VTEP component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX Edge VTEP VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the NSX Edge VTEP VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the NSX Edge VTEP component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `nsxEdgeVTepVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_v_tep_vlan_id of this Sddc.
        :rtype: str
        """
        return self._nsx_edge_v_tep_vlan_id

    @nsx_edge_v_tep_vlan_id.setter
    def nsx_edge_v_tep_vlan_id(self, nsx_edge_v_tep_vlan_id):
        """
        Sets the nsx_edge_v_tep_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX Edge VTEP component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX Edge VTEP VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the NSX Edge VTEP VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the NSX Edge VTEP component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `nsxEdgeVTepVlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_v_tep_vlan_id: The nsx_edge_v_tep_vlan_id of this Sddc.
        :type: str
        """
        self._nsx_edge_v_tep_vlan_id = nsx_edge_v_tep_vlan_id

    @property
    def nsx_edge_uplink1_vlan_id(self):
        """
        **[Required]** Gets the nsx_edge_uplink1_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX Edge Uplink 1 component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX Edge Uplink 1 VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the NSX Edge Uplink 1 VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the NSX Edge Uplink 1 component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `nsxEdgeUplink1VlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_uplink1_vlan_id of this Sddc.
        :rtype: str
        """
        return self._nsx_edge_uplink1_vlan_id

    @nsx_edge_uplink1_vlan_id.setter
    def nsx_edge_uplink1_vlan_id(self, nsx_edge_uplink1_vlan_id):
        """
        Sets the nsx_edge_uplink1_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX Edge Uplink 1 component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX Edge Uplink 1 VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the NSX Edge Uplink 1 VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the NSX Edge Uplink 1 component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `nsxEdgeUplink1VlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_uplink1_vlan_id: The nsx_edge_uplink1_vlan_id of this Sddc.
        :type: str
        """
        self._nsx_edge_uplink1_vlan_id = nsx_edge_uplink1_vlan_id

    @property
    def nsx_edge_uplink2_vlan_id(self):
        """
        **[Required]** Gets the nsx_edge_uplink2_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX Edge Uplink 2 component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX Edge Uplink 2 VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the NSX Edge Uplink 2 VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the NSX Edge Uplink 2 component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `nsxEdgeUplink2VlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_uplink2_vlan_id of this Sddc.
        :rtype: str
        """
        return self._nsx_edge_uplink2_vlan_id

    @nsx_edge_uplink2_vlan_id.setter
    def nsx_edge_uplink2_vlan_id(self, nsx_edge_uplink2_vlan_id):
        """
        Sets the nsx_edge_uplink2_vlan_id of this Sddc.
        The `OCID`__ of the VLAN used by the SDDC
        for the NSX Edge Uplink 2 component of the VMware environment.

        This attribute is not guaranteed to reflect the NSX Edge Uplink 2 VLAN
        currently used by the ESXi hosts in the SDDC. The purpose
        of this attribute is to show the NSX Edge Uplink 2 VLAN that the Oracle
        Cloud VMware Solution will use for any new ESXi hosts that you *add to this
        SDDC in the future* with :func:`create_esxi_host`.

        Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
        for the NSX Edge Uplink 2 component of the VMware environment, you
        should use :func:`update_sddc` to update the SDDC's
        `nsxEdgeUplink2VlanId` with that new VLAN's OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_uplink2_vlan_id: The nsx_edge_uplink2_vlan_id of this Sddc.
        :type: str
        """
        self._nsx_edge_uplink2_vlan_id = nsx_edge_uplink2_vlan_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Sddc.
        The date and time the SDDC was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Sddc.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Sddc.
        The date and time the SDDC was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Sddc.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Sddc.
        The date and time the SDDC was updated, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Sddc.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Sddc.
        The date and time the SDDC was updated, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Sddc.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Sddc.
        The current state of the SDDC.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Sddc.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Sddc.
        The current state of the SDDC.


        :param lifecycle_state: The lifecycle_state of this Sddc.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this Sddc.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Sddc.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Sddc.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Sddc.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this Sddc.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Sddc.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Sddc.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Sddc.
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
