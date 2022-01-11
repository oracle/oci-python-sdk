# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubscriptionSummary(object):
    """
    Summary of subscription.
    """

    #: A constant which can be used with the lifecycle_state property of a SubscriptionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SubscriptionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SubscriptionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SubscriptionSummary.
        :type id: str

        :param classic_subscription_id:
            The value to assign to the classic_subscription_id property of this SubscriptionSummary.
        :type classic_subscription_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SubscriptionSummary.
        :type compartment_id: str

        :param service_name:
            The value to assign to the service_name property of this SubscriptionSummary.
        :type service_name: str

        :param is_classic_subscription:
            The value to assign to the is_classic_subscription property of this SubscriptionSummary.
        :type is_classic_subscription: bool

        :param payment_model:
            The value to assign to the payment_model property of this SubscriptionSummary.
        :type payment_model: str

        :param region_assignment:
            The value to assign to the region_assignment property of this SubscriptionSummary.
        :type region_assignment: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SubscriptionSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param start_date:
            The value to assign to the start_date property of this SubscriptionSummary.
        :type start_date: datetime

        :param end_date:
            The value to assign to the end_date property of this SubscriptionSummary.
        :type end_date: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SubscriptionSummary.
        :type time_updated: datetime

        :param time_created:
            The value to assign to the time_created property of this SubscriptionSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'classic_subscription_id': 'str',
            'compartment_id': 'str',
            'service_name': 'str',
            'is_classic_subscription': 'bool',
            'payment_model': 'str',
            'region_assignment': 'str',
            'lifecycle_state': 'str',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'time_updated': 'datetime',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'classic_subscription_id': 'classicSubscriptionId',
            'compartment_id': 'compartmentId',
            'service_name': 'serviceName',
            'is_classic_subscription': 'isClassicSubscription',
            'payment_model': 'paymentModel',
            'region_assignment': 'regionAssignment',
            'lifecycle_state': 'lifecycleState',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'time_updated': 'timeUpdated',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._classic_subscription_id = None
        self._compartment_id = None
        self._service_name = None
        self._is_classic_subscription = None
        self._payment_model = None
        self._region_assignment = None
        self._lifecycle_state = None
        self._start_date = None
        self._end_date = None
        self._time_updated = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SubscriptionSummary.
        OCID of the subscription details for a particular root compartment or tenancy.


        :return: The id of this SubscriptionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SubscriptionSummary.
        OCID of the subscription details for a particular root compartment or tenancy.


        :param id: The id of this SubscriptionSummary.
        :type: str
        """
        self._id = id

    @property
    def classic_subscription_id(self):
        """
        **[Required]** Gets the classic_subscription_id of this SubscriptionSummary.
        Classic subscription ID.


        :return: The classic_subscription_id of this SubscriptionSummary.
        :rtype: str
        """
        return self._classic_subscription_id

    @classic_subscription_id.setter
    def classic_subscription_id(self, classic_subscription_id):
        """
        Sets the classic_subscription_id of this SubscriptionSummary.
        Classic subscription ID.


        :param classic_subscription_id: The classic_subscription_id of this SubscriptionSummary.
        :type: str
        """
        self._classic_subscription_id = classic_subscription_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SubscriptionSummary.
        OCID of the compartment. Always a tenancy OCID.


        :return: The compartment_id of this SubscriptionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SubscriptionSummary.
        OCID of the compartment. Always a tenancy OCID.


        :param compartment_id: The compartment_id of this SubscriptionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this SubscriptionSummary.
        The type of subscription, such as 'CLOUDCM', 'SAAS', 'ERP', or 'CRM'.


        :return: The service_name of this SubscriptionSummary.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this SubscriptionSummary.
        The type of subscription, such as 'CLOUDCM', 'SAAS', 'ERP', or 'CRM'.


        :param service_name: The service_name of this SubscriptionSummary.
        :type: str
        """
        self._service_name = service_name

    @property
    def is_classic_subscription(self):
        """
        Gets the is_classic_subscription of this SubscriptionSummary.
        Denotes if the subscription is from classic systems or not.


        :return: The is_classic_subscription of this SubscriptionSummary.
        :rtype: bool
        """
        return self._is_classic_subscription

    @is_classic_subscription.setter
    def is_classic_subscription(self, is_classic_subscription):
        """
        Sets the is_classic_subscription of this SubscriptionSummary.
        Denotes if the subscription is from classic systems or not.


        :param is_classic_subscription: The is_classic_subscription of this SubscriptionSummary.
        :type: bool
        """
        self._is_classic_subscription = is_classic_subscription

    @property
    def payment_model(self):
        """
        Gets the payment_model of this SubscriptionSummary.
        The pay model of the subscription, such as 'Pay as you go' or 'Monthly'.


        :return: The payment_model of this SubscriptionSummary.
        :rtype: str
        """
        return self._payment_model

    @payment_model.setter
    def payment_model(self, payment_model):
        """
        Sets the payment_model of this SubscriptionSummary.
        The pay model of the subscription, such as 'Pay as you go' or 'Monthly'.


        :param payment_model: The payment_model of this SubscriptionSummary.
        :type: str
        """
        self._payment_model = payment_model

    @property
    def region_assignment(self):
        """
        Gets the region_assignment of this SubscriptionSummary.
        Region for the subscription.


        :return: The region_assignment of this SubscriptionSummary.
        :rtype: str
        """
        return self._region_assignment

    @region_assignment.setter
    def region_assignment(self, region_assignment):
        """
        Sets the region_assignment of this SubscriptionSummary.
        Region for the subscription.


        :param region_assignment: The region_assignment of this SubscriptionSummary.
        :type: str
        """
        self._region_assignment = region_assignment

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SubscriptionSummary.
        Lifecycle state of the subscription.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SubscriptionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SubscriptionSummary.
        Lifecycle state of the subscription.


        :param lifecycle_state: The lifecycle_state of this SubscriptionSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def start_date(self):
        """
        Gets the start_date of this SubscriptionSummary.
        Subscription start time.


        :return: The start_date of this SubscriptionSummary.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this SubscriptionSummary.
        Subscription start time.


        :param start_date: The start_date of this SubscriptionSummary.
        :type: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this SubscriptionSummary.
        Subscription end time.


        :return: The end_date of this SubscriptionSummary.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this SubscriptionSummary.
        Subscription end time.


        :param end_date: The end_date of this SubscriptionSummary.
        :type: datetime
        """
        self._end_date = end_date

    @property
    def time_updated(self):
        """
        Gets the time_updated of this SubscriptionSummary.
        Date-time when subscription is updated.


        :return: The time_updated of this SubscriptionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SubscriptionSummary.
        Date-time when subscription is updated.


        :param time_updated: The time_updated of this SubscriptionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_created(self):
        """
        Gets the time_created of this SubscriptionSummary.
        Date-time when subscription is created.


        :return: The time_created of this SubscriptionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SubscriptionSummary.
        Date-time when subscription is created.


        :param time_created: The time_created of this SubscriptionSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
