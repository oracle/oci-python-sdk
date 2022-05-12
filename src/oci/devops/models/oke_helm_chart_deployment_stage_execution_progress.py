# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage_execution_progress import DeployStageExecutionProgress
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OkeHelmChartDeploymentStageExecutionProgress(DeployStageExecutionProgress):
    """
    Specifies the execution details for Kubernetes (OKE) helm chart deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OkeHelmChartDeploymentStageExecutionProgress object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.OkeHelmChartDeploymentStageExecutionProgress.deploy_stage_type` attribute
        of this class is ``OKE_HELM_CHART_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_stage_display_name:
            The value to assign to the deploy_stage_display_name property of this OkeHelmChartDeploymentStageExecutionProgress.
        :type deploy_stage_display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this OkeHelmChartDeploymentStageExecutionProgress.
        :type deploy_stage_type: str

        :param deploy_stage_id:
            The value to assign to the deploy_stage_id property of this OkeHelmChartDeploymentStageExecutionProgress.
        :type deploy_stage_id: str

        :param time_started:
            The value to assign to the time_started property of this OkeHelmChartDeploymentStageExecutionProgress.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this OkeHelmChartDeploymentStageExecutionProgress.
        :type time_finished: datetime

        :param status:
            The value to assign to the status property of this OkeHelmChartDeploymentStageExecutionProgress.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "ROLLBACK_IN_PROGRESS", "ROLLBACK_SUCCEEDED", "ROLLBACK_FAILED"
        :type status: str

        :param deploy_stage_predecessors:
            The value to assign to the deploy_stage_predecessors property of this OkeHelmChartDeploymentStageExecutionProgress.
        :type deploy_stage_predecessors: oci.devops.models.DeployStagePredecessorCollection

        :param deploy_stage_execution_progress_details:
            The value to assign to the deploy_stage_execution_progress_details property of this OkeHelmChartDeploymentStageExecutionProgress.
        :type deploy_stage_execution_progress_details: list[oci.devops.models.DeployStageExecutionProgressDetails]

        :param release_name:
            The value to assign to the release_name property of this OkeHelmChartDeploymentStageExecutionProgress.
        :type release_name: str

        :param chart_url:
            The value to assign to the chart_url property of this OkeHelmChartDeploymentStageExecutionProgress.
        :type chart_url: str

        :param version:
            The value to assign to the version property of this OkeHelmChartDeploymentStageExecutionProgress.
        :type version: str

        :param namespace:
            The value to assign to the namespace property of this OkeHelmChartDeploymentStageExecutionProgress.
        :type namespace: str

        """
        self.swagger_types = {
            'deploy_stage_display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_stage_id': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'status': 'str',
            'deploy_stage_predecessors': 'DeployStagePredecessorCollection',
            'deploy_stage_execution_progress_details': 'list[DeployStageExecutionProgressDetails]',
            'release_name': 'str',
            'chart_url': 'str',
            'version': 'str',
            'namespace': 'str'
        }

        self.attribute_map = {
            'deploy_stage_display_name': 'deployStageDisplayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_stage_id': 'deployStageId',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'status': 'status',
            'deploy_stage_predecessors': 'deployStagePredecessors',
            'deploy_stage_execution_progress_details': 'deployStageExecutionProgressDetails',
            'release_name': 'releaseName',
            'chart_url': 'chartUrl',
            'version': 'version',
            'namespace': 'namespace'
        }

        self._deploy_stage_display_name = None
        self._deploy_stage_type = None
        self._deploy_stage_id = None
        self._time_started = None
        self._time_finished = None
        self._status = None
        self._deploy_stage_predecessors = None
        self._deploy_stage_execution_progress_details = None
        self._release_name = None
        self._chart_url = None
        self._version = None
        self._namespace = None
        self._deploy_stage_type = 'OKE_HELM_CHART_DEPLOYMENT'

    @property
    def release_name(self):
        """
        Gets the release_name of this OkeHelmChartDeploymentStageExecutionProgress.
        Release name of the Helm chart.


        :return: The release_name of this OkeHelmChartDeploymentStageExecutionProgress.
        :rtype: str
        """
        return self._release_name

    @release_name.setter
    def release_name(self, release_name):
        """
        Sets the release_name of this OkeHelmChartDeploymentStageExecutionProgress.
        Release name of the Helm chart.


        :param release_name: The release_name of this OkeHelmChartDeploymentStageExecutionProgress.
        :type: str
        """
        self._release_name = release_name

    @property
    def chart_url(self):
        """
        Gets the chart_url of this OkeHelmChartDeploymentStageExecutionProgress.
        The URL of an OCIR repository.


        :return: The chart_url of this OkeHelmChartDeploymentStageExecutionProgress.
        :rtype: str
        """
        return self._chart_url

    @chart_url.setter
    def chart_url(self, chart_url):
        """
        Sets the chart_url of this OkeHelmChartDeploymentStageExecutionProgress.
        The URL of an OCIR repository.


        :param chart_url: The chart_url of this OkeHelmChartDeploymentStageExecutionProgress.
        :type: str
        """
        self._chart_url = chart_url

    @property
    def version(self):
        """
        Gets the version of this OkeHelmChartDeploymentStageExecutionProgress.
        The version of the helm chart stored in OCIR repository.


        :return: The version of this OkeHelmChartDeploymentStageExecutionProgress.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this OkeHelmChartDeploymentStageExecutionProgress.
        The version of the helm chart stored in OCIR repository.


        :param version: The version of this OkeHelmChartDeploymentStageExecutionProgress.
        :type: str
        """
        self._version = version

    @property
    def namespace(self):
        """
        Gets the namespace of this OkeHelmChartDeploymentStageExecutionProgress.
        Default namespace to be used for Kubernetes deployment when not specified in the manifest.


        :return: The namespace of this OkeHelmChartDeploymentStageExecutionProgress.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this OkeHelmChartDeploymentStageExecutionProgress.
        Default namespace to be used for Kubernetes deployment when not specified in the manifest.


        :param namespace: The namespace of this OkeHelmChartDeploymentStageExecutionProgress.
        :type: str
        """
        self._namespace = namespace

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
