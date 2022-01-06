# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApprovalPolicy(object):
    """
    Specifies the approval policy.
    """

    #: A constant which can be used with the approval_policy_type property of a ApprovalPolicy.
    #: This constant has a value of "COUNT_BASED_APPROVAL"
    APPROVAL_POLICY_TYPE_COUNT_BASED_APPROVAL = "COUNT_BASED_APPROVAL"

    def __init__(self, **kwargs):
        """
        Initializes a new ApprovalPolicy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.CountBasedApprovalPolicy`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param approval_policy_type:
            The value to assign to the approval_policy_type property of this ApprovalPolicy.
            Allowed values for this property are: "COUNT_BASED_APPROVAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type approval_policy_type: str

        """
        self.swagger_types = {
            'approval_policy_type': 'str'
        }

        self.attribute_map = {
            'approval_policy_type': 'approvalPolicyType'
        }

        self._approval_policy_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['approvalPolicyType']

        if type == 'COUNT_BASED_APPROVAL':
            return 'CountBasedApprovalPolicy'
        else:
            return 'ApprovalPolicy'

    @property
    def approval_policy_type(self):
        """
        **[Required]** Gets the approval_policy_type of this ApprovalPolicy.
        Approval policy type.

        Allowed values for this property are: "COUNT_BASED_APPROVAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The approval_policy_type of this ApprovalPolicy.
        :rtype: str
        """
        return self._approval_policy_type

    @approval_policy_type.setter
    def approval_policy_type(self, approval_policy_type):
        """
        Sets the approval_policy_type of this ApprovalPolicy.
        Approval policy type.


        :param approval_policy_type: The approval_policy_type of this ApprovalPolicy.
        :type: str
        """
        allowed_values = ["COUNT_BASED_APPROVAL"]
        if not value_allowed_none_or_none_sentinel(approval_policy_type, allowed_values):
            approval_policy_type = 'UNKNOWN_ENUM_VALUE'
        self._approval_policy_type = approval_policy_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
