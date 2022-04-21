# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCaptureFilterDetails(object):
    """
    These details can be included in a request to update a capture filter. A capture filter contains a set of rules governing what traffic a VTAP mirrors.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCaptureFilterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateCaptureFilterDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateCaptureFilterDetails.
        :type display_name: str

        :param vtap_capture_filter_rules:
            The value to assign to the vtap_capture_filter_rules property of this UpdateCaptureFilterDetails.
        :type vtap_capture_filter_rules: list[oci.core.models.VtapCaptureFilterRuleDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateCaptureFilterDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'vtap_capture_filter_rules': 'list[VtapCaptureFilterRuleDetails]',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'vtap_capture_filter_rules': 'vtapCaptureFilterRules',
            'freeform_tags': 'freeformTags'
        }

        self._defined_tags = None
        self._display_name = None
        self._vtap_capture_filter_rules = None
        self._freeform_tags = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateCaptureFilterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateCaptureFilterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateCaptureFilterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateCaptureFilterDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateCaptureFilterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateCaptureFilterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateCaptureFilterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateCaptureFilterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def vtap_capture_filter_rules(self):
        """
        Gets the vtap_capture_filter_rules of this UpdateCaptureFilterDetails.
        The set of rules governing what traffic a VTAP mirrors.


        :return: The vtap_capture_filter_rules of this UpdateCaptureFilterDetails.
        :rtype: list[oci.core.models.VtapCaptureFilterRuleDetails]
        """
        return self._vtap_capture_filter_rules

    @vtap_capture_filter_rules.setter
    def vtap_capture_filter_rules(self, vtap_capture_filter_rules):
        """
        Sets the vtap_capture_filter_rules of this UpdateCaptureFilterDetails.
        The set of rules governing what traffic a VTAP mirrors.


        :param vtap_capture_filter_rules: The vtap_capture_filter_rules of this UpdateCaptureFilterDetails.
        :type: list[oci.core.models.VtapCaptureFilterRuleDetails]
        """
        self._vtap_capture_filter_rules = vtap_capture_filter_rules

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateCaptureFilterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateCaptureFilterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateCaptureFilterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateCaptureFilterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
