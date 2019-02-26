# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeliveryPolicy(object):
    """
    The subscription delivery policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeliveryPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backoff_retry_policy:
            The value to assign to the backoff_retry_policy property of this DeliveryPolicy.
        :type backoff_retry_policy: BackoffRetryPolicy

        """
        self.swagger_types = {
            'backoff_retry_policy': 'BackoffRetryPolicy'
        }

        self.attribute_map = {
            'backoff_retry_policy': 'backoffRetryPolicy'
        }

        self._backoff_retry_policy = None

    @property
    def backoff_retry_policy(self):
        """
        Gets the backoff_retry_policy of this DeliveryPolicy.

        :return: The backoff_retry_policy of this DeliveryPolicy.
        :rtype: BackoffRetryPolicy
        """
        return self._backoff_retry_policy

    @backoff_retry_policy.setter
    def backoff_retry_policy(self, backoff_retry_policy):
        """
        Sets the backoff_retry_policy of this DeliveryPolicy.

        :param backoff_retry_policy: The backoff_retry_policy of this DeliveryPolicy.
        :type: BackoffRetryPolicy
        """
        self._backoff_retry_policy = backoff_retry_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
