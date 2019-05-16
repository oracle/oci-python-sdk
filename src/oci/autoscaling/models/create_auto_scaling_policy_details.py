# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutoScalingPolicyDetails(object):
    """
    Creation details for an autoscaling policy.

    Each autoscaling configuration can have one autoscaling policy.

    In a threshold-based autoscaling policy, an autoscaling action is triggered when a performance metric meets
    or exceeds a threshold.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutoScalingPolicyDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.autoscaling.models.CreateThresholdPolicyDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity:
            The value to assign to the capacity property of this CreateAutoScalingPolicyDetails.
        :type capacity: Capacity

        :param display_name:
            The value to assign to the display_name property of this CreateAutoScalingPolicyDetails.
        :type display_name: str

        :param policy_type:
            The value to assign to the policy_type property of this CreateAutoScalingPolicyDetails.
        :type policy_type: str

        """
        self.swagger_types = {
            'capacity': 'Capacity',
            'display_name': 'str',
            'policy_type': 'str'
        }

        self.attribute_map = {
            'capacity': 'capacity',
            'display_name': 'displayName',
            'policy_type': 'policyType'
        }

        self._capacity = None
        self._display_name = None
        self._policy_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['policyType']

        if type == 'threshold':
            return 'CreateThresholdPolicyDetails'
        else:
            return 'CreateAutoScalingPolicyDetails'

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this CreateAutoScalingPolicyDetails.
        The capacity requirements of the autoscaling policy.


        :return: The capacity of this CreateAutoScalingPolicyDetails.
        :rtype: Capacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this CreateAutoScalingPolicyDetails.
        The capacity requirements of the autoscaling policy.


        :param capacity: The capacity of this CreateAutoScalingPolicyDetails.
        :type: Capacity
        """
        self._capacity = capacity

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAutoScalingPolicyDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateAutoScalingPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAutoScalingPolicyDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateAutoScalingPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this CreateAutoScalingPolicyDetails.
        The type of autoscaling policy.


        :return: The policy_type of this CreateAutoScalingPolicyDetails.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this CreateAutoScalingPolicyDetails.
        The type of autoscaling policy.


        :param policy_type: The policy_type of this CreateAutoScalingPolicyDetails.
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
