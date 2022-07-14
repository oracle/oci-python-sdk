# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FusionEnvironmentStatus(object):
    """
    The health status of the Fusion Applications environment. For more information, see `Environment Status`__.

    __ https://docs.cloud.oracle.com/iaas/Content/fusion-applications/manage-environment.htm#environment-status
    """

    #: A constant which can be used with the status property of a FusionEnvironmentStatus.
    #: This constant has a value of "AVAILABLE"
    STATUS_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the status property of a FusionEnvironmentStatus.
    #: This constant has a value of "UNAVAILABLE"
    STATUS_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the status property of a FusionEnvironmentStatus.
    #: This constant has a value of "NOT_APPLICABLE"
    STATUS_NOT_APPLICABLE = "NOT_APPLICABLE"

    #: A constant which can be used with the status property of a FusionEnvironmentStatus.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    STATUS_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the status property of a FusionEnvironmentStatus.
    #: This constant has a value of "REFRESH_IN_PROGRESS"
    STATUS_REFRESH_IN_PROGRESS = "REFRESH_IN_PROGRESS"

    #: A constant which can be used with the status property of a FusionEnvironmentStatus.
    #: This constant has a value of "UNKNOWN"
    STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new FusionEnvironmentStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this FusionEnvironmentStatus.
            Allowed values for this property are: "AVAILABLE", "UNAVAILABLE", "NOT_APPLICABLE", "MAINTENANCE_IN_PROGRESS", "REFRESH_IN_PROGRESS", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'status': 'str'
        }

        self.attribute_map = {
            'status': 'status'
        }

        self._status = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this FusionEnvironmentStatus.
        The data plane status of FusionEnvironment.

        Allowed values for this property are: "AVAILABLE", "UNAVAILABLE", "NOT_APPLICABLE", "MAINTENANCE_IN_PROGRESS", "REFRESH_IN_PROGRESS", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this FusionEnvironmentStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this FusionEnvironmentStatus.
        The data plane status of FusionEnvironment.


        :param status: The status of this FusionEnvironmentStatus.
        :type: str
        """
        allowed_values = ["AVAILABLE", "UNAVAILABLE", "NOT_APPLICABLE", "MAINTENANCE_IN_PROGRESS", "REFRESH_IN_PROGRESS", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
