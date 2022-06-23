# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .work_request_result import WorkRequestResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PathAnalysisWorkRequestResult(WorkRequestResult):
    """
    Defines the configuration of the path analysis result.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PathAnalysisWorkRequestResult object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.PathAnalysisWorkRequestResult.result_type` attribute
        of this class is ``PATH_ANALYSIS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param result_type:
            The value to assign to the result_type property of this PathAnalysisWorkRequestResult.
            Allowed values for this property are: "PATH_ANALYSIS"
        :type result_type: str

        :param paths:
            The value to assign to the paths property of this PathAnalysisWorkRequestResult.
        :type paths: list[oci.vn_monitoring.models.Path]

        :param time_created:
            The value to assign to the time_created property of this PathAnalysisWorkRequestResult.
        :type time_created: datetime

        """
        self.swagger_types = {
            'result_type': 'str',
            'paths': 'list[Path]',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'result_type': 'resultType',
            'paths': 'paths',
            'time_created': 'timeCreated'
        }

        self._result_type = None
        self._paths = None
        self._time_created = None
        self._result_type = 'PATH_ANALYSIS'

    @property
    def paths(self):
        """
        **[Required]** Gets the paths of this PathAnalysisWorkRequestResult.
        List of various paths from source node to destination node
        for a given `PathAnalysisQuery`.


        :return: The paths of this PathAnalysisWorkRequestResult.
        :rtype: list[oci.vn_monitoring.models.Path]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """
        Sets the paths of this PathAnalysisWorkRequestResult.
        List of various paths from source node to destination node
        for a given `PathAnalysisQuery`.


        :param paths: The paths of this PathAnalysisWorkRequestResult.
        :type: list[oci.vn_monitoring.models.Path]
        """
        self._paths = paths

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PathAnalysisWorkRequestResult.
        Time the `PathAnalysisResult` was generated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PathAnalysisWorkRequestResult.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PathAnalysisWorkRequestResult.
        Time the `PathAnalysisResult` was generated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PathAnalysisWorkRequestResult.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
