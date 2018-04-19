# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDynamicGroupDetails(object):
    """
    Properties for updating a dynamic group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDynamicGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateDynamicGroupDetails.
        :type description: str

        :param matching_rule:
            The value to assign to the matching_rule property of this UpdateDynamicGroupDetails.
        :type matching_rule: str

        """
        self.swagger_types = {
            'description': 'str',
            'matching_rule': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'matching_rule': 'matchingRule'
        }

        self._description = None
        self._matching_rule = None

    @property
    def description(self):
        """
        Gets the description of this UpdateDynamicGroupDetails.
        The description you assign to the dynamic group. Does not have to be unique, and it's changeable.


        :return: The description of this UpdateDynamicGroupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDynamicGroupDetails.
        The description you assign to the dynamic group. Does not have to be unique, and it's changeable.


        :param description: The description of this UpdateDynamicGroupDetails.
        :type: str
        """
        self._description = description

    @property
    def matching_rule(self):
        """
        Gets the matching_rule of this UpdateDynamicGroupDetails.
        The matching rule to dynamically match an instance certificate to this dynamic group.
        For rule syntax, see `Managing Dynamic Groups`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingdynamicgroups.htm


        :return: The matching_rule of this UpdateDynamicGroupDetails.
        :rtype: str
        """
        return self._matching_rule

    @matching_rule.setter
    def matching_rule(self, matching_rule):
        """
        Sets the matching_rule of this UpdateDynamicGroupDetails.
        The matching rule to dynamically match an instance certificate to this dynamic group.
        For rule syntax, see `Managing Dynamic Groups`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingdynamicgroups.htm


        :param matching_rule: The matching_rule of this UpdateDynamicGroupDetails.
        :type: str
        """
        self._matching_rule = matching_rule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
