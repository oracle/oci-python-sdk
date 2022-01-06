# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import time
import uuid

import circuitbreaker
import pytest
from circuitbreaker import CircuitBreaker, CircuitBreakerMonitor

import oci
from oci import Response
from oci.circuit_breaker import CircuitBreakerStrategy, NoCircuitBreakerStrategy, DEFAULT_CIRCUIT_BREAKER_FAILURE_STATUSES_AND_CODES
from oci.exceptions import TransientServiceError


def test_default_circuit_breaker_configuration():
    default_circuit_breaker = CircuitBreakerStrategy()
    assert default_circuit_breaker.failure_threshold == 10
    assert default_circuit_breaker.recovery_timeout == 30
    assert default_circuit_breaker.failure_statuses_and_codes == DEFAULT_CIRCUIT_BREAKER_FAILURE_STATUSES_AND_CODES
    assert default_circuit_breaker.expected_exception is oci.exceptions.TransientServiceError


def test_transient_error():
    circuit_breaker = CircuitBreakerStrategy()
    assert circuit_breaker.is_transient_error(409, "IncorrectState")
    assert not circuit_breaker.is_transient_error(409, "Conflict")
    assert circuit_breaker.is_transient_error(429, "TooManyRequests")
    assert not circuit_breaker.is_transient_error(501, "NotImplemented")
    assert circuit_breaker.is_transient_error(500, None)


def test_circuit_breaker_with_default_failure_codes():
    circuit_breaker_strategy = CircuitBreakerStrategy(
        failure_threshold=1,
        recovery_timeout=10,
        name='CB1'
    )
    num1 = 1
    num2 = 3
    client = MockClient(TransientServiceError(429, 'NotFound', {}, None), 3, circuit_breaker_strategy)

    # Failed call 1
    with pytest.raises(oci.exceptions.TransientServiceError):
        client.do_call(num1=num1, num2=num2)

    # Failed call 2, Circuit breaker should be OPEN after failure threshold of 1, raises CircuitBreakerError
    with pytest.raises(circuitbreaker.CircuitBreakerError):
        client.do_call(num1=num1, num2=num2)

    assert CircuitBreakerMonitor.get('CB1').state == circuitbreaker.STATE_OPEN

    # After Recovery time Circuit Breaker should be half open
    time.sleep(10)
    assert CircuitBreakerMonitor.get('CB1').state == circuitbreaker.STATE_HALF_OPEN

    # Failed call 3, CB allows regular call, another failure makes Circuit breaker back to OPEN state
    with pytest.raises(TransientServiceError):
        client.do_call(num1=num1, num2=num2)
    assert CircuitBreakerMonitor.get('CB1').state == circuitbreaker.STATE_OPEN

    # After Recovery time Circuit Breaker should be half open state
    time.sleep(10)
    assert CircuitBreakerMonitor.get('CB1').state == circuitbreaker.STATE_HALF_OPEN

    # Successful call in HALF OPEN should state make the status go back to CLOSED
    resp = client.do_call(num1=num1, num2=num2)
    assert resp.status == 'success'
    assert resp.data == str(num1 + num2)
    assert CircuitBreakerMonitor.get('CB1').state == circuitbreaker.STATE_CLOSED


def test_circuit_breaker_with_custom_failure_codes():
    circuit_breaker_strategy = CircuitBreakerStrategy(
        failure_threshold=1,
        recovery_timeout=10,
        name='CB2',
        failure_statuses_and_codes={401: ['Custom']}
    )
    num1 = 2
    num2 = 4
    client = MockClient(TransientServiceError(401, 'Custom', {}, None), 3, circuit_breaker_strategy)

    # Failed call 1
    with pytest.raises(oci.exceptions.TransientServiceError):
        client.do_call(num1=num1, num2=num2)

    # Failed call 2, Circuit breaker should be OPEN after failure threshold of 1, raises CircuitBreakerError
    with pytest.raises(circuitbreaker.CircuitBreakerError):
        client.do_call(num1=num1, num2=num2)
    assert CircuitBreakerMonitor.get('CB2').state == circuitbreaker.STATE_OPEN

    # After Recovery time Circuit Breaker should be half open
    time.sleep(10)
    assert CircuitBreakerMonitor.get('CB2').state == circuitbreaker.STATE_HALF_OPEN

    # Failed call 3, CB allows regular call, another failure makes Circuit breaker back to OPEN state
    with pytest.raises(TransientServiceError):
        client.do_call(num1=num1, num2=num2)
    assert CircuitBreakerMonitor.get('CB2').state == circuitbreaker.STATE_OPEN

    # After Recovery time Circuit Breaker should be half open state
    time.sleep(10)
    assert CircuitBreakerMonitor.get('CB2').state == circuitbreaker.STATE_HALF_OPEN

    # Successful call in HALF OPEN should state make the status go back to CLOSED
    resp = client.do_call(num1=num1, num2=num2)
    assert resp.status == 'success'
    assert resp.data == str(num1 + num2)
    assert CircuitBreakerMonitor.get('CB2').state == circuitbreaker.STATE_CLOSED


def test_circuit_breaker_with_shared_strategy():
    circuit_breaker_strategy = CircuitBreakerStrategy(
        failure_threshold=2,
        recovery_timeout=10,
        name='CB3'
    )
    num1 = 7
    num2 = 3
    client1 = MockClient(TransientServiceError(429, 'NotFound', {}, None), 3, circuit_breaker_strategy)
    client2 = MockClient(TransientServiceError(429, 'NotFound', {}, None), 3, circuit_breaker_strategy)

    print(CircuitBreakerMonitor.get('CB3'))

    # Failed call 1 with client 1
    with pytest.raises(oci.exceptions.TransientServiceError):
        client1.do_call(num1=num1, num2=num2)

    # Failed call 2 with client 2
    with pytest.raises(oci.exceptions.TransientServiceError):
        client2.do_call(num1=num1, num2=num2)

    # CB tripped with shared CB object
    assert CircuitBreakerMonitor.get(circuit_breaker_strategy.name).state == circuitbreaker.STATE_OPEN


def test_no_circuit_breaker_strategy():
    num1 = 7
    num2 = 3
    client = MockClient(TransientServiceError(429, 'NotFound', {}, None), 3, circuit_breaker_strategy=NoCircuitBreakerStrategy())

    # Failed call 1 with client
    with pytest.raises(oci.exceptions.TransientServiceError):
        client.do_call(num1=num1, num2=num2)

    # Failed call 2 with client
    with pytest.raises(oci.exceptions.TransientServiceError):
        client.do_call(num1=num1, num2=num2)

    resp = client.do_call(num1=num1, num2=num2)
    assert resp.status == 'success'
    assert resp.data == str(num1 + num2)


def call_back_func(log):
    print("Inside Callback function")
    print(log)


def test_circuit_breaker_callback():
    num1 = 3
    num2 = 8
    circuit_breaker_strategy = CircuitBreakerStrategy(
        failure_threshold=1,
        recovery_timeout=10
    )
    client = MockClient(TransientServiceError(429, 'NotFound', {}, None), 3,
                        circuit_breaker_strategy=circuit_breaker_strategy, circuit_breaker_callback=call_back_func)
    response = client.retry_strategy.make_retrying_call(client.do_call, num1, num2)
    assert response.data == str(num1 + num2)


# A utility class which can make retrying calls and track how many calls it made
class MockClient(object):
    def __init__(self, exception_to_throw, return_success_on_call_number, circuit_breaker_strategy, circuit_breaker_callback=None):
        self.retry_strategy = oci.retry.DEFAULT_RETRY_STRATEGY
        self.retry_strategy.add_circuit_breaker_callback(circuit_breaker_callback)
        self.exception_to_throw = exception_to_throw
        self.return_success_on_call_number = return_success_on_call_number
        self.current_calls = 0
        self.circuit_breaker_strategy = circuit_breaker_strategy
        if isinstance(self.circuit_breaker_strategy, CircuitBreakerStrategy):
            circuit_breaker_name = str(
                uuid.uuid4()) if self.circuit_breaker_strategy.name is None else self.circuit_breaker_strategy.name
            # Re-use Circuit breaker if sharing a CB object.
            circuit_breaker = CircuitBreakerMonitor.get(circuit_breaker_name)
            if circuit_breaker is None:
                circuit_breaker = CircuitBreaker(
                    failure_threshold=self.circuit_breaker_strategy.failure_threshold,
                    recovery_timeout=self.circuit_breaker_strategy.recovery_timeout,
                    expected_exception=self.circuit_breaker_strategy.expected_exception,
                    name=circuit_breaker_name
                )
            self.do_call = circuit_breaker(self.do_call)

    def reset(self):
        self.current_calls = 0

    def do_call(self, num1, num2):
        self.current_calls += 1

        if self.current_calls >= self.return_success_on_call_number:
            data = str(num1 + num2)
            return Response(status='success', headers={}, data=data, request=None)
        else:
            raise self.exception_to_throw
