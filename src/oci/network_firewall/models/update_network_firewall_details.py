# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNetworkFirewallDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNetworkFirewallDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateNetworkFirewallDetails.
        :type display_name: str

        :param network_firewall_policy_id:
            The value to assign to the network_firewall_policy_id property of this UpdateNetworkFirewallDetails.
        :type network_firewall_policy_id: str

        :param network_security_group_ids:
            The value to assign to the network_security_group_ids property of this UpdateNetworkFirewallDetails.
        :type network_security_group_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateNetworkFirewallDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateNetworkFirewallDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'network_firewall_policy_id': 'str',
            'network_security_group_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'network_firewall_policy_id': 'networkFirewallPolicyId',
            'network_security_group_ids': 'networkSecurityGroupIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._network_firewall_policy_id = None
        self._network_security_group_ids = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateNetworkFirewallDetails.
        A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this UpdateNetworkFirewallDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateNetworkFirewallDetails.
        A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateNetworkFirewallDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def network_firewall_policy_id(self):
        """
        Gets the network_firewall_policy_id of this UpdateNetworkFirewallDetails.
        The `OCID`__ of the Network Firewall Policy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The network_firewall_policy_id of this UpdateNetworkFirewallDetails.
        :rtype: str
        """
        return self._network_firewall_policy_id

    @network_firewall_policy_id.setter
    def network_firewall_policy_id(self, network_firewall_policy_id):
        """
        Sets the network_firewall_policy_id of this UpdateNetworkFirewallDetails.
        The `OCID`__ of the Network Firewall Policy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param network_firewall_policy_id: The network_firewall_policy_id of this UpdateNetworkFirewallDetails.
        :type: str
        """
        self._network_firewall_policy_id = network_firewall_policy_id

    @property
    def network_security_group_ids(self):
        """
        Gets the network_security_group_ids of this UpdateNetworkFirewallDetails.
        An array of network security groups `OCID`__ associated with the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The network_security_group_ids of this UpdateNetworkFirewallDetails.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this UpdateNetworkFirewallDetails.
        An array of network security groups `OCID`__ associated with the Network Firewall.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param network_security_group_ids: The network_security_group_ids of this UpdateNetworkFirewallDetails.
        :type: list[str]
        """
        self._network_security_group_ids = network_security_group_ids

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateNetworkFirewallDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateNetworkFirewallDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateNetworkFirewallDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateNetworkFirewallDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateNetworkFirewallDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateNetworkFirewallDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateNetworkFirewallDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateNetworkFirewallDetails.
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
