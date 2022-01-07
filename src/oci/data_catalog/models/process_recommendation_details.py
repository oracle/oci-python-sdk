# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProcessRecommendationDetails(object):
    """
    Details of recommendation to be processed.
    """

    #: A constant which can be used with the recommendation_status property of a ProcessRecommendationDetails.
    #: This constant has a value of "ACCEPTED"
    RECOMMENDATION_STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the recommendation_status property of a ProcessRecommendationDetails.
    #: This constant has a value of "REJECTED"
    RECOMMENDATION_STATUS_REJECTED = "REJECTED"

    #: A constant which can be used with the recommendation_status property of a ProcessRecommendationDetails.
    #: This constant has a value of "INFERRED"
    RECOMMENDATION_STATUS_INFERRED = "INFERRED"

    def __init__(self, **kwargs):
        """
        Initializes a new ProcessRecommendationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param recommendation_key:
            The value to assign to the recommendation_key property of this ProcessRecommendationDetails.
        :type recommendation_key: str

        :param recommendation_status:
            The value to assign to the recommendation_status property of this ProcessRecommendationDetails.
            Allowed values for this property are: "ACCEPTED", "REJECTED", "INFERRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type recommendation_status: str

        :param properties:
            The value to assign to the properties property of this ProcessRecommendationDetails.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'recommendation_key': 'str',
            'recommendation_status': 'str',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'recommendation_key': 'recommendationKey',
            'recommendation_status': 'recommendationStatus',
            'properties': 'properties'
        }

        self._recommendation_key = None
        self._recommendation_status = None
        self._properties = None

    @property
    def recommendation_key(self):
        """
        **[Required]** Gets the recommendation_key of this ProcessRecommendationDetails.
        Unique identifier of the recommendation.


        :return: The recommendation_key of this ProcessRecommendationDetails.
        :rtype: str
        """
        return self._recommendation_key

    @recommendation_key.setter
    def recommendation_key(self, recommendation_key):
        """
        Sets the recommendation_key of this ProcessRecommendationDetails.
        Unique identifier of the recommendation.


        :param recommendation_key: The recommendation_key of this ProcessRecommendationDetails.
        :type: str
        """
        self._recommendation_key = recommendation_key

    @property
    def recommendation_status(self):
        """
        **[Required]** Gets the recommendation_status of this ProcessRecommendationDetails.
        The status of a recommendation.

        Allowed values for this property are: "ACCEPTED", "REJECTED", "INFERRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The recommendation_status of this ProcessRecommendationDetails.
        :rtype: str
        """
        return self._recommendation_status

    @recommendation_status.setter
    def recommendation_status(self, recommendation_status):
        """
        Sets the recommendation_status of this ProcessRecommendationDetails.
        The status of a recommendation.


        :param recommendation_status: The recommendation_status of this ProcessRecommendationDetails.
        :type: str
        """
        allowed_values = ["ACCEPTED", "REJECTED", "INFERRED"]
        if not value_allowed_none_or_none_sentinel(recommendation_status, allowed_values):
            recommendation_status = 'UNKNOWN_ENUM_VALUE'
        self._recommendation_status = recommendation_status

    @property
    def properties(self):
        """
        Gets the properties of this ProcessRecommendationDetails.
        A map of maps that contains additional properties which are specific to the associated objects.
        Each associated object defines it's set of required and optional properties.
        Example: `{
                    \"DataEntity\": {
                      \"parentId\": \"entityId\"
                    },
                    \"Term\": {
                      \"parentId\": \"glossaryId\"
                    }
                  }`


        :return: The properties of this ProcessRecommendationDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this ProcessRecommendationDetails.
        A map of maps that contains additional properties which are specific to the associated objects.
        Each associated object defines it's set of required and optional properties.
        Example: `{
                    \"DataEntity\": {
                      \"parentId\": \"entityId\"
                    },
                    \"Term\": {
                      \"parentId\": \"glossaryId\"
                    }
                  }`


        :param properties: The properties of this ProcessRecommendationDetails.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
