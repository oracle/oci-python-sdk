# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activity_problem_aggregation import ActivityProblemAggregation
from .activity_problem_aggregation_collection import ActivityProblemAggregationCollection
from .attach_target_detector_recipe_details import AttachTargetDetectorRecipeDetails
from .attach_target_responder_recipe_details import AttachTargetResponderRecipeDetails
from .candidate_responder_rule import CandidateResponderRule
from .change_detector_recipe_compartment_details import ChangeDetectorRecipeCompartmentDetails
from .change_managed_list_compartment_details import ChangeManagedListCompartmentDetails
from .change_responder_recipe_compartment_details import ChangeResponderRecipeCompartmentDetails
from .composite_condition import CompositeCondition
from .condition import Condition
from .condition_group import ConditionGroup
from .condition_metadata_type import ConditionMetadataType
from .condition_metadata_type_collection import ConditionMetadataTypeCollection
from .condition_metadata_type_summary import ConditionMetadataTypeSummary
from .condition_operator import ConditionOperator
from .config_value import ConfigValue
from .configuration import Configuration
from .create_detector_recipe_details import CreateDetectorRecipeDetails
from .create_managed_list_details import CreateManagedListDetails
from .create_responder_recipe_details import CreateResponderRecipeDetails
from .create_target_details import CreateTargetDetails
from .create_target_detector_recipe_details import CreateTargetDetectorRecipeDetails
from .create_target_responder_recipe_details import CreateTargetResponderRecipeDetails
from .detector import Detector
from .detector_collection import DetectorCollection
from .detector_configuration import DetectorConfiguration
from .detector_details import DetectorDetails
from .detector_recipe import DetectorRecipe
from .detector_recipe_collection import DetectorRecipeCollection
from .detector_recipe_detector_rule import DetectorRecipeDetectorRule
from .detector_recipe_detector_rule_collection import DetectorRecipeDetectorRuleCollection
from .detector_recipe_detector_rule_summary import DetectorRecipeDetectorRuleSummary
from .detector_recipe_summary import DetectorRecipeSummary
from .detector_rule import DetectorRule
from .detector_rule_collection import DetectorRuleCollection
from .detector_rule_summary import DetectorRuleSummary
from .detector_summary import DetectorSummary
from .execute_responder_execution_details import ExecuteResponderExecutionDetails
from .geographical_location import GeographicalLocation
from .impacted_resource_collection import ImpactedResourceCollection
from .impacted_resource_summary import ImpactedResourceSummary
from .managed_list import ManagedList
from .managed_list_collection import ManagedListCollection
from .managed_list_summary import ManagedListSummary
from .managed_list_type_collection import ManagedListTypeCollection
from .managed_list_type_summary import ManagedListTypeSummary
from .operator_summary import OperatorSummary
from .political_location import PoliticalLocation
from .problem import Problem
from .problem_aggregation import ProblemAggregation
from .problem_aggregation_collection import ProblemAggregationCollection
from .problem_collection import ProblemCollection
from .problem_history_collection import ProblemHistoryCollection
from .problem_history_summary import ProblemHistorySummary
from .problem_summary import ProblemSummary
from .problem_trend_aggregation import ProblemTrendAggregation
from .problem_trend_aggregation_collection import ProblemTrendAggregationCollection
from .recommendation_summary import RecommendationSummary
from .recommendation_summary_collection import RecommendationSummaryCollection
from .resource_type_collection import ResourceTypeCollection
from .resource_type_summary import ResourceTypeSummary
from .responder_activity_collection import ResponderActivityCollection
from .responder_activity_summary import ResponderActivitySummary
from .responder_configuration import ResponderConfiguration
from .responder_execution import ResponderExecution
from .responder_execution_aggregation import ResponderExecutionAggregation
from .responder_execution_aggregation_collection import ResponderExecutionAggregationCollection
from .responder_execution_collection import ResponderExecutionCollection
from .responder_execution_summary import ResponderExecutionSummary
from .responder_execution_trend_aggregation import ResponderExecutionTrendAggregation
from .responder_execution_trend_aggregation_collection import ResponderExecutionTrendAggregationCollection
from .responder_recipe import ResponderRecipe
from .responder_recipe_collection import ResponderRecipeCollection
from .responder_recipe_responder_rule import ResponderRecipeResponderRule
from .responder_recipe_responder_rule_collection import ResponderRecipeResponderRuleCollection
from .responder_recipe_responder_rule_summary import ResponderRecipeResponderRuleSummary
from .responder_recipe_summary import ResponderRecipeSummary
from .responder_rule import ResponderRule
from .responder_rule_collection import ResponderRuleCollection
from .responder_rule_details import ResponderRuleDetails
from .responder_rule_execution_details import ResponderRuleExecutionDetails
from .responder_rule_summary import ResponderRuleSummary
from .risk_score_aggregation import RiskScoreAggregation
from .risk_score_aggregation_collection import RiskScoreAggregationCollection
from .rule_summary import RuleSummary
from .security_score_aggregation import SecurityScoreAggregation
from .security_score_aggregation_collection import SecurityScoreAggregationCollection
from .security_score_trend_aggregation import SecurityScoreTrendAggregation
from .security_score_trend_aggregation_collection import SecurityScoreTrendAggregationCollection
from .service_type_summary import ServiceTypeSummary
from .simple_condition import SimpleCondition
from .skip_bulk_responder_execution_details import SkipBulkResponderExecutionDetails
from .target import Target
from .target_collection import TargetCollection
from .target_detector_details import TargetDetectorDetails
from .target_detector_recipe import TargetDetectorRecipe
from .target_detector_recipe_collection import TargetDetectorRecipeCollection
from .target_detector_recipe_detector_rule import TargetDetectorRecipeDetectorRule
from .target_detector_recipe_detector_rule_collection import TargetDetectorRecipeDetectorRuleCollection
from .target_detector_recipe_detector_rule_summary import TargetDetectorRecipeDetectorRuleSummary
from .target_detector_recipe_summary import TargetDetectorRecipeSummary
from .target_responder_recipe import TargetResponderRecipe
from .target_responder_recipe_collection import TargetResponderRecipeCollection
from .target_responder_recipe_responder_rule import TargetResponderRecipeResponderRule
from .target_responder_recipe_responder_rule_collection import TargetResponderRecipeResponderRuleCollection
from .target_responder_recipe_responder_rule_summary import TargetResponderRecipeResponderRuleSummary
from .target_responder_recipe_summary import TargetResponderRecipeSummary
from .target_summary import TargetSummary
from .trigger_responder_details import TriggerResponderDetails
from .update_bulk_problem_status_details import UpdateBulkProblemStatusDetails
from .update_configuration_details import UpdateConfigurationDetails
from .update_detector_recipe_details import UpdateDetectorRecipeDetails
from .update_detector_recipe_detector_rule import UpdateDetectorRecipeDetectorRule
from .update_detector_recipe_detector_rule_details import UpdateDetectorRecipeDetectorRuleDetails
from .update_detector_rule_details import UpdateDetectorRuleDetails
from .update_managed_list_details import UpdateManagedListDetails
from .update_problem_status_details import UpdateProblemStatusDetails
from .update_responder_recipe_details import UpdateResponderRecipeDetails
from .update_responder_recipe_responder_rule import UpdateResponderRecipeResponderRule
from .update_responder_recipe_responder_rule_details import UpdateResponderRecipeResponderRuleDetails
from .update_responder_rule_details import UpdateResponderRuleDetails
from .update_target_details import UpdateTargetDetails
from .update_target_detector_recipe import UpdateTargetDetectorRecipe
from .update_target_detector_recipe_details import UpdateTargetDetectorRecipeDetails
from .update_target_detector_recipe_detector_rule_details import UpdateTargetDetectorRecipeDetectorRuleDetails
from .update_target_detector_rule_details import UpdateTargetDetectorRuleDetails
from .update_target_recipe_detector_rule_details import UpdateTargetRecipeDetectorRuleDetails
from .update_target_recipe_responder_rule_details import UpdateTargetRecipeResponderRuleDetails
from .update_target_responder_recipe import UpdateTargetResponderRecipe
from .update_target_responder_recipe_details import UpdateTargetResponderRecipeDetails
from .update_target_responder_recipe_responder_rule_details import UpdateTargetResponderRecipeResponderRuleDetails
from .update_target_responder_rule_details import UpdateTargetResponderRuleDetails

# Maps type names to classes for cloud_guard services.
cloud_guard_type_mapping = {
    "ActivityProblemAggregation": ActivityProblemAggregation,
    "ActivityProblemAggregationCollection": ActivityProblemAggregationCollection,
    "AttachTargetDetectorRecipeDetails": AttachTargetDetectorRecipeDetails,
    "AttachTargetResponderRecipeDetails": AttachTargetResponderRecipeDetails,
    "CandidateResponderRule": CandidateResponderRule,
    "ChangeDetectorRecipeCompartmentDetails": ChangeDetectorRecipeCompartmentDetails,
    "ChangeManagedListCompartmentDetails": ChangeManagedListCompartmentDetails,
    "ChangeResponderRecipeCompartmentDetails": ChangeResponderRecipeCompartmentDetails,
    "CompositeCondition": CompositeCondition,
    "Condition": Condition,
    "ConditionGroup": ConditionGroup,
    "ConditionMetadataType": ConditionMetadataType,
    "ConditionMetadataTypeCollection": ConditionMetadataTypeCollection,
    "ConditionMetadataTypeSummary": ConditionMetadataTypeSummary,
    "ConditionOperator": ConditionOperator,
    "ConfigValue": ConfigValue,
    "Configuration": Configuration,
    "CreateDetectorRecipeDetails": CreateDetectorRecipeDetails,
    "CreateManagedListDetails": CreateManagedListDetails,
    "CreateResponderRecipeDetails": CreateResponderRecipeDetails,
    "CreateTargetDetails": CreateTargetDetails,
    "CreateTargetDetectorRecipeDetails": CreateTargetDetectorRecipeDetails,
    "CreateTargetResponderRecipeDetails": CreateTargetResponderRecipeDetails,
    "Detector": Detector,
    "DetectorCollection": DetectorCollection,
    "DetectorConfiguration": DetectorConfiguration,
    "DetectorDetails": DetectorDetails,
    "DetectorRecipe": DetectorRecipe,
    "DetectorRecipeCollection": DetectorRecipeCollection,
    "DetectorRecipeDetectorRule": DetectorRecipeDetectorRule,
    "DetectorRecipeDetectorRuleCollection": DetectorRecipeDetectorRuleCollection,
    "DetectorRecipeDetectorRuleSummary": DetectorRecipeDetectorRuleSummary,
    "DetectorRecipeSummary": DetectorRecipeSummary,
    "DetectorRule": DetectorRule,
    "DetectorRuleCollection": DetectorRuleCollection,
    "DetectorRuleSummary": DetectorRuleSummary,
    "DetectorSummary": DetectorSummary,
    "ExecuteResponderExecutionDetails": ExecuteResponderExecutionDetails,
    "GeographicalLocation": GeographicalLocation,
    "ImpactedResourceCollection": ImpactedResourceCollection,
    "ImpactedResourceSummary": ImpactedResourceSummary,
    "ManagedList": ManagedList,
    "ManagedListCollection": ManagedListCollection,
    "ManagedListSummary": ManagedListSummary,
    "ManagedListTypeCollection": ManagedListTypeCollection,
    "ManagedListTypeSummary": ManagedListTypeSummary,
    "OperatorSummary": OperatorSummary,
    "PoliticalLocation": PoliticalLocation,
    "Problem": Problem,
    "ProblemAggregation": ProblemAggregation,
    "ProblemAggregationCollection": ProblemAggregationCollection,
    "ProblemCollection": ProblemCollection,
    "ProblemHistoryCollection": ProblemHistoryCollection,
    "ProblemHistorySummary": ProblemHistorySummary,
    "ProblemSummary": ProblemSummary,
    "ProblemTrendAggregation": ProblemTrendAggregation,
    "ProblemTrendAggregationCollection": ProblemTrendAggregationCollection,
    "RecommendationSummary": RecommendationSummary,
    "RecommendationSummaryCollection": RecommendationSummaryCollection,
    "ResourceTypeCollection": ResourceTypeCollection,
    "ResourceTypeSummary": ResourceTypeSummary,
    "ResponderActivityCollection": ResponderActivityCollection,
    "ResponderActivitySummary": ResponderActivitySummary,
    "ResponderConfiguration": ResponderConfiguration,
    "ResponderExecution": ResponderExecution,
    "ResponderExecutionAggregation": ResponderExecutionAggregation,
    "ResponderExecutionAggregationCollection": ResponderExecutionAggregationCollection,
    "ResponderExecutionCollection": ResponderExecutionCollection,
    "ResponderExecutionSummary": ResponderExecutionSummary,
    "ResponderExecutionTrendAggregation": ResponderExecutionTrendAggregation,
    "ResponderExecutionTrendAggregationCollection": ResponderExecutionTrendAggregationCollection,
    "ResponderRecipe": ResponderRecipe,
    "ResponderRecipeCollection": ResponderRecipeCollection,
    "ResponderRecipeResponderRule": ResponderRecipeResponderRule,
    "ResponderRecipeResponderRuleCollection": ResponderRecipeResponderRuleCollection,
    "ResponderRecipeResponderRuleSummary": ResponderRecipeResponderRuleSummary,
    "ResponderRecipeSummary": ResponderRecipeSummary,
    "ResponderRule": ResponderRule,
    "ResponderRuleCollection": ResponderRuleCollection,
    "ResponderRuleDetails": ResponderRuleDetails,
    "ResponderRuleExecutionDetails": ResponderRuleExecutionDetails,
    "ResponderRuleSummary": ResponderRuleSummary,
    "RiskScoreAggregation": RiskScoreAggregation,
    "RiskScoreAggregationCollection": RiskScoreAggregationCollection,
    "RuleSummary": RuleSummary,
    "SecurityScoreAggregation": SecurityScoreAggregation,
    "SecurityScoreAggregationCollection": SecurityScoreAggregationCollection,
    "SecurityScoreTrendAggregation": SecurityScoreTrendAggregation,
    "SecurityScoreTrendAggregationCollection": SecurityScoreTrendAggregationCollection,
    "ServiceTypeSummary": ServiceTypeSummary,
    "SimpleCondition": SimpleCondition,
    "SkipBulkResponderExecutionDetails": SkipBulkResponderExecutionDetails,
    "Target": Target,
    "TargetCollection": TargetCollection,
    "TargetDetectorDetails": TargetDetectorDetails,
    "TargetDetectorRecipe": TargetDetectorRecipe,
    "TargetDetectorRecipeCollection": TargetDetectorRecipeCollection,
    "TargetDetectorRecipeDetectorRule": TargetDetectorRecipeDetectorRule,
    "TargetDetectorRecipeDetectorRuleCollection": TargetDetectorRecipeDetectorRuleCollection,
    "TargetDetectorRecipeDetectorRuleSummary": TargetDetectorRecipeDetectorRuleSummary,
    "TargetDetectorRecipeSummary": TargetDetectorRecipeSummary,
    "TargetResponderRecipe": TargetResponderRecipe,
    "TargetResponderRecipeCollection": TargetResponderRecipeCollection,
    "TargetResponderRecipeResponderRule": TargetResponderRecipeResponderRule,
    "TargetResponderRecipeResponderRuleCollection": TargetResponderRecipeResponderRuleCollection,
    "TargetResponderRecipeResponderRuleSummary": TargetResponderRecipeResponderRuleSummary,
    "TargetResponderRecipeSummary": TargetResponderRecipeSummary,
    "TargetSummary": TargetSummary,
    "TriggerResponderDetails": TriggerResponderDetails,
    "UpdateBulkProblemStatusDetails": UpdateBulkProblemStatusDetails,
    "UpdateConfigurationDetails": UpdateConfigurationDetails,
    "UpdateDetectorRecipeDetails": UpdateDetectorRecipeDetails,
    "UpdateDetectorRecipeDetectorRule": UpdateDetectorRecipeDetectorRule,
    "UpdateDetectorRecipeDetectorRuleDetails": UpdateDetectorRecipeDetectorRuleDetails,
    "UpdateDetectorRuleDetails": UpdateDetectorRuleDetails,
    "UpdateManagedListDetails": UpdateManagedListDetails,
    "UpdateProblemStatusDetails": UpdateProblemStatusDetails,
    "UpdateResponderRecipeDetails": UpdateResponderRecipeDetails,
    "UpdateResponderRecipeResponderRule": UpdateResponderRecipeResponderRule,
    "UpdateResponderRecipeResponderRuleDetails": UpdateResponderRecipeResponderRuleDetails,
    "UpdateResponderRuleDetails": UpdateResponderRuleDetails,
    "UpdateTargetDetails": UpdateTargetDetails,
    "UpdateTargetDetectorRecipe": UpdateTargetDetectorRecipe,
    "UpdateTargetDetectorRecipeDetails": UpdateTargetDetectorRecipeDetails,
    "UpdateTargetDetectorRecipeDetectorRuleDetails": UpdateTargetDetectorRecipeDetectorRuleDetails,
    "UpdateTargetDetectorRuleDetails": UpdateTargetDetectorRuleDetails,
    "UpdateTargetRecipeDetectorRuleDetails": UpdateTargetRecipeDetectorRuleDetails,
    "UpdateTargetRecipeResponderRuleDetails": UpdateTargetRecipeResponderRuleDetails,
    "UpdateTargetResponderRecipe": UpdateTargetResponderRecipe,
    "UpdateTargetResponderRecipeDetails": UpdateTargetResponderRecipeDetails,
    "UpdateTargetResponderRecipeResponderRuleDetails": UpdateTargetResponderRecipeResponderRuleDetails,
    "UpdateTargetResponderRuleDetails": UpdateTargetResponderRuleDetails
}
