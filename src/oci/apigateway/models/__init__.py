# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .access_log_policy import AccessLogPolicy
from .anonymous_route_authorization_policy import AnonymousRouteAuthorizationPolicy
from .any_of_route_authorization_policy import AnyOfRouteAuthorizationPolicy
from .api_specification import ApiSpecification
from .api_specification_logging_policies import ApiSpecificationLoggingPolicies
from .api_specification_request_policies import ApiSpecificationRequestPolicies
from .api_specification_route import ApiSpecificationRoute
from .api_specification_route_backend import ApiSpecificationRouteBackend
from .api_specification_route_request_policies import ApiSpecificationRouteRequestPolicies
from .authentication_only_route_authorization_policy import AuthenticationOnlyRouteAuthorizationPolicy
from .authentication_policy import AuthenticationPolicy
from .change_deployment_compartment_details import ChangeDeploymentCompartmentDetails
from .change_gateway_compartment_details import ChangeGatewayCompartmentDetails
from .cors_policy import CorsPolicy
from .create_deployment_details import CreateDeploymentDetails
from .create_gateway_details import CreateGatewayDetails
from .custom_authentication_policy import CustomAuthenticationPolicy
from .deployment import Deployment
from .deployment_collection import DeploymentCollection
from .deployment_summary import DeploymentSummary
from .execution_log_policy import ExecutionLogPolicy
from .gateway import Gateway
from .gateway_collection import GatewayCollection
from .gateway_summary import GatewaySummary
from .http_backend import HTTPBackend
from .header_field_specification import HeaderFieldSpecification
from .oracle_function_backend import OracleFunctionBackend
from .rate_limiting_policy import RateLimitingPolicy
from .route_authorization_policy import RouteAuthorizationPolicy
from .stock_response_backend import StockResponseBackend
from .update_deployment_details import UpdateDeploymentDetails
from .update_gateway_details import UpdateGatewayDetails
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
    "ApiSpecification": ApiSpecification,
    "ApiSpecificationLoggingPolicies": ApiSpecificationLoggingPolicies,
    "ApiSpecificationRequestPolicies": ApiSpecificationRequestPolicies,
    "ApiSpecificationRoute": ApiSpecificationRoute,
    "ApiSpecificationRouteBackend": ApiSpecificationRouteBackend,
    "ApiSpecificationRouteRequestPolicies": ApiSpecificationRouteRequestPolicies,
    "AuthenticationOnlyRouteAuthorizationPolicy": AuthenticationOnlyRouteAuthorizationPolicy,
    "AuthenticationPolicy": AuthenticationPolicy,
    "ChangeDeploymentCompartmentDetails": ChangeDeploymentCompartmentDetails,
    "ChangeGatewayCompartmentDetails": ChangeGatewayCompartmentDetails,
    "CorsPolicy": CorsPolicy,
    "CreateDeploymentDetails": CreateDeploymentDetails,
    "CreateGatewayDetails": CreateGatewayDetails,
    "CustomAuthenticationPolicy": CustomAuthenticationPolicy,
    "Deployment": Deployment,
    "DeploymentCollection": DeploymentCollection,
    "DeploymentSummary": DeploymentSummary,
    "ExecutionLogPolicy": ExecutionLogPolicy,
    "Gateway": Gateway,
    "GatewayCollection": GatewayCollection,
    "GatewaySummary": GatewaySummary,
    "HTTPBackend": HTTPBackend,
    "HeaderFieldSpecification": HeaderFieldSpecification,
    "OracleFunctionBackend": OracleFunctionBackend,
    "RateLimitingPolicy": RateLimitingPolicy,
    "RouteAuthorizationPolicy": RouteAuthorizationPolicy,
    "StockResponseBackend": StockResponseBackend,
    "UpdateDeploymentDetails": UpdateDeploymentDetails,
    "UpdateGatewayDetails": UpdateGatewayDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLog": WorkRequestLog,
    "WorkRequestLogCollection": WorkRequestLogCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
