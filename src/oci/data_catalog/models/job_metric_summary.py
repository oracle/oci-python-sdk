# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobMetricSummary(object):
    """
    Job metric summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobMetricSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this JobMetricSummary.
        :type key: str

        :param description:
            The value to assign to the description property of this JobMetricSummary.
        :type description: str

        :param job_execution_key:
            The value to assign to the job_execution_key property of this JobMetricSummary.
        :type job_execution_key: str

        :param uri:
            The value to assign to the uri property of this JobMetricSummary.
        :type uri: str

        :param time_created:
            The value to assign to the time_created property of this JobMetricSummary.
        :type time_created: datetime

        :param time_inserted:
            The value to assign to the time_inserted property of this JobMetricSummary.
        :type time_inserted: datetime

        :param category:
            The value to assign to the category property of this JobMetricSummary.
        :type category: str

        :param display_name:
            The value to assign to the display_name property of this JobMetricSummary.
        :type display_name: str

        :param sub_category:
            The value to assign to the sub_category property of this JobMetricSummary.
        :type sub_category: str

        :param unit:
            The value to assign to the unit property of this JobMetricSummary.
        :type unit: str

        :param value:
            The value to assign to the value property of this JobMetricSummary.
        :type value: str

        :param batch_key:
            The value to assign to the batch_key property of this JobMetricSummary.
        :type batch_key: str

        """
        self.swagger_types = {
            'key': 'str',
            'description': 'str',
            'job_execution_key': 'str',
            'uri': 'str',
            'time_created': 'datetime',
            'time_inserted': 'datetime',
            'category': 'str',
            'display_name': 'str',
            'sub_category': 'str',
            'unit': 'str',
            'value': 'str',
            'batch_key': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'description': 'description',
            'job_execution_key': 'jobExecutionKey',
            'uri': 'uri',
            'time_created': 'timeCreated',
            'time_inserted': 'timeInserted',
            'category': 'category',
            'display_name': 'displayName',
            'sub_category': 'subCategory',
            'unit': 'unit',
            'value': 'value',
            'batch_key': 'batchKey'
        }

        self._key = None
        self._description = None
        self._job_execution_key = None
        self._uri = None
        self._time_created = None
        self._time_inserted = None
        self._category = None
        self._display_name = None
        self._sub_category = None
        self._unit = None
        self._value = None
        self._batch_key = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this JobMetricSummary.
        Key of the job metric that is immutable.


        :return: The key of this JobMetricSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this JobMetricSummary.
        Key of the job metric that is immutable.


        :param key: The key of this JobMetricSummary.
        :type: str
        """
        self._key = key

    @property
    def description(self):
        """
        Gets the description of this JobMetricSummary.
        Detailed description of the metric.


        :return: The description of this JobMetricSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this JobMetricSummary.
        Detailed description of the metric.


        :param description: The description of this JobMetricSummary.
        :type: str
        """
        self._description = description

    @property
    def job_execution_key(self):
        """
        Gets the job_execution_key of this JobMetricSummary.
        The unique key of the parent job execution for which the job metric resource was created.


        :return: The job_execution_key of this JobMetricSummary.
        :rtype: str
        """
        return self._job_execution_key

    @job_execution_key.setter
    def job_execution_key(self, job_execution_key):
        """
        Sets the job_execution_key of this JobMetricSummary.
        The unique key of the parent job execution for which the job metric resource was created.


        :param job_execution_key: The job_execution_key of this JobMetricSummary.
        :type: str
        """
        self._job_execution_key = job_execution_key

    @property
    def uri(self):
        """
        Gets the uri of this JobMetricSummary.
        URI to the job metric instance in the API.


        :return: The uri of this JobMetricSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this JobMetricSummary.
        URI to the job metric instance in the API.


        :param uri: The uri of this JobMetricSummary.
        :type: str
        """
        self._uri = uri

    @property
    def time_created(self):
        """
        Gets the time_created of this JobMetricSummary.
        The date and time the job metric was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this JobMetricSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobMetricSummary.
        The date and time the job metric was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this JobMetricSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_inserted(self):
        """
        Gets the time_inserted of this JobMetricSummary.
        The time the metric was logged or captured in the system where the job executed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_inserted of this JobMetricSummary.
        :rtype: datetime
        """
        return self._time_inserted

    @time_inserted.setter
    def time_inserted(self, time_inserted):
        """
        Sets the time_inserted of this JobMetricSummary.
        The time the metric was logged or captured in the system where the job executed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_inserted: The time_inserted of this JobMetricSummary.
        :type: datetime
        """
        self._time_inserted = time_inserted

    @property
    def category(self):
        """
        Gets the category of this JobMetricSummary.
        Category of this metric.


        :return: The category of this JobMetricSummary.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this JobMetricSummary.
        Category of this metric.


        :param category: The category of this JobMetricSummary.
        :type: str
        """
        self._category = category

    @property
    def display_name(self):
        """
        Gets the display_name of this JobMetricSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this JobMetricSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this JobMetricSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this JobMetricSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def sub_category(self):
        """
        Gets the sub_category of this JobMetricSummary.
        Sub category of this metric under the category. Used for aggregating values. May be null.


        :return: The sub_category of this JobMetricSummary.
        :rtype: str
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """
        Sets the sub_category of this JobMetricSummary.
        Sub category of this metric under the category. Used for aggregating values. May be null.


        :param sub_category: The sub_category of this JobMetricSummary.
        :type: str
        """
        self._sub_category = sub_category

    @property
    def unit(self):
        """
        Gets the unit of this JobMetricSummary.
        Unit of this metric.


        :return: The unit of this JobMetricSummary.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this JobMetricSummary.
        Unit of this metric.


        :param unit: The unit of this JobMetricSummary.
        :type: str
        """
        self._unit = unit

    @property
    def value(self):
        """
        Gets the value of this JobMetricSummary.
        Value of this metric.


        :return: The value of this JobMetricSummary.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this JobMetricSummary.
        Value of this metric.


        :param value: The value of this JobMetricSummary.
        :type: str
        """
        self._value = value

    @property
    def batch_key(self):
        """
        Gets the batch_key of this JobMetricSummary.
        Batch key for grouping, may be null.


        :return: The batch_key of this JobMetricSummary.
        :rtype: str
        """
        return self._batch_key

    @batch_key.setter
    def batch_key(self, batch_key):
        """
        Sets the batch_key of this JobMetricSummary.
        Batch key for grouping, may be null.


        :param batch_key: The batch_key of this JobMetricSummary.
        :type: str
        """
        self._batch_key = batch_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
