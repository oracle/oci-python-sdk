# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomProtectionRuleSetting(object):
    """
    The OCID and action of a custom protection rule.
    """

    #: A constant which can be used with the action property of a CustomProtectionRuleSetting.
    #: This constant has a value of "DETECT"
    ACTION_DETECT = "DETECT"

    #: A constant which can be used with the action property of a CustomProtectionRuleSetting.
    #: This constant has a value of "BLOCK"
    ACTION_BLOCK = "BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new CustomProtectionRuleSetting object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CustomProtectionRuleSetting.
        :type id: str

        :param action:
            The value to assign to the action property of this CustomProtectionRuleSetting.
            Allowed values for this property are: "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        """
        self.swagger_types = {
            'id': 'str',
            'action': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'action': 'action'
        }

        self._id = None
        self._action = None

    @property
    def id(self):
        """
        Gets the id of this CustomProtectionRuleSetting.
        The `OCID`__ of the custom protection rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this CustomProtectionRuleSetting.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomProtectionRuleSetting.
        The `OCID`__ of the custom protection rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this CustomProtectionRuleSetting.
        :type: str
        """
        self._id = id

    @property
    def action(self):
        """
        Gets the action of this CustomProtectionRuleSetting.
        The action to take when the custom protection rule is triggered.
        `DETECT` - Logs the request when the criteria of the custom protection rule are met. `BLOCK` - Blocks the request when the criteria of the custom protection rule are met.

        Allowed values for this property are: "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this CustomProtectionRuleSetting.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this CustomProtectionRuleSetting.
        The action to take when the custom protection rule is triggered.
        `DETECT` - Logs the request when the criteria of the custom protection rule are met. `BLOCK` - Blocks the request when the criteria of the custom protection rule are met.


        :param action: The action of this CustomProtectionRuleSetting.
        :type: str
        """
        allowed_values = ["DETECT", "BLOCK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
