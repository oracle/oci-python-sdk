# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ThinAuthorizationResponse(object):
    """
    ThinAuthorizationResponse model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ThinAuthorizationResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param authorization_request:
            The value to assign to the authorization_request property of this ThinAuthorizationResponse.
        :type authorization_request: oci.identity_data_plane.models.AuthorizationRequest

        :param decision_cache_duration:
            The value to assign to the decision_cache_duration property of this ThinAuthorizationResponse.
        :type decision_cache_duration: str

        """
        self.swagger_types = {
            'authorization_request': 'AuthorizationRequest',
            'decision_cache_duration': 'str'
        }

        self.attribute_map = {
            'authorization_request': 'authorizationRequest',
            'decision_cache_duration': 'decisionCacheDuration'
        }

        self._authorization_request = None
        self._decision_cache_duration = None

    @property
    def authorization_request(self):
        """
        **[Required]** Gets the authorization_request of this ThinAuthorizationResponse.
        The policy string related to the request.


        :return: The authorization_request of this ThinAuthorizationResponse.
        :rtype: oci.identity_data_plane.models.AuthorizationRequest
        """
        return self._authorization_request

    @authorization_request.setter
    def authorization_request(self, authorization_request):
        """
        Sets the authorization_request of this ThinAuthorizationResponse.
        The policy string related to the request.


        :param authorization_request: The authorization_request of this ThinAuthorizationResponse.
        :type: oci.identity_data_plane.models.AuthorizationRequest
        """
        self._authorization_request = authorization_request

    @property
    def decision_cache_duration(self):
        """
        **[Required]** Gets the decision_cache_duration of this ThinAuthorizationResponse.
        The duration of how long this decision should be cached. Note that the type is of type java.time.Duration, not
        string.


        :return: The decision_cache_duration of this ThinAuthorizationResponse.
        :rtype: str
        """
        return self._decision_cache_duration

    @decision_cache_duration.setter
    def decision_cache_duration(self, decision_cache_duration):
        """
        Sets the decision_cache_duration of this ThinAuthorizationResponse.
        The duration of how long this decision should be cached. Note that the type is of type java.time.Duration, not
        string.


        :param decision_cache_duration: The decision_cache_duration of this ThinAuthorizationResponse.
        :type: str
        """
        self._decision_cache_duration = decision_cache_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
