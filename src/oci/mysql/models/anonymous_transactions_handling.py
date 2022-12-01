# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnonymousTransactionsHandling(object):
    """
    Specifies how the replication channel handles replicated transactions without an identifier, enabling replication
    from a source that does not use transaction-id-based replication to a replica that does.
    """

    #: A constant which can be used with the policy property of a AnonymousTransactionsHandling.
    #: This constant has a value of "ERROR_ON_ANONYMOUS"
    POLICY_ERROR_ON_ANONYMOUS = "ERROR_ON_ANONYMOUS"

    #: A constant which can be used with the policy property of a AnonymousTransactionsHandling.
    #: This constant has a value of "ASSIGN_TARGET_UUID"
    POLICY_ASSIGN_TARGET_UUID = "ASSIGN_TARGET_UUID"

    #: A constant which can be used with the policy property of a AnonymousTransactionsHandling.
    #: This constant has a value of "ASSIGN_MANUAL_UUID"
    POLICY_ASSIGN_MANUAL_UUID = "ASSIGN_MANUAL_UUID"

    def __init__(self, **kwargs):
        """
        Initializes a new AnonymousTransactionsHandling object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.mysql.models.ErrorOnAnonymousHandling`
        * :class:`~oci.mysql.models.AssignManualUuidHandling`
        * :class:`~oci.mysql.models.AssignTargetUuidHandling`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy:
            The value to assign to the policy property of this AnonymousTransactionsHandling.
            Allowed values for this property are: "ERROR_ON_ANONYMOUS", "ASSIGN_TARGET_UUID", "ASSIGN_MANUAL_UUID", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type policy: str

        """
        self.swagger_types = {
            'policy': 'str'
        }

        self.attribute_map = {
            'policy': 'policy'
        }

        self._policy = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['policy']

        if type == 'ERROR_ON_ANONYMOUS':
            return 'ErrorOnAnonymousHandling'

        if type == 'ASSIGN_MANUAL_UUID':
            return 'AssignManualUuidHandling'

        if type == 'ASSIGN_TARGET_UUID':
            return 'AssignTargetUuidHandling'
        else:
            return 'AnonymousTransactionsHandling'

    @property
    def policy(self):
        """
        **[Required]** Gets the policy of this AnonymousTransactionsHandling.
        Specifies how the replication channel handles anonymous transactions.

        Allowed values for this property are: "ERROR_ON_ANONYMOUS", "ASSIGN_TARGET_UUID", "ASSIGN_MANUAL_UUID", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The policy of this AnonymousTransactionsHandling.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this AnonymousTransactionsHandling.
        Specifies how the replication channel handles anonymous transactions.


        :param policy: The policy of this AnonymousTransactionsHandling.
        :type: str
        """
        allowed_values = ["ERROR_ON_ANONYMOUS", "ASSIGN_TARGET_UUID", "ASSIGN_MANUAL_UUID"]
        if not value_allowed_none_or_none_sentinel(policy, allowed_values):
            policy = 'UNKNOWN_ENUM_VALUE'
        self._policy = policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
