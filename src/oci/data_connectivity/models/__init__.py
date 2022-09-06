# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .abstract_call_attribute import AbstractCallAttribute
from .abstract_data_operation_config import AbstractDataOperationConfig
from .abstract_format_attribute import AbstractFormatAttribute
from .abstract_operation_attributes import AbstractOperationAttributes
from .abstract_read_attribute import AbstractReadAttribute
from .abstract_write_attribute import AbstractWriteAttribute
from .aggregator_summary import AggregatorSummary
from .attach_data_asset_info import AttachDataAssetInfo
from .attribute import Attribute
from .attribute_profile_result import AttributeProfileResult
from .avro_format_attribute import AvroFormatAttribute
from .base_type import BaseType
from .bicc_read_attributes import BiccReadAttributes
from .bip_call_attribute import BipCallAttribute
from .call_operation_config import CallOperationConfig
from .change_endpoint_compartment_details import ChangeEndpointCompartmentDetails
from .change_registry_compartment_details import ChangeRegistryCompartmentDetails
from .column import Column
from .composite_type import CompositeType
from .compression import Compression
from .config_definition import ConfigDefinition
from .config_details import ConfigDetails
from .config_parameter_definition import ConfigParameterDefinition
from .config_parameter_value import ConfigParameterValue
from .config_values import ConfigValues
from .configured_type import ConfiguredType
from .connection import Connection
from .connection_property import ConnectionProperty
from .connection_summary import ConnectionSummary
from .connection_summary_collection import ConnectionSummaryCollection
from .connection_validation import ConnectionValidation
from .connection_validation_summary import ConnectionValidationSummary
from .connectivity_usage import ConnectivityUsage
from .connectivity_usage_details import ConnectivityUsageDetails
from .connectivity_validation import ConnectivityValidation
from .connector_attribute import ConnectorAttribute
from .create_attach_data_asset_details import CreateAttachDataAssetDetails
from .create_connection_details import CreateConnectionDetails
from .create_connection_validation_details import CreateConnectionValidationDetails
from .create_connectivity_validation_details import CreateConnectivityValidationDetails
from .create_data_asset_details import CreateDataAssetDetails
from .create_data_preview_details import CreateDataPreviewDetails
from .create_data_profile_details import CreateDataProfileDetails
from .create_de_reference_artifact_details import CreateDeReferenceArtifactDetails
from .create_detach_data_asset_details import CreateDetachDataAssetDetails
from .create_dp_endpoint_details import CreateDpEndpointDetails
from .create_dp_endpoint_from_private import CreateDpEndpointFromPrivate
from .create_dp_endpoint_from_public import CreateDpEndpointFromPublic
from .create_endpoint_details import CreateEndpointDetails
from .create_entity_shape_details import CreateEntityShapeDetails
from .create_entity_shape_from_data_store import CreateEntityShapeFromDataStore
from .create_entity_shape_from_file import CreateEntityShapeFromFile
from .create_entity_shape_from_message import CreateEntityShapeFromMessage
from .create_entity_shape_from_sql import CreateEntityShapeFromSQL
from .create_entity_shape_from_table import CreateEntityShapeFromTable
from .create_entity_shape_from_view import CreateEntityShapeFromView
from .create_execute_operation_job_details import CreateExecuteOperationJobDetails
from .create_folder_details import CreateFolderDetails
from .create_full_push_down_task_details import CreateFullPushDownTaskDetails
from .create_reference_artifact_details import CreateReferenceArtifactDetails
from .create_registry_details import CreateRegistryDetails
from .create_test_network_connectivity_details import CreateTestNetworkConnectivityDetails
from .csv_format_attribute import CsvFormatAttribute
from .data_asset import DataAsset
from .data_asset_summary import DataAssetSummary
from .data_asset_summary_collection import DataAssetSummaryCollection
from .data_entity import DataEntity
from .data_entity_details import DataEntityDetails
from .data_entity_from_data_store import DataEntityFromDataStore
from .data_entity_from_data_store_entity_details import DataEntityFromDataStoreEntityDetails
from .data_entity_from_file import DataEntityFromFile
from .data_entity_from_file_entity_details import DataEntityFromFileEntityDetails
from .data_entity_from_message_entity_details import DataEntityFromMessageEntityDetails
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
from .data_format import DataFormat
from .data_preview import DataPreview
from .data_profile import DataProfile
from .data_type import DataType
from .data_type_stat import DataTypeStat
from .date_attribute import DateAttribute
from .de_reference_info import DeReferenceInfo
from .derive_entities import DeriveEntities
from .derive_entities_details import DeriveEntitiesDetails
from .derive_entities_item import DeriveEntitiesItem
from .derived_entity import DerivedEntity
from .derived_type import DerivedType
from .detach_data_asset_info import DetachDataAssetInfo
from .dp_endpoint import DpEndpoint
from .dp_endpoint_details import DpEndpointDetails
from .dp_endpoint_from_private import DpEndpointFromPrivate
from .dp_endpoint_from_private_details import DpEndpointFromPrivateDetails
from .dp_endpoint_from_public import DpEndpointFromPublic
from .dp_endpoint_from_public_details import DpEndpointFromPublicDetails
from .dp_endpoint_summary import DpEndpointSummary
from .dp_endpoint_summary_from_private import DpEndpointSummaryFromPrivate
from .dp_endpoint_summary_from_public import DpEndpointSummaryFromPublic
from .endpoint import Endpoint
from .endpoint_summary import EndpointSummary
from .endpoint_summary_collection import EndpointSummaryCollection
from .entity_profile_result import EntityProfileResult
from .entity_shape import EntityShape
from .entity_shape_from_data_store import EntityShapeFromDataStore
from .entity_shape_from_file import EntityShapeFromFile
from .entity_shape_from_message import EntityShapeFromMessage
from .entity_shape_from_sql import EntityShapeFromSQL
from .entity_shape_from_table import EntityShapeFromTable
from .entity_shape_from_view import EntityShapeFromView
from .error_details import ErrorDetails
from .excel_format_attribute import ExcelFormatAttribute
from .execute_operation_job import ExecuteOperationJob
from .execute_operation_job_details import ExecuteOperationJobDetails
from .external_storage import ExternalStorage
from .filter_push import FilterPush
from .folder import Folder
from .folder_summary import FolderSummary
from .folder_summary_collection import FolderSummaryCollection
from .foreign_key import ForeignKey
from .full_push_down_task_response import FullPushDownTaskResponse
from .generic_rest_api_attributes import GenericRestApiAttributes
from .generic_rest_call_attribute import GenericRestCallAttribute
from .hdfs_write_attributes import HdfsWriteAttributes
from .histogram import Histogram
from .input_port import InputPort
from .join import Join
from .json_format_attribute import JsonFormatAttribute
from .key import Key
from .key_attribute import KeyAttribute
from .key_range import KeyRange
from .key_range_partition_config import KeyRangePartitionConfig
from .message import Message
from .native_shape_field import NativeShapeField
from .network_connectivity_status import NetworkConnectivityStatus
from .network_connectivity_status_collection import NetworkConnectivityStatusCollection
from .numeric_attribute import NumericAttribute
from .object_freq_stat import ObjectFreqStat
from .object_metadata import ObjectMetadata
from .object_storage_write_attributes import ObjectStorageWriteAttributes
from .operation import Operation
from .operation_exec_result import OperationExecResult
from .operation_from_api import OperationFromApi
from .operation_from_procedure import OperationFromProcedure
from .operation_input_record import OperationInputRecord
from .operation_summary import OperationSummary
from .operation_summary_collection import OperationSummaryCollection
from .operation_summary_from_api import OperationSummaryFromApi
from .operation_summary_from_procedure import OperationSummaryFromProcedure
from .oracle_adwc_write_attributes import OracleAdwcWriteAttributes
from .oracle_atp_write_attributes import OracleAtpWriteAttributes
from .oracle_read_attribute import OracleReadAttribute
from .oracle_read_attributes import OracleReadAttributes
from .oracle_write_attributes import OracleWriteAttributes
from .outlier import Outlier
from .output_port import OutputPort
from .parameter import Parameter
from .parent_reference import ParentReference
from .parquet_format_attribute import ParquetFormatAttribute
from .partition_config import PartitionConfig
from .primary_key import PrimaryKey
from .profile_config import ProfileConfig
from .profile_stat import ProfileStat
from .push_down_operation import PushDownOperation
from .query import Query
from .read_operation_config import ReadOperationConfig
from .reference_artifact_summary import ReferenceArtifactSummary
from .reference_artifact_summary_collection import ReferenceArtifactSummaryCollection
from .reference_info import ReferenceInfo
from .referenced_data_object import ReferencedDataObject
from .referenced_data_object_from_api import ReferencedDataObjectFromAPI
from .referenced_data_object_from_procedure import ReferencedDataObjectFromProcedure
from .registry import Registry
from .registry_metadata import RegistryMetadata
from .registry_summary import RegistrySummary
from .registry_summary_collection import RegistrySummaryCollection
from .row import Row
from .schema import Schema
from .schema_drift_config import SchemaDriftConfig
from .schema_summary import SchemaSummary
from .schema_summary_collection import SchemaSummaryCollection
from .select import Select
from .shape import Shape
from .shape_field import ShapeField
from .sort import Sort
from .sort_clause import SortClause
from .source import Source
from .string_attribute import StringAttribute
from .structured_type import StructuredType
from .target import Target
from .test_network_connectivity import TestNetworkConnectivity
from .type import Type
from .type_library import TypeLibrary
from .type_summary import TypeSummary
from .type_system import TypeSystem
from .typed_object import TypedObject
from .types_summary_collection import TypesSummaryCollection
from .unique_key import UniqueKey
from .update_connection_details import UpdateConnectionDetails
from .update_data_asset_details import UpdateDataAssetDetails
from .update_dp_endpoint_details import UpdateDpEndpointDetails
from .update_dp_endpoint_from_private import UpdateDpEndpointFromPrivate
from .update_dp_endpoint_from_public import UpdateDpEndpointFromPublic
from .update_endpoint_details import UpdateEndpointDetails
from .update_folder_details import UpdateFolderDetails
from .update_registry_details import UpdateRegistryDetails
from .validation_message import ValidationMessage
from .validation_result import ValidationResult
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_error_summary import WorkRequestErrorSummary
from .work_request_log import WorkRequestLog
from .work_request_log_collection import WorkRequestLogCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection
from .write_operation_config import WriteOperationConfig

# Maps type names to classes for data_connectivity services.
data_connectivity_type_mapping = {
    "AbstractCallAttribute": AbstractCallAttribute,
    "AbstractDataOperationConfig": AbstractDataOperationConfig,
    "AbstractFormatAttribute": AbstractFormatAttribute,
    "AbstractOperationAttributes": AbstractOperationAttributes,
    "AbstractReadAttribute": AbstractReadAttribute,
    "AbstractWriteAttribute": AbstractWriteAttribute,
    "AggregatorSummary": AggregatorSummary,
    "AttachDataAssetInfo": AttachDataAssetInfo,
    "Attribute": Attribute,
    "AttributeProfileResult": AttributeProfileResult,
    "AvroFormatAttribute": AvroFormatAttribute,
    "BaseType": BaseType,
    "BiccReadAttributes": BiccReadAttributes,
    "BipCallAttribute": BipCallAttribute,
    "CallOperationConfig": CallOperationConfig,
    "ChangeEndpointCompartmentDetails": ChangeEndpointCompartmentDetails,
    "ChangeRegistryCompartmentDetails": ChangeRegistryCompartmentDetails,
    "Column": Column,
    "CompositeType": CompositeType,
    "Compression": Compression,
    "ConfigDefinition": ConfigDefinition,
    "ConfigDetails": ConfigDetails,
    "ConfigParameterDefinition": ConfigParameterDefinition,
    "ConfigParameterValue": ConfigParameterValue,
    "ConfigValues": ConfigValues,
    "ConfiguredType": ConfiguredType,
    "Connection": Connection,
    "ConnectionProperty": ConnectionProperty,
    "ConnectionSummary": ConnectionSummary,
    "ConnectionSummaryCollection": ConnectionSummaryCollection,
    "ConnectionValidation": ConnectionValidation,
    "ConnectionValidationSummary": ConnectionValidationSummary,
    "ConnectivityUsage": ConnectivityUsage,
    "ConnectivityUsageDetails": ConnectivityUsageDetails,
    "ConnectivityValidation": ConnectivityValidation,
    "ConnectorAttribute": ConnectorAttribute,
    "CreateAttachDataAssetDetails": CreateAttachDataAssetDetails,
    "CreateConnectionDetails": CreateConnectionDetails,
    "CreateConnectionValidationDetails": CreateConnectionValidationDetails,
    "CreateConnectivityValidationDetails": CreateConnectivityValidationDetails,
    "CreateDataAssetDetails": CreateDataAssetDetails,
    "CreateDataPreviewDetails": CreateDataPreviewDetails,
    "CreateDataProfileDetails": CreateDataProfileDetails,
    "CreateDeReferenceArtifactDetails": CreateDeReferenceArtifactDetails,
    "CreateDetachDataAssetDetails": CreateDetachDataAssetDetails,
    "CreateDpEndpointDetails": CreateDpEndpointDetails,
    "CreateDpEndpointFromPrivate": CreateDpEndpointFromPrivate,
    "CreateDpEndpointFromPublic": CreateDpEndpointFromPublic,
    "CreateEndpointDetails": CreateEndpointDetails,
    "CreateEntityShapeDetails": CreateEntityShapeDetails,
    "CreateEntityShapeFromDataStore": CreateEntityShapeFromDataStore,
    "CreateEntityShapeFromFile": CreateEntityShapeFromFile,
    "CreateEntityShapeFromMessage": CreateEntityShapeFromMessage,
    "CreateEntityShapeFromSQL": CreateEntityShapeFromSQL,
    "CreateEntityShapeFromTable": CreateEntityShapeFromTable,
    "CreateEntityShapeFromView": CreateEntityShapeFromView,
    "CreateExecuteOperationJobDetails": CreateExecuteOperationJobDetails,
    "CreateFolderDetails": CreateFolderDetails,
    "CreateFullPushDownTaskDetails": CreateFullPushDownTaskDetails,
    "CreateReferenceArtifactDetails": CreateReferenceArtifactDetails,
    "CreateRegistryDetails": CreateRegistryDetails,
    "CreateTestNetworkConnectivityDetails": CreateTestNetworkConnectivityDetails,
    "CsvFormatAttribute": CsvFormatAttribute,
    "DataAsset": DataAsset,
    "DataAssetSummary": DataAssetSummary,
    "DataAssetSummaryCollection": DataAssetSummaryCollection,
    "DataEntity": DataEntity,
    "DataEntityDetails": DataEntityDetails,
    "DataEntityFromDataStore": DataEntityFromDataStore,
    "DataEntityFromDataStoreEntityDetails": DataEntityFromDataStoreEntityDetails,
    "DataEntityFromFile": DataEntityFromFile,
    "DataEntityFromFileEntityDetails": DataEntityFromFileEntityDetails,
    "DataEntityFromMessageEntityDetails": DataEntityFromMessageEntityDetails,
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
    "DataFormat": DataFormat,
    "DataPreview": DataPreview,
    "DataProfile": DataProfile,
    "DataType": DataType,
    "DataTypeStat": DataTypeStat,
    "DateAttribute": DateAttribute,
    "DeReferenceInfo": DeReferenceInfo,
    "DeriveEntities": DeriveEntities,
    "DeriveEntitiesDetails": DeriveEntitiesDetails,
    "DeriveEntitiesItem": DeriveEntitiesItem,
    "DerivedEntity": DerivedEntity,
    "DerivedType": DerivedType,
    "DetachDataAssetInfo": DetachDataAssetInfo,
    "DpEndpoint": DpEndpoint,
    "DpEndpointDetails": DpEndpointDetails,
    "DpEndpointFromPrivate": DpEndpointFromPrivate,
    "DpEndpointFromPrivateDetails": DpEndpointFromPrivateDetails,
    "DpEndpointFromPublic": DpEndpointFromPublic,
    "DpEndpointFromPublicDetails": DpEndpointFromPublicDetails,
    "DpEndpointSummary": DpEndpointSummary,
    "DpEndpointSummaryFromPrivate": DpEndpointSummaryFromPrivate,
    "DpEndpointSummaryFromPublic": DpEndpointSummaryFromPublic,
    "Endpoint": Endpoint,
    "EndpointSummary": EndpointSummary,
    "EndpointSummaryCollection": EndpointSummaryCollection,
    "EntityProfileResult": EntityProfileResult,
    "EntityShape": EntityShape,
    "EntityShapeFromDataStore": EntityShapeFromDataStore,
    "EntityShapeFromFile": EntityShapeFromFile,
    "EntityShapeFromMessage": EntityShapeFromMessage,
    "EntityShapeFromSQL": EntityShapeFromSQL,
    "EntityShapeFromTable": EntityShapeFromTable,
    "EntityShapeFromView": EntityShapeFromView,
    "ErrorDetails": ErrorDetails,
    "ExcelFormatAttribute": ExcelFormatAttribute,
    "ExecuteOperationJob": ExecuteOperationJob,
    "ExecuteOperationJobDetails": ExecuteOperationJobDetails,
    "ExternalStorage": ExternalStorage,
    "FilterPush": FilterPush,
    "Folder": Folder,
    "FolderSummary": FolderSummary,
    "FolderSummaryCollection": FolderSummaryCollection,
    "ForeignKey": ForeignKey,
    "FullPushDownTaskResponse": FullPushDownTaskResponse,
    "GenericRestApiAttributes": GenericRestApiAttributes,
    "GenericRestCallAttribute": GenericRestCallAttribute,
    "HdfsWriteAttributes": HdfsWriteAttributes,
    "Histogram": Histogram,
    "InputPort": InputPort,
    "Join": Join,
    "JsonFormatAttribute": JsonFormatAttribute,
    "Key": Key,
    "KeyAttribute": KeyAttribute,
    "KeyRange": KeyRange,
    "KeyRangePartitionConfig": KeyRangePartitionConfig,
    "Message": Message,
    "NativeShapeField": NativeShapeField,
    "NetworkConnectivityStatus": NetworkConnectivityStatus,
    "NetworkConnectivityStatusCollection": NetworkConnectivityStatusCollection,
    "NumericAttribute": NumericAttribute,
    "ObjectFreqStat": ObjectFreqStat,
    "ObjectMetadata": ObjectMetadata,
    "ObjectStorageWriteAttributes": ObjectStorageWriteAttributes,
    "Operation": Operation,
    "OperationExecResult": OperationExecResult,
    "OperationFromApi": OperationFromApi,
    "OperationFromProcedure": OperationFromProcedure,
    "OperationInputRecord": OperationInputRecord,
    "OperationSummary": OperationSummary,
    "OperationSummaryCollection": OperationSummaryCollection,
    "OperationSummaryFromApi": OperationSummaryFromApi,
    "OperationSummaryFromProcedure": OperationSummaryFromProcedure,
    "OracleAdwcWriteAttributes": OracleAdwcWriteAttributes,
    "OracleAtpWriteAttributes": OracleAtpWriteAttributes,
    "OracleReadAttribute": OracleReadAttribute,
    "OracleReadAttributes": OracleReadAttributes,
    "OracleWriteAttributes": OracleWriteAttributes,
    "Outlier": Outlier,
    "OutputPort": OutputPort,
    "Parameter": Parameter,
    "ParentReference": ParentReference,
    "ParquetFormatAttribute": ParquetFormatAttribute,
    "PartitionConfig": PartitionConfig,
    "PrimaryKey": PrimaryKey,
    "ProfileConfig": ProfileConfig,
    "ProfileStat": ProfileStat,
    "PushDownOperation": PushDownOperation,
    "Query": Query,
    "ReadOperationConfig": ReadOperationConfig,
    "ReferenceArtifactSummary": ReferenceArtifactSummary,
    "ReferenceArtifactSummaryCollection": ReferenceArtifactSummaryCollection,
    "ReferenceInfo": ReferenceInfo,
    "ReferencedDataObject": ReferencedDataObject,
    "ReferencedDataObjectFromAPI": ReferencedDataObjectFromAPI,
    "ReferencedDataObjectFromProcedure": ReferencedDataObjectFromProcedure,
    "Registry": Registry,
    "RegistryMetadata": RegistryMetadata,
    "RegistrySummary": RegistrySummary,
    "RegistrySummaryCollection": RegistrySummaryCollection,
    "Row": Row,
    "Schema": Schema,
    "SchemaDriftConfig": SchemaDriftConfig,
    "SchemaSummary": SchemaSummary,
    "SchemaSummaryCollection": SchemaSummaryCollection,
    "Select": Select,
    "Shape": Shape,
    "ShapeField": ShapeField,
    "Sort": Sort,
    "SortClause": SortClause,
    "Source": Source,
    "StringAttribute": StringAttribute,
    "StructuredType": StructuredType,
    "Target": Target,
    "TestNetworkConnectivity": TestNetworkConnectivity,
    "Type": Type,
    "TypeLibrary": TypeLibrary,
    "TypeSummary": TypeSummary,
    "TypeSystem": TypeSystem,
    "TypedObject": TypedObject,
    "TypesSummaryCollection": TypesSummaryCollection,
    "UniqueKey": UniqueKey,
    "UpdateConnectionDetails": UpdateConnectionDetails,
    "UpdateDataAssetDetails": UpdateDataAssetDetails,
    "UpdateDpEndpointDetails": UpdateDpEndpointDetails,
    "UpdateDpEndpointFromPrivate": UpdateDpEndpointFromPrivate,
    "UpdateDpEndpointFromPublic": UpdateDpEndpointFromPublic,
    "UpdateEndpointDetails": UpdateEndpointDetails,
    "UpdateFolderDetails": UpdateFolderDetails,
    "UpdateRegistryDetails": UpdateRegistryDetails,
    "ValidationMessage": ValidationMessage,
    "ValidationResult": ValidationResult,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestErrorSummary": WorkRequestErrorSummary,
    "WorkRequestLog": WorkRequestLog,
    "WorkRequestLogCollection": WorkRequestLogCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection,
    "WriteOperationConfig": WriteOperationConfig
}
