# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CollectDeploymentDiagnosticDetails(object):
    """
    Details for collecting deployment diagnostic
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CollectDeploymentDiagnosticDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace_name:
            The value to assign to the namespace_name property of this CollectDeploymentDiagnosticDetails.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this CollectDeploymentDiagnosticDetails.
        :type bucket_name: str

        :param diagnostic_name_prefix:
            The value to assign to the diagnostic_name_prefix property of this CollectDeploymentDiagnosticDetails.
        :type diagnostic_name_prefix: str

        :param time_diagnostic_start:
            The value to assign to the time_diagnostic_start property of this CollectDeploymentDiagnosticDetails.
        :type time_diagnostic_start: datetime

        :param time_diagnostic_end:
            The value to assign to the time_diagnostic_end property of this CollectDeploymentDiagnosticDetails.
        :type time_diagnostic_end: datetime

        """
        self.swagger_types = {
            'namespace_name': 'str',
            'bucket_name': 'str',
            'diagnostic_name_prefix': 'str',
            'time_diagnostic_start': 'datetime',
            'time_diagnostic_end': 'datetime'
        }
        self.attribute_map = {
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'diagnostic_name_prefix': 'diagnosticNamePrefix',
            'time_diagnostic_start': 'timeDiagnosticStart',
            'time_diagnostic_end': 'timeDiagnosticEnd'
        }
        self._namespace_name = None
        self._bucket_name = None
        self._diagnostic_name_prefix = None
        self._time_diagnostic_start = None
        self._time_diagnostic_end = None

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this CollectDeploymentDiagnosticDetails.
        Name of namespace that serves as a container for all of your buckets


        :return: The namespace_name of this CollectDeploymentDiagnosticDetails.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this CollectDeploymentDiagnosticDetails.
        Name of namespace that serves as a container for all of your buckets


        :param namespace_name: The namespace_name of this CollectDeploymentDiagnosticDetails.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this CollectDeploymentDiagnosticDetails.
        Name of the bucket where the object is to be uploaded in the object storage


        :return: The bucket_name of this CollectDeploymentDiagnosticDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this CollectDeploymentDiagnosticDetails.
        Name of the bucket where the object is to be uploaded in the object storage


        :param bucket_name: The bucket_name of this CollectDeploymentDiagnosticDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def diagnostic_name_prefix(self):
        """
        **[Required]** Gets the diagnostic_name_prefix of this CollectDeploymentDiagnosticDetails.
        Prefix of the diagnostic collected and uploaded to object storage


        :return: The diagnostic_name_prefix of this CollectDeploymentDiagnosticDetails.
        :rtype: str
        """
        return self._diagnostic_name_prefix

    @diagnostic_name_prefix.setter
    def diagnostic_name_prefix(self, diagnostic_name_prefix):
        """
        Sets the diagnostic_name_prefix of this CollectDeploymentDiagnosticDetails.
        Prefix of the diagnostic collected and uploaded to object storage


        :param diagnostic_name_prefix: The diagnostic_name_prefix of this CollectDeploymentDiagnosticDetails.
        :type: str
        """
        self._diagnostic_name_prefix = diagnostic_name_prefix

    @property
    def time_diagnostic_start(self):
        """
        Gets the time_diagnostic_start of this CollectDeploymentDiagnosticDetails.
        The time from which the diagnostic collection should collect the logs. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_diagnostic_start of this CollectDeploymentDiagnosticDetails.
        :rtype: datetime
        """
        return self._time_diagnostic_start

    @time_diagnostic_start.setter
    def time_diagnostic_start(self, time_diagnostic_start):
        """
        Sets the time_diagnostic_start of this CollectDeploymentDiagnosticDetails.
        The time from which the diagnostic collection should collect the logs. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_diagnostic_start: The time_diagnostic_start of this CollectDeploymentDiagnosticDetails.
        :type: datetime
        """
        self._time_diagnostic_start = time_diagnostic_start

    @property
    def time_diagnostic_end(self):
        """
        Gets the time_diagnostic_end of this CollectDeploymentDiagnosticDetails.
        The time until which the diagnostic collection should collect the logs. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_diagnostic_end of this CollectDeploymentDiagnosticDetails.
        :rtype: datetime
        """
        return self._time_diagnostic_end

    @time_diagnostic_end.setter
    def time_diagnostic_end(self, time_diagnostic_end):
        """
        Sets the time_diagnostic_end of this CollectDeploymentDiagnosticDetails.
        The time until which the diagnostic collection should collect the logs. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_diagnostic_end: The time_diagnostic_end of this CollectDeploymentDiagnosticDetails.
        :type: datetime
        """
        self._time_diagnostic_end = time_diagnostic_end

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
