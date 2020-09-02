# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsEntityTypeSummary(object):
    """
    Summary of an log analytics entity type.
    """

    #: A constant which can be used with the cloud_type property of a LogAnalyticsEntityTypeSummary.
    #: This constant has a value of "CLOUD"
    CLOUD_TYPE_CLOUD = "CLOUD"

    #: A constant which can be used with the cloud_type property of a LogAnalyticsEntityTypeSummary.
    #: This constant has a value of "NON_CLOUD"
    CLOUD_TYPE_NON_CLOUD = "NON_CLOUD"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsEntityTypeSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsEntityTypeSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsEntityTypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this LogAnalyticsEntityTypeSummary.
        :type name: str

        :param internal_name:
            The value to assign to the internal_name property of this LogAnalyticsEntityTypeSummary.
        :type internal_name: str

        :param category:
            The value to assign to the category property of this LogAnalyticsEntityTypeSummary.
        :type category: str

        :param cloud_type:
            The value to assign to the cloud_type property of this LogAnalyticsEntityTypeSummary.
            Allowed values for this property are: "CLOUD", "NON_CLOUD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type cloud_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LogAnalyticsEntityTypeSummary.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this LogAnalyticsEntityTypeSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this LogAnalyticsEntityTypeSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'internal_name': 'str',
            'category': 'str',
            'cloud_type': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'internal_name': 'internalName',
            'category': 'category',
            'cloud_type': 'cloudType',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._name = None
        self._internal_name = None
        self._category = None
        self._cloud_type = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this LogAnalyticsEntityTypeSummary.
        Log analytics entity type name.


        :return: The name of this LogAnalyticsEntityTypeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsEntityTypeSummary.
        Log analytics entity type name.


        :param name: The name of this LogAnalyticsEntityTypeSummary.
        :type: str
        """
        self._name = name

    @property
    def internal_name(self):
        """
        **[Required]** Gets the internal_name of this LogAnalyticsEntityTypeSummary.
        Internal name for the log analytics entity type.


        :return: The internal_name of this LogAnalyticsEntityTypeSummary.
        :rtype: str
        """
        return self._internal_name

    @internal_name.setter
    def internal_name(self, internal_name):
        """
        Sets the internal_name of this LogAnalyticsEntityTypeSummary.
        Internal name for the log analytics entity type.


        :param internal_name: The internal_name of this LogAnalyticsEntityTypeSummary.
        :type: str
        """
        self._internal_name = internal_name

    @property
    def category(self):
        """
        **[Required]** Gets the category of this LogAnalyticsEntityTypeSummary.
        Log analytics entity type category. Category will be used for grouping and filtering.


        :return: The category of this LogAnalyticsEntityTypeSummary.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this LogAnalyticsEntityTypeSummary.
        Log analytics entity type category. Category will be used for grouping and filtering.


        :param category: The category of this LogAnalyticsEntityTypeSummary.
        :type: str
        """
        self._category = category

    @property
    def cloud_type(self):
        """
        **[Required]** Gets the cloud_type of this LogAnalyticsEntityTypeSummary.
        Nature of log analytics entity type.

        Allowed values for this property are: "CLOUD", "NON_CLOUD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The cloud_type of this LogAnalyticsEntityTypeSummary.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """
        Sets the cloud_type of this LogAnalyticsEntityTypeSummary.
        Nature of log analytics entity type.


        :param cloud_type: The cloud_type of this LogAnalyticsEntityTypeSummary.
        :type: str
        """
        allowed_values = ["CLOUD", "NON_CLOUD"]
        if not value_allowed_none_or_none_sentinel(cloud_type, allowed_values):
            cloud_type = 'UNKNOWN_ENUM_VALUE'
        self._cloud_type = cloud_type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this LogAnalyticsEntityTypeSummary.
        The current state of the log analytics entity

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LogAnalyticsEntityTypeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LogAnalyticsEntityTypeSummary.
        The current state of the log analytics entity


        :param lifecycle_state: The lifecycle_state of this LogAnalyticsEntityTypeSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this LogAnalyticsEntityTypeSummary.
        Time the log analytics entity type was created. An RFC3339 formatted datetime string.


        :return: The time_created of this LogAnalyticsEntityTypeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LogAnalyticsEntityTypeSummary.
        Time the log analytics entity type was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this LogAnalyticsEntityTypeSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this LogAnalyticsEntityTypeSummary.
        Time the log analytics entity type was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this LogAnalyticsEntityTypeSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LogAnalyticsEntityTypeSummary.
        Time the log analytics entity type was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this LogAnalyticsEntityTypeSummary.
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
