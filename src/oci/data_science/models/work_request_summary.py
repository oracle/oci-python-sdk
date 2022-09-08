# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestSummary(object):
    """
    Summary information for a work request.
    """

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "NOTEBOOK_SESSION_CREATE"
    OPERATION_TYPE_NOTEBOOK_SESSION_CREATE = "NOTEBOOK_SESSION_CREATE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "NOTEBOOK_SESSION_DELETE"
    OPERATION_TYPE_NOTEBOOK_SESSION_DELETE = "NOTEBOOK_SESSION_DELETE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "NOTEBOOK_SESSION_ACTIVATE"
    OPERATION_TYPE_NOTEBOOK_SESSION_ACTIVATE = "NOTEBOOK_SESSION_ACTIVATE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "NOTEBOOK_SESSION_DEACTIVATE"
    OPERATION_TYPE_NOTEBOOK_SESSION_DEACTIVATE = "NOTEBOOK_SESSION_DEACTIVATE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "EXPORT_MODEL_ARTIFACT"
    OPERATION_TYPE_EXPORT_MODEL_ARTIFACT = "EXPORT_MODEL_ARTIFACT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "IMPORT_MODEL_ARTIFACT"
    OPERATION_TYPE_IMPORT_MODEL_ARTIFACT = "IMPORT_MODEL_ARTIFACT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "MODEL_DEPLOYMENT_CREATE"
    OPERATION_TYPE_MODEL_DEPLOYMENT_CREATE = "MODEL_DEPLOYMENT_CREATE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "MODEL_DEPLOYMENT_DELETE"
    OPERATION_TYPE_MODEL_DEPLOYMENT_DELETE = "MODEL_DEPLOYMENT_DELETE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "MODEL_DEPLOYMENT_ACTIVATE"
    OPERATION_TYPE_MODEL_DEPLOYMENT_ACTIVATE = "MODEL_DEPLOYMENT_ACTIVATE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "MODEL_DEPLOYMENT_DEACTIVATE"
    OPERATION_TYPE_MODEL_DEPLOYMENT_DEACTIVATE = "MODEL_DEPLOYMENT_DEACTIVATE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "MODEL_DEPLOYMENT_UPDATE"
    OPERATION_TYPE_MODEL_DEPLOYMENT_UPDATE = "MODEL_DEPLOYMENT_UPDATE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "PROJECT_DELETE"
    OPERATION_TYPE_PROJECT_DELETE = "PROJECT_DELETE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "WORKREQUEST_CANCEL"
    OPERATION_TYPE_WORKREQUEST_CANCEL = "WORKREQUEST_CANCEL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "JOB_DELETE"
    OPERATION_TYPE_JOB_DELETE = "JOB_DELETE"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkRequestSummary.
        :type id: str

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequestSummary.
            Allowed values for this property are: "NOTEBOOK_SESSION_CREATE", "NOTEBOOK_SESSION_DELETE", "NOTEBOOK_SESSION_ACTIVATE", "NOTEBOOK_SESSION_DEACTIVATE", "EXPORT_MODEL_ARTIFACT", "IMPORT_MODEL_ARTIFACT", "MODEL_DEPLOYMENT_CREATE", "MODEL_DEPLOYMENT_DELETE", "MODEL_DEPLOYMENT_ACTIVATE", "MODEL_DEPLOYMENT_DEACTIVATE", "MODEL_DEPLOYMENT_UPDATE", "PROJECT_DELETE", "WORKREQUEST_CANCEL", "JOB_DELETE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequestSummary.
        :type compartment_id: str

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequestSummary.
        :type percent_complete: float

        :param resources:
            The value to assign to the resources property of this WorkRequestSummary.
        :type resources: list[oci.data_science.models.WorkRequestResource]

        :param time_accepted:
            The value to assign to the time_accepted property of this WorkRequestSummary.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this WorkRequestSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequestSummary.
        :type time_finished: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'operation_type': 'str',
            'status': 'str',
            'compartment_id': 'str',
            'percent_complete': 'float',
            'resources': 'list[WorkRequestResource]',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'operation_type': 'operationType',
            'status': 'status',
            'compartment_id': 'compartmentId',
            'percent_complete': 'percentComplete',
            'resources': 'resources',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._id = None
        self._operation_type = None
        self._status = None
        self._compartment_id = None
        self._percent_complete = None
        self._resources = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequestSummary.
        The `OCID`__ of the work request.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this WorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestSummary.
        The `OCID`__ of the work request.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this WorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequestSummary.
        The type of work the work request is doing.

        Allowed values for this property are: "NOTEBOOK_SESSION_CREATE", "NOTEBOOK_SESSION_DELETE", "NOTEBOOK_SESSION_ACTIVATE", "NOTEBOOK_SESSION_DEACTIVATE", "EXPORT_MODEL_ARTIFACT", "IMPORT_MODEL_ARTIFACT", "MODEL_DEPLOYMENT_CREATE", "MODEL_DEPLOYMENT_DELETE", "MODEL_DEPLOYMENT_ACTIVATE", "MODEL_DEPLOYMENT_DEACTIVATE", "MODEL_DEPLOYMENT_UPDATE", "PROJECT_DELETE", "WORKREQUEST_CANCEL", "JOB_DELETE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequestSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequestSummary.
        The type of work the work request is doing.


        :param operation_type: The operation_type of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["NOTEBOOK_SESSION_CREATE", "NOTEBOOK_SESSION_DELETE", "NOTEBOOK_SESSION_ACTIVATE", "NOTEBOOK_SESSION_DEACTIVATE", "EXPORT_MODEL_ARTIFACT", "IMPORT_MODEL_ARTIFACT", "MODEL_DEPLOYMENT_CREATE", "MODEL_DEPLOYMENT_DELETE", "MODEL_DEPLOYMENT_ACTIVATE", "MODEL_DEPLOYMENT_DEACTIVATE", "MODEL_DEPLOYMENT_UPDATE", "PROJECT_DELETE", "WORKREQUEST_CANCEL", "JOB_DELETE"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequestSummary.
        The current status of the work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequestSummary.
        The current status of the work request.


        :param status: The status of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequestSummary.
        The `OCID`__ of the work request's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequestSummary.
        The `OCID`__ of the work request's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this WorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def percent_complete(self):
        """
        **[Required]** Gets the percent_complete of this WorkRequestSummary.
        Percentage of the request completed.


        :return: The percent_complete of this WorkRequestSummary.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequestSummary.
        Percentage of the request completed.


        :param percent_complete: The percent_complete of this WorkRequestSummary.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequestSummary.
        The resources affected by this work request.


        :return: The resources of this WorkRequestSummary.
        :rtype: list[oci.data_science.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequestSummary.
        The resources affected by this work request.


        :param resources: The resources of this WorkRequestSummary.
        :type: list[oci.data_science.models.WorkRequestResource]
        """
        self._resources = resources

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequestSummary.
        The date and time the work request was accepted in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_accepted of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequestSummary.
        The date and time the work request was accepted in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_accepted: The time_accepted of this WorkRequestSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequestSummary.
        The date and time the work request was started in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequestSummary.
        The date and time the work request was started in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this WorkRequestSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequestSummary.
        The date and time the work request was finished in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_finished of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequestSummary.
        The date and time the work request was finished in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_finished: The time_finished of this WorkRequestSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
