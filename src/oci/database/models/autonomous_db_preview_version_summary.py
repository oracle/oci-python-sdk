# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDbPreviewVersionSummary(object):
    """
    The Autonomous Database preview version. Note that preview version software is only available for databases on `shared Exadata infrastructure`__.

    __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI
    """

    #: A constant which can be used with the db_workload property of a AutonomousDbPreviewVersionSummary.
    #: This constant has a value of "OLTP"
    DB_WORKLOAD_OLTP = "OLTP"

    #: A constant which can be used with the db_workload property of a AutonomousDbPreviewVersionSummary.
    #: This constant has a value of "DW"
    DB_WORKLOAD_DW = "DW"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDbPreviewVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this AutonomousDbPreviewVersionSummary.
        :type version: str

        :param time_preview_begin:
            The value to assign to the time_preview_begin property of this AutonomousDbPreviewVersionSummary.
        :type time_preview_begin: datetime

        :param time_preview_end:
            The value to assign to the time_preview_end property of this AutonomousDbPreviewVersionSummary.
        :type time_preview_end: datetime

        :param db_workload:
            The value to assign to the db_workload property of this AutonomousDbPreviewVersionSummary.
            Allowed values for this property are: "OLTP", "DW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_workload: str

        :param details:
            The value to assign to the details property of this AutonomousDbPreviewVersionSummary.
        :type details: str

        """
        self.swagger_types = {
            'version': 'str',
            'time_preview_begin': 'datetime',
            'time_preview_end': 'datetime',
            'db_workload': 'str',
            'details': 'str'
        }

        self.attribute_map = {
            'version': 'version',
            'time_preview_begin': 'timePreviewBegin',
            'time_preview_end': 'timePreviewEnd',
            'db_workload': 'dbWorkload',
            'details': 'details'
        }

        self._version = None
        self._time_preview_begin = None
        self._time_preview_end = None
        self._db_workload = None
        self._details = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this AutonomousDbPreviewVersionSummary.
        A valid Autonomous Database preview version.


        :return: The version of this AutonomousDbPreviewVersionSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this AutonomousDbPreviewVersionSummary.
        A valid Autonomous Database preview version.


        :param version: The version of this AutonomousDbPreviewVersionSummary.
        :type: str
        """
        self._version = version

    @property
    def time_preview_begin(self):
        """
        Gets the time_preview_begin of this AutonomousDbPreviewVersionSummary.
        The date and time when the preview version availability begins.


        :return: The time_preview_begin of this AutonomousDbPreviewVersionSummary.
        :rtype: datetime
        """
        return self._time_preview_begin

    @time_preview_begin.setter
    def time_preview_begin(self, time_preview_begin):
        """
        Sets the time_preview_begin of this AutonomousDbPreviewVersionSummary.
        The date and time when the preview version availability begins.


        :param time_preview_begin: The time_preview_begin of this AutonomousDbPreviewVersionSummary.
        :type: datetime
        """
        self._time_preview_begin = time_preview_begin

    @property
    def time_preview_end(self):
        """
        Gets the time_preview_end of this AutonomousDbPreviewVersionSummary.
        The date and time when the preview version availability ends.


        :return: The time_preview_end of this AutonomousDbPreviewVersionSummary.
        :rtype: datetime
        """
        return self._time_preview_end

    @time_preview_end.setter
    def time_preview_end(self, time_preview_end):
        """
        Sets the time_preview_end of this AutonomousDbPreviewVersionSummary.
        The date and time when the preview version availability ends.


        :param time_preview_end: The time_preview_end of this AutonomousDbPreviewVersionSummary.
        :type: datetime
        """
        self._time_preview_end = time_preview_end

    @property
    def db_workload(self):
        """
        Gets the db_workload of this AutonomousDbPreviewVersionSummary.
        The Autonomous Database workload type. The following values are valid:

        - OLTP - indicates an Autonomous Transaction Processing database
        - DW - indicates an Autonomous Data Warehouse database

        Allowed values for this property are: "OLTP", "DW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The db_workload of this AutonomousDbPreviewVersionSummary.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this AutonomousDbPreviewVersionSummary.
        The Autonomous Database workload type. The following values are valid:

        - OLTP - indicates an Autonomous Transaction Processing database
        - DW - indicates an Autonomous Data Warehouse database


        :param db_workload: The db_workload of this AutonomousDbPreviewVersionSummary.
        :type: str
        """
        allowed_values = ["OLTP", "DW"]
        if not value_allowed_none_or_none_sentinel(db_workload, allowed_values):
            db_workload = 'UNKNOWN_ENUM_VALUE'
        self._db_workload = db_workload

    @property
    def details(self):
        """
        Gets the details of this AutonomousDbPreviewVersionSummary.
        A URL that points to a detailed description of the preview version.


        :return: The details of this AutonomousDbPreviewVersionSummary.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this AutonomousDbPreviewVersionSummary.
        A URL that points to a detailed description of the preview version.


        :param details: The details of this AutonomousDbPreviewVersionSummary.
        :type: str
        """
        self._details = details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
