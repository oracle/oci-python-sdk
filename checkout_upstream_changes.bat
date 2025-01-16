@echo off

set files=src/oci/auth src/oci/circuit_breaker src/oci/core src/oci/database src/oci/database_management src/oci/database_tools src/oci/dns src/oci/identity src/oci/monitoring src/oci/object_storage src/oci/pagination src/oci/queue src/oci/retry src/oci/work_requests src/oci/_vendor src/oci/alloy.py src/oci/base_client.py src/oci/config.py src/oci/constants.py src/oci/decorators.py src/oci/exceptions.py src/oci/fips.py src/oci/regions.py src/oci/regions_definitions.py src/oci/util.py src/oci/version.py src/oci/waiter.py src/oci/__init__.py src/oci/file_storage src/oci/functions src/oci/load_balancer src/oci/network_load_balancer
git checkout upstream/master -- %files%
git status
