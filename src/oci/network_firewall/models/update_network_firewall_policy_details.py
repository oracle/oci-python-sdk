# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNetworkFirewallPolicyDetails(object):
    """
    The request details to be updated in the firewall policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNetworkFirewallPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateNetworkFirewallPolicyDetails.
        :type display_name: str

        :param mapped_secrets:
            The value to assign to the mapped_secrets property of this UpdateNetworkFirewallPolicyDetails.
        :type mapped_secrets: dict(str, MappedSecret)

        :param application_lists:
            The value to assign to the application_lists property of this UpdateNetworkFirewallPolicyDetails.
        :type application_lists: dict(str, list[Application])

        :param url_lists:
            The value to assign to the url_lists property of this UpdateNetworkFirewallPolicyDetails.
        :type url_lists: dict(str, list[UrlPattern])

        :param ip_address_lists:
            The value to assign to the ip_address_lists property of this UpdateNetworkFirewallPolicyDetails.
        :type ip_address_lists: dict(str, list[str])

        :param security_rules:
            The value to assign to the security_rules property of this UpdateNetworkFirewallPolicyDetails.
        :type security_rules: list[oci.network_firewall.models.SecurityRule]

        :param decryption_rules:
            The value to assign to the decryption_rules property of this UpdateNetworkFirewallPolicyDetails.
        :type decryption_rules: list[oci.network_firewall.models.DecryptionRule]

        :param decryption_profiles:
            The value to assign to the decryption_profiles property of this UpdateNetworkFirewallPolicyDetails.
        :type decryption_profiles: dict(str, DecryptionProfile)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateNetworkFirewallPolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateNetworkFirewallPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'mapped_secrets': 'dict(str, MappedSecret)',
            'application_lists': 'dict(str, list[Application])',
            'url_lists': 'dict(str, list[UrlPattern])',
            'ip_address_lists': 'dict(str, list[str])',
            'security_rules': 'list[SecurityRule]',
            'decryption_rules': 'list[DecryptionRule]',
            'decryption_profiles': 'dict(str, DecryptionProfile)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'mapped_secrets': 'mappedSecrets',
            'application_lists': 'applicationLists',
            'url_lists': 'urlLists',
            'ip_address_lists': 'ipAddressLists',
            'security_rules': 'securityRules',
            'decryption_rules': 'decryptionRules',
            'decryption_profiles': 'decryptionProfiles',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._mapped_secrets = None
        self._application_lists = None
        self._url_lists = None
        self._ip_address_lists = None
        self._security_rules = None
        self._decryption_rules = None
        self._decryption_profiles = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateNetworkFirewallPolicyDetails.
        A user-friendly name for the firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this UpdateNetworkFirewallPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateNetworkFirewallPolicyDetails.
        A user-friendly name for the firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateNetworkFirewallPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def mapped_secrets(self):
        """
        Gets the mapped_secrets of this UpdateNetworkFirewallPolicyDetails.
        Map defining secrets of the policy.
        The value of an entry is a \"mapped secret\" consisting of a purpose and source.
        The associated key is the identifier by which the mapped secret is referenced.


        :return: The mapped_secrets of this UpdateNetworkFirewallPolicyDetails.
        :rtype: dict(str, MappedSecret)
        """
        return self._mapped_secrets

    @mapped_secrets.setter
    def mapped_secrets(self, mapped_secrets):
        """
        Sets the mapped_secrets of this UpdateNetworkFirewallPolicyDetails.
        Map defining secrets of the policy.
        The value of an entry is a \"mapped secret\" consisting of a purpose and source.
        The associated key is the identifier by which the mapped secret is referenced.


        :param mapped_secrets: The mapped_secrets of this UpdateNetworkFirewallPolicyDetails.
        :type: dict(str, MappedSecret)
        """
        self._mapped_secrets = mapped_secrets

    @property
    def application_lists(self):
        """
        Gets the application_lists of this UpdateNetworkFirewallPolicyDetails.
        Map defining application lists of the policy.
        The value of an entry is a list of \"applications\", each consisting of a protocol identifier (such as TCP, UDP, or ICMP) and protocol-specific parameters (such as a port range).
        The associated key is the identifier by which the application list is referenced.


        :return: The application_lists of this UpdateNetworkFirewallPolicyDetails.
        :rtype: dict(str, list[Application])
        """
        return self._application_lists

    @application_lists.setter
    def application_lists(self, application_lists):
        """
        Sets the application_lists of this UpdateNetworkFirewallPolicyDetails.
        Map defining application lists of the policy.
        The value of an entry is a list of \"applications\", each consisting of a protocol identifier (such as TCP, UDP, or ICMP) and protocol-specific parameters (such as a port range).
        The associated key is the identifier by which the application list is referenced.


        :param application_lists: The application_lists of this UpdateNetworkFirewallPolicyDetails.
        :type: dict(str, list[Application])
        """
        self._application_lists = application_lists

    @property
    def url_lists(self):
        """
        Gets the url_lists of this UpdateNetworkFirewallPolicyDetails.
        Map defining URL pattern lists of the policy.
        The value of an entry is a list of URL patterns.
        The associated key is the identifier by which the URL pattern list is referenced.


        :return: The url_lists of this UpdateNetworkFirewallPolicyDetails.
        :rtype: dict(str, list[UrlPattern])
        """
        return self._url_lists

    @url_lists.setter
    def url_lists(self, url_lists):
        """
        Sets the url_lists of this UpdateNetworkFirewallPolicyDetails.
        Map defining URL pattern lists of the policy.
        The value of an entry is a list of URL patterns.
        The associated key is the identifier by which the URL pattern list is referenced.


        :param url_lists: The url_lists of this UpdateNetworkFirewallPolicyDetails.
        :type: dict(str, list[UrlPattern])
        """
        self._url_lists = url_lists

    @property
    def ip_address_lists(self):
        """
        Gets the ip_address_lists of this UpdateNetworkFirewallPolicyDetails.
        Map defining IP address lists of the policy.
        The value of an entry is a list of IP addresses or prefixes in CIDR notation.
        The associated key is the identifier by which the IP address list is referenced.


        :return: The ip_address_lists of this UpdateNetworkFirewallPolicyDetails.
        :rtype: dict(str, list[str])
        """
        return self._ip_address_lists

    @ip_address_lists.setter
    def ip_address_lists(self, ip_address_lists):
        """
        Sets the ip_address_lists of this UpdateNetworkFirewallPolicyDetails.
        Map defining IP address lists of the policy.
        The value of an entry is a list of IP addresses or prefixes in CIDR notation.
        The associated key is the identifier by which the IP address list is referenced.


        :param ip_address_lists: The ip_address_lists of this UpdateNetworkFirewallPolicyDetails.
        :type: dict(str, list[str])
        """
        self._ip_address_lists = ip_address_lists

    @property
    def security_rules(self):
        """
        Gets the security_rules of this UpdateNetworkFirewallPolicyDetails.
        List of Security Rules defining the behavior of the policy.
        The first rule with a matching condition determines the action taken upon network traffic.


        :return: The security_rules of this UpdateNetworkFirewallPolicyDetails.
        :rtype: list[oci.network_firewall.models.SecurityRule]
        """
        return self._security_rules

    @security_rules.setter
    def security_rules(self, security_rules):
        """
        Sets the security_rules of this UpdateNetworkFirewallPolicyDetails.
        List of Security Rules defining the behavior of the policy.
        The first rule with a matching condition determines the action taken upon network traffic.


        :param security_rules: The security_rules of this UpdateNetworkFirewallPolicyDetails.
        :type: list[oci.network_firewall.models.SecurityRule]
        """
        self._security_rules = security_rules

    @property
    def decryption_rules(self):
        """
        Gets the decryption_rules of this UpdateNetworkFirewallPolicyDetails.
        List of Decryption Rules defining the behavior of the policy.
        The first rule with a matching condition determines the action taken upon network traffic.


        :return: The decryption_rules of this UpdateNetworkFirewallPolicyDetails.
        :rtype: list[oci.network_firewall.models.DecryptionRule]
        """
        return self._decryption_rules

    @decryption_rules.setter
    def decryption_rules(self, decryption_rules):
        """
        Sets the decryption_rules of this UpdateNetworkFirewallPolicyDetails.
        List of Decryption Rules defining the behavior of the policy.
        The first rule with a matching condition determines the action taken upon network traffic.


        :param decryption_rules: The decryption_rules of this UpdateNetworkFirewallPolicyDetails.
        :type: list[oci.network_firewall.models.DecryptionRule]
        """
        self._decryption_rules = decryption_rules

    @property
    def decryption_profiles(self):
        """
        Gets the decryption_profiles of this UpdateNetworkFirewallPolicyDetails.
        Map defining decryption profiles of the policy.
        The value of an entry is a decryption profile.
        The associated key is the identifier by which the decryption profile is referenced.


        :return: The decryption_profiles of this UpdateNetworkFirewallPolicyDetails.
        :rtype: dict(str, DecryptionProfile)
        """
        return self._decryption_profiles

    @decryption_profiles.setter
    def decryption_profiles(self, decryption_profiles):
        """
        Sets the decryption_profiles of this UpdateNetworkFirewallPolicyDetails.
        Map defining decryption profiles of the policy.
        The value of an entry is a decryption profile.
        The associated key is the identifier by which the decryption profile is referenced.


        :param decryption_profiles: The decryption_profiles of this UpdateNetworkFirewallPolicyDetails.
        :type: dict(str, DecryptionProfile)
        """
        self._decryption_profiles = decryption_profiles

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateNetworkFirewallPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateNetworkFirewallPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateNetworkFirewallPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateNetworkFirewallPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateNetworkFirewallPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateNetworkFirewallPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateNetworkFirewallPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateNetworkFirewallPolicyDetails.
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
