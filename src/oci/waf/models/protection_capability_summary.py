# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210930


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProtectionCapabilitySummary(object):
    """
    A summary of available OCI-managed protection capabilities in WebAppFirewallPolicy.
    Protection capabilies checks HTTP requests/responses if they are malicious.
    """

    #: A constant which can be used with the type property of a ProtectionCapabilitySummary.
    #: This constant has a value of "REQUEST_PROTECTION_CAPABILITY"
    TYPE_REQUEST_PROTECTION_CAPABILITY = "REQUEST_PROTECTION_CAPABILITY"

    #: A constant which can be used with the type property of a ProtectionCapabilitySummary.
    #: This constant has a value of "RESPONSE_PROTECTION_CAPABILITY"
    TYPE_RESPONSE_PROTECTION_CAPABILITY = "RESPONSE_PROTECTION_CAPABILITY"

    def __init__(self, **kwargs):
        """
        Initializes a new ProtectionCapabilitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ProtectionCapabilitySummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this ProtectionCapabilitySummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ProtectionCapabilitySummary.
        :type description: str

        :param version:
            The value to assign to the version property of this ProtectionCapabilitySummary.
        :type version: int

        :param is_latest_version:
            The value to assign to the is_latest_version property of this ProtectionCapabilitySummary.
        :type is_latest_version: bool

        :param group_tags:
            The value to assign to the group_tags property of this ProtectionCapabilitySummary.
        :type group_tags: list[str]

        :param type:
            The value to assign to the type property of this ProtectionCapabilitySummary.
            Allowed values for this property are: "REQUEST_PROTECTION_CAPABILITY", "RESPONSE_PROTECTION_CAPABILITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param collaborative_action_threshold:
            The value to assign to the collaborative_action_threshold property of this ProtectionCapabilitySummary.
        :type collaborative_action_threshold: int

        :param collaborative_weights:
            The value to assign to the collaborative_weights property of this ProtectionCapabilitySummary.
        :type collaborative_weights: list[oci.waf.models.CollaborativeCapabilityWeight]

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'version': 'int',
            'is_latest_version': 'bool',
            'group_tags': 'list[str]',
            'type': 'str',
            'collaborative_action_threshold': 'int',
            'collaborative_weights': 'list[CollaborativeCapabilityWeight]'
        }
        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'version': 'version',
            'is_latest_version': 'isLatestVersion',
            'group_tags': 'groupTags',
            'type': 'type',
            'collaborative_action_threshold': 'collaborativeActionThreshold',
            'collaborative_weights': 'collaborativeWeights'
        }
        self._key = None
        self._display_name = None
        self._description = None
        self._version = None
        self._is_latest_version = None
        self._group_tags = None
        self._type = None
        self._collaborative_action_threshold = None
        self._collaborative_weights = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this ProtectionCapabilitySummary.
        Unique key of protection capability.


        :return: The key of this ProtectionCapabilitySummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ProtectionCapabilitySummary.
        Unique key of protection capability.


        :param key: The key of this ProtectionCapabilitySummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ProtectionCapabilitySummary.
        The display name of protection capability.


        :return: The display_name of this ProtectionCapabilitySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ProtectionCapabilitySummary.
        The display name of protection capability.


        :param display_name: The display_name of this ProtectionCapabilitySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this ProtectionCapabilitySummary.
        The description of protection capability.


        :return: The description of this ProtectionCapabilitySummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProtectionCapabilitySummary.
        The description of protection capability.


        :param description: The description of this ProtectionCapabilitySummary.
        :type: str
        """
        self._description = description

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ProtectionCapabilitySummary.
        The version of protection capability.


        :return: The version of this ProtectionCapabilitySummary.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ProtectionCapabilitySummary.
        The version of protection capability.


        :param version: The version of this ProtectionCapabilitySummary.
        :type: int
        """
        self._version = version

    @property
    def is_latest_version(self):
        """
        **[Required]** Gets the is_latest_version of this ProtectionCapabilitySummary.
        The field that shows if this is the latest version of protection capability.


        :return: The is_latest_version of this ProtectionCapabilitySummary.
        :rtype: bool
        """
        return self._is_latest_version

    @is_latest_version.setter
    def is_latest_version(self, is_latest_version):
        """
        Sets the is_latest_version of this ProtectionCapabilitySummary.
        The field that shows if this is the latest version of protection capability.


        :param is_latest_version: The is_latest_version of this ProtectionCapabilitySummary.
        :type: bool
        """
        self._is_latest_version = is_latest_version

    @property
    def group_tags(self):
        """
        Gets the group_tags of this ProtectionCapabilitySummary.
        The list of unique names protection capability group tags that are associated with this capability.
        Example: [\"PCI\", \"Recommended\"]


        :return: The group_tags of this ProtectionCapabilitySummary.
        :rtype: list[str]
        """
        return self._group_tags

    @group_tags.setter
    def group_tags(self, group_tags):
        """
        Sets the group_tags of this ProtectionCapabilitySummary.
        The list of unique names protection capability group tags that are associated with this capability.
        Example: [\"PCI\", \"Recommended\"]


        :param group_tags: The group_tags of this ProtectionCapabilitySummary.
        :type: list[str]
        """
        self._group_tags = group_tags

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ProtectionCapabilitySummary.
        The type of protection capability.

        * **REQUEST_PROTECTION_CAPABILITY** can only be used in `requestProtection` module of WebAppFirewallPolicy.

        * **RESPONSE_PROTECTION_CAPABILITY** can only be used in `responseProtection` module of WebAppFirewallPolicy.

        Allowed values for this property are: "REQUEST_PROTECTION_CAPABILITY", "RESPONSE_PROTECTION_CAPABILITY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ProtectionCapabilitySummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProtectionCapabilitySummary.
        The type of protection capability.

        * **REQUEST_PROTECTION_CAPABILITY** can only be used in `requestProtection` module of WebAppFirewallPolicy.

        * **RESPONSE_PROTECTION_CAPABILITY** can only be used in `responseProtection` module of WebAppFirewallPolicy.


        :param type: The type of this ProtectionCapabilitySummary.
        :type: str
        """
        allowed_values = ["REQUEST_PROTECTION_CAPABILITY", "RESPONSE_PROTECTION_CAPABILITY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def collaborative_action_threshold(self):
        """
        Gets the collaborative_action_threshold of this ProtectionCapabilitySummary.
        The default collaborative action threshold for OCI-managed collaborative protection capability.
        Collaborative protection capabilities are made of several simple, non-collaborative protection capabilities
        (referred to as `contributing capabilities` later on) which have weights assigned to them. These weights can
        be found in the `collaborativeWeights` array.
        For incoming/outgoing HTTP messages, all contributing capabilities are executed and the sum of all triggered
        contributing capabilities weights is calculated. Only if this sum is greater than or equal to
        `collaborativeActionThreshold` is the incoming/outgoing HTTP message marked as malicious.

        This field is ignored for non-collaborative capabilities.


        :return: The collaborative_action_threshold of this ProtectionCapabilitySummary.
        :rtype: int
        """
        return self._collaborative_action_threshold

    @collaborative_action_threshold.setter
    def collaborative_action_threshold(self, collaborative_action_threshold):
        """
        Sets the collaborative_action_threshold of this ProtectionCapabilitySummary.
        The default collaborative action threshold for OCI-managed collaborative protection capability.
        Collaborative protection capabilities are made of several simple, non-collaborative protection capabilities
        (referred to as `contributing capabilities` later on) which have weights assigned to them. These weights can
        be found in the `collaborativeWeights` array.
        For incoming/outgoing HTTP messages, all contributing capabilities are executed and the sum of all triggered
        contributing capabilities weights is calculated. Only if this sum is greater than or equal to
        `collaborativeActionThreshold` is the incoming/outgoing HTTP message marked as malicious.

        This field is ignored for non-collaborative capabilities.


        :param collaborative_action_threshold: The collaborative_action_threshold of this ProtectionCapabilitySummary.
        :type: int
        """
        self._collaborative_action_threshold = collaborative_action_threshold

    @property
    def collaborative_weights(self):
        """
        Gets the collaborative_weights of this ProtectionCapabilitySummary.
        The weights of contributing capabilities.
        Defines how much each contributing capability contributes towards the action threshold of a collaborative protection capability.

        This field is ignored for non-collaborative capabilities.


        :return: The collaborative_weights of this ProtectionCapabilitySummary.
        :rtype: list[oci.waf.models.CollaborativeCapabilityWeight]
        """
        return self._collaborative_weights

    @collaborative_weights.setter
    def collaborative_weights(self, collaborative_weights):
        """
        Sets the collaborative_weights of this ProtectionCapabilitySummary.
        The weights of contributing capabilities.
        Defines how much each contributing capability contributes towards the action threshold of a collaborative protection capability.

        This field is ignored for non-collaborative capabilities.


        :param collaborative_weights: The collaborative_weights of this ProtectionCapabilitySummary.
        :type: list[oci.waf.models.CollaborativeCapabilityWeight]
        """
        self._collaborative_weights = collaborative_weights

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
