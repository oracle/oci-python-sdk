# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .attach_catalog_private_endpoint_details import AttachCatalogPrivateEndpointDetails
from .attribute import Attribute
from .attribute_collection import AttributeCollection
from .attribute_summary import AttributeSummary
from .attribute_tag import AttributeTag
from .attribute_tag_collection import AttributeTagCollection
from .attribute_tag_summary import AttributeTagSummary
from .base_permissions_summary import BasePermissionsSummary
from .base_tag import BaseTag
from .base_tag_summary import BaseTagSummary
from .catalog import Catalog
from .catalog_permissions_summary import CatalogPermissionsSummary
from .catalog_private_endpoint import CatalogPrivateEndpoint
from .catalog_private_endpoint_summary import CatalogPrivateEndpointSummary
from .catalog_summary import CatalogSummary
from .change_catalog_compartment_details import ChangeCatalogCompartmentDetails
from .change_catalog_private_endpoint_compartment_details import ChangeCatalogPrivateEndpointCompartmentDetails
from .connection import Connection
from .connection_alias_summary import ConnectionAliasSummary
from .connection_collection import ConnectionCollection
from .connection_summary import ConnectionSummary
from .create_attribute_details import CreateAttributeDetails
from .create_catalog_details import CreateCatalogDetails
from .create_catalog_private_endpoint_details import CreateCatalogPrivateEndpointDetails
from .create_connection_details import CreateConnectionDetails
from .create_custom_property_details import CreateCustomPropertyDetails
from .create_data_asset_details import CreateDataAssetDetails
from .create_entity_details import CreateEntityDetails
from .create_folder_details import CreateFolderDetails
from .create_glossary_details import CreateGlossaryDetails
from .create_job_definition_details import CreateJobDefinitionDetails
from .create_job_details import CreateJobDetails
from .create_job_execution_details import CreateJobExecutionDetails
from .create_namespace_details import CreateNamespaceDetails
from .create_pattern_details import CreatePatternDetails
from .create_tag_details import CreateTagDetails
from .create_term_details import CreateTermDetails
from .create_term_relationship_details import CreateTermRelationshipDetails
from .custom_property import CustomProperty
from .custom_property_collection import CustomPropertyCollection
from .custom_property_get_usage import CustomPropertyGetUsage
from .custom_property_set_usage import CustomPropertySetUsage
from .custom_property_summary import CustomPropertySummary
from .custom_property_type_usage import CustomPropertyTypeUsage
from .data_asset import DataAsset
from .data_asset_collection import DataAssetCollection
from .data_asset_permissions_summary import DataAssetPermissionsSummary
from .data_asset_summary import DataAssetSummary
from .data_asset_tag import DataAssetTag
from .data_asset_tag_collection import DataAssetTagCollection
from .data_asset_tag_summary import DataAssetTagSummary
from .data_selector_pattern_details import DataSelectorPatternDetails
from .derived_logical_entities import DerivedLogicalEntities
from .detach_catalog_private_endpoint_details import DetachCatalogPrivateEndpointDetails
from .entity import Entity
from .entity_collection import EntityCollection
from .entity_summary import EntitySummary
from .entity_tag import EntityTag
from .entity_tag_collection import EntityTagCollection
from .entity_tag_summary import EntityTagSummary
from .faceted_search_aggregation import FacetedSearchAggregation
from .faceted_search_custom_property import FacetedSearchCustomProperty
from .faceted_search_date_filter_request import FacetedSearchDateFilterRequest
from .faceted_search_filter_request import FacetedSearchFilterRequest
from .faceted_search_sort_request import FacetedSearchSortRequest
from .faceted_search_string_filter_request import FacetedSearchStringFilterRequest
from .folder import Folder
from .folder_collection import FolderCollection
from .folder_summary import FolderSummary
from .folder_tag import FolderTag
from .folder_tag_collection import FolderTagCollection
from .folder_tag_summary import FolderTagSummary
from .glossary import Glossary
from .glossary_collection import GlossaryCollection
from .glossary_permissions_summary import GlossaryPermissionsSummary
from .glossary_summary import GlossarySummary
from .glossary_tree_element import GlossaryTreeElement
from .import_connection_details import ImportConnectionDetails
from .import_glossary_details import ImportGlossaryDetails
from .job import Job
from .job_collection import JobCollection
from .job_definition import JobDefinition
from .job_definition_collection import JobDefinitionCollection
from .job_definition_permissions_summary import JobDefinitionPermissionsSummary
from .job_definition_scope import JobDefinitionScope
from .job_definition_summary import JobDefinitionSummary
from .job_execution import JobExecution
from .job_execution_collection import JobExecutionCollection
from .job_execution_summary import JobExecutionSummary
from .job_log import JobLog
from .job_log_collection import JobLogCollection
from .job_log_summary import JobLogSummary
from .job_metric import JobMetric
from .job_metric_collection import JobMetricCollection
from .job_metric_summary import JobMetricSummary
from .job_summary import JobSummary
from .namespace import Namespace
from .namespace_collection import NamespaceCollection
from .namespace_summary import NamespaceSummary
from .parse_connection_details import ParseConnectionDetails
from .pattern import Pattern
from .pattern_collection import PatternCollection
from .pattern_summary import PatternSummary
from .process_recommendation_details import ProcessRecommendationDetails
from .property_definition import PropertyDefinition
from .recommendation_collection import RecommendationCollection
from .recommendation_details import RecommendationDetails
from .rule_attribute import RuleAttribute
from .rule_collection import RuleCollection
from .rule_summary import RuleSummary
from .search_criteria import SearchCriteria
from .search_result import SearchResult
from .search_result_collection import SearchResultCollection
from .search_tag_summary import SearchTagSummary
from .search_term_summary import SearchTermSummary
from .suggest_list_item import SuggestListItem
from .suggest_results import SuggestResults
from .term import Term
from .term_associated_object import TermAssociatedObject
from .term_collection import TermCollection
from .term_relationship import TermRelationship
from .term_relationship_collection import TermRelationshipCollection
from .term_relationship_summary import TermRelationshipSummary
from .term_summary import TermSummary
from .type import Type
from .type_collection import TypeCollection
from .type_custom_property_details import TypeCustomPropertyDetails
from .type_summary import TypeSummary
from .update_attribute_details import UpdateAttributeDetails
from .update_catalog_details import UpdateCatalogDetails
from .update_catalog_private_endpoint_details import UpdateCatalogPrivateEndpointDetails
from .update_connection_details import UpdateConnectionDetails
from .update_custom_property_details import UpdateCustomPropertyDetails
from .update_data_asset_details import UpdateDataAssetDetails
from .update_entity_details import UpdateEntityDetails
from .update_folder_details import UpdateFolderDetails
from .update_glossary_details import UpdateGlossaryDetails
from .update_job_definition_details import UpdateJobDefinitionDetails
from .update_job_details import UpdateJobDetails
from .update_namespace_details import UpdateNamespaceDetails
from .update_pattern_details import UpdatePatternDetails
from .update_term_details import UpdateTermDetails
from .update_term_relationship_details import UpdateTermRelationshipDetails
from .upload_credentials_details import UploadCredentialsDetails
from .validate_connection_details import ValidateConnectionDetails
from .validate_connection_result import ValidateConnectionResult
from .validate_pattern_details import ValidatePatternDetails
from .validate_pattern_result import ValidatePatternResult
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log import WorkRequestLog
from .work_request_resource import WorkRequestResource

# Maps type names to classes for data_catalog services.
data_catalog_type_mapping = {
    "AttachCatalogPrivateEndpointDetails": AttachCatalogPrivateEndpointDetails,
    "Attribute": Attribute,
    "AttributeCollection": AttributeCollection,
    "AttributeSummary": AttributeSummary,
    "AttributeTag": AttributeTag,
    "AttributeTagCollection": AttributeTagCollection,
    "AttributeTagSummary": AttributeTagSummary,
    "BasePermissionsSummary": BasePermissionsSummary,
    "BaseTag": BaseTag,
    "BaseTagSummary": BaseTagSummary,
    "Catalog": Catalog,
    "CatalogPermissionsSummary": CatalogPermissionsSummary,
    "CatalogPrivateEndpoint": CatalogPrivateEndpoint,
    "CatalogPrivateEndpointSummary": CatalogPrivateEndpointSummary,
    "CatalogSummary": CatalogSummary,
    "ChangeCatalogCompartmentDetails": ChangeCatalogCompartmentDetails,
    "ChangeCatalogPrivateEndpointCompartmentDetails": ChangeCatalogPrivateEndpointCompartmentDetails,
    "Connection": Connection,
    "ConnectionAliasSummary": ConnectionAliasSummary,
    "ConnectionCollection": ConnectionCollection,
    "ConnectionSummary": ConnectionSummary,
    "CreateAttributeDetails": CreateAttributeDetails,
    "CreateCatalogDetails": CreateCatalogDetails,
    "CreateCatalogPrivateEndpointDetails": CreateCatalogPrivateEndpointDetails,
    "CreateConnectionDetails": CreateConnectionDetails,
    "CreateCustomPropertyDetails": CreateCustomPropertyDetails,
    "CreateDataAssetDetails": CreateDataAssetDetails,
    "CreateEntityDetails": CreateEntityDetails,
    "CreateFolderDetails": CreateFolderDetails,
    "CreateGlossaryDetails": CreateGlossaryDetails,
    "CreateJobDefinitionDetails": CreateJobDefinitionDetails,
    "CreateJobDetails": CreateJobDetails,
    "CreateJobExecutionDetails": CreateJobExecutionDetails,
    "CreateNamespaceDetails": CreateNamespaceDetails,
    "CreatePatternDetails": CreatePatternDetails,
    "CreateTagDetails": CreateTagDetails,
    "CreateTermDetails": CreateTermDetails,
    "CreateTermRelationshipDetails": CreateTermRelationshipDetails,
    "CustomProperty": CustomProperty,
    "CustomPropertyCollection": CustomPropertyCollection,
    "CustomPropertyGetUsage": CustomPropertyGetUsage,
    "CustomPropertySetUsage": CustomPropertySetUsage,
    "CustomPropertySummary": CustomPropertySummary,
    "CustomPropertyTypeUsage": CustomPropertyTypeUsage,
    "DataAsset": DataAsset,
    "DataAssetCollection": DataAssetCollection,
    "DataAssetPermissionsSummary": DataAssetPermissionsSummary,
    "DataAssetSummary": DataAssetSummary,
    "DataAssetTag": DataAssetTag,
    "DataAssetTagCollection": DataAssetTagCollection,
    "DataAssetTagSummary": DataAssetTagSummary,
    "DataSelectorPatternDetails": DataSelectorPatternDetails,
    "DerivedLogicalEntities": DerivedLogicalEntities,
    "DetachCatalogPrivateEndpointDetails": DetachCatalogPrivateEndpointDetails,
    "Entity": Entity,
    "EntityCollection": EntityCollection,
    "EntitySummary": EntitySummary,
    "EntityTag": EntityTag,
    "EntityTagCollection": EntityTagCollection,
    "EntityTagSummary": EntityTagSummary,
    "FacetedSearchAggregation": FacetedSearchAggregation,
    "FacetedSearchCustomProperty": FacetedSearchCustomProperty,
    "FacetedSearchDateFilterRequest": FacetedSearchDateFilterRequest,
    "FacetedSearchFilterRequest": FacetedSearchFilterRequest,
    "FacetedSearchSortRequest": FacetedSearchSortRequest,
    "FacetedSearchStringFilterRequest": FacetedSearchStringFilterRequest,
    "Folder": Folder,
    "FolderCollection": FolderCollection,
    "FolderSummary": FolderSummary,
    "FolderTag": FolderTag,
    "FolderTagCollection": FolderTagCollection,
    "FolderTagSummary": FolderTagSummary,
    "Glossary": Glossary,
    "GlossaryCollection": GlossaryCollection,
    "GlossaryPermissionsSummary": GlossaryPermissionsSummary,
    "GlossarySummary": GlossarySummary,
    "GlossaryTreeElement": GlossaryTreeElement,
    "ImportConnectionDetails": ImportConnectionDetails,
    "ImportGlossaryDetails": ImportGlossaryDetails,
    "Job": Job,
    "JobCollection": JobCollection,
    "JobDefinition": JobDefinition,
    "JobDefinitionCollection": JobDefinitionCollection,
    "JobDefinitionPermissionsSummary": JobDefinitionPermissionsSummary,
    "JobDefinitionScope": JobDefinitionScope,
    "JobDefinitionSummary": JobDefinitionSummary,
    "JobExecution": JobExecution,
    "JobExecutionCollection": JobExecutionCollection,
    "JobExecutionSummary": JobExecutionSummary,
    "JobLog": JobLog,
    "JobLogCollection": JobLogCollection,
    "JobLogSummary": JobLogSummary,
    "JobMetric": JobMetric,
    "JobMetricCollection": JobMetricCollection,
    "JobMetricSummary": JobMetricSummary,
    "JobSummary": JobSummary,
    "Namespace": Namespace,
    "NamespaceCollection": NamespaceCollection,
    "NamespaceSummary": NamespaceSummary,
    "ParseConnectionDetails": ParseConnectionDetails,
    "Pattern": Pattern,
    "PatternCollection": PatternCollection,
    "PatternSummary": PatternSummary,
    "ProcessRecommendationDetails": ProcessRecommendationDetails,
    "PropertyDefinition": PropertyDefinition,
    "RecommendationCollection": RecommendationCollection,
    "RecommendationDetails": RecommendationDetails,
    "RuleAttribute": RuleAttribute,
    "RuleCollection": RuleCollection,
    "RuleSummary": RuleSummary,
    "SearchCriteria": SearchCriteria,
    "SearchResult": SearchResult,
    "SearchResultCollection": SearchResultCollection,
    "SearchTagSummary": SearchTagSummary,
    "SearchTermSummary": SearchTermSummary,
    "SuggestListItem": SuggestListItem,
    "SuggestResults": SuggestResults,
    "Term": Term,
    "TermAssociatedObject": TermAssociatedObject,
    "TermCollection": TermCollection,
    "TermRelationship": TermRelationship,
    "TermRelationshipCollection": TermRelationshipCollection,
    "TermRelationshipSummary": TermRelationshipSummary,
    "TermSummary": TermSummary,
    "Type": Type,
    "TypeCollection": TypeCollection,
    "TypeCustomPropertyDetails": TypeCustomPropertyDetails,
    "TypeSummary": TypeSummary,
    "UpdateAttributeDetails": UpdateAttributeDetails,
    "UpdateCatalogDetails": UpdateCatalogDetails,
    "UpdateCatalogPrivateEndpointDetails": UpdateCatalogPrivateEndpointDetails,
    "UpdateConnectionDetails": UpdateConnectionDetails,
    "UpdateCustomPropertyDetails": UpdateCustomPropertyDetails,
    "UpdateDataAssetDetails": UpdateDataAssetDetails,
    "UpdateEntityDetails": UpdateEntityDetails,
    "UpdateFolderDetails": UpdateFolderDetails,
    "UpdateGlossaryDetails": UpdateGlossaryDetails,
    "UpdateJobDefinitionDetails": UpdateJobDefinitionDetails,
    "UpdateJobDetails": UpdateJobDetails,
    "UpdateNamespaceDetails": UpdateNamespaceDetails,
    "UpdatePatternDetails": UpdatePatternDetails,
    "UpdateTermDetails": UpdateTermDetails,
    "UpdateTermRelationshipDetails": UpdateTermRelationshipDetails,
    "UploadCredentialsDetails": UploadCredentialsDetails,
    "ValidateConnectionDetails": ValidateConnectionDetails,
    "ValidateConnectionResult": ValidateConnectionResult,
    "ValidatePatternDetails": ValidatePatternDetails,
    "ValidatePatternResult": ValidatePatternResult,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLog": WorkRequestLog,
    "WorkRequestResource": WorkRequestResource
}
