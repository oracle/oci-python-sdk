# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Statement(object):
    """
    A statement object.
    """

    #: A constant which can be used with the lifecycle_state property of a Statement.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a Statement.
    #: This constant has a value of "CANCELLING"
    LIFECYCLE_STATE_CANCELLING = "CANCELLING"

    #: A constant which can be used with the lifecycle_state property of a Statement.
    #: This constant has a value of "CANCELLED"
    LIFECYCLE_STATE_CANCELLED = "CANCELLED"

    #: A constant which can be used with the lifecycle_state property of a Statement.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Statement.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a Statement.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new Statement object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Statement.
        :type id: int

        :param code:
            The value to assign to the code property of this Statement.
        :type code: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Statement.
            Allowed values for this property are: "ACCEPTED", "CANCELLING", "CANCELLED", "FAILED", "IN_PROGRESS", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param output:
            The value to assign to the output property of this Statement.
        :type output: oci.data_flow.models.StatementOutput

        :param progress:
            The value to assign to the progress property of this Statement.
        :type progress: float

        :param run_id:
            The value to assign to the run_id property of this Statement.
        :type run_id: str

        :param time_created:
            The value to assign to the time_created property of this Statement.
        :type time_created: datetime

        :param time_completed:
            The value to assign to the time_completed property of this Statement.
        :type time_completed: datetime

        """
        self.swagger_types = {
            'id': 'int',
            'code': 'str',
            'lifecycle_state': 'str',
            'output': 'StatementOutput',
            'progress': 'float',
            'run_id': 'str',
            'time_created': 'datetime',
            'time_completed': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'code': 'code',
            'lifecycle_state': 'lifecycleState',
            'output': 'output',
            'progress': 'progress',
            'run_id': 'runId',
            'time_created': 'timeCreated',
            'time_completed': 'timeCompleted'
        }

        self._id = None
        self._code = None
        self._lifecycle_state = None
        self._output = None
        self._progress = None
        self._run_id = None
        self._time_created = None
        self._time_completed = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Statement.
        The statement ID.


        :return: The id of this Statement.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Statement.
        The statement ID.


        :param id: The id of this Statement.
        :type: int
        """
        self._id = id

    @property
    def code(self):
        """
        **[Required]** Gets the code of this Statement.
        The statement code to execute.
        Example: `println(sc.version)`


        :return: The code of this Statement.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Statement.
        The statement code to execute.
        Example: `println(sc.version)`


        :param code: The code of this Statement.
        :type: str
        """
        self._code = code

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Statement.
        The current state of this statement.

        Allowed values for this property are: "ACCEPTED", "CANCELLING", "CANCELLED", "FAILED", "IN_PROGRESS", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Statement.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Statement.
        The current state of this statement.


        :param lifecycle_state: The lifecycle_state of this Statement.
        :type: str
        """
        allowed_values = ["ACCEPTED", "CANCELLING", "CANCELLED", "FAILED", "IN_PROGRESS", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def output(self):
        """
        Gets the output of this Statement.

        :return: The output of this Statement.
        :rtype: oci.data_flow.models.StatementOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """
        Sets the output of this Statement.

        :param output: The output of this Statement.
        :type: oci.data_flow.models.StatementOutput
        """
        self._output = output

    @property
    def progress(self):
        """
        Gets the progress of this Statement.
        The execution progress.


        :return: The progress of this Statement.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this Statement.
        The execution progress.


        :param progress: The progress of this Statement.
        :type: float
        """
        self._progress = progress

    @property
    def run_id(self):
        """
        Gets the run_id of this Statement.
        The ID of a run.


        :return: The run_id of this Statement.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """
        Sets the run_id of this Statement.
        The ID of a run.


        :param run_id: The run_id of this Statement.
        :type: str
        """
        self._run_id = run_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Statement.
        The date and time a application was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Statement.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Statement.
        The date and time a application was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Statement.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_completed(self):
        """
        Gets the time_completed of this Statement.
        The date and time a statement execution was completed, expressed in `RFC 3339`__ timestamp format.
        Example: `2022-05-31T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_completed of this Statement.
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this Statement.
        The date and time a statement execution was completed, expressed in `RFC 3339`__ timestamp format.
        Example: `2022-05-31T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_completed: The time_completed of this Statement.
        :type: datetime
        """
        self._time_completed = time_completed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
