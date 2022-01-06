# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubscriptionMapping(object):
    """
    Subscription mapping information.
    """

    #: A constant which can be used with the lifecycle_state property of a SubscriptionMapping.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionMapping.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionMapping.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionMapping.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionMapping.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionMapping.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionMapping.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SubscriptionMapping object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SubscriptionMapping.
        :type id: str

        :param subscription_id:
            The value to assign to the subscription_id property of this SubscriptionMapping.
        :type subscription_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SubscriptionMapping.
        :type compartment_id: str

        :param is_explicitly_assigned:
            The value to assign to the is_explicitly_assigned property of this SubscriptionMapping.
        :type is_explicitly_assigned: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SubscriptionMapping.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_terminated:
            The value to assign to the time_terminated property of this SubscriptionMapping.
        :type time_terminated: datetime

        :param time_created:
            The value to assign to the time_created property of this SubscriptionMapping.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SubscriptionMapping.
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
        **[Required]** Gets the id of this SubscriptionMapping.
        OCID of the mapping between subscription and compartment identified by the tenancy.


        :return: The id of this SubscriptionMapping.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SubscriptionMapping.
        OCID of the mapping between subscription and compartment identified by the tenancy.


        :param id: The id of this SubscriptionMapping.
        :type: str
        """
        self._id = id

    @property
    def subscription_id(self):
        """
        **[Required]** Gets the subscription_id of this SubscriptionMapping.
        OCID of the subscription.


        :return: The subscription_id of this SubscriptionMapping.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this SubscriptionMapping.
        OCID of the subscription.


        :param subscription_id: The subscription_id of this SubscriptionMapping.
        :type: str
        """
        self._subscription_id = subscription_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SubscriptionMapping.
        OCID of the compartment. Always a tenancy OCID.


        :return: The compartment_id of this SubscriptionMapping.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SubscriptionMapping.
        OCID of the compartment. Always a tenancy OCID.


        :param compartment_id: The compartment_id of this SubscriptionMapping.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_explicitly_assigned(self):
        """
        **[Required]** Gets the is_explicitly_assigned of this SubscriptionMapping.
        Denotes if the subscription is explicity assigned to the root compartment or tenancy.


        :return: The is_explicitly_assigned of this SubscriptionMapping.
        :rtype: bool
        """
        return self._is_explicitly_assigned

    @is_explicitly_assigned.setter
    def is_explicitly_assigned(self, is_explicitly_assigned):
        """
        Sets the is_explicitly_assigned of this SubscriptionMapping.
        Denotes if the subscription is explicity assigned to the root compartment or tenancy.


        :param is_explicitly_assigned: The is_explicitly_assigned of this SubscriptionMapping.
        :type: bool
        """
        self._is_explicitly_assigned = is_explicitly_assigned

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SubscriptionMapping.
        Lifecycle state of the subscription mapping.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SubscriptionMapping.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SubscriptionMapping.
        Lifecycle state of the subscription mapping.


        :param lifecycle_state: The lifecycle_state of this SubscriptionMapping.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_terminated(self):
        """
        Gets the time_terminated of this SubscriptionMapping.
        Date-time when subscription mapping was terminated.


        :return: The time_terminated of this SubscriptionMapping.
        :rtype: datetime
        """
        return self._time_terminated

    @time_terminated.setter
    def time_terminated(self, time_terminated):
        """
        Sets the time_terminated of this SubscriptionMapping.
        Date-time when subscription mapping was terminated.


        :param time_terminated: The time_terminated of this SubscriptionMapping.
        :type: datetime
        """
        self._time_terminated = time_terminated

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SubscriptionMapping.
        Date-time when subscription mapping was created.


        :return: The time_created of this SubscriptionMapping.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SubscriptionMapping.
        Date-time when subscription mapping was created.


        :param time_created: The time_created of this SubscriptionMapping.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this SubscriptionMapping.
        Date-time when subscription mapping was updated.


        :return: The time_updated of this SubscriptionMapping.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SubscriptionMapping.
        Date-time when subscription mapping was updated.


        :param time_updated: The time_updated of this SubscriptionMapping.
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
