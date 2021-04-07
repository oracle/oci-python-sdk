# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseConfigurationMetricGroup(object):
    """
    Supported configuration metric groups for database capacity planning service.
    """

    #: A constant which can be used with the metric_name property of a DatabaseConfigurationMetricGroup.
    #: This constant has a value of "DB_EXTERNAL_PROPERTIES"
    METRIC_NAME_DB_EXTERNAL_PROPERTIES = "DB_EXTERNAL_PROPERTIES"

    #: A constant which can be used with the metric_name property of a DatabaseConfigurationMetricGroup.
    #: This constant has a value of "DB_EXTERNAL_INSTANCE"
    METRIC_NAME_DB_EXTERNAL_INSTANCE = "DB_EXTERNAL_INSTANCE"

    #: A constant which can be used with the metric_name property of a DatabaseConfigurationMetricGroup.
    #: This constant has a value of "DB_OS_CONFIG_INSTANCE"
    METRIC_NAME_DB_OS_CONFIG_INSTANCE = "DB_OS_CONFIG_INSTANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseConfigurationMetricGroup object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.DBOSConfigInstance`
        * :class:`~oci.opsi.models.DBExternalInstance`
        * :class:`~oci.opsi.models.DBExternalProperties`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this DatabaseConfigurationMetricGroup.
            Allowed values for this property are: "DB_EXTERNAL_PROPERTIES", "DB_EXTERNAL_INSTANCE", "DB_OS_CONFIG_INSTANCE"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this DatabaseConfigurationMetricGroup.
        :type time_collected: datetime

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected'
        }

        self._metric_name = None
        self._time_collected = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['metricName']

        if type == 'DB_OS_CONFIG_INSTANCE':
            return 'DBOSConfigInstance'

        if type == 'DB_EXTERNAL_INSTANCE':
            return 'DBExternalInstance'

        if type == 'DB_EXTERNAL_PROPERTIES':
            return 'DBExternalProperties'
        else:
            return 'DatabaseConfigurationMetricGroup'

    @property
    def metric_name(self):
        """
        **[Required]** Gets the metric_name of this DatabaseConfigurationMetricGroup.
        Name of the metric group.

        Allowed values for this property are: "DB_EXTERNAL_PROPERTIES", "DB_EXTERNAL_INSTANCE", "DB_OS_CONFIG_INSTANCE"


        :return: The metric_name of this DatabaseConfigurationMetricGroup.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this DatabaseConfigurationMetricGroup.
        Name of the metric group.


        :param metric_name: The metric_name of this DatabaseConfigurationMetricGroup.
        :type: str
        """
        allowed_values = ["DB_EXTERNAL_PROPERTIES", "DB_EXTERNAL_INSTANCE", "DB_OS_CONFIG_INSTANCE"]
        if not value_allowed_none_or_none_sentinel(metric_name, allowed_values):
            raise ValueError(
                "Invalid value for `metric_name`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._metric_name = metric_name

    @property
    def time_collected(self):
        """
        Gets the time_collected of this DatabaseConfigurationMetricGroup.
        Collection timestamp
        Example: `\"2020-05-06T00:00:00.000Z\"`


        :return: The time_collected of this DatabaseConfigurationMetricGroup.
        :rtype: datetime
        """
        return self._time_collected

    @time_collected.setter
    def time_collected(self, time_collected):
        """
        Sets the time_collected of this DatabaseConfigurationMetricGroup.
        Collection timestamp
        Example: `\"2020-05-06T00:00:00.000Z\"`


        :param time_collected: The time_collected of this DatabaseConfigurationMetricGroup.
        :type: datetime
        """
        self._time_collected = time_collected

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
