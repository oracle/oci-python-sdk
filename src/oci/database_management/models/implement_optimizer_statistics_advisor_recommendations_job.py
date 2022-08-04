# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImplementOptimizerStatisticsAdvisorRecommendationsJob(object):
    """
    The job request details to implement the Optimizer Statistics Advisor task recommendations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImplementOptimizerStatisticsAdvisorRecommendationsJob object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :type name: str

        :param description:
            The value to assign to the description property of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :type compartment_id: str

        :param result_location:
            The value to assign to the result_location property of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :type result_location: oci.database_management.models.JobExecutionResultLocation

        :param credentials:
            The value to assign to the credentials property of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :type credentials: oci.database_management.models.ManagedDatabaseCredential

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'result_location': 'JobExecutionResultLocation',
            'credentials': 'ManagedDatabaseCredential'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'result_location': 'resultLocation',
            'credentials': 'credentials'
        }

        self._name = None
        self._description = None
        self._compartment_id = None
        self._result_location = None
        self._credentials = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        The name of the job. Valid characters are uppercase or lowercase letters,
        numbers, and \"_\". The name of the job cannot be modified. It must be unique
        in the compartment and must begin with an alphabetic character.


        :return: The name of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        The name of the job. Valid characters are uppercase or lowercase letters,
        numbers, and \"_\". The name of the job cannot be modified. It must be unique
        in the compartment and must begin with an alphabetic character.


        :param name: The name of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        The name of the execution.


        :return: The description of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        The name of the execution.


        :param description: The description of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        The `OCID`__ of the compartment in which the job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        The `OCID`__ of the compartment in which the job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def result_location(self):
        """
        **[Required]** Gets the result_location of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.

        :return: The result_location of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :rtype: oci.database_management.models.JobExecutionResultLocation
        """
        return self._result_location

    @result_location.setter
    def result_location(self, result_location):
        """
        Sets the result_location of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.

        :param result_location: The result_location of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :type: oci.database_management.models.JobExecutionResultLocation
        """
        self._result_location = result_location

    @property
    def credentials(self):
        """
        Gets the credentials of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.

        :return: The credentials of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :rtype: oci.database_management.models.ManagedDatabaseCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.

        :param credentials: The credentials of this ImplementOptimizerStatisticsAdvisorRecommendationsJob.
        :type: oci.database_management.models.ManagedDatabaseCredential
        """
        self._credentials = credentials

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
