# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .access_log_policy import AccessLogPolicy
from .anonymous_route_authorization_policy import AnonymousRouteAuthorizationPolicy
from .any_of_route_authorization_policy import AnyOfRouteAuthorizationPolicy
from .any_of_selection_key import AnyOfSelectionKey
from .api import Api
from .api_collection import ApiCollection
from .api_specification import ApiSpecification
from .api_specification_logging_policies import ApiSpecificationLoggingPolicies
from .api_specification_request_policies import ApiSpecificationRequestPolicies
from .api_specification_route import ApiSpecificationRoute
from .api_specification_route_backend import ApiSpecificationRouteBackend
from .api_specification_route_request_policies import ApiSpecificationRouteRequestPolicies
from .api_specification_route_response_policies import ApiSpecificationRouteResponsePolicies
from .api_summary import ApiSummary
from .api_validation_detail import ApiValidationDetail
from .api_validation_details import ApiValidationDetails
from .api_validation_result import ApiValidationResult
from .api_validations import ApiValidations
from .authentication_only_route_authorization_policy import AuthenticationOnlyRouteAuthorizationPolicy
from .authentication_policy import AuthenticationPolicy
from .authentication_server_policy import AuthenticationServerPolicy
from .body_validation_request_policy import BodyValidationRequestPolicy
from .ca_bundle import CaBundle
from .certificate import Certificate
from .certificate_collection import CertificateCollection
from .certificate_summary import CertificateSummary
from .certificates_ca_bundle import CertificatesCaBundle
from .certificates_certificate_authority import CertificatesCertificateAuthority
from .change_api_compartment_details import ChangeApiCompartmentDetails
from .change_certificate_compartment_details import ChangeCertificateCompartmentDetails
from .change_deployment_compartment_details import ChangeDeploymentCompartmentDetails
from .change_gateway_compartment_details import ChangeGatewayCompartmentDetails
from .change_subscriber_compartment_details import ChangeSubscriberCompartmentDetails
from .change_usage_plan_compartment_details import ChangeUsagePlanCompartmentDetails
from .client import Client
from .client_summary import ClientSummary
from .content_validation import ContentValidation
from .cors_policy import CorsPolicy
from .create_api_details import CreateApiDetails
from .create_certificate_details import CreateCertificateDetails
from .create_deployment_details import CreateDeploymentDetails
from .create_gateway_details import CreateGatewayDetails
from .create_sdk_details import CreateSdkDetails
from .create_subscriber_details import CreateSubscriberDetails
from .create_usage_plan_details import CreateUsagePlanDetails
from .custom_authentication_policy import CustomAuthenticationPolicy
from .deployment import Deployment
from .deployment_collection import DeploymentCollection
from .deployment_summary import DeploymentSummary
from .dynamic_authentication_policy import DynamicAuthenticationPolicy
from .dynamic_routing_backend import DynamicRoutingBackend
from .dynamic_routing_type_routing_backend import DynamicRoutingTypeRoutingBackend
from .dynamic_selection_key import DynamicSelectionKey
from .entitlement import Entitlement
from .entitlement_summary import EntitlementSummary
from .entitlement_target import EntitlementTarget
from .execution_log_policy import ExecutionLogPolicy
from .external_resp_cache import ExternalRespCache
from .filter_header_policy import FilterHeaderPolicy
from .filter_header_policy_item import FilterHeaderPolicyItem
from .filter_query_parameter_policy import FilterQueryParameterPolicy
from .filter_query_parameter_policy_item import FilterQueryParameterPolicyItem
from .fixed_ttl_response_cache_store_policy import FixedTTLResponseCacheStorePolicy
from .gateway import Gateway
from .gateway_collection import GatewayCollection
from .gateway_summary import GatewaySummary
from .http_backend import HTTPBackend
from .header_field_specification import HeaderFieldSpecification
from .header_transformation_policy import HeaderTransformationPolicy
from .header_validation_item import HeaderValidationItem
from .header_validation_request_policy import HeaderValidationRequestPolicy
from .ip_address import IpAddress
from .json_web_key import JsonWebKey
from .json_web_token_claim import JsonWebTokenClaim
from .jwt_authentication_policy import JwtAuthenticationPolicy
from .modify_response_validation_failure_policy import ModifyResponseValidationFailurePolicy
from .mutual_tls_details import MutualTlsDetails
from .no_cache import NoCache
from .no_content_validation import NoContentValidation
from .oracle_function_backend import OracleFunctionBackend
from .pem_encoded_public_key import PemEncodedPublicKey
from .public_key_set import PublicKeySet
from .query_parameter_transformation_policy import QueryParameterTransformationPolicy
from .query_parameter_validation_item import QueryParameterValidationItem
from .query_parameter_validation_request_policy import QueryParameterValidationRequestPolicy
from .quota import Quota
from .rate_limit import RateLimit
from .rate_limiting_policy import RateLimitingPolicy
from .remote_json_web_key_set import RemoteJsonWebKeySet
from .rename_header_policy import RenameHeaderPolicy
from .rename_header_policy_item import RenameHeaderPolicyItem
from .rename_query_parameter_policy import RenameQueryParameterPolicy
from .rename_query_parameter_policy_item import RenameQueryParameterPolicyItem
from .request_parameter_validation import RequestParameterValidation
from .response_cache_details import ResponseCacheDetails
from .response_cache_lookup_policy import ResponseCacheLookupPolicy
from .response_cache_resp_server import ResponseCacheRespServer
from .response_cache_store_policy import ResponseCacheStorePolicy
from .route_authorization_policy import RouteAuthorizationPolicy
from .sdk import Sdk
from .sdk_collection import SdkCollection
from .sdk_language_optional_parameters import SdkLanguageOptionalParameters
from .sdk_language_optional_parameters_allowed_value import SdkLanguageOptionalParametersAllowedValue
from .sdk_language_type_collection import SdkLanguageTypeCollection
from .sdk_language_type_summary import SdkLanguageTypeSummary
from .sdk_language_types import SdkLanguageTypes
from .sdk_summary import SdkSummary
from .selection_source_policy import SelectionSourcePolicy
from .set_header_policy import SetHeaderPolicy
from .set_header_policy_item import SetHeaderPolicyItem
from .set_query_parameter_policy import SetQueryParameterPolicy
from .set_query_parameter_policy_item import SetQueryParameterPolicyItem
from .simple_lookup_policy import SimpleLookupPolicy
from .single_selection_source_policy import SingleSelectionSourcePolicy
from .static_public_key import StaticPublicKey
from .static_public_key_set import StaticPublicKeySet
from .stock_response_backend import StockResponseBackend
from .subscriber import Subscriber
from .subscriber_collection import SubscriberCollection
from .subscriber_summary import SubscriberSummary
from .update_api_details import UpdateApiDetails
from .update_certificate_details import UpdateCertificateDetails
from .update_deployment_details import UpdateDeploymentDetails
from .update_gateway_details import UpdateGatewayDetails
from .update_sdk_details import UpdateSdkDetails
from .update_subscriber_details import UpdateSubscriberDetails
from .update_usage_plan_details import UpdateUsagePlanDetails
from .usage_plan import UsagePlan
from .usage_plan_collection import UsagePlanCollection
from .usage_plan_summary import UsagePlanSummary
from .usage_plans_policy import UsagePlansPolicy
from .validation_failure_policy import ValidationFailurePolicy
from .validation_request_policy import ValidationRequestPolicy
from .wildcard_selection_key import WildcardSelectionKey
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log import WorkRequestLog
from .work_request_log_collection import WorkRequestLogCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for apigateway services.
apigateway_type_mapping = {
    "AccessLogPolicy": AccessLogPolicy,
    "AnonymousRouteAuthorizationPolicy": AnonymousRouteAuthorizationPolicy,
    "AnyOfRouteAuthorizationPolicy": AnyOfRouteAuthorizationPolicy,
    "AnyOfSelectionKey": AnyOfSelectionKey,
    "Api": Api,
    "ApiCollection": ApiCollection,
    "ApiSpecification": ApiSpecification,
    "ApiSpecificationLoggingPolicies": ApiSpecificationLoggingPolicies,
    "ApiSpecificationRequestPolicies": ApiSpecificationRequestPolicies,
    "ApiSpecificationRoute": ApiSpecificationRoute,
    "ApiSpecificationRouteBackend": ApiSpecificationRouteBackend,
    "ApiSpecificationRouteRequestPolicies": ApiSpecificationRouteRequestPolicies,
    "ApiSpecificationRouteResponsePolicies": ApiSpecificationRouteResponsePolicies,
    "ApiSummary": ApiSummary,
    "ApiValidationDetail": ApiValidationDetail,
    "ApiValidationDetails": ApiValidationDetails,
    "ApiValidationResult": ApiValidationResult,
    "ApiValidations": ApiValidations,
    "AuthenticationOnlyRouteAuthorizationPolicy": AuthenticationOnlyRouteAuthorizationPolicy,
    "AuthenticationPolicy": AuthenticationPolicy,
    "AuthenticationServerPolicy": AuthenticationServerPolicy,
    "BodyValidationRequestPolicy": BodyValidationRequestPolicy,
    "CaBundle": CaBundle,
    "Certificate": Certificate,
    "CertificateCollection": CertificateCollection,
    "CertificateSummary": CertificateSummary,
    "CertificatesCaBundle": CertificatesCaBundle,
    "CertificatesCertificateAuthority": CertificatesCertificateAuthority,
    "ChangeApiCompartmentDetails": ChangeApiCompartmentDetails,
    "ChangeCertificateCompartmentDetails": ChangeCertificateCompartmentDetails,
    "ChangeDeploymentCompartmentDetails": ChangeDeploymentCompartmentDetails,
    "ChangeGatewayCompartmentDetails": ChangeGatewayCompartmentDetails,
    "ChangeSubscriberCompartmentDetails": ChangeSubscriberCompartmentDetails,
    "ChangeUsagePlanCompartmentDetails": ChangeUsagePlanCompartmentDetails,
    "Client": Client,
    "ClientSummary": ClientSummary,
    "ContentValidation": ContentValidation,
    "CorsPolicy": CorsPolicy,
    "CreateApiDetails": CreateApiDetails,
    "CreateCertificateDetails": CreateCertificateDetails,
    "CreateDeploymentDetails": CreateDeploymentDetails,
    "CreateGatewayDetails": CreateGatewayDetails,
    "CreateSdkDetails": CreateSdkDetails,
    "CreateSubscriberDetails": CreateSubscriberDetails,
    "CreateUsagePlanDetails": CreateUsagePlanDetails,
    "CustomAuthenticationPolicy": CustomAuthenticationPolicy,
    "Deployment": Deployment,
    "DeploymentCollection": DeploymentCollection,
    "DeploymentSummary": DeploymentSummary,
    "DynamicAuthenticationPolicy": DynamicAuthenticationPolicy,
    "DynamicRoutingBackend": DynamicRoutingBackend,
    "DynamicRoutingTypeRoutingBackend": DynamicRoutingTypeRoutingBackend,
    "DynamicSelectionKey": DynamicSelectionKey,
    "Entitlement": Entitlement,
    "EntitlementSummary": EntitlementSummary,
    "EntitlementTarget": EntitlementTarget,
    "ExecutionLogPolicy": ExecutionLogPolicy,
    "ExternalRespCache": ExternalRespCache,
    "FilterHeaderPolicy": FilterHeaderPolicy,
    "FilterHeaderPolicyItem": FilterHeaderPolicyItem,
    "FilterQueryParameterPolicy": FilterQueryParameterPolicy,
    "FilterQueryParameterPolicyItem": FilterQueryParameterPolicyItem,
    "FixedTTLResponseCacheStorePolicy": FixedTTLResponseCacheStorePolicy,
    "Gateway": Gateway,
    "GatewayCollection": GatewayCollection,
    "GatewaySummary": GatewaySummary,
    "HTTPBackend": HTTPBackend,
    "HeaderFieldSpecification": HeaderFieldSpecification,
    "HeaderTransformationPolicy": HeaderTransformationPolicy,
    "HeaderValidationItem": HeaderValidationItem,
    "HeaderValidationRequestPolicy": HeaderValidationRequestPolicy,
    "IpAddress": IpAddress,
    "JsonWebKey": JsonWebKey,
    "JsonWebTokenClaim": JsonWebTokenClaim,
    "JwtAuthenticationPolicy": JwtAuthenticationPolicy,
    "ModifyResponseValidationFailurePolicy": ModifyResponseValidationFailurePolicy,
    "MutualTlsDetails": MutualTlsDetails,
    "NoCache": NoCache,
    "NoContentValidation": NoContentValidation,
    "OracleFunctionBackend": OracleFunctionBackend,
    "PemEncodedPublicKey": PemEncodedPublicKey,
    "PublicKeySet": PublicKeySet,
    "QueryParameterTransformationPolicy": QueryParameterTransformationPolicy,
    "QueryParameterValidationItem": QueryParameterValidationItem,
    "QueryParameterValidationRequestPolicy": QueryParameterValidationRequestPolicy,
    "Quota": Quota,
    "RateLimit": RateLimit,
    "RateLimitingPolicy": RateLimitingPolicy,
    "RemoteJsonWebKeySet": RemoteJsonWebKeySet,
    "RenameHeaderPolicy": RenameHeaderPolicy,
    "RenameHeaderPolicyItem": RenameHeaderPolicyItem,
    "RenameQueryParameterPolicy": RenameQueryParameterPolicy,
    "RenameQueryParameterPolicyItem": RenameQueryParameterPolicyItem,
    "RequestParameterValidation": RequestParameterValidation,
    "ResponseCacheDetails": ResponseCacheDetails,
    "ResponseCacheLookupPolicy": ResponseCacheLookupPolicy,
    "ResponseCacheRespServer": ResponseCacheRespServer,
    "ResponseCacheStorePolicy": ResponseCacheStorePolicy,
    "RouteAuthorizationPolicy": RouteAuthorizationPolicy,
    "Sdk": Sdk,
    "SdkCollection": SdkCollection,
    "SdkLanguageOptionalParameters": SdkLanguageOptionalParameters,
    "SdkLanguageOptionalParametersAllowedValue": SdkLanguageOptionalParametersAllowedValue,
    "SdkLanguageTypeCollection": SdkLanguageTypeCollection,
    "SdkLanguageTypeSummary": SdkLanguageTypeSummary,
    "SdkLanguageTypes": SdkLanguageTypes,
    "SdkSummary": SdkSummary,
    "SelectionSourcePolicy": SelectionSourcePolicy,
    "SetHeaderPolicy": SetHeaderPolicy,
    "SetHeaderPolicyItem": SetHeaderPolicyItem,
    "SetQueryParameterPolicy": SetQueryParameterPolicy,
    "SetQueryParameterPolicyItem": SetQueryParameterPolicyItem,
    "SimpleLookupPolicy": SimpleLookupPolicy,
    "SingleSelectionSourcePolicy": SingleSelectionSourcePolicy,
    "StaticPublicKey": StaticPublicKey,
    "StaticPublicKeySet": StaticPublicKeySet,
    "StockResponseBackend": StockResponseBackend,
    "Subscriber": Subscriber,
    "SubscriberCollection": SubscriberCollection,
    "SubscriberSummary": SubscriberSummary,
    "UpdateApiDetails": UpdateApiDetails,
    "UpdateCertificateDetails": UpdateCertificateDetails,
    "UpdateDeploymentDetails": UpdateDeploymentDetails,
    "UpdateGatewayDetails": UpdateGatewayDetails,
    "UpdateSdkDetails": UpdateSdkDetails,
    "UpdateSubscriberDetails": UpdateSubscriberDetails,
    "UpdateUsagePlanDetails": UpdateUsagePlanDetails,
    "UsagePlan": UsagePlan,
    "UsagePlanCollection": UsagePlanCollection,
    "UsagePlanSummary": UsagePlanSummary,
    "UsagePlansPolicy": UsagePlansPolicy,
    "ValidationFailurePolicy": ValidationFailurePolicy,
    "ValidationRequestPolicy": ValidationRequestPolicy,
    "WildcardSelectionKey": WildcardSelectionKey,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLog": WorkRequestLog,
    "WorkRequestLogCollection": WorkRequestLogCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
