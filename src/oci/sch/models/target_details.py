# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetDetails(object):
    """
    An object that represents the target of the flow defined by the service connector.
    An example target is a stream (Streaming service).
    For more information about flows defined by service connectors, see
    `Service Connector Hub Overview`__.
    For configuration instructions, see
    `To create a service connector`__.

    __ https://docs.cloud.oracle.com/iaas/Content/service-connector-hub/overview.htm
    __ https://docs.cloud.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create
    """

    #: A constant which can be used with the kind property of a TargetDetails.
    #: This constant has a value of "functions"
    KIND_FUNCTIONS = "functions"

    #: A constant which can be used with the kind property of a TargetDetails.
    #: This constant has a value of "loggingAnalytics"
    KIND_LOGGING_ANALYTICS = "loggingAnalytics"

    #: A constant which can be used with the kind property of a TargetDetails.
    #: This constant has a value of "monitoring"
    KIND_MONITORING = "monitoring"

    #: A constant which can be used with the kind property of a TargetDetails.
    #: This constant has a value of "notifications"
    KIND_NOTIFICATIONS = "notifications"

    #: A constant which can be used with the kind property of a TargetDetails.
    #: This constant has a value of "objectStorage"
    KIND_OBJECT_STORAGE = "objectStorage"

    #: A constant which can be used with the kind property of a TargetDetails.
    #: This constant has a value of "streaming"
    KIND_STREAMING = "streaming"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.sch.models.NotificationsTargetDetails`
        * :class:`~oci.sch.models.ObjectStorageTargetDetails`
        * :class:`~oci.sch.models.MonitoringTargetDetails`
        * :class:`~oci.sch.models.FunctionsTargetDetails`
        * :class:`~oci.sch.models.LoggingAnalyticsTargetDetails`
        * :class:`~oci.sch.models.StreamingTargetDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this TargetDetails.
            Allowed values for this property are: "functions", "loggingAnalytics", "monitoring", "notifications", "objectStorage", "streaming", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        """
        self.swagger_types = {
            'kind': 'str'
        }

        self.attribute_map = {
            'kind': 'kind'
        }

        self._kind = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['kind']

        if type == 'notifications':
            return 'NotificationsTargetDetails'

        if type == 'objectStorage':
            return 'ObjectStorageTargetDetails'

        if type == 'monitoring':
            return 'MonitoringTargetDetails'

        if type == 'functions':
            return 'FunctionsTargetDetails'

        if type == 'loggingAnalytics':
            return 'LoggingAnalyticsTargetDetails'

        if type == 'streaming':
            return 'StreamingTargetDetails'
        else:
            return 'TargetDetails'

    @property
    def kind(self):
        """
        **[Required]** Gets the kind of this TargetDetails.
        The type descriminator.

        Allowed values for this property are: "functions", "loggingAnalytics", "monitoring", "notifications", "objectStorage", "streaming", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The kind of this TargetDetails.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this TargetDetails.
        The type descriminator.


        :param kind: The kind of this TargetDetails.
        :type: str
        """
        allowed_values = ["functions", "loggingAnalytics", "monitoring", "notifications", "objectStorage", "streaming"]
        if not value_allowed_none_or_none_sentinel(kind, allowed_values):
            kind = 'UNKNOWN_ENUM_VALUE'
        self._kind = kind

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
