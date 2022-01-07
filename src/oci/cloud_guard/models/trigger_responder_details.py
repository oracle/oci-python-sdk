# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TriggerResponderDetails(object):
    """
    The Responder details to be pushed to responder
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TriggerResponderDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param responder_rule_id:
            The value to assign to the responder_rule_id property of this TriggerResponderDetails.
        :type responder_rule_id: str

        :param configurations:
            The value to assign to the configurations property of this TriggerResponderDetails.
        :type configurations: list[oci.cloud_guard.models.ResponderConfiguration]

        """
        self.swagger_types = {
            'responder_rule_id': 'str',
            'configurations': 'list[ResponderConfiguration]'
        }

        self.attribute_map = {
            'responder_rule_id': 'responderRuleId',
            'configurations': 'configurations'
        }

        self._responder_rule_id = None
        self._configurations = None

    @property
    def responder_rule_id(self):
        """
        **[Required]** Gets the responder_rule_id of this TriggerResponderDetails.
        ResponderRule ID


        :return: The responder_rule_id of this TriggerResponderDetails.
        :rtype: str
        """
        return self._responder_rule_id

    @responder_rule_id.setter
    def responder_rule_id(self, responder_rule_id):
        """
        Sets the responder_rule_id of this TriggerResponderDetails.
        ResponderRule ID


        :param responder_rule_id: The responder_rule_id of this TriggerResponderDetails.
        :type: str
        """
        self._responder_rule_id = responder_rule_id

    @property
    def configurations(self):
        """
        Gets the configurations of this TriggerResponderDetails.
        ResponderRule configurations


        :return: The configurations of this TriggerResponderDetails.
        :rtype: list[oci.cloud_guard.models.ResponderConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this TriggerResponderDetails.
        ResponderRule configurations


        :param configurations: The configurations of this TriggerResponderDetails.
        :type: list[oci.cloud_guard.models.ResponderConfiguration]
        """
        self._configurations = configurations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
