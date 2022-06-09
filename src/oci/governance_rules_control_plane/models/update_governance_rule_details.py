# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateGovernanceRuleDetails(object):
    """
    Request object for UpdateGovernanceRule operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateGovernanceRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateGovernanceRuleDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateGovernanceRuleDetails.
        :type description: str

        :param template:
            The value to assign to the template property of this UpdateGovernanceRuleDetails.
        :type template: oci.governance_rules_control_plane.models.Template

        :param related_resource_id:
            The value to assign to the related_resource_id property of this UpdateGovernanceRuleDetails.
        :type related_resource_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateGovernanceRuleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateGovernanceRuleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'template': 'Template',
            'related_resource_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'template': 'template',
            'related_resource_id': 'relatedResourceId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._template = None
        self._related_resource_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateGovernanceRuleDetails.
        Display name of the governance rule.


        :return: The display_name of this UpdateGovernanceRuleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateGovernanceRuleDetails.
        Display name of the governance rule.


        :param display_name: The display_name of this UpdateGovernanceRuleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateGovernanceRuleDetails.
        Description of the governance rule.


        :return: The description of this UpdateGovernanceRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateGovernanceRuleDetails.
        Description of the governance rule.


        :param description: The description of this UpdateGovernanceRuleDetails.
        :type: str
        """
        self._description = description

    @property
    def template(self):
        """
        Gets the template of this UpdateGovernanceRuleDetails.

        :return: The template of this UpdateGovernanceRuleDetails.
        :rtype: oci.governance_rules_control_plane.models.Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this UpdateGovernanceRuleDetails.

        :param template: The template of this UpdateGovernanceRuleDetails.
        :type: oci.governance_rules_control_plane.models.Template
        """
        self._template = template

    @property
    def related_resource_id(self):
        """
        Gets the related_resource_id of this UpdateGovernanceRuleDetails.
        The Oracle ID (`OCID`__) of the resource, which was used as a template to create this governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The related_resource_id of this UpdateGovernanceRuleDetails.
        :rtype: str
        """
        return self._related_resource_id

    @related_resource_id.setter
    def related_resource_id(self, related_resource_id):
        """
        Sets the related_resource_id of this UpdateGovernanceRuleDetails.
        The Oracle ID (`OCID`__) of the resource, which was used as a template to create this governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param related_resource_id: The related_resource_id of this UpdateGovernanceRuleDetails.
        :type: str
        """
        self._related_resource_id = related_resource_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateGovernanceRuleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateGovernanceRuleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateGovernanceRuleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateGovernanceRuleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateGovernanceRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateGovernanceRuleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateGovernanceRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateGovernanceRuleDetails.
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
