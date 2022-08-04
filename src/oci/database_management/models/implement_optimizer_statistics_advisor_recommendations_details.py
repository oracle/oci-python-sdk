# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImplementOptimizerStatisticsAdvisorRecommendationsDetails(object):
    """
    The request details object to implement the Optimizer Statistics Advisor task recommendations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImplementOptimizerStatisticsAdvisorRecommendationsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param task_name:
            The value to assign to the task_name property of this ImplementOptimizerStatisticsAdvisorRecommendationsDetails.
        :type task_name: str

        :param job_details:
            The value to assign to the job_details property of this ImplementOptimizerStatisticsAdvisorRecommendationsDetails.
        :type job_details: oci.database_management.models.ImplementOptimizerStatisticsAdvisorRecommendationsJob

        """
        self.swagger_types = {
            'task_name': 'str',
            'job_details': 'ImplementOptimizerStatisticsAdvisorRecommendationsJob'
        }

        self.attribute_map = {
            'task_name': 'taskName',
            'job_details': 'jobDetails'
        }

        self._task_name = None
        self._job_details = None

    @property
    def task_name(self):
        """
        **[Required]** Gets the task_name of this ImplementOptimizerStatisticsAdvisorRecommendationsDetails.
        The name of the task.


        :return: The task_name of this ImplementOptimizerStatisticsAdvisorRecommendationsDetails.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """
        Sets the task_name of this ImplementOptimizerStatisticsAdvisorRecommendationsDetails.
        The name of the task.


        :param task_name: The task_name of this ImplementOptimizerStatisticsAdvisorRecommendationsDetails.
        :type: str
        """
        self._task_name = task_name

    @property
    def job_details(self):
        """
        **[Required]** Gets the job_details of this ImplementOptimizerStatisticsAdvisorRecommendationsDetails.

        :return: The job_details of this ImplementOptimizerStatisticsAdvisorRecommendationsDetails.
        :rtype: oci.database_management.models.ImplementOptimizerStatisticsAdvisorRecommendationsJob
        """
        return self._job_details

    @job_details.setter
    def job_details(self, job_details):
        """
        Sets the job_details of this ImplementOptimizerStatisticsAdvisorRecommendationsDetails.

        :param job_details: The job_details of this ImplementOptimizerStatisticsAdvisorRecommendationsDetails.
        :type: oci.database_management.models.ImplementOptimizerStatisticsAdvisorRecommendationsJob
        """
        self._job_details = job_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
