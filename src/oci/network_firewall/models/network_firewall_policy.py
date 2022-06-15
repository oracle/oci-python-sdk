# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkFirewallPolicy(object):
    """
    Description of NetworkFirewall Policy.
    """

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewallPolicy.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewallPolicy.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewallPolicy.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewallPolicy.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewallPolicy.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a NetworkFirewallPolicy.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkFirewallPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this NetworkFirewallPolicy.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this NetworkFirewallPolicy.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this NetworkFirewallPolicy.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this NetworkFirewallPolicy.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this NetworkFirewallPolicy.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this NetworkFirewallPolicy.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this NetworkFirewallPolicy.
        :type lifecycle_details: str

        :param mapped_secrets:
            The value to assign to the mapped_secrets property of this NetworkFirewallPolicy.
        :type mapped_secrets: dict(str, MappedSecret)

        :param application_lists:
            The value to assign to the application_lists property of this NetworkFirewallPolicy.
        :type application_lists: dict(str, list[Application])

        :param url_lists:
            The value to assign to the url_lists property of this NetworkFirewallPolicy.
        :type url_lists: dict(str, list[UrlPattern])

        :param ip_address_lists:
            The value to assign to the ip_address_lists property of this NetworkFirewallPolicy.
        :type ip_address_lists: dict(str, list[str])

        :param security_rules:
            The value to assign to the security_rules property of this NetworkFirewallPolicy.
        :type security_rules: list[oci.network_firewall.models.SecurityRule]

        :param decryption_rules:
            The value to assign to the decryption_rules property of this NetworkFirewallPolicy.
        :type decryption_rules: list[oci.network_firewall.models.DecryptionRule]

        :param decryption_profiles:
            The value to assign to the decryption_profiles property of this NetworkFirewallPolicy.
        :type decryption_profiles: dict(str, DecryptionProfile)

        :param is_firewall_attached:
            The value to assign to the is_firewall_attached property of this NetworkFirewallPolicy.
        :type is_firewall_attached: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this NetworkFirewallPolicy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this NetworkFirewallPolicy.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this NetworkFirewallPolicy.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'mapped_secrets': 'dict(str, MappedSecret)',
            'application_lists': 'dict(str, list[Application])',
            'url_lists': 'dict(str, list[UrlPattern])',
            'ip_address_lists': 'dict(str, list[str])',
            'security_rules': 'list[SecurityRule]',
            'decryption_rules': 'list[DecryptionRule]',
            'decryption_profiles': 'dict(str, DecryptionProfile)',
            'is_firewall_attached': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'mapped_secrets': 'mappedSecrets',
            'application_lists': 'applicationLists',
            'url_lists': 'urlLists',
            'ip_address_lists': 'ipAddressLists',
            'security_rules': 'securityRules',
            'decryption_rules': 'decryptionRules',
            'decryption_profiles': 'decryptionProfiles',
            'is_firewall_attached': 'isFirewallAttached',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._mapped_secrets = None
        self._application_lists = None
        self._url_lists = None
        self._ip_address_lists = None
        self._security_rules = None
        self._decryption_rules = None
        self._decryption_profiles = None
        self._is_firewall_attached = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this NetworkFirewallPolicy.
        The `OCID`__ of the resource - Network Firewall Policy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this NetworkFirewallPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NetworkFirewallPolicy.
        The `OCID`__ of the resource - Network Firewall Policy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this NetworkFirewallPolicy.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this NetworkFirewallPolicy.
        The `OCID`__ of the compartment containing the NetworkFirewall Policy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this NetworkFirewallPolicy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this NetworkFirewallPolicy.
        The `OCID`__ of the compartment containing the NetworkFirewall Policy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this NetworkFirewallPolicy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this NetworkFirewallPolicy.
        A user-friendly optional name for the firewall policy. Avoid entering confidential information.


        :return: The display_name of this NetworkFirewallPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this NetworkFirewallPolicy.
        A user-friendly optional name for the firewall policy. Avoid entering confidential information.


        :param display_name: The display_name of this NetworkFirewallPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this NetworkFirewallPolicy.
        The time instant at which the Network Firewall Policy was created in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this NetworkFirewallPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this NetworkFirewallPolicy.
        The time instant at which the Network Firewall Policy was created in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this NetworkFirewallPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this NetworkFirewallPolicy.
        The time instant at which the Network Firewall Policy was updated in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this NetworkFirewallPolicy.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this NetworkFirewallPolicy.
        The time instant at which the Network Firewall Policy was updated in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this NetworkFirewallPolicy.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this NetworkFirewallPolicy.
        The current state of the Network Firewall Policy.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this NetworkFirewallPolicy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this NetworkFirewallPolicy.
        The current state of the Network Firewall Policy.


        :param lifecycle_state: The lifecycle_state of this NetworkFirewallPolicy.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this NetworkFirewallPolicy.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this NetworkFirewallPolicy.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this NetworkFirewallPolicy.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this NetworkFirewallPolicy.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def mapped_secrets(self):
        """
        Gets the mapped_secrets of this NetworkFirewallPolicy.
        Map defining secrets of the policy.
        The value of an entry is a \"mapped secret\" consisting of a purpose and source.
        The associated key is the identifier by which the mapped secret is referenced.


        :return: The mapped_secrets of this NetworkFirewallPolicy.
        :rtype: dict(str, MappedSecret)
        """
        return self._mapped_secrets

    @mapped_secrets.setter
    def mapped_secrets(self, mapped_secrets):
        """
        Sets the mapped_secrets of this NetworkFirewallPolicy.
        Map defining secrets of the policy.
        The value of an entry is a \"mapped secret\" consisting of a purpose and source.
        The associated key is the identifier by which the mapped secret is referenced.


        :param mapped_secrets: The mapped_secrets of this NetworkFirewallPolicy.
        :type: dict(str, MappedSecret)
        """
        self._mapped_secrets = mapped_secrets

    @property
    def application_lists(self):
        """
        Gets the application_lists of this NetworkFirewallPolicy.
        Map defining application lists of the policy.
        The value of an entry is a list of \"applications\", each consisting of a protocol identifier (such as TCP, UDP, or ICMP) and protocol-specific parameters (such as a port range).
        The associated key is the identifier by which the application list is referenced.


        :return: The application_lists of this NetworkFirewallPolicy.
        :rtype: dict(str, list[Application])
        """
        return self._application_lists

    @application_lists.setter
    def application_lists(self, application_lists):
        """
        Sets the application_lists of this NetworkFirewallPolicy.
        Map defining application lists of the policy.
        The value of an entry is a list of \"applications\", each consisting of a protocol identifier (such as TCP, UDP, or ICMP) and protocol-specific parameters (such as a port range).
        The associated key is the identifier by which the application list is referenced.


        :param application_lists: The application_lists of this NetworkFirewallPolicy.
        :type: dict(str, list[Application])
        """
        self._application_lists = application_lists

    @property
    def url_lists(self):
        """
        Gets the url_lists of this NetworkFirewallPolicy.
        Map defining URL pattern lists of the policy.
        The value of an entry is a list of URL patterns.
        The associated key is the identifier by which the URL pattern list is referenced.


        :return: The url_lists of this NetworkFirewallPolicy.
        :rtype: dict(str, list[UrlPattern])
        """
        return self._url_lists

    @url_lists.setter
    def url_lists(self, url_lists):
        """
        Sets the url_lists of this NetworkFirewallPolicy.
        Map defining URL pattern lists of the policy.
        The value of an entry is a list of URL patterns.
        The associated key is the identifier by which the URL pattern list is referenced.


        :param url_lists: The url_lists of this NetworkFirewallPolicy.
        :type: dict(str, list[UrlPattern])
        """
        self._url_lists = url_lists

    @property
    def ip_address_lists(self):
        """
        Gets the ip_address_lists of this NetworkFirewallPolicy.
        Map defining IP address lists of the policy.
        The value of an entry is a list of IP addresses or prefixes in CIDR notation.
        The associated key is the identifier by which the IP address list is referenced.


        :return: The ip_address_lists of this NetworkFirewallPolicy.
        :rtype: dict(str, list[str])
        """
        return self._ip_address_lists

    @ip_address_lists.setter
    def ip_address_lists(self, ip_address_lists):
        """
        Sets the ip_address_lists of this NetworkFirewallPolicy.
        Map defining IP address lists of the policy.
        The value of an entry is a list of IP addresses or prefixes in CIDR notation.
        The associated key is the identifier by which the IP address list is referenced.


        :param ip_address_lists: The ip_address_lists of this NetworkFirewallPolicy.
        :type: dict(str, list[str])
        """
        self._ip_address_lists = ip_address_lists

    @property
    def security_rules(self):
        """
        Gets the security_rules of this NetworkFirewallPolicy.
        List of Security Rules defining the behavior of the policy.
        The first rule with a matching condition determines the action taken upon network traffic.


        :return: The security_rules of this NetworkFirewallPolicy.
        :rtype: list[oci.network_firewall.models.SecurityRule]
        """
        return self._security_rules

    @security_rules.setter
    def security_rules(self, security_rules):
        """
        Sets the security_rules of this NetworkFirewallPolicy.
        List of Security Rules defining the behavior of the policy.
        The first rule with a matching condition determines the action taken upon network traffic.


        :param security_rules: The security_rules of this NetworkFirewallPolicy.
        :type: list[oci.network_firewall.models.SecurityRule]
        """
        self._security_rules = security_rules

    @property
    def decryption_rules(self):
        """
        Gets the decryption_rules of this NetworkFirewallPolicy.
        List of Decryption Rules defining the behavior of the policy.
        The first rule with a matching condition determines the action taken upon network traffic.


        :return: The decryption_rules of this NetworkFirewallPolicy.
        :rtype: list[oci.network_firewall.models.DecryptionRule]
        """
        return self._decryption_rules

    @decryption_rules.setter
    def decryption_rules(self, decryption_rules):
        """
        Sets the decryption_rules of this NetworkFirewallPolicy.
        List of Decryption Rules defining the behavior of the policy.
        The first rule with a matching condition determines the action taken upon network traffic.


        :param decryption_rules: The decryption_rules of this NetworkFirewallPolicy.
        :type: list[oci.network_firewall.models.DecryptionRule]
        """
        self._decryption_rules = decryption_rules

    @property
    def decryption_profiles(self):
        """
        Gets the decryption_profiles of this NetworkFirewallPolicy.
        Map defining decryption profiles of the policy.
        The value of an entry is a decryption profile.
        The associated key is the identifier by which the decryption profile is referenced.


        :return: The decryption_profiles of this NetworkFirewallPolicy.
        :rtype: dict(str, DecryptionProfile)
        """
        return self._decryption_profiles

    @decryption_profiles.setter
    def decryption_profiles(self, decryption_profiles):
        """
        Sets the decryption_profiles of this NetworkFirewallPolicy.
        Map defining decryption profiles of the policy.
        The value of an entry is a decryption profile.
        The associated key is the identifier by which the decryption profile is referenced.


        :param decryption_profiles: The decryption_profiles of this NetworkFirewallPolicy.
        :type: dict(str, DecryptionProfile)
        """
        self._decryption_profiles = decryption_profiles

    @property
    def is_firewall_attached(self):
        """
        **[Required]** Gets the is_firewall_attached of this NetworkFirewallPolicy.
        To determine if any Network Firewall is associated with this Network Firewall Policy.


        :return: The is_firewall_attached of this NetworkFirewallPolicy.
        :rtype: bool
        """
        return self._is_firewall_attached

    @is_firewall_attached.setter
    def is_firewall_attached(self, is_firewall_attached):
        """
        Sets the is_firewall_attached of this NetworkFirewallPolicy.
        To determine if any Network Firewall is associated with this Network Firewall Policy.


        :param is_firewall_attached: The is_firewall_attached of this NetworkFirewallPolicy.
        :type: bool
        """
        self._is_firewall_attached = is_firewall_attached

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this NetworkFirewallPolicy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this NetworkFirewallPolicy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this NetworkFirewallPolicy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this NetworkFirewallPolicy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this NetworkFirewallPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this NetworkFirewallPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this NetworkFirewallPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this NetworkFirewallPolicy.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this NetworkFirewallPolicy.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this NetworkFirewallPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this NetworkFirewallPolicy.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this NetworkFirewallPolicy.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
