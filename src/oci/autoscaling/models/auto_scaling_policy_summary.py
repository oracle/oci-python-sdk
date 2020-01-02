# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalingPolicySummary(object):
    """
    Summary information for an autoscaling policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalingPolicySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutoScalingPolicySummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AutoScalingPolicySummary.
        :type display_name: str

        :param policy_type:
            The value to assign to the policy_type property of this AutoScalingPolicySummary.
        :type policy_type: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'policy_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'policy_type': 'policyType'
        }

        self._id = None
        self._display_name = None
        self._policy_type = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutoScalingPolicySummary.
        The ID of the autoscaling policy that is assigned after creation.


        :return: The id of this AutoScalingPolicySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutoScalingPolicySummary.
        The ID of the autoscaling policy that is assigned after creation.


        :param id: The id of this AutoScalingPolicySummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this AutoScalingPolicySummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this AutoScalingPolicySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutoScalingPolicySummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this AutoScalingPolicySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this AutoScalingPolicySummary.
        The type of autoscaling policy.


        :return: The policy_type of this AutoScalingPolicySummary.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this AutoScalingPolicySummary.
        The type of autoscaling policy.


        :param policy_type: The policy_type of this AutoScalingPolicySummary.
        :type: str
        """
        self._policy_type = policy_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
