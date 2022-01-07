# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ThreatFeedAction(object):
    """
    The action to take for a request that has been determined to be potentially malicious.
    """

    #: A constant which can be used with the action property of a ThreatFeedAction.
    #: This constant has a value of "OFF"
    ACTION_OFF = "OFF"

    #: A constant which can be used with the action property of a ThreatFeedAction.
    #: This constant has a value of "DETECT"
    ACTION_DETECT = "DETECT"

    #: A constant which can be used with the action property of a ThreatFeedAction.
    #: This constant has a value of "BLOCK"
    ACTION_BLOCK = "BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new ThreatFeedAction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ThreatFeedAction.
        :type key: str

        :param action:
            The value to assign to the action property of this ThreatFeedAction.
            Allowed values for this property are: "OFF", "DETECT", "BLOCK"
        :type action: str

        """
        self.swagger_types = {
            'key': 'str',
            'action': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'action': 'action'
        }

        self._key = None
        self._action = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this ThreatFeedAction.
        The unique key of the object for which the action applies.


        :return: The key of this ThreatFeedAction.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ThreatFeedAction.
        The unique key of the object for which the action applies.


        :param key: The key of this ThreatFeedAction.
        :type: str
        """
        self._key = key

    @property
    def action(self):
        """
        **[Required]** Gets the action of this ThreatFeedAction.
        The selected action. If unspecified, defaults to `OFF`.

        Allowed values for this property are: "OFF", "DETECT", "BLOCK"


        :return: The action of this ThreatFeedAction.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ThreatFeedAction.
        The selected action. If unspecified, defaults to `OFF`.


        :param action: The action of this ThreatFeedAction.
        :type: str
        """
        allowed_values = ["OFF", "DETECT", "BLOCK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            raise ValueError(
                "Invalid value for `action`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
