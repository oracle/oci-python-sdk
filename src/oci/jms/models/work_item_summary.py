# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkItemSummary(object):
    """
    The LCM work request for a JVM installation site.
    """

    #: A constant which can be used with the status property of a WorkItemSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkItemSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkItemSummary.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkItemSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a WorkItemSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkItemSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    STATUS_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the status property of a WorkItemSummary.
    #: This constant has a value of "RETRYING"
    STATUS_RETRYING = "RETRYING"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkItemSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkItemSummary.
        :type id: str

        :param work_request_id:
            The value to assign to the work_request_id property of this WorkItemSummary.
        :type work_request_id: str

        :param installation_site:
            The value to assign to the installation_site property of this WorkItemSummary.
        :type installation_site: oci.jms.models.InstallationSite

        :param status:
            The value to assign to the status property of this WorkItemSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", "NEEDS_ATTENTION", "RETRYING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param retry_count:
            The value to assign to the retry_count property of this WorkItemSummary.
        :type retry_count: int

        :param time_last_updated:
            The value to assign to the time_last_updated property of this WorkItemSummary.
        :type time_last_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'work_request_id': 'str',
            'installation_site': 'InstallationSite',
            'status': 'str',
            'retry_count': 'int',
            'time_last_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'work_request_id': 'workRequestId',
            'installation_site': 'installationSite',
            'status': 'status',
            'retry_count': 'retryCount',
            'time_last_updated': 'timeLastUpdated'
        }

        self._id = None
        self._work_request_id = None
        self._installation_site = None
        self._status = None
        self._retry_count = None
        self._time_last_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkItemSummary.
        The unique ID of ths work item.


        :return: The id of this WorkItemSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkItemSummary.
        The unique ID of ths work item.


        :param id: The id of this WorkItemSummary.
        :type: str
        """
        self._id = id

    @property
    def work_request_id(self):
        """
        **[Required]** Gets the work_request_id of this WorkItemSummary.
        The OCID of the work request created this work item.


        :return: The work_request_id of this WorkItemSummary.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this WorkItemSummary.
        The OCID of the work request created this work item.


        :param work_request_id: The work_request_id of this WorkItemSummary.
        :type: str
        """
        self._work_request_id = work_request_id

    @property
    def installation_site(self):
        """
        **[Required]** Gets the installation_site of this WorkItemSummary.

        :return: The installation_site of this WorkItemSummary.
        :rtype: oci.jms.models.InstallationSite
        """
        return self._installation_site

    @installation_site.setter
    def installation_site(self, installation_site):
        """
        Sets the installation_site of this WorkItemSummary.

        :param installation_site: The installation_site of this WorkItemSummary.
        :type: oci.jms.models.InstallationSite
        """
        self._installation_site = installation_site

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkItemSummary.
        The status of the work item.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", "NEEDS_ATTENTION", "RETRYING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkItemSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkItemSummary.
        The status of the work item.


        :param status: The status of this WorkItemSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", "NEEDS_ATTENTION", "RETRYING"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def retry_count(self):
        """
        **[Required]** Gets the retry_count of this WorkItemSummary.
        Number of times this work item is retried.


        :return: The retry_count of this WorkItemSummary.
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """
        Sets the retry_count of this WorkItemSummary.
        Number of times this work item is retried.


        :param retry_count: The retry_count of this WorkItemSummary.
        :type: int
        """
        self._retry_count = retry_count

    @property
    def time_last_updated(self):
        """
        Gets the time_last_updated of this WorkItemSummary.
        The date and time the work item was last updated. (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_last_updated of this WorkItemSummary.
        :rtype: datetime
        """
        return self._time_last_updated

    @time_last_updated.setter
    def time_last_updated(self, time_last_updated):
        """
        Sets the time_last_updated of this WorkItemSummary.
        The date and time the work item was last updated. (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_last_updated: The time_last_updated of this WorkItemSummary.
        :type: datetime
        """
        self._time_last_updated = time_last_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
