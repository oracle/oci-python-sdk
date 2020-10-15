# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSddcDetails(object):
    """
    The SDDC information to be updated.

    **Important:** Only the `displayName`, `freeFormTags`, and `definedTags` attributes
    affect the existing SDDC. Changing the other attributes affects the `Sddc` object, but not
    the VMware environment currently running on that SDDC. Those other attributes are used
    by the Oracle Cloud VMware Solution *only* for new ESXi hosts that you add to this
    SDDC in the future with :func:`create_esxi_host`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSddcDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateSddcDetails.
        :type display_name: str

        :param vmware_software_version:
            The value to assign to the vmware_software_version property of this UpdateSddcDetails.
        :type vmware_software_version: str

        :param ssh_authorized_keys:
            The value to assign to the ssh_authorized_keys property of this UpdateSddcDetails.
        :type ssh_authorized_keys: str

        :param vsphere_vlan_id:
            The value to assign to the vsphere_vlan_id property of this UpdateSddcDetails.
        :type vsphere_vlan_id: str

        :param vmotion_vlan_id:
            The value to assign to the vmotion_vlan_id property of this UpdateSddcDetails.
        :type vmotion_vlan_id: str

        :param vsan_vlan_id:
            The value to assign to the vsan_vlan_id property of this UpdateSddcDetails.
        :type vsan_vlan_id: str

        :param nsx_v_tep_vlan_id:
            The value to assign to the nsx_v_tep_vlan_id property of this UpdateSddcDetails.
        :type nsx_v_tep_vlan_id: str

        :param nsx_edge_v_tep_vlan_id:
            The value to assign to the nsx_edge_v_tep_vlan_id property of this UpdateSddcDetails.
        :type nsx_edge_v_tep_vlan_id: str

        :param nsx_edge_uplink1_vlan_id:
            The value to assign to the nsx_edge_uplink1_vlan_id property of this UpdateSddcDetails.
        :type nsx_edge_uplink1_vlan_id: str

        :param nsx_edge_uplink2_vlan_id:
            The value to assign to the nsx_edge_uplink2_vlan_id property of this UpdateSddcDetails.
        :type nsx_edge_uplink2_vlan_id: str

        :param hcx_vlan_id:
            The value to assign to the hcx_vlan_id property of this UpdateSddcDetails.
        :type hcx_vlan_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSddcDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSddcDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'vmware_software_version': 'str',
            'ssh_authorized_keys': 'str',
            'vsphere_vlan_id': 'str',
            'vmotion_vlan_id': 'str',
            'vsan_vlan_id': 'str',
            'nsx_v_tep_vlan_id': 'str',
            'nsx_edge_v_tep_vlan_id': 'str',
            'nsx_edge_uplink1_vlan_id': 'str',
            'nsx_edge_uplink2_vlan_id': 'str',
            'hcx_vlan_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'vmware_software_version': 'vmwareSoftwareVersion',
            'ssh_authorized_keys': 'sshAuthorizedKeys',
            'vsphere_vlan_id': 'vsphereVlanId',
            'vmotion_vlan_id': 'vmotionVlanId',
            'vsan_vlan_id': 'vsanVlanId',
            'nsx_v_tep_vlan_id': 'nsxVTepVlanId',
            'nsx_edge_v_tep_vlan_id': 'nsxEdgeVTepVlanId',
            'nsx_edge_uplink1_vlan_id': 'nsxEdgeUplink1VlanId',
            'nsx_edge_uplink2_vlan_id': 'nsxEdgeUplink2VlanId',
            'hcx_vlan_id': 'hcxVlanId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._vmware_software_version = None
        self._ssh_authorized_keys = None
        self._vsphere_vlan_id = None
        self._vmotion_vlan_id = None
        self._vsan_vlan_id = None
        self._nsx_v_tep_vlan_id = None
        self._nsx_edge_v_tep_vlan_id = None
        self._nsx_edge_uplink1_vlan_id = None
        self._nsx_edge_uplink2_vlan_id = None
        self._hcx_vlan_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateSddcDetails.
        The `OCID`__ of the SDDC.
        SDDC name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The display_name of this UpdateSddcDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateSddcDetails.
        The `OCID`__ of the SDDC.
        SDDC name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param display_name: The display_name of this UpdateSddcDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def vmware_software_version(self):
        """
        Gets the vmware_software_version of this UpdateSddcDetails.
        The version of bundled VMware software that the Oracle Cloud VMware Solution will
        install on any new ESXi hosts that you add to this SDDC in the future.

        For the list of versions supported by the Oracle Cloud VMware Solution, see
        :func:`
        _list_supported_vmware_software_versions`).


        :return: The vmware_software_version of this UpdateSddcDetails.
        :rtype: str
        """
        return self._vmware_software_version

    @vmware_software_version.setter
    def vmware_software_version(self, vmware_software_version):
        """
        Sets the vmware_software_version of this UpdateSddcDetails.
        The version of bundled VMware software that the Oracle Cloud VMware Solution will
        install on any new ESXi hosts that you add to this SDDC in the future.

        For the list of versions supported by the Oracle Cloud VMware Solution, see
        :func:`
        _list_supported_vmware_software_versions`).


        :param vmware_software_version: The vmware_software_version of this UpdateSddcDetails.
        :type: str
        """
        self._vmware_software_version = vmware_software_version

    @property
    def ssh_authorized_keys(self):
        """
        Gets the ssh_authorized_keys of this UpdateSddcDetails.
        One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for
        the default user on each ESXi host, only when adding new ESXi hosts to this SDDC.
        Use a newline character to separate multiple keys.
        The SSH keys must be in the format required for the `authorized_keys` file.


        :return: The ssh_authorized_keys of this UpdateSddcDetails.
        :rtype: str
        """
        return self._ssh_authorized_keys

    @ssh_authorized_keys.setter
    def ssh_authorized_keys(self, ssh_authorized_keys):
        """
        Sets the ssh_authorized_keys of this UpdateSddcDetails.
        One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for
        the default user on each ESXi host, only when adding new ESXi hosts to this SDDC.
        Use a newline character to separate multiple keys.
        The SSH keys must be in the format required for the `authorized_keys` file.


        :param ssh_authorized_keys: The ssh_authorized_keys of this UpdateSddcDetails.
        :type: str
        """
        self._ssh_authorized_keys = ssh_authorized_keys

    @property
    def vsphere_vlan_id(self):
        """
        Gets the vsphere_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the vSphere component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vsphere_vlan_id of this UpdateSddcDetails.
        :rtype: str
        """
        return self._vsphere_vlan_id

    @vsphere_vlan_id.setter
    def vsphere_vlan_id(self, vsphere_vlan_id):
        """
        Sets the vsphere_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the vSphere component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vsphere_vlan_id: The vsphere_vlan_id of this UpdateSddcDetails.
        :type: str
        """
        self._vsphere_vlan_id = vsphere_vlan_id

    @property
    def vmotion_vlan_id(self):
        """
        Gets the vmotion_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the vMotion component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vmotion_vlan_id of this UpdateSddcDetails.
        :rtype: str
        """
        return self._vmotion_vlan_id

    @vmotion_vlan_id.setter
    def vmotion_vlan_id(self, vmotion_vlan_id):
        """
        Sets the vmotion_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the vMotion component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vmotion_vlan_id: The vmotion_vlan_id of this UpdateSddcDetails.
        :type: str
        """
        self._vmotion_vlan_id = vmotion_vlan_id

    @property
    def vsan_vlan_id(self):
        """
        Gets the vsan_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the vSAN component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vsan_vlan_id of this UpdateSddcDetails.
        :rtype: str
        """
        return self._vsan_vlan_id

    @vsan_vlan_id.setter
    def vsan_vlan_id(self, vsan_vlan_id):
        """
        Sets the vsan_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the vSAN component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vsan_vlan_id: The vsan_vlan_id of this UpdateSddcDetails.
        :type: str
        """
        self._vsan_vlan_id = vsan_vlan_id

    @property
    def nsx_v_tep_vlan_id(self):
        """
        Gets the nsx_v_tep_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the NSX VTEP component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_v_tep_vlan_id of this UpdateSddcDetails.
        :rtype: str
        """
        return self._nsx_v_tep_vlan_id

    @nsx_v_tep_vlan_id.setter
    def nsx_v_tep_vlan_id(self, nsx_v_tep_vlan_id):
        """
        Sets the nsx_v_tep_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the NSX VTEP component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_v_tep_vlan_id: The nsx_v_tep_vlan_id of this UpdateSddcDetails.
        :type: str
        """
        self._nsx_v_tep_vlan_id = nsx_v_tep_vlan_id

    @property
    def nsx_edge_v_tep_vlan_id(self):
        """
        Gets the nsx_edge_v_tep_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the NSX Edge VTEP component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_v_tep_vlan_id of this UpdateSddcDetails.
        :rtype: str
        """
        return self._nsx_edge_v_tep_vlan_id

    @nsx_edge_v_tep_vlan_id.setter
    def nsx_edge_v_tep_vlan_id(self, nsx_edge_v_tep_vlan_id):
        """
        Sets the nsx_edge_v_tep_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the NSX Edge VTEP component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_v_tep_vlan_id: The nsx_edge_v_tep_vlan_id of this UpdateSddcDetails.
        :type: str
        """
        self._nsx_edge_v_tep_vlan_id = nsx_edge_v_tep_vlan_id

    @property
    def nsx_edge_uplink1_vlan_id(self):
        """
        Gets the nsx_edge_uplink1_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the NSX Edge Uplink 1 component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_uplink1_vlan_id of this UpdateSddcDetails.
        :rtype: str
        """
        return self._nsx_edge_uplink1_vlan_id

    @nsx_edge_uplink1_vlan_id.setter
    def nsx_edge_uplink1_vlan_id(self, nsx_edge_uplink1_vlan_id):
        """
        Sets the nsx_edge_uplink1_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the NSX Edge Uplink 1 component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_uplink1_vlan_id: The nsx_edge_uplink1_vlan_id of this UpdateSddcDetails.
        :type: str
        """
        self._nsx_edge_uplink1_vlan_id = nsx_edge_uplink1_vlan_id

    @property
    def nsx_edge_uplink2_vlan_id(self):
        """
        Gets the nsx_edge_uplink2_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the NSX Edge Uplink 2 component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsx_edge_uplink2_vlan_id of this UpdateSddcDetails.
        :rtype: str
        """
        return self._nsx_edge_uplink2_vlan_id

    @nsx_edge_uplink2_vlan_id.setter
    def nsx_edge_uplink2_vlan_id(self, nsx_edge_uplink2_vlan_id):
        """
        Sets the nsx_edge_uplink2_vlan_id of this UpdateSddcDetails.
        The `OCID`__ of the VLAN to use for
        the NSX Edge Uplink 2 component of the VMware environment when adding new ESXi hosts to the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsx_edge_uplink2_vlan_id: The nsx_edge_uplink2_vlan_id of this UpdateSddcDetails.
        :type: str
        """
        self._nsx_edge_uplink2_vlan_id = nsx_edge_uplink2_vlan_id

    @property
    def hcx_vlan_id(self):
        """
        Gets the hcx_vlan_id of this UpdateSddcDetails.
        This id is editable only when hcxEnabled is true


        :return: The hcx_vlan_id of this UpdateSddcDetails.
        :rtype: str
        """
        return self._hcx_vlan_id

    @hcx_vlan_id.setter
    def hcx_vlan_id(self, hcx_vlan_id):
        """
        Sets the hcx_vlan_id of this UpdateSddcDetails.
        This id is editable only when hcxEnabled is true


        :param hcx_vlan_id: The hcx_vlan_id of this UpdateSddcDetails.
        :type: str
        """
        self._hcx_vlan_id = hcx_vlan_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSddcDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateSddcDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSddcDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateSddcDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSddcDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateSddcDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSddcDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateSddcDetails.
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
