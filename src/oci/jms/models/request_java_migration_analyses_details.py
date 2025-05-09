# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestJavaMigrationAnalysesDetails(object):
    """
    Details of the request to start a Java migration analysis. The analysis requires the managed instance OCID, application installation key,
    source JDK version, and target JDK version of each selected application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestJavaMigrationAnalysesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param targets:
            The value to assign to the targets property of this RequestJavaMigrationAnalysesDetails.
        :type targets: list[oci.jms.models.JavaMigrationAnalysisTarget]

        """
        self.swagger_types = {
            'targets': 'list[JavaMigrationAnalysisTarget]'
        }
        self.attribute_map = {
            'targets': 'targets'
        }
        self._targets = None

    @property
    def targets(self):
        """
        **[Required]** Gets the targets of this RequestJavaMigrationAnalysesDetails.
        An array of migration analysis requests.


        :return: The targets of this RequestJavaMigrationAnalysesDetails.
        :rtype: list[oci.jms.models.JavaMigrationAnalysisTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this RequestJavaMigrationAnalysesDetails.
        An array of migration analysis requests.


        :param targets: The targets of this RequestJavaMigrationAnalysesDetails.
        :type: list[oci.jms.models.JavaMigrationAnalysisTarget]
        """
        self._targets = targets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
