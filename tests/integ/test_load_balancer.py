# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import pytest
import time
from . import util
from .. import test_config_container
from .. import util as top_level_utils


class TestLoadBalancer:
    BACKEND_IP_ADDRESS = "129.213.241.184"
    BACKEND_PORT = 80

    def test_operations(self, load_balancer_client, virtual_network):
        with test_config_container.create_vcr().use_cassette('test_load_balancer_operations.yml'):
            try:
                self.subtest_basic_operations(load_balancer_client, virtual_network)
                self.subtest_health_check_operations(load_balancer_client, virtual_network)
            finally:
                time.sleep(20)
                self.subtest_delete(load_balancer_client, virtual_network)

    @util.log_test
    def subtest_basic_operations(self, load_balancer_client, virtual_network):
        self.create_vcn_subnets_common(virtual_network)

        self.backend_set_name = 'BackSet-{}'.format(top_level_utils.random_number_string())
        backend_set_details = oci.load_balancer.models.BackendSetDetails()
        backend_set_details.policy = 'ROUND_ROBIN'
        backend_set_details.health_checker = oci.load_balancer.models.HealthCheckerDetails()
        backend_set_details.health_checker.protocol = 'HTTP'
        backend_set_details.health_checker.url_path = '/'
        backend_set_details.health_checker.port = 80
        backend_set_details.health_checker.retries = 1
        backend_set_details.health_checker.timeout_in_millis = 100
        backend_set_details.health_checker.interval_in_millis = 1000
        backend_set_details.session_persistence_configuration = oci.load_balancer.models.SessionPersistenceConfigurationDetails()
        backend_set_details.session_persistence_configuration.cookie_name = '*'
        backend_set_details.session_persistence_configuration.disable_fallback = False

        create_load_balancer_details = oci.load_balancer.models.CreateLoadBalancerDetails()
        create_load_balancer_details.compartment_id = util.COMPARTMENT_ID
        create_load_balancer_details.display_name = "My Load Balancer"
        create_load_balancer_details.shape_name = "100Mbps"
        create_load_balancer_details.subnet_ids = [self.subnet_ocid1, self.subnet_ocid2]
        create_load_balancer_details.backend_sets = {self.backend_set_name: backend_set_details}

        try:
            response = load_balancer_client.create_load_balancer(create_load_balancer_details)
        except oci.exceptions.ServiceError as e:
            if e.code == 'LimitExceeded':
                pytest.skip('Skipping tests as load balancer limits have been exceeded')
            else:
                raise
        util.validate_response(response)

        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        response = load_balancer_client.get_work_request(work_request_id)
        self.load_balancer_ocid = response.data.load_balancer_id

        create_backend_details = oci.load_balancer.models.CreateBackendDetails()
        create_backend_details.ip_address = self.BACKEND_IP_ADDRESS
        create_backend_details.port = self.BACKEND_PORT
        create_backend_details.weight = 1
        create_backend_details.backup = False
        create_backend_details.drain = False
        create_backend_details.offline = False

        response = load_balancer_client.create_backend(create_backend_details, self.load_balancer_ocid, self.backend_set_name)
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

    # In this test we use a fake backend so the status we get back at each level of health check
    # is UNKNOWN since we can't check something which doesn't exist
    @util.log_test
    def subtest_health_check_operations(self, load_balancer_client, virtual_network):
        kwargs = {
            'load_balancer_id': self.load_balancer_ocid,
            'backend_set_name': self.backend_set_name,
            'backend_name': '{}:{}'.format(self.BACKEND_IP_ADDRESS, self.BACKEND_PORT)
        }

        backend_health_response = self.call_with_retries_on_not_found(load_balancer_client.get_backend_health, 30, 10, **kwargs)
        assert backend_health_response.data.health_check_results == []
        assert backend_health_response.data.status == 'UNKNOWN'

        kwargs.pop('backend_name')
        backend_set_health_response = self.call_with_retries_on_not_found(load_balancer_client.get_backend_set_health, 30, 10, **kwargs)
        assert backend_set_health_response.data.critical_state_backend_names == []
        assert backend_set_health_response.data.warning_state_backend_names == []
        assert backend_set_health_response.data.unknown_state_backend_names == ['{}:{}'.format(self.BACKEND_IP_ADDRESS, self.BACKEND_PORT)]
        assert backend_set_health_response.data.total_backend_count == 1
        assert backend_set_health_response.data.status == 'UNKNOWN'

        kwargs.pop('backend_set_name')
        load_balancer_health_response = self.call_with_retries_on_not_found(load_balancer_client.get_load_balancer_health, 30, 10, **kwargs)
        assert load_balancer_health_response.data.critical_state_backend_set_names == []
        assert load_balancer_health_response.data.warning_state_backend_set_names == []
        assert load_balancer_health_response.data.unknown_state_backend_set_names == [self.backend_set_name]
        assert load_balancer_health_response.data.total_backend_set_count == 1
        assert load_balancer_health_response.data.status == 'UNKNOWN'

        list_load_balancer_healths_response = load_balancer_client.list_load_balancer_healths(util.COMPARTMENT_ID)
        assert len(list_load_balancer_healths_response.data) >= 1

        found_lb = False
        for item in list_load_balancer_healths_response.data:
            if item.load_balancer_id == self.load_balancer_ocid:
                assert item.status == 'UNKNOWN'
                found_lb = True
                break
        assert found_lb

    @util.log_test
    def subtest_delete(self, load_balancer_client, virtual_network):
        error_count = 0

        if hasattr(self, 'load_balancer_ocid') and self.load_balancer_ocid:
            if hasattr(self, 'backend_set_name') and self.backend_set_name:
                try:
                    load_balancer_client.delete_backend(
                        self.load_balancer_ocid,
                        self.backend_set_name,
                        '{}:{}'.format(self.BACKEND_IP_ADDRESS, self.BACKEND_PORT)
                    )
                except Exception as error:
                    if not hasattr(error, 'status') or error.status != 404:
                        util.print_latest_exception(error)
                        error_count = error_count + 1

                try:
                    load_balancer_client.delete_backend_set(self.load_balancer_ocid, self.backend_set_name)
                except Exception as error:
                    if not hasattr(error, 'status') or error.status != 404:
                        util.print_latest_exception(error)
                        error_count = error_count + 1

            try:
                load_balancer_client.delete_load_balancer(self.load_balancer_ocid)
                test_config_container.do_wait(load_balancer_client, load_balancer_client.get_load_balancer(self.load_balancer_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=300)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'subnet_ocid1'):
            try:
                virtual_network.delete_subnet(self.subnet_ocid1)
                test_config_container.do_wait(virtual_network, virtual_network.get_subnet(self.subnet_ocid1), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'subnet_ocid2'):
            try:
                virtual_network.delete_subnet(self.subnet_ocid2)
                test_config_container.do_wait(virtual_network, virtual_network.get_subnet(self.subnet_ocid2), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'vcn_ocid'):
            try:
                virtual_network.delete_vcn(self.vcn_ocid)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        assert error_count == 0

    def test_path_route_sets(self, load_balancer_client, virtual_network):
        self.load_balancer_ocid = None
        self.backend_set_name = None
        with test_config_container.create_vcr().use_cassette('test_load_balancer_path_route_sets.yml'):
            try:
                self.create_vcn_subnets_common(virtual_network)
                self.subtest_path_route_sets(load_balancer_client)
            finally:
                self.subtest_delete(load_balancer_client, virtual_network)

    @util.log_test
    def subtest_path_route_sets(self, load_balancer_client):
        first_backend_set_name = 'BackSet-{}'.format(top_level_utils.random_number_string())
        first_backend_set_details = oci.load_balancer.models.BackendSetDetails(
            policy='ROUND_ROBIN',
            health_checker=oci.load_balancer.models.HealthCheckerDetails(
                protocol='HTTP',
                url_path='/',
                port=80,
                retries=1,
                timeout_in_millis=100,
                interval_in_millis=1000
            ),
            session_persistence_configuration=oci.load_balancer.models.SessionPersistenceConfigurationDetails(
                cookie_name='*',
                disable_fallback=False
            )
        )

        second_backend_set_name = 'BackSet2-{}'.format(top_level_utils.random_number_string())
        second_backend_set_details = oci.load_balancer.models.BackendSetDetails(
            policy='ROUND_ROBIN',
            health_checker=oci.load_balancer.models.HealthCheckerDetails(
                protocol='HTTP',
                url_path='/superman',
                port=80,
                retries=1,
                timeout_in_millis=100,
                interval_in_millis=1000
            )
        )

        # Test that we can specify a path route set at Load Balancer create time
        response = load_balancer_client.create_load_balancer(
            oci.load_balancer.models.CreateLoadBalancerDetails(
                compartment_id=util.COMPARTMENT_ID,
                display_name='PathRouteSetLB',
                shape_name='100Mbps',
                subnet_ids=[self.subnet_ocid1, self.subnet_ocid2],
                backend_sets={
                    first_backend_set_name: first_backend_set_details,
                    second_backend_set_name: second_backend_set_details
                },
                path_route_sets={
                    'path-route-set-1': oci.load_balancer.models.PathRouteSetDetails(
                        path_routes=[
                            oci.load_balancer.models.PathRoute(
                                backend_set_name=first_backend_set_name,
                                path='/example/1',
                                path_match_type=oci.load_balancer.models.PathMatchType(match_type='PREFIX_MATCH')
                            ),
                            oci.load_balancer.models.PathRoute(
                                backend_set_name=first_backend_set_name,
                                path='/other/path/2',
                                path_match_type=oci.load_balancer.models.PathMatchType(match_type='EXACT_MATCH')
                            )
                        ]
                    )
                },
                listeners={
                    'listener1': oci.load_balancer.models.ListenerDetails(
                        default_backend_set_name=first_backend_set_name,
                        path_route_set_name='path-route-set-1',
                        port=80,
                        protocol='HTTP'
                    )
                }
            )
        )

        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)
        response = load_balancer_client.get_work_request(work_request_id)
        load_balancer_ocid = response.data.load_balancer_id

        # Check that the path route set exists and is associated with the listener
        path_route_sets = load_balancer_client.list_path_route_sets(load_balancer_ocid)
        assert len(path_route_sets.data) == 1
        assert path_route_sets.data[0].name == 'path-route-set-1'
        assert len(path_route_sets.data[0].path_routes) == 2
        found_route_one = False
        found_route_two = False
        for route in path_route_sets.data[0].path_routes:
            assert route.backend_set_name == first_backend_set_name
            if route.path == '/example/1':
                found_route_one = True
                assert route.path_match_type.match_type == 'PREFIX_MATCH'
            elif route.path == '/other/path/2':
                found_route_two = True
                assert route.path_match_type.match_type == 'EXACT_MATCH'

        path_route_set = load_balancer_client.get_path_route_set(load_balancer_ocid, 'path-route-set-1').data
        assert path_route_set == path_route_sets.data[0]

        load_balancer = load_balancer_client.get_load_balancer(load_balancer_ocid).data
        assert len(load_balancer.path_route_sets) == 1
        assert 'path-route-set-1' in load_balancer.path_route_sets
        assert load_balancer.path_route_sets['path-route-set-1'] == path_route_set

        assert load_balancer.listeners['listener1'].path_route_set_name == 'path-route-set-1'

        # Test that we can create a path route set
        response = load_balancer_client.create_path_route_set(
            oci.load_balancer.models.CreatePathRouteSetDetails(
                name='path-route-set-2',
                path_routes=[
                    oci.load_balancer.models.PathRoute(
                        backend_set_name=second_backend_set_name,
                        path='/example3/4',
                        path_match_type=oci.load_balancer.models.PathMatchType(match_type='EXACT_MATCH')
                    ),
                    oci.load_balancer.models.PathRoute(
                        backend_set_name=second_backend_set_name,
                        path='/some/kind/of/path',
                        path_match_type=oci.load_balancer.models.PathMatchType(match_type='EXACT_MATCH')
                    )
                ]
            ),
            load_balancer_ocid
        )
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        path_route_set_two = load_balancer_client.get_path_route_set(load_balancer_ocid, 'path-route-set-2').data
        assert len(path_route_set_two.path_routes) == 2
        found_route_one = False
        found_route_two = False
        for route in path_route_set_two.path_routes:
            assert route.backend_set_name == second_backend_set_name
            assert route.path_match_type.match_type == 'EXACT_MATCH'
            if route.path == '/example3/4':
                found_route_one = True
            elif route.path == '/some/kind/of/path':
                found_route_two = True
        assert found_route_one
        assert found_route_two

        path_route_sets = load_balancer_client.list_path_route_sets(load_balancer_ocid)
        assert len(path_route_sets.data) == 2
        found_path_route_set_one = False
        found_path_route_set_two = False
        for route_set in path_route_sets.data:
            if route_set.name == 'path-route-set-1':
                found_path_route_set_one = True
                assert route_set == path_route_set
            elif route_set.name == 'path-route-set-2':
                found_path_route_set_two = True
                assert route_set == path_route_set_two
        assert found_path_route_set_one
        assert found_path_route_set_two

        load_balancer = load_balancer_client.get_load_balancer(load_balancer_ocid).data
        assert len(load_balancer.path_route_sets) == 2
        assert load_balancer.path_route_sets['path-route-set-1'] == path_route_set
        assert load_balancer.path_route_sets['path-route-set-2'] == path_route_set_two

        # I can update a path route set (totally replaces the path routes)
        response = load_balancer_client.update_path_route_set(
            oci.load_balancer.models.UpdatePathRouteSetDetails(
                path_routes=[
                    oci.load_balancer.models.PathRoute(
                        backend_set_name=second_backend_set_name,
                        path='/some/update',
                        path_match_type=oci.load_balancer.models.PathMatchType(match_type='FORCE_LONGEST_PREFIX_MATCH')
                    )
                ]
            ),
            load_balancer_ocid,
            'path-route-set-2'
        )
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        path_route_set_two = load_balancer_client.get_path_route_set(load_balancer_ocid, 'path-route-set-2').data
        assert len(path_route_set_two.path_routes) == 1
        assert path_route_set_two.path_routes[0].backend_set_name == second_backend_set_name
        assert path_route_set_two.path_routes[0].path == '/some/update'
        assert path_route_set_two.path_routes[0].path_match_type.match_type == 'FORCE_LONGEST_PREFIX_MATCH'

        # I can update the path route set on an existing listener
        response = load_balancer_client.update_listener(
            oci.load_balancer.models.UpdateListenerDetails(
                default_backend_set_name=second_backend_set_name,
                path_route_set_name='path-route-set-2',
                port=80,
                protocol='HTTP'
            ),
            load_balancer_ocid,
            'listener1'
        )
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        load_balancer = load_balancer_client.get_load_balancer(load_balancer_ocid).data
        assert load_balancer.listeners['listener1'].path_route_set_name == 'path-route-set-2'

        # I can create a listener with a path route set
        response = load_balancer_client.create_listener(
            oci.load_balancer.models.CreateListenerDetails(
                name='listener2',
                default_backend_set_name=first_backend_set_name,
                port=8080,
                protocol='HTTP',
                path_route_set_name='path-route-set-1'
            ),
            load_balancer_ocid
        )
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        load_balancer = load_balancer_client.get_load_balancer(load_balancer_ocid).data
        assert load_balancer.listeners['listener2'].path_route_set_name == 'path-route-set-1'

        self._delete_path_route_set_load_balancer_resources(
            load_balancer_client,
            load_balancer_ocid,
            first_backend_set_name,
            second_backend_set_name
        )

    def create_vcn_subnets_common(self, virtual_network):
        # Create a VCN
        vcn_name = util.random_name('python_sdk_test_lb_vcn')
        cidr_block = "10.0.0.0/16"

        create_vcn_details = oci.core.models.CreateVcnDetails()
        create_vcn_details.cidr_block = cidr_block
        create_vcn_details.display_name = vcn_name
        create_vcn_details.compartment_id = util.COMPARTMENT_ID

        result = virtual_network.create_vcn(create_vcn_details)
        util.validate_response(result, expect_etag=True)

        self.vcn_ocid = result.data.id

        test_config_container.do_wait(virtual_network, virtual_network.get_vcn(self.vcn_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        # Create a subnet
        subnet_name = util.random_name('python_sdk_test_lb_subnet')

        subnet_cidr_block1 = "10.0.0.0/24"

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = util.COMPARTMENT_ID
        create_subnet_details.availability_domain = util.availability_domain()
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = self.vcn_ocid
        create_subnet_details.cidr_block = subnet_cidr_block1

        result = virtual_network.create_subnet(create_subnet_details)
        util.validate_response(result, expect_etag=True)

        self.subnet_ocid1 = result.data.id
        test_config_container.do_wait(virtual_network, virtual_network.get_subnet(self.subnet_ocid1), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        # Create a subnet
        subnet_name = util.random_name('python_sdk_test_lb_subnet')
        subnet_cidr_block2 = "10.0.1.0/24"

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = util.COMPARTMENT_ID
        create_subnet_details.availability_domain = util.second_availability_domain()
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = self.vcn_ocid
        create_subnet_details.cidr_block = subnet_cidr_block2

        result = virtual_network.create_subnet(create_subnet_details)
        util.validate_response(result, expect_etag=True)

        self.subnet_ocid2 = result.data.id
        test_config_container.do_wait(virtual_network, virtual_network.get_subnet(self.subnet_ocid2), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

    def call_with_retries_on_not_found(self, function_ref, wait_secs, max_retries, **kwargs):
        tries = 0
        while tries < max_retries:
            try:
                return function_ref(**kwargs)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    raise
                else:
                    tries = tries + 1
                    time.sleep(wait_secs)

    def _delete_path_route_set_load_balancer_resources(self, load_balancer_client, load_balancer_ocid, first_backend_set_name, second_backend_set_name):
        response = load_balancer_client.delete_listener(load_balancer_ocid, 'listener1')
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        response = load_balancer_client.delete_listener(load_balancer_ocid, 'listener2')
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        response = load_balancer_client.delete_path_route_set(load_balancer_ocid, 'path-route-set-1')
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        response = load_balancer_client.delete_path_route_set(load_balancer_ocid, 'path-route-set-2')
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        response = load_balancer_client.delete_backend_set(load_balancer_ocid, first_backend_set_name)
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        response = load_balancer_client.delete_backend_set(load_balancer_ocid, second_backend_set_name)
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        response = load_balancer_client.delete_load_balancer(load_balancer_ocid)
        work_request_id = response.headers['opc-work-request-id']
        test_config_container.do_wait(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)
