# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiSpecification(object):
    """
    The logical configuration of the API exposed by a deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApiSpecification object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param request_policies:
            The value to assign to the request_policies property of this ApiSpecification.
        :type request_policies: ApiSpecificationRequestPolicies

        :param logging_policies:
            The value to assign to the logging_policies property of this ApiSpecification.
        :type logging_policies: ApiSpecificationLoggingPolicies

        :param routes:
            The value to assign to the routes property of this ApiSpecification.
        :type routes: list[ApiSpecificationRoute]

        """
        self.swagger_types = {
            'request_policies': 'ApiSpecificationRequestPolicies',
            'logging_policies': 'ApiSpecificationLoggingPolicies',
            'routes': 'list[ApiSpecificationRoute]'
        }

        self.attribute_map = {
            'request_policies': 'requestPolicies',
            'logging_policies': 'loggingPolicies',
            'routes': 'routes'
        }

        self._request_policies = None
        self._logging_policies = None
        self._routes = None

    @property
    def request_policies(self):
        """
        Gets the request_policies of this ApiSpecification.

        :return: The request_policies of this ApiSpecification.
        :rtype: ApiSpecificationRequestPolicies
        """
        return self._request_policies

    @request_policies.setter
    def request_policies(self, request_policies):
        """
        Sets the request_policies of this ApiSpecification.

        :param request_policies: The request_policies of this ApiSpecification.
        :type: ApiSpecificationRequestPolicies
        """
        self._request_policies = request_policies

    @property
    def logging_policies(self):
        """
        Gets the logging_policies of this ApiSpecification.

        :return: The logging_policies of this ApiSpecification.
        :rtype: ApiSpecificationLoggingPolicies
        """
        return self._logging_policies

    @logging_policies.setter
    def logging_policies(self, logging_policies):
        """
        Sets the logging_policies of this ApiSpecification.

        :param logging_policies: The logging_policies of this ApiSpecification.
        :type: ApiSpecificationLoggingPolicies
        """
        self._logging_policies = logging_policies

    @property
    def routes(self):
        """
        Gets the routes of this ApiSpecification.
        A list of routes that this API exposes.


        :return: The routes of this ApiSpecification.
        :rtype: list[ApiSpecificationRoute]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """
        Sets the routes of this ApiSpecification.
        A list of routes that this API exposes.


        :param routes: The routes of this ApiSpecification.
        :type: list[ApiSpecificationRoute]
        """
        self._routes = routes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
