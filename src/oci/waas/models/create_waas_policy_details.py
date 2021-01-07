# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateWaasPolicyDetails(object):
    """
    The required data to create a WAAS policy.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateWaasPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateWaasPolicyDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateWaasPolicyDetails.
        :type display_name: str

        :param domain:
            The value to assign to the domain property of this CreateWaasPolicyDetails.
        :type domain: str

        :param additional_domains:
            The value to assign to the additional_domains property of this CreateWaasPolicyDetails.
        :type additional_domains: list[str]

        :param origins:
            The value to assign to the origins property of this CreateWaasPolicyDetails.
        :type origins: dict(str, Origin)

        :param origin_groups:
            The value to assign to the origin_groups property of this CreateWaasPolicyDetails.
        :type origin_groups: dict(str, OriginGroup)

        :param policy_config:
            The value to assign to the policy_config property of this CreateWaasPolicyDetails.
        :type policy_config: oci.waas.models.PolicyConfig

        :param waf_config:
            The value to assign to the waf_config property of this CreateWaasPolicyDetails.
        :type waf_config: oci.waas.models.WafConfigDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateWaasPolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateWaasPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'domain': 'str',
            'additional_domains': 'list[str]',
            'origins': 'dict(str, Origin)',
            'origin_groups': 'dict(str, OriginGroup)',
            'policy_config': 'PolicyConfig',
            'waf_config': 'WafConfigDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'domain': 'domain',
            'additional_domains': 'additionalDomains',
            'origins': 'origins',
            'origin_groups': 'originGroups',
            'policy_config': 'policyConfig',
            'waf_config': 'wafConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._domain = None
        self._additional_domains = None
        self._origins = None
        self._origin_groups = None
        self._policy_config = None
        self._waf_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateWaasPolicyDetails.
        The `OCID`__ of the compartment in which to create the WAAS policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateWaasPolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateWaasPolicyDetails.
        The `OCID`__ of the compartment in which to create the WAAS policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateWaasPolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateWaasPolicyDetails.
        A user-friendly name for the WAAS policy. The name can be changed and does not need to be unique.


        :return: The display_name of this CreateWaasPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateWaasPolicyDetails.
        A user-friendly name for the WAAS policy. The name can be changed and does not need to be unique.


        :param display_name: The display_name of this CreateWaasPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def domain(self):
        """
        **[Required]** Gets the domain of this CreateWaasPolicyDetails.
        The web application domain that the WAAS policy protects.


        :return: The domain of this CreateWaasPolicyDetails.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this CreateWaasPolicyDetails.
        The web application domain that the WAAS policy protects.


        :param domain: The domain of this CreateWaasPolicyDetails.
        :type: str
        """
        self._domain = domain

    @property
    def additional_domains(self):
        """
        Gets the additional_domains of this CreateWaasPolicyDetails.
        An array of additional domains for the specified web application.


        :return: The additional_domains of this CreateWaasPolicyDetails.
        :rtype: list[str]
        """
        return self._additional_domains

    @additional_domains.setter
    def additional_domains(self, additional_domains):
        """
        Sets the additional_domains of this CreateWaasPolicyDetails.
        An array of additional domains for the specified web application.


        :param additional_domains: The additional_domains of this CreateWaasPolicyDetails.
        :type: list[str]
        """
        self._additional_domains = additional_domains

    @property
    def origins(self):
        """
        Gets the origins of this CreateWaasPolicyDetails.
        A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.


        :return: The origins of this CreateWaasPolicyDetails.
        :rtype: dict(str, Origin)
        """
        return self._origins

    @origins.setter
    def origins(self, origins):
        """
        Sets the origins of this CreateWaasPolicyDetails.
        A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.


        :param origins: The origins of this CreateWaasPolicyDetails.
        :type: dict(str, Origin)
        """
        self._origins = origins

    @property
    def origin_groups(self):
        """
        Gets the origin_groups of this CreateWaasPolicyDetails.
        The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests.
        To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.


        :return: The origin_groups of this CreateWaasPolicyDetails.
        :rtype: dict(str, OriginGroup)
        """
        return self._origin_groups

    @origin_groups.setter
    def origin_groups(self, origin_groups):
        """
        Sets the origin_groups of this CreateWaasPolicyDetails.
        The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests.
        To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.


        :param origin_groups: The origin_groups of this CreateWaasPolicyDetails.
        :type: dict(str, OriginGroup)
        """
        self._origin_groups = origin_groups

    @property
    def policy_config(self):
        """
        Gets the policy_config of this CreateWaasPolicyDetails.

        :return: The policy_config of this CreateWaasPolicyDetails.
        :rtype: oci.waas.models.PolicyConfig
        """
        return self._policy_config

    @policy_config.setter
    def policy_config(self, policy_config):
        """
        Sets the policy_config of this CreateWaasPolicyDetails.

        :param policy_config: The policy_config of this CreateWaasPolicyDetails.
        :type: oci.waas.models.PolicyConfig
        """
        self._policy_config = policy_config

    @property
    def waf_config(self):
        """
        Gets the waf_config of this CreateWaasPolicyDetails.

        :return: The waf_config of this CreateWaasPolicyDetails.
        :rtype: oci.waas.models.WafConfigDetails
        """
        return self._waf_config

    @waf_config.setter
    def waf_config(self, waf_config):
        """
        Sets the waf_config of this CreateWaasPolicyDetails.

        :param waf_config: The waf_config of this CreateWaasPolicyDetails.
        :type: oci.waas.models.WafConfigDetails
        """
        self._waf_config = waf_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateWaasPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateWaasPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateWaasPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateWaasPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateWaasPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateWaasPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateWaasPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateWaasPolicyDetails.
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
