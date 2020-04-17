# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnalyticsInstanceSummary(object):
    """
    Analytics Instance metadata (summary view).
    """

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstanceSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstanceSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstanceSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstanceSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstanceSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstanceSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstanceSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the feature_set property of a AnalyticsInstanceSummary.
    #: This constant has a value of "SELF_SERVICE_ANALYTICS"
    FEATURE_SET_SELF_SERVICE_ANALYTICS = "SELF_SERVICE_ANALYTICS"

    #: A constant which can be used with the feature_set property of a AnalyticsInstanceSummary.
    #: This constant has a value of "ENTERPRISE_ANALYTICS"
    FEATURE_SET_ENTERPRISE_ANALYTICS = "ENTERPRISE_ANALYTICS"

    #: A constant which can be used with the license_type property of a AnalyticsInstanceSummary.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_TYPE_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_type property of a AnalyticsInstanceSummary.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_TYPE_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new AnalyticsInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AnalyticsInstanceSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this AnalyticsInstanceSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this AnalyticsInstanceSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AnalyticsInstanceSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AnalyticsInstanceSummary.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "INACTIVE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param feature_set:
            The value to assign to the feature_set property of this AnalyticsInstanceSummary.
            Allowed values for this property are: "SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type feature_set: str

        :param capacity:
            The value to assign to the capacity property of this AnalyticsInstanceSummary.
        :type capacity: Capacity

        :param license_type:
            The value to assign to the license_type property of this AnalyticsInstanceSummary.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_type: str

        :param email_notification:
            The value to assign to the email_notification property of this AnalyticsInstanceSummary.
        :type email_notification: str

        :param service_url:
            The value to assign to the service_url property of this AnalyticsInstanceSummary.
        :type service_url: str

        :param time_created:
            The value to assign to the time_created property of this AnalyticsInstanceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AnalyticsInstanceSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'feature_set': 'str',
            'capacity': 'Capacity',
            'license_type': 'str',
            'email_notification': 'str',
            'service_url': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'feature_set': 'featureSet',
            'capacity': 'capacity',
            'license_type': 'licenseType',
            'email_notification': 'emailNotification',
            'service_url': 'serviceUrl',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._name = None
        self._description = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._feature_set = None
        self._capacity = None
        self._license_type = None
        self._email_notification = None
        self._service_url = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AnalyticsInstanceSummary.
        The resource OCID.


        :return: The id of this AnalyticsInstanceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AnalyticsInstanceSummary.
        The resource OCID.


        :param id: The id of this AnalyticsInstanceSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AnalyticsInstanceSummary.
        The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.


        :return: The name of this AnalyticsInstanceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AnalyticsInstanceSummary.
        The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.


        :param name: The name of this AnalyticsInstanceSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this AnalyticsInstanceSummary.
        Optional description.


        :return: The description of this AnalyticsInstanceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AnalyticsInstanceSummary.
        Optional description.


        :param description: The description of this AnalyticsInstanceSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AnalyticsInstanceSummary.
        The OCID of the compartment.


        :return: The compartment_id of this AnalyticsInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AnalyticsInstanceSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this AnalyticsInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AnalyticsInstanceSummary.
        The current state of an instance.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "INACTIVE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AnalyticsInstanceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AnalyticsInstanceSummary.
        The current state of an instance.


        :param lifecycle_state: The lifecycle_state of this AnalyticsInstanceSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "INACTIVE", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def feature_set(self):
        """
        **[Required]** Gets the feature_set of this AnalyticsInstanceSummary.
        Analytics feature set.

        Allowed values for this property are: "SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The feature_set of this AnalyticsInstanceSummary.
        :rtype: str
        """
        return self._feature_set

    @feature_set.setter
    def feature_set(self, feature_set):
        """
        Sets the feature_set of this AnalyticsInstanceSummary.
        Analytics feature set.


        :param feature_set: The feature_set of this AnalyticsInstanceSummary.
        :type: str
        """
        allowed_values = ["SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS"]
        if not value_allowed_none_or_none_sentinel(feature_set, allowed_values):
            feature_set = 'UNKNOWN_ENUM_VALUE'
        self._feature_set = feature_set

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this AnalyticsInstanceSummary.

        :return: The capacity of this AnalyticsInstanceSummary.
        :rtype: Capacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this AnalyticsInstanceSummary.

        :param capacity: The capacity of this AnalyticsInstanceSummary.
        :type: Capacity
        """
        self._capacity = capacity

    @property
    def license_type(self):
        """
        Gets the license_type of this AnalyticsInstanceSummary.
        The license used for the service.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_type of this AnalyticsInstanceSummary.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this AnalyticsInstanceSummary.
        The license used for the service.


        :param license_type: The license_type of this AnalyticsInstanceSummary.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_type, allowed_values):
            license_type = 'UNKNOWN_ENUM_VALUE'
        self._license_type = license_type

    @property
    def email_notification(self):
        """
        Gets the email_notification of this AnalyticsInstanceSummary.
        Email address receiving notifications.


        :return: The email_notification of this AnalyticsInstanceSummary.
        :rtype: str
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """
        Sets the email_notification of this AnalyticsInstanceSummary.
        Email address receiving notifications.


        :param email_notification: The email_notification of this AnalyticsInstanceSummary.
        :type: str
        """
        self._email_notification = email_notification

    @property
    def service_url(self):
        """
        Gets the service_url of this AnalyticsInstanceSummary.
        URL of the Analytics service.


        :return: The service_url of this AnalyticsInstanceSummary.
        :rtype: str
        """
        return self._service_url

    @service_url.setter
    def service_url(self, service_url):
        """
        Sets the service_url of this AnalyticsInstanceSummary.
        URL of the Analytics service.


        :param service_url: The service_url of this AnalyticsInstanceSummary.
        :type: str
        """
        self._service_url = service_url

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AnalyticsInstanceSummary.
        The date and time the instance was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this AnalyticsInstanceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AnalyticsInstanceSummary.
        The date and time the instance was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this AnalyticsInstanceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this AnalyticsInstanceSummary.
        The date and time the instance was last updated (in the format defined by RFC3339).
        This timestamp represents updates made through this API. External events do not
        influence it.


        :return: The time_updated of this AnalyticsInstanceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AnalyticsInstanceSummary.
        The date and time the instance was last updated (in the format defined by RFC3339).
        This timestamp represents updates made through this API. External events do not
        influence it.


        :param time_updated: The time_updated of this AnalyticsInstanceSummary.
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
