# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .absolute_wait_criteria import AbsoluteWaitCriteria
from .absolute_wait_criteria_summary import AbsoluteWaitCriteriaSummary
from .approval_action import ApprovalAction
from .approval_policy import ApprovalPolicy
from .approve_deployment_details import ApproveDeploymentDetails
from .automated_deploy_stage_rollback_policy import AutomatedDeployStageRollbackPolicy
from .backend_set_ip_collection import BackendSetIpCollection
from .cancel_deployment_details import CancelDeploymentDetails
from .change_project_compartment_details import ChangeProjectCompartmentDetails
from .compute_instance_group_blue_green_deploy_stage_execution_progress import ComputeInstanceGroupBlueGreenDeployStageExecutionProgress
from .compute_instance_group_blue_green_traffic_shift_deploy_stage_execution_progress import ComputeInstanceGroupBlueGreenTrafficShiftDeployStageExecutionProgress
from .compute_instance_group_by_ids_selector import ComputeInstanceGroupByIdsSelector
from .compute_instance_group_by_query_selector import ComputeInstanceGroupByQuerySelector
from .compute_instance_group_canary_approval_deploy_stage_execution_progress import ComputeInstanceGroupCanaryApprovalDeployStageExecutionProgress
from .compute_instance_group_canary_deploy_stage_execution_progress import ComputeInstanceGroupCanaryDeployStageExecutionProgress
from .compute_instance_group_canary_traffic_shift_deploy_stage_execution_progress import ComputeInstanceGroupCanaryTrafficShiftDeployStageExecutionProgress
from .compute_instance_group_deploy_environment import ComputeInstanceGroupDeployEnvironment
from .compute_instance_group_deploy_environment_summary import ComputeInstanceGroupDeployEnvironmentSummary
from .compute_instance_group_deploy_stage import ComputeInstanceGroupDeployStage
from .compute_instance_group_deploy_stage_execution_progress import ComputeInstanceGroupDeployStageExecutionProgress
from .compute_instance_group_deploy_stage_summary import ComputeInstanceGroupDeployStageSummary
from .compute_instance_group_failure_policy import ComputeInstanceGroupFailurePolicy
from .compute_instance_group_failure_policy_by_count import ComputeInstanceGroupFailurePolicyByCount
from .compute_instance_group_failure_policy_by_percentage import ComputeInstanceGroupFailurePolicyByPercentage
from .compute_instance_group_linear_rollout_policy_by_count import ComputeInstanceGroupLinearRolloutPolicyByCount
from .compute_instance_group_linear_rollout_policy_by_percentage import ComputeInstanceGroupLinearRolloutPolicyByPercentage
from .compute_instance_group_rollout_policy import ComputeInstanceGroupRolloutPolicy
from .compute_instance_group_selector import ComputeInstanceGroupSelector
from .compute_instance_group_selector_collection import ComputeInstanceGroupSelectorCollection
from .count_based_approval_policy import CountBasedApprovalPolicy
from .create_compute_instance_group_deploy_environment_details import CreateComputeInstanceGroupDeployEnvironmentDetails
from .create_compute_instance_group_deploy_stage_details import CreateComputeInstanceGroupDeployStageDetails
from .create_deploy_artifact_details import CreateDeployArtifactDetails
from .create_deploy_environment_details import CreateDeployEnvironmentDetails
from .create_deploy_pipeline_deployment_details import CreateDeployPipelineDeploymentDetails
from .create_deploy_pipeline_details import CreateDeployPipelineDetails
from .create_deploy_pipeline_redeployment_details import CreateDeployPipelineRedeploymentDetails
from .create_deploy_stage_details import CreateDeployStageDetails
from .create_deployment_details import CreateDeploymentDetails
from .create_function_deploy_environment_details import CreateFunctionDeployEnvironmentDetails
from .create_function_deploy_stage_details import CreateFunctionDeployStageDetails
from .create_invoke_function_deploy_stage_details import CreateInvokeFunctionDeployStageDetails
from .create_load_balancer_traffic_shift_deploy_stage_details import CreateLoadBalancerTrafficShiftDeployStageDetails
from .create_manual_approval_deploy_stage_details import CreateManualApprovalDeployStageDetails
from .create_oke_cluster_deploy_environment_details import CreateOkeClusterDeployEnvironmentDetails
from .create_oke_deploy_stage_details import CreateOkeDeployStageDetails
from .create_project_details import CreateProjectDetails
from .create_single_deploy_stage_deployment_details import CreateSingleDeployStageDeploymentDetails
from .create_wait_deploy_stage_details import CreateWaitDeployStageDetails
from .deploy_artifact import DeployArtifact
from .deploy_artifact_collection import DeployArtifactCollection
from .deploy_artifact_override_argument import DeployArtifactOverrideArgument
from .deploy_artifact_override_argument_collection import DeployArtifactOverrideArgumentCollection
from .deploy_artifact_source import DeployArtifactSource
from .deploy_artifact_summary import DeployArtifactSummary
from .deploy_environment import DeployEnvironment
from .deploy_environment_collection import DeployEnvironmentCollection
from .deploy_environment_summary import DeployEnvironmentSummary
from .deploy_pipeline import DeployPipeline
from .deploy_pipeline_artifact import DeployPipelineArtifact
from .deploy_pipeline_artifact_collection import DeployPipelineArtifactCollection
from .deploy_pipeline_collection import DeployPipelineCollection
from .deploy_pipeline_deployment import DeployPipelineDeployment
from .deploy_pipeline_deployment_summary import DeployPipelineDeploymentSummary
from .deploy_pipeline_environment import DeployPipelineEnvironment
from .deploy_pipeline_environment_collection import DeployPipelineEnvironmentCollection
from .deploy_pipeline_parameter import DeployPipelineParameter
from .deploy_pipeline_parameter_collection import DeployPipelineParameterCollection
from .deploy_pipeline_redeployment import DeployPipelineRedeployment
from .deploy_pipeline_redeployment_summary import DeployPipelineRedeploymentSummary
from .deploy_pipeline_stage import DeployPipelineStage
from .deploy_pipeline_stage_collection import DeployPipelineStageCollection
from .deploy_pipeline_summary import DeployPipelineSummary
from .deploy_stage import DeployStage
from .deploy_stage_collection import DeployStageCollection
from .deploy_stage_execution_progress import DeployStageExecutionProgress
from .deploy_stage_execution_progress_details import DeployStageExecutionProgressDetails
from .deploy_stage_execution_step import DeployStageExecutionStep
from .deploy_stage_predecessor import DeployStagePredecessor
from .deploy_stage_predecessor_collection import DeployStagePredecessorCollection
from .deploy_stage_rollback_policy import DeployStageRollbackPolicy
from .deploy_stage_summary import DeployStageSummary
from .deployment import Deployment
from .deployment_argument import DeploymentArgument
from .deployment_argument_collection import DeploymentArgumentCollection
from .deployment_collection import DeploymentCollection
from .deployment_execution_progress import DeploymentExecutionProgress
from .deployment_summary import DeploymentSummary
from .function_deploy_environment import FunctionDeployEnvironment
from .function_deploy_environment_summary import FunctionDeployEnvironmentSummary
from .function_deploy_stage import FunctionDeployStage
from .function_deploy_stage_execution_progress import FunctionDeployStageExecutionProgress
from .function_deploy_stage_summary import FunctionDeployStageSummary
from .generic_deploy_artifact_source import GenericDeployArtifactSource
from .inline_deploy_artifact_source import InlineDeployArtifactSource
from .invoke_function_deploy_stage import InvokeFunctionDeployStage
from .invoke_function_deploy_stage_execution_progress import InvokeFunctionDeployStageExecutionProgress
from .invoke_function_deploy_stage_summary import InvokeFunctionDeployStageSummary
from .load_balancer_config import LoadBalancerConfig
from .load_balancer_traffic_shift_deploy_stage import LoadBalancerTrafficShiftDeployStage
from .load_balancer_traffic_shift_deploy_stage_execution_progress import LoadBalancerTrafficShiftDeployStageExecutionProgress
from .load_balancer_traffic_shift_deploy_stage_summary import LoadBalancerTrafficShiftDeployStageSummary
from .load_balancer_traffic_shift_rollout_policy import LoadBalancerTrafficShiftRolloutPolicy
from .manual_approval_deploy_stage import ManualApprovalDeployStage
from .manual_approval_deploy_stage_execution_progress import ManualApprovalDeployStageExecutionProgress
from .manual_approval_deploy_stage_summary import ManualApprovalDeployStageSummary
from .no_deploy_stage_rollback_policy import NoDeployStageRollbackPolicy
from .notification_config import NotificationConfig
from .ocir_deploy_artifact_source import OcirDeployArtifactSource
from .oke_cluster_deploy_environment import OkeClusterDeployEnvironment
from .oke_cluster_deploy_environment_summary import OkeClusterDeployEnvironmentSummary
from .oke_deploy_stage import OkeDeployStage
from .oke_deploy_stage_execution_progress import OkeDeployStageExecutionProgress
from .oke_deploy_stage_summary import OkeDeployStageSummary
from .project import Project
from .project_collection import ProjectCollection
from .project_summary import ProjectSummary
from .run_pipeline_deploy_stage_execution_progress import RunPipelineDeployStageExecutionProgress
from .run_validation_test_on_compute_instance_deploy_stage_execution_progress import RunValidationTestOnComputeInstanceDeployStageExecutionProgress
from .single_deploy_stage_deployment import SingleDeployStageDeployment
from .single_deploy_stage_deployment_summary import SingleDeployStageDeploymentSummary
from .update_compute_instance_group_deploy_environment_details import UpdateComputeInstanceGroupDeployEnvironmentDetails
from .update_compute_instance_group_deploy_stage_details import UpdateComputeInstanceGroupDeployStageDetails
from .update_deploy_artifact_details import UpdateDeployArtifactDetails
from .update_deploy_environment_details import UpdateDeployEnvironmentDetails
from .update_deploy_pipeline_deployment_details import UpdateDeployPipelineDeploymentDetails
from .update_deploy_pipeline_details import UpdateDeployPipelineDetails
from .update_deploy_pipeline_redeployment_details import UpdateDeployPipelineRedeploymentDetails
from .update_deploy_stage_details import UpdateDeployStageDetails
from .update_deployment_details import UpdateDeploymentDetails
from .update_function_deploy_environment_details import UpdateFunctionDeployEnvironmentDetails
from .update_function_deploy_stage_details import UpdateFunctionDeployStageDetails
from .update_invoke_function_deploy_stage_details import UpdateInvokeFunctionDeployStageDetails
from .update_load_balancer_traffic_shift_deploy_stage_details import UpdateLoadBalancerTrafficShiftDeployStageDetails
from .update_manual_approval_deploy_stage_details import UpdateManualApprovalDeployStageDetails
from .update_oke_cluster_deploy_environment_details import UpdateOkeClusterDeployEnvironmentDetails
from .update_oke_deploy_stage_details import UpdateOkeDeployStageDetails
from .update_project_details import UpdateProjectDetails
from .update_single_deploy_stage_deployment_details import UpdateSingleDeployStageDeploymentDetails
from .update_wait_deploy_stage_details import UpdateWaitDeployStageDetails
from .wait_criteria import WaitCriteria
from .wait_criteria_summary import WaitCriteriaSummary
from .wait_deploy_stage import WaitDeployStage
from .wait_deploy_stage_execution_progress import WaitDeployStageExecutionProgress
from .wait_deploy_stage_summary import WaitDeployStageSummary
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for devops services.
devops_type_mapping = {
    "AbsoluteWaitCriteria": AbsoluteWaitCriteria,
    "AbsoluteWaitCriteriaSummary": AbsoluteWaitCriteriaSummary,
    "ApprovalAction": ApprovalAction,
    "ApprovalPolicy": ApprovalPolicy,
    "ApproveDeploymentDetails": ApproveDeploymentDetails,
    "AutomatedDeployStageRollbackPolicy": AutomatedDeployStageRollbackPolicy,
    "BackendSetIpCollection": BackendSetIpCollection,
    "CancelDeploymentDetails": CancelDeploymentDetails,
    "ChangeProjectCompartmentDetails": ChangeProjectCompartmentDetails,
    "ComputeInstanceGroupBlueGreenDeployStageExecutionProgress": ComputeInstanceGroupBlueGreenDeployStageExecutionProgress,
    "ComputeInstanceGroupBlueGreenTrafficShiftDeployStageExecutionProgress": ComputeInstanceGroupBlueGreenTrafficShiftDeployStageExecutionProgress,
    "ComputeInstanceGroupByIdsSelector": ComputeInstanceGroupByIdsSelector,
    "ComputeInstanceGroupByQuerySelector": ComputeInstanceGroupByQuerySelector,
    "ComputeInstanceGroupCanaryApprovalDeployStageExecutionProgress": ComputeInstanceGroupCanaryApprovalDeployStageExecutionProgress,
    "ComputeInstanceGroupCanaryDeployStageExecutionProgress": ComputeInstanceGroupCanaryDeployStageExecutionProgress,
    "ComputeInstanceGroupCanaryTrafficShiftDeployStageExecutionProgress": ComputeInstanceGroupCanaryTrafficShiftDeployStageExecutionProgress,
    "ComputeInstanceGroupDeployEnvironment": ComputeInstanceGroupDeployEnvironment,
    "ComputeInstanceGroupDeployEnvironmentSummary": ComputeInstanceGroupDeployEnvironmentSummary,
    "ComputeInstanceGroupDeployStage": ComputeInstanceGroupDeployStage,
    "ComputeInstanceGroupDeployStageExecutionProgress": ComputeInstanceGroupDeployStageExecutionProgress,
    "ComputeInstanceGroupDeployStageSummary": ComputeInstanceGroupDeployStageSummary,
    "ComputeInstanceGroupFailurePolicy": ComputeInstanceGroupFailurePolicy,
    "ComputeInstanceGroupFailurePolicyByCount": ComputeInstanceGroupFailurePolicyByCount,
    "ComputeInstanceGroupFailurePolicyByPercentage": ComputeInstanceGroupFailurePolicyByPercentage,
    "ComputeInstanceGroupLinearRolloutPolicyByCount": ComputeInstanceGroupLinearRolloutPolicyByCount,
    "ComputeInstanceGroupLinearRolloutPolicyByPercentage": ComputeInstanceGroupLinearRolloutPolicyByPercentage,
    "ComputeInstanceGroupRolloutPolicy": ComputeInstanceGroupRolloutPolicy,
    "ComputeInstanceGroupSelector": ComputeInstanceGroupSelector,
    "ComputeInstanceGroupSelectorCollection": ComputeInstanceGroupSelectorCollection,
    "CountBasedApprovalPolicy": CountBasedApprovalPolicy,
    "CreateComputeInstanceGroupDeployEnvironmentDetails": CreateComputeInstanceGroupDeployEnvironmentDetails,
    "CreateComputeInstanceGroupDeployStageDetails": CreateComputeInstanceGroupDeployStageDetails,
    "CreateDeployArtifactDetails": CreateDeployArtifactDetails,
    "CreateDeployEnvironmentDetails": CreateDeployEnvironmentDetails,
    "CreateDeployPipelineDeploymentDetails": CreateDeployPipelineDeploymentDetails,
    "CreateDeployPipelineDetails": CreateDeployPipelineDetails,
    "CreateDeployPipelineRedeploymentDetails": CreateDeployPipelineRedeploymentDetails,
    "CreateDeployStageDetails": CreateDeployStageDetails,
    "CreateDeploymentDetails": CreateDeploymentDetails,
    "CreateFunctionDeployEnvironmentDetails": CreateFunctionDeployEnvironmentDetails,
    "CreateFunctionDeployStageDetails": CreateFunctionDeployStageDetails,
    "CreateInvokeFunctionDeployStageDetails": CreateInvokeFunctionDeployStageDetails,
    "CreateLoadBalancerTrafficShiftDeployStageDetails": CreateLoadBalancerTrafficShiftDeployStageDetails,
    "CreateManualApprovalDeployStageDetails": CreateManualApprovalDeployStageDetails,
    "CreateOkeClusterDeployEnvironmentDetails": CreateOkeClusterDeployEnvironmentDetails,
    "CreateOkeDeployStageDetails": CreateOkeDeployStageDetails,
    "CreateProjectDetails": CreateProjectDetails,
    "CreateSingleDeployStageDeploymentDetails": CreateSingleDeployStageDeploymentDetails,
    "CreateWaitDeployStageDetails": CreateWaitDeployStageDetails,
    "DeployArtifact": DeployArtifact,
    "DeployArtifactCollection": DeployArtifactCollection,
    "DeployArtifactOverrideArgument": DeployArtifactOverrideArgument,
    "DeployArtifactOverrideArgumentCollection": DeployArtifactOverrideArgumentCollection,
    "DeployArtifactSource": DeployArtifactSource,
    "DeployArtifactSummary": DeployArtifactSummary,
    "DeployEnvironment": DeployEnvironment,
    "DeployEnvironmentCollection": DeployEnvironmentCollection,
    "DeployEnvironmentSummary": DeployEnvironmentSummary,
    "DeployPipeline": DeployPipeline,
    "DeployPipelineArtifact": DeployPipelineArtifact,
    "DeployPipelineArtifactCollection": DeployPipelineArtifactCollection,
    "DeployPipelineCollection": DeployPipelineCollection,
    "DeployPipelineDeployment": DeployPipelineDeployment,
    "DeployPipelineDeploymentSummary": DeployPipelineDeploymentSummary,
    "DeployPipelineEnvironment": DeployPipelineEnvironment,
    "DeployPipelineEnvironmentCollection": DeployPipelineEnvironmentCollection,
    "DeployPipelineParameter": DeployPipelineParameter,
    "DeployPipelineParameterCollection": DeployPipelineParameterCollection,
    "DeployPipelineRedeployment": DeployPipelineRedeployment,
    "DeployPipelineRedeploymentSummary": DeployPipelineRedeploymentSummary,
    "DeployPipelineStage": DeployPipelineStage,
    "DeployPipelineStageCollection": DeployPipelineStageCollection,
    "DeployPipelineSummary": DeployPipelineSummary,
    "DeployStage": DeployStage,
    "DeployStageCollection": DeployStageCollection,
    "DeployStageExecutionProgress": DeployStageExecutionProgress,
    "DeployStageExecutionProgressDetails": DeployStageExecutionProgressDetails,
    "DeployStageExecutionStep": DeployStageExecutionStep,
    "DeployStagePredecessor": DeployStagePredecessor,
    "DeployStagePredecessorCollection": DeployStagePredecessorCollection,
    "DeployStageRollbackPolicy": DeployStageRollbackPolicy,
    "DeployStageSummary": DeployStageSummary,
    "Deployment": Deployment,
    "DeploymentArgument": DeploymentArgument,
    "DeploymentArgumentCollection": DeploymentArgumentCollection,
    "DeploymentCollection": DeploymentCollection,
    "DeploymentExecutionProgress": DeploymentExecutionProgress,
    "DeploymentSummary": DeploymentSummary,
    "FunctionDeployEnvironment": FunctionDeployEnvironment,
    "FunctionDeployEnvironmentSummary": FunctionDeployEnvironmentSummary,
    "FunctionDeployStage": FunctionDeployStage,
    "FunctionDeployStageExecutionProgress": FunctionDeployStageExecutionProgress,
    "FunctionDeployStageSummary": FunctionDeployStageSummary,
    "GenericDeployArtifactSource": GenericDeployArtifactSource,
    "InlineDeployArtifactSource": InlineDeployArtifactSource,
    "InvokeFunctionDeployStage": InvokeFunctionDeployStage,
    "InvokeFunctionDeployStageExecutionProgress": InvokeFunctionDeployStageExecutionProgress,
    "InvokeFunctionDeployStageSummary": InvokeFunctionDeployStageSummary,
    "LoadBalancerConfig": LoadBalancerConfig,
    "LoadBalancerTrafficShiftDeployStage": LoadBalancerTrafficShiftDeployStage,
    "LoadBalancerTrafficShiftDeployStageExecutionProgress": LoadBalancerTrafficShiftDeployStageExecutionProgress,
    "LoadBalancerTrafficShiftDeployStageSummary": LoadBalancerTrafficShiftDeployStageSummary,
    "LoadBalancerTrafficShiftRolloutPolicy": LoadBalancerTrafficShiftRolloutPolicy,
    "ManualApprovalDeployStage": ManualApprovalDeployStage,
    "ManualApprovalDeployStageExecutionProgress": ManualApprovalDeployStageExecutionProgress,
    "ManualApprovalDeployStageSummary": ManualApprovalDeployStageSummary,
    "NoDeployStageRollbackPolicy": NoDeployStageRollbackPolicy,
    "NotificationConfig": NotificationConfig,
    "OcirDeployArtifactSource": OcirDeployArtifactSource,
    "OkeClusterDeployEnvironment": OkeClusterDeployEnvironment,
    "OkeClusterDeployEnvironmentSummary": OkeClusterDeployEnvironmentSummary,
    "OkeDeployStage": OkeDeployStage,
    "OkeDeployStageExecutionProgress": OkeDeployStageExecutionProgress,
    "OkeDeployStageSummary": OkeDeployStageSummary,
    "Project": Project,
    "ProjectCollection": ProjectCollection,
    "ProjectSummary": ProjectSummary,
    "RunPipelineDeployStageExecutionProgress": RunPipelineDeployStageExecutionProgress,
    "RunValidationTestOnComputeInstanceDeployStageExecutionProgress": RunValidationTestOnComputeInstanceDeployStageExecutionProgress,
    "SingleDeployStageDeployment": SingleDeployStageDeployment,
    "SingleDeployStageDeploymentSummary": SingleDeployStageDeploymentSummary,
    "UpdateComputeInstanceGroupDeployEnvironmentDetails": UpdateComputeInstanceGroupDeployEnvironmentDetails,
    "UpdateComputeInstanceGroupDeployStageDetails": UpdateComputeInstanceGroupDeployStageDetails,
    "UpdateDeployArtifactDetails": UpdateDeployArtifactDetails,
    "UpdateDeployEnvironmentDetails": UpdateDeployEnvironmentDetails,
    "UpdateDeployPipelineDeploymentDetails": UpdateDeployPipelineDeploymentDetails,
    "UpdateDeployPipelineDetails": UpdateDeployPipelineDetails,
    "UpdateDeployPipelineRedeploymentDetails": UpdateDeployPipelineRedeploymentDetails,
    "UpdateDeployStageDetails": UpdateDeployStageDetails,
    "UpdateDeploymentDetails": UpdateDeploymentDetails,
    "UpdateFunctionDeployEnvironmentDetails": UpdateFunctionDeployEnvironmentDetails,
    "UpdateFunctionDeployStageDetails": UpdateFunctionDeployStageDetails,
    "UpdateInvokeFunctionDeployStageDetails": UpdateInvokeFunctionDeployStageDetails,
    "UpdateLoadBalancerTrafficShiftDeployStageDetails": UpdateLoadBalancerTrafficShiftDeployStageDetails,
    "UpdateManualApprovalDeployStageDetails": UpdateManualApprovalDeployStageDetails,
    "UpdateOkeClusterDeployEnvironmentDetails": UpdateOkeClusterDeployEnvironmentDetails,
    "UpdateOkeDeployStageDetails": UpdateOkeDeployStageDetails,
    "UpdateProjectDetails": UpdateProjectDetails,
    "UpdateSingleDeployStageDeploymentDetails": UpdateSingleDeployStageDeploymentDetails,
    "UpdateWaitDeployStageDetails": UpdateWaitDeployStageDetails,
    "WaitCriteria": WaitCriteria,
    "WaitCriteriaSummary": WaitCriteriaSummary,
    "WaitDeployStage": WaitDeployStage,
    "WaitDeployStageExecutionProgress": WaitDeployStageExecutionProgress,
    "WaitDeployStageSummary": WaitDeployStageSummary,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
