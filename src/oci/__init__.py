# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import auth, config, constants, decorators, exceptions, regions, pagination, retry, fips
from .base_client import BaseClient
from .request import Request
from .response import Response
from .signer import Signer
from .version import __version__  # noqa
from .waiter import wait_until
import os

fips.enable_fips_mode()

if "OCI_PYTHON_SDK_NO_SERVICE_IMPORTS" in os.environ:
    pass
else:
    from . import ai_anomaly_detection, ai_language, analytics, announcements_service, apigateway, apm_control_plane, apm_synthetics, apm_traces, application_migration, artifacts, audit, autoscaling, bastion, bds, blockchain, budget, cims, cloud_guard, compute_instance_agent, container_engine, core, data_catalog, data_flow, data_integration, data_safe, data_science, database, database_management, database_migration, devops, dns, dts, email, events, file_storage, functions, generic_artifacts_content, golden_gate, healthchecks, identity, integration, jms, key_management, limits, load_balancer, log_analytics, logging, loggingingestion, loggingsearch, management_agent, management_dashboard, marketplace, monitoring, mysql, network_load_balancer, nosql, object_storage, oce, ocvp, oda, ons, operator_access_control, opsi, optimizer, os_management, resource_manager, resource_search, rover, sch, secrets, service_catalog, streaming, tenant_manager_control_plane, usage_api, vault, vulnerability_scanning, waas, work_requests

    __all__ = [
        "BaseClient", "Error", "Request", "Response", "Signer", "config", "constants", "decorators", "exceptions", "regions", "wait_until", "pagination", "auth", "retry", "fips",
        "ai_anomaly_detection", "ai_language", "analytics", "announcements_service", "apigateway", "apm_control_plane", "apm_synthetics", "apm_traces", "application_migration", "artifacts", "audit", "autoscaling", "bastion", "bds", "blockchain", "budget", "cims", "cloud_guard", "compute_instance_agent", "container_engine", "core", "data_catalog", "data_flow", "data_integration", "data_safe", "data_science", "database", "database_management", "database_migration", "devops", "dns", "dts", "email", "events", "file_storage", "functions", "generic_artifacts_content", "golden_gate", "healthchecks", "identity", "integration", "jms", "key_management", "limits", "load_balancer", "log_analytics", "logging", "loggingingestion", "loggingsearch", "management_agent", "management_dashboard", "marketplace", "monitoring", "mysql", "network_load_balancer", "nosql", "object_storage", "oce", "ocvp", "oda", "ons", "operator_access_control", "opsi", "optimizer", "os_management", "resource_manager", "resource_search", "rover", "sch", "secrets", "service_catalog", "streaming", "tenant_manager_control_plane", "usage_api", "vault", "vulnerability_scanning", "waas", "work_requests"
    ]
