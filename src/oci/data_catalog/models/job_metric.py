# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobMetric(object):
    """
    A set of metrics are collected periodically to assess the state and performance characteristics of the execution
    instance of a job. The metrics are grouped based on their category and sub categories and aggregated based on
    their batch information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobMetric object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this JobMetric.
        :type key: str

        :param description:
            The value to assign to the description property of this JobMetric.
        :type description: str

        :param job_execution_key:
            The value to assign to the job_execution_key property of this JobMetric.
        :type job_execution_key: str

        :param time_inserted:
            The value to assign to the time_inserted property of this JobMetric.
        :type time_inserted: datetime

        :param category:
            The value to assign to the category property of this JobMetric.
        :type category: str

        :param display_name:
            The value to assign to the display_name property of this JobMetric.
        :type display_name: str

        :param sub_category:
            The value to assign to the sub_category property of this JobMetric.
        :type sub_category: str

        :param unit:
            The value to assign to the unit property of this JobMetric.
        :type unit: str

        :param value:
            The value to assign to the value property of this JobMetric.
        :type value: str

        :param batch_key:
            The value to assign to the batch_key property of this JobMetric.
        :type batch_key: str

        :param uri:
            The value to assign to the uri property of this JobMetric.
        :type uri: str

        :param time_created:
            The value to assign to the time_created property of this JobMetric.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this JobMetric.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this JobMetric.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this JobMetric.
        :type updated_by_id: str

        """
        self.swagger_types = {
            'key': 'str',
            'description': 'str',
            'job_execution_key': 'str',
            'time_inserted': 'datetime',
            'category': 'str',
            'display_name': 'str',
            'sub_category': 'str',
            'unit': 'str',
            'value': 'str',
            'batch_key': 'str',
            'uri': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'description': 'description',
            'job_execution_key': 'jobExecutionKey',
            'time_inserted': 'timeInserted',
            'category': 'category',
            'display_name': 'displayName',
            'sub_category': 'subCategory',
            'unit': 'unit',
            'value': 'value',
            'batch_key': 'batchKey',
            'uri': 'uri',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById'
        }

        self._key = None
        self._description = None
        self._job_execution_key = None
        self._time_inserted = None
        self._category = None
        self._display_name = None
        self._sub_category = None
        self._unit = None
        self._value = None
        self._batch_key = None
        self._uri = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this JobMetric.
        Key of the job metric that is immutable.


        :return: The key of this JobMetric.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this JobMetric.
        Key of the job metric that is immutable.


        :param key: The key of this JobMetric.
        :type: str
        """
        self._key = key

    @property
    def description(self):
        """
        Gets the description of this JobMetric.
        Detailed description of the metric.


        :return: The description of this JobMetric.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this JobMetric.
        Detailed description of the metric.


        :param description: The description of this JobMetric.
        :type: str
        """
        self._description = description

    @property
    def job_execution_key(self):
        """
        Gets the job_execution_key of this JobMetric.
        The unique key of the parent job execution for which the job metric resource is being created.


        :return: The job_execution_key of this JobMetric.
        :rtype: str
        """
        return self._job_execution_key

    @job_execution_key.setter
    def job_execution_key(self, job_execution_key):
        """
        Sets the job_execution_key of this JobMetric.
        The unique key of the parent job execution for which the job metric resource is being created.


        :param job_execution_key: The job_execution_key of this JobMetric.
        :type: str
        """
        self._job_execution_key = job_execution_key

    @property
    def time_inserted(self):
        """
        Gets the time_inserted of this JobMetric.
        The time the metric was logged or captured in the system where the job executed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_inserted of this JobMetric.
        :rtype: datetime
        """
        return self._time_inserted

    @time_inserted.setter
    def time_inserted(self, time_inserted):
        """
        Sets the time_inserted of this JobMetric.
        The time the metric was logged or captured in the system where the job executed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_inserted: The time_inserted of this JobMetric.
        :type: datetime
        """
        self._time_inserted = time_inserted

    @property
    def category(self):
        """
        Gets the category of this JobMetric.
        Category of this metric.


        :return: The category of this JobMetric.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this JobMetric.
        Category of this metric.


        :param category: The category of this JobMetric.
        :type: str
        """
        self._category = category

    @property
    def display_name(self):
        """
        Gets the display_name of this JobMetric.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this JobMetric.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this JobMetric.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this JobMetric.
        :type: str
        """
        self._display_name = display_name

    @property
    def sub_category(self):
        """
        Gets the sub_category of this JobMetric.
        Sub category of this metric under the category. Used for aggregating values. May be null.


        :return: The sub_category of this JobMetric.
        :rtype: str
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """
        Sets the sub_category of this JobMetric.
        Sub category of this metric under the category. Used for aggregating values. May be null.


        :param sub_category: The sub_category of this JobMetric.
        :type: str
        """
        self._sub_category = sub_category

    @property
    def unit(self):
        """
        Gets the unit of this JobMetric.
        Unit of this metric.


        :return: The unit of this JobMetric.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this JobMetric.
        Unit of this metric.


        :param unit: The unit of this JobMetric.
        :type: str
        """
        self._unit = unit

    @property
    def value(self):
        """
        Gets the value of this JobMetric.
        Value of this metric.


        :return: The value of this JobMetric.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this JobMetric.
        Value of this metric.


        :param value: The value of this JobMetric.
        :type: str
        """
        self._value = value

    @property
    def batch_key(self):
        """
        Gets the batch_key of this JobMetric.
        Batch key for grouping, may be null.


        :return: The batch_key of this JobMetric.
        :rtype: str
        """
        return self._batch_key

    @batch_key.setter
    def batch_key(self, batch_key):
        """
        Sets the batch_key of this JobMetric.
        Batch key for grouping, may be null.


        :param batch_key: The batch_key of this JobMetric.
        :type: str
        """
        self._batch_key = batch_key

    @property
    def uri(self):
        """
        Gets the uri of this JobMetric.
        URI to the job metric instance in the API.


        :return: The uri of this JobMetric.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this JobMetric.
        URI to the job metric instance in the API.


        :param uri: The uri of this JobMetric.
        :type: str
        """
        self._uri = uri

    @property
    def time_created(self):
        """
        Gets the time_created of this JobMetric.
        The date and time the job metric was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this JobMetric.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobMetric.
        The date and time the job metric was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this JobMetric.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this JobMetric.
        The last time that this metric was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this JobMetric.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this JobMetric.
        The last time that this metric was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this JobMetric.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this JobMetric.
        OCID of the user who created the metric for this job. Usually the executor of the job instance.


        :return: The created_by_id of this JobMetric.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this JobMetric.
        OCID of the user who created the metric for this job. Usually the executor of the job instance.


        :param created_by_id: The created_by_id of this JobMetric.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this JobMetric.
        OCID of the user who created the metric for this job. Usually the executor of the job instance.


        :return: The updated_by_id of this JobMetric.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this JobMetric.
        OCID of the user who created the metric for this job. Usually the executor of the job instance.


        :param updated_by_id: The updated_by_id of this JobMetric.
        :type: str
        """
        self._updated_by_id = updated_by_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
