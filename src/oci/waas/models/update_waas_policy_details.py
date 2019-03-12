# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateWaasPolicyDetails(object):
    """
    Updates the configuration details of a WAAS policy.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateWaasPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateWaasPolicyDetails.
        :type display_name: str

        :param additional_domains:
            The value to assign to the additional_domains property of this UpdateWaasPolicyDetails.
        :type additional_domains: list[str]

        :param origins:
            The value to assign to the origins property of this UpdateWaasPolicyDetails.
        :type origins: dict(str, Origin)

        :param policy_config:
            The value to assign to the policy_config property of this UpdateWaasPolicyDetails.
        :type policy_config: PolicyConfig

        :param waf_config:
            The value to assign to the waf_config property of this UpdateWaasPolicyDetails.
        :type waf_config: WafConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateWaasPolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateWaasPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'additional_domains': 'list[str]',
            'origins': 'dict(str, Origin)',
            'policy_config': 'PolicyConfig',
            'waf_config': 'WafConfig',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'additional_domains': 'additionalDomains',
            'origins': 'origins',
            'policy_config': 'policyConfig',
            'waf_config': 'wafConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._additional_domains = None
        self._origins = None
        self._policy_config = None
        self._waf_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateWaasPolicyDetails.
        A user-friendly name for the WAAS policy. The name is can be changed and does not need to be unique.


        :return: The display_name of this UpdateWaasPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateWaasPolicyDetails.
        A user-friendly name for the WAAS policy. The name is can be changed and does not need to be unique.


        :param display_name: The display_name of this UpdateWaasPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def additional_domains(self):
        """
        Gets the additional_domains of this UpdateWaasPolicyDetails.
        An array of additional domains protected by this WAAS policy.


        :return: The additional_domains of this UpdateWaasPolicyDetails.
        :rtype: list[str]
        """
        return self._additional_domains

    @additional_domains.setter
    def additional_domains(self, additional_domains):
        """
        Sets the additional_domains of this UpdateWaasPolicyDetails.
        An array of additional domains protected by this WAAS policy.


        :param additional_domains: The additional_domains of this UpdateWaasPolicyDetails.
        :type: list[str]
        """
        self._additional_domains = additional_domains

    @property
    def origins(self):
        """
        Gets the origins of this UpdateWaasPolicyDetails.
        A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.


        :return: The origins of this UpdateWaasPolicyDetails.
        :rtype: dict(str, Origin)
        """
        return self._origins

    @origins.setter
    def origins(self, origins):
        """
        Sets the origins of this UpdateWaasPolicyDetails.
        A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.


        :param origins: The origins of this UpdateWaasPolicyDetails.
        :type: dict(str, Origin)
        """
        self._origins = origins

    @property
    def policy_config(self):
        """
        Gets the policy_config of this UpdateWaasPolicyDetails.

        :return: The policy_config of this UpdateWaasPolicyDetails.
        :rtype: PolicyConfig
        """
        return self._policy_config

    @policy_config.setter
    def policy_config(self, policy_config):
        """
        Sets the policy_config of this UpdateWaasPolicyDetails.

        :param policy_config: The policy_config of this UpdateWaasPolicyDetails.
        :type: PolicyConfig
        """
        self._policy_config = policy_config

    @property
    def waf_config(self):
        """
        Gets the waf_config of this UpdateWaasPolicyDetails.

        :return: The waf_config of this UpdateWaasPolicyDetails.
        :rtype: WafConfig
        """
        return self._waf_config

    @waf_config.setter
    def waf_config(self, waf_config):
        """
        Sets the waf_config of this UpdateWaasPolicyDetails.

        :param waf_config: The waf_config of this UpdateWaasPolicyDetails.
        :type: WafConfig
        """
        self._waf_config = waf_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateWaasPolicyDetails.
        A simple key-value pair without any defined schema.


        :return: The freeform_tags of this UpdateWaasPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateWaasPolicyDetails.
        A simple key-value pair without any defined schema.


        :param freeform_tags: The freeform_tags of this UpdateWaasPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateWaasPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateWaasPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateWaasPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateWaasPolicyDetails.
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
