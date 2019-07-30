# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WaasPolicy(object):
    """
    The details of a Web Application Acceleration and Security (WAAS) policy. A policy describes how the WAAS service should operate for the configured web application.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the lifecycle_state property of a WaasPolicy.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a WaasPolicy.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a WaasPolicy.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a WaasPolicy.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a WaasPolicy.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a WaasPolicy.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new WaasPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WaasPolicy.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WaasPolicy.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this WaasPolicy.
        :type display_name: str

        :param domain:
            The value to assign to the domain property of this WaasPolicy.
        :type domain: str

        :param additional_domains:
            The value to assign to the additional_domains property of this WaasPolicy.
        :type additional_domains: list[str]

        :param cname:
            The value to assign to the cname property of this WaasPolicy.
        :type cname: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this WaasPolicy.
            Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this WaasPolicy.
        :type time_created: datetime

        :param origins:
            The value to assign to the origins property of this WaasPolicy.
        :type origins: dict(str, Origin)

        :param policy_config:
            The value to assign to the policy_config property of this WaasPolicy.
        :type policy_config: PolicyConfig

        :param waf_config:
            The value to assign to the waf_config property of this WaasPolicy.
        :type waf_config: WafConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this WaasPolicy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this WaasPolicy.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'domain': 'str',
            'additional_domains': 'list[str]',
            'cname': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'origins': 'dict(str, Origin)',
            'policy_config': 'PolicyConfig',
            'waf_config': 'WafConfig',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'domain': 'domain',
            'additional_domains': 'additionalDomains',
            'cname': 'cname',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'origins': 'origins',
            'policy_config': 'policyConfig',
            'waf_config': 'wafConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._domain = None
        self._additional_domains = None
        self._cname = None
        self._lifecycle_state = None
        self._time_created = None
        self._origins = None
        self._policy_config = None
        self._waf_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this WaasPolicy.
        The `OCID`__ of the WAAS policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this WaasPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WaasPolicy.
        The `OCID`__ of the WAAS policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this WaasPolicy.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this WaasPolicy.
        The `OCID`__ of the WAAS policy's compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this WaasPolicy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WaasPolicy.
        The `OCID`__ of the WAAS policy's compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this WaasPolicy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this WaasPolicy.
        The user-friendly name of the WAAS policy. The name can be changed and does not need to be unique.


        :return: The display_name of this WaasPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this WaasPolicy.
        The user-friendly name of the WAAS policy. The name can be changed and does not need to be unique.


        :param display_name: The display_name of this WaasPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def domain(self):
        """
        Gets the domain of this WaasPolicy.
        The web application domain that the WAAS policy protects.


        :return: The domain of this WaasPolicy.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this WaasPolicy.
        The web application domain that the WAAS policy protects.


        :param domain: The domain of this WaasPolicy.
        :type: str
        """
        self._domain = domain

    @property
    def additional_domains(self):
        """
        Gets the additional_domains of this WaasPolicy.
        An array of additional domains for this web application.


        :return: The additional_domains of this WaasPolicy.
        :rtype: list[str]
        """
        return self._additional_domains

    @additional_domains.setter
    def additional_domains(self, additional_domains):
        """
        Sets the additional_domains of this WaasPolicy.
        An array of additional domains for this web application.


        :param additional_domains: The additional_domains of this WaasPolicy.
        :type: list[str]
        """
        self._additional_domains = additional_domains

    @property
    def cname(self):
        """
        Gets the cname of this WaasPolicy.
        The CNAME record to add to your DNS configuration to route traffic for the domain, and all additional domains, through the WAF.


        :return: The cname of this WaasPolicy.
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """
        Sets the cname of this WaasPolicy.
        The CNAME record to add to your DNS configuration to route traffic for the domain, and all additional domains, through the WAF.


        :param cname: The cname of this WaasPolicy.
        :type: str
        """
        self._cname = cname

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this WaasPolicy.
        The current lifecycle state of the WAAS policy.

        Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this WaasPolicy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this WaasPolicy.
        The current lifecycle state of the WAAS policy.


        :param lifecycle_state: The lifecycle_state of this WaasPolicy.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this WaasPolicy.
        The date and time the policy was created, expressed in RFC 3339 timestamp format.


        :return: The time_created of this WaasPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this WaasPolicy.
        The date and time the policy was created, expressed in RFC 3339 timestamp format.


        :param time_created: The time_created of this WaasPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def origins(self):
        """
        Gets the origins of this WaasPolicy.
        A map of host servers (origins) and their keys for the web application. Origin keys are used to associate origins to specific protection rules. The key should be a user-friendly name for the host. **Examples:** `primary` or `secondary`.


        :return: The origins of this WaasPolicy.
        :rtype: dict(str, Origin)
        """
        return self._origins

    @origins.setter
    def origins(self, origins):
        """
        Sets the origins of this WaasPolicy.
        A map of host servers (origins) and their keys for the web application. Origin keys are used to associate origins to specific protection rules. The key should be a user-friendly name for the host. **Examples:** `primary` or `secondary`.


        :param origins: The origins of this WaasPolicy.
        :type: dict(str, Origin)
        """
        self._origins = origins

    @property
    def policy_config(self):
        """
        Gets the policy_config of this WaasPolicy.

        :return: The policy_config of this WaasPolicy.
        :rtype: PolicyConfig
        """
        return self._policy_config

    @policy_config.setter
    def policy_config(self, policy_config):
        """
        Sets the policy_config of this WaasPolicy.

        :param policy_config: The policy_config of this WaasPolicy.
        :type: PolicyConfig
        """
        self._policy_config = policy_config

    @property
    def waf_config(self):
        """
        Gets the waf_config of this WaasPolicy.

        :return: The waf_config of this WaasPolicy.
        :rtype: WafConfig
        """
        return self._waf_config

    @waf_config.setter
    def waf_config(self, waf_config):
        """
        Sets the waf_config of this WaasPolicy.

        :param waf_config: The waf_config of this WaasPolicy.
        :type: WafConfig
        """
        self._waf_config = waf_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this WaasPolicy.
        A simple key-value pair without any defined schema.


        :return: The freeform_tags of this WaasPolicy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this WaasPolicy.
        A simple key-value pair without any defined schema.


        :param freeform_tags: The freeform_tags of this WaasPolicy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this WaasPolicy.
        A key-value pair with a defined schema that restricts the values of tags. These predefined keys are scoped to namespaces.


        :return: The defined_tags of this WaasPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this WaasPolicy.
        A key-value pair with a defined schema that restricts the values of tags. These predefined keys are scoped to namespaces.


        :param defined_tags: The defined_tags of this WaasPolicy.
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
