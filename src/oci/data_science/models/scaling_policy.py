# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScalingPolicy(object):
    """
    The scaling policy to apply to each model of the deployment.
    """

    #: A constant which can be used with the policy_type property of a ScalingPolicy.
    #: This constant has a value of "FIXED_SIZE"
    POLICY_TYPE_FIXED_SIZE = "FIXED_SIZE"

    def __init__(self, **kwargs):
        """
        Initializes a new ScalingPolicy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_science.models.FixedSizeScalingPolicy`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this ScalingPolicy.
            Allowed values for this property are: "FIXED_SIZE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type policy_type: str

        """
        self.swagger_types = {
            'policy_type': 'str'
        }

        self.attribute_map = {
            'policy_type': 'policyType'
        }

        self._policy_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['policyType']

        if type == 'FIXED_SIZE':
            return 'FixedSizeScalingPolicy'
        else:
            return 'ScalingPolicy'

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this ScalingPolicy.
        The type of scaling policy.

        Allowed values for this property are: "FIXED_SIZE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The policy_type of this ScalingPolicy.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this ScalingPolicy.
        The type of scaling policy.


        :param policy_type: The policy_type of this ScalingPolicy.
        :type: str
        """
        allowed_values = ["FIXED_SIZE"]
        if not value_allowed_none_or_none_sentinel(policy_type, allowed_values):
            policy_type = 'UNKNOWN_ENUM_VALUE'
        self._policy_type = policy_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
