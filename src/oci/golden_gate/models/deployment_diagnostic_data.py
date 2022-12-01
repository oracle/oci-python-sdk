# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeploymentDiagnosticData(object):
    """
    Information regarding the deployment diagnostic collection
    """

    #: A constant which can be used with the diagnostic_state property of a DeploymentDiagnosticData.
    #: This constant has a value of "IN_PROGRESS"
    DIAGNOSTIC_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the diagnostic_state property of a DeploymentDiagnosticData.
    #: This constant has a value of "SUCCEEDED"
    DIAGNOSTIC_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the diagnostic_state property of a DeploymentDiagnosticData.
    #: This constant has a value of "FAILED"
    DIAGNOSTIC_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DeploymentDiagnosticData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace_name:
            The value to assign to the namespace_name property of this DeploymentDiagnosticData.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this DeploymentDiagnosticData.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this DeploymentDiagnosticData.
        :type object_name: str

        :param diagnostic_state:
            The value to assign to the diagnostic_state property of this DeploymentDiagnosticData.
            Allowed values for this property are: "IN_PROGRESS", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type diagnostic_state: str

        :param time_diagnostic_start:
            The value to assign to the time_diagnostic_start property of this DeploymentDiagnosticData.
        :type time_diagnostic_start: datetime

        :param time_diagnostic_end:
            The value to assign to the time_diagnostic_end property of this DeploymentDiagnosticData.
        :type time_diagnostic_end: datetime

        """
        self.swagger_types = {
            'namespace_name': 'str',
            'bucket_name': 'str',
            'object_name': 'str',
            'diagnostic_state': 'str',
            'time_diagnostic_start': 'datetime',
            'time_diagnostic_end': 'datetime'
        }

        self.attribute_map = {
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'object_name': 'objectName',
            'diagnostic_state': 'diagnosticState',
            'time_diagnostic_start': 'timeDiagnosticStart',
            'time_diagnostic_end': 'timeDiagnosticEnd'
        }

        self._namespace_name = None
        self._bucket_name = None
        self._object_name = None
        self._diagnostic_state = None
        self._time_diagnostic_start = None
        self._time_diagnostic_end = None

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this DeploymentDiagnosticData.
        Name of namespace that serves as a container for all of your buckets


        :return: The namespace_name of this DeploymentDiagnosticData.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this DeploymentDiagnosticData.
        Name of namespace that serves as a container for all of your buckets


        :param namespace_name: The namespace_name of this DeploymentDiagnosticData.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this DeploymentDiagnosticData.
        Name of the bucket where the object is to be uploaded in the object storage


        :return: The bucket_name of this DeploymentDiagnosticData.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this DeploymentDiagnosticData.
        Name of the bucket where the object is to be uploaded in the object storage


        :param bucket_name: The bucket_name of this DeploymentDiagnosticData.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this DeploymentDiagnosticData.
        Name of the diagnostic collected and uploaded to object storage


        :return: The object_name of this DeploymentDiagnosticData.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this DeploymentDiagnosticData.
        Name of the diagnostic collected and uploaded to object storage


        :param object_name: The object_name of this DeploymentDiagnosticData.
        :type: str
        """
        self._object_name = object_name

    @property
    def diagnostic_state(self):
        """
        **[Required]** Gets the diagnostic_state of this DeploymentDiagnosticData.
        The state of the deployment diagnostic collection.

        Allowed values for this property are: "IN_PROGRESS", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The diagnostic_state of this DeploymentDiagnosticData.
        :rtype: str
        """
        return self._diagnostic_state

    @diagnostic_state.setter
    def diagnostic_state(self, diagnostic_state):
        """
        Sets the diagnostic_state of this DeploymentDiagnosticData.
        The state of the deployment diagnostic collection.


        :param diagnostic_state: The diagnostic_state of this DeploymentDiagnosticData.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(diagnostic_state, allowed_values):
            diagnostic_state = 'UNKNOWN_ENUM_VALUE'
        self._diagnostic_state = diagnostic_state

    @property
    def time_diagnostic_start(self):
        """
        Gets the time_diagnostic_start of this DeploymentDiagnosticData.
        The time from which the diagnostic collection should collect the logs. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_diagnostic_start of this DeploymentDiagnosticData.
        :rtype: datetime
        """
        return self._time_diagnostic_start

    @time_diagnostic_start.setter
    def time_diagnostic_start(self, time_diagnostic_start):
        """
        Sets the time_diagnostic_start of this DeploymentDiagnosticData.
        The time from which the diagnostic collection should collect the logs. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_diagnostic_start: The time_diagnostic_start of this DeploymentDiagnosticData.
        :type: datetime
        """
        self._time_diagnostic_start = time_diagnostic_start

    @property
    def time_diagnostic_end(self):
        """
        Gets the time_diagnostic_end of this DeploymentDiagnosticData.
        The time until which the diagnostic collection should collect the logs. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_diagnostic_end of this DeploymentDiagnosticData.
        :rtype: datetime
        """
        return self._time_diagnostic_end

    @time_diagnostic_end.setter
    def time_diagnostic_end(self, time_diagnostic_end):
        """
        Sets the time_diagnostic_end of this DeploymentDiagnosticData.
        The time until which the diagnostic collection should collect the logs. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_diagnostic_end: The time_diagnostic_end of this DeploymentDiagnosticData.
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
