# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsEntityType(object):
    """
    Description of log analytics entity type.
    """

    #: A constant which can be used with the cloud_type property of a LogAnalyticsEntityType.
    #: This constant has a value of "CLOUD"
    CLOUD_TYPE_CLOUD = "CLOUD"

    #: A constant which can be used with the cloud_type property of a LogAnalyticsEntityType.
    #: This constant has a value of "NON_CLOUD"
    CLOUD_TYPE_NON_CLOUD = "NON_CLOUD"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsEntityType.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsEntityType.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsEntityType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this LogAnalyticsEntityType.
        :type name: str

        :param internal_name:
            The value to assign to the internal_name property of this LogAnalyticsEntityType.
        :type internal_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LogAnalyticsEntityType.
        :type compartment_id: str

        :param category:
            The value to assign to the category property of this LogAnalyticsEntityType.
        :type category: str

        :param cloud_type:
            The value to assign to the cloud_type property of this LogAnalyticsEntityType.
            Allowed values for this property are: "CLOUD", "NON_CLOUD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type cloud_type: str

        :param properties:
            The value to assign to the properties property of this LogAnalyticsEntityType.
        :type properties: list[oci.log_analytics.models.EntityTypeProperty]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LogAnalyticsEntityType.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this LogAnalyticsEntityType.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this LogAnalyticsEntityType.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'internal_name': 'str',
            'compartment_id': 'str',
            'category': 'str',
            'cloud_type': 'str',
            'properties': 'list[EntityTypeProperty]',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'internal_name': 'internalName',
            'compartment_id': 'compartmentId',
            'category': 'category',
            'cloud_type': 'cloudType',
            'properties': 'properties',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._name = None
        self._internal_name = None
        self._compartment_id = None
        self._category = None
        self._cloud_type = None
        self._properties = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this LogAnalyticsEntityType.
        Log analytics entity type name.


        :return: The name of this LogAnalyticsEntityType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsEntityType.
        Log analytics entity type name.


        :param name: The name of this LogAnalyticsEntityType.
        :type: str
        """
        self._name = name

    @property
    def internal_name(self):
        """
        **[Required]** Gets the internal_name of this LogAnalyticsEntityType.
        Internal name for the log analytics entity type.


        :return: The internal_name of this LogAnalyticsEntityType.
        :rtype: str
        """
        return self._internal_name

    @internal_name.setter
    def internal_name(self, internal_name):
        """
        Sets the internal_name of this LogAnalyticsEntityType.
        Internal name for the log analytics entity type.


        :param internal_name: The internal_name of this LogAnalyticsEntityType.
        :type: str
        """
        self._internal_name = internal_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this LogAnalyticsEntityType.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LogAnalyticsEntityType.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LogAnalyticsEntityType.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LogAnalyticsEntityType.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def category(self):
        """
        **[Required]** Gets the category of this LogAnalyticsEntityType.
        Log analytics entity type category. Category will be used for grouping and filtering.


        :return: The category of this LogAnalyticsEntityType.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this LogAnalyticsEntityType.
        Log analytics entity type category. Category will be used for grouping and filtering.


        :param category: The category of this LogAnalyticsEntityType.
        :type: str
        """
        self._category = category

    @property
    def cloud_type(self):
        """
        **[Required]** Gets the cloud_type of this LogAnalyticsEntityType.
        Log analytics entity type group. That can be CLOUD (OCI) or NON_CLOUD otherwise.

        Allowed values for this property are: "CLOUD", "NON_CLOUD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The cloud_type of this LogAnalyticsEntityType.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """
        Sets the cloud_type of this LogAnalyticsEntityType.
        Log analytics entity type group. That can be CLOUD (OCI) or NON_CLOUD otherwise.


        :param cloud_type: The cloud_type of this LogAnalyticsEntityType.
        :type: str
        """
        allowed_values = ["CLOUD", "NON_CLOUD"]
        if not value_allowed_none_or_none_sentinel(cloud_type, allowed_values):
            cloud_type = 'UNKNOWN_ENUM_VALUE'
        self._cloud_type = cloud_type

    @property
    def properties(self):
        """
        Gets the properties of this LogAnalyticsEntityType.
        The parameters used in file patterns specified in log sources for this log analytics entity type.


        :return: The properties of this LogAnalyticsEntityType.
        :rtype: list[oci.log_analytics.models.EntityTypeProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this LogAnalyticsEntityType.
        The parameters used in file patterns specified in log sources for this log analytics entity type.


        :param properties: The properties of this LogAnalyticsEntityType.
        :type: list[oci.log_analytics.models.EntityTypeProperty]
        """
        self._properties = properties

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this LogAnalyticsEntityType.
        The current lifecycle state of the log analytics entity.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LogAnalyticsEntityType.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LogAnalyticsEntityType.
        The current lifecycle state of the log analytics entity.


        :param lifecycle_state: The lifecycle_state of this LogAnalyticsEntityType.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this LogAnalyticsEntityType.
        Time the log analytics entity type was created. An RFC3339 formatted datetime string.


        :return: The time_created of this LogAnalyticsEntityType.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LogAnalyticsEntityType.
        Time the log analytics entity type was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this LogAnalyticsEntityType.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this LogAnalyticsEntityType.
        Time the log analytics entity type was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this LogAnalyticsEntityType.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LogAnalyticsEntityType.
        Time the log analytics entity type was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this LogAnalyticsEntityType.
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
