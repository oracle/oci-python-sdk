# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .abstract_call_attribute import AbstractCallAttribute
from .abstract_data_operation_config import AbstractDataOperationConfig
from .abstract_field import AbstractField
from .abstract_format_attribute import AbstractFormatAttribute
from .abstract_formatted_text import AbstractFormattedText
from .abstract_frequency_details import AbstractFrequencyDetails
from .abstract_read_attribute import AbstractReadAttribute
from .abstract_write_attribute import AbstractWriteAttribute
from .aggregator import Aggregator
from .aggregator_summary import AggregatorSummary
from .application import Application
from .application_details import ApplicationDetails
from .application_summary import ApplicationSummary
from .application_summary_collection import ApplicationSummaryCollection
from .array_type import ArrayType
from .auth_config import AuthConfig
from .auth_details import AuthDetails
from .avro_format_attribute import AvroFormatAttribute
from .base_type import BaseType
from .bicc_read_attributes import BiccReadAttributes
from .bip_call_attribute import BipCallAttribute
from .bip_read_attributes import BipReadAttributes
from .bip_report_parameter_value import BipReportParameterValue
from .cancel_rest_call_config import CancelRestCallConfig
from .change_compartment_details import ChangeCompartmentDetails
from .change_dis_application_compartment_details import ChangeDisApplicationCompartmentDetails
from .child_reference import ChildReference
from .child_reference_detail import ChildReferenceDetail
from .composite_field_map import CompositeFieldMap
from .composite_type import CompositeType
from .compression import Compression
from .conditional_composite_field_map import ConditionalCompositeFieldMap
from .conditional_input_link import ConditionalInputLink
from .conditional_output_port import ConditionalOutputPort
from .config_definition import ConfigDefinition
from .config_parameter_definition import ConfigParameterDefinition
from .config_parameter_value import ConfigParameterValue
from .config_provider import ConfigProvider
from .config_values import ConfigValues
from .configuration_details import ConfigurationDetails
from .configured_type import ConfiguredType
from .connection import Connection
from .connection_details import ConnectionDetails
from .connection_from_adwc import ConnectionFromAdwc
from .connection_from_adwc_details import ConnectionFromAdwcDetails
from .connection_from_amazon_s3 import ConnectionFromAmazonS3
from .connection_from_amazon_s3_details import ConnectionFromAmazonS3Details
from .connection_from_atp import ConnectionFromAtp
from .connection_from_atp_details import ConnectionFromAtpDetails
from .connection_from_bicc import ConnectionFromBICC
from .connection_from_bicc_details import ConnectionFromBICCDetails
from .connection_from_bip import ConnectionFromBIP
from .connection_from_bip_details import ConnectionFromBipDetails
from .connection_from_jdbc import ConnectionFromJdbc
from .connection_from_jdbc_details import ConnectionFromJdbcDetails
from .connection_from_lakehouse import ConnectionFromLakehouse
from .connection_from_lakehouse_details import ConnectionFromLakehouseDetails
from .connection_from_my_sql import ConnectionFromMySQL
from .connection_from_my_sql_details import ConnectionFromMySQLDetails
from .connection_from_object_storage import ConnectionFromObjectStorage
from .connection_from_object_storage_details import ConnectionFromObjectStorageDetails
from .connection_from_oracle import ConnectionFromOracle
from .connection_from_oracle_details import ConnectionFromOracleDetails
from .connection_from_rest_basic_auth import ConnectionFromRestBasicAuth
from .connection_from_rest_basic_auth_details import ConnectionFromRestBasicAuthDetails
from .connection_from_rest_no_auth import ConnectionFromRestNoAuth
from .connection_from_rest_no_auth_details import ConnectionFromRestNoAuthDetails
from .connection_property import ConnectionProperty
from .connection_summary import ConnectionSummary
from .connection_summary_collection import ConnectionSummaryCollection
from .connection_summary_from_adwc import ConnectionSummaryFromAdwc
from .connection_summary_from_amazon_s3 import ConnectionSummaryFromAmazonS3
from .connection_summary_from_atp import ConnectionSummaryFromAtp
from .connection_summary_from_bicc import ConnectionSummaryFromBICC
from .connection_summary_from_bip import ConnectionSummaryFromBIP
from .connection_summary_from_jdbc import ConnectionSummaryFromJdbc
from .connection_summary_from_lakehouse import ConnectionSummaryFromLakehouse
from .connection_summary_from_my_sql import ConnectionSummaryFromMySQL
from .connection_summary_from_object_storage import ConnectionSummaryFromObjectStorage
from .connection_summary_from_oracle import ConnectionSummaryFromOracle
from .connection_summary_from_rest_basic_auth import ConnectionSummaryFromRestBasicAuth
from .connection_summary_from_rest_no_auth import ConnectionSummaryFromRestNoAuth
from .connection_validation import ConnectionValidation
from .connection_validation_summary import ConnectionValidationSummary
from .connection_validation_summary_collection import ConnectionValidationSummaryCollection
from .connector_attribute import ConnectorAttribute
from .count_statistic import CountStatistic
from .count_statistic_summary import CountStatisticSummary
from .create_application_details import CreateApplicationDetails
from .create_config_provider import CreateConfigProvider
from .create_connection_details import CreateConnectionDetails
from .create_connection_from_adwc import CreateConnectionFromAdwc
from .create_connection_from_amazon_s3 import CreateConnectionFromAmazonS3
from .create_connection_from_atp import CreateConnectionFromAtp
from .create_connection_from_bicc import CreateConnectionFromBICC
from .create_connection_from_bip import CreateConnectionFromBIP
from .create_connection_from_jdbc import CreateConnectionFromJdbc
from .create_connection_from_lakehouse import CreateConnectionFromLakehouse
from .create_connection_from_my_sql import CreateConnectionFromMySQL
from .create_connection_from_object_storage import CreateConnectionFromObjectStorage
from .create_connection_from_oracle import CreateConnectionFromOracle
from .create_connection_from_rest_basic_auth import CreateConnectionFromRestBasicAuth
from .create_connection_from_rest_no_auth import CreateConnectionFromRestNoAuth
from .create_connection_validation_details import CreateConnectionValidationDetails
from .create_data_asset_details import CreateDataAssetDetails
from .create_data_asset_from_adwc import CreateDataAssetFromAdwc
from .create_data_asset_from_amazon_s3 import CreateDataAssetFromAmazonS3
from .create_data_asset_from_atp import CreateDataAssetFromAtp
from .create_data_asset_from_fusion_app import CreateDataAssetFromFusionApp
from .create_data_asset_from_jdbc import CreateDataAssetFromJdbc
from .create_data_asset_from_lakehouse import CreateDataAssetFromLakehouse
from .create_data_asset_from_my_sql import CreateDataAssetFromMySQL
from .create_data_asset_from_object_storage import CreateDataAssetFromObjectStorage
from .create_data_asset_from_oracle import CreateDataAssetFromOracle
from .create_data_asset_from_rest import CreateDataAssetFromRest
from .create_data_flow_details import CreateDataFlowDetails
from .create_data_flow_validation_details import CreateDataFlowValidationDetails
from .create_dis_application_details import CreateDisApplicationDetails
from .create_entity_shape_details import CreateEntityShapeDetails
from .create_entity_shape_from_file import CreateEntityShapeFromFile
from .create_entity_shape_from_sql import CreateEntityShapeFromSQL
from .create_external_publication_details import CreateExternalPublicationDetails
from .create_external_publication_validation_details import CreateExternalPublicationValidationDetails
from .create_folder_details import CreateFolderDetails
from .create_function_library_details import CreateFunctionLibraryDetails
from .create_patch_details import CreatePatchDetails
from .create_pipeline_details import CreatePipelineDetails
from .create_pipeline_validation_details import CreatePipelineValidationDetails
from .create_project_details import CreateProjectDetails
from .create_schedule_details import CreateScheduleDetails
from .create_source_application_info import CreateSourceApplicationInfo
from .create_task_details import CreateTaskDetails
from .create_task_from_data_loader_task import CreateTaskFromDataLoaderTask
from .create_task_from_integration_task import CreateTaskFromIntegrationTask
from .create_task_from_oci_dataflow_task import CreateTaskFromOCIDataflowTask
from .create_task_from_pipeline_task import CreateTaskFromPipelineTask
from .create_task_from_rest_task import CreateTaskFromRestTask
from .create_task_from_sql_task import CreateTaskFromSQLTask
from .create_task_run_details import CreateTaskRunDetails
from .create_task_schedule_details import CreateTaskScheduleDetails
from .create_task_validation_details import CreateTaskValidationDetails
from .create_task_validation_from_data_loader_task import CreateTaskValidationFromDataLoaderTask
from .create_task_validation_from_integration_task import CreateTaskValidationFromIntegrationTask
from .create_task_validation_from_pipeline_task import CreateTaskValidationFromPipelineTask
from .create_user_defined_function_details import CreateUserDefinedFunctionDetails
from .create_user_defined_function_validation_details import CreateUserDefinedFunctionValidationDetails
from .create_workspace_details import CreateWorkspaceDetails
from .csv_format_attribute import CsvFormatAttribute
from .custom_frequency_details import CustomFrequencyDetails
from .daily_frequency_details import DailyFrequencyDetails
from .data_asset import DataAsset
from .data_asset_from_adwc_details import DataAssetFromAdwcDetails
from .data_asset_from_amazon_s3 import DataAssetFromAmazonS3
from .data_asset_from_atp_details import DataAssetFromAtpDetails
from .data_asset_from_fusion_app import DataAssetFromFusionApp
from .data_asset_from_jdbc import DataAssetFromJdbc
from .data_asset_from_lakehouse_details import DataAssetFromLakehouseDetails
from .data_asset_from_my_sql import DataAssetFromMySQL
from .data_asset_from_object_storage_details import DataAssetFromObjectStorageDetails
from .data_asset_from_oracle_details import DataAssetFromOracleDetails
from .data_asset_from_rest_details import DataAssetFromRestDetails
from .data_asset_summary import DataAssetSummary
from .data_asset_summary_collection import DataAssetSummaryCollection
from .data_asset_summary_from_adwc import DataAssetSummaryFromAdwc
from .data_asset_summary_from_amazon_s3 import DataAssetSummaryFromAmazonS3
from .data_asset_summary_from_atp import DataAssetSummaryFromAtp
from .data_asset_summary_from_fusion_app import DataAssetSummaryFromFusionApp
from .data_asset_summary_from_jdbc import DataAssetSummaryFromJdbc
from .data_asset_summary_from_lakehouse import DataAssetSummaryFromLakehouse
from .data_asset_summary_from_my_sql import DataAssetSummaryFromMySQL
from .data_asset_summary_from_object_storage import DataAssetSummaryFromObjectStorage
from .data_asset_summary_from_oracle import DataAssetSummaryFromOracle
from .data_asset_summary_from_rest import DataAssetSummaryFromRest
from .data_entity import DataEntity
from .data_entity_details import DataEntityDetails
from .data_entity_from_data_store import DataEntityFromDataStore
from .data_entity_from_data_store_entity_details import DataEntityFromDataStoreEntityDetails
from .data_entity_from_file import DataEntityFromFile
from .data_entity_from_file_entity_details import DataEntityFromFileEntityDetails
from .data_entity_from_sql import DataEntityFromSql
from .data_entity_from_sql_entity_details import DataEntityFromSqlEntityDetails
from .data_entity_from_table import DataEntityFromTable
from .data_entity_from_table_entity_details import DataEntityFromTableEntityDetails
from .data_entity_from_view import DataEntityFromView
from .data_entity_from_view_entity_details import DataEntityFromViewEntityDetails
from .data_entity_summary import DataEntitySummary
from .data_entity_summary_collection import DataEntitySummaryCollection
from .data_entity_summary_from_data_store import DataEntitySummaryFromDataStore
from .data_entity_summary_from_file import DataEntitySummaryFromFile
from .data_entity_summary_from_sql import DataEntitySummaryFromSql
from .data_entity_summary_from_table import DataEntitySummaryFromTable
from .data_entity_summary_from_view import DataEntitySummaryFromView
from .data_flow import DataFlow
from .data_flow_details import DataFlowDetails
from .data_flow_summary import DataFlowSummary
from .data_flow_summary_collection import DataFlowSummaryCollection
from .data_flow_validation import DataFlowValidation
from .data_flow_validation_summary import DataFlowValidationSummary
from .data_flow_validation_summary_collection import DataFlowValidationSummaryCollection
from .data_format import DataFormat
from .data_type import DataType
from .dataflow_application import DataflowApplication
from .decision_operator import DecisionOperator
from .decision_output_port import DecisionOutputPort
from .dependent_object import DependentObject
from .dependent_object_summary import DependentObjectSummary
from .dependent_object_summary_collection import DependentObjectSummaryCollection
from .derived_entity import DerivedEntity
from .derived_field import DerivedField
from .derived_type import DerivedType
from .direct_field_map import DirectFieldMap
from .direct_named_field_map import DirectNamedFieldMap
from .dis_application import DisApplication
from .dis_application_summary import DisApplicationSummary
from .dis_application_summary_collection import DisApplicationSummaryCollection
from .distinct import Distinct
from .dynamic_input_field import DynamicInputField
from .dynamic_proxy_field import DynamicProxyField
from .dynamic_type import DynamicType
from .dynamic_type_handler import DynamicTypeHandler
from .end_operator import EndOperator
from .enriched_entity import EnrichedEntity
from .entity_shape import EntityShape
from .entity_shape_from_file import EntityShapeFromFile
from .entity_shape_from_sql import EntityShapeFromSQL
from .error_details import ErrorDetails
from .execute_rest_call_config import ExecuteRestCallConfig
from .expression import Expression
from .expression_operator import ExpressionOperator
from .external_publication import ExternalPublication
from .external_publication_summary import ExternalPublicationSummary
from .external_publication_summary_collection import ExternalPublicationSummaryCollection
from .external_publication_validation import ExternalPublicationValidation
from .external_publication_validation_summary import ExternalPublicationValidationSummary
from .external_publication_validation_summary_collection import ExternalPublicationValidationSummaryCollection
from .external_storage import ExternalStorage
from .field_map import FieldMap
from .field_map_wrapper import FieldMapWrapper
from .filter import Filter
from .filter_push import FilterPush
from .flatten import Flatten
from .flatten_details import FlattenDetails
from .flatten_projection_preferences import FlattenProjectionPreferences
from .flatten_type_handler import FlattenTypeHandler
from .flow_node import FlowNode
from .flow_port import FlowPort
from .flow_port_link import FlowPortLink
from .folder import Folder
from .folder_details import FolderDetails
from .folder_summary import FolderSummary
from .folder_summary_collection import FolderSummaryCollection
from .foreign_key import ForeignKey
from .function import Function
from .function_configuration_definition import FunctionConfigurationDefinition
from .function_library import FunctionLibrary
from .function_library_details import FunctionLibraryDetails
from .function_library_summary import FunctionLibrarySummary
from .function_library_summary_collection import FunctionLibrarySummaryCollection
from .function_signature import FunctionSignature
from .generic_rest_api_attributes import GenericRestApiAttributes
from .generic_rest_call_attribute import GenericRestCallAttribute
from .grouped_name_pattern_rule import GroupedNamePatternRule
from .hourly_frequency_details import HourlyFrequencyDetails
from .input_field import InputField
from .input_link import InputLink
from .input_port import InputPort
from .input_proxy_field import InputProxyField
from .intersect import Intersect
from .java_type import JavaType
from .join import Join
from .joiner import Joiner
from .json_format_attribute import JsonFormatAttribute
from .json_text import JsonText
from .key import Key
from .key_attribute import KeyAttribute
from .key_range import KeyRange
from .key_range_partition_config import KeyRangePartitionConfig
from .last_run_details import LastRunDetails
from .lookup import Lookup
from .macro_field import MacroField
from .macro_pivot_field import MacroPivotField
from .map_type import MapType
from .materialized_composite_type import MaterializedCompositeType
from .materialized_dynamic_field import MaterializedDynamicField
from .merge_operator import MergeOperator
from .message import Message
from .minus import Minus
from .monthly_frequency_details import MonthlyFrequencyDetails
from .monthly_rule_frequency_details import MonthlyRuleFrequencyDetails
from .name_list_rule import NameListRule
from .name_pattern_rule import NamePatternRule
from .named_entity_map import NamedEntityMap
from .native_shape_field import NativeShapeField
from .object_metadata import ObjectMetadata
from .object_storage_write_attribute import ObjectStorageWriteAttribute
from .object_storage_write_attributes import ObjectStorageWriteAttributes
from .oci_function import OciFunction
from .oci_vault_secret_config import OciVaultSecretConfig
from .operation import Operation
from .operation_from_api import OperationFromApi
from .operation_from_procedure import OperationFromProcedure
from .operator import Operator
from .oracle_adwc_write_attribute import OracleAdwcWriteAttribute
from .oracle_adwc_write_attributes import OracleAdwcWriteAttributes
from .oracle_atp_write_attribute import OracleAtpWriteAttribute
from .oracle_atp_write_attributes import OracleAtpWriteAttributes
from .oracle_read_attribute import OracleReadAttribute
from .oracle_read_attributes import OracleReadAttributes
from .oracle_write_attribute import OracleWriteAttribute
from .oracle_write_attributes import OracleWriteAttributes
from .output_field import OutputField
from .output_link import OutputLink
from .output_port import OutputPort
from .parameter import Parameter
from .parameter_value import ParameterValue
from .parent_reference import ParentReference
from .parquet_format_attribute import ParquetFormatAttribute
from .partition_config import PartitionConfig
from .patch import Patch
from .patch_change_summary import PatchChangeSummary
from .patch_change_summary_collection import PatchChangeSummaryCollection
from .patch_object_metadata import PatchObjectMetadata
from .patch_summary import PatchSummary
from .patch_summary_collection import PatchSummaryCollection
from .pipeline import Pipeline
from .pipeline_summary import PipelineSummary
from .pipeline_summary_collection import PipelineSummaryCollection
from .pipeline_validation import PipelineValidation
from .pipeline_validation_summary import PipelineValidationSummary
from .pipeline_validation_summary_collection import PipelineValidationSummaryCollection
from .pivot import Pivot
from .pivot_field import PivotField
from .pivot_keys import PivotKeys
from .poll_rest_call_config import PollRestCallConfig
from .primary_key import PrimaryKey
from .project import Project
from .project_details import ProjectDetails
from .project_summary import ProjectSummary
from .project_summary_collection import ProjectSummaryCollection
from .projection import Projection
from .projection_rule import ProjectionRule
from .proxy_field import ProxyField
from .published_object import PublishedObject
from .published_object_from_data_loader_task import PublishedObjectFromDataLoaderTask
from .published_object_from_integration_task import PublishedObjectFromIntegrationTask
from .published_object_from_pipeline_task import PublishedObjectFromPipelineTask
from .published_object_from_pipeline_task_summary import PublishedObjectFromPipelineTaskSummary
from .published_object_summary import PublishedObjectSummary
from .published_object_summary_collection import PublishedObjectSummaryCollection
from .published_object_summary_from_data_loader_task import PublishedObjectSummaryFromDataLoaderTask
from .published_object_summary_from_integration_task import PublishedObjectSummaryFromIntegrationTask
from .push_down_operation import PushDownOperation
from .query import Query
from .read_operation_config import ReadOperationConfig
from .reference import Reference
from .reference_summary import ReferenceSummary
from .reference_summary_collection import ReferenceSummaryCollection
from .reference_used_by import ReferenceUsedBy
from .referenced_data_object import ReferencedDataObject
from .referenced_data_object_from_api import ReferencedDataObjectFromAPI
from .referenced_data_object_from_procedure import ReferencedDataObjectFromProcedure
from .registry_metadata import RegistryMetadata
from .rename_rule import RenameRule
from .resource_configuration import ResourceConfiguration
from .resource_principal_auth_config import ResourcePrincipalAuthConfig
from .rest_call_config import RestCallConfig
from .root_object import RootObject
from .rule_based_entity_map import RuleBasedEntityMap
from .rule_based_field_map import RuleBasedFieldMap
from .rule_type_config import RuleTypeConfig
from .runtime_operator import RuntimeOperator
from .runtime_operator_summary import RuntimeOperatorSummary
from .runtime_operator_summary_collection import RuntimeOperatorSummaryCollection
from .runtime_pipeline import RuntimePipeline
from .runtime_pipeline_summary import RuntimePipelineSummary
from .runtime_pipeline_summary_collection import RuntimePipelineSummaryCollection
from .schedule import Schedule
from .schedule_summary import ScheduleSummary
from .schedule_summary_collection import ScheduleSummaryCollection
from .schema import Schema
from .schema_drift_config import SchemaDriftConfig
from .schema_summary import SchemaSummary
from .schema_summary_collection import SchemaSummaryCollection
from .scope_reference import ScopeReference
from .script import Script
from .secret_config import SecretConfig
from .select import Select
from .sensitive_attribute import SensitiveAttribute
from .shape import Shape
from .shape_field import ShapeField
from .sort import Sort
from .sort_clause import SortClause
from .sort_key import SortKey
from .sort_key_rule import SortKeyRule
from .sort_oper import SortOper
from .source import Source
from .source_application_info import SourceApplicationInfo
from .split import Split
from .start_operator import StartOperator
from .structured_type import StructuredType
from .target import Target
from .task import Task
from .task_from_data_loader_task_details import TaskFromDataLoaderTaskDetails
from .task_from_integration_task_details import TaskFromIntegrationTaskDetails
from .task_from_oci_dataflow_task_details import TaskFromOCIDataflowTaskDetails
from .task_from_pipeline_task_details import TaskFromPipelineTaskDetails
from .task_from_rest_task_details import TaskFromRestTaskDetails
from .task_from_sql_task_details import TaskFromSQLTaskDetails
from .task_operator import TaskOperator
from .task_run import TaskRun
from .task_run_details import TaskRunDetails
from .task_run_lineage_details import TaskRunLineageDetails
from .task_run_lineage_summary import TaskRunLineageSummary
from .task_run_lineage_summary_collection import TaskRunLineageSummaryCollection
from .task_run_log_summary import TaskRunLogSummary
from .task_run_summary import TaskRunSummary
from .task_run_summary_collection import TaskRunSummaryCollection
from .task_schedule import TaskSchedule
from .task_schedule_summary import TaskScheduleSummary
from .task_schedule_summary_collection import TaskScheduleSummaryCollection
from .task_summary import TaskSummary
from .task_summary_collection import TaskSummaryCollection
from .task_summary_from_data_loader_task import TaskSummaryFromDataLoaderTask
from .task_summary_from_integration_task import TaskSummaryFromIntegrationTask
from .task_summary_from_oci_dataflow_task import TaskSummaryFromOCIDataflowTask
from .task_summary_from_pipeline_task import TaskSummaryFromPipelineTask
from .task_summary_from_rest_task import TaskSummaryFromRestTask
from .task_summary_from_sql_task import TaskSummaryFromSQLTask
from .task_validation import TaskValidation
from .task_validation_summary import TaskValidationSummary
from .task_validation_summary_collection import TaskValidationSummaryCollection
from .template_summary import TemplateSummary
from .template_summary_collection import TemplateSummaryCollection
from .time import Time
from .type_library import TypeLibrary
from .type_list_rule import TypeListRule
from .type_system import TypeSystem
from .typed_expression import TypedExpression
from .typed_name_pattern_rule import TypedNamePatternRule
from .typed_object import TypedObject
from .typed_object_wrapper import TypedObjectWrapper
from .ui_properties import UIProperties
from .union import Union
from .unique_data_key import UniqueDataKey
from .unique_key import UniqueKey
from .update_application_details import UpdateApplicationDetails
from .update_connection_details import UpdateConnectionDetails
from .update_connection_from_adwc import UpdateConnectionFromAdwc
from .update_connection_from_amazon_s3 import UpdateConnectionFromAmazonS3
from .update_connection_from_atp import UpdateConnectionFromAtp
from .update_connection_from_bicc import UpdateConnectionFromBICC
from .update_connection_from_bip import UpdateConnectionFromBIP
from .update_connection_from_jdbc import UpdateConnectionFromJdbc
from .update_connection_from_lakehouse import UpdateConnectionFromLakehouse
from .update_connection_from_my_sql import UpdateConnectionFromMySQL
from .update_connection_from_object_storage import UpdateConnectionFromObjectStorage
from .update_connection_from_oracle import UpdateConnectionFromOracle
from .update_connection_from_rest_basic_auth import UpdateConnectionFromRestBasicAuth
from .update_connection_from_rest_no_auth import UpdateConnectionFromRestNoAuth
from .update_data_asset_details import UpdateDataAssetDetails
from .update_data_asset_from_adwc import UpdateDataAssetFromAdwc
from .update_data_asset_from_amazon_s3 import UpdateDataAssetFromAmazonS3
from .update_data_asset_from_atp import UpdateDataAssetFromAtp
from .update_data_asset_from_fusion_app import UpdateDataAssetFromFusionApp
from .update_data_asset_from_jdbc import UpdateDataAssetFromJdbc
from .update_data_asset_from_lakehouse import UpdateDataAssetFromLakehouse
from .update_data_asset_from_my_sql import UpdateDataAssetFromMySQL
from .update_data_asset_from_object_storage import UpdateDataAssetFromObjectStorage
from .update_data_asset_from_oracle import UpdateDataAssetFromOracle
from .update_data_asset_from_rest import UpdateDataAssetFromRest
from .update_data_flow_details import UpdateDataFlowDetails
from .update_dis_application_details import UpdateDisApplicationDetails
from .update_external_publication_details import UpdateExternalPublicationDetails
from .update_folder_details import UpdateFolderDetails
from .update_function_library_details import UpdateFunctionLibraryDetails
from .update_pipeline_details import UpdatePipelineDetails
from .update_project_details import UpdateProjectDetails
from .update_reference_details import UpdateReferenceDetails
from .update_schedule_details import UpdateScheduleDetails
from .update_task_details import UpdateTaskDetails
from .update_task_from_data_loader_task import UpdateTaskFromDataLoaderTask
from .update_task_from_integration_task import UpdateTaskFromIntegrationTask
from .update_task_from_oci_dataflow_task import UpdateTaskFromOCIDataflowTask
from .update_task_from_pipeline_task import UpdateTaskFromPipelineTask
from .update_task_from_rest_task import UpdateTaskFromRestTask
from .update_task_from_sql_task import UpdateTaskFromSQLTask
from .update_task_run_details import UpdateTaskRunDetails
from .update_task_schedule_details import UpdateTaskScheduleDetails
from .update_user_defined_function_details import UpdateUserDefinedFunctionDetails
from .update_workspace_details import UpdateWorkspaceDetails
from .user_defined_function import UserDefinedFunction
from .user_defined_function_details import UserDefinedFunctionDetails
from .user_defined_function_summary import UserDefinedFunctionSummary
from .user_defined_function_summary_collection import UserDefinedFunctionSummaryCollection
from .user_defined_function_validation import UserDefinedFunctionValidation
from .user_defined_function_validation_summary import UserDefinedFunctionValidationSummary
from .user_defined_function_validation_summary_collection import UserDefinedFunctionValidationSummaryCollection
from .validation_message import ValidationMessage
from .variable import Variable
from .weekly_frequency_details import WeeklyFrequencyDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .workspace import Workspace
from .workspace_summary import WorkspaceSummary
from .write_operation_config import WriteOperationConfig

# Maps type names to classes for data_integration services.
data_integration_type_mapping = {
    "AbstractCallAttribute": AbstractCallAttribute,
    "AbstractDataOperationConfig": AbstractDataOperationConfig,
    "AbstractField": AbstractField,
    "AbstractFormatAttribute": AbstractFormatAttribute,
    "AbstractFormattedText": AbstractFormattedText,
    "AbstractFrequencyDetails": AbstractFrequencyDetails,
    "AbstractReadAttribute": AbstractReadAttribute,
    "AbstractWriteAttribute": AbstractWriteAttribute,
    "Aggregator": Aggregator,
    "AggregatorSummary": AggregatorSummary,
    "Application": Application,
    "ApplicationDetails": ApplicationDetails,
    "ApplicationSummary": ApplicationSummary,
    "ApplicationSummaryCollection": ApplicationSummaryCollection,
    "ArrayType": ArrayType,
    "AuthConfig": AuthConfig,
    "AuthDetails": AuthDetails,
    "AvroFormatAttribute": AvroFormatAttribute,
    "BaseType": BaseType,
    "BiccReadAttributes": BiccReadAttributes,
    "BipCallAttribute": BipCallAttribute,
    "BipReadAttributes": BipReadAttributes,
    "BipReportParameterValue": BipReportParameterValue,
    "CancelRestCallConfig": CancelRestCallConfig,
    "ChangeCompartmentDetails": ChangeCompartmentDetails,
    "ChangeDisApplicationCompartmentDetails": ChangeDisApplicationCompartmentDetails,
    "ChildReference": ChildReference,
    "ChildReferenceDetail": ChildReferenceDetail,
    "CompositeFieldMap": CompositeFieldMap,
    "CompositeType": CompositeType,
    "Compression": Compression,
    "ConditionalCompositeFieldMap": ConditionalCompositeFieldMap,
    "ConditionalInputLink": ConditionalInputLink,
    "ConditionalOutputPort": ConditionalOutputPort,
    "ConfigDefinition": ConfigDefinition,
    "ConfigParameterDefinition": ConfigParameterDefinition,
    "ConfigParameterValue": ConfigParameterValue,
    "ConfigProvider": ConfigProvider,
    "ConfigValues": ConfigValues,
    "ConfigurationDetails": ConfigurationDetails,
    "ConfiguredType": ConfiguredType,
    "Connection": Connection,
    "ConnectionDetails": ConnectionDetails,
    "ConnectionFromAdwc": ConnectionFromAdwc,
    "ConnectionFromAdwcDetails": ConnectionFromAdwcDetails,
    "ConnectionFromAmazonS3": ConnectionFromAmazonS3,
    "ConnectionFromAmazonS3Details": ConnectionFromAmazonS3Details,
    "ConnectionFromAtp": ConnectionFromAtp,
    "ConnectionFromAtpDetails": ConnectionFromAtpDetails,
    "ConnectionFromBICC": ConnectionFromBICC,
    "ConnectionFromBICCDetails": ConnectionFromBICCDetails,
    "ConnectionFromBIP": ConnectionFromBIP,
    "ConnectionFromBipDetails": ConnectionFromBipDetails,
    "ConnectionFromJdbc": ConnectionFromJdbc,
    "ConnectionFromJdbcDetails": ConnectionFromJdbcDetails,
    "ConnectionFromLakehouse": ConnectionFromLakehouse,
    "ConnectionFromLakehouseDetails": ConnectionFromLakehouseDetails,
    "ConnectionFromMySQL": ConnectionFromMySQL,
    "ConnectionFromMySQLDetails": ConnectionFromMySQLDetails,
    "ConnectionFromObjectStorage": ConnectionFromObjectStorage,
    "ConnectionFromObjectStorageDetails": ConnectionFromObjectStorageDetails,
    "ConnectionFromOracle": ConnectionFromOracle,
    "ConnectionFromOracleDetails": ConnectionFromOracleDetails,
    "ConnectionFromRestBasicAuth": ConnectionFromRestBasicAuth,
    "ConnectionFromRestBasicAuthDetails": ConnectionFromRestBasicAuthDetails,
    "ConnectionFromRestNoAuth": ConnectionFromRestNoAuth,
    "ConnectionFromRestNoAuthDetails": ConnectionFromRestNoAuthDetails,
    "ConnectionProperty": ConnectionProperty,
    "ConnectionSummary": ConnectionSummary,
    "ConnectionSummaryCollection": ConnectionSummaryCollection,
    "ConnectionSummaryFromAdwc": ConnectionSummaryFromAdwc,
    "ConnectionSummaryFromAmazonS3": ConnectionSummaryFromAmazonS3,
    "ConnectionSummaryFromAtp": ConnectionSummaryFromAtp,
    "ConnectionSummaryFromBICC": ConnectionSummaryFromBICC,
    "ConnectionSummaryFromBIP": ConnectionSummaryFromBIP,
    "ConnectionSummaryFromJdbc": ConnectionSummaryFromJdbc,
    "ConnectionSummaryFromLakehouse": ConnectionSummaryFromLakehouse,
    "ConnectionSummaryFromMySQL": ConnectionSummaryFromMySQL,
    "ConnectionSummaryFromObjectStorage": ConnectionSummaryFromObjectStorage,
    "ConnectionSummaryFromOracle": ConnectionSummaryFromOracle,
    "ConnectionSummaryFromRestBasicAuth": ConnectionSummaryFromRestBasicAuth,
    "ConnectionSummaryFromRestNoAuth": ConnectionSummaryFromRestNoAuth,
    "ConnectionValidation": ConnectionValidation,
    "ConnectionValidationSummary": ConnectionValidationSummary,
    "ConnectionValidationSummaryCollection": ConnectionValidationSummaryCollection,
    "ConnectorAttribute": ConnectorAttribute,
    "CountStatistic": CountStatistic,
    "CountStatisticSummary": CountStatisticSummary,
    "CreateApplicationDetails": CreateApplicationDetails,
    "CreateConfigProvider": CreateConfigProvider,
    "CreateConnectionDetails": CreateConnectionDetails,
    "CreateConnectionFromAdwc": CreateConnectionFromAdwc,
    "CreateConnectionFromAmazonS3": CreateConnectionFromAmazonS3,
    "CreateConnectionFromAtp": CreateConnectionFromAtp,
    "CreateConnectionFromBICC": CreateConnectionFromBICC,
    "CreateConnectionFromBIP": CreateConnectionFromBIP,
    "CreateConnectionFromJdbc": CreateConnectionFromJdbc,
    "CreateConnectionFromLakehouse": CreateConnectionFromLakehouse,
    "CreateConnectionFromMySQL": CreateConnectionFromMySQL,
    "CreateConnectionFromObjectStorage": CreateConnectionFromObjectStorage,
    "CreateConnectionFromOracle": CreateConnectionFromOracle,
    "CreateConnectionFromRestBasicAuth": CreateConnectionFromRestBasicAuth,
    "CreateConnectionFromRestNoAuth": CreateConnectionFromRestNoAuth,
    "CreateConnectionValidationDetails": CreateConnectionValidationDetails,
    "CreateDataAssetDetails": CreateDataAssetDetails,
    "CreateDataAssetFromAdwc": CreateDataAssetFromAdwc,
    "CreateDataAssetFromAmazonS3": CreateDataAssetFromAmazonS3,
    "CreateDataAssetFromAtp": CreateDataAssetFromAtp,
    "CreateDataAssetFromFusionApp": CreateDataAssetFromFusionApp,
    "CreateDataAssetFromJdbc": CreateDataAssetFromJdbc,
    "CreateDataAssetFromLakehouse": CreateDataAssetFromLakehouse,
    "CreateDataAssetFromMySQL": CreateDataAssetFromMySQL,
    "CreateDataAssetFromObjectStorage": CreateDataAssetFromObjectStorage,
    "CreateDataAssetFromOracle": CreateDataAssetFromOracle,
    "CreateDataAssetFromRest": CreateDataAssetFromRest,
    "CreateDataFlowDetails": CreateDataFlowDetails,
    "CreateDataFlowValidationDetails": CreateDataFlowValidationDetails,
    "CreateDisApplicationDetails": CreateDisApplicationDetails,
    "CreateEntityShapeDetails": CreateEntityShapeDetails,
    "CreateEntityShapeFromFile": CreateEntityShapeFromFile,
    "CreateEntityShapeFromSQL": CreateEntityShapeFromSQL,
    "CreateExternalPublicationDetails": CreateExternalPublicationDetails,
    "CreateExternalPublicationValidationDetails": CreateExternalPublicationValidationDetails,
    "CreateFolderDetails": CreateFolderDetails,
    "CreateFunctionLibraryDetails": CreateFunctionLibraryDetails,
    "CreatePatchDetails": CreatePatchDetails,
    "CreatePipelineDetails": CreatePipelineDetails,
    "CreatePipelineValidationDetails": CreatePipelineValidationDetails,
    "CreateProjectDetails": CreateProjectDetails,
    "CreateScheduleDetails": CreateScheduleDetails,
    "CreateSourceApplicationInfo": CreateSourceApplicationInfo,
    "CreateTaskDetails": CreateTaskDetails,
    "CreateTaskFromDataLoaderTask": CreateTaskFromDataLoaderTask,
    "CreateTaskFromIntegrationTask": CreateTaskFromIntegrationTask,
    "CreateTaskFromOCIDataflowTask": CreateTaskFromOCIDataflowTask,
    "CreateTaskFromPipelineTask": CreateTaskFromPipelineTask,
    "CreateTaskFromRestTask": CreateTaskFromRestTask,
    "CreateTaskFromSQLTask": CreateTaskFromSQLTask,
    "CreateTaskRunDetails": CreateTaskRunDetails,
    "CreateTaskScheduleDetails": CreateTaskScheduleDetails,
    "CreateTaskValidationDetails": CreateTaskValidationDetails,
    "CreateTaskValidationFromDataLoaderTask": CreateTaskValidationFromDataLoaderTask,
    "CreateTaskValidationFromIntegrationTask": CreateTaskValidationFromIntegrationTask,
    "CreateTaskValidationFromPipelineTask": CreateTaskValidationFromPipelineTask,
    "CreateUserDefinedFunctionDetails": CreateUserDefinedFunctionDetails,
    "CreateUserDefinedFunctionValidationDetails": CreateUserDefinedFunctionValidationDetails,
    "CreateWorkspaceDetails": CreateWorkspaceDetails,
    "CsvFormatAttribute": CsvFormatAttribute,
    "CustomFrequencyDetails": CustomFrequencyDetails,
    "DailyFrequencyDetails": DailyFrequencyDetails,
    "DataAsset": DataAsset,
    "DataAssetFromAdwcDetails": DataAssetFromAdwcDetails,
    "DataAssetFromAmazonS3": DataAssetFromAmazonS3,
    "DataAssetFromAtpDetails": DataAssetFromAtpDetails,
    "DataAssetFromFusionApp": DataAssetFromFusionApp,
    "DataAssetFromJdbc": DataAssetFromJdbc,
    "DataAssetFromLakehouseDetails": DataAssetFromLakehouseDetails,
    "DataAssetFromMySQL": DataAssetFromMySQL,
    "DataAssetFromObjectStorageDetails": DataAssetFromObjectStorageDetails,
    "DataAssetFromOracleDetails": DataAssetFromOracleDetails,
    "DataAssetFromRestDetails": DataAssetFromRestDetails,
    "DataAssetSummary": DataAssetSummary,
    "DataAssetSummaryCollection": DataAssetSummaryCollection,
    "DataAssetSummaryFromAdwc": DataAssetSummaryFromAdwc,
    "DataAssetSummaryFromAmazonS3": DataAssetSummaryFromAmazonS3,
    "DataAssetSummaryFromAtp": DataAssetSummaryFromAtp,
    "DataAssetSummaryFromFusionApp": DataAssetSummaryFromFusionApp,
    "DataAssetSummaryFromJdbc": DataAssetSummaryFromJdbc,
    "DataAssetSummaryFromLakehouse": DataAssetSummaryFromLakehouse,
    "DataAssetSummaryFromMySQL": DataAssetSummaryFromMySQL,
    "DataAssetSummaryFromObjectStorage": DataAssetSummaryFromObjectStorage,
    "DataAssetSummaryFromOracle": DataAssetSummaryFromOracle,
    "DataAssetSummaryFromRest": DataAssetSummaryFromRest,
    "DataEntity": DataEntity,
    "DataEntityDetails": DataEntityDetails,
    "DataEntityFromDataStore": DataEntityFromDataStore,
    "DataEntityFromDataStoreEntityDetails": DataEntityFromDataStoreEntityDetails,
    "DataEntityFromFile": DataEntityFromFile,
    "DataEntityFromFileEntityDetails": DataEntityFromFileEntityDetails,
    "DataEntityFromSql": DataEntityFromSql,
    "DataEntityFromSqlEntityDetails": DataEntityFromSqlEntityDetails,
    "DataEntityFromTable": DataEntityFromTable,
    "DataEntityFromTableEntityDetails": DataEntityFromTableEntityDetails,
    "DataEntityFromView": DataEntityFromView,
    "DataEntityFromViewEntityDetails": DataEntityFromViewEntityDetails,
    "DataEntitySummary": DataEntitySummary,
    "DataEntitySummaryCollection": DataEntitySummaryCollection,
    "DataEntitySummaryFromDataStore": DataEntitySummaryFromDataStore,
    "DataEntitySummaryFromFile": DataEntitySummaryFromFile,
    "DataEntitySummaryFromSql": DataEntitySummaryFromSql,
    "DataEntitySummaryFromTable": DataEntitySummaryFromTable,
    "DataEntitySummaryFromView": DataEntitySummaryFromView,
    "DataFlow": DataFlow,
    "DataFlowDetails": DataFlowDetails,
    "DataFlowSummary": DataFlowSummary,
    "DataFlowSummaryCollection": DataFlowSummaryCollection,
    "DataFlowValidation": DataFlowValidation,
    "DataFlowValidationSummary": DataFlowValidationSummary,
    "DataFlowValidationSummaryCollection": DataFlowValidationSummaryCollection,
    "DataFormat": DataFormat,
    "DataType": DataType,
    "DataflowApplication": DataflowApplication,
    "DecisionOperator": DecisionOperator,
    "DecisionOutputPort": DecisionOutputPort,
    "DependentObject": DependentObject,
    "DependentObjectSummary": DependentObjectSummary,
    "DependentObjectSummaryCollection": DependentObjectSummaryCollection,
    "DerivedEntity": DerivedEntity,
    "DerivedField": DerivedField,
    "DerivedType": DerivedType,
    "DirectFieldMap": DirectFieldMap,
    "DirectNamedFieldMap": DirectNamedFieldMap,
    "DisApplication": DisApplication,
    "DisApplicationSummary": DisApplicationSummary,
    "DisApplicationSummaryCollection": DisApplicationSummaryCollection,
    "Distinct": Distinct,
    "DynamicInputField": DynamicInputField,
    "DynamicProxyField": DynamicProxyField,
    "DynamicType": DynamicType,
    "DynamicTypeHandler": DynamicTypeHandler,
    "EndOperator": EndOperator,
    "EnrichedEntity": EnrichedEntity,
    "EntityShape": EntityShape,
    "EntityShapeFromFile": EntityShapeFromFile,
    "EntityShapeFromSQL": EntityShapeFromSQL,
    "ErrorDetails": ErrorDetails,
    "ExecuteRestCallConfig": ExecuteRestCallConfig,
    "Expression": Expression,
    "ExpressionOperator": ExpressionOperator,
    "ExternalPublication": ExternalPublication,
    "ExternalPublicationSummary": ExternalPublicationSummary,
    "ExternalPublicationSummaryCollection": ExternalPublicationSummaryCollection,
    "ExternalPublicationValidation": ExternalPublicationValidation,
    "ExternalPublicationValidationSummary": ExternalPublicationValidationSummary,
    "ExternalPublicationValidationSummaryCollection": ExternalPublicationValidationSummaryCollection,
    "ExternalStorage": ExternalStorage,
    "FieldMap": FieldMap,
    "FieldMapWrapper": FieldMapWrapper,
    "Filter": Filter,
    "FilterPush": FilterPush,
    "Flatten": Flatten,
    "FlattenDetails": FlattenDetails,
    "FlattenProjectionPreferences": FlattenProjectionPreferences,
    "FlattenTypeHandler": FlattenTypeHandler,
    "FlowNode": FlowNode,
    "FlowPort": FlowPort,
    "FlowPortLink": FlowPortLink,
    "Folder": Folder,
    "FolderDetails": FolderDetails,
    "FolderSummary": FolderSummary,
    "FolderSummaryCollection": FolderSummaryCollection,
    "ForeignKey": ForeignKey,
    "Function": Function,
    "FunctionConfigurationDefinition": FunctionConfigurationDefinition,
    "FunctionLibrary": FunctionLibrary,
    "FunctionLibraryDetails": FunctionLibraryDetails,
    "FunctionLibrarySummary": FunctionLibrarySummary,
    "FunctionLibrarySummaryCollection": FunctionLibrarySummaryCollection,
    "FunctionSignature": FunctionSignature,
    "GenericRestApiAttributes": GenericRestApiAttributes,
    "GenericRestCallAttribute": GenericRestCallAttribute,
    "GroupedNamePatternRule": GroupedNamePatternRule,
    "HourlyFrequencyDetails": HourlyFrequencyDetails,
    "InputField": InputField,
    "InputLink": InputLink,
    "InputPort": InputPort,
    "InputProxyField": InputProxyField,
    "Intersect": Intersect,
    "JavaType": JavaType,
    "Join": Join,
    "Joiner": Joiner,
    "JsonFormatAttribute": JsonFormatAttribute,
    "JsonText": JsonText,
    "Key": Key,
    "KeyAttribute": KeyAttribute,
    "KeyRange": KeyRange,
    "KeyRangePartitionConfig": KeyRangePartitionConfig,
    "LastRunDetails": LastRunDetails,
    "Lookup": Lookup,
    "MacroField": MacroField,
    "MacroPivotField": MacroPivotField,
    "MapType": MapType,
    "MaterializedCompositeType": MaterializedCompositeType,
    "MaterializedDynamicField": MaterializedDynamicField,
    "MergeOperator": MergeOperator,
    "Message": Message,
    "Minus": Minus,
    "MonthlyFrequencyDetails": MonthlyFrequencyDetails,
    "MonthlyRuleFrequencyDetails": MonthlyRuleFrequencyDetails,
    "NameListRule": NameListRule,
    "NamePatternRule": NamePatternRule,
    "NamedEntityMap": NamedEntityMap,
    "NativeShapeField": NativeShapeField,
    "ObjectMetadata": ObjectMetadata,
    "ObjectStorageWriteAttribute": ObjectStorageWriteAttribute,
    "ObjectStorageWriteAttributes": ObjectStorageWriteAttributes,
    "OciFunction": OciFunction,
    "OciVaultSecretConfig": OciVaultSecretConfig,
    "Operation": Operation,
    "OperationFromApi": OperationFromApi,
    "OperationFromProcedure": OperationFromProcedure,
    "Operator": Operator,
    "OracleAdwcWriteAttribute": OracleAdwcWriteAttribute,
    "OracleAdwcWriteAttributes": OracleAdwcWriteAttributes,
    "OracleAtpWriteAttribute": OracleAtpWriteAttribute,
    "OracleAtpWriteAttributes": OracleAtpWriteAttributes,
    "OracleReadAttribute": OracleReadAttribute,
    "OracleReadAttributes": OracleReadAttributes,
    "OracleWriteAttribute": OracleWriteAttribute,
    "OracleWriteAttributes": OracleWriteAttributes,
    "OutputField": OutputField,
    "OutputLink": OutputLink,
    "OutputPort": OutputPort,
    "Parameter": Parameter,
    "ParameterValue": ParameterValue,
    "ParentReference": ParentReference,
    "ParquetFormatAttribute": ParquetFormatAttribute,
    "PartitionConfig": PartitionConfig,
    "Patch": Patch,
    "PatchChangeSummary": PatchChangeSummary,
    "PatchChangeSummaryCollection": PatchChangeSummaryCollection,
    "PatchObjectMetadata": PatchObjectMetadata,
    "PatchSummary": PatchSummary,
    "PatchSummaryCollection": PatchSummaryCollection,
    "Pipeline": Pipeline,
    "PipelineSummary": PipelineSummary,
    "PipelineSummaryCollection": PipelineSummaryCollection,
    "PipelineValidation": PipelineValidation,
    "PipelineValidationSummary": PipelineValidationSummary,
    "PipelineValidationSummaryCollection": PipelineValidationSummaryCollection,
    "Pivot": Pivot,
    "PivotField": PivotField,
    "PivotKeys": PivotKeys,
    "PollRestCallConfig": PollRestCallConfig,
    "PrimaryKey": PrimaryKey,
    "Project": Project,
    "ProjectDetails": ProjectDetails,
    "ProjectSummary": ProjectSummary,
    "ProjectSummaryCollection": ProjectSummaryCollection,
    "Projection": Projection,
    "ProjectionRule": ProjectionRule,
    "ProxyField": ProxyField,
    "PublishedObject": PublishedObject,
    "PublishedObjectFromDataLoaderTask": PublishedObjectFromDataLoaderTask,
    "PublishedObjectFromIntegrationTask": PublishedObjectFromIntegrationTask,
    "PublishedObjectFromPipelineTask": PublishedObjectFromPipelineTask,
    "PublishedObjectFromPipelineTaskSummary": PublishedObjectFromPipelineTaskSummary,
    "PublishedObjectSummary": PublishedObjectSummary,
    "PublishedObjectSummaryCollection": PublishedObjectSummaryCollection,
    "PublishedObjectSummaryFromDataLoaderTask": PublishedObjectSummaryFromDataLoaderTask,
    "PublishedObjectSummaryFromIntegrationTask": PublishedObjectSummaryFromIntegrationTask,
    "PushDownOperation": PushDownOperation,
    "Query": Query,
    "ReadOperationConfig": ReadOperationConfig,
    "Reference": Reference,
    "ReferenceSummary": ReferenceSummary,
    "ReferenceSummaryCollection": ReferenceSummaryCollection,
    "ReferenceUsedBy": ReferenceUsedBy,
    "ReferencedDataObject": ReferencedDataObject,
    "ReferencedDataObjectFromAPI": ReferencedDataObjectFromAPI,
    "ReferencedDataObjectFromProcedure": ReferencedDataObjectFromProcedure,
    "RegistryMetadata": RegistryMetadata,
    "RenameRule": RenameRule,
    "ResourceConfiguration": ResourceConfiguration,
    "ResourcePrincipalAuthConfig": ResourcePrincipalAuthConfig,
    "RestCallConfig": RestCallConfig,
    "RootObject": RootObject,
    "RuleBasedEntityMap": RuleBasedEntityMap,
    "RuleBasedFieldMap": RuleBasedFieldMap,
    "RuleTypeConfig": RuleTypeConfig,
    "RuntimeOperator": RuntimeOperator,
    "RuntimeOperatorSummary": RuntimeOperatorSummary,
    "RuntimeOperatorSummaryCollection": RuntimeOperatorSummaryCollection,
    "RuntimePipeline": RuntimePipeline,
    "RuntimePipelineSummary": RuntimePipelineSummary,
    "RuntimePipelineSummaryCollection": RuntimePipelineSummaryCollection,
    "Schedule": Schedule,
    "ScheduleSummary": ScheduleSummary,
    "ScheduleSummaryCollection": ScheduleSummaryCollection,
    "Schema": Schema,
    "SchemaDriftConfig": SchemaDriftConfig,
    "SchemaSummary": SchemaSummary,
    "SchemaSummaryCollection": SchemaSummaryCollection,
    "ScopeReference": ScopeReference,
    "Script": Script,
    "SecretConfig": SecretConfig,
    "Select": Select,
    "SensitiveAttribute": SensitiveAttribute,
    "Shape": Shape,
    "ShapeField": ShapeField,
    "Sort": Sort,
    "SortClause": SortClause,
    "SortKey": SortKey,
    "SortKeyRule": SortKeyRule,
    "SortOper": SortOper,
    "Source": Source,
    "SourceApplicationInfo": SourceApplicationInfo,
    "Split": Split,
    "StartOperator": StartOperator,
    "StructuredType": StructuredType,
    "Target": Target,
    "Task": Task,
    "TaskFromDataLoaderTaskDetails": TaskFromDataLoaderTaskDetails,
    "TaskFromIntegrationTaskDetails": TaskFromIntegrationTaskDetails,
    "TaskFromOCIDataflowTaskDetails": TaskFromOCIDataflowTaskDetails,
    "TaskFromPipelineTaskDetails": TaskFromPipelineTaskDetails,
    "TaskFromRestTaskDetails": TaskFromRestTaskDetails,
    "TaskFromSQLTaskDetails": TaskFromSQLTaskDetails,
    "TaskOperator": TaskOperator,
    "TaskRun": TaskRun,
    "TaskRunDetails": TaskRunDetails,
    "TaskRunLineageDetails": TaskRunLineageDetails,
    "TaskRunLineageSummary": TaskRunLineageSummary,
    "TaskRunLineageSummaryCollection": TaskRunLineageSummaryCollection,
    "TaskRunLogSummary": TaskRunLogSummary,
    "TaskRunSummary": TaskRunSummary,
    "TaskRunSummaryCollection": TaskRunSummaryCollection,
    "TaskSchedule": TaskSchedule,
    "TaskScheduleSummary": TaskScheduleSummary,
    "TaskScheduleSummaryCollection": TaskScheduleSummaryCollection,
    "TaskSummary": TaskSummary,
    "TaskSummaryCollection": TaskSummaryCollection,
    "TaskSummaryFromDataLoaderTask": TaskSummaryFromDataLoaderTask,
    "TaskSummaryFromIntegrationTask": TaskSummaryFromIntegrationTask,
    "TaskSummaryFromOCIDataflowTask": TaskSummaryFromOCIDataflowTask,
    "TaskSummaryFromPipelineTask": TaskSummaryFromPipelineTask,
    "TaskSummaryFromRestTask": TaskSummaryFromRestTask,
    "TaskSummaryFromSQLTask": TaskSummaryFromSQLTask,
    "TaskValidation": TaskValidation,
    "TaskValidationSummary": TaskValidationSummary,
    "TaskValidationSummaryCollection": TaskValidationSummaryCollection,
    "TemplateSummary": TemplateSummary,
    "TemplateSummaryCollection": TemplateSummaryCollection,
    "Time": Time,
    "TypeLibrary": TypeLibrary,
    "TypeListRule": TypeListRule,
    "TypeSystem": TypeSystem,
    "TypedExpression": TypedExpression,
    "TypedNamePatternRule": TypedNamePatternRule,
    "TypedObject": TypedObject,
    "TypedObjectWrapper": TypedObjectWrapper,
    "UIProperties": UIProperties,
    "Union": Union,
    "UniqueDataKey": UniqueDataKey,
    "UniqueKey": UniqueKey,
    "UpdateApplicationDetails": UpdateApplicationDetails,
    "UpdateConnectionDetails": UpdateConnectionDetails,
    "UpdateConnectionFromAdwc": UpdateConnectionFromAdwc,
    "UpdateConnectionFromAmazonS3": UpdateConnectionFromAmazonS3,
    "UpdateConnectionFromAtp": UpdateConnectionFromAtp,
    "UpdateConnectionFromBICC": UpdateConnectionFromBICC,
    "UpdateConnectionFromBIP": UpdateConnectionFromBIP,
    "UpdateConnectionFromJdbc": UpdateConnectionFromJdbc,
    "UpdateConnectionFromLakehouse": UpdateConnectionFromLakehouse,
    "UpdateConnectionFromMySQL": UpdateConnectionFromMySQL,
    "UpdateConnectionFromObjectStorage": UpdateConnectionFromObjectStorage,
    "UpdateConnectionFromOracle": UpdateConnectionFromOracle,
    "UpdateConnectionFromRestBasicAuth": UpdateConnectionFromRestBasicAuth,
    "UpdateConnectionFromRestNoAuth": UpdateConnectionFromRestNoAuth,
    "UpdateDataAssetDetails": UpdateDataAssetDetails,
    "UpdateDataAssetFromAdwc": UpdateDataAssetFromAdwc,
    "UpdateDataAssetFromAmazonS3": UpdateDataAssetFromAmazonS3,
    "UpdateDataAssetFromAtp": UpdateDataAssetFromAtp,
    "UpdateDataAssetFromFusionApp": UpdateDataAssetFromFusionApp,
    "UpdateDataAssetFromJdbc": UpdateDataAssetFromJdbc,
    "UpdateDataAssetFromLakehouse": UpdateDataAssetFromLakehouse,
    "UpdateDataAssetFromMySQL": UpdateDataAssetFromMySQL,
    "UpdateDataAssetFromObjectStorage": UpdateDataAssetFromObjectStorage,
    "UpdateDataAssetFromOracle": UpdateDataAssetFromOracle,
    "UpdateDataAssetFromRest": UpdateDataAssetFromRest,
    "UpdateDataFlowDetails": UpdateDataFlowDetails,
    "UpdateDisApplicationDetails": UpdateDisApplicationDetails,
    "UpdateExternalPublicationDetails": UpdateExternalPublicationDetails,
    "UpdateFolderDetails": UpdateFolderDetails,
    "UpdateFunctionLibraryDetails": UpdateFunctionLibraryDetails,
    "UpdatePipelineDetails": UpdatePipelineDetails,
    "UpdateProjectDetails": UpdateProjectDetails,
    "UpdateReferenceDetails": UpdateReferenceDetails,
    "UpdateScheduleDetails": UpdateScheduleDetails,
    "UpdateTaskDetails": UpdateTaskDetails,
    "UpdateTaskFromDataLoaderTask": UpdateTaskFromDataLoaderTask,
    "UpdateTaskFromIntegrationTask": UpdateTaskFromIntegrationTask,
    "UpdateTaskFromOCIDataflowTask": UpdateTaskFromOCIDataflowTask,
    "UpdateTaskFromPipelineTask": UpdateTaskFromPipelineTask,
    "UpdateTaskFromRestTask": UpdateTaskFromRestTask,
    "UpdateTaskFromSQLTask": UpdateTaskFromSQLTask,
    "UpdateTaskRunDetails": UpdateTaskRunDetails,
    "UpdateTaskScheduleDetails": UpdateTaskScheduleDetails,
    "UpdateUserDefinedFunctionDetails": UpdateUserDefinedFunctionDetails,
    "UpdateWorkspaceDetails": UpdateWorkspaceDetails,
    "UserDefinedFunction": UserDefinedFunction,
    "UserDefinedFunctionDetails": UserDefinedFunctionDetails,
    "UserDefinedFunctionSummary": UserDefinedFunctionSummary,
    "UserDefinedFunctionSummaryCollection": UserDefinedFunctionSummaryCollection,
    "UserDefinedFunctionValidation": UserDefinedFunctionValidation,
    "UserDefinedFunctionValidationSummary": UserDefinedFunctionValidationSummary,
    "UserDefinedFunctionValidationSummaryCollection": UserDefinedFunctionValidationSummaryCollection,
    "ValidationMessage": ValidationMessage,
    "Variable": Variable,
    "WeeklyFrequencyDetails": WeeklyFrequencyDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "Workspace": Workspace,
    "WorkspaceSummary": WorkspaceSummary,
    "WriteOperationConfig": WriteOperationConfig
}
