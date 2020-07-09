# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import analytics, announcements_service, apigateway, application_migration, audit, autoscaling, bds, blockchain, budget, cims, container_engine, core, data_catalog, data_flow, data_integration, data_safe, data_science, database, dns, dts, email, events, file_storage, functions, healthchecks, identity, integration, key_management, limits, load_balancer, marketplace, monitoring, mysql, nosql, object_storage, oce, ocvp, oda, ons, os_management, resource_manager, resource_search, secrets, streaming, usage_api, vault, waas, work_requests
from . import auth, config, constants, decorators, exceptions, regions, pagination, retry, fips
from .base_client import BaseClient
from .request import Request
from .response import Response
from .signer import Signer
from .version import __version__  # noqa
from .waiter import wait_until

fips.enable_fips_mode()

__all__ = [
    "BaseClient", "Error", "Request", "Response", "Signer", "config", "constants", "decorators", "exceptions", "regions", "wait_until", "pagination", "auth", "retry", "fips",
    "analytics", "announcements_service", "apigateway", "application_migration", "audit", "autoscaling", "bds", "blockchain", "budget", "cims", "container_engine", "core", "data_catalog", "data_flow", "data_integration", "data_safe", "data_science", "database", "dns", "dts", "email", "events", "file_storage", "functions", "healthchecks", "identity", "integration", "key_management", "limits", "load_balancer", "marketplace", "monitoring", "mysql", "nosql", "object_storage", "oce", "ocvp", "oda", "ons", "os_management", "resource_manager", "resource_search", "secrets", "streaming", "usage_api", "vault", "waas", "work_requests"
]
