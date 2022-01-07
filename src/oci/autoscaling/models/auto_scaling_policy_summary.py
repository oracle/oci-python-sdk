# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


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

        :param is_enabled:
            The value to assign to the is_enabled property of this AutoScalingPolicySummary.
        :type is_enabled: bool

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'policy_type': 'str',
            'is_enabled': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'policy_type': 'policyType',
            'is_enabled': 'isEnabled'
        }

        self._id = None
        self._display_name = None
        self._policy_type = None
        self._is_enabled = None

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

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this AutoScalingPolicySummary.
        Whether the autoscaling policy is enabled.


        :return: The is_enabled of this AutoScalingPolicySummary.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AutoScalingPolicySummary.
        Whether the autoscaling policy is enabled.


        :param is_enabled: The is_enabled of this AutoScalingPolicySummary.
        :type: bool
        """
        self._is_enabled = is_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
