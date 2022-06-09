# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Apdex(object):
    """
    An Apdex configuration rule.
    The Apdex score is computed based on how the response time of a span compares to two predefined threshold values.
    The first threshold defines the maximum response time that is considered satisfactory for the end user.
    The second one defines the maximum response time that is considered tolerable. All times larger than that will
    be considered frustrating for the end user.
    An Apdex configuration rule works by selecting a subset of spans based on a filter expression and applying the
    two threshold comparisons to compute a score for each of the selected spans.
    The rule has an \"isApplyToErrorSpans\" property that controls whether or not to compute the Apdex for spans that
    have been marked as errors. If this property is set to \"true\", then the Apdex score for error spans is computed in
    the same way as for non-error ones. If set to \"false\", then computation for error spans is skipped, and the score
    is set to \"frustrating\" regardless of the configured thresholds. The default is \"false\".
    The \"isEnabled\" property controls whether or not an Apdex score is computed and can be used to disable Apdex
    score for certain spans. The default is \"true\".
    The \"priority\" property specifies the importance of the rule within a rule set.
    Lower values indicate a higher priority. Rules with higher priorities are evaluated first in the rule set. The
    priority of the rules must be unique within a rule set.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Apdex object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param filter_text:
            The value to assign to the filter_text property of this Apdex.
        :type filter_text: str

        :param priority:
            The value to assign to the priority property of this Apdex.
        :type priority: int

        :param is_enabled:
            The value to assign to the is_enabled property of this Apdex.
        :type is_enabled: bool

        :param satisfied_response_time:
            The value to assign to the satisfied_response_time property of this Apdex.
        :type satisfied_response_time: int

        :param tolerating_response_time:
            The value to assign to the tolerating_response_time property of this Apdex.
        :type tolerating_response_time: int

        :param is_apply_to_error_spans:
            The value to assign to the is_apply_to_error_spans property of this Apdex.
        :type is_apply_to_error_spans: bool

        :param display_name:
            The value to assign to the display_name property of this Apdex.
        :type display_name: str

        """
        self.swagger_types = {
            'filter_text': 'str',
            'priority': 'int',
            'is_enabled': 'bool',
            'satisfied_response_time': 'int',
            'tolerating_response_time': 'int',
            'is_apply_to_error_spans': 'bool',
            'display_name': 'str'
        }

        self.attribute_map = {
            'filter_text': 'filterText',
            'priority': 'priority',
            'is_enabled': 'isEnabled',
            'satisfied_response_time': 'satisfiedResponseTime',
            'tolerating_response_time': 'toleratingResponseTime',
            'is_apply_to_error_spans': 'isApplyToErrorSpans',
            'display_name': 'displayName'
        }

        self._filter_text = None
        self._priority = None
        self._is_enabled = None
        self._satisfied_response_time = None
        self._tolerating_response_time = None
        self._is_apply_to_error_spans = None
        self._display_name = None

    @property
    def filter_text(self):
        """
        **[Required]** Gets the filter_text of this Apdex.
        The string that defines the Span Filter expression.


        :return: The filter_text of this Apdex.
        :rtype: str
        """
        return self._filter_text

    @filter_text.setter
    def filter_text(self, filter_text):
        """
        Sets the filter_text of this Apdex.
        The string that defines the Span Filter expression.


        :param filter_text: The filter_text of this Apdex.
        :type: str
        """
        self._filter_text = filter_text

    @property
    def priority(self):
        """
        **[Required]** Gets the priority of this Apdex.
        The priority controls the order in which multiple rules in a rule set are applied. Lower values indicate higher
        priorities. Rules with higher priority are applied first, and once a match is found, the rest of the rules are
        ignored. Rules within the same rule set cannot have the same priority.


        :return: The priority of this Apdex.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this Apdex.
        The priority controls the order in which multiple rules in a rule set are applied. Lower values indicate higher
        priorities. Rules with higher priority are applied first, and once a match is found, the rest of the rules are
        ignored. Rules within the same rule set cannot have the same priority.


        :param priority: The priority of this Apdex.
        :type: int
        """
        self._priority = priority

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this Apdex.
        Specifies whether the Apdex score should be computed for spans matching the rule. This can be used to disable
        Apdex score for spans that do not need or require it. The default is \"true\".


        :return: The is_enabled of this Apdex.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this Apdex.
        Specifies whether the Apdex score should be computed for spans matching the rule. This can be used to disable
        Apdex score for spans that do not need or require it. The default is \"true\".


        :param is_enabled: The is_enabled of this Apdex.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def satisfied_response_time(self):
        """
        Gets the satisfied_response_time of this Apdex.
        The maximum response time in milliseconds that is considered \"satisfactory\" for the end user.


        :return: The satisfied_response_time of this Apdex.
        :rtype: int
        """
        return self._satisfied_response_time

    @satisfied_response_time.setter
    def satisfied_response_time(self, satisfied_response_time):
        """
        Sets the satisfied_response_time of this Apdex.
        The maximum response time in milliseconds that is considered \"satisfactory\" for the end user.


        :param satisfied_response_time: The satisfied_response_time of this Apdex.
        :type: int
        """
        self._satisfied_response_time = satisfied_response_time

    @property
    def tolerating_response_time(self):
        """
        Gets the tolerating_response_time of this Apdex.
        The maximum response time in milliseconds that is considered \"tolerable\" for the end user. A response
        time beyond this threshold is considered \"frustrating\".
        This value cannot be lower than \"satisfiedResponseTime\".


        :return: The tolerating_response_time of this Apdex.
        :rtype: int
        """
        return self._tolerating_response_time

    @tolerating_response_time.setter
    def tolerating_response_time(self, tolerating_response_time):
        """
        Sets the tolerating_response_time of this Apdex.
        The maximum response time in milliseconds that is considered \"tolerable\" for the end user. A response
        time beyond this threshold is considered \"frustrating\".
        This value cannot be lower than \"satisfiedResponseTime\".


        :param tolerating_response_time: The tolerating_response_time of this Apdex.
        :type: int
        """
        self._tolerating_response_time = tolerating_response_time

    @property
    def is_apply_to_error_spans(self):
        """
        Gets the is_apply_to_error_spans of this Apdex.
        Specifies whether an Apdex score should be computed for error spans. Setting it to \"true\" means that the Apdex
        score is computed in the usual way. Setting it to \"false\" skips the Apdex computation and sets the Apdex
        score to \"frustrating\" regardless of the configured thresholds. The default is \"false\".


        :return: The is_apply_to_error_spans of this Apdex.
        :rtype: bool
        """
        return self._is_apply_to_error_spans

    @is_apply_to_error_spans.setter
    def is_apply_to_error_spans(self, is_apply_to_error_spans):
        """
        Sets the is_apply_to_error_spans of this Apdex.
        Specifies whether an Apdex score should be computed for error spans. Setting it to \"true\" means that the Apdex
        score is computed in the usual way. Setting it to \"false\" skips the Apdex computation and sets the Apdex
        score to \"frustrating\" regardless of the configured thresholds. The default is \"false\".


        :param is_apply_to_error_spans: The is_apply_to_error_spans of this Apdex.
        :type: bool
        """
        self._is_apply_to_error_spans = is_apply_to_error_spans

    @property
    def display_name(self):
        """
        Gets the display_name of this Apdex.
        The name by which a configuration entity is displayed to the end user.


        :return: The display_name of this Apdex.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Apdex.
        The name by which a configuration entity is displayed to the end user.


        :param display_name: The display_name of this Apdex.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
