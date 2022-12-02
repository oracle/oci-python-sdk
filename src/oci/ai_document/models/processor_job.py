# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProcessorJob(object):
    """
    Details of a processor job.
    """

    #: A constant which can be used with the lifecycle_state property of a ProcessorJob.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a ProcessorJob.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ProcessorJob.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a ProcessorJob.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a ProcessorJob.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a ProcessorJob.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_details property of a ProcessorJob.
    #: This constant has a value of "PARTIALLY_SUCCEEDED"
    LIFECYCLE_DETAILS_PARTIALLY_SUCCEEDED = "PARTIALLY_SUCCEEDED"

    #: A constant which can be used with the lifecycle_details property of a ProcessorJob.
    #: This constant has a value of "COMPLETELY_FAILED"
    LIFECYCLE_DETAILS_COMPLETELY_FAILED = "COMPLETELY_FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ProcessorJob object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ProcessorJob.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ProcessorJob.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ProcessorJob.
        :type display_name: str

        :param processor_config:
            The value to assign to the processor_config property of this ProcessorJob.
        :type processor_config: oci.ai_document.models.ProcessorConfig

        :param input_location:
            The value to assign to the input_location property of this ProcessorJob.
        :type input_location: oci.ai_document.models.InputLocation

        :param time_accepted:
            The value to assign to the time_accepted property of this ProcessorJob.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this ProcessorJob.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this ProcessorJob.
        :type time_finished: datetime

        :param percent_complete:
            The value to assign to the percent_complete property of this ProcessorJob.
        :type percent_complete: float

        :param output_location:
            The value to assign to the output_location property of this ProcessorJob.
        :type output_location: oci.ai_document.models.OutputLocation

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ProcessorJob.
            Allowed values for this property are: "SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ProcessorJob.
            Allowed values for this property are: "PARTIALLY_SUCCEEDED", "COMPLETELY_FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'processor_config': 'ProcessorConfig',
            'input_location': 'InputLocation',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'percent_complete': 'float',
            'output_location': 'OutputLocation',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'processor_config': 'processorConfig',
            'input_location': 'inputLocation',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'percent_complete': 'percentComplete',
            'output_location': 'outputLocation',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._processor_config = None
        self._input_location = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None
        self._percent_complete = None
        self._output_location = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ProcessorJob.
        The id of the processor job.


        :return: The id of this ProcessorJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProcessorJob.
        The id of the processor job.


        :param id: The id of this ProcessorJob.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ProcessorJob.
        The compartment identifier.


        :return: The compartment_id of this ProcessorJob.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ProcessorJob.
        The compartment identifier.


        :param compartment_id: The compartment_id of this ProcessorJob.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this ProcessorJob.
        The display name of the processor job.


        :return: The display_name of this ProcessorJob.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ProcessorJob.
        The display name of the processor job.


        :param display_name: The display_name of this ProcessorJob.
        :type: str
        """
        self._display_name = display_name

    @property
    def processor_config(self):
        """
        **[Required]** Gets the processor_config of this ProcessorJob.

        :return: The processor_config of this ProcessorJob.
        :rtype: oci.ai_document.models.ProcessorConfig
        """
        return self._processor_config

    @processor_config.setter
    def processor_config(self, processor_config):
        """
        Sets the processor_config of this ProcessorJob.

        :param processor_config: The processor_config of this ProcessorJob.
        :type: oci.ai_document.models.ProcessorConfig
        """
        self._processor_config = processor_config

    @property
    def input_location(self):
        """
        Gets the input_location of this ProcessorJob.

        :return: The input_location of this ProcessorJob.
        :rtype: oci.ai_document.models.InputLocation
        """
        return self._input_location

    @input_location.setter
    def input_location(self, input_location):
        """
        Sets the input_location of this ProcessorJob.

        :param input_location: The input_location of this ProcessorJob.
        :type: oci.ai_document.models.InputLocation
        """
        self._input_location = input_location

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this ProcessorJob.
        The job acceptance time.


        :return: The time_accepted of this ProcessorJob.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this ProcessorJob.
        The job acceptance time.


        :param time_accepted: The time_accepted of this ProcessorJob.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this ProcessorJob.
        The job start time.


        :return: The time_started of this ProcessorJob.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this ProcessorJob.
        The job start time.


        :param time_started: The time_started of this ProcessorJob.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this ProcessorJob.
        The job finish time.


        :return: The time_finished of this ProcessorJob.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this ProcessorJob.
        The job finish time.


        :param time_finished: The time_finished of this ProcessorJob.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this ProcessorJob.
        How much progress the operation has made, compared to the total amount of work to be performed.


        :return: The percent_complete of this ProcessorJob.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this ProcessorJob.
        How much progress the operation has made, compared to the total amount of work to be performed.


        :param percent_complete: The percent_complete of this ProcessorJob.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def output_location(self):
        """
        **[Required]** Gets the output_location of this ProcessorJob.

        :return: The output_location of this ProcessorJob.
        :rtype: oci.ai_document.models.OutputLocation
        """
        return self._output_location

    @output_location.setter
    def output_location(self, output_location):
        """
        Sets the output_location of this ProcessorJob.

        :param output_location: The output_location of this ProcessorJob.
        :type: oci.ai_document.models.OutputLocation
        """
        self._output_location = output_location

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ProcessorJob.
        The current state of the processor job.

        Allowed values for this property are: "SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ProcessorJob.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ProcessorJob.
        The current state of the processor job.


        :param lifecycle_state: The lifecycle_state of this ProcessorJob.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ProcessorJob.
        The detailed status of FAILED state.

        Allowed values for this property are: "PARTIALLY_SUCCEEDED", "COMPLETELY_FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this ProcessorJob.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ProcessorJob.
        The detailed status of FAILED state.


        :param lifecycle_details: The lifecycle_details of this ProcessorJob.
        :type: str
        """
        allowed_values = ["PARTIALLY_SUCCEEDED", "COMPLETELY_FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
