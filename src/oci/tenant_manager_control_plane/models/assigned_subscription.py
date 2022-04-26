# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssignedSubscription(object):
    """
    Assigned subscription information.
    """

    #: A constant which can be used with the lifecycle_state property of a AssignedSubscription.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AssignedSubscription.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AssignedSubscription.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AssignedSubscription.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AssignedSubscription.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AssignedSubscription.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AssignedSubscription.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AssignedSubscription object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AssignedSubscription.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AssignedSubscription.
        :type compartment_id: str

        :param classic_subscription_id:
            The value to assign to the classic_subscription_id property of this AssignedSubscription.
        :type classic_subscription_id: str

        :param service_name:
            The value to assign to the service_name property of this AssignedSubscription.
        :type service_name: str

        :param is_classic_subscription:
            The value to assign to the is_classic_subscription property of this AssignedSubscription.
        :type is_classic_subscription: bool

        :param region_assignment:
            The value to assign to the region_assignment property of this AssignedSubscription.
        :type region_assignment: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AssignedSubscription.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param skus:
            The value to assign to the skus property of this AssignedSubscription.
        :type skus: list[oci.tenant_manager_control_plane.models.SubscriptionSku]

        :param order_ids:
            The value to assign to the order_ids property of this AssignedSubscription.
        :type order_ids: list[str]

        :param start_date:
            The value to assign to the start_date property of this AssignedSubscription.
        :type start_date: datetime

        :param end_date:
            The value to assign to the end_date property of this AssignedSubscription.
        :type end_date: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AssignedSubscription.
        :type time_updated: datetime

        :param time_created:
            The value to assign to the time_created property of this AssignedSubscription.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'classic_subscription_id': 'str',
            'service_name': 'str',
            'is_classic_subscription': 'bool',
            'region_assignment': 'str',
            'lifecycle_state': 'str',
            'skus': 'list[SubscriptionSku]',
            'order_ids': 'list[str]',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'time_updated': 'datetime',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'classic_subscription_id': 'classicSubscriptionId',
            'service_name': 'serviceName',
            'is_classic_subscription': 'isClassicSubscription',
            'region_assignment': 'regionAssignment',
            'lifecycle_state': 'lifecycleState',
            'skus': 'skus',
            'order_ids': 'orderIds',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'time_updated': 'timeUpdated',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._compartment_id = None
        self._classic_subscription_id = None
        self._service_name = None
        self._is_classic_subscription = None
        self._region_assignment = None
        self._lifecycle_state = None
        self._skus = None
        self._order_ids = None
        self._start_date = None
        self._end_date = None
        self._time_updated = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AssignedSubscription.
        OCID of the subscription.


        :return: The id of this AssignedSubscription.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssignedSubscription.
        OCID of the subscription.


        :param id: The id of this AssignedSubscription.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AssignedSubscription.
        OCID of the compartment. Always a tenancy OCID.


        :return: The compartment_id of this AssignedSubscription.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AssignedSubscription.
        OCID of the compartment. Always a tenancy OCID.


        :param compartment_id: The compartment_id of this AssignedSubscription.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def classic_subscription_id(self):
        """
        **[Required]** Gets the classic_subscription_id of this AssignedSubscription.
        Subscription ID.


        :return: The classic_subscription_id of this AssignedSubscription.
        :rtype: str
        """
        return self._classic_subscription_id

    @classic_subscription_id.setter
    def classic_subscription_id(self, classic_subscription_id):
        """
        Sets the classic_subscription_id of this AssignedSubscription.
        Subscription ID.


        :param classic_subscription_id: The classic_subscription_id of this AssignedSubscription.
        :type: str
        """
        self._classic_subscription_id = classic_subscription_id

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this AssignedSubscription.
        The type of subscription, such as 'CLOUDCM', 'SAAS', 'ERP', or 'CRM'.


        :return: The service_name of this AssignedSubscription.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this AssignedSubscription.
        The type of subscription, such as 'CLOUDCM', 'SAAS', 'ERP', or 'CRM'.


        :param service_name: The service_name of this AssignedSubscription.
        :type: str
        """
        self._service_name = service_name

    @property
    def is_classic_subscription(self):
        """
        Gets the is_classic_subscription of this AssignedSubscription.
        Denotes if the subscription is legacy or not.


        :return: The is_classic_subscription of this AssignedSubscription.
        :rtype: bool
        """
        return self._is_classic_subscription

    @is_classic_subscription.setter
    def is_classic_subscription(self, is_classic_subscription):
        """
        Sets the is_classic_subscription of this AssignedSubscription.
        Denotes if the subscription is legacy or not.


        :param is_classic_subscription: The is_classic_subscription of this AssignedSubscription.
        :type: bool
        """
        self._is_classic_subscription = is_classic_subscription

    @property
    def region_assignment(self):
        """
        Gets the region_assignment of this AssignedSubscription.
        Region for the subscription.


        :return: The region_assignment of this AssignedSubscription.
        :rtype: str
        """
        return self._region_assignment

    @region_assignment.setter
    def region_assignment(self, region_assignment):
        """
        Sets the region_assignment of this AssignedSubscription.
        Region for the subscription.


        :param region_assignment: The region_assignment of this AssignedSubscription.
        :type: str
        """
        self._region_assignment = region_assignment

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AssignedSubscription.
        Lifecycle state of the subscription.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AssignedSubscription.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AssignedSubscription.
        Lifecycle state of the subscription.


        :param lifecycle_state: The lifecycle_state of this AssignedSubscription.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def skus(self):
        """
        Gets the skus of this AssignedSubscription.
        List of SKUs linked to the subscription.


        :return: The skus of this AssignedSubscription.
        :rtype: list[oci.tenant_manager_control_plane.models.SubscriptionSku]
        """
        return self._skus

    @skus.setter
    def skus(self, skus):
        """
        Sets the skus of this AssignedSubscription.
        List of SKUs linked to the subscription.


        :param skus: The skus of this AssignedSubscription.
        :type: list[oci.tenant_manager_control_plane.models.SubscriptionSku]
        """
        self._skus = skus

    @property
    def order_ids(self):
        """
        Gets the order_ids of this AssignedSubscription.
        List of subscription order OCIDs that contributed to this subscription.


        :return: The order_ids of this AssignedSubscription.
        :rtype: list[str]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        """
        Sets the order_ids of this AssignedSubscription.
        List of subscription order OCIDs that contributed to this subscription.


        :param order_ids: The order_ids of this AssignedSubscription.
        :type: list[str]
        """
        self._order_ids = order_ids

    @property
    def start_date(self):
        """
        Gets the start_date of this AssignedSubscription.
        Subscription start time.


        :return: The start_date of this AssignedSubscription.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this AssignedSubscription.
        Subscription start time.


        :param start_date: The start_date of this AssignedSubscription.
        :type: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this AssignedSubscription.
        Subscription end time.


        :return: The end_date of this AssignedSubscription.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this AssignedSubscription.
        Subscription end time.


        :param end_date: The end_date of this AssignedSubscription.
        :type: datetime
        """
        self._end_date = end_date

    @property
    def time_updated(self):
        """
        Gets the time_updated of this AssignedSubscription.
        Date-time when subscription is updated.


        :return: The time_updated of this AssignedSubscription.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AssignedSubscription.
        Date-time when subscription is updated.


        :param time_updated: The time_updated of this AssignedSubscription.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_created(self):
        """
        Gets the time_created of this AssignedSubscription.
        Date-time when subscription is created.


        :return: The time_created of this AssignedSubscription.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AssignedSubscription.
        Date-time when subscription is created.


        :param time_created: The time_created of this AssignedSubscription.
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
