# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAlertRuleDetails(object):
    """
    The create alert rule details. This is a batch-create.
    """

    #: A constant which can be used with the type property of a CreateAlertRuleDetails.
    #: This constant has a value of "ACTUAL"
    TYPE_ACTUAL = "ACTUAL"

    #: A constant which can be used with the type property of a CreateAlertRuleDetails.
    #: This constant has a value of "FORECAST"
    TYPE_FORECAST = "FORECAST"

    #: A constant which can be used with the threshold_type property of a CreateAlertRuleDetails.
    #: This constant has a value of "PERCENTAGE"
    THRESHOLD_TYPE_PERCENTAGE = "PERCENTAGE"

    #: A constant which can be used with the threshold_type property of a CreateAlertRuleDetails.
    #: This constant has a value of "ABSOLUTE"
    THRESHOLD_TYPE_ABSOLUTE = "ABSOLUTE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAlertRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateAlertRuleDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateAlertRuleDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this CreateAlertRuleDetails.
            Allowed values for this property are: "ACTUAL", "FORECAST"
        :type type: str

        :param threshold:
            The value to assign to the threshold property of this CreateAlertRuleDetails.
        :type threshold: float

        :param threshold_type:
            The value to assign to the threshold_type property of this CreateAlertRuleDetails.
            Allowed values for this property are: "PERCENTAGE", "ABSOLUTE"
        :type threshold_type: str

        :param recipients:
            The value to assign to the recipients property of this CreateAlertRuleDetails.
        :type recipients: str

        :param message:
            The value to assign to the message property of this CreateAlertRuleDetails.
        :type message: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAlertRuleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAlertRuleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'type': 'str',
            'threshold': 'float',
            'threshold_type': 'str',
            'recipients': 'str',
            'message': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'type': 'type',
            'threshold': 'threshold',
            'threshold_type': 'thresholdType',
            'recipients': 'recipients',
            'message': 'message',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._type = None
        self._threshold = None
        self._threshold_type = None
        self._recipients = None
        self._message = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAlertRuleDetails.
        The name of the alert rule.


        :return: The display_name of this CreateAlertRuleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAlertRuleDetails.
        The name of the alert rule.


        :param display_name: The display_name of this CreateAlertRuleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateAlertRuleDetails.
        The description of the alert rule.


        :return: The description of this CreateAlertRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAlertRuleDetails.
        The description of the alert rule.


        :param description: The description of this CreateAlertRuleDetails.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateAlertRuleDetails.
        Type of alert. Valid values are ACTUAL (the alert will trigger based on actual usage) or
        FORECAST (the alert will trigger based on predicted usage).

        Allowed values for this property are: "ACTUAL", "FORECAST"


        :return: The type of this CreateAlertRuleDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateAlertRuleDetails.
        Type of alert. Valid values are ACTUAL (the alert will trigger based on actual usage) or
        FORECAST (the alert will trigger based on predicted usage).


        :param type: The type of this CreateAlertRuleDetails.
        :type: str
        """
        allowed_values = ["ACTUAL", "FORECAST"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def threshold(self):
        """
        **[Required]** Gets the threshold of this CreateAlertRuleDetails.
        The threshold for triggering the alert expressed as a whole number or decimal value.
        If thresholdType is ABSOLUTE, threshold can have at most 12 digits before the decimal point and up to 2 digits after the decimal point.
        If thresholdType is PERCENTAGE, the maximum value is 10000 and can have up to 2 digits after the decimal point.


        :return: The threshold of this CreateAlertRuleDetails.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """
        Sets the threshold of this CreateAlertRuleDetails.
        The threshold for triggering the alert expressed as a whole number or decimal value.
        If thresholdType is ABSOLUTE, threshold can have at most 12 digits before the decimal point and up to 2 digits after the decimal point.
        If thresholdType is PERCENTAGE, the maximum value is 10000 and can have up to 2 digits after the decimal point.


        :param threshold: The threshold of this CreateAlertRuleDetails.
        :type: float
        """
        self._threshold = threshold

    @property
    def threshold_type(self):
        """
        **[Required]** Gets the threshold_type of this CreateAlertRuleDetails.
        The type of threshold.

        Allowed values for this property are: "PERCENTAGE", "ABSOLUTE"


        :return: The threshold_type of this CreateAlertRuleDetails.
        :rtype: str
        """
        return self._threshold_type

    @threshold_type.setter
    def threshold_type(self, threshold_type):
        """
        Sets the threshold_type of this CreateAlertRuleDetails.
        The type of threshold.


        :param threshold_type: The threshold_type of this CreateAlertRuleDetails.
        :type: str
        """
        allowed_values = ["PERCENTAGE", "ABSOLUTE"]
        if not value_allowed_none_or_none_sentinel(threshold_type, allowed_values):
            raise ValueError(
                "Invalid value for `threshold_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._threshold_type = threshold_type

    @property
    def recipients(self):
        """
        Gets the recipients of this CreateAlertRuleDetails.
        The audience that will receive the alert when it triggers. An empty string is interpreted as null.


        :return: The recipients of this CreateAlertRuleDetails.
        :rtype: str
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this CreateAlertRuleDetails.
        The audience that will receive the alert when it triggers. An empty string is interpreted as null.


        :param recipients: The recipients of this CreateAlertRuleDetails.
        :type: str
        """
        self._recipients = recipients

    @property
    def message(self):
        """
        Gets the message of this CreateAlertRuleDetails.
        The message to be sent to the recipients when alert rule is triggered.


        :return: The message of this CreateAlertRuleDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CreateAlertRuleDetails.
        The message to be sent to the recipients when alert rule is triggered.


        :param message: The message of this CreateAlertRuleDetails.
        :type: str
        """
        self._message = message

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAlertRuleDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAlertRuleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAlertRuleDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAlertRuleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAlertRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAlertRuleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAlertRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAlertRuleDetails.
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
