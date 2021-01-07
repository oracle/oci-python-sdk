# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WafConfig(object):
    """
    The Web Application Firewall configuration for the WAAS policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WafConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param access_rules:
            The value to assign to the access_rules property of this WafConfig.
        :type access_rules: list[oci.waas.models.AccessRule]

        :param address_rate_limiting:
            The value to assign to the address_rate_limiting property of this WafConfig.
        :type address_rate_limiting: oci.waas.models.AddressRateLimiting

        :param captchas:
            The value to assign to the captchas property of this WafConfig.
        :type captchas: list[oci.waas.models.Captcha]

        :param device_fingerprint_challenge:
            The value to assign to the device_fingerprint_challenge property of this WafConfig.
        :type device_fingerprint_challenge: oci.waas.models.DeviceFingerprintChallenge

        :param good_bots:
            The value to assign to the good_bots property of this WafConfig.
        :type good_bots: list[oci.waas.models.GoodBot]

        :param human_interaction_challenge:
            The value to assign to the human_interaction_challenge property of this WafConfig.
        :type human_interaction_challenge: oci.waas.models.HumanInteractionChallenge

        :param js_challenge:
            The value to assign to the js_challenge property of this WafConfig.
        :type js_challenge: oci.waas.models.JsChallenge

        :param origin:
            The value to assign to the origin property of this WafConfig.
        :type origin: str

        :param caching_rules:
            The value to assign to the caching_rules property of this WafConfig.
        :type caching_rules: list[oci.waas.models.CachingRule]

        :param custom_protection_rules:
            The value to assign to the custom_protection_rules property of this WafConfig.
        :type custom_protection_rules: list[oci.waas.models.CustomProtectionRuleSetting]

        :param origin_groups:
            The value to assign to the origin_groups property of this WafConfig.
        :type origin_groups: list[str]

        :param protection_rules:
            The value to assign to the protection_rules property of this WafConfig.
        :type protection_rules: list[oci.waas.models.ProtectionRule]

        :param protection_settings:
            The value to assign to the protection_settings property of this WafConfig.
        :type protection_settings: oci.waas.models.ProtectionSettings

        :param threat_feeds:
            The value to assign to the threat_feeds property of this WafConfig.
        :type threat_feeds: list[oci.waas.models.ThreatFeed]

        :param whitelists:
            The value to assign to the whitelists property of this WafConfig.
        :type whitelists: list[oci.waas.models.Whitelist]

        """
        self.swagger_types = {
            'access_rules': 'list[AccessRule]',
            'address_rate_limiting': 'AddressRateLimiting',
            'captchas': 'list[Captcha]',
            'device_fingerprint_challenge': 'DeviceFingerprintChallenge',
            'good_bots': 'list[GoodBot]',
            'human_interaction_challenge': 'HumanInteractionChallenge',
            'js_challenge': 'JsChallenge',
            'origin': 'str',
            'caching_rules': 'list[CachingRule]',
            'custom_protection_rules': 'list[CustomProtectionRuleSetting]',
            'origin_groups': 'list[str]',
            'protection_rules': 'list[ProtectionRule]',
            'protection_settings': 'ProtectionSettings',
            'threat_feeds': 'list[ThreatFeed]',
            'whitelists': 'list[Whitelist]'
        }

        self.attribute_map = {
            'access_rules': 'accessRules',
            'address_rate_limiting': 'addressRateLimiting',
            'captchas': 'captchas',
            'device_fingerprint_challenge': 'deviceFingerprintChallenge',
            'good_bots': 'goodBots',
            'human_interaction_challenge': 'humanInteractionChallenge',
            'js_challenge': 'jsChallenge',
            'origin': 'origin',
            'caching_rules': 'cachingRules',
            'custom_protection_rules': 'customProtectionRules',
            'origin_groups': 'originGroups',
            'protection_rules': 'protectionRules',
            'protection_settings': 'protectionSettings',
            'threat_feeds': 'threatFeeds',
            'whitelists': 'whitelists'
        }

        self._access_rules = None
        self._address_rate_limiting = None
        self._captchas = None
        self._device_fingerprint_challenge = None
        self._good_bots = None
        self._human_interaction_challenge = None
        self._js_challenge = None
        self._origin = None
        self._caching_rules = None
        self._custom_protection_rules = None
        self._origin_groups = None
        self._protection_rules = None
        self._protection_settings = None
        self._threat_feeds = None
        self._whitelists = None

    @property
    def access_rules(self):
        """
        Gets the access_rules of this WafConfig.
        The access rules applied to the Web Application Firewall. Used for defining custom access policies with the combination of `ALLOW`, `DETECT`, and `BLOCK` rules, based on different criteria.


        :return: The access_rules of this WafConfig.
        :rtype: list[oci.waas.models.AccessRule]
        """
        return self._access_rules

    @access_rules.setter
    def access_rules(self, access_rules):
        """
        Sets the access_rules of this WafConfig.
        The access rules applied to the Web Application Firewall. Used for defining custom access policies with the combination of `ALLOW`, `DETECT`, and `BLOCK` rules, based on different criteria.


        :param access_rules: The access_rules of this WafConfig.
        :type: list[oci.waas.models.AccessRule]
        """
        self._access_rules = access_rules

    @property
    def address_rate_limiting(self):
        """
        Gets the address_rate_limiting of this WafConfig.
        The IP address rate limiting settings used to limit the number of requests from an address.


        :return: The address_rate_limiting of this WafConfig.
        :rtype: oci.waas.models.AddressRateLimiting
        """
        return self._address_rate_limiting

    @address_rate_limiting.setter
    def address_rate_limiting(self, address_rate_limiting):
        """
        Sets the address_rate_limiting of this WafConfig.
        The IP address rate limiting settings used to limit the number of requests from an address.


        :param address_rate_limiting: The address_rate_limiting of this WafConfig.
        :type: oci.waas.models.AddressRateLimiting
        """
        self._address_rate_limiting = address_rate_limiting

    @property
    def captchas(self):
        """
        Gets the captchas of this WafConfig.
        A list of CAPTCHA challenge settings. These are used to challenge requests with a CAPTCHA to block bots.


        :return: The captchas of this WafConfig.
        :rtype: list[oci.waas.models.Captcha]
        """
        return self._captchas

    @captchas.setter
    def captchas(self, captchas):
        """
        Sets the captchas of this WafConfig.
        A list of CAPTCHA challenge settings. These are used to challenge requests with a CAPTCHA to block bots.


        :param captchas: The captchas of this WafConfig.
        :type: list[oci.waas.models.Captcha]
        """
        self._captchas = captchas

    @property
    def device_fingerprint_challenge(self):
        """
        Gets the device_fingerprint_challenge of this WafConfig.
        The device fingerprint challenge settings. Used to detect unique devices based on the device fingerprint information collected in order to block bots.


        :return: The device_fingerprint_challenge of this WafConfig.
        :rtype: oci.waas.models.DeviceFingerprintChallenge
        """
        return self._device_fingerprint_challenge

    @device_fingerprint_challenge.setter
    def device_fingerprint_challenge(self, device_fingerprint_challenge):
        """
        Sets the device_fingerprint_challenge of this WafConfig.
        The device fingerprint challenge settings. Used to detect unique devices based on the device fingerprint information collected in order to block bots.


        :param device_fingerprint_challenge: The device_fingerprint_challenge of this WafConfig.
        :type: oci.waas.models.DeviceFingerprintChallenge
        """
        self._device_fingerprint_challenge = device_fingerprint_challenge

    @property
    def good_bots(self):
        """
        Gets the good_bots of this WafConfig.
        A list of bots allowed to access the web application.


        :return: The good_bots of this WafConfig.
        :rtype: list[oci.waas.models.GoodBot]
        """
        return self._good_bots

    @good_bots.setter
    def good_bots(self, good_bots):
        """
        Sets the good_bots of this WafConfig.
        A list of bots allowed to access the web application.


        :param good_bots: The good_bots of this WafConfig.
        :type: list[oci.waas.models.GoodBot]
        """
        self._good_bots = good_bots

    @property
    def human_interaction_challenge(self):
        """
        Gets the human_interaction_challenge of this WafConfig.
        The human interaction challenge settings. Used to look for natural human interactions such as mouse movements, time on site, and page scrolling to identify bots.


        :return: The human_interaction_challenge of this WafConfig.
        :rtype: oci.waas.models.HumanInteractionChallenge
        """
        return self._human_interaction_challenge

    @human_interaction_challenge.setter
    def human_interaction_challenge(self, human_interaction_challenge):
        """
        Sets the human_interaction_challenge of this WafConfig.
        The human interaction challenge settings. Used to look for natural human interactions such as mouse movements, time on site, and page scrolling to identify bots.


        :param human_interaction_challenge: The human_interaction_challenge of this WafConfig.
        :type: oci.waas.models.HumanInteractionChallenge
        """
        self._human_interaction_challenge = human_interaction_challenge

    @property
    def js_challenge(self):
        """
        Gets the js_challenge of this WafConfig.
        The JavaScript challenge settings. Used to challenge requests with a JavaScript challenge and take the action if a browser has no JavaScript support in order to block bots.


        :return: The js_challenge of this WafConfig.
        :rtype: oci.waas.models.JsChallenge
        """
        return self._js_challenge

    @js_challenge.setter
    def js_challenge(self, js_challenge):
        """
        Sets the js_challenge of this WafConfig.
        The JavaScript challenge settings. Used to challenge requests with a JavaScript challenge and take the action if a browser has no JavaScript support in order to block bots.


        :param js_challenge: The js_challenge of this WafConfig.
        :type: oci.waas.models.JsChallenge
        """
        self._js_challenge = js_challenge

    @property
    def origin(self):
        """
        Gets the origin of this WafConfig.
        The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in `Origins`. Required when creating the `WafConfig` resource, but not on update.


        :return: The origin of this WafConfig.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this WafConfig.
        The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in `Origins`. Required when creating the `WafConfig` resource, but not on update.


        :param origin: The origin of this WafConfig.
        :type: str
        """
        self._origin = origin

    @property
    def caching_rules(self):
        """
        Gets the caching_rules of this WafConfig.
        A list of caching rules applied to the web application.


        :return: The caching_rules of this WafConfig.
        :rtype: list[oci.waas.models.CachingRule]
        """
        return self._caching_rules

    @caching_rules.setter
    def caching_rules(self, caching_rules):
        """
        Sets the caching_rules of this WafConfig.
        A list of caching rules applied to the web application.


        :param caching_rules: The caching_rules of this WafConfig.
        :type: list[oci.waas.models.CachingRule]
        """
        self._caching_rules = caching_rules

    @property
    def custom_protection_rules(self):
        """
        Gets the custom_protection_rules of this WafConfig.
        A list of the custom protection rule OCIDs and their actions.


        :return: The custom_protection_rules of this WafConfig.
        :rtype: list[oci.waas.models.CustomProtectionRuleSetting]
        """
        return self._custom_protection_rules

    @custom_protection_rules.setter
    def custom_protection_rules(self, custom_protection_rules):
        """
        Sets the custom_protection_rules of this WafConfig.
        A list of the custom protection rule OCIDs and their actions.


        :param custom_protection_rules: The custom_protection_rules of this WafConfig.
        :type: list[oci.waas.models.CustomProtectionRuleSetting]
        """
        self._custom_protection_rules = custom_protection_rules

    @property
    def origin_groups(self):
        """
        Gets the origin_groups of this WafConfig.
        The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests.
        To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.


        :return: The origin_groups of this WafConfig.
        :rtype: list[str]
        """
        return self._origin_groups

    @origin_groups.setter
    def origin_groups(self, origin_groups):
        """
        Sets the origin_groups of this WafConfig.
        The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests.
        To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.


        :param origin_groups: The origin_groups of this WafConfig.
        :type: list[str]
        """
        self._origin_groups = origin_groups

    @property
    def protection_rules(self):
        """
        Gets the protection_rules of this WafConfig.
        A list of the protection rules and their details.


        :return: The protection_rules of this WafConfig.
        :rtype: list[oci.waas.models.ProtectionRule]
        """
        return self._protection_rules

    @protection_rules.setter
    def protection_rules(self, protection_rules):
        """
        Sets the protection_rules of this WafConfig.
        A list of the protection rules and their details.


        :param protection_rules: The protection_rules of this WafConfig.
        :type: list[oci.waas.models.ProtectionRule]
        """
        self._protection_rules = protection_rules

    @property
    def protection_settings(self):
        """
        Gets the protection_settings of this WafConfig.
        The settings to apply to protection rules.


        :return: The protection_settings of this WafConfig.
        :rtype: oci.waas.models.ProtectionSettings
        """
        return self._protection_settings

    @protection_settings.setter
    def protection_settings(self, protection_settings):
        """
        Sets the protection_settings of this WafConfig.
        The settings to apply to protection rules.


        :param protection_settings: The protection_settings of this WafConfig.
        :type: oci.waas.models.ProtectionSettings
        """
        self._protection_settings = protection_settings

    @property
    def threat_feeds(self):
        """
        Gets the threat_feeds of this WafConfig.
        A list of threat intelligence feeds and the actions to apply to known malicious traffic based on internet intelligence.


        :return: The threat_feeds of this WafConfig.
        :rtype: list[oci.waas.models.ThreatFeed]
        """
        return self._threat_feeds

    @threat_feeds.setter
    def threat_feeds(self, threat_feeds):
        """
        Sets the threat_feeds of this WafConfig.
        A list of threat intelligence feeds and the actions to apply to known malicious traffic based on internet intelligence.


        :param threat_feeds: The threat_feeds of this WafConfig.
        :type: list[oci.waas.models.ThreatFeed]
        """
        self._threat_feeds = threat_feeds

    @property
    def whitelists(self):
        """
        Gets the whitelists of this WafConfig.
        A list of IP addresses that bypass the Web Application Firewall.


        :return: The whitelists of this WafConfig.
        :rtype: list[oci.waas.models.Whitelist]
        """
        return self._whitelists

    @whitelists.setter
    def whitelists(self, whitelists):
        """
        Sets the whitelists of this WafConfig.
        A list of IP addresses that bypass the Web Application Firewall.


        :param whitelists: The whitelists of this WafConfig.
        :type: list[oci.waas.models.Whitelist]
        """
        self._whitelists = whitelists

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
