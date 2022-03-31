# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IamWorkRequestSummary(object):
    """
    (For tenancies that support identity domains) The IAM work request summary. Tracks the status of asynchronous operations.
    """

    #: A constant which can be used with the operation_type property of a IamWorkRequestSummary.
    #: This constant has a value of "CREATE_DOMAIN"
    OPERATION_TYPE_CREATE_DOMAIN = "CREATE_DOMAIN"

    #: A constant which can be used with the operation_type property of a IamWorkRequestSummary.
    #: This constant has a value of "REPLICATE_DOMAIN_TO_REGION"
    OPERATION_TYPE_REPLICATE_DOMAIN_TO_REGION = "REPLICATE_DOMAIN_TO_REGION"

    #: A constant which can be used with the operation_type property of a IamWorkRequestSummary.
    #: This constant has a value of "UPDATE_DOMAIN"
    OPERATION_TYPE_UPDATE_DOMAIN = "UPDATE_DOMAIN"

    #: A constant which can be used with the operation_type property of a IamWorkRequestSummary.
    #: This constant has a value of "ACTIVATE_DOMAIN"
    OPERATION_TYPE_ACTIVATE_DOMAIN = "ACTIVATE_DOMAIN"

    #: A constant which can be used with the operation_type property of a IamWorkRequestSummary.
    #: This constant has a value of "DEACTIVATE_DOMAIN"
    OPERATION_TYPE_DEACTIVATE_DOMAIN = "DEACTIVATE_DOMAIN"

    #: A constant which can be used with the operation_type property of a IamWorkRequestSummary.
    #: This constant has a value of "DELETE_DOMAIN"
    OPERATION_TYPE_DELETE_DOMAIN = "DELETE_DOMAIN"

    #: A constant which can be used with the operation_type property of a IamWorkRequestSummary.
    #: This constant has a value of "CHANGE_COMPARTMENT_FOR_DOMAIN"
    OPERATION_TYPE_CHANGE_COMPARTMENT_FOR_DOMAIN = "CHANGE_COMPARTMENT_FOR_DOMAIN"

    #: A constant which can be used with the operation_type property of a IamWorkRequestSummary.
    #: This constant has a value of "CHANGE_LICENSE_TYPE_FOR_DOMAIN"
    OPERATION_TYPE_CHANGE_LICENSE_TYPE_FOR_DOMAIN = "CHANGE_LICENSE_TYPE_FOR_DOMAIN"

    #: A constant which can be used with the status property of a IamWorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a IamWorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a IamWorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a IamWorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a IamWorkRequestSummary.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a IamWorkRequestSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new IamWorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IamWorkRequestSummary.
        :type id: str

        :param operation_type:
            The value to assign to the operation_type property of this IamWorkRequestSummary.
            Allowed values for this property are: "CREATE_DOMAIN", "REPLICATE_DOMAIN_TO_REGION", "UPDATE_DOMAIN", "ACTIVATE_DOMAIN", "DEACTIVATE_DOMAIN", "DELETE_DOMAIN", "CHANGE_COMPARTMENT_FOR_DOMAIN", "CHANGE_LICENSE_TYPE_FOR_DOMAIN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this IamWorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param compartment_id:
            The value to assign to the compartment_id property of this IamWorkRequestSummary.
        :type compartment_id: str

        :param resources:
            The value to assign to the resources property of this IamWorkRequestSummary.
        :type resources: list[oci.identity.models.IamWorkRequestResource]

        :param percent_complete:
            The value to assign to the percent_complete property of this IamWorkRequestSummary.
        :type percent_complete: float

        :param time_accepted:
            The value to assign to the time_accepted property of this IamWorkRequestSummary.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this IamWorkRequestSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this IamWorkRequestSummary.
        :type time_finished: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'operation_type': 'str',
            'status': 'str',
            'compartment_id': 'str',
            'resources': 'list[IamWorkRequestResource]',
            'percent_complete': 'float',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'operation_type': 'operationType',
            'status': 'status',
            'compartment_id': 'compartmentId',
            'resources': 'resources',
            'percent_complete': 'percentComplete',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._id = None
        self._operation_type = None
        self._status = None
        self._compartment_id = None
        self._resources = None
        self._percent_complete = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IamWorkRequestSummary.
        The OCID of the work request.


        :return: The id of this IamWorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IamWorkRequestSummary.
        The OCID of the work request.


        :param id: The id of this IamWorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this IamWorkRequestSummary.
        The asynchronous operation tracked by this IAM work request.

        Allowed values for this property are: "CREATE_DOMAIN", "REPLICATE_DOMAIN_TO_REGION", "UPDATE_DOMAIN", "ACTIVATE_DOMAIN", "DEACTIVATE_DOMAIN", "DELETE_DOMAIN", "CHANGE_COMPARTMENT_FOR_DOMAIN", "CHANGE_LICENSE_TYPE_FOR_DOMAIN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this IamWorkRequestSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this IamWorkRequestSummary.
        The asynchronous operation tracked by this IAM work request.


        :param operation_type: The operation_type of this IamWorkRequestSummary.
        :type: str
        """
        allowed_values = ["CREATE_DOMAIN", "REPLICATE_DOMAIN_TO_REGION", "UPDATE_DOMAIN", "ACTIVATE_DOMAIN", "DEACTIVATE_DOMAIN", "DELETE_DOMAIN", "CHANGE_COMPARTMENT_FOR_DOMAIN", "CHANGE_LICENSE_TYPE_FOR_DOMAIN"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this IamWorkRequestSummary.
        The status of the work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this IamWorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this IamWorkRequestSummary.
        The status of the work request.


        :param status: The status of this IamWorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this IamWorkRequestSummary.
        The OCID of the compartment containing this IAM work request.


        :return: The compartment_id of this IamWorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IamWorkRequestSummary.
        The OCID of the compartment containing this IAM work request.


        :param compartment_id: The compartment_id of this IamWorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        Gets the resources of this IamWorkRequestSummary.
        The resources this work request affects.


        :return: The resources of this IamWorkRequestSummary.
        :rtype: list[oci.identity.models.IamWorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this IamWorkRequestSummary.
        The resources this work request affects.


        :param resources: The resources of this IamWorkRequestSummary.
        :type: list[oci.identity.models.IamWorkRequestResource]
        """
        self._resources = resources

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this IamWorkRequestSummary.
        How much progress the operation has made.


        :return: The percent_complete of this IamWorkRequestSummary.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this IamWorkRequestSummary.
        How much progress the operation has made.


        :param percent_complete: The percent_complete of this IamWorkRequestSummary.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this IamWorkRequestSummary.
        Date and time the work was accepted, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_accepted of this IamWorkRequestSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this IamWorkRequestSummary.
        Date and time the work was accepted, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_accepted: The time_accepted of this IamWorkRequestSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this IamWorkRequestSummary.
        Date and time the work started, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_started of this IamWorkRequestSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this IamWorkRequestSummary.
        Date and time the work started, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_started: The time_started of this IamWorkRequestSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this IamWorkRequestSummary.
        Date and time the work completed, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_finished of this IamWorkRequestSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this IamWorkRequestSummary.
        Date and time the work completed, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_finished: The time_finished of this IamWorkRequestSummary.
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
