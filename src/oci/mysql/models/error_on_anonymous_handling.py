# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .anonymous_transactions_handling import AnonymousTransactionsHandling
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ErrorOnAnonymousHandling(AnonymousTransactionsHandling):
    """
    Disables assignment of IDs to anonymous transactions coming from the source. Use this policy when the transaction
    identifiers are enabled in the source of the replication channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ErrorOnAnonymousHandling object with values from keyword arguments. The default value of the :py:attr:`~oci.mysql.models.ErrorOnAnonymousHandling.policy` attribute
        of this class is ``ERROR_ON_ANONYMOUS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy:
            The value to assign to the policy property of this ErrorOnAnonymousHandling.
            Allowed values for this property are: "ERROR_ON_ANONYMOUS", "ASSIGN_TARGET_UUID", "ASSIGN_MANUAL_UUID"
        :type policy: str

        """
        self.swagger_types = {
            'policy': 'str'
        }

        self.attribute_map = {
            'policy': 'policy'
        }

        self._policy = None
        self._policy = 'ERROR_ON_ANONYMOUS'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
