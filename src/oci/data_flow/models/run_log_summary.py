# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RunLogSummary(object):
    """
    A summary of a log associated with a particular run.
    """

    #: A constant which can be used with the source property of a RunLogSummary.
    #: This constant has a value of "APPLICATION"
    SOURCE_APPLICATION = "APPLICATION"

    #: A constant which can be used with the source property of a RunLogSummary.
    #: This constant has a value of "DRIVER"
    SOURCE_DRIVER = "DRIVER"

    #: A constant which can be used with the source property of a RunLogSummary.
    #: This constant has a value of "EXECUTOR"
    SOURCE_EXECUTOR = "EXECUTOR"

    #: A constant which can be used with the type property of a RunLogSummary.
    #: This constant has a value of "STDERR"
    TYPE_STDERR = "STDERR"

    #: A constant which can be used with the type property of a RunLogSummary.
    #: This constant has a value of "STDOUT"
    TYPE_STDOUT = "STDOUT"

    def __init__(self, **kwargs):
        """
        Initializes a new RunLogSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this RunLogSummary.
        :type name: str

        :param run_id:
            The value to assign to the run_id property of this RunLogSummary.
        :type run_id: str

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this RunLogSummary.
        :type size_in_bytes: int

        :param source:
            The value to assign to the source property of this RunLogSummary.
            Allowed values for this property are: "APPLICATION", "DRIVER", "EXECUTOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source: str

        :param time_created:
            The value to assign to the time_created property of this RunLogSummary.
        :type time_created: datetime

        :param type:
            The value to assign to the type property of this RunLogSummary.
            Allowed values for this property are: "STDERR", "STDOUT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'name': 'str',
            'run_id': 'str',
            'size_in_bytes': 'int',
            'source': 'str',
            'time_created': 'datetime',
            'type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'run_id': 'runId',
            'size_in_bytes': 'sizeInBytes',
            'source': 'source',
            'time_created': 'timeCreated',
            'type': 'type'
        }

        self._name = None
        self._run_id = None
        self._size_in_bytes = None
        self._source = None
        self._time_created = None
        self._type = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this RunLogSummary.
        The name of the log.
        Example: spark_driver_stderr_20190917T114000Z.log.gz


        :return: The name of this RunLogSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RunLogSummary.
        The name of the log.
        Example: spark_driver_stderr_20190917T114000Z.log.gz


        :param name: The name of this RunLogSummary.
        :type: str
        """
        self._name = name

    @property
    def run_id(self):
        """
        **[Required]** Gets the run_id of this RunLogSummary.
        The runId associated with the log.


        :return: The run_id of this RunLogSummary.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """
        Sets the run_id of this RunLogSummary.
        The runId associated with the log.


        :param run_id: The run_id of this RunLogSummary.
        :type: str
        """
        self._run_id = run_id

    @property
    def size_in_bytes(self):
        """
        Gets the size_in_bytes of this RunLogSummary.
        The size of the object in bytes.


        :return: The size_in_bytes of this RunLogSummary.
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this RunLogSummary.
        The size of the object in bytes.


        :param size_in_bytes: The size_in_bytes of this RunLogSummary.
        :type: int
        """
        self._size_in_bytes = size_in_bytes

    @property
    def source(self):
        """
        **[Required]** Gets the source of this RunLogSummary.
        The source of the log such as driver and executor.

        Allowed values for this property are: "APPLICATION", "DRIVER", "EXECUTOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source of this RunLogSummary.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this RunLogSummary.
        The source of the log such as driver and executor.


        :param source: The source of this RunLogSummary.
        :type: str
        """
        allowed_values = ["APPLICATION", "DRIVER", "EXECUTOR"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            source = 'UNKNOWN_ENUM_VALUE'
        self._source = source

    @property
    def time_created(self):
        """
        Gets the time_created of this RunLogSummary.
        The date and time the object was created, as described in `RFC 2616`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc2616


        :return: The time_created of this RunLogSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RunLogSummary.
        The date and time the object was created, as described in `RFC 2616`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc2616


        :param time_created: The time_created of this RunLogSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def type(self):
        """
        **[Required]** Gets the type of this RunLogSummary.
        The type of log such as stdout and stderr.

        Allowed values for this property are: "STDERR", "STDOUT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this RunLogSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RunLogSummary.
        The type of log such as stdout and stderr.


        :param type: The type of this RunLogSummary.
        :type: str
        """
        allowed_values = ["STDERR", "STDOUT"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
