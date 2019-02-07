# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSteeringPolicyDetails(object):
    """
    The body for defining a new steering policy.

    *Warning:* Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the template property of a CreateSteeringPolicyDetails.
    #: This constant has a value of "FAILOVER"
    TEMPLATE_FAILOVER = "FAILOVER"

    #: A constant which can be used with the template property of a CreateSteeringPolicyDetails.
    #: This constant has a value of "LOAD_BALANCE"
    TEMPLATE_LOAD_BALANCE = "LOAD_BALANCE"

    #: A constant which can be used with the template property of a CreateSteeringPolicyDetails.
    #: This constant has a value of "ROUTE_BY_GEO"
    TEMPLATE_ROUTE_BY_GEO = "ROUTE_BY_GEO"

    #: A constant which can be used with the template property of a CreateSteeringPolicyDetails.
    #: This constant has a value of "ROUTE_BY_ASN"
    TEMPLATE_ROUTE_BY_ASN = "ROUTE_BY_ASN"

    #: A constant which can be used with the template property of a CreateSteeringPolicyDetails.
    #: This constant has a value of "ROUTE_BY_IP"
    TEMPLATE_ROUTE_BY_IP = "ROUTE_BY_IP"

    #: A constant which can be used with the template property of a CreateSteeringPolicyDetails.
    #: This constant has a value of "CUSTOM"
    TEMPLATE_CUSTOM = "CUSTOM"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSteeringPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSteeringPolicyDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateSteeringPolicyDetails.
        :type display_name: str

        :param ttl:
            The value to assign to the ttl property of this CreateSteeringPolicyDetails.
        :type ttl: int

        :param health_check_monitor_id:
            The value to assign to the health_check_monitor_id property of this CreateSteeringPolicyDetails.
        :type health_check_monitor_id: str

        :param template:
            The value to assign to the template property of this CreateSteeringPolicyDetails.
            Allowed values for this property are: "FAILOVER", "LOAD_BALANCE", "ROUTE_BY_GEO", "ROUTE_BY_ASN", "ROUTE_BY_IP", "CUSTOM"
        :type template: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSteeringPolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSteeringPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param answers:
            The value to assign to the answers property of this CreateSteeringPolicyDetails.
        :type answers: list[SteeringPolicyAnswer]

        :param rules:
            The value to assign to the rules property of this CreateSteeringPolicyDetails.
        :type rules: list[SteeringPolicyRule]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'ttl': 'int',
            'health_check_monitor_id': 'str',
            'template': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'answers': 'list[SteeringPolicyAnswer]',
            'rules': 'list[SteeringPolicyRule]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'ttl': 'ttl',
            'health_check_monitor_id': 'healthCheckMonitorId',
            'template': 'template',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'answers': 'answers',
            'rules': 'rules'
        }

        self._compartment_id = None
        self._display_name = None
        self._ttl = None
        self._health_check_monitor_id = None
        self._template = None
        self._freeform_tags = None
        self._defined_tags = None
        self._answers = None
        self._rules = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSteeringPolicyDetails.
        The OCID of the compartment containing the steering policy.


        :return: The compartment_id of this CreateSteeringPolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSteeringPolicyDetails.
        The OCID of the compartment containing the steering policy.


        :param compartment_id: The compartment_id of this CreateSteeringPolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateSteeringPolicyDetails.
        A user-friendly name for the steering policy.
        Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateSteeringPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSteeringPolicyDetails.
        A user-friendly name for the steering policy.
        Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateSteeringPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def ttl(self):
        """
        Gets the ttl of this CreateSteeringPolicyDetails.
        The Time To Live for responses from the steering policy, in seconds.
        If not specified during creation, a value of 30 seconds will be used.


        :return: The ttl of this CreateSteeringPolicyDetails.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this CreateSteeringPolicyDetails.
        The Time To Live for responses from the steering policy, in seconds.
        If not specified during creation, a value of 30 seconds will be used.


        :param ttl: The ttl of this CreateSteeringPolicyDetails.
        :type: int
        """
        self._ttl = ttl

    @property
    def health_check_monitor_id(self):
        """
        Gets the health_check_monitor_id of this CreateSteeringPolicyDetails.
        The OCID of the health check monitor providing health data about the answers of the
        steering policy.
        A steering policy answer with `rdata` matching a monitored endpoint will use the health
        data of that endpoint.
        A steering policy answer with `rdata` not matching any monitored endpoint will be assumed
        healthy.


        :return: The health_check_monitor_id of this CreateSteeringPolicyDetails.
        :rtype: str
        """
        return self._health_check_monitor_id

    @health_check_monitor_id.setter
    def health_check_monitor_id(self, health_check_monitor_id):
        """
        Sets the health_check_monitor_id of this CreateSteeringPolicyDetails.
        The OCID of the health check monitor providing health data about the answers of the
        steering policy.
        A steering policy answer with `rdata` matching a monitored endpoint will use the health
        data of that endpoint.
        A steering policy answer with `rdata` not matching any monitored endpoint will be assumed
        healthy.


        :param health_check_monitor_id: The health_check_monitor_id of this CreateSteeringPolicyDetails.
        :type: str
        """
        self._health_check_monitor_id = health_check_monitor_id

    @property
    def template(self):
        """
        **[Required]** Gets the template of this CreateSteeringPolicyDetails.
        The common pattern (or lack thereof) to which the steering policy adheres. This
        value restricts the possible configurations of rules, but thereby supports
        specifically tailored interfaces. Values other than \"CUSTOM\" require the rules to
        begin with an unconditional FILTER that keeps answers contingent upon
        `answer.isDisabled != true`, followed
        _if and only if the policy references a health check monitor_ by an unconditional
        HEALTH rule, and require the last rule to be an unconditional LIMIT.
        What must precede the LIMIT rule is determined by the template value:
        - FAILOVER requires exactly an unconditional PRIORITY rule that ranks answers by pool.
          Each answer pool must have a unique priority value assigned to it. Answer data must
          be defined in the `defaultAnswerData` property for the rule and the `cases` property
          must not be defined.
        - LOAD_BALANCE requires exactly an unconditional WEIGHTED rule that shuffles answers
          by name. Answer data must be defined in the `defaultAnswerData` property for the
          rule and the `cases` property must not be defined.
        - ROUTE_BY_GEO requires exactly one PRIORITY rule that ranks answers by pool using the
          geographical location of the client as a condition. Within that rule you may only
          use `query.client.geoKey` in the `caseCondition` expressions for defining the cases.
          For each case in the PRIORITY rule each answer pool must have a unique priority
          value assigned to it. Answer data can only be defined within cases and
          `defaultAnswerData` cannot be used in the PRIORITY rule.
        - ROUTE_BY_ASN requires exactly one PRIORITY rule that ranks answers by pool using the
          ASN of the client as a condition. Within that rule you may only use
          `query.client.asn` in the `caseCondition` expressions for defining the cases.
          For each case in the PRIORITY rule each answer pool must have a unique priority
          value assigned to it. Answer data can only be defined within cases and
          `defaultAnswerData` cannot be used in the PRIORITY rule.
        - ROUTE_BY_IP requires exactly one PRIORITY rule that ranks answers by pool using the
          IP subnet of the client as a condition. Within that rule you may only use
          `query.client.address` in the `caseCondition` expressions for defining the cases.
          For each case in the PRIORITY rule each answer pool must have a unique priority
          value assigned to it. Answer data can only be defined within cases and
          `defaultAnswerData` cannot be used in the PRIORITY rule.
        - CUSTOM allows an arbitrary configuration of rules.

        For an existing steering policy, the template value may be changed to any of the
        supported options but the resulting policy must conform to the requirements for the
        new template type or else a Bad Request error will be returned.

        Allowed values for this property are: "FAILOVER", "LOAD_BALANCE", "ROUTE_BY_GEO", "ROUTE_BY_ASN", "ROUTE_BY_IP", "CUSTOM"


        :return: The template of this CreateSteeringPolicyDetails.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this CreateSteeringPolicyDetails.
        The common pattern (or lack thereof) to which the steering policy adheres. This
        value restricts the possible configurations of rules, but thereby supports
        specifically tailored interfaces. Values other than \"CUSTOM\" require the rules to
        begin with an unconditional FILTER that keeps answers contingent upon
        `answer.isDisabled != true`, followed
        _if and only if the policy references a health check monitor_ by an unconditional
        HEALTH rule, and require the last rule to be an unconditional LIMIT.
        What must precede the LIMIT rule is determined by the template value:
        - FAILOVER requires exactly an unconditional PRIORITY rule that ranks answers by pool.
          Each answer pool must have a unique priority value assigned to it. Answer data must
          be defined in the `defaultAnswerData` property for the rule and the `cases` property
          must not be defined.
        - LOAD_BALANCE requires exactly an unconditional WEIGHTED rule that shuffles answers
          by name. Answer data must be defined in the `defaultAnswerData` property for the
          rule and the `cases` property must not be defined.
        - ROUTE_BY_GEO requires exactly one PRIORITY rule that ranks answers by pool using the
          geographical location of the client as a condition. Within that rule you may only
          use `query.client.geoKey` in the `caseCondition` expressions for defining the cases.
          For each case in the PRIORITY rule each answer pool must have a unique priority
          value assigned to it. Answer data can only be defined within cases and
          `defaultAnswerData` cannot be used in the PRIORITY rule.
        - ROUTE_BY_ASN requires exactly one PRIORITY rule that ranks answers by pool using the
          ASN of the client as a condition. Within that rule you may only use
          `query.client.asn` in the `caseCondition` expressions for defining the cases.
          For each case in the PRIORITY rule each answer pool must have a unique priority
          value assigned to it. Answer data can only be defined within cases and
          `defaultAnswerData` cannot be used in the PRIORITY rule.
        - ROUTE_BY_IP requires exactly one PRIORITY rule that ranks answers by pool using the
          IP subnet of the client as a condition. Within that rule you may only use
          `query.client.address` in the `caseCondition` expressions for defining the cases.
          For each case in the PRIORITY rule each answer pool must have a unique priority
          value assigned to it. Answer data can only be defined within cases and
          `defaultAnswerData` cannot be used in the PRIORITY rule.
        - CUSTOM allows an arbitrary configuration of rules.

        For an existing steering policy, the template value may be changed to any of the
        supported options but the resulting policy must conform to the requirements for the
        new template type or else a Bad Request error will be returned.


        :param template: The template of this CreateSteeringPolicyDetails.
        :type: str
        """
        allowed_values = ["FAILOVER", "LOAD_BALANCE", "ROUTE_BY_GEO", "ROUTE_BY_ASN", "ROUTE_BY_IP", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(template, allowed_values):
            raise ValueError(
                "Invalid value for `template`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._template = template

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSteeringPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        For more information, see `Resource Tags`__.
        Example: `{\"bar-key\": \"value\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateSteeringPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSteeringPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        For more information, see `Resource Tags`__.
        Example: `{\"bar-key\": \"value\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateSteeringPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSteeringPolicyDetails.
        Usage of predefined tag keys. These predefined keys are scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateSteeringPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSteeringPolicyDetails.
        Usage of predefined tag keys. These predefined keys are scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateSteeringPolicyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def answers(self):
        """
        Gets the answers of this CreateSteeringPolicyDetails.
        The set of all answers that can potentially issue from the steering policy.


        :return: The answers of this CreateSteeringPolicyDetails.
        :rtype: list[SteeringPolicyAnswer]
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        """
        Sets the answers of this CreateSteeringPolicyDetails.
        The set of all answers that can potentially issue from the steering policy.


        :param answers: The answers of this CreateSteeringPolicyDetails.
        :type: list[SteeringPolicyAnswer]
        """
        self._answers = answers

    @property
    def rules(self):
        """
        Gets the rules of this CreateSteeringPolicyDetails.
        The pipeline of rules that will be processed in sequence to reduce the pool of answers
        to a response for any given request.

        The first rule receives a shuffled list of all answers, and every other rule receives
        the list of answers emitted by the one preceding it. The last rule populates the
        response.


        :return: The rules of this CreateSteeringPolicyDetails.
        :rtype: list[SteeringPolicyRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this CreateSteeringPolicyDetails.
        The pipeline of rules that will be processed in sequence to reduce the pool of answers
        to a response for any given request.

        The first rule receives a shuffled list of all answers, and every other rule receives
        the list of answers emitted by the one preceding it. The last rule populates the
        response.


        :param rules: The rules of this CreateSteeringPolicyDetails.
        :type: list[SteeringPolicyRule]
        """
        self._rules = rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
