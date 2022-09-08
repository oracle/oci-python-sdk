# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiSpecificationRequestPolicies(object):
    """
    Global behavior applied to all requests received by the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApiSpecificationRequestPolicies object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param authentication:
            The value to assign to the authentication property of this ApiSpecificationRequestPolicies.
        :type authentication: oci.apigateway.models.AuthenticationPolicy

        :param rate_limiting:
            The value to assign to the rate_limiting property of this ApiSpecificationRequestPolicies.
        :type rate_limiting: oci.apigateway.models.RateLimitingPolicy

        :param cors:
            The value to assign to the cors property of this ApiSpecificationRequestPolicies.
        :type cors: oci.apigateway.models.CorsPolicy

        :param mutual_tls:
            The value to assign to the mutual_tls property of this ApiSpecificationRequestPolicies.
        :type mutual_tls: oci.apigateway.models.MutualTlsDetails

        :param usage_plans:
            The value to assign to the usage_plans property of this ApiSpecificationRequestPolicies.
        :type usage_plans: oci.apigateway.models.UsagePlansPolicy

        :param dynamic_authentication:
            The value to assign to the dynamic_authentication property of this ApiSpecificationRequestPolicies.
        :type dynamic_authentication: oci.apigateway.models.DynamicAuthenticationPolicy

        """
        self.swagger_types = {
            'authentication': 'AuthenticationPolicy',
            'rate_limiting': 'RateLimitingPolicy',
            'cors': 'CorsPolicy',
            'mutual_tls': 'MutualTlsDetails',
            'usage_plans': 'UsagePlansPolicy',
            'dynamic_authentication': 'DynamicAuthenticationPolicy'
        }

        self.attribute_map = {
            'authentication': 'authentication',
            'rate_limiting': 'rateLimiting',
            'cors': 'cors',
            'mutual_tls': 'mutualTls',
            'usage_plans': 'usagePlans',
            'dynamic_authentication': 'dynamicAuthentication'
        }

        self._authentication = None
        self._rate_limiting = None
        self._cors = None
        self._mutual_tls = None
        self._usage_plans = None
        self._dynamic_authentication = None

    @property
    def authentication(self):
        """
        Gets the authentication of this ApiSpecificationRequestPolicies.

        :return: The authentication of this ApiSpecificationRequestPolicies.
        :rtype: oci.apigateway.models.AuthenticationPolicy
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """
        Sets the authentication of this ApiSpecificationRequestPolicies.

        :param authentication: The authentication of this ApiSpecificationRequestPolicies.
        :type: oci.apigateway.models.AuthenticationPolicy
        """
        self._authentication = authentication

    @property
    def rate_limiting(self):
        """
        Gets the rate_limiting of this ApiSpecificationRequestPolicies.

        :return: The rate_limiting of this ApiSpecificationRequestPolicies.
        :rtype: oci.apigateway.models.RateLimitingPolicy
        """
        return self._rate_limiting

    @rate_limiting.setter
    def rate_limiting(self, rate_limiting):
        """
        Sets the rate_limiting of this ApiSpecificationRequestPolicies.

        :param rate_limiting: The rate_limiting of this ApiSpecificationRequestPolicies.
        :type: oci.apigateway.models.RateLimitingPolicy
        """
        self._rate_limiting = rate_limiting

    @property
    def cors(self):
        """
        Gets the cors of this ApiSpecificationRequestPolicies.

        :return: The cors of this ApiSpecificationRequestPolicies.
        :rtype: oci.apigateway.models.CorsPolicy
        """
        return self._cors

    @cors.setter
    def cors(self, cors):
        """
        Sets the cors of this ApiSpecificationRequestPolicies.

        :param cors: The cors of this ApiSpecificationRequestPolicies.
        :type: oci.apigateway.models.CorsPolicy
        """
        self._cors = cors

    @property
    def mutual_tls(self):
        """
        Gets the mutual_tls of this ApiSpecificationRequestPolicies.

        :return: The mutual_tls of this ApiSpecificationRequestPolicies.
        :rtype: oci.apigateway.models.MutualTlsDetails
        """
        return self._mutual_tls

    @mutual_tls.setter
    def mutual_tls(self, mutual_tls):
        """
        Sets the mutual_tls of this ApiSpecificationRequestPolicies.

        :param mutual_tls: The mutual_tls of this ApiSpecificationRequestPolicies.
        :type: oci.apigateway.models.MutualTlsDetails
        """
        self._mutual_tls = mutual_tls

    @property
    def usage_plans(self):
        """
        Gets the usage_plans of this ApiSpecificationRequestPolicies.

        :return: The usage_plans of this ApiSpecificationRequestPolicies.
        :rtype: oci.apigateway.models.UsagePlansPolicy
        """
        return self._usage_plans

    @usage_plans.setter
    def usage_plans(self, usage_plans):
        """
        Sets the usage_plans of this ApiSpecificationRequestPolicies.

        :param usage_plans: The usage_plans of this ApiSpecificationRequestPolicies.
        :type: oci.apigateway.models.UsagePlansPolicy
        """
        self._usage_plans = usage_plans

    @property
    def dynamic_authentication(self):
        """
        Gets the dynamic_authentication of this ApiSpecificationRequestPolicies.

        :return: The dynamic_authentication of this ApiSpecificationRequestPolicies.
        :rtype: oci.apigateway.models.DynamicAuthenticationPolicy
        """
        return self._dynamic_authentication

    @dynamic_authentication.setter
    def dynamic_authentication(self, dynamic_authentication):
        """
        Sets the dynamic_authentication of this ApiSpecificationRequestPolicies.

        :param dynamic_authentication: The dynamic_authentication of this ApiSpecificationRequestPolicies.
        :type: oci.apigateway.models.DynamicAuthenticationPolicy
        """
        self._dynamic_authentication = dynamic_authentication

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
