# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceEnvironmentEndPointOverview(object):
    """
    Model describing the properties of service environment endPoint overview.
    """

    #: A constant which can be used with the environment_type property of a ServiceEnvironmentEndPointOverview.
    #: This constant has a value of "INSTANCE_URL_PROD"
    ENVIRONMENT_TYPE_INSTANCE_URL_PROD = "INSTANCE_URL_PROD"

    #: A constant which can be used with the environment_type property of a ServiceEnvironmentEndPointOverview.
    #: This constant has a value of "INSTANCE_URL_TEST"
    ENVIRONMENT_TYPE_INSTANCE_URL_TEST = "INSTANCE_URL_TEST"

    #: A constant which can be used with the environment_type property of a ServiceEnvironmentEndPointOverview.
    #: This constant has a value of "INSTANCE_URL_DEV"
    ENVIRONMENT_TYPE_INSTANCE_URL_DEV = "INSTANCE_URL_DEV"

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceEnvironmentEndPointOverview object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param environment_type:
            The value to assign to the environment_type property of this ServiceEnvironmentEndPointOverview.
            Allowed values for this property are: "INSTANCE_URL_PROD", "INSTANCE_URL_TEST", "INSTANCE_URL_DEV", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type environment_type: str

        :param url:
            The value to assign to the url property of this ServiceEnvironmentEndPointOverview.
        :type url: str

        """
        self.swagger_types = {
            'environment_type': 'str',
            'url': 'str'
        }

        self.attribute_map = {
            'environment_type': 'environmentType',
            'url': 'url'
        }

        self._environment_type = None
        self._url = None

    @property
    def environment_type(self):
        """
        **[Required]** Gets the environment_type of this ServiceEnvironmentEndPointOverview.
        Service Environemnt EndPoint type.

        Allowed values for this property are: "INSTANCE_URL_PROD", "INSTANCE_URL_TEST", "INSTANCE_URL_DEV", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The environment_type of this ServiceEnvironmentEndPointOverview.
        :rtype: str
        """
        return self._environment_type

    @environment_type.setter
    def environment_type(self, environment_type):
        """
        Sets the environment_type of this ServiceEnvironmentEndPointOverview.
        Service Environemnt EndPoint type.


        :param environment_type: The environment_type of this ServiceEnvironmentEndPointOverview.
        :type: str
        """
        allowed_values = ["INSTANCE_URL_PROD", "INSTANCE_URL_TEST", "INSTANCE_URL_DEV"]
        if not value_allowed_none_or_none_sentinel(environment_type, allowed_values):
            environment_type = 'UNKNOWN_ENUM_VALUE'
        self._environment_type = environment_type

    @property
    def url(self):
        """
        **[Required]** Gets the url of this ServiceEnvironmentEndPointOverview.
        Service Environemnt Instance EndPoint url.


        :return: The url of this ServiceEnvironmentEndPointOverview.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ServiceEnvironmentEndPointOverview.
        Service Environemnt Instance EndPoint url.


        :param url: The url of this ServiceEnvironmentEndPointOverview.
        :type: str
        """
        self._url = url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
