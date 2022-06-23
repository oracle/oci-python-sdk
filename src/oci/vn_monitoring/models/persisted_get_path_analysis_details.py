# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .get_path_analysis_details import GetPathAnalysisDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PersistedGetPathAnalysisDetails(GetPathAnalysisDetails):
    """
    Defines the configuration for getting a path analysis using the persisted `PathAnalyzerTest` resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PersistedGetPathAnalysisDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.PersistedGetPathAnalysisDetails.type` attribute
        of this class is ``PERSISTED_QUERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this PersistedGetPathAnalysisDetails.
            Allowed values for this property are: "PERSISTED_QUERY", "ADHOC_QUERY"
        :type type: str

        :param path_analyzer_test_id:
            The value to assign to the path_analyzer_test_id property of this PersistedGetPathAnalysisDetails.
        :type path_analyzer_test_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'path_analyzer_test_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'path_analyzer_test_id': 'pathAnalyzerTestId'
        }

        self._type = None
        self._path_analyzer_test_id = None
        self._type = 'PERSISTED_QUERY'

    @property
    def path_analyzer_test_id(self):
        """
        **[Required]** Gets the path_analyzer_test_id of this PersistedGetPathAnalysisDetails.
        The `OCID`__ of the `PathAnalyzerTest` resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The path_analyzer_test_id of this PersistedGetPathAnalysisDetails.
        :rtype: str
        """
        return self._path_analyzer_test_id

    @path_analyzer_test_id.setter
    def path_analyzer_test_id(self, path_analyzer_test_id):
        """
        Sets the path_analyzer_test_id of this PersistedGetPathAnalysisDetails.
        The `OCID`__ of the `PathAnalyzerTest` resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param path_analyzer_test_id: The path_analyzer_test_id of this PersistedGetPathAnalysisDetails.
        :type: str
        """
        self._path_analyzer_test_id = path_analyzer_test_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
