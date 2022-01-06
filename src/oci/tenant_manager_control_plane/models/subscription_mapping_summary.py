# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubscriptionMappingSummary(object):
    """
    Subscription mapping information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubscriptionMappingSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SubscriptionMappingSummary.
        :type id: str

        :param subscription_id:
            The value to assign to the subscription_id property of this SubscriptionMappingSummary.
        :type subscription_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SubscriptionMappingSummary.
        :type compartment_id: str

        :param is_explicitly_assigned:
            The value to assign to the is_explicitly_assigned property of this SubscriptionMappingSummary.
        :type is_explicitly_assigned: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SubscriptionMappingSummary.
        :type lifecycle_state: str

        :param time_terminated:
            The value to assign to the time_terminated property of this SubscriptionMappingSummary.
        :type time_terminated: datetime

        :param time_created:
            The value to assign to the time_created property of this SubscriptionMappingSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SubscriptionMappingSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'subscription_id': 'str',
            'compartment_id': 'str',
            'is_explicitly_assigned': 'bool',
            'lifecycle_state': 'str',
            'time_terminated': 'datetime',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'subscription_id': 'subscriptionId',
            'compartment_id': 'compartmentId',
            'is_explicitly_assigned': 'isExplicitlyAssigned',
            'lifecycle_state': 'lifecycleState',
            'time_terminated': 'timeTerminated',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._subscription_id = None
        self._compartment_id = None
        self._is_explicitly_assigned = None
        self._lifecycle_state = None
        self._time_terminated = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SubscriptionMappingSummary.
        OCID of the mapping between subscription and compartment identified by the tenancy.


        :return: The id of this SubscriptionMappingSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SubscriptionMappingSummary.
        OCID of the mapping between subscription and compartment identified by the tenancy.


        :param id: The id of this SubscriptionMappingSummary.
        :type: str
        """
        self._id = id

    @property
    def subscription_id(self):
        """
        **[Required]** Gets the subscription_id of this SubscriptionMappingSummary.
        OCID of the subscription.


        :return: The subscription_id of this SubscriptionMappingSummary.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this SubscriptionMappingSummary.
        OCID of the subscription.


        :param subscription_id: The subscription_id of this SubscriptionMappingSummary.
        :type: str
        """
        self._subscription_id = subscription_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SubscriptionMappingSummary.
        OCID of the compartment. Always a tenancy OCID.


        :return: The compartment_id of this SubscriptionMappingSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SubscriptionMappingSummary.
        OCID of the compartment. Always a tenancy OCID.


        :param compartment_id: The compartment_id of this SubscriptionMappingSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_explicitly_assigned(self):
        """
        **[Required]** Gets the is_explicitly_assigned of this SubscriptionMappingSummary.
        Denotes if the subscription is explicity assigned to the root compartment or tenancy.


        :return: The is_explicitly_assigned of this SubscriptionMappingSummary.
        :rtype: bool
        """
        return self._is_explicitly_assigned

    @is_explicitly_assigned.setter
    def is_explicitly_assigned(self, is_explicitly_assigned):
        """
        Sets the is_explicitly_assigned of this SubscriptionMappingSummary.
        Denotes if the subscription is explicity assigned to the root compartment or tenancy.


        :param is_explicitly_assigned: The is_explicitly_assigned of this SubscriptionMappingSummary.
        :type: bool
        """
        self._is_explicitly_assigned = is_explicitly_assigned

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SubscriptionMappingSummary.
        Lifecycle state of the subscription mapping.


        :return: The lifecycle_state of this SubscriptionMappingSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SubscriptionMappingSummary.
        Lifecycle state of the subscription mapping.


        :param lifecycle_state: The lifecycle_state of this SubscriptionMappingSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_terminated(self):
        """
        Gets the time_terminated of this SubscriptionMappingSummary.
        Date-time when subscription mapping was terminated.


        :return: The time_terminated of this SubscriptionMappingSummary.
        :rtype: datetime
        """
        return self._time_terminated

    @time_terminated.setter
    def time_terminated(self, time_terminated):
        """
        Sets the time_terminated of this SubscriptionMappingSummary.
        Date-time when subscription mapping was terminated.


        :param time_terminated: The time_terminated of this SubscriptionMappingSummary.
        :type: datetime
        """
        self._time_terminated = time_terminated

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SubscriptionMappingSummary.
        Date-time when subscription mapping was created.


        :return: The time_created of this SubscriptionMappingSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SubscriptionMappingSummary.
        Date-time when subscription mapping was created.


        :param time_created: The time_created of this SubscriptionMappingSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this SubscriptionMappingSummary.
        Date-time when subscription mapping was updated.


        :return: The time_updated of this SubscriptionMappingSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SubscriptionMappingSummary.
        Date-time when subscription mapping was updated.


        :param time_updated: The time_updated of this SubscriptionMappingSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
