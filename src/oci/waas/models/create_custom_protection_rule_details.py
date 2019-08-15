# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCustomProtectionRuleDetails(object):
    """
    The required data to create a Custom Protection rule.
    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCustomProtectionRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCustomProtectionRuleDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateCustomProtectionRuleDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateCustomProtectionRuleDetails.
        :type description: str

        :param template:
            The value to assign to the template property of this CreateCustomProtectionRuleDetails.
        :type template: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCustomProtectionRuleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCustomProtectionRuleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'template': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'template': 'template',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._template = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCustomProtectionRuleDetails.
        The `OCID`__ of the compartment in which to create the Custom Protection rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateCustomProtectionRuleDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCustomProtectionRuleDetails.
        The `OCID`__ of the compartment in which to create the Custom Protection rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateCustomProtectionRuleDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateCustomProtectionRuleDetails.
        A user-friendly name for the Custom Protection rule.


        :return: The display_name of this CreateCustomProtectionRuleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCustomProtectionRuleDetails.
        A user-friendly name for the Custom Protection rule.


        :param display_name: The display_name of this CreateCustomProtectionRuleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateCustomProtectionRuleDetails.
        A description for the Custom Protection rule.


        :return: The description of this CreateCustomProtectionRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateCustomProtectionRuleDetails.
        A description for the Custom Protection rule.


        :param description: The description of this CreateCustomProtectionRuleDetails.
        :type: str
        """
        self._description = description

    @property
    def template(self):
        """
        **[Required]** Gets the template of this CreateCustomProtectionRuleDetails.
        The template text of the Custom Protection rule. The syntax is based on ModSecurity Rule Language. Additionaly it needs to include two variables / placeholders which will be replaced during publishing.

        - **{{mode}}** - rule action, defined by user in UI, like `OFF`, `DETECT` or `BLOCK`.

        - **{{id_1}}** - unique rule ID which identifies a `SecRule`, generated by the system. Multiple IDs can be used by increasing the number of the variable for every `SecRule` defined in the template.

        *Example usage:*
          ```
          SecRule REQUEST_COOKIES \"regex matching SQL injection - part 1/2\" \\
                  \"phase:2,                                                 \\
                  msg:'Detects chained SQL injection attempts 1/2.',        \\
                  id: {{id_1}},                                             \\
                  ctl:ruleEngine={{mode}},                                  \\
                  deny\"
          SecRule REQUEST_COOKIES \"regex matching SQL injection - part 2/2\" \\
                  \"phase:2,                                                 \\
                  msg:'Detects chained SQL injection attempts 2/2.',        \\
                  id: {{id_2}},                                             \\
                  ctl:ruleEngine={{mode}},                                  \\
                  deny\"
          ```
          The example contains two `SecRules` each having distinct regex expression to match
          `Cookie` header value during second input analysis phase.
          The disruptive `deny` action takes effect only when `{{mode}}` is set to `BLOCK`.
          The message is logged either when `{{mode}}` is set to `DETECT` or `BLOCK`.


        For more information about ModSecurity's open source WAF rules, see `Mod Security's documentation`__.

        __ https://www.modsecurity.org/CRS/Documentation/making.html


        :return: The template of this CreateCustomProtectionRuleDetails.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this CreateCustomProtectionRuleDetails.
        The template text of the Custom Protection rule. The syntax is based on ModSecurity Rule Language. Additionaly it needs to include two variables / placeholders which will be replaced during publishing.

        - **{{mode}}** - rule action, defined by user in UI, like `OFF`, `DETECT` or `BLOCK`.

        - **{{id_1}}** - unique rule ID which identifies a `SecRule`, generated by the system. Multiple IDs can be used by increasing the number of the variable for every `SecRule` defined in the template.

        *Example usage:*
          ```
          SecRule REQUEST_COOKIES \"regex matching SQL injection - part 1/2\" \\
                  \"phase:2,                                                 \\
                  msg:'Detects chained SQL injection attempts 1/2.',        \\
                  id: {{id_1}},                                             \\
                  ctl:ruleEngine={{mode}},                                  \\
                  deny\"
          SecRule REQUEST_COOKIES \"regex matching SQL injection - part 2/2\" \\
                  \"phase:2,                                                 \\
                  msg:'Detects chained SQL injection attempts 2/2.',        \\
                  id: {{id_2}},                                             \\
                  ctl:ruleEngine={{mode}},                                  \\
                  deny\"
          ```
          The example contains two `SecRules` each having distinct regex expression to match
          `Cookie` header value during second input analysis phase.
          The disruptive `deny` action takes effect only when `{{mode}}` is set to `BLOCK`.
          The message is logged either when `{{mode}}` is set to `DETECT` or `BLOCK`.


        For more information about ModSecurity's open source WAF rules, see `Mod Security's documentation`__.

        __ https://www.modsecurity.org/CRS/Documentation/making.html


        :param template: The template of this CreateCustomProtectionRuleDetails.
        :type: str
        """
        self._template = template

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCustomProtectionRuleDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateCustomProtectionRuleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCustomProtectionRuleDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateCustomProtectionRuleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCustomProtectionRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateCustomProtectionRuleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCustomProtectionRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateCustomProtectionRuleDetails.
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
